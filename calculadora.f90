program Calculadora
  implicit none
  real :: num1, num2, resultado
  character(1) :: operacao

  ! Entrada de dados
  write(*,*) 'Digite o primeiro número: '
  read(*,*) num1

  write(*,*) 'Digite a operação (+, -, *, /): '
  read(*,*) operacao

  write(*,*) 'Digite o segundo número: '
  read(*,*) num2

  ! Realiza a operação escolhida
  select case (operacao)
    case ('+')
      resultado = num1 + num2
    case ('-')
      resultado = num1 - num2
    case ('*')
      resultado = num1 * num2
    case ('/')
      if (num2 /= 0.0) then
        resultado = num1 / num2
      else
        write(*,*) 'Erro: Divisão por zero!'
        stop
      end if
    case default
      write(*,*) 'Operação inválida!'
      stop
  end select

  ! Exibe o resultado
  write(*,*) 'Resultado: ', resultado

end program Calculadora

