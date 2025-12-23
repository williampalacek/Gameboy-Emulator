# GameBoy Emulator

A Game Boy emulator built from scratch in Python, with incremental feature development across versions.

## Project Goals

- Build a cycle-accurate Game Boy emulator from the ground up
- Understand low-level emulation concepts and hardware architecture
- Incrementally add features: base system → Game Boy Color → debugger UI → enhancements

## Current Status

**Version:** 0.1 (In Development)

- [ ] CPU (Sharp LR35902) core
- [ ] Memory Management Unit
- [ ] Graphics Processing Unit
- [ ] Input handling
- [ ] Timer & Interrupts
- [ ] Audio Processing Unit
- [ ] Game Boy Color support
- [ ] Debugger UI

## Roadmap

### Version 1.0: CPU & Memory Foundation
- Implement all CPU instructions (including CB-prefixed opcodes)
- Basic memory mapping and MMU
- Pass Blargg's cpu_instrs test ROMs

### Version 2.0: Graphics
- PPU implementation with proper timing modes
- Background, window, and sprite rendering
- Tile/map system
- Visual output to screen

### Version 3.0: Playable Games
- Joypad input handling
- Timer implementation
- Full interrupt system
- Playable commercial games

### Version 4.0: Game Boy Color
- Color palette support
- Double-speed CPU mode
- Additional RAM and VRAM banks
- CGB-specific registers

### Version 5.0: Debugger & Tools
- Register and memory viewer
- Breakpoint system
- Step-through execution
- Tile/sprite viewer
- Disassembler

### Future Enhancements
- Audio (APU) implementation
- Save states
- Rewind functionality
- Screenshot/recording capabilities
- Game Genie cheat codes
- Link cable emulation

## Building & Running
```bash
# Instructions coming soon
```

## Testing

The emulator is tested against:
- Blargg's test ROMs
- Mooneye Test Suite
- Commercial game compatibility

## Resources & References

- [Pan Docs](https://gbdev.io/pandocs/) - The definitive Game Boy technical reference
- [Game Boy CPU Manual](http://marc.rawer.de/Gameboy/Docs/GBCPUman.pdf)
- [The Ultimate Game Boy Talk](https://www.youtube.com/watch?v=HyzD8pNlpwI)
- [/r/EmuDev](https://www.reddit.com/r/EmuDev/)

## License

MIT

## Acknowledgments

Built following the excellent resources from the Game Boy development community.