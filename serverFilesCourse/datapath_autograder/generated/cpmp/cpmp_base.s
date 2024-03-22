.data
array:
	.word 3735928559
	.word 3735928559
	.word 10
	.word 20

.text
main:
	cpmp	$11, $13, $12
	cpmp	$14, $14, $12
