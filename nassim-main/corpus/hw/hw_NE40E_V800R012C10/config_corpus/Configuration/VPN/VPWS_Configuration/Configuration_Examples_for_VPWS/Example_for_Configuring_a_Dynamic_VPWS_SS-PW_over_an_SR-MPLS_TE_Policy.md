Example for Configuring a Dynamic VPWS SS-PW over an SR-MPLS TE Policy
======================================================================

This section provides an example for configuring a dynamic VPWS SS-PW over an SR-MPLS TE Policy.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001294669453__fig_dc_vrp_vpws_cfg_301501), PE1, the P, and PE2 belong to the same AS and run OSPF for IPv4 network connectivity. It is required that a bidirectional SR-MPLS TE Policy be deployed between PE1 and PE2 to carry VPWS services.

**Figure 1** Configuring a dynamic VPWS SS-PW over an SR-MPLS TE Policy![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001248189750.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv4 forwarding and configure an IPv4 address for each interface on PE1, the P, and PE2.
2. Enable OSPF on PE1, the P, and PE2 to ensure route reachability between them.
3. Configure SR-MPLS TE Policies and tunnel policies on PE1 and PE2.
4. Set up LDP sessions between PEs.
5. Enable L2VPN on PEs and establish a VPWS connection.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv4 addresses of interfaces on PE1, the P, and PE2
* OSPF area where SR-MPLS TE Policy is enabled


#### Procedure

1. Enable IPv4 forwarding and configure IPv4 addresses for interfaces.
   
   
   
   # Configure PE1. The configurations of the P and PE2 are similar to the configuration of PE1. For configuration details, see the configuration files.
   
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
   [~PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface LoopBack 0
   ```
   ```
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] commit
   ```
2. Configure an IGP on the MPLS backbone network to ensure route reachability between devices.
   
   
   
   OSPF is used in this example.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] opaque-capability enable
   ```
   ```
   [*PE1-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE1-ospf-1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] ospf 1 
   ```
   ```
   [*P-ospf-1] opaque-capability enable
   ```
   ```
   [*P-ospf-1] area 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 10.2.2.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*P-ospf-1] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] opaque-capability enable
   ```
   ```
   [*PE2-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.2.2.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE2-ospf-1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether OSPF is successfully configured.
   
   # Display OSPF neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ospf peer
   ```
   ```
    
   (M) Indicates MADJ neighbor
    
    
             OSPF Process 1 with Router ID 10.1.1.1
                   Neighbors
    
    Area 0.0.0.0 interface 10.1.1.1 (GE0/1/0)'s neighbors
    Router ID: 10.1.1.2             Address: 10.1.1.2
      State: Full           Mode:Nbr is Master     Priority: 1
      DR: 10.1.1.2          BDR: 10.1.1.1          MTU: 0
      Dead timer due in  35  sec
      Retrans timer interval: 5
      Neighbor is up for 01h46m50s
      Neighbor Up Time : 2022-04-26 04:58:15
      Authentication Sequence: [ 0 ]
   ```
3. Configure SR on the MPLS backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] ipv4 adjacency local-ip-addr 10.1.1.1 remote-ip-addr 10.1.1.2 sid 330000
   ```
   ```
   [*PE1-segment-routing] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] segment-routing
   ```
   ```
   [*P-segment-routing] ipv4 adjacency local-ip-addr 10.1.1.2 remote-ip-addr 10.1.1.1 sid 330002
   ```
   ```
   [*P-segment-routing] ipv4 adjacency local-ip-addr 10.2.2.1 remote-ip-addr 10.2.2.2 sid 330003
   ```
   ```
   [*P-segment-routing] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] ipv4 adjacency local-ip-addr 10.2.2.2 remote-ip-addr 10.2.2.1 sid 330000
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] commit
   ```
4. Configure SR-MPLS TE Policies.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing 
   ```
   ```
   [*PE1-segment-routing] segment-list pe1
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] index 10 sid label 330000
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] index 20 sid label 330003
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] quit
   ```
   ```
   [*PE1-segment-routing] sr-te policy policy100 endpoint 3.3.3.3 color 100 
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100] candidate-path preference 200
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100-path] segment-list pe1
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100-path] quit
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100] quit
   ```
   ```
   [*PE1-segment-routing] quit
   ```
   ```
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing 
   ```
   ```
   [*PE2-segment-routing] segment-list pe2
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] index 10 sid label 330000
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] index 20 sid label 330002
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] quit
   ```
   ```
   [*PE2-segment-routing] sr-te policy policy100 endpoint 1.1.1.1 color 100
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100] candidate-path preference 200
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100-path] segment-list pe2
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100-path] quit
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100] quit
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the [**display sr-te policy**](cmdqueryname=display+sr-te+policy) command to check SR-MPLS TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display sr-te policy 
   ```
   ```
   PolicyName : policy100
   Endpoint             : 3.3.3.3                        Color                : 100
   TunnelId             : 1                              TunnelType           : SR-TE Policy
   Binding SID          : 115                            MTU                  : -
   Policy State         : Up                             State Change Time    : 2022-04-26 04:56:54
   Admin State          : Up                             Traffic Statistics   : Disable
   BFD                  : Disable                        Backup Hot-Standby   : Disable
   DiffServ-Mode        : -
   Candidate-path Count : 1
    
   Candidate-path Preference: 200
   Path State           : Active                         Path Type            : Primary
   Protocol-Origin      : Configuration(30)              Originator           : 0, 0.0.0.0
   Discriminator        : 200                            Binding SID          : 115
   GroupId              : 1                              Policy Name          : policy100
   Template ID          : -
   Segment-List Count   : 1
    Segment-List        : pe1
     Segment-List ID    : 66                             XcIndex              : 2000066
     List State         : Up                             BFD State            : -
     EXP                : -                              TTL                  : -
     DeleteTimerRemain  : -                              Weight               : 1
     Label : 330000, 330003 
   ```
