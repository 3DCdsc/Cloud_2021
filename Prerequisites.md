---
title: 0. Prerequisites
has_children: false
nav_order: 1
---

# Prerequisites

This course is facilitated for people with little/no knowledge in using the cloud and Linux in general. However, for the sake of time, there is a few things we would like to get over with before we start the workshop.

### 1. Get a Google account

You will need this to access the Google Cloud Platform console to create your VMs.

**Steps:** You know how to do this :disappointed_relieved:

### 2. Sign up for Google Cloud Platform

Needed to create VMs and deploy your web app.

**Steps:**

1. Agree to the terms of service and sell your soul.
2. Click on the `Try for free` button.
3. Remember where you live and fill in your country and agree to the same ToS again.
4. Change account type to individual.
5. Fill in your card details (they won't charge it, hopefully).
6. START YOUR FREE TRIAL

Make sure that billing is enabled and you are good to go!

### 3. Create a public/private key

This is used for securely connecting to your GCE instance.

### 4. Applications required

#### 4.a. SSH client (all platforms)

You will need a ssh client to talk to your cloud server.

- Linux and macOS come built in with one inside the terminal. You can connect to the machine using this command `ssh -i PATH_TO_PRIVATE_KEY USERNAME@EXTERNAL_IP`. Alternatively you can use a GUI manager such as [Termius](https://termius.com/).
- For Windows, during the workshop I will cover how to use [PuTTY](https://www.putty.org/) to connect to your VM.

#### 4.b. Linux (Optional but highly reccomended)

You will need access to a local Linux terminal for the first part of the workshop. Since we will be covering using Linux on a VM, you may choose to not install it locally and try the commands directly on the cloud.
However, we reccomend installing a local version of Linux for ease of use (and speed, your personal computer is still much faster than VM we will be using).

For the purposes of the workshop, we will be covering how to use Ubuntu 20.04 LTS running on WSL.

- _Linux users_: `Ctrl + Alt + T` you already have access to a Linux terminal :stuck_out_tongue:
- _Windows users_: I personally reccommend installing [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps) (follow manual steps). Alternatively, if you want a desktop interface, you can use [Virtual Box](https://www.virtualbox.org/)
- _macOS users_: Use [Parallels](https://www.parallels.com/blogs/linux-on-mac/) or [Virtual Box](https://www.virtualbox.org/). Alternatively you can try setting up QEMU.
