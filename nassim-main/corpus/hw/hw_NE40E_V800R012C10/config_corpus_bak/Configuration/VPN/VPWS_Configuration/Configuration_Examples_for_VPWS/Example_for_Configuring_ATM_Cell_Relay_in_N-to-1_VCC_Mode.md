Example for Configuring ATM Cell Relay in N-to-1 VCC Mode
=========================================================

If a large number of ATM services are transparently transmitted over a PSN, you can configure ATM cell relay in N-to-1 VCC mode. In this mode, an ATM physical link can be divided into multiple PVCs, with each PVC transmitting a single type of service. For example, you can create three PVCs to transmit audio, video, and data traffic, respectively.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section does not apply to the M2K or M2K-B models.

On the network shown in [Figure 1](#EN-US_TASK_0172369975__fig_dc_vrp_vpws_cfg_600901), the NodeB connects to PE1 through two E1 links that are added to an IMA group, and four PVCs are configured on an IMA group sub-interface. The RNC connects to PE2 through E1 links that are also added to an IMA group, and four PVCs are configured on an IMA group sub-interface. A PW is established between PE1 and PE2 to transparently transmit ATM cells.

**Figure 1** Configuring ATM cell relay in N-to-1 VCC mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_vpws_cfg_600901.png)  

| Router | Interface | IP Address |
| --- | --- | --- |
| PE1 | GE0/1/0  Loopback0 | 10.1.1.1/24  192.168.2.2/32 |
| P | GE0/1/0  GE0/2/0  Loopback0 | 10.1.1.2/24  10.2.1.1/24  192.168.4.4/32 |
| PE2 | GE0/2/0  Loopback0 | 10.2.1.2/24  192.168.3.3/32 |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Run the IGP protocol on the backbone network so that devices can communicate with each other.
2. Configure basic MPLS functions on the backbone network, and configure MPLS L2VPN functions on PEs. Establish the remote MPLS LDP peer relationship between PEs at both ends of the PW.
3. Set parameters for the serial interface.
4. Configure the PW template.
5. Establish MPLS L2VC connections on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* L2VC IDs at both ends of the PW (must be the same)
* MPLS LSR IDs of the PEs and P router
* IP address of the remote peer of the PE
* Coding mode and frame format of the E1/CE1 interface

#### Procedure

1. Run the IGP protocol on the backbone network so that devices can communicate with each other. For detailed configurations, see Configuration Files.
2. Configure basic MPLS functions on the backbone network, and configure MPLS L2VPN functions on PEs. Then, establish the remote MPLS LDP peer relationship between PEs at both ends of the PW. For detailed configurations, see Configuration Files.
   
   
   
   The remote MPLS LDP peer relationship is required only for the dynamic PW.
3. Set parameters for the serial interface on PE1 and then add the serial interface to the IMA group. Set parameters for the IMA interface on PE2.
   
   
   1. Configure PE1.
      
      # Configure the channelized mode and non-CRC4 frame format for E1 0/2/1 and E1 0/2/2 on PE1.
      
      ```
      [~PE1] controller e1 0/2/1
      [~PE1-E10/2/1] channel-set 1 timeslot-list 1-15
      [*PE1] controller e1 0/2/2
      [*PE1-E10/2/2] channel-set 1 timeslot-list 16-30
      [*PE1-E10/2/2] quit
      [*PE1] commit
      ```
      
      # Create an IMA interface.
      
      ```
      [~PE1] interface ima-group 0/2/1
      [~PE1-Ima-group0/2/1] quit
      [*PE1] commit
      ```
      
      # Add the channelized serial interface to the IMA group.
      
      ```
      [~PE1] interface serial0/2/1:1
      [*PE1-Serial0/2/1:1] link-protocol atm
      [*PE1-Serial0/2/1:1] ima ima-group 0/2/1
      [*PE1-Serial0/2/1:1] quit
      [*PE1] interface serial0/2/2:1
      [*PE1-Serial0/2/2:1] link-protocol atm
      [*PE1-Serial0/2/2:1] ima ima-group 0/2/1
      [*PE1-Serial0/2/2:1] quit
      [*PE1] commit
      ```
   2. Configure PE2.
      
      # Configure the channelized mode and non-CRC4 frame format for E1 0/2/1 on PE2.
      
      ```
      [~PE2] controller e1 0/2/1
      [~PE2-E10/2/1] channel-set 1 timeslot-list 1-15
      [*PE2-E10/2/1] quit
      [*PE2] commit
      ```
      
      # Create an IMA interface.
      
      ```
      [~PE2] interface ima-group 0/2/1
      [~PE2-Ima-group0/2/1] quit
      [*PE2] commit
      ```
      
      # Add the channelized serial interface to the IMA group.
      
      ```
      [~PE2] interface serial0/2/1:1
      [*PE2-Serial0/2/1:1] link-protocol atm
      [*PE2-Serial0/2/1:1] ima ima-group 0/2/1
      [*PE2-Serial0/2/1:1] quit
      [*PE2] commit
      ```
