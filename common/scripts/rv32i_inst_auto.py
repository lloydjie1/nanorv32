#-I inst : beq of type SB-type
# -I-        SB-type  match found beq 0 0x18 3

spec['nanorv32']['rv32i']['beq']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b0
    }
}
#-I inst : bne of type SB-type
# -I-        SB-type  match found bne 1 0x18 3

spec['nanorv32']['rv32i']['bne']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b1
    }
}
#-I inst : blt of type SB-type
# -I-        SB-type  match found blt 4 0x18 3

spec['nanorv32']['rv32i']['blt']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b100
    }
}
#-I inst : bge of type SB-type
# -I-        SB-type  match found bge 5 0x18 3

spec['nanorv32']['rv32i']['bge']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b101
    }
}
#-I inst : bltu of type SB-type
# -I-        SB-type  match found bltu 6 0x18 3

spec['nanorv32']['rv32i']['bltu']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b110
    }
}
#-I inst : bgeu of type SB-type
# -I-        SB-type  match found bgeu 7 0x18 3

spec['nanorv32']['rv32i']['bgeu']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b111
    }
}
#-I inst : jalr of type I-type
# -I-        I-type  match found jalr 0 0x19 3

spec['nanorv32']['rv32i']['jalr']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b1100111,
        'func3'   : 0b0
    }
}
#-I inst : jal of type UJ-type
# -I-        UJ-type  match found jal 0x1b 3

spec['nanorv32']['rv32i']['jal']['desc'] = {
    'inst_type' : 'UJ-type',
    'decode' : {
        'opcode1' : 0b1101111
    }
}
#-I inst : lui of type U-type
# -I-        U-type  match found lui 0x0D 3

spec['nanorv32']['rv32i']['lui']['desc'] = {
    'inst_type' : 'U-type',
    'decode' : {
        'opcode1' : 0b110111
    }
}
#-I inst : auipc of type U-type
# -I-        U-type  match found auipc 0x05 3

spec['nanorv32']['rv32i']['auipc']['desc'] = {
    'inst_type' : 'U-type',
    'decode' : {
        'opcode1' : 0b10111
    }
}
#-I inst : addi of type I-type
# -I-        I-type  match found addi 0 0x04 3

spec['nanorv32']['rv32i']['addi']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b0
    }
}
#-I inst : slli of type AS-type
# -I-        AS-type  match found slli 0 1 0x04 3

spec['nanorv32']['rv32i']['slli']['desc'] = {
    'inst_type' : 'AS-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b1,
        'func7'   : 0b0
    }
}
#-I inst : slti of type AS-type
# -I-        I-type  match found slti 2 0x04 3

spec['nanorv32']['rv32i']['slti']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b10
    }
}
#-I inst : sltiu of type I-type
# -I-        I-type  match found sltiu 3 0x04 3

spec['nanorv32']['rv32i']['sltiu']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b11
    }
}
#-I inst : xori of type I-type
# -I-        I-type  match found xori 4 0x04 3

spec['nanorv32']['rv32i']['xori']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b100
    }
}
#-I inst : srli of type AS-type
# -I-        AS-type  match found srli 0 5 0x04 3

spec['nanorv32']['rv32i']['srli']['desc'] = {
    'inst_type' : 'AS-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b101,
        'func7'   : 0b0
    }
}
#-I inst : srai of type AS-type
# -I-        AS-type  match found srai 16 5 0x04 3

spec['nanorv32']['rv32i']['srai']['desc'] = {
    'inst_type' : 'AS-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b101,
        'func7'   : 0b10000
    }
}
#-I inst : ori of type I-type
# -I-        I-type  match found ori 6 0x04 3

spec['nanorv32']['rv32i']['ori']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b110
    }
}
#-I inst : andi of type I-type
# -I-        I-type  match found andi 7 0x04 3

spec['nanorv32']['rv32i']['andi']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b111
    }
}
#-I inst : add of type R-type
# -I-       R-type match found add 0 0 0x0C 3 

spec['nanorv32']['rv32i']['add']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b0,
        'func7'   : 0b0
    }
}
#-I inst : sub of type R-type
# -I-       R-type match found sub 32 0 0x0C 3 

