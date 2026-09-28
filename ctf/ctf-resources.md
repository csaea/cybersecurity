# Capture The Flag — Resources

## Environment
| Resource | Does | Link |
|---|---|---|
| CYBER.ORG Kali VM | Browser-based Kali, no install | [portal.cyber.org](https://portal.cyber.org/) |
| Kali Linux | OS preloaded with CTF tools; best for hard challenges | [kali.org](https://www.kali.org/) |

## Practice Platforms
| Platform | Does | Link |
|---|---|---|
| CyLab Security Academy | CMU's picoCTF successor; 490+ challenges, learning paths, browser webshell | [cylabacademy.org](https://cylabacademy.org/) |
| WarmupCTF | Easy beginner challenges | [warmup.ctfd.io](https://warmup.ctfd.io/challenges) |
| 316CTF | General practice | [play.316ctf.com](https://play.316ctf.com/challenges) |

---

## Cryptography & Encoding
| Tool | Does | Example |
|---|---|---|
| [CyberChef](https://gchq.github.io/CyberChef/) | Chain decoders | `From Base64` → `From Hex` |
| [CYBER.ORG Tools](https://tools.cyber.org/dashboard) | Common decoders in one place | Paste text → pick decoder |
| [HexEd.it](https://hexed.it/) | View/edit raw bytes | Check file header bytes |
| [Binwalk](https://github.com/ReFirmLabs/binwalk) | Find/extract embedded files | `binwalk -e image.png` |
| [Steghide](http://steghide.sourceforge.net/) | Extract data hidden in images/audio | `steghide extract -sf pic.jpg` |

**Tips:** Try Base64, hex, binary first · Shifted text → Caesar/Vigenère · Odd file → `strings`, hex editor, `binwalk`

## Digital Forensics
| Tool | Does | Example |
|---|---|---|
| `file` | Identify true file type | `file mystery` |
| `strings` | Pull readable text | `strings mystery \| grep pico` |
| [ExifTool](https://exiftool.org/) | Read metadata | `exiftool photo.jpg` |
| `ls -la`, `grep` | Inspect files, search text | `grep -r "flag" .` |

**Tips:** Always run `file` first · Check metadata and odd timestamps

## Networking
| Tool | Does | Example |
|---|---|---|
| [Wireshark](https://www.wireshark.org/) | Inspect packet captures | Filter `http`, Follow → TCP Stream |
| `nslookup` | Domain ↔ IP | `nslookup example.com` |
| `whois` | Domain registration info | `whois example.com` |
| [ICANN Lookup](https://lookup.icann.org/en) / [Whois.com](https://www.whois.com/whois/) | Web-based whois | Check registrar, nameservers, creation date |

## Web Exploitation
| Tool | Does | Example |
|---|---|---|
| Browser DevTools (F12) | View source, requests, cookies | Network tab → inspect response |
| [Burp Suite CE](https://portswigger.net/burp) | Intercept and replay requests | Edit a parameter → Repeater → Send |

**Tips:** Inspect cookies/tokens · Test inputs for hidden behavior

## Password Cracking
| Tool | Does | Example |
|---|---|---|
| [hashid](https://github.com/psypanda/hashid) | Identify hash type | `hashid '5f4dcc3b…'` |
| [John the Ripper](http://www.openwall.com/john/) | Crack hashes with wordlists | `john --wordlist=commonpasswords.txt hash.txt` |
| [CVE.org](https://www.cve.org/) | Look up known vulnerabilities | Search `CVE-2021-44228` |

**Tips:** Identify before cracking · Common wordlists first · Strong hashes may be infeasible

## Programming & Scripting
| Resource | Does | Example |
|---|---|---|
| [Python docs](https://docs.python.org/3/library/index.html) | Automate decoding/parsing | `python3 -c "print(chr(112))"` |
| [SQL basics](https://www.w3schools.com/sql/) | Understand queries/injection | `SELECT * FROM users;` |
| [Bash scripting](https://linuxcommand.org/lc3_writing_shell_scripts.php) | Script repetitive commands | `for f in *; do strings $f; done` |

**Tips:** Break problems into steps · Print intermediate output

## OSINT
| Tool | Does | Example |
|---|---|---|
| [Google operators](https://ahrefs.com/blog/google-advanced-search-operators/) | aka Dorking. Refine searches | `site:example.com filetype:pdf` |
| [OSINT Framework](https://osintframework.com/) | Directory of OSINT tools | Browse by data type |

**Tips:** Quote exact phrases · Verify sources

