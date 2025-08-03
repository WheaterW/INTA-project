Example for Configuring Dual-ended Packet Loss Measurement in BD EVPN Networking
================================================================================

This section provides an example for configuring dual-ended packet loss measurement in BD EVPN networking.

#### Networking Requirements

As networks rapidly develop and applications diversify, various value-added services, such as IPTV, video conferencing, and VoIP, are widely deployed. A link connectivity fault or network performance deterioration directly affects services on a live network. Therefore, performance monitoring is especially important for service transport.

As shown in [Figure 1](#EN-US_TASK_0236138932__fig_dc_vrp_cfg_01153201), PE1 and PE2 are connected through an EVPN, and CE1 and CE2 are connected to the EVPN through a BD. MAC address learning is configured between each PE and its attached CE. To provide high-quality voice services, a carrier expects to monitor packet loss performance on mobile transport links in real time while monitoring link connectivity so that they can promptly respond to calling service quality deterioration.

**Figure 1** Configuring Y.1731 functions in BD EVPN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0236138935.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

Configure dual-ended packet loss measurement for the AC link between each PE and its attached CE to continuously collect packet loss statistics.


#### Data Preparation

To complete the configuration, you need the following data:

* ID of the VLAN to which each CE interface belongs
* EVPN instance name (**evpna**), RT value, and RD value configured on each PE
* Names of the MD and MA on CE1 and PE1 and on CE2 and PE2 when basic CFM functions are configured

* Interval at which LMMs are sent

#### Procedure

1. Configure access to an EVPN through a BD. An EVPN is configured between PE1 and PE2. CE1 and CE2 access the EVPN network through a BD. For details, see the [Configuring EVPN VPLS over MPLS (BD EVPN Instance)](dc_vrp_evpn_cfg_0065.html) or configuration files in this configuration example.
2. Configure basic Ethernet CFM functions and specify the MEP type as outward.
   
   
   
   Configure basic Ethernet CFM functions on the CEs and PEs. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md1** and an MA named **ma1**.
   
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
   [~CE1] interface gigabitethernet0/1/1
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] cfm enable
   ```
   ```
   [*CE1] cfm md md1
   ```
   ```
   [*CE1-md-md1] ma ma1
   ```
   ```
   [*CE1-md-md1-ma-ma1] map vlan 2
   ```
   ```
   [*CE1-md-md1-ma-ma1] mep mep-id 2 interface gigabitethernet0/1/1 outward
   ```
   ```
   [*CE1-md-md1-ma-ma1] mep ccm-send mep-id 2 enable
   ```
   ```
   [*CE1-md-md1-ma-ma1] remote-mep mep-id 1
   ```
   ```
   [*CE1-md-md1-ma-ma1] remote-mep ccm-receive mep-id 1 enable
   ```
   ```
   [*CE1-md-md1-ma-ma1] test-id 1 mep 2 remote-mep 1
   ```
   ```
   [*CE1-md-md1-ma-ma1] commit
   ```
   
   # Configure PE1.
   
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
   [~PE1] cfm enable
   ```
   ```
   [*PE1] commit
   ```
   ```
   [~PE1] cfm md md1
   ```
   ```
   [*PE1-md-md1] ma ma1
   ```
   ```
   [*PE1-md-md1-ma-ma1] map bridge-domain 10
   ```
   ```
   [*PE1-md-md1-ma-ma1] mep mep-id 1 interface gigabitethernet0/1/1.1 vlan 2 outward
   ```
   ```
   [*PE1-md-md1-ma-ma1] mep ccm-send mep-id 1 enable
   ```
   ```
   [*PE1-md-md1-ma-ma1] remote-mep mep-id 2
   ```
   ```
   [*PE1-md-md1-ma-ma1] remote-mep ccm-receive mep-id 2 enable
   ```
   ```
   [*PE1-md-md1-ma-ma1] test-id 1 mep 1 remote-mep 2
   ```
   ```
   [*PE1-md-md1-ma-ma1] commit
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
   [~CE2] interface gigabitethernet0/1/1
   ```
   ```
   [~CE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] cfm enable
   ```
   ```
   [*CE2] cfm md md1
   ```
   ```
   [*CE2-md-md1] ma ma1
   ```
   ```
   [*CE2-md-md1-ma-ma2] map vlan 2
   ```
   ```
   [*CE2-md-md1-ma-ma2] mep mep-id 4 interface gigabitethernet0/1/1 outward
   ```
   ```
   [*CE2-md-md1-ma-ma2] mep ccm-send mep-id 4 enable
   ```
   ```
   [*CE2-md-md1-ma-ma2] remote-mep mep-id 3
   ```
   ```
   [*CE2-md-md1-ma-ma2] remote-mep ccm-receive mep-id 3 enable
   ```
   ```
   [*CE2-md-md1-ma-ma2] test-id 2 mep 4 remote-mep 3
   ```
   ```
   [*CE2-md-md1-ma-ma2] commit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] cfm enable
   ```
   ```
   [*PE2] commit
   ```
   ```
   [~PE2] cfm md md1
   ```
   ```
   [*PE2-md-md1] ma ma1
   ```
   ```
   [*PE2-md-md1-ma-ma1] map bridge-domain 10
   ```
   ```
   [*PE2-md-md1-ma-ma1] mep mep-id 3 interface gigabitethernet0/1/1.1 vlan 2 outward
   ```
   ```
   [*PE2-md-md1-ma-ma1] mep ccm-send mep-id 3 enable
   ```
   ```
   [*PE2-md-md1-ma-ma1] remote-mep mep-id 4
   ```
   ```
   [*PE2-md-md1-ma-ma1] remote-mep ccm-receive mep-id 4 enable
   ```
   ```
   [*PE2-md-md1-ma-ma1] test-id 2 mep 3 remote-mep 4
   ```
   ```
   [*PE2-md-md1-ma-ma1] commit
   ```
