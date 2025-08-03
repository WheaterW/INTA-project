Example for Disabling MAC Address Learning on an Interface
==========================================================

Example for Disabling MAC Address Learning on an Interface

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176664489__fig_dc_cfg_mac_006401), user networks 1 and 2 belong to VLAN 10 and VLAN 20, respectively. The two user networks are connected to DeviceA through DeviceB, and DeviceA is connected to DeviceB through 100GE 1/0/1. To prevent attackers from attacking DeviceA with a large number of packets containing forged source MAC addresses, disable MAC address learning on DeviceA's 100GE 1/0/1.

**Figure 1** Networking for disabling MAC address learning on an interface![](public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001130624962.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLANs and add 100GE 1/0/1 to them to implement Layer 2 forwarding.
2. Disable MAC address learning on 100GE 1/0/1 to prevent MAC address attacks.

#### Procedure

1. Create VLANs and add 100GE 1/0/1 to them.
   
   
   
   # Add 100GE 1/0/1 to VLAN 10 and VLAN 20.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10 20
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
2. Disable MAC address learning on 100GE 1/0/1.
   
   
   
   # Disable MAC address learning on 100GE 1/0/1, and set an action to discard packets with unknown MAC addresses.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] mac-address learning disable action discard
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display current-configuration interface** command in any view to check whether MAC address learning has been disabled.

```
[~DeviceA] display current-configuration interface 100ge 1/0/1
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10 20
 mac-address learning disable action discard
#
return
```

#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 10 20
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10 20
 mac-address learning disable action discard
#
return
```