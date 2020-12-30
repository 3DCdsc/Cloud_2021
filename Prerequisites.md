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
