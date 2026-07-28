# hello – pure machine code x86-64 ELF

> No assembler. No compiler. No libc. Just bytes.

A tiny (~170 byte) Linux executable that prints `Hello, world!` and exits. Every single byte of the ELF header and the machine instructions was placed by hand – the only "tool" used is Python to pack the structs.

## Quick start

```bash
python3 make_hello.py
chmod +x hello
./hello
