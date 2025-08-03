Example for Configuring a Device to Access Another Device as an STelnet Client (Password and RSA Authentication)
================================================================================================================

Example for Configuring a Device to Access Another Device as an STelnet Client (Password and RSA Authentication)

#### Networking Requirements

The customer requires secure data exchange between the server and client. In [Figure 1](#EN-US_TASK_0000001513053082__fig13411164017368), two login users **client001** and **client002** are configured and they use the password and RSA authentication modes respectively to log in to the SSH server. A new port number is configured, and the default port number is not used.

**Figure 1** Network diagram for login to another device using STelnet![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001987318233.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the SSH server to generate a local key pair to implement secure data exchange between the server and client.
2. Configure different authentication modes for the SSH users **client001** and **client002** on the SSH server.
3. Enable the STelnet service on the SSH server.
4. Configure the STelnet service type for the SSH users **client001** and **client002** on the SSH server.
5. Set an SSH server listening port number on the SSH server to prevent attackers from accessing the standard SSH service port, ensuring security.
6. Log in to the SSH server as the **client001** and **client002** users through STelnet.

#### Procedure

1. Configure the server to generate a local key pair.
   
   
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
2. Create SSH users on the server.
   
   
   
   # Configure a VTY user interface.
   
   ```
   [~SSH Server] user-interface vty 0 4
   [~SSH Server-ui-vty0-4] authentication-mode aaa
   [*SSH Server-ui-vty0-4] protocol inbound ssh
   [*SSH Server-ui-vty0-4] quit
   [*SSH Server] commit
   ```
   * Create an SSH user named **client001**.
     
     # Create an SSH user named **client001** and configure the password authentication mode for the user.
     
     ```
     [~SSH Server] aaa
     [~SSH Server-aaa] local-user client001 password
     Please configure the login password (8-128)
     It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
     Please enter password:                                      
     Please confirm password:                               
     [*SSH Server-aaa] local-user client001 privilege level 3
     [*SSH Server-aaa] local-user client001 service-type ssh
     [*SSH Server-aaa] quit
     [*SSH Server] ssh user client001
     [*SSH Server] ssh user client001 authentication-type password
     [*SSH Server] commit
     ```
     
     # Configure the encryption algorithm, HMAC authentication algorithm, key exchange algorithm list, and public key algorithm on **client001**.
     
     ```
     <HUAWEI> system-view
     [~HUAWEI] sysname client001
     [*HUAWEI] commit
     [~client001] ssh client cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
     [*client001] ssh client hmac sha2_256 sha2_512
     [*client001] ssh client key-exchange dh_group_exchange_sha256 dh_group16_sha512
     [*client001] ssh client publickey rsa_sha2_256 rsa_sha2_512
     [*client001] commit
     ```
   * Create an SSH user named **client002**.
     
     # Create an SSH user named **client002** and configure the RSA authentication mode for the user.
     
     ```
     [~SSH Server] ssh user client002
     [*SSH Server] ssh user client002 authentication-type rsa
     [*SSH Server] ssh authorization-type default root
     [*SSH Server] commit
     ```
     
     # Configure **client002** to generate a local key pair.
     
     ```
     <HUAWEI> system-view
     [~HUAWEI] sysname client002
     [*HUAWEI] commit
     [~client002] rsa local-key-pair create
     The key name will be: client002_Host
     The range of public key size is (2048, 4096).
     NOTE: Key pair generation will take a short while.
     Please input the modulus [default = 3072]:
     [*client002] commit
     ```
     
     # Configure the encryption algorithm, HMAC authentication algorithm, key exchange algorithm list, and public key algorithm on **client002**.
     
     ```
     [~client002] ssh client cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
     [*client002] ssh client hmac sha2_256 sha2_512
     [*client002] ssh client key-exchange dh_group_exchange_sha256 dh_group16_sha512
     [*client002] ssh client publickey rsa_sha2_256 rsa_sha2_512
     [*client002] commit
     ```
     # Check the public key in the RSA key pair generated on the client.
     ```
     [~client002] display rsa local-key-pair public
     ======================Host key==========================
     Time of Key pair created : 2023-12-27 18:00:55 
     Key Name    : Host 
     Key modulus : 3072 
     Key Type    : RSA Encryption Key
     ========================================================
     Key code:
     3082010A
       02820101
         00A4BAB8 B964077E F7657F7F E4BE1DE8 71EE1707
         E4EE2864 2D06FBE0 BFC1CB52 F99B7A99 0132B709
         3F841CA2 3544B8B2 6EE0A9ED 04B19FE3 FB3DA86D
         BE68FFE2 2303108D BDC24B80 A1793A08 FDA0B6C1
         13C31EA5 298EC9B1 2B0BC8BD 32CFF896 29F8CA98
         8B1724AF 5DA8A390 20906ADE 6A8AD77D 6234F0C8
         DC965BA0 1771D9C0 A89ED49B 5ECF7EE2 D5997527
         FC87FE03 E51658C1 0996DFDF DC456376 2FA4B268
         4345131D 431419D2 DD5E4003 6A7D3295 145F3175
         22E80686 E6B39A05 799D6BCF A78F69B6 BC2D0836
         F5013421 77D68B89 A9EC182A 04B87BE3 500FCE14
         9C95CF78 75704359 0C70FD60 1EFC0B99 32F02142
         4CE781E4 36A60BFC 2CBD07F6 9E700CEE 4D0203
         010001
     
     Key fingerprint:   
       ssh-rsa 3072 47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU
     
     Host public key for PEM format code:
     ---- BEGIN SSH2 PUBLIC KEY ----
     AAAAB3NzaC1yc2EAAAADAQABAAABAQCkuri5ZAd+92V/f+S+Hehx7hcH5O4oZC0G
     ++C/wctS+Zt6mQEytwk/hByiNUS4sm7gqe0EsZ/j+z2obb5o/+IjAxCNvcJLgKF5
     Ogj9oLbBE8MepSmOybErC8i9Ms/4lin4ypiLFySvXaijkCCQat5qitd9YjTwyNyW
     W6AXcdnAqJ7Um17PfuLVmXUn/If+A+UWWMEJlt/f3EVjdi+ksmhDRRMdQxQZ0t1e
     QANqfTKVFF8xdSLoBobms5oFeZ1rz6ePaba8LQg29QE0IXfWi4mp7BgqBLh741AP
     zhSclc94dXBDWQxw/WAe/AuZMvAhQkzngeQ2pgv8LL0H9p5wDO5N
     ---- END SSH2 PUBLIC KEY ----
     
     Public key code for pasting into OpenSSH authorized_keys file:
     ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkuri5ZAd+92V/f+S+Hehx7hcH5O4oZC0G++C/wctS+Zt6mQEytwk/hByiNUS4sm7gqe0EsZ/j+z2obb5o/+IjAxCNvcJLgKF5Ogj9oLbBE8MepSmOybErC8i9Ms/4lin4ypiLFySvXaijkCCQat5qitd9YjTwyNyWW6AXcdnAqJ7Um17PfuLVmXUn/If+A+UWWMEJlt/f3EVjdi+ksmhDRRMdQxQZ0t1eQANqfTKVFF8xdSLoBobms5oFeZ1rz6ePaba8LQg29QE0IXfWi4mp7BgqBLh741APzhSclc94dXBDWQxw/WAe/AuZMvAhQkzngeQ2pgv8LL0H9p5wDO5N rsa-key
     ```
     
     # Copy the RSA public key (the information in bold in the **display** command output) generated on the client to the server.
     ```
     [~SSH Server] rsa peer-public-key rsakey001
     [*SSH Server-rsa-public-key] public-key-code begin
     [*SSH Server-rsa-public-key-rsa-key-code] 3082010A
     [*SSH Server-rsa-public-key-rsa-key-code] 2820101
     [*SSH Server-rsa-public-key-rsa-key-code] 00A4BAB8 B964077E F7657F7F E4BE1DE8 71EE1707
     [*SSH Server-rsa-public-key-rsa-key-code] E4EE2864 2D06FBE0 BFC1CB52 F99B7A99 0132B709
     [*SSH Server-rsa-public-key-rsa-key-code] 3F841CA2 3544B8B2 6EE0A9ED 04B19FE3 FB3DA86D
     [*SSH Server-rsa-public-key-rsa-key-code] BE68FFE2 2303108D BDC24B80 A1793A08 FDA0B6C1
     [*SSH Server-rsa-public-key-rsa-key-code] 13C31EA5 298EC9B1 2B0BC8BD 32CFF896 29F8CA98
     [*SSH Server-rsa-public-key-rsa-key-code] 8B1724AF 5DA8A390 20906ADE 6A8AD77D 6234F0C8
     [*SSH Server-rsa-public-key-rsa-key-code] DC965BA0 1771D9C0 A89ED49B 5ECF7EE2 D5997527
     [*SSH Server-rsa-public-key-rsa-key-code] FC87FE03 E51658C1 0996DFDF DC456376 2FA4B268
     [*SSH Server-rsa-public-key-rsa-key-code] 4345131D 431419D2 DD5E4003 6A7D3295 145F3175
     [*SSH Server-rsa-public-key-rsa-key-code] 22E80686 E6B39A05 799D6BCF A78F69B6 BC2D0836
     [*SSH Server-rsa-public-key-rsa-key-code] F5013421 77D68B89 A9EC182A 04B87BE3 500FCE14
     [*SSH Server-rsa-public-key-rsa-key-code] 9C95CF78 75704359 0C70FD60 1EFC0B99 32F02142
     [*SSH Server-rsa-public-key-rsa-key-code] 4CE781E4 36A60BFC 2CBD07F6 9E700CEE 4D
     [*SSH Server-rsa-public-key-rsa-key-code] 203
     [*SSH Server-rsa-public-key-rsa-key-code] 10001
     [*SSH Server-rsa-public-key-rsa-key-code] public-key-code end
     [*SSH Server-rsa-public-key] peer-public-key end
     [*SSH Server] commit
     ```
     
     # On the server, bind the RSA public key of the STelnet client to the SSH user **client002**.
     
     ```
     [~SSH Server] ssh user client002 assign rsa-key rsakey001
     [*SSH Server] commit
     ```
3. Enable the STelnet service on the SSH server and specify the source interface for the SSH server.
   
   
   
   # Enable the STelnet service.
   
   ```
   [~SSH Server] stelnet server enable
   ```
   
   # Specify the source interface for the SSH server.
   
   ```
   [*SSH Server] ssh server-source all-interface 
   [*SSH Server] commit
   ```
   
   # Configure the public key algorithm, encryption algorithm, key exchange algorithm list, HMAC authentication algorithm, and minimum key length on the SSH server.
   
   ```
   [~SSH Server] ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
   [*SSH Server] ssh server hmac sha2_256 sha2_512
   [*SSH Server] ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
   [*SSH Server] ssh server publickey rsa_sha2_256 rsa_sha2_512
   [*SSH Server] ssh server dh-exchange min-len 3072
   [*SSH Server] commit
   ```
4. Set the service type to STelnet for the SSH users **client001** and **client002**.
   
   
   ```
   [~SSH Server] ssh user client001 service-type stelnet
   [*SSH Server] ssh user client002 service-type stelnet
   ```
5. Configure a new listening port number on the SSH server.
   
   
   ```
   [*SSH Server] ssh server port 1025
   [*SSH Server] commit
   ```
6. Connect the STelnet clients to the SSH server.
   
   
   
   # Enable the first login function for the SSH clients.
   
   Enable first login for **client001**.
   
   ```
   [~client001] ssh client first-time enable
   [*client001] commit
   [~client001] quit
   ```
   
   Enable first login for **client002**.
   
   ```
   [~client002] ssh client first-time enable
   [*client002] commit
   [~client002] quit
   ```
   
   # Log in to the SSH server from **client001** in password authentication mode by entering the user name and password.
   
   ```
   <client001> stelnet 10.1.1.1 1025
   Trying 10.1.1.1 ...
   Press CTRL+K to abort
   Connected to 10.1.1.1 ...
   The server's public key does not match the one cached before. 
   The server is not authenticated. Continue to access it?[Y/N]:y
   The keyname:10.1.1.1 already exists. Update it? [Y/N]:n
   
   Please input the username: client001    
   Enter password:
   ```
   
   Enter the password. The following information indicates that the login is successful:
   
   ```
   Warning: The initial password poses security risks.                             
   The password needs to be changed. Change now? [Y/N]:n
   
   Info: The max number of VTY users is 21, the number of current VTY users online is 4, and total number of terminal users online is 4.                           
         The current login time is 2023-12-31 11:22:06.                            
   <SSH Server>
   ```
   
   # Log in to the SSH server from **client002** in RSA authentication mode.
   
   ```
   <client002> stelnet 10.1.1.1 1025
   Trying 10.1.1.1 ...
   Press CTRL+K to abort
   Connected to 10.1.1.1 ...
   The server's public key does not match the one cached before. 
   The server is not authenticated. Continue to access it?[Y/N]:y
   The keyname:10.1.1.1 already exists. Update it? [Y/N]: n
   
   Please input the username: client002
   Info: The max number of VTY users is 21, the number of current VTY users online is 4, and total number of terminal users online is 4.                           
         The current login time is 2023-12-31 11:36:06. 
   <SSH Server>
   ```
   
   If the user view is displayed, the login is successful. If the message **Session is disconnected** is displayed, the login fails.

#### Verifying the Configuration

# Attackers fail to log in to the SSH server using the default listening port number 22.

```
<client002> stelnet 10.1.1.1
Trying 10.1.1.1 ...
Press CTRL+K to abort
Error: Failed to connect to the remote host.
```

The **display ssh server status** command output indicates that the STelnet service has been enabled. The **display ssh user-information** command output contains information about SSH users on the server.

# Check the status of the SSH server.

```
[~SSH Server] display ssh server status  
SSH Version                                : 2.0
SSH authentication timeout (Seconds)       : 60
SSH authentication retries (Times)         : 3
SSH server key generating interval (Hours) : 0
SSH version 1.x compatibility              : Enable
SSH server keepalive                       : Disable
SFTP IPv4 server                           : Disable
SFTP IPv6 server                           : Disable
STELNET IPv4 server                        : Enable
STELNET IPv6 server                        : Enable
SNETCONF IPv4 server                    : Enable
SNETCONF IPv6 server                       : Enable
SNETCONF IPv4 server port(830)             : Disable
SNETCONF IPv6 server port(830)             : Disable
SCP IPv4 server                            : Enable
SCP IPv6 server                            : Enable
SSH port forwarding                        : Disable
SSH IPv4 server port                       : 1025
SSH IPv6 server port                       : 1025
ACL name                                   :
ACL number                                 :
ACL6 name                                  : 
ACL6 number                                :
SSH server ip-block                        : Enable
```

# Check information about SSH users.

```
[~SSH Server] display ssh user-information
--------------------------------------------------------------------------------
User Name             : client001
Authentication type   : password
User public key name  : -
User public key type  : -
Sftp directory        : -
Service type          : stelnet

User Name             : client002
Authentication type   : rsa
User public key name  : -
User public key type  : -
Sftp directory        : -
Service type          : stelnet
--------------------------------------------------------------------------------
Total 2, 2 printed    
```

#### Configuration Scripts

* SSH server
  
  ```
  #
  sysname SSH Server
  #
  rsa peer-public-key rsakey001
   public-key-code begin
   3082010A
    02820101
      00A4BAB8 B964077E F7657F7F E4BE1DE8 71EE1707 E4EE2864 2D06FBE0 BFC1CB52
      F99B7A99 0132B709 3F841CA2 3544B8B2 6EE0A9ED 04B19FE3 FB3DA86D BE68FFE2
      2303108D BDC24B80 A1793A08 FDA0B6C1 13C31EA5 298EC9B1 2B0BC8BD 32CFF896
      29F8CA98 8B1724AF 5DA8A390 20906ADE 6A8AD77D 6234F0C8 DC965BA0 1771D9C0
      A89ED49B 5ECF7EE2 D5997527 FC87FE03 E51658C1 0996DFDF DC456376 2FA4B268
      4345131D 431419D2 DD5E4003 6A7D3295 145F3175 22E80686 E6B39A05 799D6BCF
      A78F69B6 BC2D0836 F5013421 77D68B89 A9EC182A 04B87BE3 500FCE14 9C95CF78
      75704359 0C70FD60 1EFC0B99 32F02142 4CE781E4 36A60BFC 2CBD07F6 9E700CEE
      4D
    0203
      010001
   public-key-code end
   peer-public-key end
  #
  aaa
   local-user client001 password irreversible-cipher $1d$v!=.5/:(q-$xL=\K+if"'S}>k7vGP5$_ox0B@ys7.'DBHL~3*aN$
   local-user client001 service-type ssh
   local-user client001 privilege level 3
  #
  ssh server port 1025
  stelnet server enable
  ssh user client001
  ssh user client001 authentication-type password
  ssh user client001 service-type stelnet
  ssh user client002
  ssh user client002 authentication-type rsa
  ssh user client002 assign rsa-key rsakey001
  ssh user client002 service-type stelnet
  ssh authorization-type default root 
  ssh server-source all-interface
  #
  ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
  ssh server hmac sha2_256 sha2_512
  ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
  ssh server publickey rsa_sha2_256 rsa_sha2_512
  ssh server dh-exchange min-len 3072
  #
  user-interface vty 0 4
   authentication-mode aaa
   protocol inbound ssh
  #
  return
  ```
* client001
  
  ```
  #
  sysname client001
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
* client002
  
  ```
  #
  sysname client002
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