Example for Configuring a Device to Access Another Device as an STelnet Client (Password Authentication)
========================================================================================================

Example for Configuring a Device to Access Another Device as an STelnet Client (Password Authentication)

#### Networking Requirements

The customer requires secure data exchange between the server and client. In [Figure 1](#EN-US_TASK_0000001827083937__fig1864417281813), the SSH user **Client** is configured to use the password authentication mode to log in to the SSH server. A new port number is configured, and the default port number is not used.

**Figure 1** Network diagram for login to another device using STelnet![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001780387520.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. On the SSH server, set the authentication mode to password authentication for the SSH user.
2. Enable the STelnet service on the SSH server.
3. Set the service type of the SSH user to STelnet on the SSH server.
4. Set an SSH server listening port number on the SSH server to prevent attackers from accessing the standard SSH service port, ensuring security.
5. Configure the SSH user to log in to the SSH server through STelnet.

#### Procedure

1. Create an SSH user on the server.
   
   
   
   # Configure a VTY user interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname SSH Server
   [*HUAWEI] commit
   [~SSH Server] user-interface vty 0 4
   [~SSH Server-ui-vty0-4] authentication-mode aaa
   [*SSH Server-ui-vty0-4] protocol inbound ssh
   [*SSH Server-ui-vty0-4] user privilege level 3
   [*SSH Server-ui-vty0-4] quit
   [*SSH Server] commit
   ```
   
   # Create an SSH user named **client**. Configure the password authentication mode for the user and set the password to **YsHsjx\_202206**.
   
   ```
   [~SSH Server] aaa
   [~SSH Server-aaa] local-user client password
   Please configure the login password (8-128)
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   [*SSH Server-aaa] local-user client privilege level 3
   [*SSH Server-aaa] local-user client service-type ssh
   [*SSH Server-aaa] quit
   [*SSH Server] ssh user client
   [*SSH Server] ssh user client authentication-type password
   [*SSH Server] commit
   ```
   
   # Configure the encryption algorithm, HMAC authentication algorithm, key exchange algorithm list, and public key algorithm on **Client**.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname client
   [*HUAWEI] commit
   [~client] ssh client cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
   [*client] ssh client hmac sha2_256 sha2_512
   [*client] ssh client key-exchange dh_group_exchange_sha256 dh_group16_sha512
   [*client] ssh client publickey rsa_sha2_256 rsa_sha2_512
   [*client] commit
   ```
2. Enable the STelnet service on the SSH server and specify the source interface for the SSH server.
   
   
   
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
3. Set the service type of the SSH user **client** to STelnet.
   
   
   ```
   [~SSH Server] ssh user client service-type stelnet
   ```
4. Configure a new listening port number on the SSH server.
   
   
   ```
   [*SSH Server] ssh server port 1025
   [*SSH Server] commit
   ```
5. Connect the STelnet client to the SSH server.
   
   
   
   # Enable the first login function for the SSH client.
   
   Enable first login for **client**.
   
   ```
   [~client] ssh client first-time enable
   [*client] commit
   [~client] quit
   ```
   
   # Log in to the SSH server from the STelnet client in password authentication mode by entering the user name and password.
   
   ```
   <client> stelnet 10.1.1.1 1025
   Trying 10.1.1.1 ...
   Press CTRL+K to abort
   Connected to 10.1.1.1 ...
   The server's public key does not match the one cached before. 
   The server is not authenticated. Continue to access it?[Y/N]:y
   The keyname:10.1.1.1 already exists. Update it? [Y/N]:n
   
   Please input the username: client    
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
   
   If the user view is displayed, the login is successful. If the message **Session is disconnected** is displayed, the login fails.

#### Verifying the Configuration

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
STELNET IPv4 server                     : Enable
STELNET IPv6 server                        : Enable
SNETCONF IPv4 server                       : Enable
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
User Name             : client
Authentication type   : password
User public key name  : --
User public key type  : --
Sftp directory        : flash:
Service type          : stelnet
--------------------------------------------------------------------------------
Total 1, 1 printed    
```

#### Configuration Scripts

* SSH server
  
  ```
  #
  sysname SSH Server
  #
  aaa
   local-user client password irreversible-cipher $1d$v!=.5/:(q-$xL=\K+if"'S}>k7vGP5$_ox0B@ys7.'DBHL~3*aN$
   local-user client service-type ssh
   local-user client privilege level 3
  #
  ssh server port 1025
  stelnet server enable
  ssh user client
  ssh user client authentication-type password
  ssh user client service-type stelnet
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
   user privilege level 3
  #
  return
  ```
* Client
  
  ```
  #
  sysname client
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