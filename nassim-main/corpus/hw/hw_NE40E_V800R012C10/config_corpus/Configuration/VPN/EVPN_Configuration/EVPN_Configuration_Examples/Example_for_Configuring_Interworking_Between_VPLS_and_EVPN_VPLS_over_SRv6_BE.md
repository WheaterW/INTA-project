Example for Configuring Interworking Between VPLS and EVPN VPLS over SRv6 BE
============================================================================

This section provides an example for configuring interworking between VPLS and EVPN VPLS over SRv6 BE when they are both deployed on a network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0307196816__fig_dc_vrp_evpn_cfg_011401), VPLS is deployed between the UPE and SPEs; EVPN VPLS over SRv6 BE is deployed between SPEs and the NPE. Interworking between VPLS and EVPN VPLS over SRv6 BE is implemented by binding a BD to a VSI and an EVPN instance on the SPE, thereby enabling all PWs in the VSI to access the EVPN through the BD.

**Figure 1** Configuring interworking between VPLS and EVPN VPLS over SRv6 BE![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](figure/en-us_image_0307196820.png "Click to enlarge")

**Table 1** Device interfaces and their IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| UPE | GigabitEthernet 0/1/1 | 10.1.2.1/24 |
| GigabitEthernet 0/1/2 | 10.1.3.1/24 |
| GigabitEthernet 0/1/3 | - |
| Loopback 1 | 1.1.1.1/32 |
| SPE1 | GigabitEthernet 0/1/1 | 10.1.2.2/24 |
| GigabitEthernet 0/1/2 | 10.2.3.1/24 |
| 2001:DB8:10::1/64 |
| GigabitEthernet 0/1/3 | 2001:DB8:20::1/64 |
| Loopback 1 | 2.2.2.2/32 |
| 2001:DB8:2::2/64 |
| SPE2 | GigabitEthernet 0/1/1 | 10.1.3.2/24 |
| GigabitEthernet 0/1/2 | 10.2.3.2/24 |
| 2001:DB8:10::2/64 |
| GigabitEthernet 0/1/3 | 2001:DB8:30::1/64 |
| Loopback 1 | 3.3.3.3/32 |
| 2001:DB8:3::3/64 |
| NPE | GigabitEthernet 0/1/0 | 2001:DB8:20::2/64 |
| GigabitEthernet 0/1/1 | 2001:DB8:30::2/64 |
| GigabitEthernet 0/1/3 | - |
| Loopback 1 | 4.4.4.4/32 |
| 2001:DB8:4::4/64 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on each device. Configure OSPF between the UPE and SPEs (VPLS network) to implement IPv4 route interworking; configure IS-ISv6 on the SPEs and NPE (EVPN network) to implement IPv6 route interworking.
2. Configure basic MPLS LDP functions on the UPE and SPEs.
3. Configure BD EVPN on the SPEs and NPE.
4. Configure SRv6 BE between the SPEs and NPE.
5. Configure PWs between the UPE and SPEs.
6. Configure BFD for PW on the UPE and SPEs.
7. Configure an interface monitoring group on SPE1 so that SPE1 can detect network-side interface status changes immediately if the changes occur.

#### Data Preparation

To complete the configuration, you need the following data:

* Interfaces and IP addresses of devices
* MPLS LSR IDs of devices
* Names, RDs, and VPN targets of the EVPN instances created on the SPEs and NPE
* Locator names, Arguments field lengths, and dynamically generated opcodes on the SPEs and NPE

#### Procedure

