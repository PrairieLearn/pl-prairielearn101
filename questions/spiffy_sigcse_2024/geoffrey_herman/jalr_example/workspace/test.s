.data
array:	.word	1	255	1024	f	g

# every register starts holding the address of "array"
#
# this is a cheat so that we don't need to implement addi and lui in
# our machine.

.text
main:   
	lw	$2,  0($20)	# $2 = 1	(0x1)
	lw	$3,  4($20)	# $3 = 255	(0xff)
	lw	$5, 12($20)	# $5 = f	(function address)
	lw	$6, 16($20)	# $6 = g	(function address)

	jalr	$5  		# call function f
	add	$8, $7, $3	

	jalr	$6  		# call function g
	or	$10, $9, $3


f:	add	$7, $2, $2	
	jalr	$ra 		# use jalr as a jr since we don't have that


g:	sub	$9, $8, $2
