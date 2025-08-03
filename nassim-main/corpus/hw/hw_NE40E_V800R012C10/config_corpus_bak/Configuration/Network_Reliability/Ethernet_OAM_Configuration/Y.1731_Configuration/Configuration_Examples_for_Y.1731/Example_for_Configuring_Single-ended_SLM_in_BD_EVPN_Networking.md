Example for Configuring Single-ended SLM in BD EVPN Networking
==============================================================

This section provides an example for configuring single-ended SLM in BD EVPN networking.

#### Networking Requirements

As networks rapidly develop and applications diversify, various value-added services, such as IPTV, video conferencing, and VoIP, are widely deployed. A link connectivity fault or network performance deterioration directly affects services on a live network. Therefore, performance monitoring is especially important for service transport.

As shown in [Figure 1](#EN-US_TASK_0172362199__fig_dc_vrp_cfg_01153201), PE1 and PE2 are connected through an EVPN, and CE1 and CE2 are connected to the EVPN through a BD. To monitor network performance in real time, a carrier expects to collect accurate performance statistics about LM on the link between PE1 and PE2. The carrier can configure single-ended SLM to promptly respond to calling service quality deterioration.

**Figure 1** Configuring single-ended SLM in BD EVPN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_cfg_01151605.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure on-demand single-ended SLM for the service path between PEs' AC interfaces.
2. Configure proactive single-ended SLM for the service path between PEs' AC interfaces.


#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name (**evpna**), RD value, and RT value
* BD ID
* MD name, MA name, and MEP ID for configuring basic CFM functions on each PE

#### Procedure

1. Configure on-demand single-ended SLM for the service path between PEs' AC interfaces.
   
   
   1. Configure access to an EVPN through a BD.
      
      An EVPN is configured between PE1 and PE2. CE1 and CE2 access the EVPN network through a BD. For details, see the [Configuring EVPN VPLS over MPLS (BD EVPN Instance)](dc_vrp_evpn_cfg_0065.html) or configuration files in this configuration example.
   2. Configure basic Ethernet CFM functions and specify the MEP type as inward.
      
      Configure basic Ethernet CFM functions on each PE. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md1** and an MA named **ma1**, and bind the MA to the BD.
      
      # Configure PE1.
      
      ```
      [~PE1] cfm enable
      ```
      ```
      [*PE1] cfm version standard
      ```
      ```
      [*PE1] cfm md md1
      ```
      ```
      [*PE1-md-md1] ma ma1
      ```
      ```
      [*PE1-md-md1-ma-ma1] map bridge-domain 10
      ```
      ```
      [*PE1-md-md1-ma-ma1] mep mep-id 1 interface gigabitethernet0/1/1.1 vlan 2 inward
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
      
      # Configure PE2.
      
      ```
      [~PE2] cfm enable
      ```
      ```
      [*PE2] cfm version standard
      ```
      ```
      [*PE2] cfm md md1
      ```
      ```
      [*PE2-md-md1] ma ma1
      ```
      ```
      [*PE2-md-md1-ma-ma1] map bridge-domain 10
      ```
      ```
      [*PE2-md-md1-ma-ma1] mep mep-id 2 interface gigabitethernet0/1/1.1 vlan 2 inward
      ```
      ```
      [*PE2-md-md1-ma-ma1] mep ccm-send mep-id 2 enable
      ```
      ```
      [*PE2-md-md1-ma-ma1] remote-mep mep-id 1
      ```
      ```
      [*PE2-md-md1-ma-ma1] remote-mep ccm-receive mep-id 1 enable
      ```
      ```
      [*PE2-md-md1-ma-ma1] test-id 1 mep 2 remote-mep 1
      ```
      ```
      [*PE2-md-md1-ma-ma1] commit
      ```
   3. Enable PE2 to receive SLM frames.
      
      # Configure PE2.
      
      ```
      [~PE2-md-md1-ma-ma1] loss-measure single-ended-synthetic receive test-id 1 time-out 300
      ```
      ```
      [*PE2-md-md1-ma-ma1] commit
      ```
      ```
      [~PE2-md-md1-ma-ma1] quit
      ```
      ```
      [~PE2-md-md1] quit
      ```
   4. Configure on-demand single-ended SLM for the service path between PEs' AC interfaces.
      
      # Configure PE1.
      
      ```
      [~PE1-md-md1-ma-ma1] loss-measure single-ended-synthetic send test-id 1 interval 1000 sending-count 10 time-out 2
      ```
      ```
      [*PE1-md-md1-ma-ma1] commit
      ```
      ```
      [~PE1-md-md1-ma-ma1] quit
      ```
      ```
      [~PE1-md-md1] quit
      ```
   5. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to check statistics about single-ended SLM.
      
      ```
      [~PE1]display  y1731  statistic-type single-synthetic-loss test-id 1
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
2. Configure proactive single-ended SLM for the service path between PEs' AC interfaces.
   
   
   1. Enable PE2 to receive SLM frames.
      
      # Configure PE2.
      
      ```
      [~PE2] cfm md md1
      ```
      ```
      [~PE2-md-md1] ma ma1
      ```
      ```
      [~PE2-md-md-ma-ma1] loss-measure single-ended-synthetic receive test-id 1 time-out 300
      ```
      ```
      [*PE2-md-md-ma-ma1] commit
      ```
      ```
      [~PE2-md-md1-ma-ma1] quit
      ```
      ```
      [~PE2-md-md1] quit
      ```
   2. Configure proactive single-ended SLM for the service path between PEs' AC interfaces.
      
      # Configure PE1.
      
      ```
      [~PE1] cfm md md1
      ```
      ```
      [~PE1-md-md1] ma ma1
      ```
      ```
      [~PE1-md-md1-ma-ma1] loss-measure single-ended-synthetic continual send test-id 1 interval 1000
      ```
      ```
      [*PE1-md-md-ma-ma1] commit
      ```
      ```
      [~PE1-md-md1-ma-ma1] quit
      ```
      ```
      [~PE1-md-md1] quit
      ```
   3. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to check statistics about single-ended SLM.
      
      ```
      [~PE1] display  y1731  statistic-type single-synthetic-loss test-id 1
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

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  cfm version standard
  cfm enable
  #
  evpn vpn-instance evpna bd-mode
    route-distinguisher 100:1
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  bridge-domain 10 
    evpn binding vpn-instance evpna
  #
  mpls ldp
  #
  ipv4-family
  #
  interface GigabitEthernet0/1/1
    undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
    encapsulation dot1q vid 2
    rewrite pop single
    bridge-domain 10
  #
  interface GigabitEthernet0/1/2
    ip address 10.1.1.1 255.255.255.0
    mpls
    mpls ldp
  #
  interface LoopBack0
    ip address 1.1.1.1 255.255.255.255
  #
   bgp 100
    peer 2.2.2.2 as-number 100
    peer 2.2.2.2 connect-interface LoopBack0
  #
  ipv4-family unicast
   undo synchronization
   peer 2.2.2.2 enable
  #
  l2vpn-family evpn
    peer 2.2.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  evpn source-address 1.1.1.1 
  #
   cfm md md1                      
   ma ma1
    map bridge-domain 10
    mep mep-id 1 interface GigabitEthernet0/1/1.1 vlan 2 inward                                    
    mep ccm-send mep-id 1 enable                                                  
    remote-mep mep-id 2
    remote-mep ccm-receive mep-id 2 enable                                     
    test-id 1 mep 1 remote-mep 2
    loss-measure single-ended-synthetic continual send test-id 1 interval 1000    
  #                                                                               
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  cfm version standard
  cfm enable
  #
  evpn vpn-instance evpna
    route-distinguisher 200:1
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  bridge-domain 10 
   evpn binding vpn-instance evpna
  #
  mpls ldp
  #
  ipv4-family
  #
  interface GigabitEthernet0/1/1
    undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
    encapsulation dot1q vid 2
    rewrite pop single
    bridge-domain 10
  #
  interface GigabitEthernet0/1/2
    undo shutdown
    ip address 10.2.1.1 255.255.255.0
    mpls
    mpls ldp
  #
  interface LoopBack0
    ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
    peer 1.1.1.1 as-number 100
    peer 1.1.1.1 connect-interface LoopBack0
  #
  ipv4-family unicast
     undo synchronization
     peer 1.1.1.1 enable
  #
  l2vpn-family evpn
     peer 1.1.1.1 enable
  #
  ospf 1
    area 0.0.0.0
     network 2.2.2.2 0.0.0.0
     network 10.2.1.0 0.0.0.255
  #
  evpn source-address 2.2.2.2
  #
   cfm md md1   
   ma ma1
    map bridge-domain 10
    mep mep-id 2 interface GigabitEthernet0/1/1.1 vlan 2 inward                                 
    mep ccm-send mep-id 2 enable                                               
    remote-mep mep-id 1                                                          
    remote-mep ccm-receive mep-id 1 enable                                        
    test-id 1 mep 2 remote-mep 1                                               
    loss-measure single-ended-synthetic receive test-id 1 time-out 300 
  #                                                                               
  return
  ```