# Contributing to QSOL

> **"Small Is Beautiful. Fast is Holy."**

Thank you for your interest in contributing to QSOL! This document defines our sacred constraints and guidelines.

## The Sacred Constraints

QSOL has three inviolable principles that every contribution must honor:

### 1. Size - "Small Is Beautiful"

**Constraints:**
- Individual module source code: **< 1000 lines** of code (excluding tests)
- Module dependencies: **< 5** external libraries (fewer is better, zero is ideal)
- Total module size (source + deps): **< 10 MB** (smaller is always better)
- Documentation must be proportional: don't document complexity, remove it

**Guidelines:**
- If your module exceeds limits, split it into smaller modules
- Challenge every dependency - can you implement it yourself in fewer lines?
- Use standard library features before external dependencies
- Code golf is not the goal - clarity within minimal size is

**Review Criteria:**
- Can the entire module be understood in 30 minutes?
- Is every line of code necessary?
- Are dependencies justified and minimal?

### 2. Speed - "Fast is Holy"

**Constraints:**
- Build time: **< 10 seconds** on modern hardware
- Startup time: **< 100ms** for CLI tools
- Response time: **< 50ms** for interactive operations
- Memory footprint: **< 50 MB** for typical workloads

**Guidelines:**
- Profile before optimizing, but always optimize
- Choose algorithms wisely - O(n) beats O(n²)
- Avoid startup overhead - lazy loading when appropriate
- Measure, don't guess - include benchmarks

**Review Criteria:**
- Does the build complete in seconds?
- Does the tool feel instant in normal use?
- Is memory usage reasonable for the task?

### 3. Transparency - "Clarity Over Complexity"

**Constraints:**
- Code should be readable by programmers with 1-2 years experience
- No magic - avoid metaprogramming unless absolutely necessary
- Function complexity: **< 50 lines** per function (simpler is better)
- Cyclomatic complexity: **< 10** per function

**Guidelines:**
- Write code for humans first, machines second
- Use descriptive names - clarity over brevity
- Avoid clever tricks - prefer obvious solutions
- Comments explain "why", not "what"
- If you need extensive documentation, simplify the code

**Review Criteria:**
- Can an intermediate programmer understand this?
- Is the code self-documenting?
- Are there any "magical" behaviors?

## How to Contribute

### Before You Start

1. **Check existing modules** - Don't duplicate functionality
2. **Verify alignment** - Does your idea fit the QSOL philosophy?
3. **Start small** - Begin with a minimal proof of concept

### Module Checklist

Every QSOL module submission must include:

- [ ] Source code following sacred constraints
- [ ] README.md with:
  - [ ] Clear purpose statement (one sentence)
  - [ ] Installation instructions
  - [ ] Usage examples
  - [ ] Build instructions (if needed)
- [ ] Build script or clear compilation instructions
- [ ] License notice
- [ ] (Optional but encouraged) Tests
- [ ] (Optional) Benchmarks demonstrating speed

### Submission Process

1. **Fork the repository**
2. **Create your module** in `modules/your-module-name/`
3. **Test thoroughly** - verify all constraints are met
4. **Document clearly** - README is mandatory
5. **Submit a Pull Request** with:
   - Description of what the module does
   - Evidence of constraint compliance (size, speed metrics)
   - Why it belongs in QSOL

### Code Style

- **Consistency** - Match the style of existing code
- **Simplicity** - Prefer standard patterns
- **Clarity** - Name things well
- **Brevity** - Remove unnecessary code

Language-specific guidelines are minimal. Follow the community standards for your language, but always prioritize clarity and simplicity.

## What We're Looking For

### Great QSOL Modules:
- Text processing utilities that do one thing perfectly
- File format converters with zero dependencies
- Development tools that build in seconds
- Data transformers that run instantly
- Local-first productivity tools

### Not Suitable for QSOL:
- Large frameworks or platforms
- Modules requiring heavy dependencies
- Cloud-dependent services
- Modules with excessive build times
- Overly complex solutions to simple problems

## Review Process

All contributions are reviewed for:

1. **Philosophical Alignment** - Does it embody QSOL principles?
2. **Constraint Compliance** - Size, speed, and transparency
3. **Code Quality** - Is it well-written and clear?
4. **Documentation** - Is it complete and helpful?
5. **Usefulness** - Does it solve a real problem?

Reviews typically complete within a week. We may request changes to meet constraints.

## Testing Your Contribution

Before submitting, verify:

```bash
# Size check
find modules/your-module/ -name '*.ext' | xargs wc -l
# Should be < 1000 lines

# Build time check
time ./build.sh
# Should complete in < 10 seconds

# Startup time check (for CLI tools)
time your-tool --version
# Should complete in < 100ms

# Memory check
/usr/bin/time -v your-tool test-input
# Check "Maximum resident set size"
```

## Questions?

- Open an issue for discussion
- Propose ideas before implementing large modules
- Ask for feedback early and often

## Recognition

Contributors who embody QSOL principles will be recognized in the module README and repository contributors list.

---

**Remember:** The goal is not to write the smallest code or the fastest code at all costs. The goal is to write code that is small, fast, AND clear. When in doubt, choose clarity.

*"Simplicity is the ultimate sophistication."* - Leonardo da Vinci
