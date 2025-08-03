Example for Configuring Coexistence of Traditional VPLS and EVPN VPLS
=====================================================================

To prevent service interruptions during VPLS-to-EVPN evolution, configure coexistence of traditional VPLS and EVPN VPLS.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370646__fig868818241190), traditional VPLS is deployed. It is required that EVPN be deployed on PE1 and PE3, so that BGP EVPN can be used to transmit services between PE1 and PE3. To meet this requirement, an EVPN instance needs to be configured and bound to the BD on PE1 and PE3. Then, a BGP EVPN peer relationship needs to be established between PE1 and PE3.

**Figure 1** Configuring the coexistence of traditional VPLS and EVPN VPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/2/0, and GigabitEthernet0/3/0, respectively.


  
![](figure/en-us_image_0000001179249890.png)  


#### Configuration Precautions

During the configuration process, note the following:

* For the same EVPN instance, the export VPN target list of one site shares VPN targets with the import VPN target lists of the other sites. Conversely, the import VPN target list of one site shares VPN targets with the export VPN target lists of the other sites.
* Using each PE's local loopback interface address as its EVPN source address is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an EVPN instance in BD mode and a BD on each of PE1 and PE3, and bind the BD to the EVPN instance on each PE.
2. Configure a source address on each of PE1 and PE3.
3. Establish a BGP EVPN peer relationship between PE1 and PE3.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* EVPN instance evrf1's RD (100:1) and RT (1:1) on each PE

#### Procedure

1. Ensure that an EVC has been configured to carry a VPLS service. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370646__file1).
   
   
   
   Run the **display vsi name e1 verbose** command on PE1. The command output shows that the VSI named **e1** has separate PWs to PE2 and PE3, and the VSI status and PW status are up.
   
   ```
   [~PE1] display vsi name e1 verbose
   ```
   ```
    
   
    ***VSI Name               : e1
       Work Mode              : bd-mode
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 2
       PW Signaling           : bgp
       Member Discovery Style : --
       Bridge-domain Mode     : enable
       PW MAC Learn Style     : qualify
       Encapsulation Type     : vlan
       MTU                    : 1500
       Diffserv Mode          : uniform
       Service Class          : --
       Color                  : --
       DomainId               : 255
       Domain Name            : 
       Ignore AcState         : disable
       P2P VSI                : disable
       Create Time            : 0 days, 0 hours, 50 minutes, 49 seconds
       VSI State              : up
       Resource Status        : --
   
       BGP RD                 : 100:1
       SiteID/Range/Offset    : 1/10/0
       Import vpn target      : 1:1                    
       Export vpn target      : 1:1                    
       Remote Label Block     : 294928/8/0 294928/8/0 
       Local Label Block      : 0/294928/8/0 
    
       Access Bridge-domain   : Bridge-domain 10 
       Vac State              : up 
       Last Up Time           : 2018/03/23 11:01:50
       Total Up Time          : 0 days, 0 hours, 37 minutes, 53 seconds
   
     **PW Information:
   
      *Peer Ip Address        : 2.2.2.2
       PW State               : up
       Local VC Label         : 294930
       Remote VC Label        : 294929
       PW Type                : label
       Tunnel ID              : 0x0000000001004c4bc1 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 129
       Nkey                   : 16777346
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : --
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       PW Last Up Time        : 2018/03/23 11:38:42
       PW Total Up Time       : 0 days, 0 hours, 1 minutes, 1 seconds
      *Peer Ip Address        : 3.3.3.3
       PW State               : up
       Local VC Label         : 294931
       Remote VC Label        : 294929
       PW Type                : label
       Tunnel ID              : 0x0000000001004c4b42 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 130
       Nkey                   : 16777347
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : --
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       PW Last Up Time        : 2018/03/23 11:39:10
       PW Total Up Time       : 0 days, 0 hours, 0 minutes, 33 seconds
   ```
2. Configure an EVPN instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-bd10] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE3-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE3-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE3-evpn-instance-evrf1] quit
   ```
   ```
   [*PE3] bridge-domain 10
   ```
   ```
   [*PE3-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE3-bd10] quit
   ```
   ```
   [*PE3] commit
   ```
3. Configure a source address on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 3.3.3.3
   ```
   ```
   [*PE3] commit
   ```
4. Establish a BGP EVPN peer relationship between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [~PE3-bgp] l2vpn-family evpn
   ```
   ```
   [*PE3-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*PE3-bgp-af-evpn] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
