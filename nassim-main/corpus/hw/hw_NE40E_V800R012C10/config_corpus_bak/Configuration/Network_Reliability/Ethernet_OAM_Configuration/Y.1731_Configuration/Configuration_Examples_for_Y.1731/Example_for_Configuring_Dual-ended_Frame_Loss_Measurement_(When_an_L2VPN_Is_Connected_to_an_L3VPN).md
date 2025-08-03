Example for Configuring Dual-ended Frame Loss Measurement (When an L2VPN Is Connected to an L3VPN)
==================================================================================================

This section provides an example for configuring dual-ended frame loss measurement when an L2VPN is connected to an L3VPN.

#### Networking Requirements

As networks continue to develop and diversify, various value-added services such as IPTV, video conferencing, and VoIP are becoming increasingly popular. The performance monitoring function can be used to check the performance of links that transmit services.

In [Figure 1](#EN-US_TASK_0172362182__fig_dc_vrp_y1731_cfg_005801), CFM is configured to monitor the link between CE1 and PE3. CCMs are not expected to monitor link connectivity because the CCMs consume a lot of bandwidth resources. To meet higher requirements for voice services, a carrier needs a function to monitor frame loss performance on mobile links in real time and make prompt responses to calling performance deterioration.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

A VLAN dot1q sub-interface, dot1q termination sub-interface, QinQ termination sub-interface, or L3VE interface on an L2VPN can be connected to an L3VPN. In this example, a VLAN dot1q sub-interface is used. An L2VPN is configured to access a public network, or L3VPN services are configured.


**Figure 1** L2VPN connected to an L3VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Sub-interfaces3.1 in this example is GE0/3/1.1.


  
![](images/fig_dc_vrp_y1731_cfg_005801.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure on-demand dual-ended frame loss measurement.


#### Data Preparation

To complete the configuration, you need the following data:

* MD name and MA name on CE1 and PE3
* Interval at which LMMs are sent and number of intervals

#### Procedure

1. Configure basic Ethernet CFM functions, including outward-facing MEPs.
   
   
   
   Configure basic Ethernet CFM functions on CE1 and PE3. Configure Ethernet CFM in compliance with IEEE Std 802.1ag-2007 and create an MD named **md3** and an MA named **ma3**.
   
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
   [~CE1] interface gigabitethernet0/3/1.1
   ```
   ```
   [*CE1-GigabitEthernet0/3/1.1] vlan-type dot1q 200
   ```
   ```
   [*CE1-GigabitEthernet0/3/1.1] commit
   ```
   ```
   [*CE1-GigabitEthernet0/3/1.1] quit
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
   [*CE1-md-md3-ma-ma3] mep mep-id 3 interface gigabitethernet0/3/1.1 vlan 200 outward 
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
   
   # Configure PE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE3
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [*PE3-GigabitEthernet0/3/1.1] vlan-type dot1q 200
   ```
   ```
   [*PE3-GigabitEthernet0/3/1.1] commit
   ```
   ```
   [*PE3-GigabitEthernet0/3/1.1] quit
   ```
   ```
   [*PE3] commit
   ```
   ```
   [*PE3] cfm enable
   ```
   ```
   [*PE3] cfm commit
   ```
   ```
   [*PE3] cfm md md3
   ```
   ```
   [*PE3-md-md3] ma ma3
   ```
   ```
   [*PE3-md-md3-ma-ma3] mep mep-id 4 interface gigabitethernet0/3/1.1 vlan 200 outward 
   ```
   ```
   [*PE3-md-md3-ma-ma3] mep ccm-send mep-id 4 enable
   ```
   ```
   [*PE3-md-md3-ma-ma3] remote-mep mep-id 3
   ```
   ```
   [*PE3-md-md3-ma-ma3] remote-mep ccm-receive mep-id 3 enable
   ```
   ```
   [*PE3-md-md3-ma-ma3] test-id 1 mep 4
   ```
   ```
   [*PE3-md-md3-ma-ma3] commit
   ```
2. Configure dual-ended frame loss measurement.
   
   
   
   # Configure PE3.
   
   ```
   [~PE3-md-md3-ma-ma3] loss-measure dual-ended continual test-id 1
   ```
   ```
   [*PE3-md-md3-ma-ma3] quit
   ```
   ```
   [*PE3-md-md3] quit
   ```
   ```
   [*PE3] commit
   ```
   
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
3. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command to dual-ended frame loss statistics on CE1.
   
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
   interface GigabitEthernet0/3/1.1
   vlan-type dot1q 200
  #
   cfm version standard
   cfm enable
  #
   cfm md md3
    ma ma3
     mep mep-id 3 interface GigabitEthernet0/3/1.1 vlan 200 outward
     mep ccm-send mep-id 3 enable
     remote-mep mep-id 4
     remote-mep ccm-receive mep-id 4 enable
     test-id 1 mep 3 remote-mep 4
     loss-measure dual-ended continual test-id 1
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  
   sysname PE3
  #
   interface GigabitEthernet0/3/1.1
   vlan-type dot1q 200
  #
   cfm version standard
   cfm enable
  #
   cfm md md3
    ma ma3
     mep mep-id 4 interface GigabitEthernet0/3/1.1 vlan 200 outward
     mep ccm-send mep-id 4 enable
     remote-mep mep-id 3
     remote-mep ccm-receive mep-id 3 enable
     test-id 1 mep 4
     loss-measure dual-ended continual test-id 1
  #
  return
  ```