Example for Configuring Interworking Between VXLAN EVPN and traditional VPLS
============================================================================

This section provides an example for configuring interworking between EVPN VXLAN and traditional VPLS to implement interconnection between a DC and an enterprise.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370624__fig_dc_vrp_mpls-l3vpn-v4_cfg_011201), PE3 and the TOR switch are dual-homed to PE1 and PE2. An MPLS L2VPN with PWs is deployed between the PEs. An EVPN VXLAN is deployed in the DC, and PE1 and PE2 are the DC's egress devices.

**Figure 1** Configuring interworking between EVPN VXLAN and traditional VPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 0 through 2 in this example represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


  
![](images/fig_vxlan_vpls_03.png)  

**Table 1** Device interfaces and their IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| PE1 | GigabitEthernet 0/1/1 | 10.1.1.1/24 |
| GigabitEthernet 0/1/2 | 192.168.14.1/24 |
| Loopback 0 | 1.1.1.1/32 |
| Loopback 100 | 1.1.1.100/32 |
| PE2 | GigabitEthernet 0/1/1 | 10.2.1.2/24 |
| GigabitEthernet 0/1/2 | 192.168.24.1/24 |
| Loopback 0 | 2.2.2.2/32 |
| Loopback 100 | 2.2.2.100/32 |
| PE3 | GigabitEthernet 0/1/0 | - |
| GigabitEthernet 0/1/1 | 10.1.1.3/24 |
| GigabitEthernet 0/1/2 | 10.2.1.3/24 |
| Loopback 0 | 3.3.3.3/32 |
| TOR | 10GE 0/1/0 | - |
| 10GE 0/1/1 | 192.168.14.4/24 |
| 10GE 0/1/2 | 192.168.24.4/24 |
| Loopback 100 | 4.4.4.100/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP routing protocol on devices to ensure Layer 2 network connectivity.
2. Configure basic MPLS functions and MPLS LDP on PE1, PE2, and PE3. Establish LDP LSPs between PE3 and PE1 and between PE3 and PE2.
3. Configure EVPN instances on PE1, PE2, and the TOR switch.
4. Configure MPLS VPLS connections between PE3 and PE1 and between PE3 and PE2.
5. Configure VXLAN between the TOR switch and PE1 and between the TOR and PE2 for interconnection.
6. Create an EVPN instance and a VSI and bind them to the same BD on each of PE1 and PE2 to implement VXLAN and VPLS interworking.

#### Data Preparation

To complete the configuration, you need the following data:

* Interfaces and their IP addresses
* MPLS LSR IDs of PEs
* Names, RDs, and VPN targets of the EVPN instances of PE1, PE2, and the TOR switch
* Names and IDs of the VSIs on the PEs
* IP addresses of peers and tunnel policies used for setting up peer relationships

#### Procedure

1. Configure interfaces addresses and an IGP on the PE and TOR switch. OSPF is used in this example.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370624__file_01).
2. Configure basic MPLS functions and MPLS LDP on PE1, PE2, and PE3. Establish LDP LSPs between PE3 and PE1 and between PE3 and PE2.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370624__file_01).
3. Configure EVPN instances on PE1, PE2, and the TOR switch.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance tor bd-mode
   ```
   ```
   [*PE1-evpn-instance-tor] route-distinguisher 1.1.1.100:10
   ```
   ```
   [*PE1-evpn-instance-tor] vpn-target 10:10 export-extcommunity
   ```
   ```
   [*PE1-evpn-instance-tor] vpn-target 10:10 import-extcommunity
   ```
   ```
   [*PE1-evpn-instance-tor] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configurations of the TOR switch and PE2 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370624__file_01).
4. Configure a BGP EVPN peer relationship between the TOR switch and each of PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 4.4.4.100 as-number 65001
   ```
   ```
   [*PE1-bgp] peer 4.4.4.100 ebgp-max-hop 255
   ```
   ```
   [*PE1-bgp] peer 4.4.4.100 connect-interface LoopBack100
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] policy vpn-target
   ```
   ```
   [*PE1-bgp-af-evpn] peer 4.4.4.100 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 4.4.4.100 advertise encap-type vxlan
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
   
   The configurations of the TOR switch and PE2 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370624__file_01).
