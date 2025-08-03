Example for Configuring One-way Frame Delay Measurement in VLL Networking
=========================================================================

This section provides an example showing how to configure one-way frame delay measurement in virtual leased line (VLL) networking.

#### Networking Requirements

As networks rapidly develop and applications diversify, various value-added services, such as IPTV, video conferencing, and VoIP, are widely deployed. A link connectivity fault or network performance deterioration directly affects services on a live network. Therefore, performance monitoring is especially important for service transmission channels.

As shown in [Figure 1](#EN-US_TASK_0172362156__fig_dc_vrp_cfg_01153401), connectivity fault management (CFM) is configured between each customer edge (CE) and provider edge (PE) and between PEs. To provide high-quality video services, providers hope to monitor the unidirectional delay over mobile bearer links in real time, while monitoring link connectivity. Monitoring the unidirectional delay over mobile bearer links allows the providers to respond quickly to video service quality deterioration.

**Figure 1** Configuring Y.1731 functions in VLL networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_cfg_01153201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure on-demand one-way frame delay measurement for the pseudo wire (PW) between the PEs to periodically collect statistics about the delay in frame transmission.
2. Configure proactive one-way frame delay measurement for the PW between the PEs to continuously collect statistics about the delay in frame transmission.


#### Prerequisites

1588 time synchronization has been configured on PE1 and PE2.


#### Data Preparation

To complete the configuration, you need the following data:

* ID of an L2VC of a VLL between PE1 and PE2.
* Names of the maintenance domain (MD) and maintenance association (MA) between PE1 and PE2 and between CE1 and PE1.
* Interval at which one-way delay measurement (1DM) messages are sent and the number of times when on-demand 1DM messages are sent.

#### Procedure

1. Configure on-demand one-way frame delay measurement for a PW based on ACs on PEs. 
   
   
   1. Configure a VLL connection.
      
      Configure a VLL connection between PE1 and PE2. For detailed configurations, see the chapter "VLL Configuration" in the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - VPN* or configuration files in this configuration example.
      
      After the configuration is complete, run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) command on each PE to view VC and AC information.
      
      ```
      [~PE1] display mpls l2vc                                           
       total LDP VC : 1     1 up       0 down
      
       *client interface       : Gigabitethernet0/1/1.1
        Administrator PW       : no
        session state          : up
        AC status              : up
        VC state               : up
        Label state            : 0
        Token state            : 0
        VC ID                  : 1001
        VC type                : GigabitEthernet
        destination            : 2.2.2.2
        local VC label         : 16             remote VC label      : 16
        control word           : disable
        remote control word    : disable
        forwarding entry       : exist
        local group ID         : 0
        remote group ID        : 0
        local AC OAM State     : up
        local PSN OAM State    : up
        local forwarding state : forwarding
        local status code      : 0x0
        remote AC OAM state    : up
        remote PSN OAM state   : up
        remote forwarding state: forwarding
        remote status code     : 0x0
        ignore standby state   : no
        BFD for PW             : unavailable
        VCCV State             : up
        manual fault           : not set
        active state           : active
        OAM Protocol           : --
        OAM Status             : --
        OAM Fault Type         : --
        PW APS ID              : --
        PW APS Status          : --
        TTL Value              : 1
        link state             : up
        local VC MTU           : 1500           remote VC MTU        : 1500
        local VCCV             : alert ttl lsp-ping bfd
        remote VCCV            : alert ttl lsp-ping bfd
        tunnel policy name     : --
        traffic behavior name  : --
        PW template name       : --
        primary or secondary   : primary
        load balance type      : flow
        Access-port            : false
        Switchover Flag        : false
        VC tunnel info         : 1 tunnels
          NO.0  TNL type       : ldp   , TNL ID : 0x0000000001004c4e42
        create time            : 4 days, 15 hours, 59 minutes, 12 seconds
        up time                : 0 days, 15 hours, 23 minutes, 17 seconds
        last change time       : 0 days, 15 hours, 23 minutes, 17 seconds
        VC last up time        : 2012/07/24 09:37:33
        VC total up time       : 4 days, 15 hours, 57 minutes, 50 seconds
        CKey                   : 1
        NKey                   : 436207716
        PW redundancy mode     : frr
        AdminPw interface      : --
        AdminPw link state     : --
        Forward state          : send inactive, receive inactive 
        Diffserv Mode          : uniform
        Service Class          : --
        Color                  : --
        DomainId               : --
        Domain Name            : --                                      
      ```
   2. Configure basic Ethernet CFM functions and specify the MEP type as inward.
      
      Configure basic Ethernet CFM functions on each PE. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md1** and an MA named **ma1**, and bind the MA to the VLL.
      
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
      [*PE1-md-md1-ma-ma1] map mpls l2vc 1001 tagged
      ```
      ```
      [*PE1-md-md1-ma-ma1] mep mep-id 1 interface gigabitethernet0/1/1.1 inward
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
      [*PE2-md-md1-ma-ma1] map mpls l2vc 1001 tagged
      ```
      ```
      [*PE2-md-md1-ma-ma1] mep mep-id 2 interface gigabitethernet0/1/1.1 inward
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
      [*PE2-md-md1-ma-ma1] test-id 1 mep 2
      ```
      ```
      [*PE2-md-md1-ma-ma1] commit
      ```
   3. Configure the 1DM reception function on PE2.
      
      # Configure PE2.
      
      ```
      [~PE2-md-md1-ma-ma1] delay-measure one-way receive test-id 1
      ```
      ```
      [*PE2-md-md1-ma-ma1] commit
      ```
   4. Enable on-demand one-way frame delay measurement on the PW on a VLL network. 
      
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
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE2 to view the statistics about the delay in unidirectional packet transmission.
      
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
2. Configure proactive one-way frame delay measurement for a PW based on ACs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Proactive one-way frame delay measurement can be configured to continuously monitor the performance of a PW.
   
   1. Configure the 1DM reception function on PE2.
      
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
   2. Enable proactive one-way frame delay measurement.
      
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
   3. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to view the statistics about the delay in unidirectional packet transmission.
      
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
   mpls lsr-id 1.1.1.1
   mpls
  #
   mpls l2vpn
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 1
   mpls l2vc 2.2.2.2 1001
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls ldp 
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
   cfm md md1
   ma ma1
    map mpls l2vc 1001 tagged
    mep mep-id 1 interface GigabitEthernet0/1/1.1 inward
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
   mpls lsr-id 2.2.2.2
   mpls
  #
   mpls l2vpn
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 1
   mpls l2vc 1.1.1.1 1001
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.1.0 0.0.0.255 
  #
   cfm md md1
   ma ma1
    map mpls l2vc 1001 raw
    mep mep-id 2 interface GigabitEthernet0/1/1.1 inward
    mep ccm-send mep-id 2 enable
    remote-mep mep-id 1
    remote-mep ccm-receive mep-id 1 enable
    test-id 1 mep 2
    delay-measure one-way receive test-id 1
    test-id 3 mep 2 remote-mep 1
    delay-measure one-way continual send test-id 3 interval 1000
  #
  return
  ```