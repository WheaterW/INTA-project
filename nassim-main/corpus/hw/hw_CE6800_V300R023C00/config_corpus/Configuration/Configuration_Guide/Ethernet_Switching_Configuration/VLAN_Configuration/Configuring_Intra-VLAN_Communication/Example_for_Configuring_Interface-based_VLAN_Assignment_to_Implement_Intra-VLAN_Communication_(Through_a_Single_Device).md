Example for Configuring Interface-based VLAN Assignment to Implement Intra-VLAN Communication (Through a Single Device)
=======================================================================================================================

Example for Configuring Interface-based VLAN Assignment to Implement Intra-VLAN Communication (Through a Single Device)

#### Networking Requirements

On DeviceA in [Figure 1](#EN-US_TASK_0000001130622836__fig1940610568513), the interfaces connected to Host1 and Host2 are added to VLAN 2, and the interfaces connected to Host3 and Host4 are added to VLAN 3. With this configuration, hosts in the same VLAN can directly communicate with each other at Layer 2, but hosts in different VLANs cannot. Specifically:

* Host1 and Host2 can communicate with each other, and Host3 and Host4 can communicate with each other.
* Host1 and Host2 cannot communicate with Host3 and Host4 in VLAN 3.

**Figure 1** Networking diagram of configuring interface-based VLAN assignment for intra-VLAN communication through a single device![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001176742349.png)

#### Procedure

1. On DeviceA, create VLANs and configure the interfaces connected to the hosts as access interfaces.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2 3
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type access
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] portswitch
   [*DeviceA-100GE1/0/4] port link-type access
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] commit
   ```
2. Add interfaces to VLANs.
   
   
   
   # Add 100GE 1/0/1 and 100GE 1/0/2 to VLAN 2.
   
   ```
   [~DeviceA] vlan 2
   [*DeviceA-vlan2] port 100ge 1/0/1 to 1/0/2
   [*DeviceA-vlan2] quit
   [*DeviceA] commit
   ```
   
   # Add 100GE 1/0/3 and 100GE 1/0/4 to VLAN 3.
   
   ```
   [~DeviceA] vlan 3
   [*DeviceA-vlan3] port 100ge 1/0/3 to 1/0/4
   [*DeviceA-vlan3] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**display vlan**](cmdqueryname=display+vlan) command to check the VLAN status.

```
[~DeviceA] display vlan
The total number of vlans is : 2
--------------------------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
MAC-LRN: MAC-address learning;  STAT: Statistic;
BC: Broadcast; MC: Multicast;   UC: Unknown-unicast;
FWD: Forward;  DSD: Discard;
--------------------------------------------------------------------------------

VID          Ports
--------------------------------------------------------------------------------
   2         UT:100GE1/0/1(U)   100GE1/0/2(U)
   3         UT:100GE1/0/3(U)   100GE1/0/4(U)

VID  Type     Status  Property  MAC-LRN STAT    BC  MC  UC  Description
--------------------------------------------------------------------------------
   2 common   enable  default   enable  disable FWD FWD FWD VLAN 0002
   3 common   enable  default   enable  disable FWD FWD FWD VLAN 0003
```

# Hosts in VLAN 2 cannot ping hosts in VLAN 3, but those in the same VLAN can ping each other.


#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 2 to 3
#
interface 100GE1/0/1
 port default vlan 2
#
interface 100GE1/0/2
 port default vlan 2
#
interface 100GE1/0/3
 port default vlan 3
#
interface 100GE1/0/4
 port default vlan 3
#
return
```