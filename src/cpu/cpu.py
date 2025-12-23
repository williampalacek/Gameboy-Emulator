class CPU:
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
        self.F = 0xB0  # Flags: [Z N H C 0 0 0 0]
        
        # 16-bit registers
        self.SP = 0xFFFE  # Stack pointer
        self.PC = 0x0100  # Program counter
        
        self.memory = memory
        
        self.halted = False
        self.ime = False  # Interrupt Master Enable
        self.cycles = 0
        
        
        
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
        """
        Decode and execute an instruction based on its opcode.
        For now, only NOP is implemented.
        """
        if opcode == 0x00:  # NOP - No Operation
            self.cycles = 4
        else:
            raise NotImplementedError(f"Opcode 0x{opcode:02X} not implemented")