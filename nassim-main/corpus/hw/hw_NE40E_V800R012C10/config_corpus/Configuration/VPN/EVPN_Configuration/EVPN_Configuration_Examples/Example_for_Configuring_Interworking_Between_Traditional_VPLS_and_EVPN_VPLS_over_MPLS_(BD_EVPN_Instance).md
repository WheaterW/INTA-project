Example for Configuring Interworking Between Traditional VPLS and EVPN VPLS over MPLS (BD EVPN Instance)
========================================================================================================

The aggregation layer of a network still uses traditional VPLS, whereas the core network has evolved to EVPN. To allow communication between different layers, interworking between traditional VPLS and EVPN VPLS over MPLS (BD EVPN instance) must be configured.

#### Networking Requirements

On the network shown in the following figure, a VPLS network is deployed between the CSG and ASGs, and an EVPN is deployed between the RSG and ASGs. Access-side PW interfaces for EVPN can be configured on ASGs to implement interworking between VPLS and EVPN VPLS over MPLS (BD EVPN instance).

**Figure 1** Configuring interworking between traditional VPLS and EVPN VPLS over MPLS (BD EVPN instance)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](figure/en-us_image_0000001179409856.png)  

**Table 1** Device interfaces and their IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| CSG | GigabitEthernet 0/1/1 | 10.1.2.1/24 |
| GigabitEthernet 0/1/2 | 10.1.3.1/24 |
| GigabitEthernet 0/1/3 | - |
| Loopback 1 | 1.1.1.1/32 |
| ASG1 | GigabitEthernet 0/1/1 | 10.1.2.2/24 |
| GigabitEthernet 0/1/2 | 10.2.3.1/24 |
| GigabitEthernet 0/1/3 | 10.2.4.1/24 |
| Loopback 1 | 2.2.2.2/32 |
| ASG2 | GigabitEthernet 0/1/1 | 10.1.3.2/24 |
| GigabitEthernet 0/1/2 | 10.2.3.2/24 |
| GigabitEthernet 0/1/3 | 10.3.4.1/24 |
| Loopback 1 | 3.3.3.3/32 |
| RSG | GigabitEthernet 0/1/0 | 10.2.4.2/24 |
| GigabitEthernet 0/1/1 | 10.3.4.2/24 |
| GigabitEthernet 0/1/3 | - |
| Loopback 1 | 4.4.4.4/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on each device. Because the VPLS network (between the CSG and ASGs) and EVPN (between the RSG and ASGs) reside at different layers, use different IGP processes to implement route communication.
2. Configure basic MPLS LDP functions on the CSG, RSG, and ASGs.
3. Configure the EVPN function on the RSG and ASGs.
4. Configure PW connections between the CSG and ASGs.
5. Configure BFD for PW on CSGs and ASGs.
6. Configure an interface monitoring group on ASG1 to detect network-side interface status changes in a timely manner.

#### Data Preparation

To complete the configuration, you need the following data:

* Interfaces and IP addresses of devices
* MPLS LSR IDs of devices
* Names, RDs, and VPN targets of the EVPN instances created on the RSG and ASGs

#### Procedure

