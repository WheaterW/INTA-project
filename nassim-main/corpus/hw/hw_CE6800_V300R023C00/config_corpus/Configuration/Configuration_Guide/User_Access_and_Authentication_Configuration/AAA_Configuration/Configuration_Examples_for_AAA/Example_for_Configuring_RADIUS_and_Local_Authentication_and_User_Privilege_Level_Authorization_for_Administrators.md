Example for Configuring RADIUS and Local Authentication and User Privilege Level Authorization for Administrators
=================================================================================================================

Example for Configuring RADIUS and Local Authentication and User Privilege Level Authorization for Administrators

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563995865__fig_dc_ar_cfg_004001), a RADIUS server is deployed on an enterprise network. The enterprise requires that the administrator use RADIUS authentication to log in to DeviceA through STelnet. The specific requirements are as follows:

1. The administrator can log in to the device through STelnet only after entering a correct user name and password.
2. After the administrator logs in to the device through STelnet, the privilege level 3 is authorized to the administrator.
3. If the server does not respond to the authentication request from the device (for example, the link between the device and server is disconnected), local authentication is performed when the administrator attempts to log in to the device.

**Figure 1** Network diagram for configuring RADIUS and local authentication and user privilege level authorization for administrators![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001513155706.png)

#### Configuration Roadmap

1. Configure STelnet login on DeviceA: Set the authentication mode for accessing VTY user interfaces to AAA, enable the STelnet service, and configure the authentication mode and service type for SSH users.
2. Configure RADIUS authentication on DeviceA: Create a RADIUS server template and AAA schemes, and apply the server template and AAA schemes to a domain.
3. Configure a local user on DeviceA: Configure a local user name, password, and privilege level.
4. Configure a RADIUS server.

#### Precautions

* Ensure that there are reachable routes between devices before the configuration.
* Ensure that the shared key in the RADIUS server template is the same as that configured on the RADIUS server.
* If the login account is not created on the server but exists on the local host, RADIUS authentication is considered failed, and local authentication is not performed. Local authentication is performed only when the server is down or does not respond.
* After the domain is set as the global default administrative domain and the user name of the administrator contains the domain name or does not contain any domain name, the administrator uses AAA configuration in the global default administrative domain.
* If the RADIUS server does not support the user name containing a domain name, run the **undo radius-server user-name domain-included** command in the RADIUS server template view to configure the device to send packets that do not contain a domain name to the RADIUS server.
* After the **undo radius-server user-name domain-included** command is run, the device changes only the user name format in the sent packet, without affecting the domain to which the user belongs. For example, after this command is run, the user with the user name **username@huawei.com** still uses AAA configuration in the domain **huawei.com**.
* When the extended RADIUS attribute HW-Exec-Privilege (26-29) is used to authorize the priority of an administrator, the value ranges from 0 to 3. The value greater than or equal to 4 is invalid.

#### Procedure

