Example for Configuring VPWS Heterogeneous Interworking Between Ethernet and HDLC Links
=======================================================================================

Example_for_Configuring_VPWS_Heterogeneous_Interworking_Between_Ethernet_and_HDLC_Links

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369926__fig_dc_vrp_vpws_cfg_301601), CE1 connects to PE1 over a GE link, and CE2 connects to PE2 over an HDLC link.

CE1 and CE2 are required to communicate.

**Figure 1** Network diagram of configuring VPWS heterogeneous interworking between Ethernet and HDLC links (LDP VPWS)![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 through 4 represent GE0/1/0, GE0/2/0, POS0/1/0, and POS0/2/0, respectively.

  
![](images/fig_dc_vrp_vpws_cfg_301601.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable an IGP on the MPLS backbone network for communication between devices (PEs and Ps) on the backbone network.
2. Establish a remote MPLS LDP session between PEs.
3. Establish a tunnel between PEs based on the tunnel policy and create a VPWS connection.
4. Ensure that CE interfaces have the same MTUs as the PE interfaces they connect to.
5. Configure on each PE the MAC address or IP address that each PE uses as the destination address when sending packets to its connected CE.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of the remote peer of each PE
* VC IDs
* MTUs of interconnected PE and CE interfaces
* MAC addresses that PEs use as the destination addresses when sending packets to their connected CEs

#### Procedure

1. Configure an IP address and an IGP on each interface of the MPLS backbone network. This example uses OSPF as the IGP. The configuration details are not provided here. For configuration details, see xref in this section.
   
   
   
   After the configuration is complete, run the **display ip routing-table** command on each LSR. The command output shows that each LSR has learned routes destined for the LSR IDs of other LSRs. Run the **display ospf peer** command. The command output shows that the OSPF neighbor relationship has been set up and its status is **FULL**.
2. Configure MPLS and MPLS LDP, establish an LDP LSP, and establish a remote LDP session between PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.9
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] quit
   ```
   ```
   [*PE1] mpls ldp remote-peer 3.3.3.9
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.9] remote-ip 3.3.3.9
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.9] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] mpls lsr-id 2.2.2.9
   ```
   ```
   [*P] mpls
   ```
   ```
   [*P-mpls] quit
   ```
   ```
   [*P] mpls ldp
   ```
   ```
   [*P-mpls-ldp] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/2/0] commit
   ```
   ```
   [~P-GigabitEthernet0/2/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 3.3.3.9
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] quit
   ```
   ```
   [*PE2] mpls ldp remote-peer 1.1.1.9
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.9] remote-ip 1.1.1.9
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.9] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] quit
   ```
   
   After the configuration is complete, run the **display mpls ldp session** command on each LSR to view information about the established LDP session.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
   --------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
   --------------------------------------------------------------------------
    2.2.2.9:0          Operational DU   Passive  000:00:00    4/5
    3.3.3.9:0          Operational DU   Passive  000:00:02    10/10
   --------------------------------------------------------------------------
   TOTAL: 2 Session(s) Found.
   ```