1. Configure an IGP on each device. Because the VPLS network (between the CSG and ASGs) and EVPN (between the RSG and ASGs) reside at different layers, use different IGP processes to implement route communication.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370643__file_01).
2. Configure basic MPLS LDP functions on the CSG, RSG, and ASGs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370643__file_01).
3. Configure the EVPN function on the RSG and ASGs.
   
   
   
   # Configure ASG1.
   
   ```
   [~ASG1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*ASG1-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*ASG1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*ASG1-evpn-instance-evrf1] quit
   ```
   ```
   [*ASG1] evpn source-address 2.2.2.2
   ```
   ```
   [*ASG1] bgp 100
   ```
   ```
   [*ASG1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*ASG1-bgp] peer 3.3.3.3 connect-interface LoopBack 1
   ```
   ```
   [*ASG1-bgp] peer 4.4.4.4 as-number 100
   ```
   ```
   [*ASG1-bgp] peer 4.4.4.4 connect-interface LoopBack 1
   ```
   ```
   [*ASG1-bgp] l2vpn-family evpn
   ```
   ```
   [*ASG1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*ASG1-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*ASG1-bgp-af-evpn] quit
   ```
   ```
   [*ASG1-bgp] quit
   ```
   ```
   [*ASG1] bridge-domain 10
   ```
   ```
   [*ASG1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*ASG1-bd10] quit
   ```
   ```
   [*ASG1] commit
   ```
   
   The configuration of ASG2 is similar to that of ASG1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370643__file_01).
   
   # Configure the RSG.
   
   ```
   [~RSG] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*RSG-evpn-instance-evrf1] route-distinguisher 100:3
   ```
   ```
   [*RSG-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*RSG-evpn-instance-evrf1] quit
   ```
   ```
   [*RSG] evpn source-address 4.4.4.4
   ```
   ```
   [*RSG] bgp 100
   ```
   ```
   [*RSG-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*RSG-bgp] peer 2.2.2.2 connect-interface LoopBack 1
   ```
   ```
   [*RSG-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*RSG-bgp] peer 3.3.3.3 connect-interface LoopBack 1
   ```
   ```
   [*RSG-bgp] l2vpn-family evpn
   ```
   ```
   [*RSG-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*RSG-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*RSG-bgp-af-evpn] quit
   ```
   ```
   [*RSG-bgp] quit
   ```
   ```
   [*RSG] bridge-domain 10
   ```
   ```
   [*RSG-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*RSG-bd10] quit
   ```
   ```
   [*RSG] interface GigabitEthernet 0/1/3.1 mode l2
   ```
   ```
   [*RSG-GigabitEthernet0/1/3.1] encapsulation dot1q vid 100
   ```
   ```
   [*RSG-GigabitEthernet0/1/3.1] bridge-domain 10
   ```
   ```
   [*RSG-GigabitEthernet0/1/3.1] quit
   ```
   ```
   [*RSG] commit
   ```
