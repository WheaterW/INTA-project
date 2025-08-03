Example for Configuring TDMoPSN
===============================

Time division multiplexing (TDM) transparent transmission provides a new alternative for wireless carriers. It enables services between the base transceiver stations (BTSs) and base station controllers (BSCs) in the same city to be transparently transmitted over simple and cost-effective links on a metro Ethernet. The data of fractional E1 interfaces can be transmitted from GSM BTSs to BSCs in Structure-Aware TDM Circuit Emulation Service over Packet Switched Network (CESoPSN) mode.

#### Networking Requirements

Generally, on a 2G RAN, one to three E1 interfaces on a BTS are connected to a BSC. Some mobile carriers do not have fixed network infrastructure, and have to rent E1 lines from fixed-line network carriers at a high price. By deploying the TDMoPSN service, that is, TDM transparent transmission on a 2G RAN, carriers can transmit services between the BTSs and BSCs in the same city over TDM links on a simple and cost-effective metro Ethernet network.

On the network shown in [Figure 1](#EN-US_TASK_0172369963__fig_dc_vrp_vpws_cfg_601301), it is required that the BTS and PE1 be connected through two E1 links, and the BSC and PE2 be connected through CPOS interfaces. On the channelized serial interface of an E1 link, the encapsulation protocol is TDM. Then, a PW is set up between PE1 and PE2 to transparently transmit TDM frames.

**Figure 1** Network diagram of configuring TDMoPSN![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and CPOS0/3/0, respectively.


  
![](figure/en-us_image_0000001308753274.png)  

| Router | Interface | IP Address |
| --- | --- | --- |
| PE1 | GE0/1/0  Loopback0 | 10.1.1.1/24  192.168.2.2/32 |
| P | GE0/1/0  GE0/2/0  Loopback0 | 10.1.1.2/24  10.2.1.1/24  192.168.4.4/32 |
| PE2 | GE0/2/0  Loopback0 | 10.2.1.2/24  192.168.3.3/32 |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Run an IGP on the backbone network so that devices can communicate with each other.
2. Configure basic MPLS functions on the backbone network, and configure MPLS L2VPN functions on PEs. Then, establish a remote MPLS LDP peer relationship between the endpoint PEs of the PW.
3. Configure parameters for the TDM interface.
4. Configure PWs.
5. Establish MPLS L2VC connections on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* Same L2VC ID at both ends of the PW
* MPLS LSR IDs of the PEs and P router
* IP addresses assigned to the remote peers of PEs
* Coding mode and frame format of the E1/CE1 interface

#### Procedure

1. Run an IGP on the backbone network so that devices can communicate with each other. For detailed configurations, see Configuration Files.
2. Configure basic MPLS functions on the backbone network, and configure MPLS L2VPN functions on PEs. Establish a remote MPLS LDP peer relationship between the endpoint PEs of the PW. For detailed configurations, see Configuration Files.
   
   
   
   The remote MPLS LDP peer relationship is required only for the dynamic PW.
3. Configure parameters for the TDM interface.
   
   
   1. Configure PE1.
      
      # Configure the channelized mode, AMI code, and CRC4 frames for CE1 0/2/11 and CE1 0/2/2 on PE1.
      
      ```
      [~PE1] controller e1 0/2/1
      [~PE1-E1 0/2/1] using ce1
      [*PE1-E1 0/2/1] code ami
      [*PE1-E1 0/2/1] frame-format crc4
      [*PE1-E1 0/2/1] channel-set 1 timeslot-list 1-15
      [*PE1-E1 0/2/1] quit
      [*PE1] controller e1 0/2/2
      [*PE1-E1 0/2/2] using ce1
      [*PE1-E1 0/2/2] code ami
      [*PE1-E1 0/2/2] frame-format crc4
      [*PE1-E1 0/2/2] channel-set 1 timeslot-list 16-31
      [*PE1-E1 0/2/2] quit
      [*PE1] commit
      ```
   2. Configure PE2.
      
      # Set parameters for the CPOS interface on PE2.
      
      ```
      [~PE2] controller cpos 0/3/1
      [~PE2-Cpos0/3/1] e1 1 channel-set 1 timeslot-list 1-15
      [*PE2-Cpos0/3/1] e1 2 channel-set 2 timeslot-list 16-31
      [*PE2-Cpos0/3/1] quit
      [*PE2] commit
      ```
4. Configure the encapsulation protocol on the serial interface as TDM.
   
   
   1. Configure PE1.
      
      ```
      [~PE1] interface serial0/2/1:1
      [~PE1-Serial0/2/1:1] link-protocol tdm
      [*PE1-Serial0/2/1:1] quit
      [*PE1] interface serial0/2/2:1
      [*PE1-Serial0/2/2:1] link-protocol tdm
      [*PE1-Serial0/2/2:1] quit
      [*PE1] commit
      ```
   2. Configure PE2.
      
      ```
      [~PE2] interface serial0/3/1:1
      [~PE2-Serial0/3/1:1] link-protocol tdm
      [*PE2-Serial0/3/1:1] quit
      [*PE2] interface serial0/3/1:2
      [*PE2-Serial0/3/1:2] link-protocol tdm
      [*PE2-Serial0/3/1:2] quit
      [*PE2] commit
      ```
5. Configure PWs.
   
   
   1. Configure PE1.
      
      ```
      [~PE1] pw-template 1to3
      [*PE1-pw-template-1to3] peer-address 192.168.3.3
      [*PE1-pw-template-1to3] jitter-buffer depth 20
      [*PE1-pw-template-1to3] tdm-encapsulation-number 40
      [*PE1-pw-template-1to3] idle-code 33
      [*PE1-pw-template-1to3] quit
      [*PE1] interface serial0/2/1:1
      [*PE1-Serial0/2/1:1] mpls l2vc pw-template 1to3 100
      [*PE1] interface serial0/2/2:1
      [*PE1-Serial0/2/2:1] mpls l2vc pw-template 1to3 200
      [*PE1-Serial0/2/2:1] quit
      [*PE1] commit
      ```
   2. Configure PE2.
      
      ```
      [~PE2] pw-template 3to1
      [*PE2-pw-template-3to1] peer-address 192.168.2.2
      [*PE2-pw-template-3to1] jitter-buffer depth 20
      [*PE2-pw-template-3to1] tdm-encapsulation-number 40
      [*PE2-pw-template-3to1] idle-code 33
      [*PE2-pw-template-3to1] quit
      [*PE2] interface serial0/3/1:1
      [*PE2-Serial0/3/1:1] mpls l2vc pw-template 3to1 100
      [*PE2-Serial0/3/1:1] undo shutdown
      [*PE2-Serial0/3/1:1] quit
      [*PE2] interface serial0/3/1:2
      [*PE2-Serial0/3/1:2] mpls l2vc pw-template 3to1 200
      [*PE2-Serial0/3/1:2] undo shutdown
      [*PE2-Serial0/3/1:2] quit
      [*PE2] commit
      ```
6. Verify the configuration.
   
   
   
   Run the **display mpls l2vc** command on PEs to check PW status. The command output shows that the status is up.
   
   The following example uses the command output on PE1.
   
   ```
   <~PE1> display mpls l2vc interface serial0/2/1:1
   *client interface       : Serial0/2/1:1 is up
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
     TDM encapsulation number : 40
     jitter-buffer            : 20
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

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 192.168.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  pw-template 1to3
   peer-address 192.168.3.3
   jitter-buffer depth 20
   tdm-encapsulation-number 40
   idle-code 33
  #
  mpls ldp
  #
   mpls ldp remote-peer 192.168.3.3
   remote-ip 192.168.3.3 
  #
  controller e1 0/2/1
   using ce1
   code ami
   frame-format crc4
   channel-set 1 timeslot-list 1-15
   undo shutdown
  #
  controller e1 0/2/2
   using ce1
   code ami
   frame-format crc4
   channel-set 1 timeslot-list 16-31
   undo shutdown
  #
  interface serial0/2/1:1
   link-protocol tdm
   mpls l2vc pw-template 1to3 100
   undo shutdown
  #
  interface serial0/2/2:1
   link-protocol tdm
   mpls l2vc pw-template 1to3 200
   undo shutdown
  #
  interface GigabitEthernet0/1/0
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
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 192.168.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  pw-template 3to1
   peer-address 192.168.2.2
   jitter-buffer depth 20
   tdm-encapsulation-number 40
   idle-code 33
  #
  mpls ldp
  #
  mpls ldp remote-peer 192.168.2.2
   remote-ip 192.168.2.2
  #
  controller cpos 0/3/1
   e1 1 channel-set 1 timeslot-list 1-15
   code ami
   e1 2 channel-set 2 timeslot-list 16-31
  #
  interface serial0/3/1:1
   link-protocol tdm
   mpls l2vc pw-template 3to1 100
   undo shutdown
  #
  interface serial0/3/1:2
   link-protocol tdm
   mpls l2vc pw-template 3to1 200
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
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 192.168.4.4
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
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