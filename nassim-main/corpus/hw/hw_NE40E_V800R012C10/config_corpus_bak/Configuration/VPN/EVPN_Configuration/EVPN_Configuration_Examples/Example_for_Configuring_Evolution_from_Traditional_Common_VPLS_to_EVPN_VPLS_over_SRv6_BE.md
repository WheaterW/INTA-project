Example for Configuring Evolution from Traditional Common VPLS to EVPN VPLS over SRv6 BE
========================================================================================

If a large number of traditional common VPLS services exist on the live network, you can configure evolution from traditional common VPLS to EVPN VPLS over SRv6 BE to prevent long-time traffic interruption caused by direct transition from traditional common VPLS to EVPN VPLS over SRv6 BE.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001602532165__fig_dc_vrp_bgp_cfg_407101), traditional common VPLS services have been deployed. It is required that EVPN be deployed on PE1, PE2, and PE3, so that services can be carried over BGP EVPN between PEs. To meet this requirement, an EVPN instance needs to be configured and bound to the BD on PEs. Then, BGP EVPN peer relationships need to be established between PEs.

**Figure 1** Configuring evolution from traditional VPLS to EVPN VPLS over SRv6 BE![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000001552827106.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| PE1 | Loopback 0 | 1.1.1.1/32  2001:DB8:1::1/128 |
| GE 0/2/0 | 10.1.1.1/24  2001:DB8:10::1/64 |
| GE 0/3/0 | 10.2.1.1/24  2001:DB8:20::1/64 |
| PE2 | Loopback 0 | 2.2.2.2/32  2001:DB8:2::2/128 |
| GE 0/2/0 | 10.2.1.2/24  2001:DB8:20::2/64 |
| GE 0/3/0 | 10.3.1.2/24  2001:DB8:30::2/64 |
| PE3 | Loopback 0 | 3.3.3.3/32  2001:DB8:3::3/128 |
| GE 0/1/0 | 10.1.1.3/24  2001:DB8:10::3/64 |
| GE 0/2/0 | 10.3.1.3/24  2001:DB8:30::3/64 |





#### Precautions

During the configuration process, note the following:

* For the same EVPN instance, the export VPN target list of one site shares VPN targets with the import VPN target lists of the other sites. Conversely, the import VPN target list of one site shares VPN targets with the export VPN target lists of the other sites.
* Using the local loopback interface address of each PE as the source address of the PE is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure LDP VPLS on PE1, PE2, CE1, and CE2.
2. Enable IPv6 forwarding and configure an IPv6 address for each involved interface on PE1 and PE2.
3. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on each of PE1 and PE2.
4. Establish a BGP EVPN peer relationship between PEs.
5. Configure BD EVPN on PEs.
6. Configure SRv6 BE on PEs.
7. Create a BD EVPN instance and a BD on each of PE1 and PE3, and bind the BD to the EVPN instance on each PE.
8. Configure a source address on each of PE1 and PE3.
9. Establish a BGP EVPN peer relationship between PE1 and PE3.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name (evrf1)
* RD and RT of the EVPN instance

#### Procedure

1. Configure an IPv4/IPv6 address for each involved interface and configure IGP on each device. Configure OSPF on PEs for IPv4 route reachability and IS-ISv6 on PEs for IPv6 route reachability.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0000001602532165__en-us_task_0172368978_section_dc_vrp_srv6_cfg_all_002205).
2. Ensure that a non-EVC connection has been configured to carry a VPLS service. For configuration details, see [Configuration Files](#EN-US_TASK_0000001602532165__en-us_task_0172368978_section_dc_vrp_srv6_cfg_all_002205).
   
   
   
   Run the **display vsi name e1 verbose** command on PE1. The command output shows that the VSI named **e1** has separate PWs to PE2 and PE3, and the VSI status and PW status are up.
   
   ```
   [~PE1] display vsi name e1 verbose
    
    ***VSI Name               : e1
       Work Mode              : normal
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 9
       PW Signaling           : ldp
       Member Discovery Style : --
       Bridge-domain Mode     : disable
       PW MAC Learn Style     : unqualify
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
       Create Time            : 0 days, 0 hours, 7 minutes, 39 seconds
       VSI State              : up
       Resource Status        : --
    
       VSI ID                 : 10
      *Peer Router ID         : 2.2.2.2
       Negotiation-vc-id      : 10
       Encapsulation Type     : vlan
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 48106
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004cab42 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       CKey                   : 641
       NKey                   : 16777840
       Stp Enable             : 0
       PwIndex                : 641
       Control Word           : disable
       BFD for PW             : unavailable
      *Peer Router ID         : 3.3.3.3
       Negotiation-vc-id      : 10
       Encapsulation Type     : vlan
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 48107
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004cab43 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       CKey                   : 642
       NKey                   : 16777841
       Stp Enable             : 0
       PwIndex                : 642
       Control Word           : disable
       BFD for PW             : unavailable
    
       Interface Name         : Ethernet3/0/9.1
       State                  : up
       Ac Block State         : unblocked
       Access Port            : false
       Last Up Time           : 2023/04/18 14:20:16
       Total Up Time          : 0 days, 0 hours, 6 minutes, 35 seconds
    
     **PW Information:
    
      *Peer Ip Address        : 2.2.2.2
       PW State               : up
       Local VC Label         : 48106
       Remote VC Label        : 48099
       Remote Control Word    : disable
       PW Type                : label
       Local  VCCV            : alert lsp-ping bfd 
       Remote VCCV            : alert lsp-ping bfd 
       Tunnel ID              : 0x0000000001004cab42 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 641
       Nkey                   : 16777840
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : --
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       Monitor Group Name     : --
       PW Last Up Time        : 2023/04/18 14:20:22
       PW Total Up Time       : 0 days, 0 hours, 6 minutes, 29 seconds
      *Peer Ip Address        : 3.3.3.3
       PW State               : up
       Local VC Label         : 48107
       Remote VC Label        : 48101
       Remote Control Word    : disable
       PW Type                : label
       Local  VCCV            : alert lsp-ping bfd 
       Remote VCCV            : alert lsp-ping bfd 
       Tunnel ID              : 0x0000000001004cab43 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 642
       Nkey                   : 16777841
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : --
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       Monitor Group Name     : --
       PW Last Up Time        : 2023/04/18 14:20:51
       PW Total Up Time       : 0 days, 0 hours, 6 minutes, 0 seconds
   ```
3. Establish a BGP EVPN peer relationship between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:2::2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:2::2 connect-interface loopback 0
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 0
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:2::2 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:2::2 advertise encap-type srv6
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
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
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] router-id 2.2.2.2
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 0
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:3::3 connect-interface loopback 0
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] router-id 3.3.3.3
   ```
   ```
   [*PE3-bgp] peer 2001:DB8:1::1 as-number 100
   ```
   ```
   [*PE3-bgp] peer 2001:DB8:1::1 connect-interface loopback 0
   ```
   ```
   [*PE3-bgp] peer 2001:DB8:2::2 as-number 100
   ```
   ```
   [*PE3-bgp] peer 2001:DB8:2::2 connect-interface loopback 0
   ```
   ```
   [*PE3-bgp] l2vpn-family evpn
   ```
   ```
   [*PE3-bgp-af-evpn] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE3-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   ```
   ```
   [*PE3-bgp-af-evpn] peer 2001:DB8:2::2 enable
   ```
   ```
   [*PE3-bgp-af-evpn] peer 2001:DB8:2::2 advertise encap-type srv6
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
4. Configure SRv6 BE and a BD EVPN instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator PE1_BUM ipv6-prefix 2001:DB8:12:: 64 args 10
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] locator PE1_UNICAST ipv6-prefix 2001:DB8:11:: 64
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] segment-routing ipv6 locator PE1_UNICAST
   ```
   ```
   [*PE1-isis-1] segment-routing ipv6 locator PE1_BUM auto-sid-disable
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 locator PE1_BUM unicast-locator PE1_UNICAST
   ```
   ```
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 best-effort
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   ```
   ```
   [*PE2-segment-routing-ipv6] locator PE2_BUM ipv6-prefix 2001:DB8:22:: 64 args 10
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE2-segment-routing-ipv6] locator PE2_UNICAST ipv6-prefix 2001:DB8:21:: 64
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE2-segment-routing-ipv6] quit
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] segment-routing ipv6 locator PE2_UNICAST
   ```
   ```
   [*PE2-isis-1] segment-routing ipv6 locator PE2_BUM auto-sid-disable
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] route-distinguisher 100:2
   ```
   ```
   [*PE2-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 locator PE2_BUM unicast-locator PE2_UNICAST
   ```
   ```
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 best-effort
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] segment-routing ipv6
   ```
   ```
   [*PE3-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*PE3-segment-routing-ipv6] locator PE3_BUM ipv6-prefix 2001:DB8:32:: 64 args 10
   ```
   ```
   [*PE3-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE3-segment-routing-ipv6] locator PE3_UNICAST ipv6-prefix 2001:DB8:31:: 64
   ```
   ```
   [*PE3-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE3-segment-routing-ipv6] quit
   ```
   ```
   [*PE3] isis 1
   ```
   ```
   [*PE3-isis-1] segment-routing ipv6 locator PE3_UNICAST
   ```
   ```
   [*PE3-isis-1] segment-routing ipv6 locator PE3_BUM auto-sid-disable
   ```
   ```
   [*PE3-isis-1] quit
   ```
   ```
   [*PE3] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE3-evpn-instance-evrf1] route-distinguisher 100:3
   ```
   ```
   [*PE3-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE3-evpn-instance-evrf1] segment-routing ipv6 locator PE3_BUM unicast-locator PE3_UNICAST
   ```
   ```
   [*PE3-evpn-instance-evrf1] segment-routing ipv6 best-effort
   ```
   ```
   [*PE3-evpn-instance-evrf1] quit
   ```
   ```
   [*PE3] commit
   ```
5. On PEs, create a BD, run a command to indicate that the BD is evolving from VPLS to EVPN, and bind the BD to VSIs and EVPN instances.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] vpls-to-evpn migration in-process
   ```
   ```
   [*PE1-bd10] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [~PE1-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [~PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] l2 binding vsi e1
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
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 2.2.2.2
   ```
   ```
   [*PE2] bridge-domain 10
   ```
   ```
   [*PE2-bd10] vpls-to-evpn migration in-process
   ```
   ```
   [*PE2-bd10] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [~PE2-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [~PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] bridge-domain 10
   ```
   ```
   [*PE2-bd10] l2 binding vsi e1
   ```
   ```
   [*PE2-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE2-bd10] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 3.3.3.3
   ```
   ```
   [*PE3] bridge-domain 10
   ```
   ```
   [*PE3-bd10] vpls-to-evpn migration in-process
   ```
   ```
   [*PE3-bd10] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/3/0.1
   ```
   ```
   [~PE3-GigabitEthernet0/3/0.1] bridge-domain 10
   ```
   ```
   [~PE13-GigabitEthernet0/3/0.1] quit
   ```
   ```
   [*PE3] bridge-domain 10
   ```
   ```
   [*PE3-bd10] l2 binding vsi e1
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
6. Verifying the Configuration
   
   
   
   After completing the configurations, run the **display bgp evpn peer** command on PE1. The command output shows that BGP peer relationships are in the **Established** state, indicating that BGP peer relationships have been successfully established between PEs.
   
   ```
   [~PE1] display bgp evpn peer 
    
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
    
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:2::2                    4         100       63       65     0 00:48:30 Established        1
     2001:DB8:3::3                    4         100       64       65     0 00:47:36 Established        1
   ```
   
   
   
   Run the **display bgp evpn all routing-table** command on PE1. The command output shows information about inclusive multicast routes received from PE2 and PE3.
   
   ```
   [~PE1] display bgp evpn all routing-table 
    
    
    Local AS number : 100
    
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    
    
    EVPN address family:
    Number of Inclusive Multicast Routes: 3
    Route Distinguisher: 100:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1                                    
    Route Distinguisher: 100:2
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:2.2.2.2                                           2001:DB8:2::2                                
    Route Distinguisher: 100:3
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3                                
       
    
    EVPN-Instance evrf1:
    Number of Inclusive Multicast Routes: 3
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1                                    
    *>i   0:32:2.2.2.2                                           2001:DB8:2::2                                
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3
   ```
   
   
   
   Run the **display vsi name e1 verbose** command on PE1. The command output shows that the PWs from PE1 to PE2 and PE3 do not exist.
   
   ```
   [~PE1] display vsi name e1 verbose 
    
    ***VSI Name               : e1
       Work Mode              : normal
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 9
       PW Signaling           : ldp
       Member Discovery Style : --
       Bridge-domain Mode     : disable
       PW MAC Learn Style     : unqualify
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
       Create Time            : 0 days, 0 hours, 46 minutes, 36 seconds
       VSI State              : up
       Resource Status        : --
    
       VSI ID                 : 10
      *Peer Router ID         : 2.2.2.2
       Negotiation-vc-id      : 10
       Encapsulation Type     : vlan
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 48106
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004cab42 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       CKey                   : 641
       NKey                   : 16777840
       Stp Enable             : 0
       PwIndex                : 641
       Control Word           : disable
       BFD for PW             : unavailable
      *Peer Router ID         : 3.3.3.3
       Negotiation-vc-id      : 10
       Encapsulation Type     : vlan
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 48107
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004cab43 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       CKey                   : 642
       NKey                   : 16777841
       Stp Enable             : 0
       PwIndex                : 642
       Control Word           : disable
       BFD for PW             : unavailable
    
       Interface Name         : Ethernet3/0/9.1
       State                  : up
       Ac Block State         : unblocked
       Access Port            : false
       Last Up Time           : 2023/04/18 14:20:16
       Total Up Time          : 0 days, 0 hours, 45 minutes, 32 seconds
    
       Access Bridge-domain   : Bridge-domain 10 
       Vac State              : up 
       Last Up Time           : 2023/04/18 14:20:16
       Total Up Time          : 0 days, 0 hours, 45 minutes, 32 seconds
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE1_BUM unicast-locator PE1_UNICAST
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi e1
   pwsignal ldp
    vsi-id 10
    peer 2.2.2.2
    peer 3.3.3.3
  #
  bridge-domain 10
   vpls-to-evpn migration in-process
   l2 binding vsi e1
   evpn binding vpn-instance evrf1
  #
  mpls ldp
   #
   ipv4-family
  # 
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1_BUM ipv6-prefix 2001:DB8:12:: 64 args 10
   locator PE1_UNICAST ipv6-prefix 2001:DB8:11:: 64
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1_UNICAST
   segment-routing ipv6 locator PE1_BUM auto-sid-disable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10 
   bridge-domain 10
   l2 binding vsi e1 
  #
  interface GigabitEthernet0/2/0
   undo shutdown 
   ipv6 enable
   ip address 10.1.1.1 255.255.255.0 
   ipv6 address 2001:DB8:10::1/64 
   isis ipv6 enable 1 
   mpls 
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown 
   ipv6 enable
   ip address 10.2.1.1 255.255.255.0 
   ipv6 address 2001:DB8:20::1/64 
   isis ipv6 enable 1 
   mpls 
   mpls ldp
  #
  interface LoopBack0
   ipv6 enable
   ip address 1.1.1.1 255.255.255.255
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #
  bgp 100
   router-id 1.1.1.1
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack0
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack0
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
  ospf 1
   opaque-capability enable
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
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:2
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE2_BUM unicast-locator PE2_UNICAST
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi e1
   pwsignal bgp
    vsi-id 10
    peer 1.1.1.1
    peer 3.3.3.3
  #
  bridge-domain 10
   vpls-to-evpn migration in-process
   l2 binding vsi e1
   evpn binding vpn-instance evrf1
  #
  mpls ldp
   #
   ipv4-family
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator PE2_BUM ipv6-prefix 2001:DB8:22:: 64 args 10
   locator PE2_UNICAST ipv6-prefix 2001:DB8:21:: 64
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2_UNICAST
   segment-routing ipv6 locator PE2_BUM auto-sid-disable
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #               
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   bridge-domain 10
   l2 binding vsi e1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ip address 10.2.1.2 255.255.255.0
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ip address 10.3.1.2 255.255.255.0 
   ipv6 address 2001:DB8:30::2/64
   isis ipv6 enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ipv6 enable
   ip address 2.2.2.2 255.255.255.255
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1 
  #
  bgp 100
   router-id 2.2.2.2
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack0
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack0 
   #
   ipv4-family unicast
    undo synchronization
   #
   l2vpn-family evpn 
    policy vpn-target 
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6 
  #
  ospf 1 
    area 0.0.0.0 
     network 2.2.2.2 0.0.0.0 
     network 10.2.1.0 0.0.0.255 
     network 10.3.1.0 0.0.0.255 
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
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:3
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE3_BUM unicast-locator PE3_UNICAST
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn      
  #
  vsi e1
   pwsignal bgp
    vsi-id 10
    peer 1.1.1.1
    peer 2.2.2.2
  #
  bridge-domain 10
   vpls-to-evpn migration in-process
   l2 binding vsi e1
   evpn binding vpn-instance evrf1
  #
  mpls ldp
   #
   ipv4-family
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator PE3_BUM ipv6-prefix 2001:DB8:32:: 64 args 10
   locator PE3_UNICAST ipv6-prefix 2001:DB8:31:: 64 
   # 
   isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE3_UNICAST
   segment-routing ipv6 locator PE3_BUM auto-sid-disable 
   # 
  # 
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ip address 10.1.1.3 255.255.255.0 
   ipv6 address 2001:DB8:10::3/64
   isis ipv6 enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ip address 10.3.1.3 255.255.255.0
   ipv6 address 2001:DB8:30::3/64
   isis ipv6 enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.1
   vlan-type dot1q 10
   bridge-domain 10
   l2 binding vsi e1
  #
  interface LoopBack0
   ipv6 enable
   ip address 3.3.3.3 255.255.255.255
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1 
  #
  bgp 100
   router-id 3.3.3.3 
   peer 2001:DB8:1::1 as-number 100 
   peer 2001:DB8:1::1 connect-interface LoopBack0
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack0 
   # 
   ipv4-family unicast 
    undo synchronization 
   # 
   l2vpn-family evpn 
    policy vpn-target 
    peer 2001:DB8:1::1 enable 
    peer 2001:DB8:1::1 advertise encap-type srv6 
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 advertise encap-type srv6
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