4. Configure PW connections between the CSG and ASGs.
   
   
   
   # Configure the CSG.
   
   ```
   [~CSG] mpls l2vpn 
   ```
   ```
   [*CSG-l2vpn] quit
   ```
   ```
   [*CSG] vsi vsi1 bd-mode
   ```
   ```
   [*CSG-vsi-vsi1] pwsignal ldp
   ```
   ```
   [*CSG-vsi-vsi1-ldp] vsi-id 1
   ```
   ```
   [*CSG-vsi-vsi1-ldp] peer 2.2.2.2
   ```
   ```
   [*CSG-vsi-vsi1-ldp] peer 3.3.3.3
   ```
   ```
   [*CSG-vsi-vsi1-ldp] protect-group vsi1
   ```
   ```
   [*CSG-vsi-vsi1-ldp-protect-group-vsi1] protect-mode pw-redundancy master
   ```
   ```
   [*CSG-vsi-vsi1-ldp-protect-group-vsi1] peer 2.2.2.2 preference 1
   ```
   ```
   [*CSG-vsi-vsi1-ldp-protect-group-vsi1] peer 3.3.3.3 preference 2
   ```
   ```
   [*CSG-vsi-vsi1-ldp-protect-group-vsi1] quit
   ```
   ```
   [*CSG-vsi-vsi1-ldp] quit
   ```
   ```
   [*CSG-vsi-vsi1] quit
   ```
   ```
   [*CSG] bridge-domain 10
   ```
   ```
   [*CSG-bd10] l2 binding vsi vsi1
   ```
   ```
   [*CSG-bd10] quit
   ```
   ```
   [*CSG] interface GigabitEthernet 0/1/3.1 mode l2
   ```
   ```
   [*CSG-GigabitEthernet0/1/3.1] encapsulation dot1q vid 100
   ```
   ```
   [*CSG-GigabitEthernet0/1/3.1] bridge-domain 10
   ```
   ```
   [*CSG-GigabitEthernet0/1/3.1] quit
   ```
   ```
   [*CSG] commit
   ```
   
   # Configure ASG1.
   
   ```
   [~ASG1] mpls l2vpn
   ```
   ```
   [*ASG1-l2vpn] quit
   ```
   ```
   [*ASG1] evpn
   ```
   ```
   [*ASG1-evpn] esi 0000.1111.1111.1111.1111
   ```
   ```
   [*ASG1-evpn-esi-0000.1111.1111.1111.1111] evpn redundancy-mode single-active
   ```
   ```
   [*ASG1-evpn-esi-0000.1111.1111.1111.1111] quit
   ```
   ```
   [*ASG1-evpn] quit
   ```
   ```
   [*ASG1] vsi vsi1 bd-mode
   ```
   ```
   [*ASG1-vsi-vsi1] pwsignal ldp
   ```
   ```
   [*ASG1-vsi-vsi1-ldp] vsi-id 1
   ```
   ```
   [*ASG1-vsi-vsi1-ldp] peer 1.1.1.1 upe
   ```
   ```
   [*ASG1-vsi-vsi1-ldp] peer 1.1.1.1 pw pw1
   ```
   ```
   [*ASG1-vsi-vsi1-ldp-pw-pw1] esi 0000.1111.1111.1111.1111
   ```
   ```
   [*ASG1-vsi-vsi1-ldp-pw-pw1] quit
   ```
   ```
   [*ASG1-vsi-vsi1-ldp] quit
   ```
   ```
   [*ASG1-vsi-vsi1] quit
   ```
   ```
   [*ASG1] bridge-domain 10
   ```
   ```
   [*ASG1-bd10] l2 binding vsi vsi1
   ```
   ```
   [*ASG1-bd10] quit
   ```
   ```
   [*ASG1] commit
   ```
   
   # Configure ASG2.
   
   ```
   [~ASG2] mpls l2vpn
   ```
   ```
   [*ASG2-l2vpn] quit
   ```
   ```
   [*ASG2] evpn
   ```
   ```
   [*ASG2-evpn] esi 0000.1111.1111.1111.1111
   ```
   ```
   [*ASG2-evpn-esi-0000.1111.1111.1111.1111] evpn redundancy-mode single-active
   ```
   ```
   [*ASG2-evpn-esi-0000.1111.1111.1111.1111] quit
   ```
   ```
   [*ASG2-evpn] quit
   ```
   ```
   [*ASG2] vsi vsi1 bd-mode
   ```
   ```
   [*ASG2-vsi-vsi1] pwsignal ldp
   ```
   ```
   [*ASG2-vsi-vsi1-ldp] vsi-id 1
   ```
   ```
   [*ASG2-vsi-vsi1-ldp] peer 1.1.1.1 upe
   ```
   ```
   [*ASG2-vsi-vsi1-ldp] peer 1.1.1.1 pw pw1
   ```
   ```
   [*ASG2-vsi-vsi1-ldp-pw-pw1] esi 0000.1111.1111.1111.1111
   ```
   ```
   [*ASG2-vsi-vsi1-ldp-pw-pw1] quit
   ```
   ```
   [*ASG2-vsi-vsi1-ldp] quit
   ```
   ```
   [*ASG2-vsi-vsi1] quit
   ```
   ```
   [*ASG2] bridge-domain 10
   ```
   ```
   [*ASG2-bd10] l2 binding vsi vsi1
   ```
   ```
   [*ASG2-bd10] quit
   ```
   ```
   [*ASG2] commit
   ```