1. Configure IP addresses for interfaces.
   
   
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
2. Configure STelnet login.
   
   
   
   # Configure DeviceA to generate a local key pair.
   
   ```
   [~DeviceA] rsa local-key-pair create
   The key name will be:Host
   The range of public key size is (2048, 4096).
   NOTE: Key pair generation will take a short while.
   Please input the modulus [default = 3072]:3072 
   ```
   
   # Set the authentication mode and protocol for accessing VTY user interfaces 0 to 4 to AAA and SSH, respectively.
   
   ```
   [*DeviceA] user-interface vty 0 4 
   [*DeviceA-ui-vty0-4] authentication-mode aaa 
   [*DeviceA-ui-vty0-4] protocol inbound ssh
   [*DeviceA-ui-vty0-4] quit
   ```
   
   # Enable the SSH server function on DeviceA.
   
   ```
   [*DeviceA] stelnet server enable 
   [*DeviceA] ssh server-source -i vlanif 10
   ```
   
   # Set the authentication mode of all SSH users to password authentication.
   
   ```
   [*DeviceA] ssh authentication-type default password
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If only the authentication mode and service type of a few SSH users need to be set to password authentication and STelnet, you can specify the SSH user name to set the authentication mode and service type of a single SSH user. For example, set the authentication mode and service type of an SSH user named **admin** to password authentication and STelnet, respectively.
   
   [DeviceA] **ssh user admin authentication-type password**
   
   [DeviceA] **ssh user admin service-type stelnet**
3. Configure RADIUS authentication, authorization, and accounting.
   
   
   
   # Configure a RADIUS server template for communication between DeviceA and RADIUS server.
   
   ```
   [~DeviceA] radius-server template 1
   [*DeviceA-radius-1] radius-server authentication 10.1.6.6 1812
   [*DeviceA-radius-1] radius-server accounting 10.1.6.6 1813
   [*DeviceA-radius-1] radius-server shared-key cipher YsHsjx_202206139
   [*DeviceA-radius-1] quit
   [*DeviceA] commit
   ```
   
   # Configure an AAA authentication scheme and set the authentication mode to RADIUS and local authentication.
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] authentication-scheme auth1
   [*DeviceA-aaa-authen-auth1] authentication-mode radius local
   [*DeviceA-aaa-authen-auth1] quit
   ```
   
   # Configure an AAA accounting scheme named **acc1** and set the accounting mode to RADIUS accounting.
   
   ```
   [*DeviceA-aaa] accounting-scheme acc1 
   [*DeviceA-aaa-accounting-acc1] accounting-mode radius 
   [*DeviceA-aaa-accounting-acc1] quit
   ```
   
   # Apply the AAA schemes and RADIUS server template to a domain.
   
   ```
   [*DeviceA-aaa] domain huawei.com
   [*DeviceA-aaa-domain-huawei.com] authentication-scheme auth1
   [*DeviceA-aaa-domain-huawei.com] accounting-scheme acc1
   [*DeviceA-aaa-domain-huawei.com] radius-server 1
   [*DeviceA-aaa-domain-huawei.com] quit
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
4. Configure the domain to which the administrator belongs as the global default administrative domain so that the administrator does not need to enter the domain name during an STelnet login to DeviceA.
   
   
   ```
   [~DeviceA] domain huawei.com admin
   [*DeviceA] commit
   ```
5. Configure AAA local authentication. Set the local user name to **user1-huawei**, password to **YsHsjx\_202206**, and privilege level to 3.
   
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] local-user user1-huawei password irreversible-cipher YsHsjx_202206
   [*DeviceA-aaa] local-user user1-huawei service-type ssh
   [*DeviceA-aaa] local-user user1-huawei privilege level 3
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
6. Configure a RADIUS server.
   
   
   
   The configuration includes adding a device, adding a user, and setting the user privilege level to 3.

#### Verifying the Configuration

* The administrator can log in to DeviceA through the STelnet client after entering the correct user name and password.
* When the link between DeviceA and the server is operational, run the **display access-user username** *user-name* **detail** command on DeviceA to check information about the user **user1-huawei**.
  
  In the command output, the values of **User access type**, **User Privilege**, **User authentication type**, **Current authentication method**, **Current authorization method**, and **Current accounting method** indicate that the user login mode is SSH, the privilege level is 3, the authentication type is administrator authentication, and the authentication, authorization, as well as accounting modes are RADIUS.
  
  ```
  <DeviceA> display access-user username user1-huawei detail
   ------------------------------------------------------------------------------
  Basic:
    User ID                         : 16414
    User name                       : user1-huawei
    Domain-name                     : huawei.com
    User MAC                        : -
    User IP address                 : 10.1.1.10
    User IPv6 address               : -
    User access time                : 2024/07/01 10:49:22
    User accounting session ID      : example010000000000006d****010001e
    User access type                : SSH
    User Privilege                  : 3
    User Group                      : -
  
  AAA:
    User authentication type        : Administrator authentication
    Current authentication method   : RADIUS
    Current authorization method    : RADIUS
    Current accounting method       : RADIUS
  ```
* When the link between DeviceA and the RADIUS server is disconnected, run the **display access-user username** *user-name* **detail** command on DeviceA to check information about the user **user1-huawei**.
  
  In the command output, the values of **User access type**, **User Privilege**, **User authentication type**, **Current authentication method**, **Current authorization method**, and **Current accounting method** indicate that the user login mode is SSH, the privilege level is 3, the authentication type is administrator authentication, the authentication mode is local, and the accounting mode is RADIUS.
  
  ```
  <DeviceA> display access-user username user1-huawei detail
   ------------------------------------------------------------------------------
  Basic:
    User ID                         : 16414
    User name                       : user1-huawei
    Domain-name                     : huawei.com
    User MAC                        : -
    User IP address                 : 10.1.1.10
    User IPv6 address               : -
    User access time                : 2024/07/01 10:49:22
    User accounting session ID      : example010000000000006d****010001e
    User access type                : SSH
    User Privilege                  : 3
    User Group                      : -
  
  AAA:
    User authentication type        : Administrator authentication
    Current authentication method   : Local
    Current authorization method    : -
    Current accounting method       : RADIUS
  ```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
radius-server template 1                                                        
 radius-server shared-key cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!SKvr${[Fs.3t@/5k|BENhEu>W(3\~XG!!D;!!!!!2jp5!!!!!!A!!!!3"pK8qv!}9M#(4$jGWvQF/R[CNe/+:W^jk8HUe&W%+%#
 radius-server authentication 10.1.6.6 1812 weight 80                           
 radius-server accounting 10.1.6.6 1813 weight 80
#
aaa
 authentication-scheme auth1    
  authentication-mode radius local 
 accounting-scheme acc1    
  accounting-mode radius  
 domain huawei.com            
  authentication-scheme auth1     
  accounting-scheme acc1
  radius-server 1      
 local-user user1-huawei password irreversible-cipher $1d$OwseVRh@LH}ZeTBm$1nH4$ab>d(N{-%0!ab48y=Ic*xEUR4pVhR2"9-~,$
 local-user user1-huawei privilege level 3
 local-user user1-huawei service-type ssh   
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
stelnet server enable 
ssh server-source -i Vlanif10
#
user-interface vty 0 4           
 authentication-mode aaa           
 protocol inbound ssh
# 
return 
```