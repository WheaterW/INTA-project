Example for Configuring Eth-Trunk Sub-interfaces to Support Communication Between VLANs
=======================================================================================

This example is applicable to the communication between users on different network segments and in different VLANs. In addition, the configuration in this example improves the bandwidth and therefore ensures the communication quality between users.

#### Networking Requirements

Users in different communities and on different network segments require the same services, such as Internet, IPTV, and VoIP services. The network administrator in each community configures a VLAN for each service to simplify management. After the configuration, users in different communities belong to different VLANs, but the users need to communicate with each other for the same services. In addition, traffic load balancing must be implemented and link bandwidth improved to ensure communication quality.

On the network shown in [Figure 1](#EN-US_TASK_0172362936__fig_dc_vrp_ethtrunk_cfg_002401), users in communities 1 and 2 belong to different VLANs and network segments but all require the Internet service. These users must be able to communicate with each other.

**Figure 1** Networking for configuring Eth-Trunk sub-interfaces to support communication between VLANs![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/1 and GE0/2/1, respectively.


  
![](figure/en-us_image_0257440148.png)

#### Precautions

* The host IP addresses in VLAN 10 and the IP address of Eth-Trunk1.2 must be on the same network segment.
* The host IP addresses in VLAN 20 and the IP address of Eth-Trunk1.1 must be on the same network segment.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Eth-Trunk sub-interface on each PE and assign an IP address to the sub-interface for Layer 3 routability.
2. Configure 802.1Q as the encapsulation mode for each Eth-Trunk sub-interface and associate each sub-interface with a VLAN, so that Eth-Trunk sub-interfaces can provide access services for users in different VLANs.
3. Verify the configuration.

#### Data Preparation

To complete the configuration, you need the following data:

* IDs of Eth-Trunk interfaces and their member interfaces on the PE
* Associated VLAN IDs and IP addresses of Eth-Trunk sub-interfaces on the PE
* IDs of Eth-Trunk interfaces and their member interfaces on the switch

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For details about how to configure the switch, see the related switch configuration guide.



#### Procedure

1. Create Eth-Trunk sub-interfaces and assign IP addresses to them.
   
   
   
   # Configure the PE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE
   ```
   ```
   [*HUAWEI] commit
   ```
   
   # Create Eth-Trunk1.
   
   ```
   [~PE] interface eth-trunk 1
   ```
   ```
   [*PE-Eth-Trunk1] quit
   ```
   
   # Add GE0/1/1 and GE0/2/1 to Eth-Trunk1.
   
   ```
   [*PE] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/1/1] eth-trunk 1
   ```
   ```
   [*PE-GigabitEthernet0/1/1] commit
   ```
   ```
   [*PE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/2/1] eth-trunk 1
   ```
   ```
   [*PE-GigabitEthernet0/2/1] commit
   ```
   ```
   [*PE-GigabitEthernet0/2/1] quit
   ```
   
   # Create Eth-Trunk1.1 and assign an IP address to it.
   
   ```
   [*PE] interface eth-trunk 1.1
   ```
   ```
   [*PE-Eth-Trunk1.1] ip address 10.110.1.10 24
   ```
   
   # Create Eth-Trunk1.2 and assign an IP address to it.
   
   ```
   [*PE] interface eth-trunk 1.2
   ```
   ```
   [*PE-Eth-Trunk1.2] ip address 10.110.2.10 24
   ```
2. Configure an encapsulation mode for each Eth-Trunk sub-interface and associate the sub-interfaces with VLANs.
   
   
   
   # Encapsulate Eth-Trunk1.1 with 802.1Q and associate it with VLAN 20.
   
   ```
   [*PE-Eth-Trunk1.1] vlan-type dot1q 20
   ```
   ```
   [*PE-Eth-Trunk1.1] commit
   ```
   ```
   [~PE-Eth-Trunk1.1] quit
   ```
   
   # Encapsulate Eth-Trunk1.2 with 802.1Q and associate it with VLAN 10.
   
   ```
   [*PE-Eth-Trunk1.2] vlan-type dot1q 10
   ```
   ```
   [*PE-Eth-Trunk1.2] commit
   ```
   ```
   [~PE-Eth-Trunk1.2] quit
   ```
3. Verify the configuration.
   
   
   
   Assign IP addresses on the same network segment as the IP address of Eth-Trunk1.2 to the hosts in VLAN 10, and set the default gateway address to 10.110.2.10/24, which is the IP address of Eth-Trunk1.2.
   
   Assign IP addresses on the same network segment as the IP address of Eth-Trunk1.1 to the hosts in VLAN 20, and set the default gateway address to 10.110.1.10/24, which is the IP address of Eth-Trunk1.1.
   
   After the configuration, the hosts in VLAN 10 and VLAN 20 can ping each other successfully.

#### PE configuration file

```
#
sysname PE
#
interface Eth-Trunk1
 #
interface Eth-Trunk1.1
 vlan-type dot1q 20
 ip address 10.110.1.10 255.255.255.0
#
interface Eth-Trunk1.2
 vlan-type dot1q 10
 ip address 10.110.2.10 255.255.255.0
#
interface GigabitEthernet0/1/1
 undo shutdown
 eth-trunk 1
#
interface GigabitEthernet0/2/1
 undo shutdown
 eth-trunk 1
#
return
```