1. Configure interface IP addresses according to [Figure 1](#EN-US_TASK_0307196816__fig_dc_vrp_evpn_cfg_011401). 
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0307196816__file_01).
2. Configure an IGP on each device.
   
   
   
   Configure OSPF between the UPE and SPEs (VPLS network) to implement IPv4 route interworking; configure IS-ISv6 on the SPEs and NPE (EVPN network) to implement IPv6 route interworking. For detailed configurations, see [Configuration Files](#EN-US_TASK_0307196816__file_01).
3. Configure basic MPLS LDP functions on the UPE and SPEs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0307196816__file_01).
4. Configure BD EVPN on the SPEs and NPE.
   
   
   
   # Configure SPE1.
   
   ```
   [~SPE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*SPE1-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*SPE1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*SPE1-evpn-instance-evrf1] quit
   ```
   ```
   [*SPE1] evpn source-address 2.2.2.2
   ```
   ```
   [*SPE1] bgp 100
   ```
   ```
   [*SPE1-bgp] router-id 2.2.2.2
   ```
   ```
   [*SPE1-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*SPE1-bgp] peer 2001:DB8:3::3 connect-interface LoopBack 1
   ```
   ```
   [*SPE1-bgp] peer 2001:DB8:4::4 as-number 100
   ```
   ```
   [*SPE1-bgp] peer 2001:DB8:4::4 connect-interface LoopBack 1
   ```
   ```
   [*SPE1-bgp] l2vpn-family evpn
   ```
   ```
   [*SPE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   ```
   ```
   [*SPE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   ```
   ```
   [*SPE1-bgp-af-evpn] peer 2001:DB8:4::4 enable
   ```
   ```
   [*SPE1-bgp-af-evpn] peer 2001:DB8:4::4 advertise encap-type srv6
   ```
   ```
   [*SPE1-bgp-af-evpn] quit
   ```
   ```
   [*SPE1-bgp] quit
   ```
   ```
   [*SPE1] bridge-domain 10
   ```
   ```
   [*SPE1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*SPE1-bd10] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   The configuration of SPE2 is similar to that of SPE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0307196816__file_01).
   
   # Configure the NPE.
   
   ```
   [~NPE] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*NPE-evpn-instance-evrf1] route-distinguisher 100:3
   ```
   ```
   [*NPE-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*NPE-evpn-instance-evrf1] quit
   ```
   ```
   [*NPE] evpn source-address 4.4.4.4
   ```
   ```
   [*NPE] bgp 100
   ```
   ```
   [*NPE-bgp] router-id 4.4.4.4
   ```
   ```
   [*NPE-bgp] peer 2001:DB8:2::2 as-number 100
   ```
   ```
   [*NPE-bgp] peer 2001:DB8:2::2 connect-interface LoopBack 1
   ```
   ```
   [*NPE-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*NPE-bgp] peer 2001:DB8:3::3 connect-interface LoopBack 1
   ```
   ```
   [*NPE-bgp] l2vpn-family evpn
   ```
   ```
   [*NPE-bgp-af-evpn] peer 2001:DB8:2::2 enable
   ```
   ```
   [*NPE-bgp-af-evpn] peer 2001:DB8:2::2 advertise encap-type srv6
   ```
   ```
   [*NPE-bgp-af-evpn] peer 2001:DB8:3::3 enable
   ```
   ```
   [*NPE-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   ```
   ```
   [*NPE-bgp-af-evpn] quit
   ```
   ```
   [*NPE-bgp] quit
   ```
   ```
   [*NPE] bridge-domain 10
   ```
   ```
   [*NPE-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*NPE-bd10] quit
   ```
   ```
   [*NPE] interface GigabitEthernet 0/1/3.1 mode l2
   ```
   ```
   [*NPE-GigabitEthernet0/1/3.1] encapsulation dot1q vid 100
   ```
   ```
   [*NPE-GigabitEthernet0/1/3.1] bridge-domain 10
   ```
   ```
   [*NPE-GigabitEthernet0/1/3.1] quit
   ```
   ```
   [*NPE] commit
   ```
5. Configure SRv6 BE between the SPEs and NPE.
   
   
   
   # Configure SPE1.
   
   ```
   [~SPE1] segment-routing ipv6
   [*SPE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*SPE1-segment-routing-ipv6] locator SPE1 ipv6-prefix 2001:DB8:11:: 64
   [*SPE1-segment-routing-ipv6-locator] quit
   [*SPE1-segment-routing-ipv6] locator SPE1_ARG ipv6-prefix 2001:DB8:12:: 64 args 10
   [*SPE1-segment-routing-ipv6-locator] quit
   [*SPE1-segment-routing-ipv6] quit
   [*SPE1] isis 1
   [*SPE1-isis-1] segment-routing ipv6 locator SPE1
   [*SPE1-isis-1] segment-routing ipv6 locator SPE1_ARG auto-sid-disable
   [*SPE1-isis-1] quit
   [*SPE1] evpn vpn-instance evrf1 bd-mode
   [*SPE1-evpn-instance-evrf1] segment-routing ipv6 locator SPE1_ARG unicast-locator SPE1
   [*SPE1-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*SPE1-evpn-instance-evrf1] quit
   [*SPE1] commit
   ```
   
   # Configure SPE2.
   
   ```
   [~SPE2] segment-routing ipv6
   [*SPE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*SPE2-segment-routing-ipv6] locator SPE2 ipv6-prefix 2001:DB8:21:: 64
   [*SPE2-segment-routing-ipv6-locator] quit
   [*SPE2-segment-routing-ipv6] locator SPE2_ARG ipv6-prefix 2001:DB8:22:: 64 args 10
   [*SPE2-segment-routing-ipv6-locator] quit
   [*SPE2-segment-routing-ipv6] quit
   [*SPE2] isis 1
   [*SPE2-isis-1] segment-routing ipv6 locator SPE2
   [*SPE2-isis-1] segment-routing ipv6 locator SPE2_ARG auto-sid-disable
   [*SPE2-isis-1] quit
   [*SPE2] evpn vpn-instance evrf1 bd-mode
   [*SPE2-evpn-instance-evrf1] segment-routing ipv6 locator SPE2_ARG unicast-locator SPE2
   [*SPE2-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*SPE2-evpn-instance-evrf1] quit
   [*SPE2] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] segment-routing ipv6
   [*NPE-segment-routing-ipv6] encapsulation source-address 2001:DB8:4::4
   [*NPE-segment-routing-ipv6] locator NPE ipv6-prefix 2001:DB8:31:: 64
   [*NPE-segment-routing-ipv6-locator] quit
   [*NPE-segment-routing-ipv6] locator NPE_ARG ipv6-prefix 2001:DB8:32:: 64 args 10
   [*NPE-segment-routing-ipv6-locator] quit
   [*NPE-segment-routing-ipv6] quit
   [*NPE] isis 1
   [*NPE-isis-1] segment-routing ipv6 locator NPE
   [*NPE-isis-1] segment-routing ipv6 locator NPE_ARG auto-sid-disable
   [*NPE-isis-1] quit
   [*NPE] evpn vpn-instance evrf1 bd-mode
   [*NPE-evpn-instance-evrf1] segment-routing ipv6 locator NPE_ARG unicast-locator NPE
   [*NPE-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*NPE-evpn-instance-evrf1] quit
   [*NPE] commit
   ```
6. Configure PWs between the UPE and SPEs.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] mpls l2vpn 
   ```
   ```
   [*UPE-l2vpn] quit
   ```
   ```
   [*UPE] vsi vsi1 bd-mode
   ```
   ```
   [*UPE-vsi-vsi1] pwsignal ldp
   ```
   ```
   [*UPE-vsi-vsi1-ldp] vsi-id 1
   ```
   ```
   [*UPE-vsi-vsi1-ldp] peer 2.2.2.2
   ```
   ```
   [*UPE-vsi-vsi1-ldp] peer 3.3.3.3
   ```
   ```
   [*UPE-vsi-vsi1-ldp] protect-group vsi1
   ```
   ```
   [*UPE-vsi-vsi1-ldp-protect-group-vsi1] protect-mode pw-redundancy master
   ```
   ```
   [*UPE-vsi-vsi1-ldp-protect-group-vsi1] peer 2.2.2.2 preference 1
   ```
   ```
   [*UPE-vsi-vsi1-ldp-protect-group-vsi1] peer 3.3.3.3 preference 2
   ```
   ```
   [*UPE-vsi-vsi1-ldp-protect-group-vsi1] quit
   ```
   ```
   [*UPE-vsi-vsi1-ldp] quit
   ```
   ```
   [*UPE-vsi-vsi1] quit
   ```
   ```
   [*UPE] bridge-domain 10
   ```
   ```
   [*UPE-bd10] l2 binding vsi vsi1
   ```
   ```
   [*UPE-bd10] quit
   ```
   ```
   [*UPE] interface GigabitEthernet 0/1/3.1 mode l2
   ```
   ```
   [*UPE-GigabitEthernet0/1/3.1] encapsulation dot1q vid 100
   ```
   ```
   [*UPE-GigabitEthernet0/1/3.1] bridge-domain 10
   ```
   ```
   [*UPE-GigabitEthernet0/1/3.1] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure SPE1.
   
   ```
   [~SPE1] mpls l2vpn
   ```
   ```
   [*SPE1-l2vpn] quit
   ```
   ```
   [*SPE1] evpn
   ```
   ```
   [*SPE1-evpn] esi 0000.1111.1111.1111.1111
   ```
   ```
   [*SPE1-evpn-esi-0000.1111.1111.1111.1111] evpn redundancy-mode single-active
   ```
   ```
   [*SPE1-evpn-esi-0000.1111.1111.1111.1111] quit
   ```
   ```
   [*SPE1-evpn] quit
   ```
   ```
   [*SPE1] vsi vsi1 bd-mode
   ```
   ```
   [*SPE1-vsi-vsi1] pwsignal ldp
   ```
   ```
   [*SPE1-vsi-vsi1-ldp] vsi-id 1
   ```
   ```
   [*SPE1-vsi-vsi1-ldp] peer 1.1.1.1 upe
   ```
   ```
   [*SPE1-vsi-vsi1-ldp] peer 1.1.1.1 pw pw1
   ```
   ```
   [*SPE1-vsi-vsi1-ldp-pw-pw1] esi 0000.1111.1111.1111.1111
   ```
   ```
   [*SPE1-vsi-vsi1-ldp-pw-pw1] quit
   ```
   ```
   [*SPE1-vsi-vsi1-ldp] quit
   ```
   ```
   [*SPE1-vsi-vsi1] quit
   ```
   ```
   [*SPE1] bridge-domain 10
   ```
   ```
   [*SPE1-bd10] l2 binding vsi vsi1
   ```
   ```
   [*SPE1-bd10] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   # Configure SPE2.
   
   ```
   [~SPE2] mpls l2vpn
   ```
   ```
   [*SPE2-l2vpn] quit
   ```
   ```
   [*SPE2] evpn
   ```
   ```
   [*SPE2-evpn] esi 0000.1111.1111.1111.1111
   ```
   ```
   [*SPE2-evpn-esi-0000.1111.1111.1111.1111] evpn redundancy-mode single-active
   ```
   ```
   [*SPE2-evpn-esi-0000.1111.1111.1111.1111] quit
   ```
   ```
   [*SPE2-evpn] quit
   ```
   ```
   [*SPE2] vsi vsi1 bd-mode
   ```
   ```
   [*SPE2-vsi-vsi1] pwsignal ldp
   ```
   ```
   [*SPE2-vsi-vsi1-ldp] vsi-id 1
   ```
   ```
   [*SPE2-vsi-vsi1-ldp] peer 1.1.1.1 upe
   ```
   ```
   [*SPE2-vsi-vsi1-ldp] peer 1.1.1.1 pw pw1
   ```
   ```
   [*SPE2-vsi-vsi1-ldp-pw-pw1] esi 0000.1111.1111.1111.1111
   ```
   ```
   [*SPE2-vsi-vsi1-ldp-pw-pw1] quit
   ```
   ```
   [*SPE2-vsi-vsi1-ldp] quit
   ```
   ```
   [*SPE2-vsi-vsi1] quit
   ```
   ```
   [*SPE2] bridge-domain 10
   ```
   ```
   [*SPE2-bd10] l2 binding vsi vsi1
   ```
   ```
   [*SPE2-bd10] quit
   ```
   ```
   [*SPE2] commit
   ```
