Example for Configuring Layer 2 Multicast Entry Limit in a VLAN Scenario
========================================================================

This section provides an example for configuring Layer 2 multicast entry limit in a VLAN scenario.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367991__fig_dc_vrp_l2mc_cfg_005801), IPTV services are deployed on the VLAN network, and a CE is connected to the upper layer network through a PE and finally accesses the IPTV server. The CE is downlinked to a residential network VLAN 100.

To reduce the pressure on physical link bandwidth on the VLAN, configure a multicast entry limit for the VLAN on the CE as required to limit the number of multicast groups after fully evaluating the network capability and requirements. This ensures high IPTV service quality for users in the downstream VLAN.

The required Layer 2 multicast entry limit configurations on the CE are as follows:

* A maximum of 10 multicast group members can join VLAN 100.
* Limit the number of multicast groups on the downstream interface GE 0/1/1 as follows:
  + Limit the number of multicast groups in VLAN 100 to 10.

**Figure 1** Configuring Layer 2 multicast entry limit in a VLAN scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/1.


  
![](images/fig_dc_vrp_l2mc_cfg_005801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VLAN 100 on the CE so that downstream subscribers can receive multicast data.
2. Enable IGMP snooping globally and in the VLAN to implement on-demand multicast data distribution in the VLAN and reduce bandwidth consumption at both the user side and network side.
3. Configure Layer 2 multicast entry limit for VLAN 100 and for GE 0/1/1 to control the multicast group numbers.

#### Data Preparation

To complete the configuration, you need the following data:

* VLAN ID of the residential network attached to the CE: 100
* Maximum numbers of Layer 2 multicast entries

#### Procedure

1. Configure a VLAN.
   
   
   
   # Configure VLAN 100 on the CE.
   
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
   [~CE] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE] vlan 100
   ```
   ```
   [*CE-vlan100] port gigabitethernet 0/1/1
   ```
   ```
   [*CE-vlan100] quit
   ```
   ```
   [*CE] commit
   ```
2. Enable IGMP snooping.
   
   
   
   # Enable IGMP snooping globally on the CE.
   
   ```
   [~CE] igmp-snooping enable
   ```
   ```
   [*CE] commit
   ```
   
   # Enable IGMP snooping in VLAN 100.
   
   ```
   [~CE] vlan 100
   ```
   ```
   [~CE-vlan100] igmp-snooping enable
   ```
   ```
   [*CE-vlan100] quit
   ```
   ```
   [*CE] commit
   ```
3. Configure a multicast entry limit for the VLAN.
   
   
   
   # Configure the CE.
   
   ```
   [~CE] l2-multicast limit max-entry 10 vlan 100
   ```
   ```
   [*CE] commit
   ```
4. Configure a limit on the number of multicast groups for GE0/1/1.
   
   
   
   # Configure a multicast entry limit on GE 0/1/1 of the CE.
   
   ```
   [~CE] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE-GigabitEthernet0/1/1] l2-multicast limit max-entry 10 vlan 100
   ```
   ```
   [*CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE] commit
   ```
5. Verify the configuration.
   
   
   
   After completing the configurations, run the **display l2-multicast limit** command on the CE. The command output shows Layer 2 multicast entry limit configurations.
   
   ```
   [~CE] display l2-multicast limit
   ```
   ```
   L2-multicast limit information
   ------------------------------------------------------------------------------
                                                  ConfigEntries 
                                                  CurrentEntries
   ------------------------------------------------------------------------------
   VLAN 100 limit information:
   ------------------------------------------------------------------------------
                                                  10           
                                                  0  
   interface GigabitEthernet0/1/1 VLAN 100 limit information:
   ------------------------------------------------------------------------------
                                                  10           
                                                  0
   
   ```

#### Configuration Files

* CE configuration file
  
  ```
  #
  sysname CE
  #
  vlan batch 100
  #
  igmp-snooping enable
  l2-multicast limit max-entry 10 vlan 100
  #
  vlan 100
   igmp-snooping enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port default vlan 100
   l2-multicast limit max-entry 10 vlan 100
  #
  return
  ```