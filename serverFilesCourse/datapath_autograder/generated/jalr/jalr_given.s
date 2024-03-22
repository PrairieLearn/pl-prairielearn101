.data
array:
	.word 1
	.word 255
	.word 1024
	.word 4194336
	.word 4194344

.text
main:
	lw	$2, 0($20)
	lw	$3, 4($20)
	lw	$5, 12($20)
	lw	$6, 16($20)
	jalr	$5
	add	$8, $7, $3
	jalr	$6
	or	$10, $9, $3
	add	$7, $2, $2
	jalr	$ra
	sub	$9, $8, $2
