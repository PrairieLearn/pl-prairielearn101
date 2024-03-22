.data
array:
	.word 3735928559
	.word 3735928559
	.word -1
	.word -10234

.text
main:
	cpmp	$11, $13, $12
	cpmp	$15, $14, $12
