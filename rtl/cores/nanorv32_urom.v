//****************************************************************************/
//  J2 CPU
//  RTL IMPLEMENTATION, Synchronous Version
//
//  Copyright (C) yyyy  Ronan Barzic - rbarzic@gmail.com
//  Date            :  Wed Feb 24 18:56:12 2016
//
//  This program is free software; you can redistribute it and/or
//  modify it under the terms of the GNU General Public License
//  as published by the Free Software Foundation; either version 2
//  of the License, or (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program; if not, write to the Free Software
//  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,MA 02110-1301,USA.
//
//
//  Filename        :  nanorv32_urom.v
//
//  Description     :  Micro ROM for reset sequence and interrupt entry/exit
//                     The content of this ROM is generated from
//                     common/micro_rom/micro_rom.S
//
//****************************************************************************/



module nanorv32_urom (/*AUTOARG*/
   // Outputs
   dout,
   // Inputs
   addr
   );

`include "nanorv32_parameters.v"

   input [NANORV32_UROM_ADDR_MSB:0] addr;
   output [NANORV32_DATA_MSB:0]     dout;

   /*AUTOINPUT*/
   /*AUTOOUTPUT*/

   /*AUTOREG*/
   // Beginning of automatic regs (for this module's undeclared outputs)
   reg [NANORV32_DATA_MSB:0] dout;
   // End of automatics
   /*AUTOWIRE*/

   // Very stupip async ROM - We let the synthesis tool
   // choose the best implementation
   always @* begin
      case(addr)
      //@begin[micro_rom]
        0: dout<= 32'h00100093;
        1: dout<= 32'h00000013;
        2: dout<= 32'hfe112e23;
        3: dout<= 32'hfe212c23;
        4: dout<= 32'hfe512a23;
        5: dout<= 32'hfe612823;
        6: dout<= 32'hfe712623;
        7: dout<= 32'hfea12423;
        8: dout<= 32'hfeb12223;
        9: dout<= 32'hfec12023;
        10: dout<= 32'hfcd12e23;
        11: dout<= 32'hfce12c23;
        12: dout<= 32'hfcf12a23;
        13: dout<= 32'hfff00093;
        14: dout<= 32'h00000097;
        15: dout<= 32'hfc112823;
        16: dout<= 32'hfd010113;
        17: dout<= 32'h08000067;
        18: dout<= 32'h00300093;
        19: dout<= 32'h00000013;
      //@end[micro_rom]
        default: begin
           dout<= 32'h0000000;
        end

      endcase
   end




endmodule // nanorv32_urom
/*
 Local Variables:
 verilog-library-directories:(
 "."
 )
 End:
 */
