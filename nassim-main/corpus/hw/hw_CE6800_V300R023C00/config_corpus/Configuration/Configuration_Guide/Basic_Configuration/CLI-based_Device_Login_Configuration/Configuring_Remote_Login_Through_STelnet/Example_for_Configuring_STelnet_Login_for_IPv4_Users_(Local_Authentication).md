Example for Configuring STelnet Login for IPv4 Users (Local Authentication)
===========================================================================

Example for Configuring STelnet Login for IPv4 Users (Local Authentication)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513173042__fig_dc_cfg_login_001601), after the STelnet server function is enabled on the device functioning as the SSH server, the PC functioning as the SSH client can connect to the SSH server in different authentication modes. This section uses the RSA authentication mode as an example to describe how to log in to the SSH server using STelnet.

To improve system security and prevent unauthorized users from logging in to the SSH server, you can configure an ACL rule on the SSH server.

**Figure 1** Network diagram of STelnet login  
![](figure/en-us_image_0000001564013293.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set an IP address of the management interface for the SSH server.
2. Configure the SSH server to generate a local key pair.
3. Configure a VTY user interface on the SSH server.
4. Create a local user and configure the user access type.
5. Create an SSH user and configure the authentication mode for the user.
6. On the SSH client, create a key pair based on the configured SSH user authentication mode and copy the public key to the SSH server.
7. On the SSH server, edit the public key and assign it to the user.
8. Enable STelnet on the SSH server and set the service type of the SSH user to STelnet.
9. On the SSH server, configure an ACL to allow access from the STelnet client.
10. Set parameters for STelnet login to the server.

#### Data Preparation

To complete the configuration, ensure that the following configurations have been completed:

![](public_sys-resources/note_3.0-en-us.png) 

To ensure high security, you are advised to use the RSA key pair whose length is 3072 bits or longer.

* OpenSSH has been installed on the SSH client.
* The IP address of the management interface for the SSH server is 10.248.103.194/24.
* The local user's authentication mode is set to password authentication, and the user name and password are admin123 and YsHsjx\_202206, respectively.
* The SSH user's authentication mode is RSA.
* ACL 2000 is configured to allow the clients on the network segment 10.248.103.0/24 to access the SSH server.

#### Procedure

1. Set an IP address of the management interface for the SSH server.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname SSH Server
   [*HUAWEI] commit
   [~SSH Server] interface meth 0/0/0
   [~SSH Server-MEth0/0/0] ip address 10.248.103.194 255.255.255.0
   [*SSH Server-MEth0/0/0] quit
   [*SSH Server] commit
   ```
2. Configure the SSH server to generate a local key pair.
   
   
   ```
   [~SSH Server] rsa local-key-pair create
   The key name will be:Host
   The range of public key size is (2048, 4096).
   NOTE: Key pair generation will take a short while.
   Please input the modulus [default = 3072]:3072
   [*SSH Server] commit
   ```
3. Configure a VTY user interface on the SSH server.
   
   
   ```
   [~SSH Server] user-interface vty 0 4
   [~SSH Server-ui-vty0-4] authentication-mode aaa
   [*SSH Server-ui-vty0-4] protocol inbound ssh
   [*SSH Server-ui-vty0-4] quit
   [*SSH Server] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If SSH is configured as the login protocol, the device automatically disables the Telnet function.
4. On the server, create a local user and configure the user access type.
   
   
   ```
   [~SSH Server] aaa
   [~SSH Server-aaa] local-user admin123 password
   Please configure the login password (8-128)
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   [*SSH Server-aaa] local-user admin123 service-type ssh
   [*SSH Server-aaa] local-user admin123 privilege level 3
   [*SSH Server-aaa] quit
   [*SSH Server] commit
   ```
5. Create an SSH user on the server and configure the authentication mode for the user.
   
   
   ```
   [~SSH Server] ssh user admin123
   [*SSH Server] ssh user admin123 authentication-type rsa
   [*SSH Server] commit
   ```
6. Configure the public key algorithm, encryption algorithm, key exchange algorithm list, HMAC authentication algorithm, and minimum key length on the SSH server.
   
   
   ```
   [~SSH Server] ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
   [*SSH Server] ssh server hmac sha2_256 sha2_512
   [*SSH Server] ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
   [*SSH Server] ssh server publickey rsa_sha2_256 rsa_sha2_512
   [*SSH Server] ssh server dh-exchange min-len 3072
   [*SSH Server] commit
   ```
7. Use OpenSSH to create an RSA key pair on the SSH client and copy the public key to the SSH server.
   
   
   
   Access the Windows CLI, create an RSA key pair, and save it to the local **id\_rsa.pub** file. (The following information is for reference only.)
   
   
   
   ```
   C:\Users\User1> ssh-keygen -t rsa
   Generating public/private rsa key pair.
   Enter file in which to save the key (C:\Users\User1/.ssh/id_rsa):
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
   Your identification has been saved in C:\Users\User1/.ssh/id_rsa.
   Your public key has been saved in C:\Users\User1/.ssh/id_rsa.pub.
   The key fingerprint is:
   SHA256:c43yubJjCUjY3JqH0aVZwJFM3gWJcH4YI5+4HUDAIqo 
   The key's randomart image is:
   +---[RSA 3072]----+
   | ..o==B=.o.      |
   |o .  O=*+.       |
   |o. +.oB=o        |
   |. . =o=o   o     |
   |.  ..*. S o .    |
   |E   = o  = .     |
   |     . . .o      |
   |        =  .     |
   |       ..+.      |
   +----[SHA256]-----+
   ```
8. On the SSH server, edit the public key generated using OpenSSH on the SSH client and assign it to the user.
   
   
   ```
   [~SSH Server] rsa peer-public-key rsa01 encoding-type openssh
   [*SSH Server-rsa-public-key] public-key-code begin
   [*SSH Server-rsa-public-key-rsa-key-code] ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCg5Ag490i6ilB7QuCVb35B8RJEh1DIYB88h2p1qjdh7qdMQv8rpJaVAgQWxwzKZO0XdFuz4ReGQzTCSf7Det7Ajicddw3qi+6P8hRqZj6MPdLg/o3RN4aPCfr/LFWCwqJ3gWGHlOC7qqjRk+6pySVoiWcSk5/elBkU7WVk/cSWrt4qFXJV373OCesKcEVeDvAa1Tvx6L3LQroBqUO0EXzDgOthPCmOqiqvS5h3JipzqVsesdSKjeInooCQzSOv5eePpBcFcIvU6wFiLIZ5vnf6YtypgTVzHuje/sh4xM7Iuuon7AYXKHT8NpO9jd9zA/lKaRPXyDtei1O1Bt/5lxnn 
   [*SSH Server-rsa-public-key-rsa-key-code] public-key-code end
   [*SSH Server-rsa-public-key] peer-public-key end
   [*SSH Server] ssh user admin123 assign rsa-key rsa01
   [*SSH Server] commit
   ```
9. Enable the STelnet function and set the user service type to STelnet.
   
   
   ```
   [~SSH Server] stelnet server enable
   [*SSH Server] ssh server-source all-interface
   [*SSH Server] ssh user admin123 service-type stelnet
   [*SSH Server] commit
   ```
10. Configure an ACL rule. 
    
    
    ```
    [~SSH Server] acl 2000
    [*SSH Server-acl4-basic-2000] rule permit source 10.248.103.0 24
    [*SSH Server-acl4-basic-2000] quit
    [*SSH Server] ssh server acl 2000
    [*SSH Server] commit
    ```
    ![](public_sys-resources/note_3.0-en-us.png) 
    * You can determine whether to configure ACL rules as required.
    * If the management interface is bound to the VPN instance **\_management\_vpn\_ by default**, the command for creating an ACL rule is as follows: **rule permit vpn-instance \_management\_vpn\_ source 10.248.103.0 24**

#### Verifying the Configuration

Use OpenSSH to log in to the SSH server from the client. Access the Windows CLI and run the OpenSSH commands to access the device using STelnet.

```
C:\Users\User1> ssh admin123@10.248.103.194
Enter passphrase for key 'C:\Users\User/.ssh/id_rsa':
Info: The max number of VTY users is 21, the number of current VTY users online is 4, and total number of terminal users online is 4.
      The current login time is 2020-12-15 15:58:03.
<SSH Server>
```

#### Configuration Scripts

```
#
sysname SSH Server
#
acl number 2000
 rule 5 permit source 10.248.103.0 0.0.0.255
#
rsa peer-public-key rsa01 encoding-type openssh
 public-key-code begin
  ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCg5Ag490i6ilB7QuCVb35B8RJEh1DIYB88h2p1qjdh7qdMQv8rpJaVAgQWxwzKZO0XdFuz4ReGQzTCSf7Det7Ajicddw3qi+6P8hRqZj6MPdLg/o3RN4aPCfr/LFWCwqJ3gWGHlOC7qqjRk+6pySVoiWcSk5/elBkU7WVk/cSWrt4qFXJV373OCesKcEVeDvAa1Tvx6L3LQroBqUO0EXzDgOthPCmOqiqvS5h3JipzqVsesdSKjeInooCQzSOv5eePpBcFcIvU6wFiLIZ5vnf6YtypgTVzHuje/sh4xM7Iuuon7AYXKHT8NpO9jd9zA/lKaRPXyDtei1O1Bt/5lxnn rsa-key
 public-key-code end
 peer-public-key end
#
aaa
 local-user admin123 password irreversible-cipher $1d$+,JS+))\\2$KVNj(.3`_5x0FCKGv}H&.kUTI`Ff&H*eBqO.ua>)$
 local-user admin123 service-type terminal ssh
 local-user admin123 privilege level 3
#
interface MEth0/0/0
 ip address 10.248.103.194 255.255.255.0
#
stelnet server enable
ssh user admin123
ssh user admin123 authentication-type rsa
ssh user admin123 assign rsa-key rsa01
ssh user admin123 service-type stelnet
ssh server-source all-interface
ssh server acl 2000
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