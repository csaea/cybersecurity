This Quick Reference is based on CyLab Security Academy easy to medium challenges.
Refer to [CTF-Resources](ctf-resources) for online tools.

**Navigation**
| Command | Does | Example |
|---|---|---|
| `ls` / `ls -la` | List files; `-la` shows hidden files and permissions | `ls -la ~/challenge` |
| `cd` | Enter dir, go up (`..`), root (`/`), home (`~`) | `cd /home/kali/Documents` |
| `pwd` | Show current location | `pwd` → `/home/kali/Downloads` |
| **Tab** | Autocomplete; press twice to list options | `cd Add` + Tab → `cd Addadshashanammu/` |
| **↑ / ↓** | Scroll through previous commands to rerun or edit | ↑ → recalls `nc jupiter.challenges.picoctf.org 14291` |

**Files**
| Command | Does | Example |
|---|---|---|
| `wget` | Download a file | `wget https://example.com/flag` |
| `cat` | Print a file in Terminal | `cat flag.txt` |
| `file` | Identify a file's real type, regardless of extension | `file mystery` → `mystery: PNG image data` |
| `unzip` | Extract an archive | `unzip files.zip` |
| `nano` | Edit text (Ctrl+O save, Ctrl+X exit) | `nano calc.py` |

**Running programs**
| Command | Does | Example |
|---|---|---|
| `chmod +x` | Grant execute permission for a binary | `chmod +x myExecutable` |
| `./` | Run a program in the current folder | `./myExecutable` |
| `python3` | Run a Python script (with or without options) | `python3 ende.py` |
| `-h` | Show help/options | `./warm -h`, `./calc.py -vO` |

**Searching**
| Command | Does | Example |
|---|---|---|
| `grep` | Find specific text in a file | `grep "London" file` |
| `grep -r` | -r Recursive searches every file in every directory below current | `grep -r "picoCTF" .` |
| `find` | Locate files by name | `find . -name "*flag*"` |
| `strings` | Extract readable text from a binary | `strings program` |
| `\|` | Pipe takes the output of one command and plugs it into another command | `strings program \| grep pico` |

**Remote connections**
| Command | Does | Example |
|---|---|---|
| `nc` | Connect to a remote service | `nc jupiter.challenges.picoctf.org 14291` |
| `ssh` | Log into a remote shell through a specific port | `ssh ctf-player@venus.picoctf.net -p 52218` |

**Number conversions** (`python3 -c "print(...)"`)

Computers store everything as numbers -- including text. CTF challenges often hide flags as hex, binary, or decimal values that must be converted back to readable characters. `python3 -c "print(...)"` runs one line of Python directly in Terminal as a quick calculator, e.g. `python3 -c "print(chr(112))"` prints `p`.

| Expression | Does | Example → Result |
|---|---|---|
| `0x..` | Hex → decimal | `0x3D` → `61` |
| `bin()` | Decimal → binary | `bin(42)` → `0b101010` |
| `int(x, 2)` | Binary → decimal | `int('101010', 2)` → `42` |
| `chr()` / `ord()` | Decimal ↔ ASCII | `chr(112)` → `p`, `ord('p')` → `112` |