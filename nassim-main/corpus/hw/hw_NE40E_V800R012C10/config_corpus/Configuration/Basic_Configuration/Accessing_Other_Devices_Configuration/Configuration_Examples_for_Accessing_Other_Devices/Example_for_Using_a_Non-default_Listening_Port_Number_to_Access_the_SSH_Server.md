Example for Using a Non-default Listening Port Number to Access the SSH Server
==============================================================================

A non-default listening port number can be configured for the SSH server to allow only authorized users to establish SSH connections with the server.

#### Networking Requirements

The default listening port number is 22. If attackers continuously access this port, bandwidth resources are consumed and performance of the server deteriorates. As a result, authorized users cannot access the server.

If the listening port number of the SSH server is changed to a non-default one, attackers do not know the change and continue to send requests for socket connections to port 22. The SSH server denies the connection requests because the listening port number is incorrect.

Authorized users can set up socket connections with the SSH server by using the new listening port number to implement the following functions: negotiate the version of the SSH protocol, negotiate the algorithm, generate the session key, authenticate, send the session request, and attend the session.

**Figure 1** Using a non-default listening port number to access the SSH server![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents GigabitEthernet0/0/0.


  
![](figure/en-us_image_0241143970.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure users client001 and client002 on the SSH server to use different authentication modes to log in to the SSH server.
2. Configure client002 and the SSH server to generate local key pairs, and bind client002 to the RSA public key of the SSH server to authenticate the client when the client attempts to log in to the server.
3. Enable the STelnet and SFTP server functions on the SSH server.
4. Configure the service type and authorized directory for the SSH users.
5. Configure a non-default listening port number of the SSH server to allow only authorized users to access the server.
6. Use STelnet and SFTP respectively on client001 and client002 to log in to the SSH server.

#### Data Preparation

To complete the configuration, you need the following data:

* Client001: password authentication and STelnet service type
* Client002: RSA authentication (public key: RsaKey001) and SFTP service type
* IP address of the SSH server: 10.1.1.2
* Listening port number of the SSH server: 1025

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
   The key name will be: CE1_Host  
   The range of public key size is (2048, 3072).  
   NOTE: Key pair generation will take a short while.  
   Please input the modulus [default = 3072]:3072
   ```
   ```
   [*SSH Server] commit
   ```
2. Configure the RSA public key on the server.
   
   
   
   # Configure the client to generate a local key pair.
   
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
   [*client002] commit
   ```
   
   # Check the RSA public key generated on the client.
   
   ```
   [~client002] display rsa local-key-pair public
   ```
   ```
   =====================================================
   ```
   ```
   Time of Key pair created: 16:38:51  2007/5/25
   ```
   ```
   Key name: client002_Host
   ```
   ```
   Key type: RSA encryption Key
   ```
   ```
   =====================================================
   ```
   ```
   Key code:
   ```
   ```
   3047
   ```
   ```
     0240
   ```
   ```
       BFF35E4B C61BD786 F907B5DE 7D6770C3 E5FD17AB
   ```
   ```
       203C8FCB BBC8FDF2 F7CB674E 519E8419 0F6B97A8
   ```
   ```
       EA91FC4B B9E18836 5E74BFD5 4C687767 A89C6B43
   ```
   ```
       1D7E3E1B
   ```
   ```
     0203
   ```
   ```
       010001
   ```
   ```
   Host public key for PEM format code:
   ```
   ```
   ---- BEGIN SSH2 PUBLIC KEY ----
   ```
   ```
   AAAAB3NzaC1yc2EAAAADAQABAAAAQQC/815LxhvXhvkHtd59Z3DD5f0XqyA8j8u7
   ```
   ```
   yP3y98tnTlGehBkPa5eo6pH8S7nhiDZedL/VTGh3Z6ica0Mdfj4b
   ```
   ```
   ---- END SSH2 PUBLIC KEY ----
   ```
   ```
   Public key code for pasting into OpenSSH authorized_keys file:
   ```
   ```
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQC/815LxhvXhvkHtd59Z3DD5f0XqyA8j8u7yP3y98tn
   ```
   ```
   TlGehBkPa5eo6pH8S7nhiDZedL/VTGh3Z6ica0Mdfj4b rsa-key
   ```
   ```
   =====================================================
   ```
   ```
   Time of Key pair created: 16:38:51  2007/5/25
   ```
   ```
   Key name: client002_Server
   ```
   ```
   Key type: RSA encryption Key
   ```
   ```
   =====================================================
   ```
   ```
   Key code:
   ```
   ```
   3067
   ```
   ```
     0260
   ```
   ```
       BCFAC085 49A2E70E 1284F901 937D7B63 D7A077AB
   ```
   ```
       D2797280 4BCA86C0 4CD18B70 5DFAC9D3 9A3F3E74
   ```
   ```
       9B2AF4CB 69FA6483 E87DA590 7B47721A 16391E27
   ```
   ```
       1C76ABAB 743C568B 1B35EC7A 8572A096 BCA9DF0E
   ```
   ```
       BC89D3DB 5A83698C 9063DB39 A279DD89
   ```
   ```
     0203
   ```
   ```
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
   [*SSH Server-rsa-key-code] 3047
   ```
   ```
   [*SSH Server-rsa-key-code] 0240
   ```
   ```
   [*SSH Server-rsa-key-code] BFF35E4B C61BD786 F907B5DE 7D6770C3 E5FD17AB
   ```
   ```
   [*SSH Server-rsa-key-code] 203C8FCB BBC8FDF2 F7CB674E 519E8419 0F6B97A8
   ```
   ```
   [*SSH Server-rsa-key-code] EA91FC4B B9E18836 5E74BFD5 4C687767 A89C6B43
   ```
   ```
   [*SSH Server-rsa-key-code] 1D7E3E1B
   ```
   ```
   [*SSH Server-rsa-key-code] 0203
   ```
   ```
   [*SSH Server-rsa-key-code] 010001
   ```
   ```
   [*SSH Server-rsa-key-code] public-key-code end
   ```
   ```
   [*SSH Server-rsa-public-key] peer-public-key end
   ```
   ```
   [*SSH Server-rsa-public-key] commit
   ```
3. Create SSH users on the server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   There are several authentication modes for SSH users: password, RSA, password-RSA, ECC, password-ECC, and All.
   
   * If the authentication mode is password, password-ECC, or password-RSA, configure a local user on the server with the same user name.
   * If the authentication mode is RSA, password-RSA, ECC, password-ECC, or All, save the RSA or ECC public key generated on the SSH client to the server.
   
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
     
     # Create an SSH user named client001 and configure password authentication for the user.
     
     ```
     [~SSH Server] ssh user client001
     ```
     ```
     [*SSH Server] ssh user client001 authentication-type password
     ```
     ```
     [*SSH Server] commit
     ```
     
     # Set a password for **client001**.
     
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
     
     # Set the service type of client001 to STelnet.
     
     ```
     [~SSH Server] ssh user client001 service-type stelnet
     ```
   * Create an SSH user named client002.
     
     # Create an SSH user named client002, configure RSA authentication for the user, and bind the RSA public key to client002.
     
     ```
     [~SSH Server] ssh user client002
     ```
     ```
     [*SSH Server] ssh user client002 authentication-type rsa
     ```
     ```
     [*SSH Server] ssh user client002 assign rsa-key RsaKey001
     ```
     ```
     [*SSH Server] commit
     ```
     
     # Set the service type of client002 to SFTP and configure the authorized directory for the user.
     
     ```
     [~SSH Server] ssh user client002 service-type sftp
     ```
     ```
     [*SSH Server] ssh user client002 sftp-directory cfcard:
     ```
     ```
     [*SSH Server] commit
     ```
4. Enable the STelnet and SFTP server functions on the SSH server.
   
   
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
   [*SSH Server] stelnet server enable
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
5. Configure a new listening port number on the SSH server.
   
   
   ```
   [*SSH Server] ssh server port 1025
   ```
6. Connect the SSH client and the SSH server.
   
   
   
   # If the client logs in to the server for the first time, enable first authentication on the client.
   
   Enable first authentication on client001.
   
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
   
   Enable first authentication on client002.
   
   ```
   [*client002] ssh client first-time enable
   ```
   ```
   [*client002] commit
   ```
   
   # Connect client001 to the SSH server using the new listening port number.
   
   ```
   [~client001] stelnet 10.1.1.1 1025
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
   Connected to 10.1.1.1 ...
   ```
   ```
   The server is not authenticated. Continue to access it?(Y/N):y
   ```
   ```
   Save the server's public key?(Y/N):y
   ```
   ```
   The server's public key will be saved with the name 10.1.1.1. Please wait...
   ```
   ```
   Enter password:   
   ```
   
   The following information indicates that the login is successful:
   
   ```
   Info: The max number of VTY users is 10, and the number
   ```
   ```
         of current VTY users on line is 1.       
   ```
   ```
   <SSH Server>
   ```
   
   # Connect client002 to the SSH server using the new listening port number.
   
   ```
   [~client002] sftp 10.1.1.1 1025
   ```
   ```
   Please input the username:client002
   ```
   ```
   Trying 10.1.1.1 ...
   ```
   ```
   Press CTRL+K to abort
   ```
   ```
   The server is not authenticated. Continue to access it?(Y/N):y
   ```
   ```
   Save the server's public key?(Y/N):y
   ```
   ```
   The server's public key will be saved with the name 10.1.1.1. Please wait.
   ..
   ```
   ```
   sftp-client> 
   ```
7. Verify the configuration.
   
   
   
   Attackers fail to log in to the SSH server using the default listening port number 22.
   
   ```
   [~client002] sftp 10.1.1.1
   ```
   ```
   Please input the username:client002
   ```
   ```
   Trying 10.1.1.1 ...
   ```
   ```
   Press CTRL+K to abort
   ```
   ```
   Error: Failed to connect to the server.      
   ```
   
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
  stelnet server enable
  sftp server enable
  ssh server-source -i loopback 0
  ssh server port 1025
  ssh user client001
  ssh user client001 authentication-type password
  ssh user client001 service-type stelnet
  ssh user client002
  ssh user client002 authentication-type rsa
  ssh user client002 assign rsa-key rsakey001
  ssh user client002 sftp-directory cfcard:
  ssh user client002 service-type sftp
  #
  aaa
   local-user client001 password cipher @%@%UyQs4,KTtSwJo(4QmW#K,LC:@%@%
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
* Client001 configuration file
  
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
* Client002 configuration file
  
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