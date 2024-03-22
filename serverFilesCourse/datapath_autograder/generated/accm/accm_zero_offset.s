.data
array:
	.word 3735928559
	.word 3735928559
	.word 10
	.word 20

.text
main:
	accm	$11, 0($13)
	accm	$12, 0($14)
