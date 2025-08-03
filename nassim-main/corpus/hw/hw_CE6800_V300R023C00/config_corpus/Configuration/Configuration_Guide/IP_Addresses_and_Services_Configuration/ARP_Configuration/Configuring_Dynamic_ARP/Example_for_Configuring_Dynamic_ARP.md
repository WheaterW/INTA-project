Example for Configuring Dynamic ARP
===================================

Example for Configuring Dynamic ARP

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130783828__fig_dc_cfg_arp_002101), interface 1 on DeviceA is connected to Server1, Server2, and Server3 through DeviceB, and interface 2 is connected to DeviceC and then to Server. The requirements are as follows:

* Interface 1 and interface 2 belong to VLAN 2 and VLAN 3, respectively.
* To adapt to rapid network changes and ensure correct packet forwarding, configure dynamic ARP parameters on VLANIF 2 of DeviceA.
* To ensure secure communication between DeviceA and Server and prevent invalid ARP messages from entering DeviceA, add a static ARP entry on VLANIF 3 of DeviceA. The IP and MAC addresses of DeviceC are 10.2.2.3 and 00e0-fc01-0000, respectively.

**Figure 1** Network diagram of configuring ARP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176743513.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLANs and add interfaces to the VLANs.
2. Configure dynamic ARP parameters for a user-side VLANIF interface.
3. Configure a static ARP entry.

#### Procedure

1. Create VLANs and add interfaces to the VLANs.
   
   # Create VLAN 2 and VLAN 3.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 2 3
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Add interface 1 to VLAN 2 and interface 2 to VLAN 3.
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE 1/0/1] portswitch
   [~DeviceA-100GE 1/0/1] port link-type trunk
   [~DeviceA-100GE 1/0/1] port trunk allow-pass vlan 2
   [~DeviceA-100GE 1/0/1] quit
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE 1/0/2] portswitch
   [~DeviceA-100GE 1/0/2] port link-type trunk
   [~DeviceA-100GE 1/0/2] port trunk allow-pass vlan 3
   [~DeviceA-100GE 1/0/2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure dynamic ARP parameters for a VLANIF interface.
   
   # Create VLANIF 2.
   ```
   [~DeviceA] interface vlanif 2
   ```
   
   # Configure an IP address for VLANIF 2.
   ```
   [*DeviceA-Vlanif2] ip address 10.1.1.1 255.255.255.0
   ```
   
   # Set the aging time of dynamic ARP entries to 60s.
   ```
   [*DeviceA-Vlanif2] arp timeout 60
   ```
   
   # Set the number of probes for aging dynamic ARP entries to 2.
   ```
   [*DeviceA-Vlanif2] arp detect times 2
   [*DeviceA-Vlanif2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure a static ARP entry.
   
   # Create VLANIF 3.
   ```
   [~DeviceA] interface vlanif 3
   ```
   
   # Configure an IP address for VLANIF 3.
   ```
   [*DeviceA-Vlanif3] ip address 10.2.2.2 255.255.255.0
   [*DeviceA-Vlanif3] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure a static ARP entry with the IP address 10.2.2.3, MAC address 00e0-fc01-0000, VLAN ID 3, and outbound interface 100GE 1/0/2.
   ```
   [~DeviceA] arp static 10.2.2.3 00e0-fc01-0000 vlan 3 interface 100ge 1/0/2
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] quit
   ```

#### Verifying the Configuration

# Run the **display current-configuration** command to check the aging time of dynamic ARP entries, number of probes for aging dynamic ARP entries, and static ARP entry information.

```
<DeviceA> display current-configuration | include arp
 arp detect times 2
 arp timeout 60
arp static 10.2.2.3 00e0-fc01-0000 vlan 3 interface 100GE1/0/2
```
#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 2 to 3
#
interface vlanif2
 ip address 10.1.1.1 255.255.255.0
 arp detect times 2
 arp timeout 60
#
interface vlanif3
 ip address 10.2.2.2 255.255.255.0
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 2
#
interface 100GE1/0/2
 port link-type trunk
 port trunk allow-pass vlan 3
#
arp static 10.2.2.3 00e0-fc01-0000 vlan 3 interface 100GE1/0/2
#
return
```