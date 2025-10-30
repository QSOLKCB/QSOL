# 🚀 QSOL v1.0.0 — *Small Is Beautiful. Fast Is Holy.*

**Release Type:** Foundational  
**Tag:** `v1.0.0`  
**Codename:** *Bootstrap Rebellion*  
**Author:** EmergentMonk (Trent Slade)  
**Philosophy:** "Every byte should earn its keep."

---

## 🧬 The Doctrine

QSOL is the anti-bloat micro-framework — a return to code that breathes.

It borrows from [tinyapps.org](https://tinyapps.org), the hacker ethos of the '90s, and the MEMESTACKS philosophy.

No frameworks wrapped around frameworks. No 500 MB build trees. No lies about "simplicity."

Just lean, local-first tools that compile in seconds and *move like lightning*.

---

## 🛠️ Core Additions

**Four working exemplars of the QSOL creed:**

* **Line Counter** — 60 LOC (C/Python), pure stdlib.
* **Web Server** — 122 LOC, 55 ms startup.
* **File Converter** — 202 LOC, handles 10k rows/sec.
* **Task Runner** — 150 LOC, no DSL, no config — just functions.

Every file is under 100 KB. Every module builds in under 3 seconds.

Zero dependencies. Zero excuses.

---

## 📜 Documentation

* **`MEMESTACKS_PHILOSOPHY.md`** — Three sacred laws: *Small Is Beautiful, Fast Is Holy, Clarity Over Complexity.*
* **`QSOL_SPEC.md`** — The doctrine itself: structure, creed, performance vows.
* **`CONSTRAINTS_VALIDATION.md`** — Proof of compliance; all metrics pass.
* **`QUICKSTART.md`** — Spin up a working tool in < 60 seconds.

Markdown? Tolerated only because it fits inside 100 KB.

---

## ⚙️ Metrics of Purity

| Constraint   | Limit    | Achieved   | Margin        |
| ------------ | -------- | ---------- | ------------- |
| File Size    | < 100 KB | 5.6 KB max | 94% under     |
| Build Time   | < 10 s   | 0.33 s     | 97% faster    |
| Startup Time | < 100 ms | 25-55 ms   | 45-75% faster |
| Dependencies | None     | 0          | 100% stdlib   |

---

## 🔒 Patch Note

Codex flagged a minor issue:

`--no-index` flag didn't suppress directory listing.

Fix incoming: override `list_directory()` to send 403 Forbidden.

QSOL doesn't serve what it doesn't mean to.

---

## 🧠 Next

* **QSOL-TinyOS:** micro-runtime for embedded execution.
* **QSOL-Signal:** zero-latency messaging layer.
* **FUZZ-2.0 Spec Integration:** audio-visual minimalism engine.

---

## 🔥 Declaration

> "We are done feeding bloated gods.  
> We build lean. We build local. We build fast.  
> Small is beautiful. Fast is holy. QSOL is free."

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/QSOLKCB/QSOL.git
cd QSOL

# Try a template in 30 seconds
cd modules/example
python3 linecount.py README.md

# Start a web server instantly
cd ../webserver
python3 serve.py
```

See [QUICKSTART.md](QUICKSTART.md) for detailed examples.

---

## 🤝 Contributing

We welcome contributions that align with the QSOL philosophy. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting.

Remember: **The best code is no code. The second best is simple code.**

---

## 📄 License

QSOL is open-source software licensed under [MIT License](LICENSE).

---

## 🙏 Acknowledgments

QSOL draws inspiration from:
- [tinyapps.org](https://tinyapps.org) — Celebrating small, focused software
- The Unix Philosophy — Do one thing and do it well
- The Suckless movement — Simplicity and clarity
- Plan 9 — Clean, minimal design

---

<div align="center">

**QSOL v1.0.0**

*"Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away."*  
— Antoine de Saint-Exupéry

[![Release](https://img.shields.io/badge/release-v1.0.0-blue.svg)](https://github.com/QSOLKCB/QSOL/releases/tag/v1.0.0)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Philosophy](https://img.shields.io/badge/philosophy-MEMESTACKS-purple.svg)](MEMESTACKS_PHILOSOPHY.md)

**Small Is Beautiful. Fast Is Holy.**

</div>