5. Verify the configuration.
   
   
   
   After completing the configurations, run the **display bgp evpn peer** command on PE1. The command output shows that BGP peer relationships are in the **Established** state, indicating that a BGP peer relationship has been successfully established between PE1 and PE3.
   
   ```
   [~PE1] display bgp evpn peer
   ```
   ```
    
    BGP local router ID : 10.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     3.3.3.3         4         100        7        9     0 00:00:07 Established        1
   ```
   
   Run the **display bgp evpn all routing-table** command on PE1. The command output shows the inclusive multicast route received from PE3.
   
   ```
   [~PE1] display bgp evpn all routing-table 
   ```
   ```
    Local AS number : 100
   
    BGP Local router ID is 10.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    EVPN address family:
    Number of Inclusive Multicast Routes: 2
    Route Distinguisher: 100:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1
    *>i   0:32:3.3.3.3                                        3.3.3.3
       
   
    EVPN-Instance evrf1:
    Number of Inclusive Multicast Routes: 2
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1
    *>i   0:32:3.3.3.3                                        3.3.3.3
   ```
   
   Run the **display alarm active root verbose** command on PE1. The command output shows information about the alarm triggered when the VPLS VC on PE1 goes down. The value of HWL2VpnStateChangeReason (alarm cause parameter) is 98, indicating that the establishment of an EVPN connection causes the VPLS VC to go down.
   
   ```
   [~PE1] display alarm active root verbose 
   ```
   ```
   Sequence    : 46        
   AlarmId     : 0xD4D0001             AlarmName : hwVplsVcDown                                                    
   AlarmType   : communication         Severity  : Major            State : active 
   RootKindFlag: Independent           
   StartTime   : 2018-03-26 02:42:23                     
   Description : The status of the VPLS VC turned DOWN. (VsiName=e1, PwId=3, RemoteIp=3.3.3.3, PwType=1, HWL2VpnStateChangeReason=98, SysUpTime=23691243, TunnelPolicyName=-)
   ```
   
   Run the **display vsi name e1 verbose** command on PE1. The command output shows that only the PW to PE2 is available and its status is up.
   
   ```
   [~PE1] display vsi name e1 verbose
   ```
   ```
    ***VSI Name               : e1
       Work Mode              : bd-mode
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 2
       PW Signaling           : bgp
       Member Discovery Style : --
       Bridge-domain Mode     : enable
       PW MAC Learn Style     : qualify
       Encapsulation Type     : vlan
       MTU                    : 1500
       Diffserv Mode          : uniform
       Service Class          : --
       Color                  : --
       DomainId               : 255
       Domain Name            : 
       Ignore AcState         : disable
       P2P VSI                : disable
       Create Time            : 0 days, 1 hours, 0 minutes, 52 seconds
       VSI State              : up
       Resource Status        : --
   
       BGP RD                 : 100:1
       SiteID/Range/Offset    : 1/10/0
       Import vpn target      : 1:1                    
       Export vpn target      : 1:1                    
       Remote Label Block     : 294928/8/0 294928/8/0 
       Local Label Block      : 0/294928/8/0 
    
       Access Bridge-domain   : Bridge-domain 10 
       Vac State              : up 
       Last Up Time           : 2018/03/23 11:01:50
       Total Up Time          : 0 days, 0 hours, 47 minutes, 56 seconds
   
     **PW Information:
   
      *Peer Ip Address        : 2.2.2.2
       PW State               : up
       Local VC Label         : 294930
       Remote VC Label        : 294929
       PW Type                : label
       Tunnel ID              : 0x0000000001004c4bc1 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 129
       Nkey                   : 16777346
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : --
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       PW Last Up Time        : 2018/03/23 11:38:42
       PW Total Up Time       : 0 days, 0 hours, 11 minutes, 4 seconds
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn      
  #
  vsi e1 bd-mode
   pwsignal bgp
    route-distinguisher 100:1
    vpn-target 1:1 import-extcommunity
    vpn-target 1:1 export-extcommunity
    site 1 range 10 default-offset 0
  #
  bridge-domain 10
   l2 binding vsi e1
   evpn binding vpn-instance evrf1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   l2vpn-ad-family
    policy vpn-target
    signaling vpls
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi e1 bd-mode
   pwsignal bgp
    route-distinguisher 100:1
    vpn-target 1:1 import-extcommunity
    vpn-target 1:1 export-extcommunity
    site 2 range 10 default-offset 0
  #
  bridge-domain 10
   l2 binding vsi e1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #               
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #
   l2vpn-ad-family
    policy vpn-target
    signaling vpls
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn      
  #
  vsi e1 bd-mode
   pwsignal bgp
    route-distinguisher 100:1
    vpn-target 1:1 import-extcommunity
    vpn-target 1:1 export-extcommunity
    site 3 range 10 default-offset 0
  #
  bridge-domain 10
   l2 binding vsi e1
   evpn binding vpn-instance evrf1
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
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #
   l2vpn-ad-family
    policy vpn-target
    signaling vpls
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
  #
  ospf 1
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  evpn source-address 3.3.3.3
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```