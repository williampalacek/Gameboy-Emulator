import sys
sys.path.append('src')

from cpu import CPU
from memory import Memory

def test_cpu_initialization():
    """Test that CPU initializes with correct register values."""
    memory = Memory()
    cpu = CPU(memory)
    
    # Check 8-bit registers match post-boot state
    assert cpu.A == 0x01, f"A should be 0x01, got 0x{cpu.A:02X}"
    assert cpu.F == 0xA0, f"F should be 0xA0, got 0x{cpu.F:02X}"
    assert cpu.B == 0x00, f"B should be 0x00, got 0x{cpu.B:02X}"
    assert cpu.C == 0x13, f"C should be 0x13, got 0x{cpu.C:02X}"
    
    # Check 16-bit registers
    assert cpu.PC == 0x0100, f"PC should start at 0x0100, got 0x{cpu.PC:04X}"
    assert cpu.SP == 0xFFFE, f"SP should start at 0xFFFE, got 0x{cpu.SP:04X}"
    
    # Check state flags
    assert cpu.halted == False
    assert cpu.ime == False
    
    print("✓ CPU initialization test passed!")

def test_flag_operations():
    """Test that flag get/set operations work correctly."""
    memory = Memory()
    cpu = CPU(memory)
    
    # Start with F = 0xA0 = 0b10100000 (Z and H flags set, C clear)
    assert cpu.get_flag('Z') == True, "Z flag should be set initially"
    assert cpu.get_flag('N') == False, "N flag should be clear initially"
    assert cpu.get_flag('H') == True, "H flag should be set initially"
    assert cpu.get_flag('C') == False, "C flag should be clear initially"
    
    # Test setting flags
    cpu.set_flag('C', True)
    assert cpu.get_flag('C') == True, "C flag should be set"
    assert cpu.F == 0xB0, f"F should be 0xB0 (0xA0 with C set), got 0x{cpu.F:02X}"
    
    # Test clearing flags
    cpu.set_flag('Z', False)
    assert cpu.get_flag('Z') == False, "Z flag should be clear"
    
    print("✓ Flag operations test passed!")

def test_register_pairs():
    """Test that 16-bit register pair operations work."""
    memory = Memory()
    cpu = CPU(memory)
    
    # Test setting BC
    cpu.set_bc(0x1234)
    assert cpu.B == 0x12, f"B should be 0x12, got 0x{cpu.B:02X}"
    assert cpu.C == 0x34, f"C should be 0x34, got 0x{cpu.C:02X}"
    assert cpu.get_bc() == 0x1234, f"BC should be 0x1234, got 0x{cpu.get_bc():04X}"
    
    # Test setting HL
    cpu.set_hl(0xABCD)
    assert cpu.H == 0xAB, f"H should be 0xAB, got 0x{cpu.H:02X}"
    assert cpu.L == 0xCD, f"L should be 0xCD, got 0x{cpu.L:02X}"
    assert cpu.get_hl() == 0xABCD, f"HL should be 0xABCD, got 0x{cpu.get_hl():04X}"
    
    print("✓ Register pair operations test passed!")

def test_stack_operations():
    """Test push and pop stack operations."""
    memory = Memory()
    cpu = CPU(memory)
    
    initial_sp = cpu.SP  # Should be 0xFFFE
    
    # Push a value
    cpu.push_stack(0x1234)
    assert cpu.SP == initial_sp - 2, f"SP should decrease by 2, got 0x{cpu.SP:04X}"
    
    # Check memory has correct bytes
    assert memory.read(initial_sp - 1) == 0x12, "High byte should be at SP-1"
    assert memory.read(initial_sp - 2) == 0x34, "Low byte should be at SP-2"
    
    # Pop the value back
    value = cpu.pop_stack()
    assert value == 0x1234, f"Popped value should be 0x1234, got 0x{value:04X}"
    assert cpu.SP == initial_sp, f"SP should return to initial value 0x{initial_sp:04X}"
    
    print("✓ Stack operations test passed!")

def test_nop_instruction():
    """Test that NOP instruction executes correctly."""
    memory = Memory()
    cpu = CPU(memory)
    
    # Write NOP instruction (0x00) at PC
    memory.write(0x0100, 0x00)
    
    initial_pc = cpu.PC
    
    # Execute one instruction
    cycles = cpu.step()
    
    assert cycles == 4, f"NOP should take 4 cycles, got {cycles}"
    assert cpu.PC == initial_pc + 1, f"PC should increment by 1, got 0x{cpu.PC:04X}"
    
    print("✓ NOP instruction test passed!")

if __name__ == "__main__":
    test_cpu_initialization()
    test_flag_operations()
    test_register_pairs()
    test_stack_operations()
    test_nop_instruction()
    print("\n🎉 All CPU tests passed!")