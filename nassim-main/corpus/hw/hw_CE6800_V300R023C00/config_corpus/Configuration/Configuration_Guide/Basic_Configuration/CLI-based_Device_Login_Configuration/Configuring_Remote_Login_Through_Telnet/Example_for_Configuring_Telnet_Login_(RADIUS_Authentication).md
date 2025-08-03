Example for Configuring Telnet Login (RADIUS Authentication)
============================================================

Example for Configuring Telnet Login (RADIUS Authentication)

#### Networking Requirements

The network administrator requires remote management and maintenance on a device and high network security for protecting the network against unauthorized access. To meet the requirements, you can configure Telnet login based on ACL rules and RADIUS authentication.

In [Figure 1](#EN-US_TASK_0000001601628757__fig6799115116392), DeviceA is the Telnet server, and there are reachable routes between the network administrator's PC and DeviceA and between DeviceA and the RADIUS server. The IP address and port number of the RADIUS server are 10.1.6.6/24 and 1812, respectively.

**Figure 1** Network diagram for configuring Telnet login based on ACL rules and RADIUS authentication  
![](figure/en-us_image_0000001867991237.png)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set device interface parameters.
2. Configure Telnet to enable users to log in to the device through Telnet.
3. Configure an ACL rule to ensure that only users matching the ACL rule can log in to the device.
4. Configure the RADIUS protocol to implement RADIUS authentication. After the configuration is complete, users must use the user name and password configured on the RADIUS server to log in to the device through Telnet, ensuring login security.
5. Configure the RADIUS server.

#### Configuration Precautions

* In insecure network environments, you are advised to use a secure password authentication mode, encryption authentication algorithm, and protocol. For details about secure configuration examples, see [Example for Configuring STelnet Login (RADIUS Authentication)](vrp_login_cfg_0029.html).
* Ensure that there are reachable routes between devices before the configuration.

* Ensure that the IP address, port number, and shared key of the RADIUS server are configured correctly on the device and are the same as those on the RADIUS server.
* After a domain is configured as the global default administrative domain, the AAA configuration in this domain is used, regardless of whether the user name of the administrator contains the domain name.
* Ensure that a user has been configured on the RADIUS server. In this example, the user **admin123@huawei.com** (*user name*@*domain name*) and password **YsHsjx\_202206** have been configured on the RADIUS server.
* If the RADIUS server does not support the user names containing domain names, run the **undo radius-server user-name domain-included** command to configure the device not to encapsulate the domain name in the user name when sending packets to the RADIUS server.

#### Procedure

1. Run the **install feature-software WEAKEA** command in the user view to install the weak security algorithm/protocol feature package (WEAKEA).
2. Set interface parameters.
   
   
   
   # Configure IP addresses for interfaces.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] vlan batch 10 20
   [*DeviceA] interface 100ge 1/0/1 
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2 
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 10.1.1.2 255.255.255.0
   [*DeviceA-Vlanif10] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ip address 10.1.6.2 255.255.255.0
   [*DeviceA-Vlanif20] quit
   [*DeviceA] commit
   ```
3. Set the server port number and enable the Telnet server function.
   
   
   ```
   [~DeviceA] undo telnet server disable
   [*DeviceA] telnet server port 1025
   [*DeviceA] telnet server-source all-interface
   [*DeviceA] commit
   ```
4. Set parameters for the VTY user interface.
   
   
   
   # Set the authentication mode and protocol for accessing VTY user interfaces 0 to 4 to AAA and Telnet, respectively.
   
   ```
   [~DeviceA] user-interface vty 0 4 
   [*DeviceA-ui-vty0-4] authentication-mode aaa
   [*DeviceA-ui-vty0-4] protocol inbound telnet
   [*DeviceA-ui-vty0-4] user privilege level 3
   [*DeviceA-ui-vty0-4] quit
   [*DeviceA] commit
   ```
   
   # Configure an ACL rule to allow the administrator to log in. The IP address of the administrator's PC is 10.137.217.10.
   
   
   
   ```
   [~DeviceA] acl 2000
   [*DeviceA-acl4-basic-2000] rule permit source 10.137.217.10 0
   [*DeviceA-acl4-basic-2000] quit
   [*DeviceA] user-interface vty 0 4
   [*DeviceA-ui-vty0-4] acl 2000 inbound
   [*DeviceA-ui-vty0-4] quit
   [*DeviceA] commit
   ```
5. Configure RADIUS authentication.
   
   
   
   # Configure a RADIUS server template for communication between DeviceA and the RADIUS server.
   
   ```
   [~DeviceA] radius-server template template1
   [*DeviceA-radius-template1] radius-server authentication 10.1.6.6 1812 weight 80
   [*DeviceA-radius-template1] radius-server shared-key cipher YsHsjx_202206
   [*DeviceA-radius-template1] quit
   [*DeviceA] commit
   ```
   
   # Configure an AAA authentication scheme and set the authentication mode to RADIUS.
   
   ```
   [~DeviceA] aaa
   [*DeviceA-aaa] authentication-scheme auth1
   [*DeviceA-aaa-authen-auth1] authentication-mode radius
   [*DeviceA-aaa-authen-auth1] quit
   ```
   
   # Create a domain, and apply the AAA authentication scheme and RADIUS server template to the domain.
   
   ```
   [*DeviceA-aaa] domain huawei.com
   [*DeviceA-aaa-domain-huawei.com] authentication-scheme auth1
   [*DeviceA-aaa-domain-huawei.com] radius-server template1
   [*DeviceA-aaa-domain-huawei.com] quit
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
   
   # Configure the domain **huawei.com** as the global default administrative domain so that the administrator does not need to enter the domain name when logging in to the device.
   
   ```
   [~DeviceA] domain huawei.com admin
   [*DeviceA] commit
   ```
6. Configure the RADIUS server.
   
   
   
   The configuration includes the following steps: add a device, add a user, and set the user privilege level to 3.

#### Verifying the Configuration

# Set the IP address of the administrator's PC to 10.137.217.10 and run the following command on the Windows CLI of the administrator's PC to telnet to the device:

```
C:\Documents and Settings\Administrator> telnet 10.1.1.2 1025
```
# In the login window, enter the user name **admin123** and password **YsHsjx\_202206** configured on the RADIUS server as prompted, and press **Enter**. If the authentication succeeds, you can successfully log in to DeviceA through Telnet. (The following information is for reference only.)
```
Username:admin123
Password:
Info: The max number of VTY users is 21, the number of current VTY users online is 1, and total number of terminal users online is 1.
      The current login time is 2020-12-15 14:23:00.
[*DeviceA]
```


#### Configuration Scripts

```
#
sysname DeviceA
#
acl number 2000
 rule 5 permit source 10.137.217.10 0
#
radius-server template template1                                                        
 radius-server shared-key cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!SKvr${[Fs.3t@/5k|BENhEu>W(3\~XG!!D;!!!!!2jp5!!!!!!A!!!!3"pK8qv!}9M#(4$jGWvQF/R[CNe/+:W^jk8HUe&W%+%#
 radius-server authentication 10.1.6.6 1812 weight 80                           
#
aaa
 authentication-scheme auth1    
  authentication-mode radius   
 domain huawei.com            
  authentication-scheme auth1     
  radius-server template1      
#  
domain huawei.com admin 
#
vlan batch 10 20
#
interface Vlanif10
 ip address 10.1.1.2 255.255.255.0
#
interface Vlanif20
 ip address 10.1.6.2 255.255.255.0
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
#
interface 100GE1/0/2
 port link-type trunk
 port trunk allow-pass vlan 20
#
telnet server-source all-interface
telnet server port 1025
#
user-interface vty 0 4  
 acl 2000 inbound
 authentication-mode aaa 
 user privilege level 3
 protocol inbound telnet
return 
```