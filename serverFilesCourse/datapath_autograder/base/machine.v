module mips_decode(ALUOp, RegWrite, BEQ, ALUSrc, MemRead, MemWrite, MemToReg, RegDst, 
                   opcode, funct);

   output [2:0] ALUOp;
   output       RegWrite, BEQ, ALUSrc, MemRead, MemWrite, MemToReg, RegDst;
   input  [5:0] opcode, funct;

   wire new_inst = 0; // boolean expression for when it's the new instruction

   // control signals for new instruction
   wire [2:0] new_ALUOp = 0;
   wire new_RegWrite    = 0;
   wire new_BEQ         = 0;
   wire new_ALUSrc      = 0;
   wire new_MemRead     = 0;
   wire new_MemWrite    = 0;
   wire new_MemToReg    = 0;
   wire new_RegDst      = 0;

   wire [2:0] given_ALUOp;
   wire       given_RegWrite, given_BEQ, given_ALUSrc, given_MemRead,
              given_MemWrite, given_MemToReg, given_RegDst;
   given_decode given(given_ALUOp, given_RegWrite, given_BEQ, given_ALUSrc,
                      given_MemRead, given_MemWrite, given_MemToReg, given_RegDst,
                      opcode, funct);
   mux2v #(3) ALUOp_mux(ALUOp, given_ALUOp, new_ALUOp, new_inst);
   mux2v #(1) RegWrite_mux(RegWrite, given_RegWrite, new_RegWrite, new_inst);
   mux2v #(1) BEQ_mux(BEQ, given_BEQ, new_BEQ, new_inst);
   mux2v #(1) ALUSrc_mux(ALUSrc, given_ALUSrc, new_ALUSrc, new_inst);
   mux2v #(1) MemRead_mux(MemRead, given_MemRead, new_MemRead, new_inst);
   mux2v #(1) MemWrite_mux(MemWrite, given_MemWrite, new_MemWrite, new_inst);
   mux2v #(1) MemToReg_mux(MemToReg, given_MemToReg, new_MemToReg, new_inst);
   mux2v #(1) RegDst_mux(RegDst, given_RegDst, new_RegDst, new_inst);
   
endmodule // mips_decode

module machine(clk, reset);
   input        clk, reset;

   wire [31:0]  PC;
   wire [31:2]  next_PC, PC_plus4, PC_target;
   wire [31:0]  inst;
   
   wire [31:0]  imm = {{ 16{inst[15]} }, inst[15:0] };  // sign-extended immediate
   wire [4:0]   rs = inst[25:21];
   wire [4:0]   rt = inst[20:16];
   wire [4:0]   rd = inst[15:11];
   wire [5:0]   opcode = inst[31:26];
   wire [5:0]   funct = inst[5:0];

   wire [4:0]   wr_regnum;
   wire [2:0]   ALUOp;

   wire         RegWrite, BEQ, ALUSrc, MemRead, MemWrite, MemToReg, RegDst;
   wire         PCSrc, zero, negative;
   wire [31:0]  rd1_data, rd2_data, B_data, alu_out_data, load_data, wr_data;


   register #(30, 30'h100000) PC_reg(PC[31:2], next_PC[31:2], clk, /* enable */1'b1, reset);
   assign PC[1:0] = 2'b0;  // bottom bits hard coded to 00
   adder30 next_PC_adder(PC_plus4, PC[31:2], 30'h1);
   adder30 target_PC_adder(PC_target, PC_plus4, imm[29:0]);
   mux2v #(30) branch_mux(next_PC, PC_plus4, PC_target, PCSrc);
   assign PCSrc = BEQ & zero;
      
   instruction_memory imem (inst, PC[31:2]);

   mips_decode decode(ALUOp, RegWrite, BEQ, ALUSrc, MemRead, MemWrite, MemToReg, RegDst, 
                      opcode, funct);
   
   regfile rf (rd1_data, rd2_data,
               rs, rt, wr_regnum, wr_data, 
               RegWrite, clk, reset);

   mux2v #(32) imm_mux(B_data, rd2_data, imm, ALUSrc);
   alu32 alu(alu_out_data, zero, negative, ALUOp, rd1_data, B_data);
   
   data_mem data_memory(load_data, alu_out_data, rd2_data, MemRead, MemWrite, clk, reset);
   
   mux2v #(32) wb_mux(wr_data, alu_out_data, load_data, MemToReg);
   mux2v #(5) rd_mux(wr_regnum, rt, rd, RegDst);
   
endmodule // machine
