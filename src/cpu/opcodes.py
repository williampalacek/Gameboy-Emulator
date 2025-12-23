"""
Opcode implementations for the Game Boy CPU.
Each method implements one specific instruction.
"""

class Opcodes:
    """
    Mixin class containing all CPU instruction implementations.
    Inherits CPU's registers, memory, and helper methods.
    """
    
    # === Control Flow ===
    
    def op_nop(self):
        """0x00 - NOP: No Operation"""
        pass
    
    # === 8-bit Immediate Loads ===
    
    def op_ld_b_n(self):
        """0x06 - LD B, n"""
        self.B = self.fetch_byte()
    
    def op_ld_c_n(self):
        """0x0E - LD C, n"""
        self.C = self.fetch_byte()
    
    def op_ld_d_n(self):
        """0x16 - LD D, n"""
        self.D = self.fetch_byte()
    
    def op_ld_e_n(self):
        """0x1E - LD E, n"""
        self.E = self.fetch_byte()
    
    def op_ld_h_n(self):
        """0x26 - LD H, n"""
        self.H = self.fetch_byte()
    
    def op_ld_l_n(self):
        """0x2E - LD L, n"""
        self.L = self.fetch_byte()
    
    def op_ld_a_n(self):
        """0x3E - LD A, n"""
        self.A = self.fetch_byte()
    
    # === Register to Register Loads ===
    
    # Loading into B
    def op_ld_b_b(self):
        """0x40 - LD B, B"""
        self.B = self.B
    
    def op_ld_b_c(self):
        """0x41 - LD B, C"""
        self.B = self.C
    
    def op_ld_b_d(self):
        """0x42 - LD B, D"""
        self.B = self.D
    
    def op_ld_b_e(self):
        """0x43 - LD B, E"""
        self.B = self.E
    
    def op_ld_b_h(self):
        """0x44 - LD B, H"""
        self.B = self.H
    
    def op_ld_b_l(self):
        """0x45 - LD B, L"""
        self.B = self.L
    
    def op_ld_b_a(self):
        """0x47 - LD B, A"""
        self.B = self.A
    
    # Loading into C
    def op_ld_c_b(self):
        """0x48 - LD C, B"""
        self.C = self.B
    
    def op_ld_c_c(self):
        """0x49 - LD C, C"""
        self.C = self.C
    
    def op_ld_c_d(self):
        """0x4A - LD C, D"""
        self.C = self.D
    
    def op_ld_c_e(self):
        """0x4B - LD C, E"""
        self.C = self.E
    
    def op_ld_c_h(self):
        """0x4C - LD C, H"""
        self.C = self.H
    
    def op_ld_c_l(self):
        """0x4D - LD C, L"""
        self.C = self.L
    
    def op_ld_c_a(self):
        """0x4F - LD C, A"""
        self.C = self.A
    
    # Loading into D
    def op_ld_d_b(self):
        """0x50 - LD D, B"""
        self.D = self.B
    
    def op_ld_d_c(self):
        """0x51 - LD D, C"""
        self.D = self.C
    
    def op_ld_d_d(self):
        """0x52 - LD D, D"""
        self.D = self.D
    
    def op_ld_d_e(self):
        """0x53 - LD D, E"""
        self.D = self.E
    
    def op_ld_d_h(self):
        """0x54 - LD D, H"""
        self.D = self.H
    
    def op_ld_d_l(self):
        """0x55 - LD D, L"""
        self.D = self.L
    
    def op_ld_d_a(self):
        """0x57 - LD D, A"""
        self.D = self.A
    
    # Loading into E
    def op_ld_e_b(self):
        """0x58 - LD E, B"""
        self.E = self.B
    
    def op_ld_e_c(self):
        """0x59 - LD E, C"""
        self.E = self.C
    
    def op_ld_e_d(self):
        """0x5A - LD E, D"""
        self.E = self.D
    
    def op_ld_e_e(self):
        """0x5B - LD E, E"""
        self.E = self.E
    
    def op_ld_e_h(self):
        """0x5C - LD E, H"""
        self.E = self.H
    
    def op_ld_e_l(self):
        """0x5D - LD E, L"""
        self.E = self.L
    
    def op_ld_e_a(self):
        """0x5F - LD E, A"""
        self.E = self.A
    
    # Loading into H
    def op_ld_h_b(self):
        """0x60 - LD H, B"""
        self.H = self.B
    
    def op_ld_h_c(self):
        """0x61 - LD H, C"""
        self.H = self.C
    
    def op_ld_h_d(self):
        """0x62 - LD H, D"""
        self.H = self.D
    
    def op_ld_h_e(self):
        """0x63 - LD H, E"""
        self.H = self.E
    
    def op_ld_h_h(self):
        """0x64 - LD H, H"""
        self.H = self.H
    
    def op_ld_h_l(self):
        """0x65 - LD H, L"""
        self.H = self.L
    
    def op_ld_h_a(self):
        """0x67 - LD H, A"""
        self.H = self.A
    
    # Loading into L
    def op_ld_l_b(self):
        """0x68 - LD L, B"""
        self.L = self.B
    
    def op_ld_l_c(self):
        """0x69 - LD L, C"""
        self.L = self.C
    
    def op_ld_l_d(self):
        """0x6A - LD L, D"""
        self.L = self.D
    
    def op_ld_l_e(self):
        """0x6B - LD L, E"""
        self.L = self.E
    
    def op_ld_l_h(self):
        """0x6C - LD L, H"""
        self.L = self.H
    
    def op_ld_l_l(self):
        """0x6D - LD L, L"""
        self.L = self.L
    
    def op_ld_l_a(self):
        """0x6F - LD L, A"""
        self.L = self.A
    
    # Loading into A
    def op_ld_a_b(self):
        """0x78 - LD A, B"""
        self.A = self.B
    
    def op_ld_a_c(self):
        """0x79 - LD A, C"""
        self.A = self.C
    
    def op_ld_a_d(self):
        """0x7A - LD A, D"""
        self.A = self.D
    
    def op_ld_a_e(self):
        """0x7B - LD A, E"""
        self.A = self.E
    
    def op_ld_a_h(self):
        """0x7C - LD A, H"""
        self.A = self.H
    
    def op_ld_a_l(self):
        """0x7D - LD A, L"""
        self.A = self.L
    
    def op_ld_a_a(self):
        """0x7F - LD A, A"""
        self.A = self.A
    
    # === Memory Indirect Loads ===
    
    # Reading from (HL)
    def op_ld_b_hl(self):
        """0x46 - LD B, (HL)"""
        address = self.get_hl()
        self.B = self.memory.read(address)
    
    def op_ld_c_hl(self):
        """0x4E - LD C, (HL)"""
        address = self.get_hl()
        self.C = self.memory.read(address)
    
    def op_ld_d_hl(self):
        """0x56 - LD D, (HL)"""
        address = self.get_hl()
        self.D = self.memory.read(address)
    
    def op_ld_e_hl(self):
        """0x5E - LD E, (HL)"""
        address = self.get_hl()
        self.E = self.memory.read(address)
    
    def op_ld_h_hl(self):
        """0x66 - LD H, (HL)"""
        address = self.get_hl()
        self.H = self.memory.read(address)
    
    def op_ld_l_hl(self):
        """0x6E - LD L, (HL)"""
        address = self.get_hl()
        self.L = self.memory.read(address)
    
    def op_ld_a_hl(self):
        """0x7E - LD A, (HL)"""
        address = self.get_hl()
        self.A = self.memory.read(address)
    
    # Writing to (HL)
    def op_ld_hl_b(self):
        """0x70 - LD (HL), B"""
        address = self.get_hl()
        self.memory.write(address, self.B)
    
    def op_ld_hl_c(self):
        """0x71 - LD (HL), C"""
        address = self.get_hl()
        self.memory.write(address, self.C)
    
    def op_ld_hl_d(self):
        """0x72 - LD (HL), D"""
        address = self.get_hl()
        self.memory.write(address, self.D)
    
    def op_ld_hl_e(self):
        """0x73 - LD (HL), E"""
        address = self.get_hl()
        self.memory.write(address, self.E)
    
    def op_ld_hl_h(self):
        """0x74 - LD (HL), H"""
        address = self.get_hl()
        self.memory.write(address, self.H)
    
    def op_ld_hl_l(self):
        """0x75 - LD (HL), L"""
        address = self.get_hl()
        self.memory.write(address, self.L)
    
    def op_ld_hl_a(self):
        """0x77 - LD (HL), A"""
        address = self.get_hl()
        self.memory.write(address, self.A)
    
    def op_ld_hl_n(self):
        """0x36 - LD (HL), n: Write immediate byte to memory at HL"""
        address = self.get_hl()
        value = self.fetch_byte()
        self.memory.write(address, value)