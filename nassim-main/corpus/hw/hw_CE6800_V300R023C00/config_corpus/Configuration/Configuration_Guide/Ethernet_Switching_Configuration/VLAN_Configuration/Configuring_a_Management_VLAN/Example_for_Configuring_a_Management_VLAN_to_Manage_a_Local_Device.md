Example for Configuring a Management VLAN to Manage a Local Device
==================================================================

Example for Configuring a Management VLAN to Manage a Local Device

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130622864__fig799819397431), the PC and DeviceA are on the same network segment. A user wants to log in to DeviceA through STelnet using DeviceA's management VLAN.

**Figure 1** Network diagram for configuring a management VLAN to manage a local device![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001130782714.png)

#### Procedure

1. Create a management VLAN.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 2
   [*DeviceA-vlan2] management-vlan
   [*DeviceA-vlan2] quit
   [*DeviceA] commit
   ```
2. Add interfaces to the management VLAN.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
3. Create a VLANIF interface for the management VLAN and configure an IP address for this interface.
   
   
   ```
   [~DeviceA] interface vlanif 2
   [*DeviceA-Vlanif2] ip address 10.10.10.2 24
   [*DeviceA-Vlanif2] quit
   [*DeviceA] commit
   ```
4. Generate a local key pair on DeviceA.
   
   
   ```
   [~DeviceA] rsa local-key-pair create 
   The key name will be:Host 
   The range of public key size is (2048, 3072). 
   NOTE: Key pair generation will take a short while. 
   Please input the modulus [default = 3072]:
   ```
5. Configure VTY user interfaces on DeviceA.
   
   
   ```
   [~DeviceA] user-interface vty 0 4
   [*DeviceA-ui-vty0-4] authentication-mode aaa 
   [*DeviceA-ui-vty0-4] protocol inbound ssh 
   [*DeviceA-ui-vty0-4] quit
   [*DeviceA] commit
   ```
6. Create an SSH user.
   
   
   ```
   [~DeviceA] aaa 
   [*DeviceA-aaa] local-user client001 password irreversible-cipher Huawei@123
   [*DeviceA-aaa] local-user client001 privilege level 3 
   [*DeviceA-aaa] local-user client001 service-type ssh 
   [*DeviceA-aaa] quit
   [*DeviceA] ssh user client001
   [*DeviceA] ssh user client001 authentication-type password
   [*DeviceA] commit
   ```
7. Enable the STelnet service.
   
   
   ```
   [~DeviceA] stelnet server enable
   [*DeviceA] ssh user client001 service-type stelnet
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If there are intermediate devices between the PC and DeviceA, configure the intermediate devices to transparently transmit packets of the management VLAN (VLAN 2 in this example).

#### Verifying the Configuration

After configuration is complete, you can log in to DeviceA from a PC using password authentication. You are advised to use **OpenSSH** as the SSH login software. After logging in to DeviceA from a PC, you can centrally manage DeviceA.


#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 2
#
vlan 2
 management-vlan
#
aaa
 local-user client001 password irreversible-cipher $1b$g/#_YP]w_)$IWm]C@&R&C9bFS<b>6P6'wB$R:#)y6*Hz:Z4(+S=$
 local-user client001 privilege level 3
 local-user client001 service-type ssh
#
interface Vlanif2
 ip address 10.10.10.2 255.255.255.0
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 2
#
stelnet server enable
ssh user client001
ssh user client001 authentication-type password
ssh user client001 service-type stelnet
#
user-interface vty 0 4
 authentication-mode aaa
#
return
```