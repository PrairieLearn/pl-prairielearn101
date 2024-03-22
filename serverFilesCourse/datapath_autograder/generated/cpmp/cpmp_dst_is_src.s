.data
array:
	.word 3735928559
	.word 3735928559
	.word 10
	.word 20

.text
main:
	cpmp	$11, $13, $13
	cpmp	$12, $14, $12
