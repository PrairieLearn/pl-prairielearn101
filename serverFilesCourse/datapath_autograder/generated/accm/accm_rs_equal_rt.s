.data
array:
	.word 3735928559
	.word 3735928559
	.word 10
	.word 20

.text
main:
	accm	$13, 4($13)
	accm	$14, -4($14)
