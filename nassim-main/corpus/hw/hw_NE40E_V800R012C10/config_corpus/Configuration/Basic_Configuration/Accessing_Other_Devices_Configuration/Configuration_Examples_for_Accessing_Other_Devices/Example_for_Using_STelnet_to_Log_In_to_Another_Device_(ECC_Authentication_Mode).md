Example for Using STelnet to Log In to Another Device (ECC Authentication Mode)
===============================================================================

This section provides an example for using STelnet to log in to another device. To allow an STelnet client to log in to an SSH server, configure the client and server to generate local key pairs, configure the server to generate an ECC public key, and bind the public key to the corresponding user.

#### Networking Requirements

Large numbers of devices need to be managed and maintained on a network. You cannot connect each device to a terminal. When no reachable route exists between remote devices and a terminal, you can use Telnet to log in to the remote devices from the device that you have logged in to. Telnet provides no secure authentication mode, and data is transmitted in simple mode over TCP, which brings security risks.

STelnet is a secure Telnet service over SSH connections. SSH provides encryption and authentication and protects devices against attacks, such as IP spoofing. As shown in [Figure 1](#EN-US_TASK_0172360133__fig_dc_vrp_basic_cfg_011001), after the STelnet service is enabled on the SSH server, the STelnet clients can log in to the SSH server in RSA, DSA, ECC, SM2, X509v3-SSH-RSA, password, password-RSA, password-ECC, password-DSA, password-SM2, password-X509v3-RSA, or all authentication mode.

**Figure 1** Network diagram of using STelnet to log in to another device![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 represents GigabitEthernet0/0/0.


  
![](figure/en-us_image_0000002111411298.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure users client001 and client002 on the SSH server to use different authentication modes to log in to the server.
2. Configure the STelnet client client002 and SSH server to generate local key pairs, and bind the ECC public key of the STelnet client to the user client002 so that the client is authenticated when it logs in to the server.
3. Enable the STelnet service on the SSH server.
4. Set the service type of the SSH users client001 and client002 to STelnet.
5. Enable SSH client first-time authentication.
6. Configure users client001 and client002 to log in to the SSH server using STelnet.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication mode of the user client001: password authentication
* Authentication mode of the user client002: ECC authentication (public key: Ecckey001)
* IP address of the SSH server: 10.1.1.1

#### Procedure

1. Configure the server to generate a local key pair.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname SSH Server
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~SSH Server] ecc local-key-pair create
   ```
   ```
   Info: The key name will be: SSH Server_Host_ECC
   Info: The key modulus can be any one of the following: 256, 384, 521.
   Info: Key pair generation will take a short while.
   Please input the modulus [default=521]:521
   Info: Generating keys...
   Info: Succeeded in creating the ECC host keys.
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
   [*SSH Server-ui-vty0-4] user privilege level 3
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
     [*SSH Server-aaa] commit
     ```
     ```
     [~SSH Server-aaa] quit
     ```
   * Create an SSH user named client002.
     
     # Create an SSH user named client002 and configure ECC authentication for it.
     
     ```
     [~SSH Server] ssh user client002
     ```
     ```
     [*SSH Server] ssh user client002 authentication-type ecc
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
3. Configure an ECC public key on the server.
   
   
   
   # Configure the client client002 to generate a local key pair.
   
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
   [~client002] ecc local-key-pair create
   ```
   ```
   Info: The key name will be: client002_Host_ECC
   Info: The key modulus can be any one of the following: 256, 384, 521.
   Info: Key pair generation will take a short while.
   Please input the modulus [default=521]:521
   Info: Generating keys...
   Info: Succeeded in creating the ECC host keys.
   ```
   ```
   [*client002] commit
   ```
   
   # Check the ECC public key generated on the client.
   
   ```
   [~client002] display ecc local-key-pair public
   ```
   ```
   ======================Host Key==========================
   Time of Key pair created : 2013-01-22 10:33:06
   Key Name : client002_Host_ECC
   Key Type : ECC Encryption Key
   ========================================================
   Key Code:                                                                                                                           
     04D7635B C047B02E 20C1E6CB E04B5E5C 7DCADD88                                                                                      
     F676AB0E C91ACB3C B0394B18 FA29E5C2 0426F924                                                                                      
     DAD9AA02 C531E5ED C6783FFA 41235A16 8D7723E0                                                                                      
     7E63D68D E7  
   
   Host Public Key for PEM format Code:
   ---- BEGIN SSH2 PUBLIC KEY ----
   AAAAE2VjZHNhLXNoYTItbmlzdHAxOTIAAABBBL+PCqbAEJKKKUpCYdSfyiyY5Iq3
   DM9ZB3mjx62wShmmNMiZJAV+02aMJ6CsHBuWCbVLO/Zg8Ng3kGXC4ltmLXM=
   ---- END SSH2 PUBLIC KEY ----
   ```
   
   # Copy the ECC public key generated on the client to the server.
   
   ```
   [~SSH Server] ecc peer-public-key Ecckey001
   Enter "ECC public key" view, return system view with "peer-public-key end".
   ```
   ```
   [*SSH Server-ecc-public-key] public-key-code begin
   Enter "ECC key code" view, return last view with "public-key-code end".
   ```
   ```
   [*SSH Server-ecc-public-key-ecc-key-code] 04BF8F0A A6C01092 8A294A42 61D49FCA 2C98E48A
   ```
   ```
   [*SSH Server-ecc-public-key-ecc-key-code] B70CCF59 0779A3C7 ADB04A19 A634C899 24057ED3
   ```
   ```
   [*SSH Server-ecc-public-key-ecc-key-code] 668C27A0 AC1C1B96 09B54B3B F660F0D8 379065C2
   ```
   ```
   [*SSH Server-ecc-public-key-ecc-key-code] E25B662D 73
   ```
   ```
   [*SSH Server-ecc-public-key-ecc-key-code] public-key-code end
   ```
   ```
   [*SSH Server-ecc-public-key] peer-public-key end
   ```
   ```
   [*SSH Server] commit
   ```
4. Bind the ECC public key of the SSH client to the SSH user client002.
   
   
   ```
   [~SSH Server] ssh user client002 assign ecc-key ecckey001
   ```
   ```
   [*SSH Server] commit
   ```
5. Enable the STelnet service on the SSH server.
   
   
   
   # Enable the STelnet service.
   
   ```
   [~SSH Server] stelnet server enable
   ```
   ```
   [*SSH Server] ssh server-source -i GigabitEthernet0/0/0
   ```
   ```
   [*SSH Server] commit
   ```
6. Set the service type of the SSH users client001 and client002 to STelnet.
   
   
   ```
   [*SSH Server] ssh user client001 service-type stelnet
   ```
   ```
   [*SSH Server] ssh user client002 service-type stelnet
   ```
   ```
   [*SSH Server] commit
   ```
7. Connect the STelnet clients to the SSH server.
   
   
   
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
   
   # Connect the STelnet client client001 to the SSH server in password authentication mode by entering the username and password.
   
   ```
   <~client001> stelnet 10.1.1.1
   ```
   ```
   Trying 10.1.1.1 ...
   Press CTRL+K to abort
   Connected to 10.1.1.1 ...
   Please input the username:client001
   Enter password:   
   ```
   
   The following information indicates that the login is successful:
   
   ```
   Info: The max number of VTY users is 20, and the number
         of current VTY users on line is 6.
         The current login time is 2011-01-06 11:42:42.
         First login successfully.
   ```
   ```
   <SSH Server>
   ```
   
   # Connect the STelnet client client002 to the SSH server in ECC authentication mode.
   
   ```
   <~client002> stelnet 10.1.1.1
   ```
   ```
   Trying 10.1.1.1 ...
   Press CTRL+K to abort
   Connected to 10.1.1.1 ...      
   The server is not authenticated. Continue to access it?(Y/N):y
   Save the server's public key?(Y/N):y
   The server's public key will be saved with the name 10.1.1.1. Please wait...    
   Please input the username: client002
   Info: The max number of VTY users is 20, and the number
         of current VTY users on line is 6.
         The current login time is 2011-01-06 11:42:42.
   
   ```
   ```
   <SSH Server>
   ```
   
   If the login succeeds, the user view is displayed. If the login fails, the "Session is disconnected" message is displayed.
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
   Sftp-directory          : -
   Service-type            : stelnet
   
   Username                : client002
   Authentication-type     : ecc
   User-public-key-name    : ecckey001
   User-public-key-type    : ECC
   Sftp-directory          : -
   Service-type            : stelnet
   ----------------------------------------------------
   Total 2, 2 printed
   ```

#### Configuration Files

* SSH server configuration file
  
  ```
  #
   sysname SSH Server
  #
  ecc peer-public-key ecckey001
  public-key-code begin
      04BF8F0A A6C01092 8A294A42 61D49FCA 2C98E48A
      B70CCF59 0779A3C7 ADB04A19 A634C899 24057ED3
      668C27A0 AC1C1B96 09B54B3B F660F0D8 379065C2
      E25B662D 73
  public-key-code end
  peer-public-key end
  #
  stelnet server enable
  ssh server-source -i GigabitEthernet0/0/0
  ssh user client001
  ssh user client001 authentication-type password
  ssh user client001 service-type stelnet
  ssh user client002
  ssh user client002 assign ecc-key ecckey001
  ssh user client002 authentication-type ecc
  ssh authorization-type default root
  ssh user client002 service-type stelnet
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
   local-user client001 service-type ssh
   #
  user-interface vty 0 4
   authentication-mode aaa
   protocol inbound ssh
   user privilege level 3
  #
  return
  ```
* SSH client client001 configuration file
  
  ```
  #
   sysname client001
  #
  interface GigabitEthernet0/0/0
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
   ip address 10.1.3.3 255.255.0.0
  #
  ssh client first-time enable
  #
  return
  ```