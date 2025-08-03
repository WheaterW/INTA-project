Example for Configuring a Device as an SCP Client
=================================================

Example for Configuring a Device as an SCP Client

#### Networking Requirements

Compared with SFTP, SCP simplifies file transfer operations by combining user identity authentication and file transfer to improve configuration efficiency.

In [Figure 1](#EN-US_TASK_0000001513150622__fig_dc_cfg_file_0037), the routes between the SCP client and SSH server are reachable. The SCP client needs to download files from the SSH server.

**Figure 1** Network diagram for configuring a device to access files on another device as an SCP client![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001564110705.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Generate a local key pair on the SSH server.
2. Create an SSH user on the SSH server.
3. Enable the SCP server function on the SSH server.
4. Download files from the SSH server to the SCP client.

#### Procedure

1. Generate a local key pair on the server.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname SSH Server
   [*HUAWEI] commit
   [~SSH Server] rsa local-key-pair create
   The key name will be:Host
   The range of public key size is (2048, 4096).
   NOTE: Key pair generation will take a short while.
   Please input the modulus [default = 3072]:
   [*SSH Server] commit
   ```
2. Create an SSH user on the server.
   
   
   
   # Configure a VTY user interface.
   
   ```
   [~SSH Server] user-interface vty 0 4
   [*SSH Server-ui-vty0-4] authentication-mode aaa
   [*SSH Server-ui-vty0-4] protocol inbound ssh
   [*SSH Server-ui-vty0-4] quit
   ```
   
   # Create an SSH user named **Client**, set the authentication mode to **password**, and set the service type to **all**.
   
   ```
   [*SSH Server] ssh user Client
   [*SSH Server] ssh user Client authentication-type password
   [*SSH Server] ssh user Client service-type all
   ```
   
   # Set a password for the **Client** user.
   
   ```
   [*SSH Server] aaa
   [*SSH Server-aaa] local-user Client password
   Please configure the login password (8-128)
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   Info: Add a new user.
   [*SSH Server-aaa] local-user Client service-type ssh
   [*SSH Server-aaa] local-user Client privilege level 3 
   [*SSH Server-aaa] quit
   ```
3. Enable the SCP server function on the SSH server.
   
   
   ```
   [*SSH Server] scp server enable 
   [*SSH Server] ssh server-source all-interface
   [*SSH Server] commit
   ```
4. Configure the public key algorithm, encryption algorithm, key exchange algorithm list, HMAC authentication algorithm, and minimum key length on the SSH server.
   
   
   ```
   [~SSH Server] ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
   [*SSH Server] ssh server hmac sha2_256 sha2_512
   [*SSH Server] ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
   [*SSH Server] ssh server publickey rsa_sha2_256 rsa_sha2_512
   [*SSH Server] ssh server dh-exchange min-len 3072
   [*SSH Server] commit
   ```
5. Configure the encryption algorithm, HMAC authentication algorithm, key exchange algorithm list, and public key algorithm on the client.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname SCP Client
   [*SCP Client] ssh client cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
   [*SCP Client] ssh client hmac sha2_256 sha2_512
   [*SCP Client] ssh client key-exchange dh_group_exchange_sha256 dh_group16_sha512
   [*SCP Client] ssh client publickey rsa_sha2_256 rsa_sha2_512
   [*SCP Client] commit
   ```

#### Verifying the Configuration

Download files from the SSH server to the SCP client.

# Enable the first login function for the SSH client.

```
<HUAWEI> system-view
[~HUAWEI] sysname SCP Client
[*HUAWEI] commit
[~SCP Client] ssh client first-time enable
[*SCP Client] commit
```

# Download the **backup.cfg** file from the SSH server at 10.1.1.1 to the local directory using the aes256\_ctr encryption algorithm.

```
[~SCP Client] scp -cipher aes256_ctr Client@10.1.1.1:backup.cfg backup.cfg
Trying 10.1.1.1 ...
Press CTRL+K to abort
Connected to 10.1.1.1 ...
 Continue to access it? [Y/N]:y
 [Y/N]:y
The server's public key will be saved with the name 10.1.1.1. Please wait...

Enter password:
backup.cfg                     100%        19174Bytes            7Kb/s
```

#### Configuration Scripts

* SSH server
  
  ```
  #
  sysname SSH Server
  #
  aaa
   local-user Client password irreversible-cipher $#z$!9S<a#>H7{7dI>%0S{AcKGC=t:zjv14LlQqHO\\P.*=<x1]u;y*P`'GR3[m}$
   local-user Client service-type terminal ssh
   local-user Client privilege level 3 
  #
  scp server enable
  ssh user Client
  ssh user Client authentication-type password
  ssh user Client service-type all  
  ssh server-source all-interface
  #
  user-interface vty 0 4
   authentication-mode aaa
   protocol inbound ssh
  #
  ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
  ssh server hmac sha2_256 sha2_512
  ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
  ssh server publickey rsa_sha2_256 rsa_sha2_512
  ssh server dh-exchange min-len 3072
  #
  return
  ```
* SCP client
  
  ```
  #
  sysname SCP Client
  #
  ssh client first-time enable
  #
  ssh client cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
  ssh client hmac sha2_256 sha2_512
  ssh client key-exchange dh_group_exchange_sha256 dh_group16_sha512
  ssh client publickey rsa_sha2_256 rsa_sha2_512
  #
  return
  ```