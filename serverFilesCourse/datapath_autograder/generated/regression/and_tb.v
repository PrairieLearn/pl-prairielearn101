module test;
    /* Make a regular pulsing clock. */
    reg       clk = 0;
    always #5 clk = !clk;
    integer   i;

    reg       reset = 1, done = 0;

    machine m(clk, reset);

    wire [31:0] PC = { m.PC_reg.q, 2'b00 };
    initial $display("PC values");
    always #10 $display("0x%x", PC);
   
    initial begin
        # 6
            reset = 0;
            m.rf.r[2] = 11259375;
            m.rf.r[3] = 252645135;
            m.rf.r[4] = 4042322160;

        # 640 // ought to be enough for anyone
            done = 1;
    end

    // periodically check for the end of simulation.  When it happens
    // dump the register file contents.
    always @(negedge clk)
    begin
        if (done === 1'b1 || m.inst === 32'h00000000)
        begin
            $display("\nRegisters");
            for (i = 0; i < 32; i = i + 1)
                $display("0x%x", m.rf.r[i]);

            $display("\nMemory");
            for (i = 32'h4000; i < 32'h4004; i = i + 1)
                $display("0x%x", m.data_memory.data_seg[i]);

            $finish;
        end
    end
endmodule // test