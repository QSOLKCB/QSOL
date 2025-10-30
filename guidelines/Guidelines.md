# QSOL Development Guidelines

## Core Philosophy

**Small Is Beautiful. Fast is Holy.**

## Sacred Constraints

Every QSOL module must adhere to:

1. **Build in seconds** - If it takes minutes, it's too complex
2. **Run without bloat** - Minimal memory, minimal dependencies
3. **Honor clarity** - Code as documentation
4. **Stay local** - No unnecessary network calls
5. **Be transparent** - No hidden behavior

## Design Principles

1. **Simplicity as Precision** - Complexity is laziness in disguise
2. **Fast is Holy** - No operation, build, or startup may exceed 1s
3. **No Dependencies Without Purpose** - Every import must justify its weight
4. **Readable ≠ Verbose** - Clear over clever; concise over clunky
5. **Local First, Cloud Optional** - Offline by default
6. **Transparent by Design** - No opaque binaries or configs
7. **Memory is Sacred** - Reuse, recycle, reduce allocations

## Structural Rules

- **File Size Cap:** 100 KB per module (max)
- **Build Time:** ≤ 3 s from clean source on mid-range CPU
- **Startup Latency:** ≤ 1 s
- **Dependencies:** Zero by default; any external import must be justified in README
- **Code Ratio:** 80% logic / 20% scaffolding
- **Docs:** Only `README.md` per module. If the code can't explain itself, it isn't QSOL

## Contributing

Before submitting:
1. Ensure your code meets all Sacred Constraints
2. Add a clear README to your module
3. Keep dependencies to absolute minimum
4. Test build and run times
5. Write clear, self-documenting code

Remember: **The best code is no code. The second best is simple code.**
