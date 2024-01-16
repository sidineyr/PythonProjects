section .data
    a dd 2        ; Coeficiente a
    b dd -5       ; Coeficiente b
    c dd 2        ; Coeficiente c
    delta dd 0    ; Variável para armazenar o delta
    raiz1 dd 0    ; Primeira raiz
    raiz2 dd 0    ; Segunda raiz
    msg1 db 'As raízes são: ', 0
    msg2 db 'Raiz 1: ', 0
    msg3 db 'Raiz 2: ', 0

section .text
    global _start

_start:
    ; Calcula o delta: delta = b^2 - 4ac
    fld dword [b]
    fild dword [b]
    fmulp st1, st0    ; b^2
    fld dword [a]
    fld dword [c]
    fmulp st1, st0    ; ac
    faddp            ; b^2 + 4ac
    fstp dword [delta]

    ; Verifica o valor de delta
    fld dword [delta]
    fcomip st0, st1   ; Compara delta com zero
    fstsw ax
    sahf
    jl sem_raizes     ; Se delta < 0, não há raízes reais

    ; Calcula as raízes: raiz1 = (-b + sqrt(delta)) / (2a)
    fld dword [b]
    fchs             ; Negativo de b
    fld dword [delta]
    fsqrt            ; sqrt(delta)
    faddp            ; -b + sqrt(delta)
    fld dword [a]
    fild dword 2     ; 2a
    fdivp            ; (-b + sqrt(delta)) / (2a)
    fstp dword [raiz1]

    ; Calcula a segunda raiz: raiz2 = (-b - sqrt(delta)) / (2a)
    fld dword [b]
    fchs             ; Negativo de b
    fld dword [delta]
    fsqrt            ; sqrt(delta)
    fsubp            ; -b - sqrt(delta)
    fld dword [a]
    fild dword 2     ; 2a
    fdivp            ; (-b - sqrt(delta)) / (2a)
    fstp dword [raiz2]

    ; Exibe as raízes
    mov eax, 4
    mov ebx, 1
    mov ecx, msg1
    mov edx, 16
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, msg2
    mov edx, 9
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, [raiz1]
    mov edx, 8
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, msg3
    mov edx, 9
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, [raiz2]
    mov edx, 8
    int 0x80

    ; Sai do programa
    mov eax, 1
    xor ebx, ebx
    int 0x80

sem_raizes:
    ; Exibe mensagem se não há raízes reais
    mov eax, 4
    mov ebx, 1
    mov ecx, sem_raizes_msg
    mov edx, 21
    int 0x80

    ; Sai do programa
    mov eax, 1
    xor ebx, ebx
    int 0x80

section .data
    sem_raizes_msg db 'Não há raízes reais.', 0