5. Configure BFD for PW on CSGs and ASGs.
   
   
   
   # Configure the CSG.
   
   ```
   [~CSG] bfd 
   [*CSG-bfd] quit
   [*CSG] bfd 1 bind pw vsi vsi1 peer 2.2.2.2
   [*CSG-bfd-lsp-session-1] discriminator local 1
   [*CSG-bfd-lsp-session-1] discriminator remote 1
   [*CSG-bfd-lsp-session-1] min-tx-interval 10
   [*CSG-bfd-lsp-session-1] min-rx-interval 10
   [*CSG-bfd-lsp-session-1] quit
   [*CSG] bfd 2 bind pw vsi vsi1 peer 3.3.3.3
   [*CSG-bfd-lsp-session-2] discriminator local 2
   [*CSG-bfd-lsp-session-2] discriminator remote 2
   [*CSG-bfd-lsp-session-2] min-tx-interval 10
   [*CSG-bfd-lsp-session-2] min-rx-interval 10
   [*CSG-bfd-lsp-session-2] quit
   [*CSG] commit
   ```
   
   # Configure ASG1.
   
   ```
   [~ASG1] bfd
   [*ASG1-bfd] quit
   [*ASG1] bfd 1 bind pw vsi vsi1 peer 1.1.1.1
   [*ASG1-bfd-lsp-session-1] discriminator local 1
   [*ASG1-bfd-lsp-session-1] discriminator remote 1
   [*ASG1-bfd-lsp-session-1] min-tx-interval 10
   [*ASG1-bfd-lsp-session-1] min-rx-interval 10
   [*ASG1-bfd-lsp-session-1] quit
   [*ASG1] commit
   ```
   
   # Configure ASG2.
   
   ```
   [~ASG2] bfd
   [*ASG2-bfd] quit
   [*ASG2] bfd 2 bind pw vsi vsi1 peer 1.1.1.1
   [*ASG2-bfd-lsp-session-2] discriminator local 2
   [*ASG2-bfd-lsp-session-2] discriminator remote 2
   [*ASG2-bfd-lsp-session-2] min-tx-interval 10
   [*ASG2-bfd-lsp-session-2] min-rx-interval 10
   [*ASG2-bfd-lsp-session-2] quit
   [*ASG2] commit
   ```
6. Configure an interface monitoring group on ASG1.
   
   
   
   # Configure ASG1.
   
   ```
   [~ASG1] monitor-group 1
   [*ASG1-monitor-group-1] monitor enable
   [*ASG1-monitor-group-1] binding interface GigabitEthernet 0/1/2 down-weight 10
   [*ASG1-monitor-group-1] binding interface GigabitEthernet 0/1/3 down-weight 10
   [*ASG1-monitor-group-1] quit
   [*ASG1] interface GigabitEthernet 0/1/1
   [*ASG1-GigabitEthernet 0/1/1] track monitor-group 1
   [*ASG1-GigabitEthernet 0/1/1] quit
   [*ASG1] commit
   ```
