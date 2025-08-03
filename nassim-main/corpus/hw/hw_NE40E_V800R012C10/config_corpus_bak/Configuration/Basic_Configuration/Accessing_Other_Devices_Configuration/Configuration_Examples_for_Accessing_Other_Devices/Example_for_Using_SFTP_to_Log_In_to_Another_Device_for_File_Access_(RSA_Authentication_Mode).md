Example for Using SFTP to Log In to Another Device for File Access (RSA Authentication Mode)
============================================================================================

To allow an SFTP client to log in to an SSH server, configure the client and server to generate local key pairs, configure the server to generate an RSA public key, and bind the public key to the corresponding user.

#### Networking Requirements

SFTP is a secure service over SSH connections. It allows remote users to log in to a device to manage and transfer files with higher security guarantee. Because the device can function as an SFTP client, you can log in to a remote SSH server from the device to implement secure file transfer.

As shown in [Figure 1](#EN-US_TASK_0172360142__fig_dc_vrp_basic_cfg_011301), after the SFTP service is enabled on the SSH server, the SFTP clients can log in to the SSH server in RSA, DSA, ECC, SM2, X509v3-SSH-RSA, password, password-RSA, password-ECC, password-DSA, password-SM2, password-X509v3-RSA, or all authentication mode for file access.

**Figure 1** Network diagram of using SFTP to log in to another device for file access![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 represents GigabitEthernet0/0/0.


  
![](images/fig_dc_vrp_basic_cfg_011001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure users client001 and client002 on the SSH server to use different authentication modes to log in to the server.
2. Configure the SFTP client client002 and SSH server to generate local key pairs, and bind the RSA public key of the SFTP client to the user client002 so that the client is authenticated when it logs in to the server.
3. Enable the SFTP service on the SSH server.
4. Configure a service type and authorized directory for the SSH users.
5. Configure users client001 and client002 to log in to the SSH server through SFTP for file access.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication mode of the user client001: password authentication
* Authentication mode of the user client002: RSA authentication (public key: rsakey001)
* IP address of the SSH server: 10.1.1.2

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
   [~SSH Server] rsa local-key-pair create
   ```
   ```
   The key name will be: SSH Server_Host  
   The range of public key size is (2048, 3072).  
   NOTE: Key pair generation will take a short while.  
   Please input the modulus [default = 3072]:3072
   ```
2. Create SSH users on the server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   SSH users can be authenticated in password, RSA, password-RSA, ECC, password-ECC, DSA, password-DSA, SM2, password-SM2, or all mode.
   
   * If the authentication mode of an SSH user is password, password-RSA, password-DSA, password-SM2, or password-ECC, a local user with the same name as the SSH user must be configured.
   * If the authentication mode of an SSH user is RSA, password-RSA, DSA, password-DSA, SM2, password-SM2, ECC, password-ECC, or all, the RSA, DSA, SM2, or ECC public key generated on the SSH client needs to be saved to the server.
   
   # Configure VTY user interfaces.
   
   ```
   [~SSH Server] user-interface vty 0 4
   ```
   ```
   [~SSH Server-ui-vty0-4] authentication-mode aaa
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
     
     # Create an SSH user named client002 and configure RSA authentication for it.
     
     ```
     [~SSH Server] ssh user client002
     ```
     ```
     [*SSH Server] ssh user client002 authentication-type rsa
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
3. Configure an RSA public key on the server.
   
   
   
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
   [~client002] rsa local-key-pair create
   ```
   ```
   The key name will be: client002_Host  
   The range of public key size is (2048, 3072).  
   NOTE: Key pair generation will take a short while.  
   Please input the modulus [default = 3072]:3072
   ```
   ```
   [*client002] commit
   ```
   
   # Check the RSA public key generated on the client.
   
   ```
   [~client002] display rsa local-key-pair public
   ```
   ```
   ======================Host Key==========================
   Time of Key pair created : 13:22:1 2010/10/25
   Key Name : client002_Host
   Key Type : RSA Encryption Key
   ========================================================
   Key Code: 
   
   308188
     028180
       B21315DD 859AD7E4 A6D0D9B8 121F23F0 006BB1BB
       A443130F 7CDB95D8 4A4AE2F3 D94A73D7 36FDFD5F
       411B8B73 3CDD494A 236F35AB 9BBFE19A 7336150B
       40A35DE6 2C6A82D7 5C5F2C36 67FBC275 2DF7E4C5
       1987178B 8C364D57 DD0AA24A A0C2F87F 474C7931
       A9F7E8FE E0D5A1B5 092F7112 660BD153 7FB7D5B2
       171896FB 1FFC38CD 
     0203
       010001
   
   Host Public Key for PEM format Code: 
   ---- BEGIN SSH2 PUBLIC KEY ----
   AAAAB3NzaC1yc2EAAAADAQABAAAAgQCyExXdhZrX5KbQ2bgSHyPwAGuxu6RDEw98
   25XYSkri89lKc9c2/f1fQRuLczzdSUojbzWrm7/hmnM2FQtAo13mLGqC11xfLDZn
   +8J1LffkxRmHF4uMNk1X3QqiSqDC+H9HTHkxqffo/uDVobUJL3ESZgvRU3+31bIX
   GJb7H/w4zQ==
   ---- END SSH2 PUBLIC KEY ----
   
   
   Public key code for pasting into OpenSSH authorized_keys file: 
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQCyExXdhZrX5KbQ2bgSHyPwAGuxu6RDEw9825XYSkri
   89lKc9c2/f1fQRuLczzdSUojbzWrm7/hmnM2FQtAo13mLGqC11xfLDZn+8J1LffkxRmHF4uMNk1X3Qqi
   SqDC+H9HTHkxqffo/uDVobUJL3ESZgvRU3+31bIXGJb7H/w4zQ== rsa-key
   
   Host Public key for SSH1 format code: 
   1024 65537 125048203250833642388841080101906750228075076456213955541037945628567
   57310398880086451511608221218821171562865637463140847157102422109476944363593619
   24637760514734544191988044752471924402237145321162849626052751701862381759745461
   33321165741031171160914926309797395278974490949461701171569544048167828558985421
   
   ======================Server Key========================
   Time of Key pair created : 13:22:1 2010/10/25
   Key Name : client002_Server
   Key Type : RSA Encryption Key
   ========================================================
   Key Code: 
                 
   3067
     0260
       BDCEC48F 1EDA55AF 80C71881 CF22D6A4 02682F2F
       E50035C8 E1539F1F 9EB3FCAC 2BFEF147 EEF59F23
       7270C3DD 22135C16 AAC236DE EFBF9865 E50D8D26
       B7651BCB 6D87BC2B 96559C38 04FC034B 54CFE7B3
       2B1BBA18 A96FFC29 EF70069D DD1EE053 
     0203
       010001
   
   ```
   
   # Copy the RSA public key generated on the client to the server.
   
   ```
   [~SSH Server] rsa peer-public-key rsakey001
   ```
   ```
   Enter "RSA public key" view, return system view with "peer-public-key end".
   ```
   ```
   [*SSH Server-rsa-public-key] public-key-code begin
   ```
   ```
   Enter "RSA key code" view, return last view with "public-key-code end".
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] 308188
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] 028180
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] B21315DD 859AD7E4 A6D0D9B8 121F23F0 006BB1BB
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] A443130F 7CDB95D8 4A4AE2F3 D94A73D7 36FDFD5F
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] 411B8B73 3CDD494A 236F35AB 9BBFE19A 7336150B
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] 40A35DE6 2C6A82D7 5C5F2C36 67FBC275 2DF7E4C5
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] 1987178B 8C364D57 DD0AA24A A0C2F87F 474C7931
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] A9F7E8FE E0D5A1B5 092F7112 660BD153 7FB7D5B2
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] 171896FB 1FFC38CD
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] 0203
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] 010001
   ```
   ```
   [*SSH Server-rsa-key-code] public-key-code end
   ```
   ```
   [*SSH Server-rsa-public-key] peer-public-key end
   ```
   ```
   [*SSH Server] commit
   ```
4. Bind the RSA public key of the SSH client to the SSH user client002.
   
   
   ```
   [~SSH Server] ssh user client002 assign rsa-key rsakey001
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
   
   
   
   Two SSH users are configured on the SSH server: client001 in password authentication mode and client002 in RSA authentication mode.
   
   ```
   [~SSH Server] ssh user client001 service-type sftp
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
   ```
   [*SSH Server] commit
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
   [*client002] ssh client first-time enable
   ```
   ```
   [*client002] commit
   ```
   
   # Connect the SFTP client client001 to the SSH server in password authentication mode.
   
   ```
   [~client001] sftp 10.1.1.1
   ```
   ```
   Please input the username:client001
   ```
   ```
   Trying 10.1.1.1 ...
   ```
   ```
   Press CTRL+K to abort
   ```
   ```
   The server is not authenticated. Continue to access it? [Y/N] :y 
   ```
   ```
   Save the server's public key? [Y/N] : y
   ```
   ```
   The server's public key will be saved with the name 10.1.1.1. Please wait
   ```
   ```
   Enter password:   
   ```
   
   # Connect the SFTP client client002 to the SSH server in RSA authentication mode.
   
   ```
   [~client002] sftp 10.1.1.1
   ```
   ```
   Please input the username: client002
   ```
   ```
   Trying 10.1.1.1 ...
   ```
   ```
   Press CTRL+K to abort
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
   User-public-key-name    : -
   Sftp-directory          : cfcard:
   Service-type            : sftp
   
   Username                : client002
   Authentication-type     : rsa
   User-public-key-name    : rsakey001
   Sftp-directory          : -
   Service-type            : sftp
   ----------------------------------------------------
   ```

#### Configuration Files

* SSH server configuration file
  
  ```
  #
   sysname SSH Server
  #
  rsa peer-public-key rsakey001
  public-key-code begin
  308188
    028180
      B21315DD 859AD7E4 A6D0D9B8 121F23F0 006BB1BB A443130F 7CDB95D8 4A4AE2F3
      D94A73D7 36FDFD5F 411B8B73 3CDD494A 236F35AB 9BBFE19A 7336150B 40A35DE6
      2C6A82D7 5C5F2C36 67FBC275 2DF7E4C5 1987178B 8C364D57 DD0AA24A A0C2F87F
      474C7931 A9F7E8FE E0D5A1B5 092F7112 660BD153 7FB7D5B2 171896FB 1FFC38CD
    0203
      010001
  public-key-code end
  peer-public-key end
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
  ssh user client002 assign rsa-key rsakey001
  ssh user client002 authentication-type rsa
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
  interface GigabitEthernet0/0/0
   undo shutdown
   ip address 10.1.1.2 255.255.0.0
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
  #
  return
  ```