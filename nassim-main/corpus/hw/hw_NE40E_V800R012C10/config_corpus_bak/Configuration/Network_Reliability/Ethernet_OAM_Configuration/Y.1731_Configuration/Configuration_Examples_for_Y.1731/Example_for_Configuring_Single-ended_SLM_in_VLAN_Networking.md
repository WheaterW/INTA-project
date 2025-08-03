Example for Configuring Single-ended SLM in VLAN Networking
===========================================================

This section provides an example for configuring single-ended synthetic loss measurement (SLM) in virtual local area network (VLAN) networking.

#### Networking Requirements

As networks rapidly develop and applications diversify, various value-added services, such as Internet Protocol television (IPTV), video conferencing, and Voice over Internet Protocol (VoIP), are more widely used than ever before. Any link connectivity fault or network performance deterioration directly affects service quality on a live network, making performance monitoring on the pipes that transmit these services absolutely essential.

On the point-to-multipoint network shown in [Figure 1](#EN-US_TASK_0172362176__fig_dc_vrp_y1731_cfg_007501), PE1 and PE2 are connected through a VLAN. A carrier wants to collect accurate performance statistics about LM on the link between CE1 and CE2. To monitor network performance in real time, the carrier can configure single-ended SLM on the VLAN. This configuration allows the carrier to immediately adjust the network in case of voice quality deterioration.

**Figure 1** Single-ended SLM in VLAN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example is GE 0/1/1.


  
![](images/fig_dc_vrp_y1731_cfg_007501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure single-ended on-demand SLM on a link between customer edges (CEs).
2. Configure single-ended proactive SLM on a link between CEs.


#### Data Preparation

To complete the configuration, you need the following data:

* ID of the VLAN to which the CEs belong
* Names of the maintenance domain (MD) and maintenance association (MA) in which CE1 and CE2 reside

#### Procedure

1. Configure single-ended on-demand SLM.
   
   
   1. Configure basic Ethernet connectivity fault management (CFM) functions and set the maintenance association end point (MEP) type to outward.
      
      Configure basic Ethernet CFM functions on each CE. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md3** and an MA named **ma3**, and bind the MA to the VLAN.
      
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
      [*CE2-md-md3-ma-ma3] test-id 1 mep 3 remote-mep 4
      ```
      ```
      [*CE2-md-md3-ma-ma3] commit
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
      [*CE2] cfm version standard
      ```
      ```
      [*CE2] cfm md md3
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
   2. Enable CE to send or receive SLM frames.
      
      # Configure CE2.
      
      ```
      [*CE2-md-md3-ma-ma3] loss-measure single-ended-synthetic receive test-id 1 time-out 300
      ```
      ```
      [*CE2-md-md3-ma-ma3] commit
      ```
      ```
      [~CE2-md-md3-ma-ma3] quit
      ```
      ```
      [~CE2-md-md3] quit
      ```
      
      # Configure CE1
      
      ```
      [~CE1-md-md3-ma-ma3] loss-measure single-ended-synthetic send test-id 1 interval 1000 sending-count 10 time-out 2
      ```
      ```
      [*CE1-md-md3-ma-ma3] commit
      ```
      ```
      [~CE1-md-md3-ma-ma3] quit
      ```
      ```
      [~CE1-md-md3] quit
      ```
   3. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on CE1 to view statistics about single-ended on-demand SLM.
      
      ```
      <CE1>display  y1731  statistic-type single-synthetic-loss test-id 1
      --------------------------------------------------------------------------------
      Index       L-send R-send L-recv Unack  L-loss R-loss L-loss-ratio R-loss-ratio 
      --------------------------------------------------------------------------------
      1016        10     10     10     0           0      0      0.0000%      0.0000% 
      --------------------------------------------------------------------------------
      Average Local-loss  :          0    Average Local-loss Ratio  :         0.0000% 
      Maximum Local-loss  :          0    Maximum Local-loss Ratio  :         0.0000% 
      Minimum Local-loss  :          0    Minimum Local-loss Ratio  :         0.0000% 
      Average Remote-loss :          0    Average Remote-loss Ratio :         0.0000% 
      Maximum Remote-loss :          0    Maximum Remote-loss Ratio :         0.0000% 
      Minimum Remote-loss :          0    Minimum Remote-loss Ratio :         0.0000% 
      
      ```
2. Configure single-ended proactive SLM.
   
   
   1. Enable single-ended proactive SLM.
      
      # Configure CE2.
      
      ```
      [*CE2-md-md3-ma-ma3] loss-measure single-ended-synthetic receive test-id 1 time-out 300
      ```
      ```
      [*CE1-md-md1-ma-ma1] commit
      ```
      ```
      [~CE2-md-md3-ma-ma3] quit
      ```
      ```
      [~CE2-md-md3] quit
      ```
      
      # Configure CE1.
      
      ```
      [*CE1-md-md1-ma-ma1] loss-measure single-ended-synthetic continual send test-id 1 interval 1000
      ```
      ```
      [*CE1-md-md1-ma-ma1] commit
      ```
      ```
      [~CE1-md-md1-ma-ma1] quit
      ```
      ```
      [~CE1-md-md1] quit
      ```
   2. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on CE1 to view statistics about single-ended proactive SLM.
      
      ```
      <CE1> display  y1731  statistic-type single-synthetic-loss test-id 1
      ```
      ```
      --------------------------------------------------------------------------------
      Index       L-send R-send L-recv Unack  L-loss R-loss L-loss-ratio R-loss-ratio 
      --------------------------------------------------------------------------------
      1016        10     10     10     0           0      0      0.0000%      0.0000% 
      1017        10     10     10     0           0      0      0.0000%      0.0000% 
      1018        10     10     10     0           0      0      0.0000%      0.0000% 
      1019        10     10     10     0           0      0      0.0000%      0.0000% 
      1020        10     10     10     0           0      0      0.0000%      0.0000% 
      1021        10     10     10     0           0      0      0.0000%      0.0000% 
      --------------------------------------------------------------------------------
      Average Local-loss  :          0    Average Local-loss Ratio  :         0.0000% 
      Maximum Local-loss  :          0    Maximum Local-loss Ratio  :         0.0000% 
      Minimum Local-loss  :          0    Minimum Local-loss Ratio  :         0.0000% 
      Average Remote-loss :          0    Average Remote-loss Ratio :         0.0000% 
      Maximum Remote-loss :          0    Maximum Remote-loss Ratio :         0.0000% 
      Minimum Remote-loss :          0    Minimum Remote-loss Ratio :         0.0000% 
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
    loss-measure single-ended-synthetic continual send test-id 1 interval 1000 
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
     loss-measure single-ended-synthetic receive test-id 1 time-out 300
  #
  return
  ```