7. Verify the configuration.
   
   
   
   Run the **display vsi name vsi1 verbose** command on ASG1. The command output shows that both the VSI and PW are in the up state.
   
   ```
   [~ASG1] display vsi name vsi1 verbose
   ```
   ```
    ***VSI Name               : vsi1
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
       Create Time            : 0 days, 14 hours, 3 minutes, 23 seconds
       VSI State              : up
       Resource Status        : --
                   
       VSI ID                 : 1
      *Peer Router ID         : 1.1.1.1
       Negotiation-vc-id      : 1
       Encapsulation Type     : vlan
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 48123
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004c4b42 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       CKey                   : 1
       NKey                   : 16777393
       Stp Enable             : 0
       PwIndex                : 1
       Control Word           : disable
       BFD for PW             : available
    
       Access Bridge-domain   : Bridge-domain 10 
       Vac State              : down 
       Last Up Time           : 0000/00/00 00:00:00
       Total Up Time          : 0 days, 0 hours, 0 minutes, 0 seconds
   
     **PW Information:
   
      *Peer Ip Address        : 1.1.1.1
       PW State               : up
       Local VC Label         : 48123
       Remote VC Label        : 48122
       Remote Control Word    : disable
       PW Type                : MEHVPLS
       Local  VCCV            : alert lsp-ping bfd 
       Remote VCCV            : alert lsp-ping bfd 
       Tunnel ID              : 0x0000000001004c4b42 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 1
       Nkey                   : 16777393
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : --
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       Monitor Group Name     : 1
       PW Last Up Time        : 2019/01/03 12:22:30
       PW Total Up Time       : 0 days, 13 hours, 50 minutes, 43 seconds
   ```
   
   Run the **display bgp evpn all routing-table** command on ASG1 to check EVPN routes. The command output shows the MAC routes on the VPLS-side interface and the ES routes and per-ES Ethernet A-D routes corresponding to the ESI of the PW.
   
   ```
   [~ASG1] display bgp evpn all routing-table
   ```
   ```
    Local AS number : 100
   
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
    
    EVPN address family:
    Number of A-D Routes: 4
    Route Distinguisher: 100:1
          Network(ESI/EthTagId)                                  NextHop
    *>    0000.1111.1111.1111.1111:0                             127.0.0.1
    Route Distinguisher: 100:2
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.1111.1111.1111:0                             3.3.3.3
    Route Distinguisher: 2.2.2.2:0
          Network(ESI/EthTagId)                                  NextHop
    *>    0000.1111.1111.1111.1111:4294967295                    127.0.0.1
    Route Distinguisher: 3.3.3.3:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.1111.1111.1111:4294967295                    3.3.3.3
       
   
    EVPN-Instance evrf1:
    Number of A-D Routes: 3
          Network(ESI/EthTagId)                                  NextHop
    *>    0000.1111.1111.1111.1111:0                             127.0.0.1
    * i                                                          3.3.3.3
    *>i   0000.1111.1111.1111.1111:4294967295                    3.3.3.3
    
    EVPN address family:
    Number of Mac Routes: 1
    Route Distinguisher: 100:1
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>    0:48:00e0-fc12-3456:0:0.0.0.0                          0.0.0.0
       
   
    EVPN-Instance evrf1:
    Number of Mac Routes: 1
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>    0:48:00e0-fc12-3456:0:0.0.0.0                          0.0.0.0
    
    EVPN address family:
    Number of Inclusive Multicast Routes: 3
    Route Distinguisher: 100:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:2.2.2.2                                           127.0.0.1
    Route Distinguisher: 100:2
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:3.3.3.3                                           3.3.3.3
    Route Distinguisher: 100:3
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:4.4.4.4                                           4.4.4.4
       
   
    EVPN-Instance evrf1:
    Number of Inclusive Multicast Routes: 3
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:2.2.2.2                                           127.0.0.1
    *>i   0:32:3.3.3.3                                           3.3.3.3
    *>i   0:32:4.4.4.4                                           4.4.4.4
    
    EVPN address family:
    Number of ES Routes: 2
    Route Distinguisher: 2.2.2.2:0
          Network(ESI)                                           NextHop
    *>    0000.1111.1111.1111.1111                               127.0.0.1
    Route Distinguisher: 3.3.3.3:0
          Network(ESI)                                           NextHop
    *>i   0000.1111.1111.1111.1111                               3.3.3.3
       
   
    EVPN-Instance evrf1:
    Number of ES Routes: 2
          Network(ESI)                                           NextHop
    *>    0000.1111.1111.1111.1111                               127.0.0.1
    * i                                                          3.3.3.3
   ```
   
   The route details include information about the associated PW. The following uses MAC routes as an example.
   
   ```
   [~ASG1] display bgp evpn all routing-table mac-route 0:48:00e0-fc12-3456:0:0.0.0.0
   ```
   ```
    BGP local router ID : 2.2.2.2
    Local AS number : 100
    Total routes of Route Distinguisher(100:1): 1
    BGP routing table entry information of 0:48:00e0-fc12-3456:0:0.0.0.0:
    Imported route.
    From: 0.0.0.0 (0.0.0.0) 
    Route Duration: 0d13h48m24s
    Original nexthop: 0.0.0.0
    Qos information : 0x0
    Ext-Community: RT <1 : 1>, SoO <2.2.2.2 : 0>
    AS-path Nil, origin incomplete, pref-val 0, valid, local, best, select, pre 255
    Route Type: 2 (MAC Advertisement Route)
    Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc12-3456/48, IP Address/Len: 0.0.0.0/0, ESI:0000.1111.1111.1111.1111
    Advertised to such 2 peers:
       3.3.3.3
       4.4.4.4
   
       
   
    EVPN-Instance evrf1:
    Number of Mac Routes: 1
    BGP routing table entry information of 0:48:00e0-fc12-3456:0:0.0.0.0:
    Route Distinguisher: 100:1
    Imported route.
    From: 0.0.0.0 (0.0.0.0) 
    Route Duration: 0d13h48m26s
    Direct Out-interface: PW<peerip:1.1.1.1 vcid:1 vctype:vlan>
    Original nexthop: 0.0.0.0
    Qos information : 0x0
    AS-path Nil, origin incomplete, pref-val 0, valid, local, best, select, pre 255
    Route Type: 2 (MAC Advertisement Route)
    Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc12-3456/48, IP Address/Len: 0.0.0.0/0, ESI:0000.1111.1111.1111.1111
    Not advertised to any peer yet
   ```

