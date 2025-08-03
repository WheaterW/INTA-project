Example for Configuring TDMoPSN
===============================

TDM transparent cell transport provides a new alternative for wireless operators. Through TDM transparent cell transport, services between the BTSs and BSCs in the same city can be transparently transmitted over CES links in a Metro Ethernet (ME) network. Data of the fractional E1 interface can be transmitted from the GSM BTS to BSC in the mode of structuralized CES circuit emulation.Through TDM transparent cell transport, services between the users and companies in the same city can be transparently transmitted over TDM links in a Metro Ethernet (ME) network.

#### Networking Requirements

Generally, on a 2G RAN, one to three E1 interfaces on a BTS are connected to a BSC. Some mobile operators do not own fixed network infrastructure, and have to rent E1 lines of fixed-line network operators at a high price. By deploying CESoPSN service, that is, CES transparent transmission on a 2G RAN, these mobile operators can achieve transparent transmission of 2G services between the BTSs and BSCs in the same city over CES links in a Metro Ethernet (ME) network, which is both simple and cost-saving.

As shown in [Figure 1](#EN-US_TASK_0172364240__fig_dc_atnv_cfg_00713901), it is required that the BTSUser and PE1 should be connected through two E1 links. The BSCCompany and PE2 should be connected through the CPOS interface. On the channelized serial interface of E1 links, configure the encapsulation protocol as TDM. Then, a PW is set up between PE1 and PE2 to transparently transmit TDM data.

**Figure 1** Networking diagram of configuring TDMoPSN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, interface4, and interface5 represent GE 0/2/0, GE 0/2/1, E1 0/1/1, E1 0/1/2, and CPOS 0/1/1, respectively.


  
![](images/fig_dc_atn_tdm_cfg_001001.png)

| Router | Interface | IP Address |
| --- | --- | --- |
| PE1 | GE 0/2/0  Loopback0 | 10.1.1.1/24  192.168.2.2/32 |
| P | GE 0/2/0  GE 0/2/1  Loopback0 | 10.1.1.2/24  10.2.1.1/24  192.168.4.4/32 |
| PE2 | GE 0/2/0  Loopback0 | 10.2.1.2/24  192.168.3.3/32 |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Run the IGP protocol on the backbone network so that devices can communicate with each other.
2. Configure basic MPLS functions on the backbone network, and configure MPLS L2VPN functions on PE devices. Establish the remote MPLS LDP peer relationship between PEs at both ends of the PW.
3. Configure parameters for the TDM interface.
4. Configure the PW template.
5. Establish MPLS L2VC connections on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* L2VC IDs at both ends of the PW (must be the same)
* MPLS LSR IDs of the PEs and P router
* IP addresses of the remote peers of PEs
* Coding mode and frame format of the E1/CE1 interface

#### Procedure

1. Run the IGP protocol on the backbone network so that devices can communicate with each other. For detailed configurations, see the configuration file of this example.
2. Configure basic MPLS functions on the backbone network, and configure MPLS L2VPN functions on PE devices. Then, establish the remote MPLS LDP peer relationship between PEs at both ends of the PW. For detailed configurations, see the configuration file of this example.
   
   
   
   The remote MPLS LDP peer relationship is required only for the dynamic PW.
3. Configure parameters for the TDM interface.
   
   
   1. Configure PE1.
      
      # Configure the channelized mode and CRC4 frames for CE1 0/3/1 and CE1 0/3/2 on PE1.
      
      ```
      [~PE1] controller e1 0/1/1
      [~PE1-E1 0/1/1] using ce1
      [*PE1-E1 0/1/1] frame-format crc4
      [*PE1-E1 0/1/1] channel-set 1 timeslot-list 1-31
      [*PE1-E1 0/1/1] quit
      [*PE1] controller e1 0/1/2
      [*PE1-E1 0/1/2] using ce1
      [*PE1-E1 0/1/2] frame-format crc4
      [*PE1-E1 0/1/2] channel-set 1 timeslot-list 1-31
      [*PE1-E1 0/1/2] quit
      [*PE1-E1 0/1/2] commit
      ```
   2. Configure PE2.
      
      # Set parameters for the CPOS interface on PE2.
      
      ```
      [~PE2] controller cpos 0/1/1
      [~PE2-Cpos0/1/1] e1 1 channel-set 1 timeslot-list 1-31
      [*PE2-Cpos0/1/1] e1 2 channel-set 2 timeslot-list 1-31
      [*PE2-Cpos0/1/1] quit
      [*PE2] commit
      ```
4. Configure the encapsulation protocol on the serial interface as TDM.
   
   
   1. Configure PE1.
      
      ```
      [~PE1] interface serial0/1/1:1
      [~PE1-Serial0/1/1:1] link-protocol tdm
      [*PE1-Serial0/1/1:1] quit
      [*PE1] interface serial0/1/1:1
      [*PE1-Serial0/1/1:1] link-protocol tdm
      [*PE1-Serial0/1/1:1] quit
      [*PE1] commit
      ```
   2. Configure PE2.
      
      ```
      [~PE2] interface serial0/1/1/1:1
      [~PE2-Serial0/1/1/1:1] link-protocol tdm
      [*PE2-Serial0/1/1/1:1] quit
      [*PE2] interface serial0/1/1/2:2
      [*PE2-Serial0/1/1/2:2] link-protocol tdm
      [*PE2-Serial0/1/1/2:2] quit
      [*PE2] commit
      ```
5. Configuring the PW.
   
   
   1. Configure PE1.
      ```
      [~PE1] pw-template 1to3
      [*PE1-pw-template-1to3] peer-address 192.168.3.3
      [*PE1-pw-template-1to3] jitter-buffer depth 8
      [*PE1-pw-template-1to3] tdm-encapsulation-number 24
      [*PE1-pw-template-1to3] quit
      [*PE1] interface serial0/1/1:1
      [*PE1-Serial0/1/1:1] mpls l2vc pw-template 1to3 100
      [*PE1] interface serial0/1/2:1
      [*PE1-Serial0/1/2:1] mpls l2vc pw-template 1to3 200
      [*PE1-Serial0/1/2:1] quit
      [*PE1] commit
      ```
   2. Configure PE2.
      
      ```
      [~PE2] pw-template 3to1
      [*PE2-pw-template-3to1] peer-address 192.168.2.2
      [*PE2-pw-template-3to1] jitter-buffer depth 8
      [*PE2-pw-template-3to1] tdm-encapsulation-number 24
      [*PE2-pw-template-3to1] quit
      [*PE2] interface serial0/1/1/1:1
      [*PE2-Serial0/1/1/1:1] mpls l2vc pw-template 3to1 100 control-word 
      [*PE2-Serial0/1/1/1:1] undo shutdown
      [*PE2-Serial0/1/1/1:1] quit
      [*PE2] interface serial0/1/1/2:2
      [*PE2-Serial0/1/1/2:2] mpls l2vc pw-template 3to1 200 control-word 
      [*PE2-Serial0/1/1/2:2] undo shutdown
      [*PE2-Serial0/1/1/2:2] quit
      [*PE2] commit
      ```
6. Verify the configuration.
   
   
   
   Run the **display mpls l2vc** command on PEs. You can view that the status of the PW is Up.
   
   Take the display on PE1 as an example:
   
   ```
   <PE1> display mpls l2vc interface serial0/1/1:1
    *client interface       : Serial0/1/1:1 is up
     session state          : up
     AC status              : up
     VC state               : up
     VC ID                  : 100
     VC type                : CESoPSN basic mode
     destination            : 192.168.3.3
     local group ID         : 0 
     remote group ID        : 0
     local VC label         : 146432
     remote VC label        : 145287
     TDM encapsulation number : 24
     jitter-buffer            : 8
     idle-code                : 33
     rtp-header               : disable
     local AC OAM State     : up
     local PSN State        : up
     local forwarding state : forwarding
     local status code      : 0x0
     remote AC OAM state    : up
     remote PSN state       : up
     remote forwarding state: forwarding
     remote statuscode      : 0x0   
     BFD for PW             : unavailable
     manual fault           : not set
     active state           : active
     forwarding entry       : not exist
     link state             : up
     local VC MTU           : 1500         
     remote VC MTU          : 1500
     local VCCV             : alert lsp-ping bfd
     remote VCCV            : none
     local control word     : disable      
     remote control word    : disable
     tunnel policy name     : --
     traffic behavior name  : --
     PW template name       : --
     primary or secondary   : primary
     VC tunnel/token info  : 1 tunnels/tokens
     NO.0 TNL type : lsp , TNL ID : 0x208000
     create time            : 0 days, 4 hours, 48 minutes, 51 seconds
     up time                : 0 days, 3 hours, 43 minutes, 49 seconds
     last change time       : 0 days, 0 hours, 39 minutes, 29 seconds
     VC last up time        : 2008/12/26 12:02:49
     VC total up time       : 0 days, 3 hours, 43 minutes, 49 seconds
     CKey                   : 11
     NKey                   : 10
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

#### Configuration Files

* Configuration file of PE1
  
  ```
  #
   sysname PE1
  #
   mpls lsr-id 192.168.2.2
   mpls
  #
   mpls l2vpn
  #
  pw-template 1to3
   peer-address 192.168.3.3
   jitter-buffer depth 8
   tdm-encapsulation-number 24
  #
  mpls ldp
  #
   mpls ldp remote-peer 192.168.3.3
   remote-ip 192.168.3.3 
  #
  controller e1 0/1/1
  using ce1
  frame-format crc4
  channel-set 1 timeslot-list 1-31
  undo shutdown
  #
  controller e1 0/1/2
  using ce1
  frame-format crc4
  channel-set 1 timeslot-list 1-31
  undo shutdown
  #
  interface serial0/1/1:1
  link-protocol tdm
  mpls l2vc pw-template 1to3 100
  undo shutdown
  #
  interface serial0/1/2:1
  link-protocol tdm
  mpls l2vc pw-template 1to3 200
  undo shutdown
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 192.168.2.2 255.255.255.255
  #
  ospf 1
  area 0.0.0.0
    network 192.168.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  
  ```
* Configuration file of PE2
  
  ```
  #
   sysname PE2
  #
   mpls lsr-id 192.168.3.3
   mpls
  #
   mpls l2vpn
  #
  pw-template 3to1
   peer-address 192.168.2.2
   jitter-buffer depth 8
   tdm-encapsulation-number 24
  #
  mpls ldp
  #
   mpls ldp remote-peer 192.168.2.2
   remote-ip 192.168.2.2
  #
  controller cpos 0/1/1
  e1 1 channel-set 1 timeslot-list 1-31
  e1 2 channel-set 2 timeslot-list 1-31
  #
  interface serial0/1/1/1:1
  link-protocol tdm
  mpls l2vc pw-template 3to1 100 control-word
  undo shutdown
  #
  interface serial0/1/1/2:2
  link-protocol tdm
  mpls l2vc pw-template 3to1 200 control-word
  undo shutdown
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 192.168.3.3 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 192.168.3.3 0.0.0.0
    network 10.2.2.0 0.0.0.255
  #
  return
  
  ```
* Configuration file of P
  
  ```
  #
   sysname P
  #
   mpls lsr-id 192.168.4.4
   mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ip address 10.2.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 192.168.4.4 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 192.168.4.4 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.2.0 0.0.0.255
  #
  return
  
  ```