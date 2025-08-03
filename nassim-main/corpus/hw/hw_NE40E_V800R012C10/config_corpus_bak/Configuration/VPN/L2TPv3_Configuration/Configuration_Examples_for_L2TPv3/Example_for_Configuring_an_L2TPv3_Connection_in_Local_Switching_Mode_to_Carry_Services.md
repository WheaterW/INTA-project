Example for Configuring an L2TPv3 Connection in Local Switching Mode to Carry Services
======================================================================================

This section provides an example for configuring an L2TPv3 connection in local switching mode to forward service packets received from an EVC Layer 2 sub-interface. The packets are encapsulated using L2TPv3 and transparently transmitted.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369207__fig_037FBC9D), L2TPv3 enables PE1 to function as a local switching device to forward packets through an EVC Layer 2 sub-interface. This implementation allows CE1 and CE2 to exchange packets without using a VPN.![](../../../../public_sys-resources/note_3.0-en-us.png) 

An L2TPv3 connection in local switching mode supports the following service access modes: whole-interface mode, C-tag termination mode, S-tag termination mode, and S-tag+C-tag termination mode. The L2TPv3 tunnel configurations for different service access modes are similar. The following configuration example uses the C-tag termination mode.


**Figure 1** Networking for an L2TPv3 connection in local switching mode  
![](images/fig_dc_vrp_l2tpv3_cfg_000012.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| CE1 | GE0/1/1 | - |
| PE1 | GE0/1/1.4 | - |
| GE0/1/2.4 | - |
| CE2 | GE0/1/1 | - |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable L2TPv3.
2. Configure the inbound and outbound interfaces for the L2TPv3 PW.

#### Data Preparation

To complete the configuration, you need the following data:

* Types and numbers of L2TPv3 interfaces
* Configure the inbound and outbound interfaces for the L2TPv3 PW.

#### Procedure

1. Enable L2TPv3 on PE1.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] l2tpv3 enable
   ```
   ```
   [*PE1] commit
   ```
2. Configure L2TPv3 functions on PE1.
   
   
   
   # Configure PE1 to allow services to access the L2TPv3 PW in C-tag termination mode.
   
   ```
   [~PE1] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] rewrite pop single
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] commit
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/1.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/2/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE1-Gigabitethernet0/2/1.4] rewrite pop single
   ```
   ```
   [*PE1-Gigabitethernet0/2/1.4] commit
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] quit
   ```
   ```
   [*PE1] l2tpv3 local connection dot1q interface GigabitEthernet0/1/1.4 out-interface GigabitEthernet0/2/1.4
   ```
3. Configure a VLAN service on CE1.
   
   
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
   [~CE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] commit
   ```
4. Configure a VLAN service on CE2.
   
   
   ```
   [~CE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] commit
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  vlan 2
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  l2tpv3 enable
  l2tpv3 local connection dot1q interface GigabitEthernet0/1/1.4 out-interface GigabitEthernet0/2/1.4
  #
  interface GigabitEthernet0/1/1.4 mode l2
   encapsulation dot1q vid 2
   rewrite pop single
  #
  interface GigabitEthernet0/2/1.4 mode l2
   encapsulation dot1q vid 2
   rewrite pop single
  #
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  vlan 2
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
  #
  return
  ```