CES ACR Configuration Example - E1 Link
=======================================

CES_ACR_Configuration_Example_-_E1_Link

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001779081110__fig_dc_ne_clock_cfg_502101), gNodeB and PE1 are connected through an E1 link, and NGC and PE2 are connected through E1 interfaces. The encapsulation protocol is configured as TDM on the channelized serial interfaces of the E1 link. A PW is formed between PE1 and PE2 to transparently transmit TDM cells.

After the ACR function is configured on PE1, PE1 can transparently transmit clock signals through the PW to implement time synchronization between PE1 and PE2.

**Figure 1** Typical networking for configuring ACR![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configurations in this example are performed on PE1 and PE2. The HUAWEI NE40E-M2 series can function as PE1 or PE2.

In this example, interface1, interface2, and interface3 represent E1 0/1/0, GE0/2/0, and GE0/2/1, respectively.


  
![](figure/en-us_image_0000001825840881.png)

| **Device** | **Interface** | **IP Address** |
| --- | --- | --- |
| PE1 | GE0/2/0  Loopback0 | 10.1.1.1/24  2.2.2.2/32 |
| P | GE0/2/0  GE0/2/1  Loopback0 | 10.1.1.2/24  10.2.1.1/24  4.4.4.4/32 |
| PE2 | GE0/2/1  Loopback0 | 10.2.1.2/24  3.3.3.3/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the P and PEs to implement interworking.
2. Configure basic MPLS functions. Configure MPLS L2VPN on PE1 and PE2, and establish a remote MPLS LDP peer relationship between PE1 and PE2.
3. Configure the CES ACR function on PE1 and PE2.
4. Configure the encapsulation protocol as TDM for the serial interfaces on PE1 and PE2.
5. Configure a PW on PE1 and PE2.

#### Data Preparation

To complete the configuration, you need the following data:

* L2VC IDs on both ends of the PW
* MPLS LSR IDs of PE1, P, and PE2
* IP addresses of the loopback interfaces used to configure remote peers on PE1 and PE2
* ID of the clock recovery domain on PE1

#### Procedure

1. Run an IGP on the backbone network so that devices can communicate with each other. For configuration files, see Configuration Files in this section.
2. Configure basic MPLS functions on the backbone network, and configure MPLS L2VPN on PEs. Establish a remote MPLS LDP peer relationship between the PEs at both ends of the PW. For configuration files, see Configuration Files in this section.
   
   
   
   A remote MPLS LDP peer relationship needs to be set up only between dynamic PWs.
3. Configure ACR on PE1 and PE2.
   
   
   1. Configure PE1.
      
      ```
      [*PE1] controller e1 0/1/0
      [*PE1-E1 0/1/0] clock recovery-domain 1
      [*PE1-E1 0/1/0] commit
      [*PE1-E1 0/1/0] quit
      ```
      
      # Configure PE1 to obtain a clock source recovered by CES ACR from clock recovery domain 1 on subcard 1 of the interface board.
      
      ```
      [*PE1] clock source cesacr slot 0 card 1 recovery-domain 1 synchronization enable
      [*PE1] clock source cesacr slot 0 card 1 recovery-domain 1 ssm prc
      [*PE1] clock source cesacr slot 0 card 1 recovery-domain 1 priority 1
      [*PE1] commit
      [~PE1] quit
      ```
4. Configure the encapsulation protocol of the serial interface as TDM.
   
   
   1. Configure PE1.
      
      ```
      [*PE1] controller e1 0/1/0
      [*PE1-E1 0/1/0] using ce1
      [*PE1-E1 0/1/0] channel-set 1 timeslot-list 1-31
      [*PE1-E1 0/1/0] commit
      [~PE1-E1 0/1/0] quit
      ```
      ```
      [*PE1] interface serial0/1/0:1
      [*PE1-Serial0/1/0:1] link-protocol tdm
      [*PE1-Serial0/1/0:1] commit
      [~PE1-Serial0/1/0:1] quit
      ```
   2. Configure PE2.
      
      ```
      [*PE2] controller e1 0/1/0
      [*PE2-E1 0/1/0] using ce1
      [*PE2-E1 0/1/0] channel-set 1 timeslot-list 1-31
      [*PE2-E1 0/1/0] commit
      [~PE2-E1 0/1/0] quit
      ```
      ```
      [*PE2] interface serial0/1/0:1
      [*PE2-Serial0/1/0:1] link-protocol tdm
      [*PE2-Serial0/1/0:1] commit
      [~PE2-Serial0/1/0:1] quit
      ```
5. Configure a PW.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   PW protection is supported. If one of multiple CES PWs fails, clock recovery is automatically switched to another CES PW.
   
   1. Configure PE1.
      
      ```
      [*PE1] interface serial0/1/0:1
      ```
      ```
      [*PE1-Serial0/1/0:1] mpls l2vc 3.3.3.3 100 control-word tdm-encapsulation-number 8
      ```
      ```
      [*PE1-Serial0/1/0:1] commit
      ```
      ```
      [~PE1-Serial0/1/0:1] quit
      ```
   2. Configure PE2.
      
      ```
      [*PE2] interface serial0/1/0:1
      ```
      ```
      [*PE2-Serial0/1/0:1] mpls l2vc 2.2.2.2 100 control-word tdm-encapsulation-number 8
      ```
      ```
      [*PE2-Serial0/1/0:1] commit
      ```
      ```
      [~PE2-Serial0/1/0:1] quit
      ```
6. Verify the configuration.
   
   
   
   After completing the configurations, run the **display mpls l2vc interface serial0/1/0:1** command on PE1 to check the PW status. The command output shows that the PW is in the Active state.
   
   ```
   *client interface       : Serial0/1/0:1 is up
     session state          : up
     AC state               : up
     VC state               : up
     VC ID                  : 100
     VC type                : CESoPSN basic mode
     destination            : 3.3.3.3
     local group ID         : 0            remote group ID      : 0
     local VC label         : 146433       remote VC label      : 146432
     TDM encapsulation number: 8
     jitter-buffer           : 20
     idle-code               : ff
     rtp-header              : disable
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
     forwarding entry       : exist
     link state             : up
     local VC MTU           : 1500         remote VC MTU        : 0
     local VCCV             : alert lsp-ping bfd
     remote VCCV            : alert lsp-ping bfd
     local control word     : disable      remote control word  : disable
     tunnel policy name     : --
     traffic behavior name  : --
     PW template name       : --
     primary or secondary   : primary
     VC tunnel/token info   : 1 tunnels/tokens
       NO.0  TNL type : lsp   , TNL ID : 0x40800b
     create time            : 0 days, 0 hours, 20 minutes, 27 seconds
     up time                : 0 days, 0 hours, 6 minutes, 33 seconds
     last change time       : 0 days, 0 hours, 6 minutes, 33 seconds
     VC last up time        : 2010/02/21 17:42:25
     VC total up time       : 0 days, 0 hours, 14 minutes, 38 seconds
     CKey                   : 8
     NKey                   : 7                
     
   ```
   
   Run the **display acr-dcr slot 0 card 1 recovery-domain 1** command on PE1. If **Master PW State** is displayed as **lock** in the command output, PE1 has traced the clock transmitted by PE2.
   
   ```
   [~PE1] display acr-dcr slot 0 card 1 recovery-domain 1
   ```
   ```
   Domain info
     ----------------------------------------------------------
     E1 count:  1
     Master PW SerialPort:Serial0/1/0:1,    Channel ID:404
     Master PW state: lock
   
     E1 info
     ----------------------------------------------------------
     E1 number:20,   Port:E1 0/1/0,   Direction:2,
         PW SerialPortName:Serial0/1/0:1,   Channel ID:404      
         PW count:1
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 2.2.2.2
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  mpls ldp remote-peer 3.3.3.3
   remote-ip 3.3.3.3 
  #
  clock source cesacr slot 0 card 1 recovery-domain 1 synchronization enable
  clock source cesacr slot 0 card 1 recovery-domain 1 ssm prc
  clock source cesacr slot 0 card 1 recovery-domain 1 priority 1
  #
  controller e1 0/1/0
  using ce1
  channel-set 1 timeslot-list 1-31
  clock recovery-domain 1
  undo shutdown
  #
  interface serial0/1/0:1
  link-protocol tdm
  mpls l2vc 3.3.3.3 100 control-word tdm-encapsulation-number 8
  undo shutdown
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
  area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 3.3.3.3
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  mpls ldp remote-peer 2.2.2.2
   remote-ip 2.2.2.2
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ip address 10.2.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  controller e1 0/1/0
  using ce1
  channel-set 1 timeslot-list 1-31
  clock recovery-domain 1
  undo shutdown
  #
  interface Serial0/1/0:1                                                       
   link-protocol tdm                                                              
   mpls l2vc 2.2.2.2 100 control-word tdm-encapsulation-number 8                                               
   undo shutdown
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.2.2.0 0.0.0.255
  #
  return
  
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 4.4.4.4
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
   ip address 4.4.4.4 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.2.0 0.0.0.255
  #
  return
  
  ```