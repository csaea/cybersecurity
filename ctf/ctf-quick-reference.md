This Quick Reference is based on CyLab Security Academy's General Skills in CTFs.

**Navigation**
| Command | Does | Example |
|---|---|---|
| `ls` / `ls -la` | List files; `-la` shows hidden files and permissions | `ls -la ~/challenge` |
| `cd` | Enter dir, go up (`..`), root (`/`), home (`~`) | `cd ../drop-in` |
| `pwd` | Show current location | `pwd` → `/home/ctf-player` |
| **Tab** | Autocomplete; press twice to list options | `cd Add` + Tab → `cd Addadshashanammu/` |

**Files**
| Command | Does | Example |
|---|---|---|
| `cat` | Print a file | `cat flag.txt` |
| `nano` | Edit (Ctrl+O save, Ctrl+X exit) | `nano notes.txt` |
| `wget` | Download a file | `wget https://example.com/flag` |
| `unzip` | Extract an archive | `unzip files.zip` |

**Running programs**
| Command | Does | Example |
|---|---|---|
| `chmod +x` | Grant execute permission | `chmod +x warm` |
| `./` | Run a program in the current folder | `./warm` |
| `python3` | Run a Python script | `python3 ende.py -d flag.txt.en` |
| `-h` | Show help/options | `./warm -h` |

**Searching**
| Command | Does | Example |
|---|---|---|
| `grep` | Find text in a file | `grep "picoCTF" file` |
| `grep -r` | Search every file below here | `grep -r "picoCTF" .` |
| `find` | Locate files by name | `find . -name "*flag*"` |
| `strings` | Extract readable text from a binary | `strings program` |
| `\|` | Pipe output into another command | `strings program \| grep pico` |

**Remote connections**
| Command | Does | Example |
|---|---|---|
| `nc` | Connect to a remote service | `nc jupiter.challenges.picoctf.org 14291` |
| `ssh` | Log into a remote shell | `ssh ctf-player@venus.picoctf.net -p 52218` |

**Number conversions** (`python3 -c "print(...)"`)
| Expression | Does | Example → Result |
|---|---|---|
| `0x..` | Hex → decimal | `0x3D` → `61` |
| `bin()` | Decimal → binary | `bin(42)` → `0b101010` |
| `int(x, 2)` | Binary → decimal | `int('101010', 2)` → `42` |
| `chr()` / `ord()` | Decimal ↔ ASCII | `chr(112)` → `p`, `ord('p')` → `112` |