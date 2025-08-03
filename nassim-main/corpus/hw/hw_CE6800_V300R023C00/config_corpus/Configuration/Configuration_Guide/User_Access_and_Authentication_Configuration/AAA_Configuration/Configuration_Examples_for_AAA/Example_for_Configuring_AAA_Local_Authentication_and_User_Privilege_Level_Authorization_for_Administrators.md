Example for Configuring AAA Local Authentication and User Privilege Level Authorization for Administrators
==========================================================================================================

Example for Configuring AAA Local Authentication and User Privilege Level Authorization for Administrators

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512836118__fig_dc_ar_cfg_004001), the enterprise requires that the administrator use AAA local authentication to log in to the device through STelnet. The specific requirements are as follows:

1. The administrator can log in to the device through STelnet only after entering a correct user name and password.
2. After the administrator logs in to the device through STelnet, the privilege level 3 is authorized to the administrator.

**Figure 1** Network diagram for configuring AAA local authentication and user privilege level authorization for administrators![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001564115885.png)

#### Configuration Roadmap

1. Configure STelnet login on DeviceA: Set the authentication mode for accessing VTY user interfaces to AAA, enable the STelnet service, and configure the authentication mode and service type for SSH users.
2. Configure AAA local authentication: Configure a user name and password, set the user access type, and set the user privilege level.

#### Precautions

Ensure that there are reachable routes between devices before the configuration.


#### Procedure

1. Configure IP addresses for interfaces.
   
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceA 
   [*DeviceA] commit
   [~DeviceA] vlan batch 10
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 192.168.10.1 24
   [*DeviceA-Vlanif10] quit
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
3. Configure AAA local authentication.
   
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] local-user user1-huawei password irreversible-cipher YsHsjx_202206
   [*DeviceA-aaa] local-user user1-huawei service-type ssh
   [*DeviceA-aaa] local-user user1-huawei privilege level 3
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

The administrator can log in to DeviceA through the STelnet client after entering the correct user name and password.


#### Configuration Scripts

```
#
sysname DeviceA
#
aaa
 local-user user1-huawei password irreversible-cipher $1d$OwseVRh@LH}ZeTBm$1nH4$ab>d(N{-%0!ab48y=Ic*xEUR4pVhR2"9-~,$
 local-user user1-huawei privilege level 3
 local-user user1-huawei service-type ssh   
# 
vlan batch 10
#
interface Vlanif10
 ip address 192.168.10.1 255.255.255.0
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
#
stelnet server enable 
ssh server-source -i Vlanif 10
#
user-interface vty 0 4           
 authentication-mode aaa           
 protocol inbound ssh
# 
return 
```