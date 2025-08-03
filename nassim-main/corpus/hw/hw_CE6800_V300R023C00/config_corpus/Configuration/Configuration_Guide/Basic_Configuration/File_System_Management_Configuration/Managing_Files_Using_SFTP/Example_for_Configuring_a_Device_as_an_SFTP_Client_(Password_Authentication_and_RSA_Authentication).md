Example for Configuring a Device as an SFTP Client (Password Authentication and RSA Authentication)
===================================================================================================

Example for Configuring a Device as an SFTP Client (Password Authentication and RSA Authentication)

#### Networking Requirements

The SSH protocol uses encryption to secure the connection between a client and a server. All user authentication, commands, output, and file transfers are encrypted to protect against attacks in the network. A client can securely connect to the SSH server and transfer files using SFTP.

In [Figure 1](#EN-US_TASK_0000001512671490__fig_dc_cfg_file_002501), routes between the SSH server and clients client001 and client002 are reachable. In this example, a Huawei device functions as the SSH server.

The two clients are required to connect to the SSH server in password and RSA authentication modes respectively to ensure secure access to files on the SSH server.

**Figure 1** Network diagram for accessing files on another device using SFTP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001513030662.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Generate a local key pair and enable the SFTP server function on the server so that the server and client can securely exchange data.
2. On the SSH server, configure **client001** and **client002** to access the SSH server in password and RSA authentication modes, respectively.
3. Generate a local key pair on **client002** and configure the RSA public key of **client002** on the SSH server so that the server can authenticate the client when the client attempts to access the server.
4. Configure **client001** and **client002** to connect to the SSH server using SFTP for file access.

#### Procedure

1. On the server, generate a local key pair and enable the SFTP server function.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname SSH Server
   [*HUAWEI] commit
   [~SSH Server] rsa local-key-pair create
   The key name will be:Host_Server 
   The range of public key size is (2048, 4096). 
   NOTE: Key pair generation will take a short while. 
   Please input the modulus [default = 3072]:3072
   [*SSH Server] sftp server enable
   [*SSH Server] ssh server-source all-interface
   [*SSH Server] commit
   ```
2. Configure the public key algorithm, encryption algorithm, key exchange algorithm list, HMAC authentication algorithm, and minimum key length on the SSH server.
   
   
   ```
   [~SSH Server] ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
   [*SSH Server] ssh server hmac sha2_256 sha2_512
   [*SSH Server] ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
   [*SSH Server] ssh server publickey rsa_sha2_256 rsa_sha2_512
   [*SSH Server] ssh server dh-exchange min-len 3072
   [*SSH Server] commit
   ```
3. Create SSH users on the server.
   
   
   
   # Create an SSH user named **client001** and configure the password authentication mode for the user.
   
   ```
   [~SSH Server] ssh user client001
   [*SSH Server] ssh user client001 authentication-type password
   [*SSH Server] ssh user client001 service-type sftp
   [*SSH Server] ssh user client001 sftp-directory flash:/
   [*SSH Server] aaa
   [*SSH Server-aaa] local-user client001 password
   Please configure the login password (8-128) 
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   Info: Add a new user.
   [*SSH Server-aaa] local-user client001 service-type ssh
   [*SSH Server-aaa] local-user client001 privilege level 3
   [*SSH Server-aaa] quit
   [*SSH Server] commit
   ```
   
   # Create an SSH user named **client002** and configure the RSA authentication mode for the user.
   
   ```
   [~SSH Server] ssh user client002
   [*SSH Server] ssh user client002 authentication-type rsa
   [*SSH Server] ssh authorization-type default root
   [*SSH Server] ssh user client002 service-type sftp
   [*SSH Server] ssh user client002 sftp-directory flash:/
   [*SSH Server] commit
   ```
4. Configure the encryption algorithm, HMAC authentication algorithm, key exchange algorithm list, and public key algorithm on **client001**.
   
   
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
5. Generate a local key pair on **client002** and configure the RSA public key of **client002** on the SSH server.
   
   
   
   # Generate a local key pair the client.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname client002
   [*HUAWEI] commit
   [~client002] rsa local-key-pair create        
   The key name will be:Host_Server 
   The range of public key size is (2048, 4096). 
   NOTE: Key pair generation will take a short while. 
   Please input the modulus [default = 3072]:3072
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
   
   # Check the RSA public key on the client.
   
   ```
   [~client002] display rsa local-key-pair public  
   ======================Host key==========================
   Time of Key pair created : 2023-12-27 18:00:55 
   Key Name    : Host 
   Key modulus : 3072 
   Key Type    : RSA Encryption Key
   ========================================================
   Key code:
   3082010A                                                                          02820101                                                                      
       00BBB7A0 4924AF13 04F2662D 2ED43B9D 589967EB                                
       D8A4F785 5AD1F662 13845081 0C65F6B3 88A9C415                                
       D81C34BD 41A4B580 70DC7460 E4A5407B 9B95630F                                
       E211F4B3 1115772D FB95D3DC 915A1858 D0DE49F7                                
       F39DD7A7 7795F2B9 C9562E8B 598CB50F 6D39240D                                
       B5C6F1D3 33A218D0 98C30104 F8F3A8CA 7172C95B                                
       03AEC0A0 8A7E99F6 6C1939AA 52CC2E31 B6703278                                
       AEE1BCD8 DC21FCA2 041C9A4C 1856A935 6894998D                                
       FBFA88FF 1708C3A6 7E092368 ACE983D7 C8DDCDF5                                
       26F5D4E5 16A15C5C D6D0018E 4EAFE055 B93FCB87                                
       2BB46EFB 02C04C3B F167A417 380CD0B0 0BC59493                                
       646CBE96 BCAF3DB7 AD0AFA0A 5D14155E D7F97DC1                                
       32693DE5 4B103442 8E0F4DAD 2598BE5E 19                                      
     0203                                                                          
       010001                                                                                                                                                   
   Key fingerprint:   
      ssh-rsa 3072 47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU
   
   Host public key for PEM format code:                                            
   ---- BEGIN SSH2 PUBLIC KEY ----                                                 
   AAAAB3NzaC1yc2EAAAADAQABAAABAQC7t6BJJK8TBPJmLS7UO51YmWfr2KT3hVrR                
   9mIThFCBDGX2s4ipxBXYHDS9QaS1gHDcdGDkpUB7m5VjD+IR9LMRFXct+5XT3JFa                
   GFjQ3kn3853Xp3eV8rnJVi6LWYy1D205JA21xvHTM6IY0JjDAQT486jKcXLJWwOu                
   wKCKfpn2bBk5qlLMLjG2cDJ4ruG82Nwh/KIEHJpMGFapNWiUmY37+oj/FwjDpn4J                
   I2is6YPXyN3N9Sb11OUWoVxc1tABjk6v4FW5P8uHK7Ru+wLATDvxZ6QXOAzQsAvF                
   lJNkbL6WvK89t60K+gpdFBVe1/l9wTJpPeVLEDRCjg9NrSWYvl4Z                            
   ---- END SSH2 PUBLIC KEY ----                                                   
                                                                                   
   Public key code for pasting into OpenSSH authorized_keys file:                  
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7t6BJJK8TBPJmLS7UO51YmWfr2KT3hVrR9mIThFCB
   DGX2s4ipxBXYHDS9QaS1gHDcdGDkpUB7m5VjD+IR9LMRFXct+5XT3JFaGFjQ3kn3853Xp3eV8rnJVi6L
   WYy1D205JA21xvHTM6IY0JjDAQT486jKcXLJWwOuwKCKfpn2bBk5qlLMLjG2cDJ4ruG82Nwh/KIEHJpM
   GFapNWiUmY37+oj/FwjDpn4JI2is6YPXyN3N9Sb11OUWoVxc1tABjk6v4FW5P8uHK7Ru+wLATDvxZ6QX
   OAzQsAvFlJNkbL6WvK89t60K+gpdFBVe1/l9wTJpPeVLEDRCjg9NrSWYvl4Z== rsa-key            
   ```
   # Configure the RSA public key of the client on the server. (The information in bold in the **display** command output is the RSA public key of the client. Copy the key to the server.)
   ```
   [~SSH Server] rsa peer-public-key rsakey001 encoding-type der
   [*SSH Server-rsa-public-key] public-key-code begin
   [*SSH Server-rsa-public-key-rsa-key-code] 3082010A
   [*SSH Server-rsa-public-key-rsa-key-code] 02820101
   [*SSH Server-rsa-public-key-rsa-key-code] 00BBB7A0 4924AF13 04F2662D 2ED43B9D 589967EB
   [*SSH Server-rsa-public-key-rsa-key-code] D8A4F785 5AD1F662 13845081 0C65F6B3 88A9C415
   [*SSH Server-rsa-public-key-rsa-key-code] D81C34BD 41A4B580 70DC7460 E4A5407B 9B95630F
   [*SSH Server-rsa-public-key-rsa-key-code] E211F4B3 1115772D FB95D3DC 915A1858 D0DE49F7
   [*SSH Server-rsa-public-key-rsa-key-code] F39DD7A7 7795F2B9 C9562E8B 598CB50F 6D39240D
   [*SSH Server-rsa-public-key-rsa-key-code] B5C6F1D3 33A218D0 98C30104 F8F3A8CA 7172C95B
   [*SSH Server-rsa-public-key-rsa-key-code] 03AEC0A0 8A7E99F6 6C1939AA 52CC2E31 B6703278
   [*SSH Server-rsa-public-key-rsa-key-code] AEE1BCD8 DC21FCA2 041C9A4C 1856A935 6894998D
   [*SSH Server-rsa-public-key-rsa-key-code] FBFA88FF 1708C3A6 7E092368 ACE983D7 C8DDCDF5
   [*SSH Server-rsa-public-key-rsa-key-code] 26F5D4E5 16A15C5C D6D0018E 4EAFE055 B93FCB87
   [*SSH Server-rsa-public-key-rsa-key-code] 2BB46EFB 02C04C3B F167A417 380CD0B0 0BC59493
   [*SSH Server-rsa-public-key-rsa-key-code] 646CBE96 BCAF3DB7 AD0AFA0A 5D14155E D7F97DC1
   [*SSH Server-rsa-public-key-rsa-key-code] 32693DE5 4B103442 8E0F4DAD 2598BE5E 19
   [*SSH Server-rsa-public-key-rsa-key-code] 0203
   [*SSH Server-rsa-public-key-rsa-key-code] 010001
   [*SSH Server-rsa-public-key-rsa-key-code] public-key-code end
   [*SSH Server-rsa-public-key] peer-public-key end
   ```
   
   # Bind the **client002** user to the RSA public key of **client002**.
   
   ```
   [*SSH Server] ssh user client002 assign rsa-key rsakey001
   [*SSH Server] commit
   ```
6. Connect SFTP clients to the SSH server.
   
   
   
   # Enable the first login function for the SSH clients.
   
   Enable first login for **client001**.
   
   ```
   [~client001] ssh client first-time enable
   [*client001] commit
   ```
   
   Enable first login for **client002**.
   
   ```
   [~client002] ssh client first-time enable
   [*client002] commit
   ```
   
   # Log in to the SSH server from **client001** in password authentication mode.
   
   ```
   [~client001] sftp 10.1.1.1 
   Trying 10.1.1.1 ...
   Press CTRL+K to abort
   Connected to 10.1.1.1 ...
   The server's public key does not match the one cached before. 
   The server is not authenticated. Continue to access it? [Y/N]:y
   The keyname:10.1.1.1 already exists. Update it? [Y/N]:n  
   
   Please input the username: client001
   Enter password:
   sftp-client>
   ```
   
   # Log in to the SSH server from **client002** in RSA authentication mode.
   
   ```
   [~client002] sftp 10.1.1.1 
   Trying 10.1.1.1 ...
   Press CTRL+K to abort
   Connected to 10.1.1.1 ...
   The server's public key does not match the one cached before. 
   The server is not authenticated. Continue to access it? [Y/N]:y
   The keyname:10.1.1.1 already exists. Update it? [Y/N]:n  
   
   Please input the username: client002
   sftp-client>
   ```

#### Verifying the Configuration

Run the **display ssh server status** command on the SSH server. The command output indicates that the SFTP server function has been enabled. Run the **display ssh user-information** command to check information about SSH users on the server.

# Check the status of the SSH server.

```
[~SSH Server] display ssh server status
SSH Version                                : 2.0
SSH authentication timeout (Seconds)       : 60
SSH authentication retries (Times)         : 3
SSH server key generating interval (Hours) : 0
SSH version 1.x compatibility              : Disable
SSH server keepalive                       : Enable
SFTP IPv4 server                           : Enable
SFTP IPv6 server                           : Enable
STELNET IPv4 server                        : Enable
STELNET IPv6 server                        : Enable
SNETCONF IPv4 server                       : Disable
SNETCONF IPv6 server                       : Disable
SNETCONF IPv4 server port(830)             : Disable
SNETCONF IPv6 server port(830)             : Disable
SCP IPv4 server                            : Enable
SCP IPv6 server                            : Enable
SSH IPv4 server port                       : 22
SSH IPv6 server port                       : 22
ACL name                                   : --
ACL number                                 : --
ACL6 name                                  : --
ACL6 number                                : --
SSH server ip-block                        : Enable
```

# Check information about SSH users.

```
[~SSH Server] display ssh user-information
--------------------------------------------------------------------------------
User Name             : client001
Authentication type   : password
User public key name  : --
User public key type  : --
Sftp directory        : flash:
Service type          : sftp

User Name             : client002
Authentication type   : rsa
User public key name  : --
User public key type  : --
Sftp directory        : flash:
Service type          : sftp
--------------------------------------------------------------------------------
Total 2, 2 printed 
```

#### Configuration Scripts

* SSH server
  
  ```
  #
  sysname SSH Server
  #
  rsa peer-public-key rsakey001 encoding-type der
   public-key-code begin
   3082010A                                                                       
    02820101                                                                      
      00BBB7A0 4924AF13 04F2662D 2ED43B9D 589967EB D8A4F785 5AD1F662 13845081     
      0C65F6B3 88A9C415 D81C34BD 41A4B580 70DC7460 E4A5407B 9B95630F E211F4B3     
      1115772D FB95D3DC 915A1858 D0DE49F7 F39DD7A7 7795F2B9 C9562E8B 598CB50F     
      6D39240D B5C6F1D3 33A218D0 98C30104 F8F3A8CA 7172C95B 03AEC0A0 8A7E99F6     
      6C1939AA 52CC2E31 B6703278 AEE1BCD8 DC21FCA2 041C9A4C 1856A935 6894998D     
      FBFA88FF 1708C3A6 7E092368 ACE983D7 C8DDCDF5 26F5D4E5 16A15C5C D6D0018E     
      4EAFE055 B93FCB87 2BB46EFB 02C04C3B F167A417 380CD0B0 0BC59493 646CBE96     
      BCAF3DB7 AD0AFA0A 5D14155E D7F97DC1 32693DE5 4B103442 8E0F4DAD 2598BE5E     
      19                                                                          
    0203                                                                          
      010001  
   public-key-code end
   peer-public-key end
  #
  aaa
   local-user client001 password irreversible-cipher $1d$g8wLJ`LjL!$CyE(V{3qg5DdU:PM[6=6O$UF-.fQ,Q}>^)OBzgoU$
   local-user client001 service-type ssh
   local-user client001 privilege level 3 
  #
  sftp server enable
  ssh user client001
  ssh user client001 authentication-type password
  ssh user client001 service-type sftp
  ssh user client001 sftp-directory flash:/
  ssh user client002
  ssh user client002 authentication-type rsa 
  ssh user client002 assign rsa-key rsakey001
  ssh user client002 service-type sftp
  ssh user client002 sftp-directory flash:/ 
  ssh authorization-type default root  
  ssh server-source all-interface
  #
  ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
  ssh server hmac sha2_256 sha2_512
  ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
  ssh server publickey rsa_sha2_256 rsa_sha2_512
  ssh server dh-exchange min-len 3072
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