Example for Configuring Dual-ended Frame Loss Measurement in VLAN Networking
============================================================================

This section provides an example showing how to configure dual-ended frame loss measurement in VLAN networking.

#### Networking Requirements

With the increasing popularization and wide application of the Internet, various value-added services such as IPTV, video conferencing, and VoIP services are widely deployed. Link connectivity and network performance determine the Quality of Services (QoS) on bearer networks. Therefore, performance monitoring is especially important for service transmission channels.

As shown in [Figure 1](#EN-US_TASK_0172362173__fig_dc_vrp_cfg_01154101), CFM is configured between CEs. To provide high-quality audio services, providers hope to monitor the frame loss over mobile bearer links in real time, while monitoring link connectivity. Monitoring the frame loss over mobile bearer links allows the providers to respond quickly to video service quality deterioration.

**Figure 1** Networking diagram for configuring Y.1731 function on a VLAN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example are GE 0/1/1, GE 0/1/2 respectively.


  
![](images/fig_dc_vrp_cfg_01154001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure dual-ended frame loss measurement for the end-to-end link between the CEs to collect frame loss statistics.


#### Data Preparation

To complete the configuration, you need the following data:

* ID of the VLAN to which each CE interface belongs
* Names of the MD and MA on CE1 and CE2
* Interval at which LMMs are sent

#### Procedure

1. Configure basic Ethernet CFM functions and specify the MEP type as outward.
   
   
   
   Configure basic Ethernet CFM functions on each CE. Specify the Ethernet CFM protocol in the version of IEEE Standard 802.1ag-2007. Create an MD named **md3** and an MA named **ma3**, and bind the MA to the VLAN.
   
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
   [~CE1] vlan 2
   ```
   ```
   [~CE1] interface gigabitethernet0/1/1
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] portswitch
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
   ```
   [~CE1] cfm enable
   ```
   ```
   [*CE1] cfm md md3
   ```
   ```
   [*CE1-md-md3] ma ma3
   ```
   ```
   [*CE1-md-md3-ma-ma3] map vlan 2
   ```
   ```
   [*CE1-md-md3-ma-ma3] mep mep-id 3 interface gigabitethernet0/1/1 outward
   ```
   ```
   [*CE1-md-md3-ma-ma3] mep ccm-send mep-id 3 enable
   ```
   ```
   [*CE1-md-md3-ma-ma3] remote-mep mep-id 4
   ```
   ```
   [*CE1-md-md3-ma-ma3] remote-mep ccm-receive mep-id 4 enable
   ```
   ```
   [*CE1-md-md3-ma-ma3] test-id 1 mep 3 remote-mep 4
   ```
   ```
   [*CE1-md-md3-ma-ma3] commit
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
   [~CE2] vlan 2
   ```
   ```
   [~CE2] interface gigabitethernet0/1/1
   ```
   ```
   [~CE2-GigabitEthernet0/1/1]portswitch
   ```
   ```
   [~CE2-GigabitEthernet0/1/1]port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/1]port trunk allow-pass vlan 2
   ```
   ```
   [*CE2-GigabitEthernet0/1/1]quit
   ```
   ```
   [*CE2] cfm enable
   ```
   ```
   [*CE2] commit
   ```
   ```
   [~CE2] cfm md md3
   ```
   ```
   [*CE2-md-md3] ma ma3
   ```
   ```
   [*CE2-md-md3-ma-ma3] map vlan 2
   ```
   ```
   [*CE2-md-md3-ma-ma3] mep mep-id 4 interface gigabitethernet0/1/1 outward
   ```
   ```
   [*CE2-md-md3-ma-ma3] mep ccm-send mep-id 4 enable
   ```
   ```
   [*CE2-md-md3-ma-ma3] remote-mep mep-id 3
   ```
   ```
   [*CE2-md-md3-ma-ma3] remote-mep ccm-receive mep-id 3 enable
   ```
   ```
   [*CE2-md-md3-ma-ma3] test-id 1 mep 4 remote-mep 3
   ```
   ```
   [*CE2-md-md3-ma-ma3] commit
   ```
2. Enable dual-ended frame loss measurement in a VLAN.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1-md-md3-ma-ma3] loss-measure dual-ended continual test-id 1
   ```
   ```
   [*CE1-md-md3-ma-ma3] quit
   ```
   ```
   [*CE1-md-md3] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2-md-md3-ma-ma3] loss-measure dual-ended continual test-id 1
   ```
   ```
   [*CE2-md-md3-ma-ma3] quit
   ```
   ```
   [*CE2-md-md3] quit
   ```
   ```
   [*CE2] commit
   ```
3. Verify the configuration.
   
   # Run the **display y1731 statistics-type dual-loss** command on CE1 to view dual-ended frame loss statistics.
   ```
   <CE1> display y1731 statistic-type dual-loss
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
   port link-type trunk
   port trunk allow-pass vlan 2
  #
   cfm md md3
    ma ma3
     map vlan 2
     mep mep-id 3 interface GigabitEthernet0/1/1 outward
     mep ccm-send mep-id 3 enable
     remote-mep mep-id 4
     remote-mep ccm-receive mep-id 4 enable
     test-id 1 mep 3 remote-mep 4
     loss-measure dual-ended continual test-id 1
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
   sysname CE2
  #
   vlan 2
  #
   cfm version standard
   cfm enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
  #
   cfm md md3
    ma ma3
     map vlan 2
     mep mep-id 4 interface GigabitEthernet0/1/1 outward
     mep ccm-send mep-id 4 enable
     remote-mep mep-id 3
     remote-mep ccm-receive mep-id 3 enable
     test-id 1 mep 4 remote-mep 3
     loss-measure dual-ended continual test-id 1
  #
  return
  ```