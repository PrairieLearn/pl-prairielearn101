all: machine
.PHONY: all machine clean no_deps_or_beqs beqs_but_no_deps deps_but_no_beqs pipeline_test

# Verilog simulations sometimes enter infinite loops, and piping the simulation
# through grep (below) causes it to be block-buffered, meaning nothing gets
# printed out to the screen, confusing people. This is to force line-buffering;
# script should be available everywhere but it uses different parameters on
# Linux and OS X, making it simpler to use stdbuf on Linux instead
ifneq ($(shell command -v stdbuf;),)
    UNBUFFER = stdbuf -oL
else ifneq ($(shell command -v script;),)
    UNBUFFER = script -q /dev/null
endif

# dumping register values causes spurious VCD warnings to be printed during execution,
# hence the use of grep to filter them up. However, the presence of 'VCD warning' in a
# command freaked a bunch of people out last time, so I'm echoing a fake command instead
# of the actual one to prevent any confusion
machine: machine_exe 
ifeq ($(wildcard memory.text.dat),)
	$(error You need to set up a test case (regression, test, or custom))
else
	@echo ./$<
	@$(UNBUFFER) ./$< | grep -v 'VCD warning'
endif

machine_exe: mips_defines.v modules.v mux_lib.v rom.v machine.v machine_tb.v 
	iverilog -o $@ -Wall $^

clean:
	rm -f machine_exe m.vcd


test: 
	rm -f memory.text.dat memory.data.dat
	ln -s test.text.dat memory.text.dat
	ln -s test.data.dat memory.data.dat

regression: 
	rm -f memory.text.dat memory.data.dat
	ln -s regression.text.dat memory.text.dat
	ln -s regression.data.dat memory.data.dat

custom: custom.text.dat custom.data.dat
	rm -f memory.text.dat memory.data.dat
	ln -s custom.text.dat memory.text.dat
	ln -s custom.data.dat memory.data.dat

custom.text.dat custom.data.dat: custom.s
	./spim-datapath -vasm custom -file custom.s
