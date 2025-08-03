Example for Configuring IPSG Based on a Static Binding Table on an Interface
============================================================================

Example for Configuring IPSG Based on a Static Binding Table on an Interface

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512849698__fig991833219390), PC1 and PC2 access the network through DeviceA, and they both use static IP addresses. The administrator wants users to use fixed IP addresses to access the Internet.

**Figure 1** Network diagram of configuring IPSG based on a static binding table on an interface![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001564009537.png)

#### Procedure

1. Create static binding entries on Device A.
   
   
   
   # Create static binding entries on Device A.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] user-bind static ip-address 10.0.0.1 mac-address 00e0-fc12-3456
   [*DeviceA] user-bind static ip-address 10.0.0.11 mac-address 00e0-fc12-3478
   ```
2. Enable IPSG.
   
   # Enable IPSG on 100GE1/0/1, and 100GE1/0/2 of DeviceA.
   ```
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] [ipv4 source check user-bind enable](cmdqueryname=ipv4+source+check+user-bind+enable)
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] [ipv4 source check user-bind enable](cmdqueryname=ipv4+source+check+user-bind+enable)
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display static binding entries.

```
[~DeviceA] display ip source check user-bind status
DHCP Bind-table on slot 1:  
---------------------------------------------------------------------------------------------------------- 
IP Address        MAC Address            Vlan(O/I)        Interface     
                                         Type             Status                                                                        
----------------------------------------------------------------------------------------------------------- 
10.0.0.1           00e0-fc12-3456           -   /-           -           
                                         Static           IPv4/-
10.0.0.11          00e0-fc12-3478           -   /-           -           
                                         Static           IPv4/-
----------------------------------------------------------------------------------------------------------- 
Total count:           2                      
```

#### Configuration Files

DeviceA

```
#
sysname DeviceA
#
user-bind static ip-address 10.0.0.1 mac-address 00e0-fc12-3456
user-bind static ip-address 10.0.0.11 mac-address 00e0-fc12-3478
#
interface 100GE1/0/1
 ipv4 source check user-bind enable
#
interface 100GE1/0/2
 ipv4 source check user-bind enable
#
return
```