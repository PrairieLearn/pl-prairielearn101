////////////////////////////////////////////////////////////////////////
//
// Module: rom
//
// Author: Jared Smolens
//
// Description:
//  Reads a file named 'memory.dat' for 32-bit binary MIPS instructions.
//  Will read up to 256 instructions.
//
////////////////////////////////////////////////////////////////////////
//
// You shouldn't need to edit this file
// 
////////////////////////////////////////////////////////////////////////

module instruction_memory (data, addr);
   output [31:0]    data;
   input  [29:0]    addr;
   
   //declare size words of width bits for storage
   reg [31:0]       memWords [0:255];  
   reg [31:0]       i;          // for initialization

   assign data = memWords[addr[7:0]];   // output the data in the memory 
   
   // whenever addr changes, the word it points to is put
   // on the data lines
   
   initial
     begin
        // this is the memory initialization routine
        // it happens once on startup...
        // note! this is not synthesizable
           
        // set memory to zero
        for (i = 0 ; i < 256 ; i = i + 1 )
          begin
             memWords[i] = 0;
          end
        
        // read in the program from a file, mem.dat
        $readmemh("memory.text.dat", memWords);
     end
   
endmodule // instruction_memory

module data_mem(data_out, addr, data_in, mem_read, mem_write, clk, reset);
   parameter     // size of data segment
     data_start   = 32'h10000000,
     data_words   = 'h40000, /* 1 M */
     data_length  = data_words * 4;
   
   input         clk, reset;

   // Inputs and ouptuts: Port 1
   output [31:0] data_out;     // Memory read data
   input  [31:0] addr;         // Memory address
   input  [31:0] data_in;      // Memory write data
   input         mem_read;      // Read enable (active high)
   input         mem_write;     // Write enable (active high)

   wire [18:0] index;
   wire [31:0] d_out;
   wire        valid_address;
   // wire [31:0] d_out, internal_data_in;

   // Memory segments
   reg [31:0]    data_seg[0:data_words-1];

   // Verilog implementation stuff
   integer       i;

   always@(reset)
     if (reset == 1'b1)
       begin
          // Initialize memory (prevents x-pessimism problem)
          for(i = 0; i < data_words; i = i + 1)
          data_seg[i] = 32'hdeadbeef;

          // Grab initial memory values
          $readmemh("memory.data.dat", data_seg);
       end

   assign valid_address = (addr >= data_start[31:0]) && (addr < (data_start[31:0] + data_words));
   assign index = addr[21:2];
   assign d_out = data_seg[index];
   assign data_out = d_out & {32{mem_read}};

   wire [31:0] internal_data_in = data_in;
   always @(posedge clk)
   begin
     if ((reset == 1'b0) && (valid_address == 1'b1))
     begin
       if (mem_write == 1'b1)
         data_seg[index] <= internal_data_in;
     end // if ((reset == 1'b0) && (valid_address == 1'b1))
   end // always @ (negedge clk)
   
endmodule // data_mem

