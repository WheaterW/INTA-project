Example for Configuring One-way Frame Delay Measurement in BD EVPN Networking
=============================================================================

This section provides an example for configuring one-way frame delay measurement in BD EVPN networking.

#### Networking Requirements

As networks rapidly develop and applications diversify, various value-added services, such as IPTV, video conferencing, and VoIP, are widely deployed. A link connectivity fault or network performance deterioration directly affects services on a live network. Therefore, performance monitoring is especially important for service transport.

As shown in [Figure 1](#EN-US_TASK_0172362197__fig_dc_vrp_cfg_01153201), PE1 and PE2 are connected through an EVPN, and CE1 and CE2 are connected to the EVPN through a BD. CFM is configured between each PE and its attached CE and between PEs to monitor link connectivity. To provide high-quality video services, a carrier expects to monitor one-way delay on mobile transport links in real time while monitoring link connectivity so that they can promptly respond to video service quality deterioration.

**Figure 1** Configuring one-way frame delay measurement in BD EVPN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_cfg_01151605.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure on-demand one-way frame delay measurement for the service path between PEs' AC interfaces to collect frame delay statistics on demand.
2. Configure proactive one-way frame delay measurement for the service path between PEs' AC interfaces to continuously collect frame delay statistics.


#### Prerequisites

1588 time synchronization has been configured on PE1 and PE2.


#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name **evpna**, RT value, and RD value on each PE
* BD ID
* MD name, MA name, and MEP ID for configuring basic CFM functions
* Interval at which one-way delay measurement (1DM) messages are sent and the number of times that a 1DM message is sent in on-demand one-way frame delay measurement

#### Procedure

1. Configure on-demand one-way frame delay measurement for the service path between PEs' AC interfaces.
   
   
   1. Configure access to an EVPN through a BD.
      
      An EVPN is configured between PE1 and PE2. CE1 and CE2 access the EVPN network through a BD. For details, see the [Configuring EVPN VPLS over MPLS (BD EVPN Instance)](dc_vrp_evpn_cfg_0065.html) or configuration files in this configuration example.
   2. Configure basic Ethernet CFM functions and specify the MEP type as inward.
      
      Configure basic Ethernet CFM functions on each PE. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md1** and an MA named **ma1**, and bind the MA to the BD.
      
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
   3. Configure PE2 to receive 1DM messages.
      
      # Configure PE2.
      
      ```
      [~PE2-md-md1-ma-ma1] delay-measure one-way receive test-id 1
      ```
      ```
      [*PE2-md-md1-ma-ma1] commit
      ```
   4. Enable on-demand one-way frame delay measurement for the service path between PEs' AC interfaces on the EVPN.
      
      # Configure PE1.
      
      ```
      [~PE1-md-md1-ma-ma1] delay-measure one-way send test-id 1 interval 1000 count 20
      ```
      ```
      [*PE1-md-md1-ma-ma1] quit
      ```
      ```
      [*PE1-md-md1] quit
      ```
   5. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE2 to check statistics about one-way frame delay.
      
      ```
      [~PE2] display y1731 statistic-type oneway-delay
      Latest one-way delay statistics of test-id 1:
      --------------------------------------------------------------------------------
      Index    Delay(usec)    Delay variation(usec)
      --------------------------------------------------------------------------------
          1            181                        -
          2            356                      175
          3            166                      190
          4            180                       14
          5            162                       18
          6            160                        2
          7            177                       17
          8            149                       28
          9            190                       41
         10            185                        5
         11            230                       45
         12            221                        9
         13            184                       37
         14            415                      231
         15            187                      228
         16            235                       48
         17            184                       51
         18            184                        0
         19            168                       16
         20            185                       17
      --------------------------------------------------------------------------------
      Average delay(usec) :         204    Average delay variation(usec) :         61
      Maximum delay(usec) :         415    Maximum delay variation(usec) :        231
      Minimum delay(usec) :         149    Minimum delay variation(usec) :          0
      
      
      ```
2. Configure proactive one-way frame delay measurement for the service path between PEs' AC interfaces.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To continuously collect frame delay statistics on the service path between PEs' AC interfaces, configure proactive one-way frame delay measurement.
   
   1. Configure PE1 to receive 1DMMs.
      
      # Configure PE1.
      
      ```
      [~PE1] cfm md md1
      ```
      ```
      [*PE1-md-md1] ma ma1
      ```
      ```
      [*PE1-md-md1-ma-ma1] test-id 3 mep 1
      ```
      ```
      [*PE1-md-md1-ma-ma1] delay-measure one-way continual receive test-id 3
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
   2. Enable proactive one-way frame delay measurement in the BD.
      
      # Configure PE2.
      
      ```
      [~PE2] cfm md md1
      ```
      ```
      [*PE2-md-md1] ma ma1
      ```
      ```
      [*PE2-md-md1-ma-ma1] test-id 3 mep 2 remote-mep 1
      ```
      ```
      [*PE2-md-md1-ma-ma1] delay-measure one-way continual send test-id 3 interval 1000
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
   3. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to check statistics about one-way frame delay.
      
      ```
      [~PE1] display y1731 statistic-type oneway-delay
      Latest one-way delay statistics of test-id 3:
      --------------------------------------------------------------------------------
      Index    Delay(usec)    Delay variation(usec)
      --------------------------------------------------------------------------------
          1            181                        -
          2            356                      175
          3            166                      190
          4            180                       14
          5            162                       18
          6            160                        2
          7            177                       17
          8            149                       28
          9            190                       41
         10            185                        5
         11            230                       45
         12            221                        9
         13            184                       37
         14            415                      231
         15            187                      228
         16            235                       48
         17            184                       51
         18            184                        0
         19            168                       16
         20            185                       17
      --------------------------------------------------------------------------------
      Average delay(usec) :         204    Average delay variation(usec) :         61
      Maximum delay(usec) :         415    Maximum delay variation(usec) :        231
      Minimum delay(usec) :         149    Minimum delay variation(usec) :          0
      
      ```

#### Configuration Files

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
  ```
  ```
  #
  cfm md md1
   ma ma1
    map bridge-domain 10
    mep mep-id 1 interface GigabitEthernet0/1/1.1 vlan 2 inward
    mep ccm-send mep-id 1 enable
    remote-mep mep-id 2
    remote-mep ccm-receive mep-id 2 enable
    test-id 1 mep 1 remote-mep 2
    test-id 3 mep 1
    delay-measure one-way continual receive test-id 3
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
  ```
  ```
  #
  cfm md md1
   ma ma1
    map bridge-domain 10
    mep mep-id 2 interface GigabitEthernet0/1/1.1 vlan 2 inward
    mep ccm-send mep-id 2 enable
    remote-mep mep-id 1
    remote-mep ccm-receive mep-id 1 enable
    test-id 1 mep 2 remote-mep 1
    delay-measure one-way receive test-id 1
    test-id 3 mep 2 remote-mep 1
    delay-measure one-way continual send test-id 3 interval 1000
  #
  return
  ```