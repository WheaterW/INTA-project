Example for Configuring MAC Address Flapping Prevention
=======================================================

Example for Configuring MAC Address Flapping Prevention

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001884597729__fig881552172510), users need to access an enterprise server connected to an interface of a device. If an unauthorized user uses the MAC address of the server to send packets to another interface of the device, that interface learns the MAC address of the server. Then, packets sent from users to the server are forwarded to the unauthorized user. As a result, users cannot access the server, and important data may be intercepted by the unauthorized user. MAC address flapping prevention can be configured to improve server security and prevent attacks from unauthorized users.

**Figure 1** Networking for configuring MAC address flapping prevention![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001924169041.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN and add interfaces to the VLAN to implement Layer 2 forwarding.
2. Configure MAC address flapping prevention on the interface connected to the server.

#### Procedure

1. On DeviceA, create a VLAN and add interfaces to the VLAN.
   
   
   
   # Add 100GE 1/0/1 and 100GE 1/0/2 to VLAN 10.
   
   
   
   ```
   <HUAWEI>  system-view
   [~HUAWEI] sysname DeviceA
   [~DeviceA] vlan batch 10
   [~DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 10 
   [*DeviceA-100GE1/0/2] quit
   [~DeviceA] interface 100geint 1/0/1
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/1] port link-type hybrid
   [*DeviceA-100GE1/0/1] port hybrid pvid vlan 10
   [*DeviceA-100GE1/0/1] port hybrid untagged vlan 10
   [*DeviceA-100GE1/0/1] quit
   [~DeviceA] commit
   ```
2. # Configure MAC address flapping prevention on 100GE 1/0/1.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] mac-address learning priority 2
   [*DeviceA-100GE1/0/1] quit
   [~DeviceA] undo mac-address learning priority 2 allow-flapping
   [~DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display current-configuration** command in any view to check whether the MAC address learning priority of the interface is correct.

```
[~DeviceA]  display current-configuration interface 100ge 1/0/1
#
interface 100GE1/0/1
 port link-type hybrid
 port hybrid pvid vlan 10  
 port hybrid untagged vlan 10
 mac-address learning priority 2
#
return
```

#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 10
undo mac-address learning priority 2 allow-flapping
#
interface 100GE1/0/1
 port link-type hybrid
 port hybrid pvid vlan 10  
 port hybrid untagged vlan 10
 mac-address learning priority 2
#
interface 100GE1/0/2
 port link-type trunk
 port trunk allow-pass vlan 10
#
return
```