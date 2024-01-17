(defun adicao (num1 num2)
  (+ num1 num2))

(defun subtracao (num1 num2)
  (- num1 num2))

(defun multiplicacao (num1 num2)
  (* num1 num2))

(defun divisao (num1 num2)
  (if (zerop num2)
      (error "Erro: Divisão por zero!")
      (/ num1 num2)))

;; Exemplos de uso:

(write-line "Digite o primeiro número:")
(setf num1 (parse-integer (read-line)))

(write-line "Digite a operação (+, -, *, /):")
(setf operacao (read-line))

(write-line "Digite o segundo número:")
(setf num2 (parse-integer (read-line)))

(cond ((string= operacao "+") (write-line (adicao num1 num2)))
      ((string= operacao "-") (write-line (subtracao num1 num2)))
      ((string= operacao "*") (write-line (multiplicacao num1 num2)))
      ((string= operacao "/") (write-line (divisao num1 num2)))
      (t (write-line "Operação inválida!")))

