Example for Configuring Static MAC Address Entries
==================================================

Example for Configuring Static MAC Address Entries

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001517340228__fig156041758113319), a server is connected to 100GE 1/0/2 of a device. To prevent the device from broadcasting the packets destined for the server, it is required that a static MAC address entry of the server be configured on the device so that the device always unicasts the packets destined for the server through 100GE 1/0/2. In addition, it is required that the MAC address of the PC be statically bound to 100GE 1/0/1 to ensure secure communication between the PC and the server.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


**Figure 1** Network diagram for configuring static MAC address entries  
![](figure/en-us_image_0000001569192441.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN and add interfaces to the VLAN to implement Layer 2 forwarding.
2. Configure the static MAC address entry of the server on an interface.

#### Procedure

1. Create VLAN 2 and add 100GE 1/0/1 and 100GE 1/0/2 to VLAN 2.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 2
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
2. Configure a static MAC address entry of the PC on 100GE 1/0/1.
   
   
   ```
   [~DeviceA] mac-address static 00e0-fc12-3456 100ge 1/0/1 vlan 2
   [*DeviceA] commit
   ```
3. Configure a static MAC address entry of the server on 100GE 1/0/2.
   
   
   ```
   [~DeviceA] mac-address static 00e0-fc12-3457 100ge 1/0/2 vlan 2
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**display mac-address static**](cmdqueryname=display+mac-address+static) **vlan** *vlan-id* [ **verbose** ] command in any view to check static MAC address entries configured based on a specified VLAN.
```
[~DeviceA] display mac-address static vlan 2
------------------------------------------------------------------------------- 
MAC Address          VLAN/VSI/BD                    Learned-From        Type        Age
-------------------------------------------------------------------------------
00e0-fc12-3456       2/-/-                         100GE1/0/1            static        -
00e0-fc12-3457       2/-/-                         100GE1/0/2            static        -
-------------------------------------------------------------------------------
Total items: 2
```


#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 2
#
interface 100GE1/0/1
 port link-type access
 port default vlan 2
#
interface 100GE1/0/2
 port link-type access
 port default vlan 2
#
mac-address static 00e0-fc12-3456 100GE1/0/1 vlan 2
mac-address static 00e0-fc12-3457 100GE1/0/2 vlan 2
#
return
```