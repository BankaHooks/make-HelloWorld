import struct

# --- ELF Header ---
e_ident = b'\x7fELF\x02\x01\x01\x00' + b'\x00' * 8
e_type = 2            # ET_EXEC
e_machine = 0x3E      # x86-64
e_version = 1
e_entry = 0x400078    # точка входа = base + ehdr_size + phdr_size
e_phoff = 64
e_shoff = 0
e_flags = 0
e_ehsize = 64
e_phentsize = 56
e_phnum = 1
e_shentsize = 0
e_shnum = 0
e_shstrndx = 0

ehdr = e_ident + struct.pack(
    '<HHIQQQIHHHHHH',
    e_type, e_machine, e_version, e_entry,
    e_phoff, e_shoff, e_flags, e_ehsize,
    e_phentsize, e_phnum, e_shentsize, e_shnum, e_shstrndx
)
assert len(ehdr) == 64

# --- Program Header (PT_LOAD) ---
code = (
    b'\xb8\x01\x00\x00\x00'
    b'\xbf\x01\x00\x00\x00'
    b'\x48\x8d\x35\x10\x00\x00\x00'
    b'\xba\x16\x00\x00\x00'
    b'\x0f\x05'
    b'\xb8\x3c\x00\x00\x00'
    b'\x31\xff'
    b'\x0f\x05'
)
msg = 'Привет, мир!\n'.encode('utf-8')
data = code + msg
filesize = 64 + 56 + len(data)

p_type = 1            # PT_LOAD
p_flags = 5           # PF_R | PF_X
p_offset = 0
p_vaddr = 0x400000
p_paddr = 0x400000
p_filesz = filesize
p_memsz = filesize
p_align = 0x1000

phdr = struct.pack(
    '<IIQQQQQQ',
    p_type, p_flags, p_offset,
    p_vaddr, p_paddr, p_filesz, p_memsz, p_align
)
assert len(phdr) == 56

# --- Запись исполняемого файла ---
with open('hello', 'wb') as f:
    f.write(ehdr)
    f.write(phdr)
    f.write(data)
