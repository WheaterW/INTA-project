Example for Using SFTP to Log In to Another Device for File Access (SM2 Authentication Mode)
============================================================================================

To allow an SFTP client to log in to an SSH server, configure the client and server to generate local key pairs, configure the server to generate an SM2 public key, and bind the public key to the corresponding user.

#### Networking Requirements

SFTP is a secure service over SSH connections. It allows remote users to log in to a device to manage and transfer files with higher security guarantee. Because the device can function as an SFTP client, you can log in to a remote SSH server from the device to implement secure file transfer.

As shown in [Figure 1](#EN-US_TASK_0172360145__fig_dc_vrp_basic_cfg_011301), after the SFTP service is enabled on the SSH server, the SFTP clients can log in to the SSH server in RSA, DSA, ECC, SM2, X509v3-SSH-RSA, password, password-RSA, password-ECC, password-DSA, password-SM2, password-X509v3-RSA, or all authentication mode for file access.

**Figure 1** Network diagram of using SFTP to log in to another device for file access![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 represents GigabitEthernet0/0/0.


  
![](figure/en-us_image_0000002111416816.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure users client001 and client002 on the SSH server to use different authentication modes to log in to the server.
2. Configure the SFTP client client002 and SSH server to generate local key pairs, and bind the SM2 public key of the SFTP client to the user client002 so that the client is authenticated when it logs in to the server.
3. Enable the SFTP service on the SSH server.
4. Configure a service type and authorized directory for the SSH users.
5. Configure users client001 and client002 to log in to the SSH server through SFTP for file access.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication mode of the user client001: password authentication
* Authentication mode of the user client002: SM2 authentication (public key: sm2key001)
* IP address of the SSH server: 10.1.1.2

#### Procedure

1. Configure the server to generate a local key pair.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [*HUAWEI] sysname SSH Server
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~SSH Server] ssh server publickey sm2
   ```
2. Create SSH users on the server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   SSH users can be authenticated in password, RSA, password-RSA, ECC, password-ECC, DSA, password-DSA, SM2, password-SM2, or all mode.
   
   * If the authentication mode of an SSH user is password, password-RSA, password-DSA, password-SM2, or password-ECC, a local user with the same name as the SSH user must be configured.
   * If the authentication mode of an SSH user is RSA, password-RSA, DSA, password-DSA, SM2, password-SM2, ECC, password-ECC, or all, the RSA, DSA, SM2, or ECC public key generated on the SSH client needs to be saved to the server.
   
   # Configure VTY user interfaces.
   
   ```
   [*SSH Server] user-interface vty 0 4
   ```
   ```
   [*SSH Server-ui-vty0-4] authentication-mode aaa
   ```
   ```
   [*SSH Server-ui-vty0-4] protocol inbound ssh
   ```
   ```
   [*SSH Server-ui-vty0-4] commit
   ```
   ```
   [~SSH Server-ui-vty0-4] quit
   ```
   * Create an SSH user named client001.
     
     # Create an SSH user named client001 and configure password authentication for it.
     
     ```
     [~SSH Server] ssh user client001
     ```
     ```
     [*SSH Server] ssh user client001 authentication-type password
     ```
     ```
     [*SSH Server] ssh server cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr 
     ```
     ```
     [*SSH Server] ssh server hmac sha2_512 sha2_256
     ```
     ```
     [*SSH Server] ssh server key-exchange dh_group_exchange_sha256 
     ```
     ```
     [*SSH Server] ssh server publickey rsa_sha2_256 rsa_sha2_512 
     ```
     ```
     [*SSH Server] ssh server dh-exchange min-len 3072
     ```
     ```
     [*SSH Server] ssh client publickey rsa_sha2_256 rsa_sha2_512
     ```
     ```
     [*SSH Server] ssh client cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr 
     ```
     ```
     [*SSH Server] ssh client hmac sha2_512 sha2_256 
     ```
     ```
     [*SSH Server] ssh client key-exchange dh_group_exchange_sha256 
     ```
     ```
     [*SSH Server] commit
     ```
     
     # Configure a password for the SSH user client001.
     
     ```
     [~SSH Server] aaa
     ```
     ```
     [*SSH Server-aaa] local-user client001 password
     ```
     ```
     Please configure the password (8-128)
     Enter Password:
     Confirm Password:
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The password must meet the following requirements:
     
     + The password is entered in man-machine interaction mode. The system does not display the entered password.
     + A password is a string of 8 to 16 case-sensitive characters and must contain at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
     + Special characters exclude question marks (?) and spaces. However, spaces are allowed in the password if the password is enclosed in quotation marks.
       - Double quotation marks cannot contain double quotation marks if spaces are used in a password.
       - Double quotation marks can contain double quotation marks if no space is used in a password.
       
       For example, the password "Aa123"45"" is valid, but the password "Aa 123"45"" is invalid.
     
     The configured password is displayed in ciphertext in the configuration file.
     
     ```
     [*SSH Server-aaa] local-user client001 service-type ssh
     ```
     ```
     [*SSH Server-aaa] local-user client001 level 3
     ```
     ```
     [*SSH Server-aaa] commit
     ```
     ```
     [~SSH Server-aaa] quit
     ```
   * Create an SSH user named client002.
     
     # Create an SSH user named client002 and configure SM2 authentication for it.
     
     ```
     [~SSH Server] ssh user client002
     ```
     ```
     [*SSH Server] ssh user client002 authentication-type sm2
     ```
     ```
     [*SSH Server] ssh server cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr 
     ```
     ```
     [*SSH Server] ssh server hmac sha2_512 sha2_256
     ```
     ```
     [*SSH Server] ssh server key-exchange dh_group_exchange_sha256 
     ```
     ```
     [*SSH Server] ssh server publickey rsa_sha2_256 rsa_sha2_512 
     ```
     ```
     [*SSH Server] ssh server dh-exchange min-len 3072
     ```
     ```
     [*SSH Server] ssh client publickey rsa_sha2_256 rsa_sha2_512
     ```
     ```
     [*SSH Server] ssh client cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr 
     ```
     ```
     [*SSH Server] ssh client hmac sha2_512 sha2_256 
     ```
     ```
     [*SSH Server] ssh client key-exchange dh_group_exchange_sha256 
     ```
     ```
     [*SSH Server] ssh authorization-type default root
     ```
     ```
     [*SSH Server] commit
     ```
3. Configure an SM2 public key on the server.
   
   
   
   # Configure the specified client to generate a local key pair.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname client002
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~client002] ssh client publickey sm2
   ```
   ```
   [~client002] sm2 key-pair label sm2key001
   ```
   ```
   Info: Key pair generation will take a short while. Please wait...
   Info: Creating the key pair succeeded.
   ```
   ```
   [~client002] ssh client assign sm2-host-key sm2key001
   ```
   ```
   [*client002] commit
   ```
   
   # Check the SM2 public key generated on the client.
   
   ```
   [~client002] display sm2 key-pair
   ```
   ```
   =====================================
    Label Name: sm2key001
    Modulus: 521
    Time of Key pair created: 2018-06-19 15:39:45
   =====================================
   Key : 
       0474F110 F90F131B B6F6D929 9A23A41E F1AB1666 AC4BE4EE EF2CD876
       2B633F80 DD5CF42F 147A722F DE527F39 247F3744 C23296BE FE3BE502
       EEF7D9EC BC28A576 7E
   =====================================
   ```
   
   # Copy the SM2 public key generated on the client to the server.
   
   ```
   [~SSH Server] sm2 peer-public-key sm2key001
   ```
   ```
   Enter "SM2 public key" view, return system view with "peer-public-key end".
   ```
   ```
   [*SSH Server-sm2-public-key] public-key-code begin
   ```
   ```
   Enter "SM2 key code" view, return last view with "public-key-code end".
   ```
   ```
   [*SSH Server-sm2-public-key-sm2-key-code] 0474F110 F90F131B B6F6D929 9A23A41E F1AB1666
   ```
   ```
   [*SSH Server-sm2-public-key-sm2-key-code] AC4BE4EE EF2CD876 2B633F80 DD5CF42F 147A722F
   ```
   ```
   [*SSH Server-sm2-public-key-sm2-key-code] DE527F39 247F3744 C23296BE FE3BE502 EEF7D9EC
   ```
   ```
   [*SSH Server-sm2-public-key-sm2-key-code] BC28A576 7E
   ```
   ```
   [*SSH Server-sm2-public-key-sm2-key-code] public-key-code end
   ```
   ```
   [*SSH Server-sm2-public-key] peer-public-key end
   ```
   ```
   [*SSH Server] commit
   ```
4. Bind the SM2 public key of the SSH client to the SSH user client002.
   
   
   ```
   [~SSH Server] ssh user client002 assign sm2-key sm2key001
   ```
   ```
   [*SSH Server] commit
   ```
5. Enable the SFTP service on the SSH server.
   
   
   
   # Enable the SFTP service.
   
   ```
   [~SSH Server] interface LoopBack 0
   ```
   ```
   [~SSH Server-LoopBack0] ip address 10.1.1.1 255.255.255.255
   ```
   ```
   [*SSH Server-LoopBack0] quit
   ```
   ```
   [*SSH Server] sftp server enable
   ```
   ```
   [*SSH Server] ssh server-source -i loopback 0
   ```
   ```
   [*SSH Server] commit
   ```
6. Configure a service type and authorized directory for the SSH users.
   
   
   
   Two SSH users are configured on the SSH server: client001 in password authentication mode and client002 in SM2 authentication mode.
   
   ```
   [*SSH Server] ssh user client001 service-type sftp
   ```
   ```
   [*SSH Server] ssh user client001 sftp-directory cfcard:
   ```
   ```
   [*SSH Server] ssh user client002 service-type sftp
   ```
   ```
   [*SSH Server] ssh user client002 sftp-directory cfcard:
   ```
7. Connect the SFTP clients to the SSH server.
   
   
   
   # For the first login, enable SSH client first-time authentication.
   
   Enable first-time authentication for the client client001.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname client001
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~client001] ssh client first-time enable
   ```
   ```
   [*client001] commit
   ```
   
   Enable first-time authentication for the client client002.
   
   ```
   [~client002] ssh client first-time enable
   ```
   ```
   [*client002] commit
   ```
   
   # Connect the SFTP client client001 to the SSH server in password authentication mode.
   
   ```
   [~client001] sftp 10.1.1.1
   ```
   ```
   Trying 10.1.1.1 ...
   ```
   ```
   Press CTRL+K to abort
   ```
   ```
   Connected to 10.1.1.1 ...      
   ```
   ```
   Please input the username:client001
   ```
   ```
   Enter password:   
   ```
   
   # Connect the SFTP client client002 to the SSH server in SM2 authentication mode.
   
   ```
   [~client002] sftp 10.1.1.1
   ```
   ```
   Trying 10.1.1.1 ...
   ```
   ```
   Press CTRL+K to abort
   ```
   ```
   Connected to 10.1.1.1 ...      
   ```
   ```
   The server is not authenticated. Continue to access it? [Y/N] :y 
   ```
   ```
   Save the server's public key? [Y/N] :y 
   ```
   ```
   The server's public key will be saved with the name 10.1.1.1. Please wait.
   ```
   ```
   Please input the username: client002
   ```
8. Verify the configuration.
   
   
   
   # Check the status of the SSH server.
   
   ```
   [~SSH Server] display ssh server status
   ```
   ```
   SSH Version                                : 2.0
   SSH authentication timeout (Seconds)       : 60
   SSH authentication retries (Times)         : 3
   SSH server key generating interval (Hours) : 0
   SSH version 1.x compatibility              : Enable
   SSH server keepalive                       : Disable
   SFTP IPv4 server                           : Enable
   SFTP IPv6 server                           : Enable
   STELNET IPv4 server                        : Enable
   STELNET IPv6 server                        : Enable
   SNETCONF IPv4 server                       : Enable
   SNETCONF IPv6 server                       : Enable
   SNETCONF IPv4 server port(830)             : Disable
   SNETCONF IPv6 server port(830)             : Disable
   SCP IPv4 server                            : Enable
   SCP IPv6 server                            : Enable
   SSH port forwarding                        : Disable
   SSH IPv4 server port                       : 22
   SSH IPv6 server port                       : 22
   ACL name                                   :
   ACL number                                 :
   ACL6 name                                  : 
   ACL6 number                                :
   SSH server ip-block                        : Enable
   ```
   
   # Check SSH user information.
   
   ```
   [~SSH Server] display ssh user-information
   ```
   ```
   ----------------------------------------------------
   Username                : client001
   Authentication-type     : password
   User-public-key-name    : 
   User-public-key-type    : -
   Sftp-directory          : cfcard:
   Service-type            : sftp
   
   Username                : client002
   Authentication-type     : sm2
   User-public-key-name    : sm2key001
   User-public-key-type    : SM2
   Sftp-directory          : cfcard:
   Service-type            : sftp
   ----------------------------------------------------
   Total 2, 2 printed
   ```

#### Configuration Files

* SSH server configuration file
  
  ```
  #
   sysname SSH Server
  #
  interface GigabitEthernet0/0/0   
   undo shutdown 
   ip address 10.1.1.2 255.255.0.0 
  #
  sm2 peer-public-key sm2key001
  public-key-code begin
      0474F110 F90F131B B6F6D929 9A23A41E F1AB1666
      AC4BE4EE EF2CD876 2B633F80 DD5CF42F 147A722F
      DE527F39 247F3744 C23296BE FE3BE502 EEF7D9EC
      BC28A576 7E
  #
  interface loopback 0
   ip address 10.1.1.1 255.255.255.255
  sftp server enable
  ssh server-source -i loopback 0
  ssh user client001
  ssh user client001 authentication-type password
  ssh user client001 sftp-directory cfcard:
  ssh user client001 service-type sftp
  ssh user client002
  ssh user client002 assign sm2-key sm2key001
  ssh user client002 authentication-type sm2
  ssh authorization-type default root
  ssh user client002 sftp-directory cfcard:
  ssh user client002 service-type sftp
  #
  ssh server cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr 
  ssh server hmac sha2_512 sha2_256 
  ssh server key-exchange dh_group_exchange_sha256
  #
  ssh server publickey rsa_sha2_256 rsa_sha2_512
  #
  ssh server dh-exchange min-len 3072
  #
  ssh client publickey dsa ecc rsa rsa_sha2_256 rsa_sha2_512
  #
  ssh client cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr
  ssh client hmac sha2_512 sha2_256
  ssh client key-exchange dh_group_exchange_sha256
  #
  aaa
   local-user client001 password cipher @%@%UyQs4,KTtSwJo(4QmW#K,LC:@%@%
   local-user client001 level 3
   local-user client001 service-type ssh
  #
  user-interface vty 0 4
   authentication-mode aaa
   protocol inbound ssh
  #
  return
  ```
* SSH client client001 configuration file
  
  ```
  #
   sysname client001
  #
  interface GigabitEthernet0/0/0
   undo shutdown
   ip address 10.1.2.2 255.255.0.0
  #
   ssh client first-time enable
  #
  return
  ```
* SSH client client002 configuration file
  
  ```
  #
   sysname client002
  #
  interface GigabitEthernet0/0/0
   undo shutdown
  ip address 10.1.3.3 255.255.0.0
  #
  ssh client first-time enable
  ssh client assign sm2-host-key sm2key001
  #
  ssh client publickey sm2
  #
  return
  ```