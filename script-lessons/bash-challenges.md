# Bash/Linux Scripting Challenges 

The following challenges will test not only knowledge of Bash, but will also test your research skills. Look up unfamiliar commands, or solutions to unfamliar problems, online. There is always lots of documentation and solutions to similar problems elsewhere. You just have to know how to look! You can also look up info about a command with the `man` (manual) command. 

> **IMPORTANT**: Run these challenges in a virtual machine!

## Table of Contents
- [System Challenges](#System-Challenges)
- [Attack Simulation Challenges](#Attack-Simulation-Challenges)

---

## System Challenges 

### Challenge 1.1 - Tree to File

**Objectives**:  
- Create an executable script that outputs the `tree` structure of a directory (and its subdirectories) into a new text file. 
- Display a message when the script is complete
- Automatically open the new file.

**Commands/Concepts**: `tree`, `echo`, `>`, `open`

---

### Challenge 1.2 - Backup Script  

**Objectives**:  
- Create a script that copies all contents from one directory to a new, backup directory. 
- List all the files in the backup directory in the terminal. 
- Print a message that the backup is complete, along with the date.

**Commands/Concepts**: `cp`, `mkdir`, `ls`, `echo`, `date`, `-r`, `*`

---

### Challenge 1.3 - Sort and Save

**Objectives**:  
- Setup: In the CLI, create a text file with a list of random words. Each word should be on a new line. 
- Create a script that sorts the contents of the text file alphabetically and saves the result to a new file.
- Print a message indicating that the sorting is complete.

**Commands/Concepts**: `/n`, `touch`, `sort`, `echo`, `>`  

---

### Challenge 1.4 - Rename Files

**Objectives**:  
- Create a script that renames all `.txt` files in a directory by adding a prefix (e.g., "backup_", or "october_") to each file's name.
- Display a message with the name of each renamed file.

**Commands/Concepts**: `mv`, `for`, `echo`, `basename`, `find`

---

### Challenge 1.5 - Directory Cleaner

**Objectives**:  
- Write a script that deletes all files older than 30 days in a specified directory.
- Add a safety check to ask for confirmation before deletion occurs.
- Print the number of files deleted.

**Commands/Concepts**: `find`, `rm`, `-mtime`, `-exec`, `echo`, `read`

---

### Challenge 1.6 - Disk Space Checker

**Objectives**:  
- Write a script that checks the available disk space on the system.
- Print a warning message if the available space is below a certain threshold (e.g., 5 GB).
- Print the current disk usage to the terminal.

**Commands/Concepts**: `df`, `grep`, `awk`, `echo`, `if`

---
---
---
---
---
---
---

## Attack Simulation Challenges

### Challenge 2.1 - CPU Resource Flood

**Objectives**: Use resource exhaustion to simulate:
1. A DoS attack
2. A countermeasure

**Steps**:
1. In one terminal window, run `top` and take note of the total tasks running.
2. In a second terminal, create a script that iterates over a `dd` command 1000 times to overload the system.
3. Run the script.
4. Monitor CPU usage with `top` or `htop` to observe the resource consumption. *(Warning! Your system may crash.)*
5. Write a countermeasure script that limits the number of processes that can run.
6. Try running the first script again and see if your second script is successful. 

**Commands/Concepts**: `dd`, `top` or `htop`, `ulimit`.

---

### Challenge 2.2 - File Permissions

**Objectives**: Demonstrate how malware might alter file permissions to gain unauthorized access.

**Part I**:  
- Create an executable file using `touch`.
- Modify the file permissions using `chmod` to make it executable by others.
- Simulate an attack where a script is placed inside a shared directory and is executed without proper authorization.

**Part II**:  
- Write a countermeasure script to restore secure permissions to all files in a directory.

**Commands/Concepts**: `chmod`, `touch`, `ls`, `chmod 777`, `find`.

---

### Challenge 2.3 - Malware Executing System Commands (Privilege Escalation)

**Objectives**: Learn how attackers use privilege escalation through malicious scripts.

**Part I**:  
- Create a script that executes a system command (like `ls` or `cat`) but is disguised as an innocuous file.
- Use `chmod` to make the file executable and simulate the attack.

**Part II**:  
- Write a detection script that identifies and alerts the user to newly created executable files in sensitive directories.

**Commands/Concepts**: `chmod`, `ls`, `cat`, `ps`, `find`.

---

### Challenge 2.4 - The Hidden Alias

**Objective**: Learn how attackers can hide malicious commands in aliases or environment variables.

**Steps**:
- Create an alias that runs a harmful command when you type a common command (e.g., `ls`).
- Use `echo` to define the alias in the `.bashrc` file.
- Test the alias by typing the command (e.g., `ls`) to see the malicious behavior.
- Write a script that lists all current aliases and looks for suspicious ones.

**Commands/Concepts**: `alias`, `echo`, `cat`, `grep`.

---

### Challenge 2.5 - Propagation

**Objective**: Propagate via USB drives.

**Steps**:
- Write a simple script that copies itself to a USB drive and automatically runs when the USB is inserted.
- Use `touch` and `cp` to simulate the process of copying malicious files to the USB.
- Create a script to detect if a device is connected and if there are new executable files on the USB.

**Commands/Concepts**: `cp`, `ls`, `touch`, `chmod`, `find`.

---

### Challenge 2.6 - Modify System Files

**Objective**: Show how an attacker might inject malicious code into critical system files.

**Steps**:
- Use `echo` and `cat` to append a command to a critical file (e.g., `/etc/hosts` or `/etc/passwd`).
- Simulate the effect by trying to access the system or a network service.
- Create a monitoring script that checks these files regularly for unauthorized changes.

**Commands/Concepts**: `echo`, `cat`, `cp`, `chmod`, `find`.
