Example for Configuring Ethernet Sub-interfaces to Support Communication Between VLANs
======================================================================================

You can configure Ethernet sub-interfaces to enable users in different VLANs and network segments to communicate with each other.

#### Networking Requirements

Users in different communities and network segments require the same services, such as Internet, IPTV, and VoIP services. The network administrator in each community configures a VLAN for each service to simplify management. After the configuration, users in different communities belong to different VLANs, but the users need to communicate with each other for the same services.

On the network shown in [Figure 1](#EN-US_TASK_0172362797__fig_dc_vrp_ethernet_cfg_001601), users in communities 1 to 4 belong to different VLANs and network segments but all require the Internet service. These users must be able to communicate with each other.

**Figure 1** Network diagram of configuring Ethernet sub-interfaces for inter-VLAN communication![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, subinterface1.1, subinterface1.2, subinterface2.1, subinterface2.2 represent GE0/1/1.1, GE0/1/1.2, GE0/2/1.1, and GE0/2/1.2, respectively.


  
![](images/fig_dc_vrp_ethernet_cfg_001601.png)

#### Precautions

IP addresses of hosts in a VLAN must be in the same network segment as the IP address of the PE sub-interface associated with the VLAN.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create sub-interfaces on the PE and associate the sub-interfaces with VLANs so that the sub-interfaces can identify packets carrying VLAN tags.
2. Assign an IP address to each sub-interface for communication at the network layer.

#### Data Preparation

To complete the configuration, you need the following data:

* VLAN IDs associated with the PE sub-interfaces
* VLAN IDs associated with the PE sub-interfaces

#### Procedure

1. Create sub-interfaces on the PE and associate the sub-interfaces with VLANs.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*PE-GigabitEthernet0/1/1.1] vlan-type dot1q 10
   ```
   ```
   [*PE-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/1/1.2
   ```
   ```
   [*PE-GigabitEthernet0/1/1.2] vlan-type dot1q 20
   ```
   ```
   [*PE-GigabitEthernet0/1/1.2] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/1.1
   ```
   ```
   [*PE-GigabitEthernet0/2/1.1] vlan-type dot1q 30
   ```
   ```
   [*PE-GigabitEthernet0/2/1.1] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/1.2
   ```
   ```
   [*PE-GigabitEthernet0/2/1.2] vlan-type dot1q 40
   ```
   ```
   [*PE-GigabitEthernet0/2/1.2] quit
   ```
2. Configure IP addresses.
   
   
   ```
   [*PE] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*PE-GigabitEthernet0/1/1.1] ip address 10.110.6.3 24
   ```
   ```
   [*PE-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/1/1.2
   ```
   ```
   [*PE-GigabitEthernet0/1/1.2] ip address 10.110.5.3 24
   ```
   ```
   [*PE-GigabitEthernet0/1/1.2] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/1.1
   ```
   ```
   [*PE-GigabitEthernet0/2/1.1] ip address 10.110.4.3 24
   ```
   ```
   [*PE-GigabitEthernet0/2/1.1] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/1.2
   ```
   ```
   [*PE-GigabitEthernet0/2/1.2] ip address 10.110.3.3 24
   ```
   ```
   [*PE-GigabitEthernet0/2/1.2] quit
   ```
   ```
   [*PE] commit
   ```
3. For detailed configurations on the switch, see the related Configuration Guide.
4. Verify the configuration.
   
   
   
   On PCs in VLAN 10, configure the IP address 10.110.6.3/24 of GE 0/1/1.1 as the default gateway address.
   
   On PCs in VLAN 20, configure the IP address 10.110.5.3/24 of GE 0/1/1.2 as the default gateway address.
   
   On PCs in VLAN 30, configure the IP address 10.110.4.3/24 of GE 0/2/1.1 as the default gateway address.
   
   On PCs in VLAN 40, configure the IP address 10.110.3.3/24 of GE 0/2/1.2 as the default gateway address.
   
   After the configurations are complete, PCs in VLANs 10, 20, 30, and 40 can ping each other.

#### PE Configuration File

```
#
sysname PE
#
interface GigabitEthernet0/1/1
 undo shutdown
#
interface GigabitEthernet0/1/1.1
 vlan-type dot1q 10
 ip address 10.110.6.3 255.255.255.0
#
interface GigabitEthernet0/1/1.2
 vlan-type dot1q 20
 ip address 10.110.5.3 255.255.255.0
#
interface GigabitEthernet0/2/1
 undo shutdown
#
interface GigabitEthernet0/2/1.1
 vlan-type dot1q 30
 ip address 10.110.4.3 255.255.255.0
#
interface GigabitEthernet0/2/1.2
 vlan-type dot1q 40
 ip address 10.110.3.3 255.255.255.0
#
return
```