3. Configure dual-ended packet loss measurement.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1-md-md1-ma-ma1] loss-measure dual-ended continual test-id 1
   ```
   ```
   [*CE1-md-md1-ma-ma1] quit
   ```
   ```
   [*CE1-md-md1] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1-md-md1-ma-ma1] loss-measure dual-ended continual test-id 1
   ```
   ```
   [*PE1-md-md1-ma-ma1] quit
   ```
   ```
   [*PE1-md-md1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2-md-md1-ma-ma1] loss-measure dual-ended continual test-id 2
   ```
   ```
   [*CE2-md-md1-ma-ma1] quit
   ```
   ```
   [*CE2-md-md1] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2-md-md1-ma-ma1] loss-measure dual-ended continual test-id 2
   ```
   ```
   [*PE2-md-md1-ma-ma1] quit
   ```
   ```
   [*PE2-md-md1] quit
   ```
   ```
   [*PE2] commit
   ```
4. Verify the configuration.
   
   
   
   After the configuration is complete, run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on CE1 to check statistics about dual-ended packet loss.
   
   ```
   [~CE1] display y1731 statistic-type dual-loss
   Latest dual-ended loss statistics of test-id 1:
   --------------------------------------------------------------------------------
   Index    Local-loss    Local-loss ratio    Remote-loss    Remote-loss ratio
   --------------------------------------------------------------------------------
       1             0             0.0000%              0              0.0000%
       2             0             0.0000%              0              0.0000%
       3             0             0.0000%              0              0.0000%
       4             0             0.0000%              0              0.0000%
       5             0             0.0000%              0              0.0000%
       6             0             0.0000%              0              0.0000%
       7             0             0.0000%              0              0.0000%
       8             0             0.0000%              0              0.0000%
       9             0             0.0000%              0              0.0000%
      10             0             0.0000%              0              0.0000%
   --------------------------------------------------------------------------------
   Average Local-loss  :          0    Average Local-loss Ratio  :   0.0000%
   Maximum Local-loss  :          0    Maximum Local-loss Ratio  :   0.0000%
   Minimum Local-loss  :          0    Minimum Local-loss Ratio  :   0.0000%
   Average Remote-loss :          0    Average Remote-loss Ratio :   0.0000%
   Maximum Remote-loss :          0    Maximum Remote-loss Ratio :   0.0000%
   Minimum Remote-loss :          0    Minimum Remote-loss Ratio :   0.0000%
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  vlan batch 2
  #
  cfm version standard
  cfm enable
  #
  interface GigabitEthernet0/1/1
    portswitch
    undo shutdown
    port trunk allow-pass vlan 2
  #
  cfm md md1
   ma ma1
    map vlan 2
    mep mep-id 2 interface GigabitEthernet0/1/1 outward
    mep ccm-send mep-id 2 enable
    remote-mep mep-id 1
    remote-mep ccm-receive mep-id 1 enable
    test-id 1 mep 2 remote-mep 1
    loss-measure dual-ended continual test-id 1
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  cfm enable
  #
  evpn vpn-instance evpna bd-mode
    route-distinguisher 100:1
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  bridge-domain 10 
    evpn binding vpn-instance evpna
  #
  interface GigabitEthernet0/1/1.1 mode l2
    encapsulation dot1q vid 2
    rewrite pop single
    bridge-domain 10
  #
  cfm md md1
    ma ma1
     map bridge-domain 10
     mep mep-id 1 interface GigabitEthernet0/1/1.1 vlan 2 outward
     mep ccm-send mep-id 1 enable
     remote-mep mep-id 2
     remote-mep ccm-receive mep-id 2 enable
     test-id 1 mep 1 remote-mep 2
     loss-measure dual-ended continual test-id 1
  #                                              
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  vlan batch 2
  #
  cfm version standard
  cfm enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port trunk allow-pass vlan 2
  #
  cfm md md1
   ma ma1
    map vlan 2
    mep mep-id 4 interface GigabitEthernet0/1/1 outward
    mep ccm-send mep-id 4 enable
    remote-mep mep-id 3
    remote-mep ccm-receive mep-id 3 enable
    test-id 2 mep 4 remote-mep 3
    loss-measure dual-ended continual test-id 2
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  cfm enable
  #
   evpn vpn-instance evpna bd-mode
    route-distinguisher 200:1
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  bridge-domain 10 
    evpn binding vpn-instance evpna
  #
  interface GigabitEthernet0/1/1.1 mode l2
    encapsulation dot1q vid 2
    rewrite pop single
    bridge-domain 10
  #
  cfm md md1
  ma ma1
    map bridge-domain 10
    mep mep-id 1 interface GigabitEthernet0/1/1.1 vlan 2 outward
    mep ccm-send mep-id 3 enable
    remote-mep mep-id 4
    remote-mep ccm-receive mep-id 4 enable
    test-id 2 mep 3 remote-mep 4
    loss-measure dual-ended continual test-id 2
  #                                              
  return
  ```