3. Configure VPWS heterogeneous interworking.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] ip address 10.10.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls l2vc 3.3.3.9 1 ip-interworking
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] local-ce ip 10.10.1.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface pos 0/1/0
   ```
   ```
   [*CE2-Pos0/1/0] mtu 1500
   ```
   ```
   [*CE2-Pos0/1/0] shutdown
   ```
   ```
   [*CE2-Pos0/1/0] link-protocol hdlc
   ```
   ```
   [*CE2-Pos0/1/0] ip address 10.10.1.2 24
   ```
   ```
   [*CE2-Pos0/1/0] commit
   ```
   ```
   [*CE2-Pos0/1/0] undo shutdown
   ```
   ```
   [*CE2-Pos0/1/0] commit
   ```
   ```
   [~CE2-Pos0/1/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
   ```
   [*PE2] interface pos 0/2/0
   ```
   ```
   [*PE2-Pos0/2/0] mtu 1500
   ```
   ```
   [*PE2-Pos0/2/0] shutdown
   ```
   ```
   [*PE2-Pos0/2/0] link-protocol hdlc
   ```
   ```
   [*PE2-Pos0/2/0] mpls l2vc 1.1.1.9 1 ip-interworking
   ```
   ```
   [*PE2-Pos0/2/0] commit
   ```
   ```
   [*PE2-Pos0/2/0] undo shutdown
   ```
   ```
   [*PE2-Pos0/2/0] commit
   ```
   ```
   [~PE2-Pos0/2/0] quit
   ```
4. Verify the configuration.
   
   
   
   After completing the configurations, run the **display mpls l2vc** command on PEs. The command output shows that **VC state** is **up** and **VC type** is **IP-interworking**.
   
   ```
   <PE1> display mpls l2vc interface gigabitethernet 0/1/0
   ```
   ```
   *client interface       : GigabitEthernet0/1/0 is up
    Administrator PW       : no
    session state          : up
    AC status              : up
    VC state               : up
    Label state            : 0
    Token state            : 0
    VC ID                  : 100
    VC type                : IP-interworking
    destination            : 192.168.3.3
    local group ID         : 0         remote group ID      : 0
    local VC label         : 18        remote VC label      : 18
    local AC OAM State     : up
    local PSN OAM State    : up
    local forwarding state : forwarding
    local status code      : 0x0 (forwarding)
    remote AC OAM State    : up
    remote PSN OAM state   : up
    remote forwarding state: forwarding
    remote status code     : 0x0 (forwarding)
    ignore standby state   : no
    BFD for PW             : unavailable
    VCCV State             : --
    manual fault           : not set
    active state           : active
    forwarding entry       : exist
    OAM Protocol           : --
    OAM Status             : --
    OAM Fault Type         : --
    PW APS ID              : --  
    PW APS Status          : --
    TTL Value              : 1
    link state             : up
    local VC MTU           : 1500      remote VC MTU        : 1500
    local VCCV             : alert ttl lsp-ping bfd
    remote VCCV            : alert ttl lsp-ping bfd
    local control word     : disable   remote control word  : disable
    tunnel policy name     : --
    PW template name       : --
    primary or secondary   : primary
    load balance type      : flow
    Access-port            : false
    Switchover Flag        : false
    VC tunnel info         : 1 tunnels
       NO.0 TNL type       : ldp, TNL ID : 0x0000000001004c4b43
    create time            : 0 days, 0 hours, 6 minutes, 29 seconds
    up time                : 0 days, 0 hours, 5 minutes, 21 seconds
    last change time       : 0 days, 0 hours, 5 minutes, 21 seconds
    VC last up time        : 2012/12/05 02:50:41
    VC total up time       : 0 days, 0 hours, 5 minutes, 21 seconds
    CKey                   : 1
    NKey                   : 1493172332
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
   
   In addition, CE1 and CE2 can ping each other.
   
   ```
   <CE1> ping 10.10.1.2
   ```
   ```
     PING 10.10.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.10.1.2: bytes=56 Sequence=1 ttl=253 time=4 ms
       Reply from 10.10.1.2: bytes=56 Sequence=2 ttl=253 time=2 ms
       Reply from 10.10.1.2: bytes=56 Sequence=3 ttl=253 time=1 ms
       Reply from 10.10.1.2: bytes=56 Sequence=4 ttl=253 time=2 ms
       Reply from 10.10.1.2: bytes=56 Sequence=5 ttl=253 time=2 ms
   
     --- 10.10.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/2/4 ms
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  mpls ldp remote-peer 3.3.3.9
   remote-ip 3.3.3.9
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   local-ce ip 10.10.1.1
   mpls l2vc 3.3.3.9 1 ip-interworking
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.9
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
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  mpls ldp remote-peer 1.1.1.9
   remote-ip 1.1.1.9
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface Pos0/2/0
   mtu 1500
   undo shutdown
   link-protocol hdlc
   mpls l2vc 1.1.1.9 1 ip-interworking
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 10.2.1.0 0.0.0.255
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface Pos0/1/0
   mtu 1500
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
   link-protocol hdlc
  #
  return
  ```