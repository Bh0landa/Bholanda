.data
	msg: .asciiz "Hello World!"
.text
	add $s0, $t1, $t0
	li $v0, 4
	la $a0, msg
	syscall