4. Configure the PW and configure N-to-1 VCC transparent transmission of ATM cells.
   
   
   1. Configure PE1.
      
      ```
      [~PE1] pw-template 1to3
      [*PE1-pw-template-1to3] peer-address 192.168.3.3
      [*PE1-pw-template-1to3] atm-pack-overtime 1000
      [*PE1-pw-template-1to3] quit
      [*PE1] interface ima-group 0/2/1.1
      [*PE1-Ima-group0/2/1.1] pvc 1/100
      [*PE1-Ima-group0/2/1.1-1/100] quit
      [*PE1-Ima-group0/2/1.1] pvc 1/200
      [*PE1-Ima-group0/2/1.1-1/200] quit
      [*PE1-Ima-group0/2/1.1] pvc 1/300
      [*PE1-Ima-group0/2/1.1-1/300] quit
      [*PE1-Ima-group0/2/1.1] pvc 1/400
      [*PE1-Ima-group0/2/1.1-1/400] quit
      [*PE1-Ima-group0/2/1.1] mpls l2vc pw-template 1to3 100
      [*PE1-Ima-group0/2/1.1] undo shutdown
      [*PE1-Ima-group0/2/1.1] quit
      [*PE1] commit
      ```
   2. Configure PE2.
      
      ```
      [~PE2] pw-template 3to1
      [*PE2-pw-template-3to1] peer-address 192.168.2.2
      [*PE2-pw-template-3to1] quit
      [*PE2] interface ima-group 0/2/1.1
      [*PE2-Ima-group0/2/1.1] pvc 1/100
      [*PE2-Ima-group0/2/1.1-1/100] quit
      [*PE2-Ima-group0/2/1.1] pvc 1/200
      [*PE2-Ima-group0/2/1.1-1/200] quit
      [*PE2-Ima-group0/2/1.1] pvc 1/300
      [*PE2-Ima-group0/2/1.1-1/300] quit
      [*PE2-Ima-group0/2/1.1] pvc 1/400
      [*PE2-Ima-group0/2/1.1-1/400] quit
      [*PE2-Ima-group0/2/1.1] mpls l2vc pw-template 3to1 100
      [*PE2-Ima-group0/2/1.1] undo shutdown
      [*PE2-Ima-group0/2/1.1] quit
      [*PE2] commit
      ```
5. Verify the configuration.
   
   
   
   Run the **display mpls l2vc** command on PEs to check PW status. The command output shows that the status is up.
   
   # The display on PE1 is as follows:
   
   ```
   <PE1> display mpls l2vc interface ima-group 0/2/1.1
   *client interface       : Ima-group 0/2/1.1 is up
     session state          : up
     AC status               : up
     VC state               : up
     VC ID                  : 4
     VC type                : ATM Nto1 VCC
     destination            : 192.168.3.3
     local group ID         : 0            remote group ID      : 0
     local VC label         : 146439       remote VC label      : 21504
     max ATM cells          : 28
     ATM pack overtime      : 1000
     seq-number             : disable
     local AC OAM State     : up
     local PSN State        : up
     local forwarding state : not forwarding
     local status code      : 0x0
     remote AC OAM state    : up
     remote PSN state       : up
     remote forwarding state: forwarding
     remote statuscode      : 0x0
     BFD for PW             : unavailable
     manual fault           : not set
     active state           : active
     forwarding entry       : not exist
     link state             : down
     local VC MTU           : 1500
     remote VC MTU        : 0
     local VCCV             : cw alert ttl lsp-ping bfd
     remote VCCV            : none
     local control word     : enable
     remote control word    : none
     tunnel policy name     : --
     traffic behavior name  : --
     PW template name       : --
     primary or secondary   : primary
     VC tunnel/token info   : 1 tunnels/tokens
     NO.0 TNL type : lsp , TNL ID : 0x208000
     create time            : 0 days, 0 hours, 0 minutes, 16 seconds
     up time                : 0 days, 0 hours, 0 minutes, 0 seconds
     last change time       : 0 days, 0 hours, 0 minutes, 16 seconds
     VC last up time        : 0000/00/00 00:00:00
     VC total up time       : 0 days, 0 hours, 0 minutes, 0 seconds
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
   atm-pack-overtime 1000
  #
  mpls ldp
  #
  mpls ldp remote-peer 192.168.3.3
   remote-ip 192.168.3.3 
  #
  controller e1 0/2/1
  using ce1
  code ami
  channel-set 1 timeslot-list 1-15
  undo shutdown
  #
  interface serial0/2/1:1
  link-protocol atm
  ima ima-group 0/2/1
  undo shutdown
  #
  controller e1 0/2/2
  using ce1
  code ami
  channel-set 1 timeslot-list 16-30
  undo shutdown
  #
  interface serial0/2/2:1
  link-protocol atm
  ima ima-group 0/2/1
  undo shutdown
  #
  interface ima-group 0/2/1
   undo shutdown
  #
  interface ima-group 0/2/1.1
   pvc 1/100
   pvc 1/200
   pvc 1/300
   pvc 1/400
   mpls l2vc pw-template 1to3 100
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
   atm-pack-overtime 1000
  #
  mpls ldp
  #
  mpls ldp remote-peer 192.168.2.2
   remote-ip 192.168.2.2
  #
  controller e1 0/2/1
  using ce1
  channel-set 1 timeslot-list 1-15
  undo shutdown
  #
  interface serial0/2/1:1
  link-protocol atm
  ima ima-group 0/2/1
  undo shutdown
  #
  interface ima-group 0/2/1
   undo shutdown
  #
  interface ima-group 0/2/1.1
   pvc 1/100
   pvc 1/200
   pvc 1/300
   pvc 1/400
   mpls l2vc pw-template 3to1 100
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