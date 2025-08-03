Example for Configuring Telnet Login for IPv4 Users (Local Authentication)
==========================================================================

Example for Configuring Telnet Login for IPv4 Users (Local Authentication)

#### Networking Requirements

Users want to easily configure and manage the device shown in [Figure 1](#EN-US_TASK_0000001563893025__fig_dc_cfg_login_001501). AAA authentication needs to be configured for Telnet users on the server, and an ACL needs to be configured to ensure that only the users matching the ACL can log in to the device.

**Figure 1** Network diagram of Telnet login  
![](figure/en-us_image_0000001512693928.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for the management interface on the Telnet server.
2. Configure Telnet login, that is, enable the Telnet server function and configure the server port number to remotely maintain network devices.
3. Set VTY user interface parameters, including an ACL policy, to ensure that only users matching the ACL can log in to the device.
4. Configure the user name and password for the administrator, and configure an AAA authentication policy to ensure that only users passing the authentication can log in to the device.

#### Configuration Precautions

In insecure network environments, you are advised to use a secure password authentication mode, encryption authentication algorithm, and protocol. For details about the configuration example of secure authentication, see [Example for Configuring STelnet Login for IPv4 Users (Local Authentication)](vrp_login_cfg_0016.html).


#### Procedure

1. Log in to the device. If you log in to the device for the first time, perform operations in [First Login Through the Console Port](vrp_first_cfg_0004.html) and then perform the following steps to set up the Telnet login environment.
2. Run the **install feature-software WEAKEA** command in the user view to install the weak security algorithm/protocol feature package (WEAKEA).
3. Set an IP address of the management interface for the Telnet server.
   
   
   ```
   <HUAWEI> system-view    
   [~HUAWEI] sysname Telnet Server
   [*HUAWEI] commit
   [~Telnet Server] interface meth 0/0/0
   [~Telnet Server-MEth0/0/0] ip address 10.137.217.177 255.255.255.0
   [*Telnet Server-MEth0/0/0] quit
   [*Telnet Server] commit
   ```
4. Set the server port number and enable the server function.
   
   
   ```
   [~Telnet Server] undo telnet server disable
   [*Telnet Server] telnet server port 1025
   [*Telnet Server] telnet server-source all-interface
   [*Telnet Server] commit
   ```
5. Set parameters for the VTY user interface.
   
   
   
   # Set the maximum number of VTY user interfaces.
   
   ```
   [~Telnet Server] user-interface maximum-vty 8
   [*Telnet Server] commit
   ```
   
   # Configure an ACL rule that allows device login from specified host addresses. The IP address of PC1 is 10.137.217.10, and the IP address of PC2 is 10.137.217.20.
   
   ```
   [~Telnet Server] acl 2001
   [*Telnet Server-acl4-basic-2001] rule permit source 10.137.217.10 0
   [*Telnet Server-acl4-basic-2001] rule deny source 10.137.217.20 0
   [*Telnet Server-acl4-basic-2001] quit
   [*Telnet Server] user-interface vty 0 7
   [*Telnet Server-ui-vty0-7] acl 2001 inbound
   [*Telnet Server-ui-vty0-7] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * You can determine whether to configure ACL rules as required.
   * If the management interface is bound to the VPN instance **\_management\_vpn\_** by default, the commands for creating ACL rules are as follows:
     + **rule permit vpn-instance \_management\_vpn\_ source 10.137.217.10 0**
     + **rule deny vpn-instance \_management\_vpn\_ source 10.137.217.20 0**
   
   # Configure terminal attributes for the VTY user interface.
   
   ```
   [~Telnet Server-ui-vty0-7] shell
   [*Telnet Server-ui-vty0-7] idle-timeout 20
   [*Telnet Server-ui-vty0-7] screen-length 30
   [*Telnet Server-ui-vty0-7] history-command max-size 20
   [*Telnet Server-ui-vty0-7] commit
   ```
   
   # Configure the authentication mode for the VTY user interface.
   
   ```
   [~Telnet Server-ui-vty0-7] authentication-mode aaa
   [*Telnet Server-ui-vty0-7] user privilege level 3
   [*Telnet Server-ui-vty0-7] protocol inbound telnet
   [*Telnet Server-ui-vty0-7] quit
   [*Telnet Server] commit
   ```
6. Configure information about the administrator who logs in to the device.
   
   
   
   # Configure the authentication mode for the login user.
   
   ```
   [~Telnet Server] aaa
   [~Telnet Server-aaa] local-user admin1234 password
   Please configure the login password (8-128)
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   [*Telnet Server-aaa] local-user admin1234 service-type telnet
   [*Telnet Server-aaa] local-user admin1234 privilege level 3
   [*Telnet Server-aaa] quit
   [*Telnet Server] commit
   ```

#### Verifying the Configuration

# Run the following command on the CLI of PC1 to telnet to the device:

```
C:\Documents and Settings\Administrator> telnet 10.137.217.177 1025
```
# Press **Enter**, and enter the user name and password configured for AAA authentication in the login window. If the authentication is successful, the command line prompt for the user view is displayed, indicating that you have successfully logged in to the device.
```
Username:admin1234
Password:
Info: The max number of VTY users is 21, the number of current VTY users online is 1, and total number of terminal users online is 1.
      The current login time is 2020-12-15 14:23:00.
<Telnet Server>
```


#### Configuration Scripts

```
#
sysname Telnet Server
#
telnet server-source all-interface
telnet server port 1025
#
acl number 2001
 rule 5 permit source 10.137.217.10 0
 rule 10 deny source 10.137.217.20 0 
#
aaa
 local-user admin1234 password irreversible-cipher $1d$g8wLJ`LjL!$CyE(V{3qg5DdU:PM[6=6O$UF-.fQ,Q}>^)OBzgoU$
 local-user admin1234 service-type telnet
 local-user admin1234 privilege level 3
#
interface MEth0/0/0
 ip address 10.137.217.177 255.255.255.0
#
user-interface maximum-vty 8
#
user-interface vty 0 7
 acl 2001 inbound
 authentication-mode aaa
 user privilege level 3
 protocol inbound telnet
 history-command max-size 20
 idle-timeout 20 0
 screen-length 30
#
return
```