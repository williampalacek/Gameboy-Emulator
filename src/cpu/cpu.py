from .opcodes import Opcodes

class CPU(Opcodes):
    def __init__(self, memory):
        """
        Initialize the Game Boy CPU (Sharp LR35902).
        This is a modified Z80 - similar instruction set but different timing.
        """
        # 8-bit registers
        self.A = 0x01  # Accumulator
        self.B = 0x00
        self.C = 0x13
        self.D = 0x00
        self.E = 0xD8
        self.H = 0x01
        self.L = 0x4D
        self.F = 0xA0  # Flags: [Z N H C 0 0 0 0] = [1 0 1 0 0 0 0 0]
        
        # 16-bit registers
        self.SP = 0xFFFE  # Stack pointer
        self.PC = 0x0100  # Program counter
        
        self.memory = memory
        
        self.halted = False
        self.ime = False  # Interrupt Master Enable
        self.cycles = 0
        
        # Build opcode lookup table
        self.opcode_table = self._build_opcode_table()
        
    
    def _build_opcode_table(self):
        """
        Map opcodes to (handler, cycles).
        Uses dictionary lookup instead of if/elif chain.
        """
        return {
            # Control
            0x00: (self.op_nop, 4),
            
            # 8-bit immediate loads (8 cycles)
            0x06: (self.op_ld_b_n, 8),
            0x0E: (self.op_ld_c_n, 8),
            0x16: (self.op_ld_d_n, 8),
            0x1E: (self.op_ld_e_n, 8),
            0x26: (self.op_ld_h_n, 8),
            0x2E: (self.op_ld_l_n, 8),
            0x3E: (self.op_ld_a_n, 8),
            
            # Register to register (4 cycles)
            0x40: (self.op_ld_b_b, 4), 0x41: (self.op_ld_b_c, 4),
            0x42: (self.op_ld_b_d, 4), 0x43: (self.op_ld_b_e, 4),
            0x44: (self.op_ld_b_h, 4), 0x45: (self.op_ld_b_l, 4),
            0x47: (self.op_ld_b_a, 4),
            
            0x48: (self.op_ld_c_b, 4), 0x49: (self.op_ld_c_c, 4),
            0x4A: (self.op_ld_c_d, 4), 0x4B: (self.op_ld_c_e, 4),
            0x4C: (self.op_ld_c_h, 4), 0x4D: (self.op_ld_c_l, 4),
            0x4F: (self.op_ld_c_a, 4),
            
            0x50: (self.op_ld_d_b, 4), 0x51: (self.op_ld_d_c, 4),
            0x52: (self.op_ld_d_d, 4), 0x53: (self.op_ld_d_e, 4),
            0x54: (self.op_ld_d_h, 4), 0x55: (self.op_ld_d_l, 4),
            0x57: (self.op_ld_d_a, 4),
            
            0x58: (self.op_ld_e_b, 4), 0x59: (self.op_ld_e_c, 4),
            0x5A: (self.op_ld_e_d, 4), 0x5B: (self.op_ld_e_e, 4),
            0x5C: (self.op_ld_e_h, 4), 0x5D: (self.op_ld_e_l, 4),
            0x5F: (self.op_ld_e_a, 4),
            
            0x60: (self.op_ld_h_b, 4), 0x61: (self.op_ld_h_c, 4),
            0x62: (self.op_ld_h_d, 4), 0x63: (self.op_ld_h_e, 4),
            0x64: (self.op_ld_h_h, 4), 0x65: (self.op_ld_h_l, 4),
            0x67: (self.op_ld_h_a, 4),
            
            0x68: (self.op_ld_l_b, 4), 0x69: (self.op_ld_l_c, 4),
            0x6A: (self.op_ld_l_d, 4), 0x6B: (self.op_ld_l_e, 4),
            0x6C: (self.op_ld_l_h, 4), 0x6D: (self.op_ld_l_l, 4),
            0x6F: (self.op_ld_l_a, 4),
            
            0x78: (self.op_ld_a_b, 4), 0x79: (self.op_ld_a_c, 4),
            0x7A: (self.op_ld_a_d, 4), 0x7B: (self.op_ld_a_e, 4),
            0x7C: (self.op_ld_a_h, 4), 0x7D: (self.op_ld_a_l, 4),
            0x7F: (self.op_ld_a_a, 4),
            
            # Memory indirect (8 cycles)
            0x46: (self.op_ld_b_hl, 8), 0x4E: (self.op_ld_c_hl, 8),
            0x56: (self.op_ld_d_hl, 8), 0x5E: (self.op_ld_e_hl, 8),
            0x66: (self.op_ld_h_hl, 8), 0x6E: (self.op_ld_l_hl, 8),
            0x7E: (self.op_ld_a_hl, 8),
            
            0x70: (self.op_ld_hl_b, 8), 0x71: (self.op_ld_hl_c, 8),
            0x72: (self.op_ld_hl_d, 8), 0x73: (self.op_ld_hl_e, 8),
            0x74: (self.op_ld_hl_h, 8), 0x75: (self.op_ld_hl_l, 8),
            0x77: (self.op_ld_hl_a, 8),
            
            0x36: (self.op_ld_hl_n, 12),
        }
    
        
    def get_flag(self, flag):
        """
        Check if a specific flag is set.
        Returns True if set, False if clear.
        """
        flag_bits = {
            'Z': 0x80,  # Zero flag - bit 7
            'N': 0x40,  # Subtract flag - bit 6
            'H': 0x20,  # Half-carry flag - bit 5
            'C': 0x10   # Carry flag - bit 4
        }
        return (self.F & flag_bits[flag]) != 0
    
    def set_flag(self, flag, value):
        """
        Set or clear a specific flag.
        value=True sets the flag, value=False clears it.
        """
        flag_bits = {
            'Z': 0x80,
            'N': 0x40,
            'H': 0x20,
            'C': 0x10
        }
        if value:
            self.F |= flag_bits[flag]  # Set bit with OR
        else:
            self.F &= ~flag_bits[flag]  # Clear bit with AND of inverted mask
            
            
            
    def get_bc(self):
        """Get BC as a 16-bit value (B is high byte, C is low byte)."""
        return (self.B << 8) | self.C
    
    def set_bc(self, value):
        """Set BC from a 16-bit value."""
        self.B = (value >> 8) & 0xFF
        self.C = value & 0xFF
    
    def get_de(self):
        """Get DE as a 16-bit value."""
        return (self.D << 8) | self.E
    
    def set_de(self, value):
        """Set DE from a 16-bit value."""
        self.D = (value >> 8) & 0xFF
        self.E = value & 0xFF
    
    def get_hl(self):
        """Get HL as a 16-bit value."""
        return (self.H << 8) | self.L
    
    def set_hl(self, value):
        """Set HL from a 16-bit value."""
        self.H = (value >> 8) & 0xFF
        self.L = value & 0xFF
    
    def get_af(self):
        """Get AF as a 16-bit value."""
        return (self.A << 8) | self.F
    
    def set_af(self, value):
        """Set AF from a 16-bit value."""
        self.A = (value >> 8) & 0xFF
        self.F = value & 0xF0  # Lower 4 bits of F are always 0
        
        
    
    def fetch_byte(self):
        """
        Fetch one byte from memory at PC and increment PC.
        This is how the CPU reads instructions and operands.
        """
        byte = self.memory.read(self.PC)
        self.PC = (self.PC + 1) & 0xFFFF  # Keep PC in 16-bit range (wraps at 0xFFFF)
        return byte
    
    def fetch_word(self):
        """
        Fetch a 16-bit word (2 bytes) from memory.
        Game Boy is little-endian: low byte first, then high byte.
        """
        low = self.fetch_byte()
        high = self.fetch_byte()
        return (high << 8) | low
    
    
    
    def push_stack(self, value):
        """
        Push a 16-bit value onto the stack.
        Stack grows downward, so SP decreases.
        """
        self.SP = (self.SP - 1) & 0xFFFF
        self.memory.write(self.SP, (value >> 8) & 0xFF)  # High byte first
        self.SP = (self.SP - 1) & 0xFFFF
        self.memory.write(self.SP, value & 0xFF)          # Then low byte
    
    def pop_stack(self):
        """
        Pop a 16-bit value from the stack.
        Reads low byte first (SP points to it), then high byte.
        """
        low = self.memory.read(self.SP)
        self.SP = (self.SP + 1) & 0xFFFF
        high = self.memory.read(self.SP)
        self.SP = (self.SP + 1) & 0xFFFF
        return (high << 8) | low
    
    
    
    def step(self):
        """
        Execute one instruction and return cycle count.
        This is called repeatedly to run the emulator.
        """
        if self.halted:
            return 4  # HALT instruction pauses CPU but still consumes cycles
        
        opcode = self.fetch_byte()
        self.cycles = 0
        self.execute(opcode)
        
        return self.cycles
    
    def execute(self, opcode):
        """Execute opcode using lookup table."""
        if opcode in self.opcode_table:
            handler, cycles = self.opcode_table[opcode]
            handler()
            self.cycles = cycles
        else:
            raise NotImplementedError(f"Opcode 0x{opcode:02X} not implemented")