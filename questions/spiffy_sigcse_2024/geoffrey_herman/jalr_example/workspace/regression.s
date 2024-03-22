.data
array:	.word	22	42

# every register except $0 starts holding the address of "array"
#
# this is a cheat so that we don't need to implement addi and lui in
# our pipelined machine.

.text
main:
	lw	$2, 0($28)	# $2 = 22	(0x16)
	lw	$3, 4($28)	# $3 = 42	(0x2a)
	add	$4, $2, $3	# $4 = 64	(0x40)
	sub	$5, $2, $4	# $5 = -42	(0xffffffd6)
	and	$6, $3, $5	# $6 = 2	(0x2)
	or	$7, $2, $3	# $7 = 62	(0x3e)
	slt	$8, $2, $5	# $8 = 0	(0x0)
	slt	$9, $6, $3	# $9 = 1	(0x1)

	beq	$8, $9, skip	# not taken
	sw	$3, 0($28)
	beq	$10, $11, skip	# taken
	sw	$2, 4($28)

skip:
	lw	$10, 0($28)	# $10 = 42	(0x2a)
	lw	$11, 4($28)	# $11 = 42	(0x2a)
