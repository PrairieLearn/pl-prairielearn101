.data
array:
	.word 3735928559
	.word 3735928559
	.word 10
	.word -20

.text
main:
	accm	$11, 4($13)
	accm	$12, -4($14)
