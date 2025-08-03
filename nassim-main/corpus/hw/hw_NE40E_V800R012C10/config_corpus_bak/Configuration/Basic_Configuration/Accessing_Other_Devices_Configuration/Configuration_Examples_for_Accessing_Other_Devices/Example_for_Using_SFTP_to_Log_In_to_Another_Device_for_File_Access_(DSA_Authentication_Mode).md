Example for Using SFTP to Log In to Another Device for File Access (DSA Authentication Mode)
============================================================================================

To allow an SFTP client to log in to an SSH server, configure the client and server to generate local key pairs, configure the server to generate a DSA public key, and bind the public key to the corresponding user.

#### Networking Requirements

SFTP is a secure service over SSH connections. It allows remote users to log in to a device to manage and transfer files with higher security guarantee. Because the device can function as an SFTP client, you can log in to a remote SSH server from the device to implement secure file transfer.

As shown in [Figure 1](#EN-US_TASK_0172360143__fig_dc_vrp_basic_cfg_012401), after the SFTP service is enabled on the SSH server, the SFTP clients can log in to the SSH server in RSA, DSA, ECC, SM2, X509v3-SSH-RSA, password, password-RSA, password-ECC, password-DSA, password-SM2, password-X509v3-RSA, or all authentication mode for file access.

**Figure 1** Network diagram of using SFTP to log in to another device for file access![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 represents GigabitEthernet0/0/0.


  
![](figure/en-us_image_0000002146973433.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure users client001 and client002 on the SSH server to use different authentication modes to log in to the server.
2. Configure the SFTP client client002 and SSH server to generate local key pairs, and bind the DSA public key of the SFTP client to the user client002 so that the client is authenticated when it logs in to the server.
3. Enable the SFTP service on the SSH server.
4. Configure a service type and authorized directory for the SSH users.
5. Configure users client001 and client002 to log in to the SSH server through SFTP for file access.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication mode of the user client001: password authentication
* Authentication mode of the user client002: DSA authentication (public key: dsakey001)
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
   [~SSH Server] dsa local-key-pair create
   ```
   ```
   Info: The key name will be: SSH SERVER_Host_DSA
   Info: The key modulus can be any one of the following : 2048.
   Info: Key pair generation will take a short while.
   Info: Generating keys...
   Info: Succeeded in creating the DSA host keys.
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
     [*SSH Server-aaa]local-user client001 password
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
     
     # Create an SSH user named client002 and configure DSA authentication for it.
     
     ```
     [~SSH Server] ssh user client002
     ```
     ```
     [*SSH Server] ssh user client002 authentication-type dsa
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
3. Configure a DSA public key on the server.
   
   
   
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
   [~client002] dsa local-key-pair create
   ```
   ```
   Info: The key name will be: client002_Host_DSA
   Info: The key modulus can be any one of the following : 2048.
   Info: Key pair generation will take a short while.
   Info: Generating keys...
   Info: Succeeded in creating the DSA host keys.
   ```
   ```
   [*client002] commit
   ```
   
   # Check the DSA public key generated on the client.
   
   ```
   [~client002] display dsa local-key-pair public
   ```
   ```
   ========================================================
   Time of Key pair created : 2013-05-21 17:18:17
   Key name    : client002_Host_DSA
   Key modulus : 1024
   Key type    : DSA Encryption Key
   ========================================================
   Key code:
   
   3082019F
     028180
       A49C5EAF 906C80B1 C474CCB0 D47C6965 22DFCF3C
       9602BAD8 FCE8F7E3 7A69BE18 8CB7D858 6B50EEBC
       54BFB089 61A0DD31 5F7F3080 F0DB47E4 ECDCC10E
       7EC18D31 35CD78F7 E002FB6B 4CB59BA5 E2CDB898
       43FAD059 98B8EEA8 E7395FC7 CA9D1655 47927368
       9914AF09 6CFDC125 6CC8A07F DDDE603B F31C4EA4
       0B752AC7 817E877F 
     0214
       CBC5C0BC 2D7B6DFE 15A7F9A3 6F6ED15B 6ECC9F27
     028180
       6D3202E7 4DCAC5DB 97034305 8D79FDB2 76D5CAA2
       C8D00C3D 666F61D4 F2E36445 4027FD04 0D61B2A3
       AF3CED6B C36CC68D E8DF35F9 FAF802ED 73BCBD66
       C55AE0F6 69530C14 1B33A5A1 CF77D636 75A5EF3B
       264AB66E 2A8CFFB1 690E45F8 6FACF1B3 E2A11328
       C14BA7F3 CA0D198B 3ED94368 45BA5E89 F1ADB79E
       F459F826 B9A5CF6D 
     028180
       409C0AE7 1DDDDA8C F3924608 DC32728C D6FA51FB
       B4933D03 E30780E1 676AA9EE E3A9B677 97DB1D3A
       57AF479C 3BDC4096 291B4548 43D88851 DCFEB04D
       593F1459 9145FB0B 071CEEE5 5F951E64 CA6C4C16
       6192B926 9AD8764E E9F8661C 8EC08D08 BD83BCE3
       E054EE39 20207689 433B07A1 1219B9F3 945E88F0
       3A8FC0FB 9883905B 
   
   Host public Key for PEM format Code:
   ---- BEGIN SSH2 PUBLIC KEY ----
   AAAAB3NzaC1kc3MAAACBAKScXq+QbICxxHTMsNR8aWUi3888lgK62Pzo9+N6ab4Y
   jLfYWGtQ7rxUv7CJYaDdMV9/MIDw20fk7NzBDn7BjTE1zXj34AL7a0y1m6XizbiY
   Q/rQWZi47qjnOV/Hyp0WVUeSc2iZFK8JbP3BJWzIoH/d3mA78xxOpAt1KseBfod/
   AAAAFQDLxcC8LXtt/hWn+aNvbtFbbsyfJwAAAIBtMgLnTcrF25cDQwWNef2ydtXK
   osjQDD1mb2HU8uNkRUAn/QQNYbKjrzzta8Nsxo3o3zX5+vgC7XO8vWbFWuD2aVMM
   FBszpaHPd9Y2daXvOyZKtm4qjP+xaQ5F+G+s8bPioRMowUun88oNGYs+2UNoRbpe
   ifGtt570WfgmuaXPbQAAAIBAnArnHd3ajPOSRgjcMnKM1vpR+7STPQPjB4DhZ2qp
   7uOptneX2x06V69HnDvcQJYpG0VIQ9iIUdz+sE1ZPxRZkUX7Cwcc7uVflR5kymxM
   FmGSuSaa2HZO6fhmHI7AjQi9g7zj4FTuOSAgdolDOwehEhm585ReiPA6j8D7mIOQ
   Ww==
   ---- END SSH2 PUBLIC KEY ----
   
   Public key code for pasting into OpenSSH authorized_keys file:
   ssh-dss AAAAB3NzaC1kc3MAAACBAKScXq+QbICxxHTMsNR8aWUi3888lgK62Pzo9+N6ab4YjLfYWGtQ7rxUv7CJYaDdMV9/MIDw20fk7NzBDn7BjTE1zXj34AL7a0y1m6XizbiYQ/rQWZi47qjnOV/Hyp0WVUeSc2iZFK8JbP3BJWzIoH/d3mA78xxOpAt1KseBfod/AAAAFQDLxcC8LXtt/hWn+aNvbtFbbsyfJwAAAIBtMgLnTcrF25cDQwWNef2ydtXKosjQDD1mb2HU8uNkRUAn/QQNYbKjrzzta8Nsxo3o3zX5+vgC7XO8vWbFWuD2aVMMFBszpaHPd9Y2daXvOyZKtm4qjP+xaQ5F+G+s8bPioRMowUun88oNGYs+2UNoRbpeifGtt570WfgmuaXPbQAAAIBAnArnHd3ajPOSRgjcMnKM1vpR+7STPQPjB4DhZ2qp7uOptneX2x06V69HnDvcQJYpG0VIQ9iIUdz+sE1ZPxRZkUX7Cwcc7uVflR5kymxMFmGSuSaa2HZO6fhmHI7AjQi9g7zj4FTuOSAgdolDOwehEhm585ReiPA6j8D7mIOQWw== dsa-key
   
   ```
   
   # Copy the DSA public key generated on the client to the server.
   
   ```
   [~SSH Server] dsa peer-public-key dsakey001 encoding-type der
   Info: Enter "DSA public key" view, return system view with "peer-public-key end".
   ```
   ```
   [*SSH Server-dsa-public-key] public-key-code begin
   Info: Enter "DSA key code" view, return last view with "public-key-code end".
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 3082019F
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 028180
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] A49C5EAF 906C80B1 C474CCB0 D47C6965 22DFCF3C
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 9602BAD8 FCE8F7E3 7A69BE18 8CB7D858 6B50EEBC
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 54BFB089 61A0DD31 5F7F3080 F0DB47E4 ECDCC10E
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 7EC18D31 35CD78F7 E002FB6B 4CB59BA5 E2CDB898
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 43FAD059 98B8EEA8 E7395FC7 CA9D1655 47927368
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 9914AF09 6CFDC125 6CC8A07F DDDE603B F31C4EA4
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 0B752AC7 817E877F
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 0214
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] CBC5C0BC 2D7B6DFE 15A7F9A3 6F6ED15B 6ECC9F27
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 028180
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 6D3202E7 4DCAC5DB 97034305 8D79FDB2 76D5CAA2
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] C8D00C3D 666F61D4 F2E36445 4027FD04 0D61B2A3
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] AF3CED6B C36CC68D E8DF35F9 FAF802ED 73BCBD66
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] C55AE0F6 69530C14 1B33A5A1 CF77D636 75A5EF3B
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 264AB66E 2A8CFFB1 690E45F8 6FACF1B3 E2A11328
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] C14BA7F3 CA0D198B 3ED94368 45BA5E89 F1ADB79E
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] F459F826 B9A5CF6D
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 028180
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 409C0AE7 1DDDDA8C F3924608 DC32728C D6FA51FB
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] B4933D03 E30780E1 676AA9EE E3A9B677 97DB1D3A
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 57AF479C 3BDC4096 291B4548 43D88851 DCFEB04D
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 593F1459 9145FB0B 071CEEE5 5F951E64 CA6C4C16
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 6192B926 9AD8764E E9F8661C 8EC08D08 BD83BCE3
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] E054EE39 20207689 433B07A1 1219B9F3 945E88F0
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] 3A8FC0FB 9883905B
   ```
   ```
   [*SSH Server-dsa-public-key-dsa-key-code] public-key-code end
   ```
   ```
   [*SSH Server-dsa-public-key] peer-public-key end
   ```
   ```
   [*SSH Server] commit
   ```
4. Bind the DSA public key of the SSH client to the SSH user client002.
   
   
   ```
   [~SSH Server] ssh user client002 assign dsa-key dsakey001
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
   
   
   
   Two SSH users are configured on the SSH server: client001 in password authentication mode and client002 in DSA authentication mode.
   
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
   
   # Connect the SFTP client client002 to the SSH server in DSA authentication mode.
   
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
   User Name               : client001
   Authentication-Type     : password
   User-public-key-name    : -
   User-public-key-type    : -
   Sftp-directory          : cfcard:
   Service-type            : sftp
   
   User Name               : client002
   Authentication-Type     : dsa
   User-public-key-name    : -
   User-public-key-type    : -
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
  dsa peer-public-key dsakey001
  public-key-code begin
  3082019F
    028180
      A49C5EAF 906C80B1 C474CCB0 D47C6965 22DFCF3C
      9602BAD8 FCE8F7E3 7A69BE18 8CB7D858 6B50EEBC
      54BFB089 61A0DD31 5F7F3080 F0DB47E4 ECDCC10E
      7EC18D31 35CD78F7 E002FB6B 4CB59BA5 E2CDB898
      43FAD059 98B8EEA8 E7395FC7 CA9D1655 47927368
      9914AF09 6CFDC125 6CC8A07F DDDE603B F31C4EA4
      0B752AC7 817E877F 
    0214
      CBC5C0BC 2D7B6DFE 15A7F9A3 6F6ED15B 6ECC9F27
    028180
      6D3202E7 4DCAC5DB 97034305 8D79FDB2 76D5CAA2
      C8D00C3D 666F61D4 F2E36445 4027FD04 0D61B2A3
      AF3CED6B C36CC68D E8DF35F9 FAF802ED 73BCBD66
      C55AE0F6 69530C14 1B33A5A1 CF77D636 75A5EF3B
      264AB66E 2A8CFFB1 690E45F8 6FACF1B3 E2A11328
      C14BA7F3 CA0D198B 3ED94368 45BA5E89 F1ADB79E
      F459F826 B9A5CF6D 
    028180
      409C0AE7 1DDDDA8C F3924608 DC32728C D6FA51FB
      B4933D03 E30780E1 676AA9EE E3A9B677 97DB1D3A
      57AF479C 3BDC4096 291B4548 43D88851 DCFEB04D
      593F1459 9145FB0B 071CEEE5 5F951E64 CA6C4C16
      6192B926 9AD8764E E9F8661C 8EC08D08 BD83BCE3
      E054EE39 20207689 433B07A1 1219B9F3 945E88F0
      3A8FC0FB 9883905B 
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
  ssh user client002 assign dsa-key dsakey001
  ssh user client002 authentication-type dsa
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