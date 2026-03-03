.data
	msg: .asciiz "Hello World!" #string a ser impressa
.text
	add $s0, $t1, $t0
	li $v0, 4 #imprimir char ou string
	la $a0, msg
	syscall
