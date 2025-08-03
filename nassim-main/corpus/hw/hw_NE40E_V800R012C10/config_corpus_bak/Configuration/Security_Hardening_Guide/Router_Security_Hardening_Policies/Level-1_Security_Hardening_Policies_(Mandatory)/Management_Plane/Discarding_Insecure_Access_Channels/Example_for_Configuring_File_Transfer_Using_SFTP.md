Example for Configuring File Transfer Using SFTP
================================================

Example_for_Configuring_File_Transfer_Using_SFTP

#### Networking Requirements

In [Figure 1](#EN-US_CONCEPT_0000001134463702__fig_01), if the SFTP server function is enabled on the device functioning as an SSH server, the PC functioning as an SFTP client can connect to the SSH server after being authenticated in all, RSA, DSA, password, password-rsa, or password-dsa mode.

This example describes how to configure login to the SSH server in password mode.

**Figure 1** Networking diagram for performing file operations using SFTP  
![](figure/en-us_image_0000001180503161.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| SSH Server | GE0/1/1 | 10.137.217.225/16 |
| SSH Server | Loopback0 | 1.1.1.1/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Generate a local key pair on the SSH server to implement secure data exchange between the server and client.
2. Configure an SSH user, including setting an authentication type, username, password, and authorized directory for the user.
3. Enable the SFTP server function on the SSH server and configure the service type for the SSH user.
4. Configure the source interface of the SSH server.

#### Data Preparation

To complete the configuration, you need the following data:

* SSH user's authentication type: password authentication; username: client001 (with the password YsHsjx\_202206)
* User level 3 for user **client001**.
* IP address of the SSH server: 10.137.217.225
* Loopback address of the SSH server: 1.1.1.1

#### Procedure

1. Generate a local key pair on the server.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname SSH Server
   [*HUAWEI] commit
   [~SSH Server] rsa local-key-pair create
   ```
   ```
   The key name will be: HUAWEI_Host   
   The range of public key size is (2048, 3072).  
   NOTE: Key pair generation will take a short while.  
   Please input the modulus [default = 3072]:3072
   ```
2. Configure the username and password for the SSH user on the server.
   ```
   [*SSH Server] aaa
   [*SSH Server-aaa] local-user client001 password
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   Info: A new user is added.
   [*SSH Server-aaa] local-user client001 level 3
   [*SSH Server-aaa] local-user client001 service-type ssh
   [*SSH Server-aaa] commit
   [~SSH Server-aaa] quit
   ```
3. Enable the SFTP server function and set the service type to SFTP.
   ```
   [~SSH Server] interface loopback 0 
   [~SSH Server-LoopBack0] ip address 1.1.1.1 255.255.255.255
   [*SSH Server-LoopBack0] quit
   [*SSH Server] sftp server enable
   [*SSH Server] ssh server-source -i loopback 0
   [*SSH Server] ssh user client001
   [*SSH Server] ssh user client001 authentication-type password
   [*SSH Server] ssh user client001 service-type sftp
   [*SSH Server] commit
   ```
4. Configure the authorized directory for the SSH user.
   ```
   [~SSH Server] ssh user client001 sftp-directory cfcard:
   [*SSH Server] commit
   ```
5. Verify the configuration.
   
   Start the SFTP software on the client, and enter the user name, password, and port number (22 by default) to access the SSH server and transfer files.

#### Configuration File

* SSH server configuration file

```
#
 sysname SSH Server
#
aaa
 local-user client001 password irreversible-cipher $1a$jbB7=)5o.6$::j(W-#|XF&f6"M0>X**1bD0%2_"{4XX!lO="Sn0$
 local-user client001 level 3
 local-user client001 service-type ssh
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 10.137.217.225 255.255.0.0
#
interface loopback 0
 ip address 1.1.1.1 255.255.255.255
sftp server enable
ssh server-source -i loopback 0
ssh user client001
ssh user client001 authentication-type password
ssh user client001 service-type sftp
ssh user client001 sftp-directory cfcard:
#
return
```