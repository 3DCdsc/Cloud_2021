---
title: Linux
has_children: false
nav_order: 2
---

# Linux

## What is Linux?

![What is Linux?](images/linux%20logo.png)

Linux is a platform of choice to run desktops, servers, and embedded systems across the globe, Linux is one of the most reliable, secure and worry-free operating systems available. Just like Windows, iOS, and Mac OS, Linux is an operating system. In fact, one of the most popular platforms on the planet, Android, is powered by the Linux operating system. An operating system is software that manages all of the hardware resources associated with your desktop or laptop. To put it simply, the operating system manages the communication between your software and your hardware. Without the operating system (OS), the software wouldn't function. Linux is the leading operating system on servers (over 96.4% of the top 1 million web servers' operating systems are Linux),[28] leads other big iron systems such as mainframe computers, and is the only OS used on TOP500 supercomputers (since November 2017, having gradually eliminated all competitors).

**_Fun Fact:_**
SpaceX's Falcon 9's and the Dragon 2's avionics use a customized version of Linux!

## 2. What is Command Line Interface (CLI)?

![](images/terminal%20vs%20cmd.png)
CLI is a command line that accepts text input to execute operating system functions.
In the 1960s, using only computer terminals, this was the only way to interact with computers.
In the 1970s an 1980s, command line input was commonly used by Unix systems and PC systems like MS-DOS and Apple DOS.
Today, with graphical user interfaces (GUI), most users never use command-line interfaces (CLI).
However, CLI is still used by software developers and system administrators to configure computers, install software, and access features that are not available in the graphical interface.
Linux's CLI is called _Terminal_ while Windows CLI is called _Command Prompt (CMD)_.

## 3. Linux CLI Basics

### 3.1. Navigating in the CLI

| Command | Meaning                 | What it does                                                |
| ------- | ----------------------- | ----------------------------------------------------------- |
| `pwd`   | print working directory | show current directory of the terminal session              |
| `cd`    | change directory        | move to a different directory                               |
| `ls`    | list                    | list folders and files in `pwd`                             |
| `rm`    | remove                  | remove file\directory                                       |
| `mkdir` | make directory          | create a new directory                                      |
| `cp`    | copy                    | create a copy of a file or directory                        |
| `mv`    | move                    | move a file or directory, also used to rename files         |
| `clear` | clear                   | clean the terminal output                                   |
| `cat`   | concatenate             | used to print the contents of files and join files together |
| `wget`  | -                       | download files from the internet                            |
| `top`   | -                       | see running processes                                       |

### Paths in Linux

There are two ways to find a directory in Linux.

1. **Absolute path:** Starts from the root directory (`/`) and traces all folders to reach the file. You can also start absolute paths from home directory (`~`).
   e.g. `/home/shohamc1/main.py` or `~/main.py`
2. **Relative path:** Path expressed relative to `pwd`. `.` is used for current directory, `..` is used for the parent directory.
   e.g. If you are at `/home/shohamc1` and you want to access `abc.txt` at `/`, you can access it using the path `../../abc.txt`.

#### `ls`

Some additional, useful functionality for `ls`:

1. `ls -l`
   the argument **_l_** means long, list the long way shows the info of the files/dir including date of create, created by who

2. `ls {dir}`
   to list a particular directory without changing your current working directory

#### `rm`

To delete a directory, you need to use the `-r` (recursive) flag.

1. `rm -r /path/to/dir`

2. `rm *` - removing all

3. `rm *.txt` - removing all txt file

4. `rm {filenames}*` - removing all files of the same name

### 3.2. What is sudo?

```bash
$ sudo {any command}
```

sudo = **super user do**

Sudo is used to gain highest privilege access (similar to administrator mode in Windows, but a lot more powerful).
Superuser privilege is not available by default because as it is quick easy to break Linux systems as you can do almost anything in `sudo` mode, including deleting the whole hard disk itself.

### 3.3. How to run a file with an app?

To run a file with any installed app, use

```bash
$ {name of the app} {name of the file}
```

eg: Open .py with python3 runs the program you wrote, open .py with nano edits the code of your program

`nano helloworld.py` edits the code.

![](images/run%20w%20nano.png)

`python3 helloworld.py` runs the program named "helloworld" with python

![](images/run%20w%20python.png)

### 3.4. Creating new files

#### 3.4.a. `touch`

Touch can be used to create multiple files of any type.

```bash
$ touch file1.txt file2.py file3.jar file4.css file5.html
```

#### 3.4.b. Opening a text editor and saving

> `nano` is the default text editor in Linux. Alternatively you can use `vim`, `micro` or `emacs`.

1. `nano <name of your file>` opens an empty file with the given filename.
2. Save using `Ctrl + O`. Alternatively you can quit using `Ctrl + X` and agree to overwrite changes.

### 3.5. Installing packages (Apps) from official repository

**_Note: Remember to use sudo_**

In Windows we install softwares using installers, generally with the .exe file extension. In Linux, the installers are called packages. The packages in Linux are mostly stored in a repository. If it is not available in the official repository, users need to download the package file and install it manually.

```bash
$ apt-cache search {name of the program}
```

searching something in the repository

```bash
$ apt-get install {name of the program}
```

installing apps that are in the official repositories

```bash
$ apt-get remove {name of the program}
```

### 3.6. How about installing something that is not in the official repo?

1. Use a web browser download the package (`.deb` for Debian based distros)
2. Locate the package and install it.

```bash
$ sudo apt install /path/to/deb
```

### 3.7. Updating the apps

```bash
$ apt update
```

Updates the list of available packages and their versions, but it does not install or upgrade any packages.

```bash
$ apt upgrade
```

Installs newer versions of the packages you have. After updating the lists, the package manager knows about available updates for the software you have installed.

**_You should first run `update` then `upgrade`._**

#### [Next](GCE_Intro.md)
