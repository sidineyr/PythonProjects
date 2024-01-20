import Foundation

func realizarOperacao(_ operacao: String, entre num1: Double, e num2: Double) -> Double? {
    switch operacao {
    case "+":
        return num1 + num2
    case "-":
        return num1 - num2
    case "*":
        return num1 * num2
    case "/":
        if num2 != 0 {
            return num1 / num2
        } else {
            print("Erro: Divisão por zero!")
            return nil
        }
    default:
        print("Operação inválida!")
        return nil
    }
}

// Solicitação de entrada do usuário
print("Digite o primeiro número:")
if let num1 = Double(readLine() ?? "") {
    print("Digite a operação (+, -, *, /):")
    if let operacao = readLine(), "+-*/".contains(operacao), operacao.count == 1 {
        print("Digite o segundo número:")
        if let num2 = Double(readLine() ?? "") {
            if let resultado = realizarOperacao(operacao, entre: num1, e: num2) {
                print("Resultado: \(resultado)")
            }
        } else {
            print("Número inválido!")
        }
    } else {
        print("Operação inválida!")
    }
} else {
    print("Número inválido!")
}

