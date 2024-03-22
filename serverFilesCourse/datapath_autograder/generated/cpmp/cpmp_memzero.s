.data
array:
	.word 3735928559
	.word 3735928559
	.word 0
	.word 0

.text
main:
	cpmp	$11, $13, $12
	cpmp	$15, $14, $12
