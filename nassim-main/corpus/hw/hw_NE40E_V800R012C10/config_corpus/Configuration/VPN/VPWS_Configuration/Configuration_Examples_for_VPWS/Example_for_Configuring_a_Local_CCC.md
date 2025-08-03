Example for Configuring a Local CCC
===================================

A local Circuit Cross Connect (CCC) is a connection between two CEs connected to the same PE. The PE functions similar to a Layer 2 switch to directly transmit packets without using LSPs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369905__fig_dc_vrp_vpws_cfg_301301), the CEs and PE are connected through GigabitEthernet interfaces.

A local CCC is set up between CE1 and CE2.

**Figure 1** Networking for a local CCC![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 and 2 represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_vpws_cfg_301301.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic MPLS functions on the PE and enable MPLS L2VPN.
2. Establish a local CCC between CE1 and CE2 on the PE. A local CCC is bidirectional, and only one connection is required.

#### Data Preparation

No data is required except interface IP addresses.


#### Procedure

1. Configure CEs.
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure CE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE2] interface gigabitethernet 0/1/0
   ```
   ```
   [~CE2-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~CE2-GigabitEthernet0/1/0] quit
   ```
2. Configure the PE.
   
   
   
   # Configure an LSR ID and enable MPLS and MPLS L2VPN.
   
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
   [~PE] interface loopback 1
   ```
   ```
   [*PE-LoopBack1] ip address 1.1.1.9 32
   ```
   ```
   [*PE-LoopBack1] quit
   ```
   ```
   [*PE] mpls lsr-id 1.1.1.9
   ```
   ```
   [*PE] mpls
   ```
   ```
   [*PE-mpls] quit
   ```
   ```
   [*PE] mpls l2vpn
   ```
   ```
   [*PE-l2vpn] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE-GigabitEthernet0/2/0] quit
   ```
   
   # Establish a local CCC between CE1 and CE2.
   
   ```
   [~PE] ccc ce1-ce2 interface gigabitethernet 0/1/0 out-interface gigabitethernet 0/2/0
   ```
   ```
   [*PE] commit
   ```
3. Verify the configuration.
   
   
   
   After completing the configurations, check CCC information on the PE. The command output shows that a local CCC has been established and its status is Up.
   
   ```
   <PE> display vll ccc
   ```
   ```
   total  ccc vc : 1
   local  ccc vc : 1,  1 up
   remote ccc vc : 0,  0 up
   
   name: ce1-ce2, type: local, state: up,
   intf1: GigabitEthernet0/1/0 (up),access-port: false
   
   intf2: GigabitEthernet0/2/0 (up),access-port: false
   VC last up time : 2012/03/08 05:13:10
   VC total up time:  0 days, 0 hours, 0 minutes, 14 seconds 
   ```
   
   Run the **display l2vpn ccc-interface vc-type all** command. The command output shows that the VC type is **ccc** and the VC status is **up**.
   
   ```
   <PE> display l2vpn ccc-interface vc-type all
   ```
   ```
   Total ccc-interface of CCC: 2
   up (2), down (0)
   Interface                     Encap Type               State     VC Type
   GigabitEthernet0/1/0                      ethernet                      up        ccc
   GigabitEthernet0/2/0                      ethernet                      up        ccc
   ```
   ```
   <CE1> ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=4 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=2 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=1 ms
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/1/4 ms
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  return
  ```
* Configuration file of the PE
  
  ```
  #
  sysname PE
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls l2vpn
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  ccc ce1-ce2 interface GigabitEthernet0/1/0 out-interface GigabitEthernet0/2/0
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```