5. Establish an LDP session.
   
   
   
   Establish a remote session between PE1 and PE2.
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.1
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
   [*PE1] mpls ldp remote-peer 3.3.3.3
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.3] remote-ip 3.3.3.3
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.3] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 3.3.3.3
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
   [*PE2] mpls ldp remote-peer 1.1.1.1
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, an LDP session is successfully set up between the PEs.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    --------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
    --------------------------------------------------------------------------
    3.3.3.3:0          Operational DU   Passive  0000:02:43   655/656
    --------------------------------------------------------------------------
    TOTAL: 1 Session(s) Found
   ```
6. Configure a tunnel policy and establish a VPWS connection.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] tunnel-policy tp1
   ```
   ```
   [*PE1-tunnel-policy-tp1] tunnel select-seq sr-te-policy load-balance-number 1 unmix
   ```
   ```
   [*PE1-tunnel-policy-tp1] quit
   ```
   ```
   [*PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] vlan-type dot1q 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] mpls l2vc 3.3.3.3 200 tunnel-policy tp1 endpoint 3.3.3.3 color 100
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] tunnel-policy tp1
   ```
   ```
   [*PE2-tunnel-policy-tp1] tunnel select-seq sr-te-policy load-balance-number 1 unmix
   ```
   ```
   [*PE2-tunnel-policy-tp1] quit
   ```
   ```
   [*PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] vlan-type dot1q 2
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] mpls l2vc 1.1.1.1 200 tunnel-policy tp1 endpoint 1.1.1.1 color 100
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure CE1.
   
   ```
   [~CE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] commit
   ```
   
   Configure CE2.
   
   ```
   [~CE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 2
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The VC IDs at the two ends of a VPWS connection must be the same. Otherwise, the VC cannot go up.
   * No IP address needs to be configured on PE interfaces connecting to CEs.
7. Verify the configuration.
   
   
   
   View VPWS connection information on PEs. The command output shows that a VC has been established and its status is up.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls l2vc interface gigabitethernet 0/2/0.1
   ```
   ```
    *client interface       : GigabitEthernet0/2/0.1 is up
     Administrator PW       : no
     session state          : up
     AC status              : up
     VC state               : up
     Label state            : 0
     Token state            : 0
     VC ID                  : 200
     VC type                : VLAN
     destination            : 3.3.3.3
     local group ID         : 0            remote group ID      : 0
     local VC label         : 48060        remote VC label      : 48000
     local AC OAM State     : up
     local PSN OAM State    : up
     local forwarding state : forwarding
     local status code      : 0x0 (forwarding)
     remote AC OAM state    : up
     remote PSN OAM state   : up
     remote forwarding state: forwarding
     remote status code     : 0x0 (forwarding)
     remote interface       : GigabitEthernet0/2/0.1
     ignore standby state   : no
     BFD for PW             : unavailable
     VCCV State             : up
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
     local VC MTU           : 1500         remote VC MTU        : 1500
     local VCCV             : alert ttl lsp-ping bfd
     remote VCCV            : alert ttl lsp-ping bfd
     local control word     : disable      remote control word  : disable
     tunnel policy name     : tp1
     PW template name       : --
     primary or secondary   : primary
     load balance type      : flow
     Access-port            : false
     Switchover Flag        : false
     VC tunnel info         : 1 tunnels
       NO.0  TNL type       : srtepolicy     , TNL ID : 0x000000003200000001
     create time            : 0 days, 2 hours, 57 minutes, 19 seconds
     up time                : 0 days, 0 hours, 41 minutes, 31 seconds
     last change time       : 0 days, 0 hours, 41 minutes, 31 seconds
     VC last up time        : 2022/04/26 07:12:43
     VC total up time       : 0 days, 2 hours, 46 minutes, 58 seconds
     CKey                   : 65
     NKey                   : 16777373
     PW redundancy mode     : frr
     AdminPw interface      : --
     AdminPw link state     : --
     Forward state          : send active, receive active
     Diffserv Mode          : uniform
     Service Class          : --
     Color                  : --
     DomainId               : --
     Domain Name            : -- 
   ```
   
   CE1 and CE2 can ping each other.
   
   ```
   [~CE1] ping 10.10.1.2
   ```
   ```
     PING 10.10.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.10.1.2: bytes=56 Sequence=1 ttl=255 time=4 ms
       Reply from 10.10.1.2: bytes=56 Sequence=2 ttl=255 time=3 ms
       Reply from 10.10.1.2: bytes=56 Sequence=3 ttl=255 time=3 ms
       Reply from 10.10.1.2: bytes=56 Sequence=4 ttl=255 time=4 ms
       Reply from 10.10.1.2: bytes=56 Sequence=5 ttl=255 time=3 ms
    
     --- 10.10.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 3/3/4 ms
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1
   ip address 10.10.1.1 255.255.255.0
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 2
   ip address 10.10.1.2 255.255.255.0
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
   #
   ipv4-family
  #
  mpls ldp remote-peer 3.3.3.3
   remote-ip 3.3.3.3
  #
  segment-routing
   ipv4 adjacency local-ip-addr 10.1.1.1 remote-ip-addr 10.1.1.2 sid 330000
   segment-list pe1
    index 10 sid label 330000
    index 20 sid label 330003
   sr-te policy policy100 endpoint 3.3.3.3 color 100
    candidate-path preference 200
     segment-list pe1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown 
  #
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 1
   mpls l2vc 3.3.3.3 200 tunnel-policy tp1 endpoint 3.3.3.3 color 100 
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255 
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255 
  #
  tunnel-policy tp1
   tunnel select-seq sr-te-policy load-balance-number 1 unmix 
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  segment-routing
   ipv4 adjacency local-ip-addr 10.1.1.2 remote-ip-addr 10.1.1.1 sid 330002
   ipv4 adjacency local-ip-addr 10.2.2.1 remote-ip-addr 10.2.2.2 sid 330003
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.2.1 255.255.255.0
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.2.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
   #
   ipv4-family
  #
  mpls ldp remote-peer 1.1.1.1
   remote-ip 1.1.1.1
  #
  segment-routing
   ipv4 adjacency local-ip-addr 10.2.2.2 remote-ip-addr 10.2.2.1 sid 330000
   segment-list pe2
    index 10 sid label 330000
    index 20 sid label 330002
   sr-te policy policy100 endpoint 1.1.1.1 color 100
    candidate-path preference 200
     segment-list pe2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.2.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown 
  #
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 2
   mpls l2vc 1.1.1.1 200 tunnel-policy tp1 endpoint 1.1.1.1 color 100
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.2.2.0 0.0.0.255
  #
  tunnel-policy tp1
   tunnel select-seq sr-te-policy load-balance-number 1 unmix
  #
  return
  ```