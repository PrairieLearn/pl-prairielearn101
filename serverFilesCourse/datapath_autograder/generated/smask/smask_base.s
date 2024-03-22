.data
array:
	.word 3735928559
	.word 3735928559
	.word 10
	.word -20

.text
main:
	smask	$12, $14, 0x0f0f