#### Configuration Files

* CSG configuration file
  ```
  #
  sysname CSG
  #
  bfd
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1 bd-mode
   pwsignal ldp
    vsi-id 1      
    peer 2.2.2.2 
    peer 3.3.3.3 
    protect-group vsi1 
     protect-mode pw-redundancy master
     peer 2.2.2.2 preference 1
     peer 3.3.3.3 preference 2
  #
  bridge-domain 10
   l2 binding vsi vsi1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
  #
  interface GigabitEthernet0/1/3.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 100
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  bfd 1 bind pw vsi vsi1 peer 2.2.2.2
   discriminator local 1
   discriminator remote 1
   min-tx-interval 10
   min-rx-interval 10
  #
  bfd 2 bind pw vsi vsi1 peer 3.3.3.3
   discriminator local 2
   discriminator remote 2
   min-tx-interval 10
   min-rx-interval 10
  #
  return
  ```
* ASG1 configuration file
  
  ```
  #
  sysname ASG1
  #
  evpn
   #
   mac-duplication
   #
   esi 0000.1111.1111.1111.1111
    evpn redundancy-mode single-active
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bfd
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1 bd-mode
   pwsignal ldp
    vsi-id 1
    peer 1.1.1.1 upe 
    peer 1.1.1.1 pw pw1
     esi 0000.1111.1111.1111.1111
  #
  bridge-domain 10
   l2 binding vsi vsi1
   evpn binding vpn-instance evrf1
  #
  mpls ldp
  #
  monitor-group 1
   monitor enable
   binding interface GigabitEthernet0/1/2 down-weight 10
   binding interface GigabitEthernet0/1/3 down-weight 10
  #
  isis 1          
   is-level level-1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   track monitor-group 1
   mpls
   mpls ldp
  #               
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.2.3.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.2.4.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1  
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
  #
  ospf 100
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.2.0 0.0.0.255
  #
  bfd 1 bind pw vsi vsi1 peer 1.1.1.1
   discriminator local 1
   discriminator remote 1
   min-tx-interval 10
   min-rx-interval 10
  #
  evpn source-address 2.2.2.2
  #
  return
  ```
* ASG2 configuration file
  
  ```
  #
  sysname ASG2
  #
  evpn
   #
   mac-duplication
   #
   esi 0000.1111.1111.1111.1111
    evpn redundancy-mode single-active
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:2
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bfd
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1 bd-mode
   pwsignal ldp
    vsi-id 1
    peer 1.1.1.1 upe 
    peer 1.1.1.1 pw pw1
     esi 0000.1111.1111.1111.1111
  #
  bridge-domain 10
   l2 binding vsi vsi1
   evpn binding vpn-instance evrf1
  #
  mpls ldp
  #
  isis 1          
   is-level level-1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   mpls
   mpls ldp       
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.2.3.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.3.4.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
  #
  ospf 100
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.3.0 0.0.0.255
  #
  bfd 2 bind pw vsi vsi1 peer 1.1.1.1
   discriminator local 2
   discriminator remote 2
   min-tx-interval 10
   min-rx-interval 10
  #
  evpn source-address 3.3.3.3
  #
  return
  ```
* RSG configuration file
  
  ```
  #
  sysname RSG
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:3
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  mpls ldp
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.2.4.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp       
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.3.4.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  #
  evpn source-address 4.4.4.4
  #
  return
  ```