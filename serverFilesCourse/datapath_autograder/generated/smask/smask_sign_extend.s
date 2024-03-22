.data
array:
	.word 3735928559
	.word 3735928559
	.word 10
	.word -20

.text
main:
	smask	$11, $13, -32768
	smask	$12, $14, -4096
