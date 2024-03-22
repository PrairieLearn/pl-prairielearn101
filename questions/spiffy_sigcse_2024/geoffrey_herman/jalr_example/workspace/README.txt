Suggestion of how to solve this problem.

 1. Read the prompt and figure out how you think test.s should behave.
 
 2. design the circuit on paper
 
 3. make a copy of the original 'machine.v', so you can later 
    diff your modified version with it, if you end up breaking anything.  
    You have the Reset button on the workspace in the worst-case scenario.
 
 4. run:
            make regression
            make > regress
 
    to create a file called 'regress'. The regression tests will help you 
    make sure that you didn't break the original functionality of the datapath.
 
 5. modify 'machine.v' to implement the changes you drew on paper. Don't modify 
    any other files as your copy of those files will be replaced by our copies of them.
 
 6. run:
            make test
            make
 
    to run your Verilog against the test input that has your instruction. If the 
    results are not what you expected them to be from step 1, then we suggest 
    firing up the vcd viewer (recommend just clicking to open (i.e., don't right-click 
    and choose waveform viewer) as there are too many signals for the waveform 
    viewer to handle) to trace down your errors, especially if you are getting X's or 
    Z's in register values.  Start by looking at the values going into the register 
    file and trace them backward until you find the first spot where they go bad. It 
    can be useful to compare your modified code with your original code using

           diff machine.v orig_machine.v
 
    (where 'orig_machine.v' is whatever you called the copy you made earlier)
 
 7. when your test input is working, run:
 
            make regression
            make > regress.new
            diff regress.new regress
 
    like before, this will run the regression test, but in addition compare
    your new results to what they should be.  Fix any bugs.
 
 8. if you want to write your own test cases, edit 'custom.s' and then run:
            make custom
            make
 
 9. Celebrate!

We've provided the following files:

        prompt.txt              (a description of what instruction
                                 to implement)

        machine.v               (a single-cycle machine for you to
                                 modify to add a new instruction)

        mips_defines.v          (Verilog components; you shouldn't
        modules.v                edit these, as you won't submit
        mux_lib.v                them.)
        rom.v

        machine_tb.v            (a standard testbench)

        Makefile

        test.s                  (a test that includes the instruction
        test.data.dat            that you are supposed to implement.)
        test.text.dat

        regression.s            (a regression test consisting of the
        regression.data.dat      instructions that the machine already
        regression.text.dat      implements to help you know if you
                                 broke the existing functionality.)

        custom.s                (a file for you to write your own test
        spim-datapath            case, if you wish, and program to
                                 assemble and run said test case.)

        MIPSGreenSheet.pdf      (for your reference)
