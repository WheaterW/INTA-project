Example for Configuring Single-ended Packet Loss Measurement in VPLS Networking
===============================================================================

This section provides an example showing how to configure single-ended packet loss measurement in VPLS networking.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172362161__fig_dc_vrp_cfg_01153601), CFM is configured between each CE and PE and between PEs. CCMs are not used to monitor link connectivity, preventing them from using a lot of network bandwidth resources. To provide higher-quality voice services, carriers hope to monitor packet loss performance on mobile bearer links in real time so that they can promptly respond to video service quality deterioration.

**Figure 1** Configuring Y.1731 functions in VPLS networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_cfg_01153601.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure single-ended packet loss measurement for the PW between the PEs to collect packet loss statistics.
2. Configure single-ended packet loss measurement for the AC between each PE and its attached CE to collect packet loss statistics.


#### Data Preparation

To complete the configuration, you need the following data:

* Configure the name of a VSI and the IP address of the interface of a VPLS.
* Configure the names of the MD and MA between PE1 and PE2 and between CE1 and PE1.
* Configure a VLAN ID on CE interfaces for collecting AC-side packet statistics.
* Configure the interval at which LM messages are sent and the number of times when LM messages are sent.

#### Procedure

1. Configure on-demand single-ended packet loss measurement for a PW between the PEs.
   
   
   1. Configure a VPLS connection.
      
      Configure a VPLS connection between PE1 and PE2. For detailed configurations, see the chapter "VPLS Configuration" in the *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - VPN* or configuration files in this example.
      
      After the configuration is complete, run the [**display vsi name**](cmdqueryname=display+vsi++name) *vsi-name* **verbose** command on each PE to view information about the related VSI and PW.
      
      ```
      <PE1> display vsi  name ldp1 verbose                                          
       ***VSI Name               : ldp1
          Administrator VSI      : no
          Isolate Spoken         : disable
          VSI Index              : 1
          PW Signaling           : ldp
          Member Discovery Style : static
          Bridge-domain Mode     : disable
          PW MAC Learn Style     : unqualify
          Encapsulation Type     : vlan
          MTU                    : 1500
          Diffserv Mode          : uniform
          Service Class          : --
          Color                  : --
          DomainId               : 255
          Domain Name            :
          Ignore AcState         : disable
          P2P VSI                : disable
          Create Time            : 0 days, 0 hours, 10 minutes, 10 seconds
          VSI State              : up
      
          VSI ID                 : 1
         *Peer Router ID         : 1.1.1.1
          primary or secondary   : primary
          ignore-standby-state   : no
          VC Label               : 4187
          Peer Type              : dynamic
          Session                : up
          Tunnel ID              : 0x0000000001004c4b42 
          Broadcast Tunnel ID    : --
          Broad BackupTunnel ID  : -- 
          CKey                   : 1
          NKey                   : 2281701546
          Stp Enable             : 0
          PwIndex                : 1
          Control Word           : enable
       
          Interface Name         : GigabitEthernet0/1/1.1
          State                  : up
          Access Port            : false
          Last Up Time           : 2013/02/21 08:44:46
          Total Up Time          : 0 days, 0 hours, 0 minutes, 14 seconds
      
        **PW Information:
      
         *Peer Ip Address        : 1.1.1.1
          PW State               : up
          Local VC Label         : 4187
          Remote VC Label        : 4187
          Remote Control Word    : enable
          PW Type                : label
          Tunnel ID              : 0x0000000001004c4b42 
          Broadcast Tunnel ID    : --
          Broad BackupTunnel ID  : --
          Ckey                   : 1
          Nkey                   : 2281701546
          Main PW Token          : 0x0
          Slave PW Token         : 0x0
          Tnl Type               : ldp
          OutInterface           : LDP LSP
          Backup OutInterface    : --
          Stp Enable             : 0
          PW Last Up Time        : 2013/02/21 08:44:46
          PW Total Up Time       : 0 days, 0 hours, 0 minutes, 14 seconds
      ```
   2. Configure basic Ethernet CFM functions and specify the MEP type as inward.
      
      Configure basic Ethernet CFM functions on each PE. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md1** and an MA named **ma1**, and bind the MA to the VSI.
      
      # Configure PE1.
      
      ```
      [~PE1] cfm enable
      ```
      ```
      [*PE1] cfm md md1
      ```
      ```
      [*PE1-md-md1] ma ma1
      ```
      ```
      [*PE1-md-md1-ma-ma1] map vsi ldp1
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
      [*PE1-md-md1-ma-ma1]  test-id 1 mep 1 remote-mep 2 peer-ip 1.1.1.1
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
      
      # Configure PE2.
      
      ```
      [~PE2] cfm enable
      ```
      ```
      [*PE2] cfm md md1
      ```
      ```
      [*PE2-md-md1] ma ma1
      ```
      ```
      [*PE2-md-md1-ma-ma1] map vsi ldp1
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
      [*PE2-md-md1-ma-ma1] test-id 1 mep 2 peer-ip 2.2.2.2
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
   3. Configure the LMM reception function on PE2.
      
      # Configure PE2.
      
      ```
      [~PE2-md-md1-ma-ma1] loss-measure single-ended receive test-id 1
      ```
   4. Enable on-demand single-ended packet loss measurement on the VPLS network.
      
      # Configure PE1.
      
      ```
      [~PE1-md-md1-ma-ma1] loss-measure single-ended send test-id 1 interval 1000 count 20
      ```
      ```
      [*PE1-md-md1-ma-ma1] quit
      ```
      ```
      [*PE1-md-md1] quit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      When single-ended packet loss measurement is enabled on PE1, related configuration commands are not displayed in the configuration file.
   5. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to view single-ended packet loss statistics.
      
      ```
      [PE1] display y1731 statistic-type single-loss
      Latest single-ended loss statistics of test-id 1:
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
         11             0             0.0000%              0              0.0000%
      --------------------------------------------------------------------------------
      Average Local-loss  :          0    Average Local-loss Ratio  :   0.0000%
      Maximum Local-loss  :          0    Maximum Local-loss Ratio  :   0.0000%
      Minimum Local-loss  :          0    Minimum Local-loss Ratio  :   0.0000%
      Average Remote-loss :          0    Average Remote-loss Ratio :   0.0000%
      Maximum Remote-loss :          0    Maximum Remote-loss Ratio :   0.0000%
      Minimum Remote-loss :          0    Minimum Remote-loss Ratio :   0.0000%
      
      ```
2. Configure on-demand single-ended packet loss measurement for the AC between CE1 and PE1.
   
   
   1. Configure basic Ethernet CFM functions and specify the MEP type as outward.
      
      Configure basic Ethernet CFM functions on each PE. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md1** and an MA named **ma2**, and bind the MA to the VSI.
      
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
      [*CE1-GigabitEthernet0/1/1] port default vlan 2
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
      [*CE1-md-md1] ma ma2
      ```
      ```
      [*CE1-md-md1-ma-ma2] map vlan 2
      ```
      ```
      [*CE1-md-md1-ma-ma2] mep mep-id 3 interface gigabitethernet0/1/1 outward
      ```
      ```
      [*CE1-md-md1-ma-ma2] mep ccm-send mep-id 3 enable
      ```
      ```
      [*CE1-md-md1-ma-ma2] remote-mep mep-id 4
      ```
      ```
      [*CE1-md-md1-ma-ma2] remote-mep ccm-receive mep-id 4 enable
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
      [~PE1] cfm md md1
      ```
      ```
      [*PE1-md-md1] ma ma2
      ```
      ```
      [*PE1-md-md1-ma-ma2] map vsi ldp1
      ```
      ```
      [*PE1-md-md1-ma-ma2] mep mep-id 4 interface gigabitethernet0/1/1.1 outward
      ```
      ```
      [*PE1-md-md1-ma-ma2] mep ccm-send mep-id 4 enable
      ```
      ```
      [*PE1-md-md1-ma-ma2] remote-mep mep-id 3
      ```
      ```
      [*PE1-md-md1-ma-ma2] remote-mep ccm-receive mep-id 3 enable
      ```
   2. Configure the test instance.
      
      # Configure CE1.
      
      ```
      [*CE1] cfm md md1
      ```
      ```
      [*CE1-md-md1] ma ma2
      ```
      ```
      [*CE1-md-md1-ma-ma2] test-id 2 mep 3
      ```
      ```
      [*CE1-md-md1-ma-ma2] quit
      ```
      ```
      [*CE1-md-md1] quit
      ```
      ```
      [*CE1] commit
      ```
      
      # Configure PE1.
      
      ```
      [~PE1] cfm md md1
      ```
      ```
      [*PE1-md-md1] ma ma2
      ```
      ```
      [*PE1-md-md1-ma-ma2] test-id 2 mep 4 remote-mep 3
      ```
      ```
      [*PE1-md-md1-ma-ma2] quit
      ```
      ```
      [*PE1-md-md1] quit
      ```
      ```
      [*PE1] commit
      ```
   3. Configure the LMM reception function on CE1.
      
      # Configure CE1.
      
      ```
      [~CE1-md-md1-ma-ma2] loss-measure single-ended receive test-id 2
      ```
      ```
      [*CE1-md-md1-ma-ma2] quit
      ```
      ```
      [*CE1-md-md1] quit
      ```
      ```
      [*CE1] commit
      ```
   4. Enable on-demand single-ended packet loss measurement.
      
      # Configure PE1.
      
      ```
      [~PE1-md-md1-ma-ma2] loss-measure single-ended send test-id 2 interval 1000 count 10
      ```
      ```
      [*PE1-md-md1-ma-ma2] quit
      ```
      ```
      [*PE1-md-md1] quit
      ```
      ```
      [*PE1] commit
      ```
   5. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to view single-ended packet loss statistics.
      
      ```
      <PE1> display y1731 statistic-type single-loss
      Latest single-ended loss statistics of test-id 1:
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
         11             0             0.0000%              0              0.0000%
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
   port default vlan 2
  #
   cfm md md1
    ma ma2
     map vlan 2
     mep mep-id 3 interface GigabitEthernet0/1/1 outward
     mep ccm-send mep-id 3 enable
     remote-mep mep-id 4
     remote-mep ccm-receive mep-id 4 enable
     test-id 2 mep 3
     loss-measure single-ended receive test-id 2
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
   sysname PE1
  #
   cfm version standard
   cfm enable
  #
   mpls lsr-id 2.2.2.2
   mpls
  #
   mpls l2vpn
  #
  vsi ldp1 static
   pwsignal ldp
    vsi-id 1
    peer 1.1.1.1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 1
   l2 binding vsi ldp1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
   cfm md md1
    ma ma1
     map vsi ldp1
     mep mep-id 1 interface GigabitEthernet0/1/1.1 inward
     mep ccm-send mep-id 1 enable
     remote-mep mep-id 2
     remote-mep ccm-receive mep-id 2 enable
     test-id 1 mep 1 remote-mep 2 peer-ip 1.1.1.1
     loss-measure single-ended send test-id 1 interval 1000 count 20
  #
    ma ma2
     map vsi ldp1
     mep mep-id 4 interface GigabitEthernet0/1/1.1 outward
     mep ccm-send mep-id 4 enable
     remote-mep mep-id 3
     remote-mep ccm-receive mep-id 3 enable
     test-id 2 mep 4 remote-mep 3
     loss-measure single-ended receive test-id 2
     loss-measure single-ended send test-id 2 interval 1000 count 10
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
   mpls lsr-id 1.1.1.1
   mpls
  #
   mpls l2vpn
  #
  vsi ldp1 static
   pwsignal ldp
    vsi-id 1
    peer 2.2.2.2
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 2
   l2 binding vsi ldp1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
   cfm md md1
    ma ma1
     map vsi ldp1
     mep mep-id 2 interface GigabitEthernet0/1/1.1 inward
     mep ccm-send mep-id 2 enable
     remote-mep mep-id 1
     remote-mep ccm-receive mep-id 1 enable
     test-id 1 mep 2 peer-ip 2.2.2.2
     loss-measure single-ended receive test-id 1
  #
  return
  ```