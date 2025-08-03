Example for Configuring Layer 2 Multicast SSM Mapping
=====================================================

This section provides an example for configuring Layer 2 multicast SSM mapping.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367975__fig_dc_vrp_l2mc_cfg_003701), GE0/1/0 on PE1 is connected to PE2 and belongs to VLAN 10. GE 0/1/0 on PE2 is a static router port.

IGMPv3 is running on PE1 while IGMPv2 is running on PE2.

Then, SSM mapping needs to be configured on PE1 so that PE1 can map the multicast group addresses of the received packets with no source addresses to specific sources. In addition, the querier function needs to be enabled for VLAN 10 on PE1 so that PE1 can send Query messages periodically to PE2.

**Figure 1** Networking diagram of Layer 2 multicast SSM mapping![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/1/1, respectively.


  
![](images/fig_dc_vrp_l2mc_cfg_003701.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLANs and enable basic IGMP snooping functions.
2. Configure the version numbers of IGMP snooping running on PE1 and PE2.
3. Enable the querier function for VLAN 10 on PE1.
4. Configure GE 0/1/0 on PE2 as a static router port.
5. Configure an IGMP snooping SSM policy.

#### Data Preparation

To complete the configuration, you need the following data:

* VLAN ID: 10
* IGMP snooping version number: 3 on PE1 and 2 on PE2
* Static multicast group address: 224.1.1.1

#### Procedure

1. Create VLANs.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet0/1/0
   [~PE1-GigabitEthernet0/1/0] portswitch
   [*PE1-GigabitEthernet0/1/0] undo shutdown
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] vlan 10
   [*PE1-vlan10] port gigabitethernet 0/1/0
   [*PE1-vlan10] commit
   [~PE1-vlan10] quit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE2
   [*HUAWEI] commit
   [~PE2] interface gigabitethernet 0/1/0
   [~PE2-GigabitEthernet0/1/0] portswitch
   [*PE2-GigabitEthernet0/1/0] undo shutdown
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] vlan 10
   [*PE2-vlan10] port gigabitethernet 0/1/0
   [*PE2-vlan10] commit
   [~PE2-vlan10] quit
   ```
2. Enable global IGMP snooping and IGMP snooping in a VLAN.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] igmp-snooping enable
   [*PE1] vlan 10
   [*PE1-vlan10] igmp-snooping enable
   [*PE1-vlan10] commit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] igmp-snooping enable
   [*PE2] vlan 10
   [*PE2-vlan10] igmp-snooping enable
   [*PE2-vlan10] igmp-snooping report-suppress
   [*PE2-vlan10] commit
   ```
