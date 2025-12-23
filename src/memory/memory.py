class Memory:
    """
    Basic memory management for the Game Boy.
    For now, this is just a simple 64KB array.
    """
    def __init__(self):
        # Game Boy has 16-bit address space = 64KB
        self.memory = [0] * 0x10000  # 65536 bytes, all initialized to 0
    
    def read(self, address):
        """Read a byte from memory at the given address."""
        return self.memory[address & 0xFFFF]  # Mask to keep address in range
    
    def write(self, address, value):
        """Write a byte to memory at the given address."""
        self.memory[address & 0xFFFF] = value & 0xFF  # Mask to keep value 8-bit