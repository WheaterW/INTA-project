Example for Using IPv6 SFTP to Operate Files
============================================

In this example, a local key pair is configured on the SSH server, and a username and a password are configured on the server for an IPv6 SSH user. After the IPv6 SFTP service is enabled and the SFTP client is connected to the server, you can perform file operations.

#### Networking Requirements

As the device deployment scale increases, more and more devices need to be maintained and upgraded remotely. Online software upgrade, a new upgrade method by loading software packages remotely, facilitates remote upgrades, reduces upgrade costs, shortens the time that customers wait for upgrades, and improves customers' satisfaction. FTP is usually used to transmit data for online upgrades. FTP transmits data and even user names and passwords in plaintext, bringing security risks.

SFTP resolves the security issue. It enables you to securely log in to a remote device for file management, improving data transmission security. You can use SFTP to log in to a remote device from a device functioning as a client for secure file transfer and online upgrades.

As shown in [Figure 1](#EN-US_TASK_0193002354__fig_dc_vrp_vfm_cfg_002601), after the IPv6 SFTP server function is enabled on the device that functions as an SSH server, the PC that functions as an IPv6 SFTP client can use all, RSA, DSA, ECC, SM2, x509v3-ssh-rsa, password, password-rsa, password-ecc, password-dsa, password-sm2, or password-x509v3-rsa as the authentication mode to connect to the SSH server.

**Figure 1** Using IPv6 SFTP to operate files![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GigabitEthernet0/0/0.


  
![](images/fig_dc_vrp_vfm_cfg_002601.png)

#### Precautions

After you log in to the SFTP server through the console port, configure an IPv6 address of a logical interface as the source IPv6 address for SFTP login.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a local user and configure it.
2. Enable the IPv6 SFTP service on the SSH server and configure a service type for the user.

#### Data Preparation

To complete the configuration, you need the following data:

* SFTP software installed on the SFTP client
* Authentication mode: password Username: client001
* Level (3) of the user client001
* IPv6 address (2001:db8::1/32) of the SSH server
* IPv6 routes available between the SFTP client and server
* User type (SSH) and authentication mode (password)

#### Procedure

1. Configure an IP address for the management interface of the SFTP server.
   
   
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
   [~SSH Server] interface GigabitEthernet0/0/0
   ```
   ```
   [~SSH Server-GigabitEthernet0/0/0] undo shutdown
   ```
   ```
   [~SSH Server-GigabitEthernet0/0/0] ipv6 enable
   ```
   ```
   [*SSH Server-GigabitEthernet0/0/0] ipv6 address 2001:db8::1 32
   ```
   ```
   [*SSH Server-GigabitEthernet0/0/0] quit
   ```
   ```
   [*SSH Server] commit
   ```
2. Configure the user name and password for the local user on the server.
   
   
   ```
   [*SSH Server] aaa
   ```
   ```
   [*SSH Server-aaa] local-user client001 password
   ```
   ```
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   ```
   ```
   [*SSH Server-aaa] local-user client001 level 3
   ```
   ```
   [*SSH Server-aaa] local-user client001 service-type ssh
   ```
   ```
   [*SSH Server-aaa] quit
   ```
   ```
   [*SSH Server] commit
   ```
3. Enable the SFTP function and set the service type to SFTP for the SSH user.
   
   
   ```
   [~SSH Server] interface LoopBack 0
   ```
   ```
   [~SSH Server-LoopBack0] ip address 2001:db8::2 64
   ```
   ```
   [*SSH Server-LoopBack0] quit
   ```
   ```
   [~SSH Server] sftp ipv6 server enable
   ```
   ```
   [*SSH Server] ssh ipv6 server-source -i loopback 0
   ```
   ```
   [*SSH Server] ssh user client001
   ```
   ```
   [*SSH Server] ssh user client001 authentication-type password
   ```
   ```
   [*SSH Server] commit
   ```
   ```
   [~SSH Server] ssh user client001 service-type sftp
   ```
   ```
   [*SSH Server] commit
   ```
4. Configure the authorized directory for the SSH user.
   
   
   ```
   [~SSH Server] ssh user client001 sftp-directory cfcard:/
   ```
   ```
   [*SSH Server] commit
   ```
5. Verify the configuration.
   
   
   
   Start the SFTP software on the client, and enter the username, password, and port number (22 by default) to access the SSH server and transfer files.

#### SSH server configuration file

```
#
sysname SSH Server
#
aaa
 local-user client001 password cipher @%@%.OuC6Vo7Z,A'y~/KB&,vmd@%@%
 local-user client001 service-type ssh
 local-user client001 level 3
#
interface GigabitEthernet0/0/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8::1/32
#
interface LoopBack 0
 ipv6 address 2001:DB8::2/64
sftp ipv6 server enable
ssh ipv6 server-source -i loopback 0
ssh user client001
ssh user client001 authentication-type password
ssh user client001 service-type sftp
ssh user client001 sftp-directory cfcard:/
#
return
```