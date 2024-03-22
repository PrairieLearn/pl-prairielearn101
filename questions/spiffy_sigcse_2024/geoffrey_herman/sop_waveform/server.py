import random

#############################################################################
### DISCLAIMER: This code is super janky and is more a proof of concept   ###
### than a desired way of implementing this problem. I'm working from my  ###
### limited knowledge of regex and string editing in Python. Someone with ###
### more knowledge of both could certainly make a more elegant solution   ###
#############################################################################
MAPPINGS = {'out': '!',
	'a': '"',
	'b': '#',
	'c': '$',
	'd': '%',
	'not_a': '&',
	'not_b': "'",
	'not_c': '(',
	'not_d': ')',
	'out_a1': '*',
	'out_a2': '+',
	'out_a3': ',',
	'out_a4': '-'
}

def generate(data):

	# variables to use for expressions
	bools = ['a', 'b', 'c', 'd']

	####################
	### VCD PREAMBLE ###
	####################

	vcd = '''$date
	Tue Jul  4 01:58:44 2023
$end
$version
	Icarus Verilog
$end
$timescale
	1s
$end
$scope module test $end
$var wire 1 ! out $end
$var reg 1 " a $end
$var reg 1 # b $end
$var reg 1 $ c $end
$var reg 1 % d $end
$scope module sop1 $end
$var wire 1 " a $end
$var wire 1 # b $end
$var wire 1 $ c $end
$var wire 1 % d $end
$var wire 1 & not_a $end
$var wire 1 ' not_b $end
$var wire 1 ( not_c $end
$var wire 1 ) not_d $end
$var wire 1 ! out $end
$var wire 1 * out_a1 $end
$var wire 1 + out_a2 $end
$var wire 1 , out_a3 $end
$var wire 1 - out_a4 $end
$upscope $end
$upscope $end
$enddefinitions $end
#0
$dumpvars
'''


	###########################
	### GENERATE RANDOM VCD ###
	###########################
	# Choose random 4-input truth table with 4 rows that equal 1 and construct VCD file

	sop = ''
	num_prod = 4

	# choose 
	products = random.sample(range(2**len(bools)), num_prod + 1)
	products.sort()

	bug = random.choice(products)
	products.remove(bug)
	bugged = random.choice(products)

	prod_bin = ['', '', '', '']
	for x in range(num_prod):
		prod_bin[x] = '{0:04b}'.format(products[x])

	#################################
	### CREATE BOOLEAN EXPRESSION ###
	#################################

	jj = 1
	for x in products:
		prod = ''	# initialize product term for HTML
		num = x 	# copy x to num so we can do math on it
		num_prod -= 1

		### iterate through the Boolean variables to construct expression
		### have to reverse index the bools because we are stripping off the least-significant bits
		for ii in range(len(bools)):
			if num % 2 == 1:
				prod = bools[3-ii] + prod
			else:
				prod = bools[3-ii] + "'" + prod

			num //= 2

		# info to export product term to html
		data['params'][f'prod{jj}'] = prod
		if x == bugged:
			data['params'][f'bug{jj}'] = 'true'
		else:
			data['params'][f'bug{jj}'] = 'false'
		jj += 1

		# concatenate product terms
		if num_prod > 0:
			sop += prod + " + "
		else:
			sop += prod

	#######################
	### CREATE VCD FILE ###
	#######################

	# VCD files produce one line per signal that changes
	ii = 1 # index of current product term

	# Remove the bugged product term and replace with buggy product term
	products.remove(bugged)
	products.append(bug)
	products.sort()

	# Handle first case separately since all signals are new
	if bug == 0 or 0 in products:
		old_vals = {'out': 1,
		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0,
		'not_a': 1,
		'not_b': 1,
		'not_c': 1,
		'not_d': 1,
		'out_a1': 1,
		'out_a2': 0,
		'out_a3': 0,
		'out_a4': 0
		}
		ii = 2
	else:
		old_vals = {'out': 0,
		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0,
		'not_a': 1,
		'not_b': 1,
		'not_c': 1,
		'not_d': 1,
		'out_a1': 0,
		'out_a2': 0,
		'out_a3': 0,
		'out_a4': 0
		}


	for key in old_vals:
		vcd += str(old_vals[key]) + MAPPINGS[key] + '\n'

	vcd += '$end\n#10\n'

	# set up for remaining test cases
	x_bin = [0, 0, 0, 0]
	new_vals = old_vals.copy()

	# Check for which signals change each time stamp
	# Produce output for each changed signal
	for x in range(1, 2**len(bools)):
		x_bin[0] = x % 2
		x_bin[1] = x // 2 % 2
		x_bin[2] = x // 4 % 2
		x_bin[3] = x // 8 % 2

		new_vals['d'] = x_bin[0]
		new_vals['c'] = x_bin[1]
		new_vals['b'] = x_bin[2]
		new_vals['a'] = x_bin[3]

		new_vals['not_d'] = 1-x_bin[0]
		new_vals['not_c'] = 1-x_bin[1]
		new_vals['not_b'] = 1-x_bin[2]
		new_vals['not_a'] = 1-x_bin[3]

		new_vals['out_a1'] = 0
		new_vals['out_a2'] = 0
		new_vals['out_a3'] = 0
		new_vals['out_a4'] = 0
		new_vals['out'] = 0

		if x in products:
			new_vals[f'out_a{ii}'] = 1
			new_vals['out'] = 1
			ii += 1

		for key in old_vals:
			if old_vals[key] != new_vals[key]:
				vcd += str(new_vals[key]) + MAPPINGS[key] + '\n'

		vcd += f'#{(x+1)*10}\n'

		old_vals = new_vals.copy()

	#############################
	### EXPORT WORKSPACE FILE ###
	#############################

	### Comment for top of file so students have the spec in the .v
	data["params"]["_workspace_files"] = [
	{
			"name" : "test.vcd", "contents" : vcd
		}
	]

	#######################################
	### SEND BOOLEAN EXPRESSION TO HTML ###
	#######################################

	data["params"]["expression"] = sop

	#############################
	### SEND FEEDBACK TO HTML ###
	#############################

	feedback = prod_bin[0] + ', '
	feedback += prod_bin[1] + ', '
	feedback += prod_bin[2] + ', or '
	feedback += prod_bin[3]

	data["params"]["feedback"] = feedback

	return data