3. Configure the version numbers of IGMP snooping running on PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1-vlan10] igmp-snooping version 3
   ```
   ```
   [*PE1-vlan10] commit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2-vlan10] igmp-snooping version 2
   ```
   ```
   [*PE2-vlan10] commit
   ```
4. Enable the querier function for VLAN 10 on PE1 so that PE1 can send General Query messages to PE2.
   
   
   ```
   [~PE1] igmp-snooping send-query enable
   [*PE1] vlan 10
   [*PE1-vlan10] igmp-snooping querier enable
   [*PE1-vlan10] commit
   [~PE1-vlan10] quit
   ```
5. Configure GE 0/1/0 on PE2 as a static router port and statically add GE 0/1/1 on PE2 to the multicast group with group address being 224.1.1.1.
   
   
   ```
   [~PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] igmp-snooping static-router-port vlan 10 
   [*PE2] interface gigabitethernet 0/1/1
   [*PE2-GigabitEthernet0/1/1] portswitch
   [*PE2-GigabitEthernet0/1/1] undo shutdown
   [*PE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 10
   [*PE2-GigabitEthernet0/1/1] l2-multicast static-group group-address 224.1.1.1 vlan 10
   [*PE2-GigabitEthernet0/1/1] commit
   [~PE2-GigabitEthernet0/1/1] quit
   ```
6. Configure an IGMP snooping SSM policy.
   
   
   ```
   [~PE1] acl number 2008
   [*PE1-acl-basic-2008] rule 5 permit source 224.1.1.1 0
   [*PE1-acl-basic-2008] quit
   [*PE1] vlan 10 
   [*PE1-vlan10] igmp-snooping ssm-policy 2008
   [*PE1-vlan10] igmp-snooping ssm-mapping enable 
   [*PE1-vlan10] igmp-snooping ssm-mapping 224.1.1.1 24 10.1.1.2
   [*PE1-vlan10] igmp-snooping ssm-mapping 224.1.1.1 24 10.1.1.3
   [*PE1-vlan10] igmp-snooping ssm-mapping 224.1.1.1 24 10.1.1.4
   [*PE1-vlan10] commit
   ```
7. Verify the configuration.
   
   
   
   # Run the **display igmp-snooping vlan configuration** command on PE1 to view VLAN configurations.
   
   ```
   [~PE1] display igmp-snooping vlan configuration
    IGMP Snooping Configuration for VLAN 10
        igmp-snooping enable
        igmp-snooping version 3
        igmp-snooping querier enable
        igmp-snooping ssm-mapping enable
        igmp-snooping ssm-policy 2008
        igmp-snooping ssm-mapping 224.1.1.1 255.255.255.0 10.1.1.2
        igmp-snooping ssm-mapping 224.1.1.1 255.255.255.0 10.1.1.3
        igmp-snooping ssm-mapping 224.1.1.1 255.255.255.0 10.1.1.4
   ```
   
   # After PE1 receives a Report message, run the **display igmp-snooping port-info** command to check port information. In the command output, **Source** indicates a multicast source IP address, and **Group** indicates a multicast group IP address.
   
   ```
   [~PE1] display igmp-snooping port-info
    -----------------------------------------------------------------------------------
     Flag: S:Static     D:Dynamic     M:Ssm-mapping
           A:Active     P:Protocol    F:Fast-channel                                
                       (Source, Group)  Port                                      Flag
    -------------------------------------------------------------------------------
    VLAN 10, 3 Entry(s)
                  (10.1.1.2, 224.1.1.1)                                        P--
                                         GigabitEthernet0/1/0                  --M
                                                           1 port(s) include
                  (10.1.1.3, 224.1.1.1)                                        P--
                                         GigabitEthernet0/1/0                  --M
                                                           1 port(s) include
                  (10.1.1.4, 224.1.1.1)                                        P--
                                         GigabitEthernet0/1/0                  --M
                                                           1 port(s) include
    -------------------------------------------------------------------------------
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  vlan batch 10
  #
  igmp-snooping enable
  igmp-snooping send-query enable
  #
  vlan 10
   igmp-snooping enable
   igmp-snooping querier enable
   igmp-snooping ssm-mapping enable
   igmp-snooping version 3
   igmp-snooping ssm-policy 2008
   igmp-snooping ssm-mapping 224.1.1.1 255.255.255.0 10.1.1.2
   igmp-snooping ssm-mapping 224.1.1.1 255.255.255.0 10.1.1.3
   igmp-snooping ssm-mapping 224.1.1.1 255.255.255.0 10.1.1.4
  #
  acl number 2008
   rule 5 permit source 224.1.1.1 0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   portswitch
   port default vlan 10
  #
  return
  
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  vlan batch 10
  #
  igmp-snooping enable
  #
  vlan 10
   igmp-snooping enable
   igmp-snooping report-suppress
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   portswitch
   port default vlan 10
   igmp-snooping static-router-port vlan 10
  #   
  interface GigabitEthernet0/1/1
   undo shutdown
   portswitch
   port trunk allow-pass vlan 10
   l2-multicast static-group group-address 224.1.1.1 vlan 10
  #
  return
  ```