7. Configure BFD for PW on the UPE and SPEs.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] bfd 
   [*UPE-bfd] quit
   [*UPE] bfd 1 bind pw vsi vsi1 peer 2.2.2.2
   [*UPE-bfd-lsp-session-1] discriminator local 1
   [*UPE-bfd-lsp-session-1] discriminator remote 1
   [*UPE-bfd-lsp-session-1] min-tx-interval 10
   [*UPE-bfd-lsp-session-1] min-rx-interval 10
   [*UPE-bfd-lsp-session-1] quit
   [*UPE] bfd 2 bind pw vsi vsi1 peer 3.3.3.3
   [*UPE-bfd-lsp-session-2] discriminator local 2
   [*UPE-bfd-lsp-session-2] discriminator remote 2
   [*UPE-bfd-lsp-session-2] min-tx-interval 10
   [*UPE-bfd-lsp-session-2] min-rx-interval 10
   [*UPE-bfd-lsp-session-2] quit
   [*UPE] commit
   ```
   
   # Configure SPE1.
   
   ```
   [~SPE1] bfd
   [*SPE1-bfd] quit
   [*SPE1] bfd 1 bind pw vsi vsi1 peer 1.1.1.1
   [*SPE1-bfd-lsp-session-1] discriminator local 1
   [*SPE1-bfd-lsp-session-1] discriminator remote 1
   [*SPE1-bfd-lsp-session-1] min-tx-interval 10
   [*SPE1-bfd-lsp-session-1] min-rx-interval 10
   [*SPE1-bfd-lsp-session-1] quit
   [*SPE1] commit
   ```
   
   # Configure SPE2.
   
   ```
   [~SPE2] bfd
   [*SPE2-bfd] quit
   [*SPE2] bfd 2 bind pw vsi vsi1 peer 1.1.1.1
   [*SPE2-bfd-lsp-session-2] discriminator local 2
   [*SPE2-bfd-lsp-session-2] discriminator remote 2
   [*SPE2-bfd-lsp-session-2] min-tx-interval 10
   [*SPE2-bfd-lsp-session-2] min-rx-interval 10
   [*SPE2-bfd-lsp-session-2] quit
   [*SPE2] commit
   ```
8. Configure an interface monitoring group on SPE1.
   
   
   
   # Configure SPE1.
   
   ```
   [~SPE1] monitor-group 1
   [*SPE1-monitor-group-1] monitor enable
   [*SPE1-monitor-group-1] binding interface GigabitEthernet 0/1/2 down-weight 10
   [*SPE1-monitor-group-1] binding interface GigabitEthernet 0/1/3 down-weight 10
   [*SPE1-monitor-group-1] quit
   [*SPE1] interface GigabitEthernet 0/1/1
   [*SPE1-GigabitEthernet 0/1/1] track monitor-group 1
   [*SPE1-GigabitEthernet 0/1/1] quit
   [*SPE1] commit
   ```
9. Verify the configuration.
   
   
   
   Run the **display vsi name vsi1 verbose** command on SPE1. The command output shows that both the VSI and PW are in the up state.
   
   ```
   [~SPE1] display vsi name vsi1 verbose
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
   
   Run the **display bgp evpn all routing-table** command on SPE1 to check EVPN routes. The command output shows the MAC routes on the VPLS-side interface and the ES routes and per-ES Ethernet A-D routes corresponding to the ESI of the PW.
   
   ```
   [~SPE1] display bgp evpn all routing-table
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
    *>i   0000.1111.1111.1111.1111:0                             2001:DB8:3::3
    Route Distinguisher: 2.2.2.2:0
          Network(ESI/EthTagId)                                  NextHop
    *>    0000.1111.1111.1111.1111:4294967295                    127.0.0.1
    Route Distinguisher: 3.3.3.3:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.1111.1111.1111:4294967295                    2001:DB8:3::3
       
   
    EVPN-Instance evrf1:
    Number of A-D Routes: 3
          Network(ESI/EthTagId)                                  NextHop
    *>    0000.1111.1111.1111.1111:0                             127.0.0.1
    * i                                                          2001:DB8:3::3
    *>i   0000.1111.1111.1111.1111:4294967295                    2001:DB8:3::3
    
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
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3
    Route Distinguisher: 100:3
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:4.4.4.4                                           2001:DB8:4::4
       
   
    EVPN-Instance evrf1:
    Number of Inclusive Multicast Routes: 3
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:2.2.2.2                                           127.0.0.1
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3
    *>i   0:32:4.4.4.4                                           2001:DB8:4::4
    
    EVPN address family:
    Number of ES Routes: 2
    Route Distinguisher: 2.2.2.2:0
          Network(ESI)                                           NextHop
    *>    0000.1111.1111.1111.1111                               127.0.0.1
    Route Distinguisher: 3.3.3.3:0
          Network(ESI)                                           NextHop
    *>i   0000.1111.1111.1111.1111                               2001:DB8:3::3
       
   
    EVPN-Instance evrf1:
    Number of ES Routes: 2
          Network(ESI)                                           NextHop
    *>    0000.1111.1111.1111.1111                               127.0.0.1
    * i                                                          2001:DB8:3::3
   ```
   
   The route details include information about the associated PW. The following uses MAC routes as an example.
   
   ```
   [~SPE1] display bgp evpn all routing-table mac-route 0:48:00e0-fc12-3456:0:0.0.0.0
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

* UPE configuration file
  ```
  #
  sysname UPE
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
  mpls ldp remote-peer 2.2.2.2
   remote-ip 2.2.2.2
  #
  mpls ldp remote-peer 3.3.3.3
   remote-ip 3.3.3.3
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
* SPE1 configuration file
  
  ```
  #
  sysname SPE1
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
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator SPE1_ARG unicast-locator SPE1 
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
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator SPE1 ipv6-prefix 2001:DB8:11:: 64
   locator SPE1_ARG ipv6-prefix 2001:DB8:12:: 64 args 10
  #
  mpls ldp
  #
  mpls ldp remote-peer 1.1.1.1
   remote-ip 1.1.1.1
  #
  mpls ldp remote-peer 3.3.3.3
   remote-ip 3.3.3.3
  #
  monitor-group 1
   monitor enable
   binding interface GigabitEthernet0/1/2 down-weight 10
   binding interface GigabitEthernet0/1/3 down-weight 10
  #
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator SPE1
   segment-routing ipv6 locator SPE1_ARG auto-sid-disable
   #
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
   ipv6 enable
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   isis ipv6 enable 1  
  #
  bgp 100
   router-id 2.2.2.2
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   peer 2001:DB8:4::4 as-number 100
   peer 2001:DB8:4::4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
    peer 2001:DB8:4::4 enable
    peer 2001:DB8:4::4 advertise encap-type srv6
  #
  ospf 100
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.2.3.0 0.0.0.255
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
* SPE2 configuration file
  
  ```
  #
  sysname SPE2
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
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator SPE2_ARG unicast-locator SPE2
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
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator SPE2 ipv6-prefix 2001:DB8:21:: 64
   locator SPE2_ARG ipv6-prefix 2001:DB8:22:: 64 args 10
  #
  mpls ldp
  #
  mpls ldp remote-peer 1.1.1.1
   remote-ip 1.1.1.1
  #
  mpls ldp remote-peer 2.2.2.2
   remote-ip 2.2.2.2
  #
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator SPE2
   segment-routing ipv6 locator SPE2_ARG auto-sid-disable
   #
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
   ipv6 enable
   ipv6 address 2001:DB8:10::2/64
   isis ipv6 enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:30::1/64
   isis ipv6 enable 1
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   ipv6 enable
   ipv6 address 2001:DB8:3::3/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 3.3.3.3
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   peer 2001:DB8:4::4 as-number 100
   peer 2001:DB8:4::4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 advertise encap-type srv6
    peer 2001:DB8:4::4 enable
    peer 2001:DB8:4::4 advertise encap-type srv6
  #
  ospf 100
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 10.2.3.0 0.0.0.255
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
* NPE configuration file
  
  ```
  #
  sysname NPE
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:3
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator NPE_ARG unicast-locator NPE
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:4::4
   locator NPE ipv6-prefix 2001:DB8:31:: 64
   locator NPE_ARG ipv6-prefix 2001:DB8:32:: 64 args 10
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator NPE
   segment-routing ipv6 locator NPE_ARG auto-sid-disable
   #
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:30::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/3.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   ipv6 enable
   ipv6 address 2001:DB8:4::4/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 4.4.4.4
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 advertise encap-type srv6
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
  #
  evpn source-address 4.4.4.4
  #
  return
  ```