spec['nanorv32']['rv32i']['sub']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b0,
        'func7'   : 0b100000
    }
}
#-I inst : sll of type R-type
# -I-       R-type match found sll 0 1 0x0C 3 

spec['nanorv32']['rv32i']['sll']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b1,
        'func7'   : 0b0
    }
}
#-I inst : slt of type R-type
# -I-       R-type match found slt 0 2 0x0C 3 

spec['nanorv32']['rv32i']['slt']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b10,
        'func7'   : 0b0
    }
}
#-I inst : sltu of type R-type
# -I-       R-type match found sltu 0 3 0x0C 3 

spec['nanorv32']['rv32i']['sltu']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b11,
        'func7'   : 0b0
    }
}
#-I inst : xor of type R-type
# -I-       R-type match found xor 0 4 0x0C 3 

spec['nanorv32']['rv32i']['xor']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b100,
        'func7'   : 0b0
    }
}
#-I inst : srl of type R-type
# -I-       R-type match found srl 0 5 0x0C 3 

spec['nanorv32']['rv32i']['srl']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b101,
        'func7'   : 0b0
    }
}
#-I inst : sra of type R-type
# -I-       R-type match found sra 32 5 0x0C 3 

spec['nanorv32']['rv32i']['sra']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b101,
        'func7'   : 0b100000
    }
}
#-I inst : or of type R-type
# -I-       R-type match found or 0 6 0x0C 3 

spec['nanorv32']['rv32i']['or']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b110,
        'func7'   : 0b0
    }
}
#-I inst : and of type R-type
# -I-       R-type match found and 0 7 0x0C 3 

spec['nanorv32']['rv32i']['and']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b111,
        'func7'   : 0b0
    }
}
#-I inst : lb of type I-type
# -I-        I-type  match found lb 0 0x00 3

spec['nanorv32']['rv32i']['lb']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b0
    }
}
#-I inst : lw of type I-type
# -I-        I-type  match found lw 2 0x00 3

spec['nanorv32']['rv32i']['lw']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b10
    }
}
#-I inst : ld of type I-type
# -I-        I-type  match found ld 3 0x00 3

spec['nanorv32']['rv32i']['ld']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b11
    }
}
#-I inst : lbu of type I-type
# -I-        I-type  match found lbu 4 0x00 3

spec['nanorv32']['rv32i']['lbu']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b100
    }
}
#-I inst : lhu of type I-type
# -I-        I-type  match found lhu 5 0x00 3

spec['nanorv32']['rv32i']['lhu']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b101
    }
}
#-I inst : lwu of type I-type
# -I-        I-type  match found lwu 6 0x00 3

spec['nanorv32']['rv32i']['lwu']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b110
    }
}
#-I inst : sb of type S-type
# -I-        S-type  match found sb 0 0x08 3

spec['nanorv32']['rv32i']['sb']['desc'] = {
    'inst_type' : 'S-type',
    'decode' : {
        'opcode1' : 0b100011,
        'func3'   : 0b0
    }
}
#-I inst : sh of type S-type
# -I-        S-type  match found sh 1 0x08 3

spec['nanorv32']['rv32i']['sh']['desc'] = {
    'inst_type' : 'S-type',
    'decode' : {
        'opcode1' : 0b100011,
        'func3'   : 0b1
    }
}
#-I inst : sw of type S-type
# -I-        S-type  match found sw 2 0x08 3

spec['nanorv32']['rv32i']['sw']['desc'] = {
    'inst_type' : 'S-type',
    'decode' : {
        'opcode1' : 0b100011,
        'func3'   : 0b10
    }
}
#-I inst : sd of type S-type
# -I-        S-type  match found sd 3 0x08 3

spec['nanorv32']['rv32i']['sd']['desc'] = {
    'inst_type' : 'S-type',
    'decode' : {
        'opcode1' : 0b100011,
        'func3'   : 0b11
    }
}
#-I inst : fence of type F-type
#-I inst : fence.i of type F-type
#-I inst : scall of type SYS-type
#-I inst : sbreak of type SYS-type
{}
None
