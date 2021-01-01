---
title: Connecting to your instance
parent: Google Compute Engine
has_children: false
nav_order: 1
---

# Connecting to your instance

### :exclamation: We will only cover connecting to GCE using PuTTY

#### Why use PuTTY and private keys and all that?

Security. You usually don't want random internet strangers taking control over your code and servers.

### Using SSH keys to connect to your instance

1. Get your public and private keys. PuTTYgen will give you a private key in `.ppk` form, and copy your public key from the interface. Your public key should start with `ssh-rsa` and end with your key comment. **Goes without saying, your should keep your private key private.**
2. Go to your instance on GCP and click on the edit button. Scroll down to the SSH Keys section. Click on the `Add item` button and paste in your public SSH key. If everything is correct then you should see your username on the left side.
3. Click on save. Give your instance a while to update.
4. From the interface, get the external IP of your machine.
5. Open PuTTY, paste the external IP in the `Host name`. SSH port used in GCP (and in general) is 22. On the left sidebar, under connection, expand SSH, then click on Auth. At the bottom click on browse and select your private key.
6. Go back to the session screen. You might want to save the configuration. To do this type in a name under Saved sessions and click the save button.
7. Press `Open`. If there is a prompt, say yes. You should get a new window asking for a username. Put in the username from the public key, and you should be able to access the VM!
