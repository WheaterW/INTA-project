Example for Configuring Single-ended SLM in EVPN Networking
===========================================================

This section provides an example for configuring single-ended synthetic packet loss measurement (SLM) in EVPN networking.

#### Networking Requirements

As networks rapidly develop and applications diversify, various value-added services, such as Internet Protocol television (IPTV), video conferencing, and Voice over Internet Protocol (VoIP), are more widely used than ever before. Any link connectivity fault or network performance deterioration directly affects service quality on a live network. Therefore, performance monitoring is especially important for service transmission channels.

On the point-to-point network shown in [Figure 1](#EN-US_TASK_0172362196__fig_dc_vrp_cfg_01153201), a carrier wants to collect accurate performance statistics about LM on the link between PE1 and PE2. To monitor network performance in real time, the carrier can configure single-ended SLM on the EVPN network. This configuration allows the carrier to immediately adjust the network in case of voice quality deterioration.

**Figure 1** Configuring Y.1731 functions in EVPN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_cfg_01151605.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure single-ended on-demand SLM.
2. Configure single-ended proactive SLM.


#### Data Preparation

To complete the configuration, you need the following data:

* Layer 2 virtual circuit (L2VC) ID for configuring basic EVPN functions
* Names of the MD and MA between PE1 and PE2 and between CE1 and PE1

#### Procedure

1. Configure single-ended on-demand SLM for AC-side links.
   
   
   1. Configure an EVPN connection.
      
      Configure an EVPN connection between PE1 and PE2. The configuration details are not provided here. For details, see the [EVPN Configuration](dc_vrp_evpn_cfg_0000.html) or configuration files in this configuration example.
   2. Configure basic Ethernet connectivity fault management (CFM) functions and set the maintenance association end point (MEP) type to inward.
      
      Configure basic Ethernet CFM functions on each PE. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md1** and an MA named **ma1**, and bind the MA to the EVPN instance.
      
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
      [*PE1-md-md1-ma-ma1] map evpn vpn-instance evpna
      ```
      ```
      [*PE1-md-md1-ma-ma1] mep mep-id 1 interface gigabitethernet0/1/1 inward
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
      [*PE2-md-md1-ma-ma1] map evpn vpn-instance evpna
      ```
      ```
      [*PE2-md-md1-ma-ma1] mep mep-id 2 interface gigabitethernet0/1/1 inward
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
   4. Enable single-ended on-demand SLM on the AC side in EVPN networking.
      
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
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to view statistics about single-ended on-demand SLM.
      
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
2. Configure single-ended proactive SLM on a PW between PEs. 
   
   
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
   2. Enable proactive single-ended SLM on an EVPN.
      
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
      [*PE2-md-md-ma-ma1] commit
      ```
      ```
      [~PE1-md-md1-ma-ma1] quit
      ```
      ```
      [~PE1-md-md1] quit
      ```
   3. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to view statistics about single-ended proactive SLM.
      
      ```
      [~PE1] display  y1731  statistic-type single-synthetic-loss test-id 1
      Latest single-synthetic-loss statistics of test-id 1:
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
  evpn vpn-instance evpna
    route-distinguisher 100:1
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
   ipv4-family
  #
  interface GigabitEthernet0/1/1
    undo shutdown
    evpn binding vpn-instance evpna
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
    map evpn vpn-instance evpna                                                    
    mep mep-id 1 interface GigabitEthernet0/1/1 inward                                    
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
  mpls ldp
  #
  ipv4-family
  #
  interface GigabitEthernet0/1/1
   evpn binding vpn-instance evpna
  #
  interface GigabitEthernet0/1/2
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
    map evpn vpn-instance evpna                                                    
    mep mep-id 2 interface GigabitEthernet0/1/1 inward                                 
    mep ccm-send mep-id 2 enable                                               
    remote-mep mep-id 1                                                          
    remote-mep ccm-receive mep-id 1 enable                                        
    test-id 1 mep 2 remote-mep 1                                               
    loss-measure single-ended-synthetic receive test-id 1 time-out 300 
  #                                                                               
  return 
  ```