5. Configure a VSI on each of PE1, PE2, and PE3.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] vsi cpe bd-mode
   ```
   ```
   [*PE1-vsi-cpe] pwsignal ldp
   ```
   ```
   [*PE1-vsi-cpe-ldp] vsi-id 10
   ```
   ```
   [*PE1-vsi-cpe-ldp] peer 3.3.3.3
   ```
   ```
   [*PE1-vsi-cpe-ldp] quit
   ```
   ```
   [*PE1-vsi-cpe] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] vsi cpe bd-mode
   ```
   ```
   [*PE2-vsi-cpe] pwsignal ldp
   ```
   ```
   [*PE2-vsi-cpe-ldp] vsi-id 10
   ```
   ```
   [*PE2-vsi-cpe-ldp] peer 3.3.3.3
   ```
   ```
   [*PE2-vsi-cpe-ldp] quit
   ```
   ```
   [*PE2-vsi-cpe] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] vsi cpe bd-mode
   ```
   ```
   [*PE3-vsi-cpe] pw-redundancy mac-withdraw rfc-compatible
   ```
   ```
   [*PE3-vsi-cpe] pwsignal ldp
   ```
   ```
   [*PE3-vsi-cpe-ldp] vsi-id 10
   ```
   ```
   [*PE3-vsi-cpe-ldp] peer 1.1.1.1
   ```
   ```
   [*PE3-vsi-cpe-ldp] peer 2.2.2.2
   ```
   ```
   [*PE3-vsi-cpe-ldp] protect-group 10
   ```
   ```
   [*PE3-vsi-cpe-ldp-protect-group-10] protect-mode pw-redundancy master
   ```
   ```
   [*PE3-vsi-cpe-ldp-protect-group-10] reroute delay 60
   ```
   ```
   [*PE3-vsi-cpe-ldp-protect-group-10] peer 1.1.1.1 preference 1
   ```
   ```
   [*PE3-vsi-cpe-ldp-protect-group-10] peer 2.2.2.2 preference 2
   ```
   ```
   [*PE3-vsi-cpe-ldp-protect-group-10] quit
   ```
   ```
   [*PE3-vsi-cpe-ldp] quit
   ```
   ```
   [*PE3-vsi-cpe] quit
   ```
   ```
   [*PE3] commit
   ```
6. Bind the VSI and EVPN instance to the same BD on each of PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] vxlan vni 10 split-horizon-mode
   ```
   ```
   [*PE1-bd10] evpn binding vpn-instance tor
   ```
   ```
   [*PE1-bd10] l2 binding vsi cpe
   ```
   ```
   [*PE1-bd10] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration of PE2 is similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370624__file_01).
7. Verify the configuration.
   
   
   
   Run the **display vsi name cpe verbose** command on each PE. The command output shows that the PW and VSI are up. The following example uses the command output on PE1.
   
   ```
   [~PE1] display vsi name cpe verbose
   ```
   ```
    ***VSI Name               : cpe
       Work Mode              : bd-mode
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 1
       PW Signaling           : ldp
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
       Multicast Fast Switch  : disable
       Create Time            : 0 days, 3 hours, 24 minutes, 44 seconds
       VSI State              : up
       Resource Status        : --
                   
       VSI ID                 : 10
      *Peer Router ID         : 3.3.3.3
       Negotiation-vc-id      : 10
       Encapsulation Type     : vlan
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 48123
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004c4b44 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       CKey                   : 1
       NKey                   : 16777348
       Stp Enable             : 0
       PwIndex                : 1
       Control Word           : disable
       BFD for PW             : unavailable
    
       Access Bridge-domain   : Bridge-domain 10 
       Vac State              : down 
       Last Up Time           : 0000/00/00 00:00:00
       Total Up Time          : 0 days, 0 hours, 0 minutes, 0 seconds
   
     **PW Information:
   
      *Peer Ip Address        : 3.3.3.3
       PW State               : up
       Local VC Label         : 48123
       Remote VC Label        : 48124
       Remote Control Word    : disable
       PW Type                : label
       Local  VCCV            : alert lsp-ping bfd 
       Remote VCCV            : alert lsp-ping bfd 
       Tunnel ID              : 0x0000000001004c4b44 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 1
       Nkey                   : 16777348
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : --
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       PW Last Up Time        : 2018/08/29 08:11:47
       PW Total Up Time       : 0 days, 1 hours, 46 minutes, 33 seconds
   ```
   
   Run the **display vxlan tunnel** command on each PE. The command output shows that the VXLAN tunnel is Up. The following example uses the command output on PE1.
   
   ```
   [~PE1] display vxlan tunnel
   ```
   ```
   Number of vxlan tunnel : 1
   Tunnel ID   Source                Destination           State  Type     Uptime
   -----------------------------------------------------------------------------------
   4026531841  1.1.1.100             4.4.4.100             up    dynamic  00:18:05
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance tor bd-mode
   route-distinguisher 1.1.1.100:10
   vpn-target 10:10 export-extcommunity
   vpn-target 10:10 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi cpe bd-mode 
   pwsignal ldp
    vsi-id 10
    peer 3.3.3.3 
  #
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance tor
   l2 binding vsi cpe
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.14.1 255.255.255.0
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  interface LoopBack100
   ip address 1.1.1.100 255.255.255.255
  #
  interface Nve1
   source 1.1.1.100
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100
   peer 4.4.4.100 as-number 65001
   peer 4.4.4.100 ebgp-max-hop 255
   peer 4.4.4.100 connect-interface LoopBack100
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.100 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 4.4.4.100 enable
    peer 4.4.4.100 advertise encap-type vxlan
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  ospf 100
   area 0.0.0.1
    network 1.1.1.100 0.0.0.0
    network 192.168.14.0 0.0.0.255
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
  evpn vpn-instance tor bd-mode
   route-distinguisher 2.2.2.100:10
   vpn-target 10:10 export-extcommunity
   vpn-target 10:10 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi cpe bd-mode 
   pwsignal ldp
    vsi-id 10
    peer 3.3.3.3 
  #
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance tor
   l2 binding vsi cpe
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.24.1 255.255.255.0
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  interface LoopBack100
   ip address 2.2.2.100 255.255.255.255
  #
  interface Nve1
   source 2.2.2.100
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100
   peer 4.4.4.100 as-number 65001
   peer 4.4.4.100 ebgp-max-hop 255
   peer 4.4.4.100 connect-interface LoopBack100
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.100 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 4.4.4.100 enable
    peer 4.4.4.100 advertise encap-type vxlan
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.2.1.0 0.0.0.255
  #
  ospf 100
   area 0.0.0.1
    network 2.2.2.100 0.0.0.0
    network 192.168.24.0 0.0.0.255
  #
  evpn source-address 2.2.2.2
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  vsi cpe bd-mode
   pw-redundancy mac-withdraw rfc-compatible
   pwsignal ldp
    vsi-id 10
    peer 1.1.1.1 
    peer 2.2.2.2  
    protect-group 10 
     protect-mode pw-redundancy master
     reroute delay 60
     peer 1.1.1.1 preference 1
     peer 2.2.2.2 preference 2
  #
  bridge-domain 10
   l2 binding vsi cpe
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
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.3 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.2.1.3 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
  #
  return
  ```
* TOR configuration file
  
  ```
  #
  sysname TOR
  #
  evpn vpn-instance tor bd-mode
   route-distinguisher 4.4.4.100:10
   vpn-target 10:10 export-extcommunity
   vpn-target 10:10 import-extcommunity
  #
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance tor
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.14.4 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown  
   ip address 192.168.24.4 255.255.255.0
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  interface LoopBack100
   ip address 4.4.4.100 255.255.255.255
  #
  interface Nve1
   source 4.4.4.100
   vni 10 head-end peer-list protocol bgp
  #
  interface NULL0
  #
  bgp 65001
   peer 1.1.1.100 as-number 100
   peer 1.1.1.100 ebgp-max-hop 255
   peer 1.1.1.100 connect-interface LoopBack100
   peer 2.2.2.100 as-number 100
   peer 2.2.2.100 ebgp-max-hop 255
   peer 2.2.2.100 connect-interface LoopBack100
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.100 enable
    peer 2.2.2.100 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.100 enable
    peer 1.1.1.100 advertise encap-type vxlan
    peer 2.2.2.100 enable
    peer 2.2.2.100 advertise encap-type vxlan
  #
  ospf 100
   area 0.0.0.1
    network 4.4.4.100 0.0.0.0
    network 192.168.14.0 0.0.0.255
    network 192.168.24.0 0.0.0.255
  #
  evpn source-address 4.4.4.4
  #
  return
  ```