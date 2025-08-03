Example for Configuring a Device as an SFTP Server (IPv4)
=========================================================

Example for Configuring a Device as an SFTP Server (IPv4)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513030650__fig12144153491016), PC1 connects to the device at 10.1.1.5. Files need to be securely transferred between PC1 and the device. To ensure secure file transfer, the device needs to be configured as an SSH server to provide the SFTP service, so that the SSH server can authenticate the client (PC1) and bidirectional data is encrypted. In addition, an ACL policy needs to be configured so that only PC1 can access the SSH server.

**Figure 1** Network diagram for performing file operations using SFTP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001955564514.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Generate a local key pair and enable the SFTP server function on the SSH server so that the server and client can securely exchange data.
2. Configure SSH user information including the authentication mode, service type, authorized directory, user name, and password.
3. Configure access permissions on the SSH server to control access from SSH users.
4. Connect to the SSH server from the PC using the third-party software OpenSSH.

#### Procedure

1. Configure an IP address for the SSH server.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname SSH Server
   [*HUAWEI] commit
   [*SSH Server] interface 100ge 1/0/1
   [~SSH Server-100GE1/0/1] undo portswitch
   [*SSH Server-100GE1/0/1] ip address 10.1.1.5 255.255.255.0
   [*SSH Server-100GE1/0/1] quit
   [*SSH Server] commit
   ```
2. On the SSH server, generate a local key pair and enable the SFTP server function.
   
   
   ```
   [~SSH Server] rsa local-key-pair create
   The key name will be:Host_Server 
   The range of public key size is (2048, 4096). 
   NOTE: Key pair generation will take a short while. 
   Please input the modulus [default = 3072]:3072
   [*SSH Server] sftp server enable
   [*SSH Server] ssh server-source all-interface
   [*SSH Server] commit
   ```
3. Configure the public key algorithm, encryption algorithm, key exchange algorithm list, HMAC authentication algorithm, and minimum key length on the SSH server.
   
   
   ```
   [~SSH Server] ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
   [*SSH Server] ssh server hmac sha2_256 sha2_512
   [*SSH Server] ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
   [*SSH Server] ssh server publickey rsa_sha2_256 rsa_sha2_512
   [*SSH Server] ssh server dh-exchange min-len 3072
   [*SSH Server] commit
   ```
4. Configure SSH user information including the authentication mode, service type, authorized directory, user name, and password.
   
   
   ```
   [~SSH Server] ssh user client001 authentication-type password
   Info: Succeeded in adding a new SSH user. 
   [*SSH Server] ssh user client001 service-type sftp
   [*SSH Server] ssh user client001 sftp-directory flash:/
   [*SSH Server] aaa
   [*SSH Server-aaa] local-user client001 password
   Please configure the login password (8-128)
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   Info: Add a new user.
   [*SSH Server-aaa] local-user client001 privilege level 3
   [*SSH Server-aaa] local-user client001 service-type ssh
   [*SSH Server-aaa] quit
   [*SSH Server] commit
   ```
5. Configure access permissions on the SSH server.
   
   
   ```
   [~SSH Server] acl 2001
   [*SSH Server-acl4-basic-2001] rule permit source 10.1.1.1 0
   [*SSH Server-acl4-basic-2001] rule deny source 10.1.1.2 0
   [*SSH Server-acl4-basic-2001] quit
   [*SSH Server] ssh server acl 2001
   [*SSH Server] commit
   ```

#### Verifying the Configuration

Connect to the SSH server from the PC using the third-party software OpenSSH.

The Windows CLI can identify OpenSSH commands only when OpenSSH is installed on the terminal.

```
C:/Documents and Settings/Administrator> sftp client001@10.1.1.5
Connecting to 10.1.1.5...
The authenticity of host "10.1.1.5 (10.1.1.5)" can't be established.
DSA key fingerprint is 0d:48:82:fd:2f:52:1c:f0:c4:22:70:80:8f:7b:fd:78.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added "10.1.1.5" (DSA) to the list of known hosts.
client001@10.1.1.5's password:
sftp>
```

After you connect to the SSH server using the third-party software, the SFTP view is displayed. You can then perform file operations in the SFTP view.


#### Configuration Scripts

```
#
sysname SSH Server
#
acl number 2001
 rule 5 permit source 10.1.1.1 0
 rule 10 deny source 10.1.1.2 0
#
aaa
 local-user client001 password irreversible-cipher $1d$v!=.5/:(q-$xL=\K+if"'S}>k7vGP5$_ox0B@ys7.'DBHL~3*aN$
 local-user client001 service-type ssh
 local-user client001 privilege level 3
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.1.5 255.255.255.0
#
sftp server enable
ssh server-source all-interface
ssh server acl 2001
ssh user client001
ssh user client001 authentication-type password
ssh user client001 service-type sftp
ssh user client001 sftp-directory flash:
#
ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
ssh server hmac sha2_256 sha2_512
ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
ssh server publickey rsa_sha2_256 rsa_sha2_512
ssh server dh-exchange min-len 3072
#
return
```