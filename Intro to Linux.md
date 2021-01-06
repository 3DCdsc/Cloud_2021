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
CLI is a command line program that accepts text input to execute operating system functions.
In the 1960s, using only computer terminals, this was the only way to interact with computers.
In the 1970s an 1980s, command line input was commonly used by Unix systems and PC systems like MS-DOS and Apple DOS.
Today, with graphical user interfaces (GUI), most users never use command-line interfaces (CLI).
However, CLI is still used by software developers and system administrators to configure computers, install software, and access features that are not available in the graphical interface.
Linux's CLI is called _Terminal_ while Window's CLI is called _Command Prompt (CMD)_

## 3. Linux CLI Basics

#### 3.1. Navigating in the CLI



> print working directory
```
pwd
```



> change directory
```
cd
```
Often used with ls to show where to go

1. `cd ~`
   is the shortcut to home dir
2. `cd ..`
   to go back 1 level


> list
```
ls
```

 



List all available directories/files

1. `ls -l`
   the argument **_l_** means long, list the long way shows the info of the files/dir including date of create, created by who

2. `ls {dir}`
   to list a particular directory without changing your current working directory


> make new directory

`mkdir `

> remove
```
rm
```

To delete something, if deleting a dir need -rf

1. `rm -rf {directory}`

2. `rm *`
   removing all

3. `rm *.txt`
   removing all txt file

4. `rm {filenames}*`
   removing all files of the same name

```
cp
```

copy files
`-cp {file name} {directory}`

```
mv
```

> move

1. Use to moving files to another dir
   `-mv {file name} {directory}`

2. Use to renaming
   `{current file/dir name} {desired new name}`

```
clear
```

> clear the cluttered screen

#### 3.2 What is sudo?

`sudo {any command}`

> super user do

To gain highest privilege access
SU privilege is not available by default because it could be dangerous if user accidentally wreck the system with some commands.

#### 3.3 How to run a file with any app?

To run a file with any installed app,

```
{name of the app} {name of the file}
```

eg: open .py with python3 runs the program you wrote, open .py with nano edits the code of your program

`nano helloworld.py` edits the code of the program

![](images/run%20w%20nano.PNG)

`python3 helloworld.py` runs the program named helloworld with python

![](images/run%20w%20python.PNG)

#### 3.4.a Creating a file method 1 : touch

```
touch
```

> creating multiple files of any type

1. `touch file1.txt file2.py file3.jar file4.css file5.html`

#### 3.4.b Creating a file method 2 : Creating a file with text editor, then save

> **_nano_** is the default text editor in Linux.

Step 1:
`nano {name of your file}` opens an empty nano named {name of your file}

Step 2:
_Write Out (Ctrl + O)_

to save the file under any file extension such as .css, .html, .js or .py etc

#### 3.5 Installing packages (Apps) from official repository
  **_Note: Remember to use sudo_**

In windows we install softwares using installers, generally with the .exe file extension. In Linux, the installers are called packages. The packages in Linux are mostly stored in a repository. If it is not available in the official repository, users need to download the package file and install it manually.

```
apt-cache search {name of the program}
```

searching something in the repository

```
apt-get install {name of the program}
```

installing apps that are in the official repositories

```
apt-get remove {name of the program}
```

uninstalling

#### 3.6 How about installing something that is not in the official repo?

Step 1: Web browser download the package
Step 2: Locate the package and run it with `sudo apt-get -i {name of the package.deb}`
#### 3.7 Updating the apps

```
apt-get update
```

Updates the list of available packages and their versions, but it does not install or upgrade any packages

```
apt-get upgrade
```

 Installs newer versions of the packages you have. After updating the lists, the package manager knows about available updates for the software you have installed.

***You should first run `update` then `upgrade`***
