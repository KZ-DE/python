section .text
    global _start       ; Wajib deklarasi untuk linker atau ld.

_start:                 ; Memberi info dari titik masuk linker.
    mov    edx, len     ; Deklarasi panjang dari message atau pesan.
    mov    ecx, msg     ; Deklarasi register pesan yang akan di tulis.
    mov    ebx, 1       ; Deklarasi stdout.
    mov    eax, 4       ; Sistem dari sys_write untuk iniliasi perintah, atau biasa disebut nomor panggilan sistem.
    int    0x80         ; Memanggil kernel untuk melakukan perintah diatas.
    mov    eax, 1       ; Sistem dari sys_swrite untuk iniliasi perintah atau biasa disebut nomor panggilan sistem.
    int    0x80         ; Memanggil kernel untuk melakukan perintah diatas.

section .data
msg     db      'bellshade',    0xa     ; Pesan yang akan di print.
len     equ     $ -msg                  ; Membaca panjang dari string 'bellsahde'.