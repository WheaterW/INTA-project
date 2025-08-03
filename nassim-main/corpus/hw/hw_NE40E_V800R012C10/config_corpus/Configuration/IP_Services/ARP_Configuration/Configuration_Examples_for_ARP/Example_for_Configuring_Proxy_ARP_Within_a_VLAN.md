Example for Configuring Proxy ARP Within a VLAN
===============================================

If user isolation is configured for different users in the same virtual local area network (VLAN), the users cannot communicate with each other. To resolve this problem, you can configure proxy Address Resolution Protocol (ARP) for the VLAN.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364520__fig_dc_vrp_arp_cfg_206301), CE is connected to the sub-interface Eth-Trunk 1.1 of PE. Eth-Trunk 1.1 is associated with VLAN 10.

Host A and Host B are two users connected with CE. On CE, the interfaces connected with Host A and Host B belong to the same VLAN. User isolation in a VLAN is configured on CE.

To implement communication between Host A and Host B, enable proxy ARP within a VLAN on Eth-Trunk 1.1 of PE.

**Figure 1** Configuring proxy ARP within a VLAN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](figure/en-us_image_0000001577331473.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN on the CE and configure the users that need to communicate with each other to belong to the same VLAN.
2. Create Eth-Trunk 1.1 on the PE and configure an IP address for the interface as the gateway IP address.
3. Associate Eth-Trunk 1.1 with VLAN 10.
4. Enable proxy ARP on Eth-Trunk 1.1 so that isolated users in VLAN 10 can communicate with each other.

#### Data Preparation

To complete the configuration, you need the following data:

* ID of the VLAN to which hosts belong: 10
* IP address of Eth-Trunk 1.1: 10.10.10.1/24
* ID of the VLAN associated with Eth-Trunk 1.1: 10
* Host A's IP address: 10.10.10.2/24; Host B's IP address: 10.10.10.3/24

#### Procedure

1. Create VLANs on CEs and determine the VLANs to which users belong.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE] vlan 10
   ```
   ```
   [*CE-vlan 10] commit
   ```
   ```
   [~CE-vlan 10] quit
   ```
   ```
   [~CE] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/1] port default vlan 10
   ```
   ```
   [*CE-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [~CE] interface gigabitethernet 0/1/2
   ```
   ```
   [~CE-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/2] port default vlan 10
   ```
   ```
   [*CE-GigabitEthernet0/1/2] commit
   ```
   ```
   [~CE-GigabitEthernet0/1/2] quit
   ```
   ```
   [~CE] vlan 10
   ```
   ```
   [*CE-vlan 10] port isolate gigabitethernet 0/1/1 gigabitethernet 0/1/2
   ```
   ```
   [*CE-vlan 10] commit
   ```
   ```
   [~CE-vlan 10] quit
   ```
2. On CE, configure the trunk interface GE 0/1/3 to allow VLAN 10 to pass through.
   
   
   ```
   [~CE] interface gigabitethernet 0/1/3
   ```
   ```
   [~CE-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/3] port link-type trunk
   ```
   ```
   [*CE-GigabitEthernet0/1/3] port trunk allow-pass vlan 10
   ```
   ```
   [*CE-GigabitEthernet0/1/3] commit
   ```
   ```
   [~CE-GigabitEthernet0/1/3] quit
   ```
3. Create Eth-Trunk 1.1 on the PE and configure an IP address for Eth-Trunk 1.1.
   
   
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
   [~PE] interface eth-trunk 1.1
   ```
   ```
   [*PE-Eth-Trunk1.1] ip address 10.10.10.1 255.255.255.0
   ```
   ```
   [*PE-Eth-Trunk1.1] commit
   ```
4. Configure IP addresses for Host A and Host B.
   
   
   
   # Configure IP addresses for Host A and Host B. The IP addresses must be in the same network segment with the IP address of Eth-Trunk 1.1.
   
   After successful configuration, Host A and Host B can ping the PE, but cannot ping each other.
5. Associate Eth-Trunk 1.1 with VLAN 10.
   
   
   ```
   [~PE-Eth-Trunk1.1] vlan-type dot1q 10
   ```
   ```
   [*PE-Eth-Trunk1.1] commit
   ```
6. Enable proxy ARP in VLAN 10 on Eth-Trunk 1.1.
   
   
   ```
   [~PE-Eth-Trunk1.1] arp-proxy inner-sub-vlan-proxy enable
   ```
   ```
   [*PE-Eth-Trunk1.1] commit
   ```
7. Verify the configuration.
   
   
   
   Host A and Host B can ping each other.

#### Configuration Files

* PE configuration file
  
  ```
  #
  sysname PE
  #
  interface Eth-Trunk1
   undo shutdown
  #
  interface Eth-Trunk1.1
   undo shutdown
   vlan-type dot1q 10
   ip address 10.10.10.1 255.255.255.0
   arp-proxy inner-sub-vlan-proxy enable
  #
  return
  ```
* CE configuration file
  
  ```
  #
  sysname CE
  #
  vlan 10
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port default vlan 10
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port default vlan 10
  #
  vlan 10
   port isolate GigabitEthernet0/1/1 GigabitEthernet0/1/2
  #
  interface GigabitEthernet0/1/3 
   portswitch 
   undo shutdown 
   port link-type trunk 
   port trunk allow-pass vlan 10
  #
  return
  ```