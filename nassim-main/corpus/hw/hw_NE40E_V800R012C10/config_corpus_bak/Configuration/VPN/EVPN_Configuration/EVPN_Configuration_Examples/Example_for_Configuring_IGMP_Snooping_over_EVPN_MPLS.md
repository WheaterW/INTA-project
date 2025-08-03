Example for Configuring IGMP Snooping over EVPN MPLS
====================================================

On a network where an EVPN carries multicast services, to reduce redundant traffic and conserve bandwidth resources, configure an EVPN over mLDP P2MP tunnel for service transmission.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370667__fig_dc_vrp_evpn_cfg_009501), EVPN is deployed on PEs to carry Layer 2 multicast services. PE1 is the root node, and PE2 and PE3 are leaf nodes. The multicast source and the receiver are on the access side. By default, when the EVPN function is deployed on a network to carry Layer 2 multicast services, multicast data packets are broadcast on the network. The devices that do not need to receive the multicast data packets also receive these packets, which wastes network bandwidth resources. To resolve this issue, deploy IGMP snooping over EVPN MPLS. After IGMP snooping over EVPN MPLS is deployed, IGMP snooping packets are transmitted on the network through EVPN routes, and multicast forwarding entries are generated on devices. Multicast data packets from a multicast source are advertised only to the devices that need these packets, conserving network bandwidth resources.

**Figure 1** Configuring IGMP snooping over EVPN MPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_evpn_cfg_009501.png)

#### Configuration Precautions

During the configuration process, note the following:

* For the same EVPN instance, the export VPN target list of one site shares VPN targets with the import VPN target lists of the other sites. Conversely, the import VPN target list of one site shares VPN targets with the export VPN target lists of the other sites.
* Using each PE's local loopback interface address as its EVPN source address is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the backbone network to enable PEs and the RR to communicate.
2. Configure MPLS and mLDP P2MP on the backbone network and set up an mLDP P2MP tunnel.
3. Create an EVPN instance in BD mode and a BD on each PE, and bind the BD to the EVPN instance on each PE.
4. Configure a source address on each PE.
5. Configure each PE's sub-interface connecting to a CE.
6. Configure an ESI for each PE interface that connects to a CE.
7. Configure BGP EVPN peer relationships between the PEs and RR, and on the RR, specify the PEs as RR clients.
8. Configure EVPN to use an mLDP P2MP tunnel for service transmission on each PE.
9. Configure IGMP snooping over EVPN MPLS on each PE.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* EVPN instance evrf1's RD (100:1) and RT (1:1) on each PE

#### Procedure

1. Configure interface addresses on the RR and PEs according to [Figure 1](#EN-US_TASK_0172370667__fig_dc_vrp_evpn_cfg_009501). For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370667__file1).
2. Configure an IGP on the backbone network to enable PEs and the RR to communicate. OSPF is used as an IGP in this example.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] area 0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE1-ospf-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE2-ospf-1] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ospf 1
   ```
   ```
   [*PE3-ospf-1] area 0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 4.4.4.4 0.0.0.0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE3-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE3-ospf-1] quit
   ```
   
   # Configure the RR.
   
   ```
   [~RR] ospf 1
   ```
   ```
   [*RR-ospf-1] area 0
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~RR-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~RR-ospf-1] quit
   ```
3. Configure MPLS and mLDP P2MP on the backbone network and set up an mLDP P2MP tunnel.
   
   
   
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
   [*PE1-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE1-mpls-ldp] quit
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
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 2.2.2.2
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
   [*PE2-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE2-mpls-ldp] quit
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
   
   # Configure the RR.
   
   ```
   [~RR] mpls lsr-id 3.3.3.3
   ```
   ```
   [*RR] mpls
   ```
   ```
   [*RR-mpls] quit
   ```
   ```
   [*RR] mpls ldp
   ```
   ```
   [*RR-mpls-ldp] mldp p2mp
   ```
   ```
   [*RR-mpls-ldp] quit
   ```
   ```
   [*RR] interface gigabitethernet 0/1/0
   ```
   ```
   [*RR-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*RR-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*RR-GigabitEthernet0/1/0] quit
   ```
   ```
   [*RR] interface gigabitethernet 0/2/0
   ```
   ```
   [*RR-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*RR-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*RR-GigabitEthernet0/2/0] quit
   ```
   ```
   [*RR] interface gigabitethernet 0/3/0
   ```
   ```
   [*RR-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*RR-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*RR-GigabitEthernet0/3/0] commit
   ```
   ```
   [~RR-GigabitEthernet0/3/0] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls lsr-id 4.4.4.4
   ```
   ```
   [*PE3] mpls
   ```
   ```
   [*PE3-mpls] quit
   ```
   ```
   [*PE3] mpls ldp
   ```
   ```
   [*PE3-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE3-mpls-ldp] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE3-GigabitEthernet0/1/0] quit
   ```
4. Configure an EVPN instance on each PE.
   
   
   
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
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] bridge-domain 10
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
5. Configure a source address on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 2.2.2.2
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 4.4.4.4
   ```
   ```
   [*PE3] commit
   ```
6. Configure an Eth-Trunk sub-interface on each PE connecting to a CE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface eth-trunk 10
   ```
   ```
   [*PE1-Eth-Trunk10] quit
   ```
   ```
   [*PE1] interface eth-trunk 10.1 mode l2
   ```
   ```
   [*PE1-Eth-Trunk10.1] encapsulation dot1q vid 100
   ```
   ```
   [*PE1-Eth-Trunk10.1] rewrite pop single
   ```
   ```
   [*PE1-Eth-Trunk10.1] bridge-domain 10
   ```
   ```
   [*PE1-Eth-Trunk10.1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] eth-trunk 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface eth-trunk 10
   ```
   ```
   [*PE2-Eth-Trunk10] quit
   ```
   ```
   [*PE2] interface eth-trunk 10.1 mode l2
   ```
   ```
   [*PE2-Eth-Trunk10.1] encapsulation dot1q vid 100
   ```
   ```
   [*PE2-Eth-Trunk10.1] rewrite pop single
   ```
   ```
   [*PE2-Eth-Trunk10.1] bridge-domain 10
   ```
   ```
   [*PE2-Eth-Trunk10.1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] eth-trunk 10
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] e-trunk 1
   ```
   ```
   [*PE2-e-trunk-1] peer-address 4.4.4.4 source-address 2.2.2.2
   ```
   ```
   [*PE2-e-trunk-1] quit
   ```
   ```
   [*PE2] interface eth-trunk 20
   ```
   ```
   [*PE2-Eth-Trunk20] e-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk20] e-trunk mode force-master
   ```
   ```
   [*PE2-Eth-Trunk20] quit
   ```
   ```
   [*PE2] interface eth-trunk 20.1 mode l2
   ```
   ```
   [*PE2-Eth-Trunk20.1] encapsulation dot1q vid 100
   ```
   ```
   [*PE2-Eth-Trunk20.1] rewrite pop single
   ```
   ```
   [*PE2-Eth-Trunk20.1] bridge-domain 10
   ```
   ```
   [*PE2-Eth-Trunk20.1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] eth-trunk 20
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] interface eth-trunk 10
   ```
   ```
   [*PE3-Eth-Trunk10] quit
   ```
   ```
   [*PE3] interface eth-trunk 10.1 mode l2
   ```
   ```
   [*PE3-Eth-Trunk10.1] encapsulation dot1q vid 100
   ```
   ```
   [*PE3-Eth-Trunk10.1] rewrite pop single
   ```
   ```
   [*PE3-Eth-Trunk10.1] bridge-domain 10
   ```
   ```
   [*PE3-Eth-Trunk10.1] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] eth-trunk 10
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE3] e-trunk 1
   ```
   ```
   [*PE3-e-trunk-1] peer-address 2.2.2.2 source-address 4.4.4.4
   ```
   ```
   [*PE3-e-trunk-1] quit
   ```
   ```
   [*PE3] interface eth-trunk 20
   ```
   ```
   [*PE3-Eth-Trunk20] e-trunk 1
   ```
   ```
   [*PE3-Eth-Trunk20] e-trunk mode force-master
   ```
   ```
   [*PE3-Eth-Trunk20] quit
   ```
   ```
   [*PE3] interface eth-trunk 20.1 mode l2
   ```
   ```
   [*PE3-Eth-Trunk20.1] encapsulation dot1q vid 100
   ```
   ```
   [*PE3-Eth-Trunk20.1] rewrite pop single
   ```
   ```
   [*PE3-Eth-Trunk20.1] bridge-domain 10
   ```
   ```
   [*PE3-Eth-Trunk20.1] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] eth-trunk 20
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE3] commit
   ```
7. Configure an ESI for each PE interface that connects to a CE.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] interface eth-trunk 10
   ```
   ```
   [*PE2-Eth-Trunk10] esi 0000.1111.2222.4444.5555
   ```
   ```
   [*PE2-Eth-Trunk10] quit
   ```
   ```
   [*PE2] interface eth-trunk 20
   ```
   ```
   [*PE2-Eth-Trunk20] esi 0000.2222.2222.3333.4444
   ```
   ```
   [*PE2-Eth-Trunk20] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] interface eth-trunk 10
   ```
   ```
   [*PE3-Eth-Trunk10] esi 0000.1111.3333.4444.5555
   ```
   ```
   [*PE3-Eth-Trunk10] quit
   ```
   ```
   [*PE3] interface eth-trunk 20
   ```
   ```
   [*PE3-Eth-Trunk20] esi 0000.2222.3333.3333.4444
   ```
   ```
   [*PE3-Eth-Trunk20] quit
   ```
   ```
   [*PE3] commit
   ```
8. Configure BGP EVPN peer relationships between the PEs and RR, and on the RR, specify the PEs as RR clients.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
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
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 3.3.3.3 enable
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
   [*PE3-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE3-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*PE3-bgp] l2vpn-family evpn
   ```
   ```
   [*PE3-bgp-af-evpn] peer 3.3.3.3 enable
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
   
   # Configure the RR.
   
   ```
   [~RR] bgp 100
   ```
   ```
   [*RR-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*RR-bgp] peer 1.1.1.1 connect-interface loopback 0
   ```
   ```
   [*RR-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*RR-bgp] peer 2.2.2.2 connect-interface loopback 0
   ```
   ```
   [*RR-bgp] peer 4.4.4.4 as-number 100
   ```
   ```
   [*RR-bgp] peer 4.4.4.4 connect-interface loopback 0
   ```
   ```
   [*RR-bgp] l2vpn-family evpn
   ```
   ```
   [*RR-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 1.1.1.1 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 2.2.2.2 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 4.4.4.4 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] quit
   ```
   ```
   [*RR-bgp] quit
   ```
   ```
   [*RR] commit
   ```
   
   After completing the configurations, run the **display bgp evpn peer** command on the RR. The command output shows that BGP peer relationships have been established between the PEs and RR and are in the **Established** state.
   
   ```
   [~RR] display bgp evpn peer
   ```
   ```
    
    BGP local router ID : 10.1.1.2
    Local AS number : 100
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     1.1.1.1         4         100      231      253     0 03:07:26 Established        6
     2.2.2.2         4         100      231      256     0 03:07:44 Established        6
     4.4.4.4         4         100      232      254     0 03:07:54 Established        6
   ```
9. Configure EVPN to use an mLDP P2MP tunnel for service transmission on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [~PE1-evpn-instance-evrf1] inclusive-provider-tunnel
   ```
   ```
   [*PE1-evpn-instance-evrf1-inclusive] root
   ```
   ```
   [*PE1-evpn-instance-evrf1-inclusive-root] mldp p2mp
   ```
   ```
   [*PE1-evpn-instance-evrf1-inclusive-root-mldpp2mp] root-ip 1.1.1.1
   ```
   ```
   [*PE1-evpn-instance-evrf1-inclusive-root-mldpp2mp] quit
   ```
   ```
   [*PE1-evpn-instance-evrf1-inclusive-root] quit
   ```
   ```
   [*PE1-evpn-instance-evrf1-inclusive] quit
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [~PE2-evpn-instance-evrf1] inclusive-provider-tunnel
   ```
   ```
   [*PE2-evpn-instance-evrf1-inclusive] leaf
   ```
   ```
   [*PE2-evpn-instance-evrf1-inclusive-leaf] quit
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [~PE3-evpn-instance-evrf1] inclusive-provider-tunnel
   ```
   ```
   [*PE3-evpn-instance-evrf1-inclusive] leaf
   ```
   ```
   [*PE3-evpn-instance-evrf1-inclusive-leaf] quit
   ```
   ```
   [*PE3-evpn-instance-evrf1] quit
   ```
   ```
   [*PE3] commit
   ```
10. Configure IGMP snooping over EVPN MPLS on each PE.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] igmp-snooping enable
    ```
    ```
    [*PE1] bridge-domain 10
    ```
    ```
    [*PE1-bd10] igmp-snooping enable
    ```
    ```
    [*PE1-bd10] igmp-snooping proxy
    ```
    ```
    [*PE1-bd10] igmp-snooping signal-synch enable
    ```
    ```
    [*PE1-bd10] evi vpn-target 100:1
    ```
    ```
    [*PE1-bd10] quit
    ```
    ```
    [*PE1] commit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] igmp-snooping enable
    ```
    ```
    [*PE2] bridge-domain 10
    ```
    ```
    [*PE2-bd10] igmp-snooping enable
    ```
    ```
    [*PE2-bd10] igmp-snooping proxy
    ```
    ```
    [*PE2-bd10] igmp-snooping signal-synch enable
    ```
    ```
    [*PE2-bd10] evi vpn-target 100:1
    ```
    ```
    [*PE2-bd10] quit
    ```
    ```
    [*PE2] commit
    ```
    
    # Configure PE3.
    
    ```
    [~PE3] igmp-snooping enable
    ```
    ```
    [*PE3] bridge-domain 10
    ```
    ```
    [*PE3-bd10] igmp-snooping enable
    ```
    ```
    [*PE3-bd10] igmp-snooping proxy
    ```
    ```
    [*PE3-bd10] igmp-snooping signal-synch enable
    ```
    ```
    [*PE3-bd10] evi vpn-target 100:1
    ```
    ```
    [*PE3-bd10] quit
    ```
    ```
    [*PE3] commit
    ```
11. Verify the configuration.
    
    
    
    Run the **display evpn vpn-instance name evrf1 inclusive-provider-tunnel verbose** command on PE1. The command output shows information related to the root node.
    
    ```
    [~PE1] display evpn vpn-instance name evrf1 inclusive-provider-tunnel verbose
    ```
    ```
     VPN-Instance Name and ID : evrf1, 3
      Address family bd-evpn
      Route Distinguisher : 100:1
      Label Policy        : label per bridge-domain
      Export VPN Targets  : 1:1
      Import VPN Targets  : 1:1
      Bridge-domain       : 10
      Ingress provider tunnel
        PMSI type      : P2MP mLDP
        Root ip        : 1.1.1.1
        Opaque value   : 01000400008001
        State          : up
      Egress provider tunnel
      Egress PMSI count: 0
    ```
    
    Run the **display evpn vpn-instance name evrf1 inclusive-provider-tunnel verbose** command on PE2 or PE3. The command output shows information related to the leaf node. The command output on PE2 is used as an example.
    
    ```
    [~PE2] display evpn vpn-instance name evrf1 inclusive-provider-tunnel verbose
    ```
    ```
     VPN-Instance Name and ID : evrf1, 3
      Address family bd-evpn
      Route Distinguisher : 100:1
      Label Policy        : label per bridge-domain
      Export VPN Targets  : 1:1
      Import VPN Targets  : 1:1
      Bridge-domain       : 10
      Ingress provider tunnel
      Egress provider tunnel
      Egress PMSI count: 1
       *PMSI type      : P2MP mLDP
        Root ip        : 1.1.1.1
        Opaque value   : 01000400008001
        State          : up
    
    ```
    
    Run the **display bgp evpn all routing-table join-route** command on each PE. The command output shows Join route information. The following example uses the command output on PE1.
    
    ```
    [~PE1] display bgp evpn all routing-table join-route
    ```
    ```
     Local AS number : 100
    
     BGP Local router ID is 1.1.1.1
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
     
     EVPN address family:
     Number of IGMP Join Synch Routes: 2
     Route Distinguisher: 100:1
           Network(ESI/EthTagId/IpAddrLen/SAddr/IpAddrLen/GAddr/IpAddrLen/OAddr)                          NextHop
     *>    0000.1111.2222.4444.5555:0:0:0.0.0.0:32:225.0.0.1:32:1.1.1.1                                   127.0.0.1
     *>    0000.1111.3333.4444.5555:0:0:0.0.0.0:32:225.0.0.1:32:1.1.1.1                                   127.0.0.1
        
    
     EVPN-Instance evrf1:
     Number of IGMP Join Synch Routes: 1
           Network(ESI/EthTagId/IpAddrLen/SAddr/IpAddrLen/GAddr/IpAddrLen/OAddr)                          NextHop
     *>    0000.1111.2222.4444.5555:0:0:0.0.0.0:32:225.0.0.1:32:1.1.1.1                                   127.0.0.1
     *>    0000.1111.3333.4444.5555:0:0:0.0.0.0:32:225.0.0.1:32:1.1.1.1                                   127.0.0.1
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  igmp-snooping enable
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
   inclusive-provider-tunnel
    root
     mldp p2mp
      root-ip 1.1.1.1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
   igmp-snooping enable
   igmp-snooping proxy
   igmp-snooping signal-synch enable
   evi vpn-target 100:1 export-extcommunity
   evi vpn-target 100:1 import-extcommunity
  #
  mpls ldp
   mldp p2mp
  #
  interface Eth-Trunk10
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
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
  igmp-snooping enable
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
   inclusive-provider-tunnel
    leaf
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
   igmp-snooping enable
   igmp-snooping proxy
   igmp-snooping signal-synch enable
   evi vpn-target 100:1 export-extcommunity
   evi vpn-target 100:1 import-extcommunity
  #
  mpls ldp
   mldp p2mp
  #
  e-trunk 1
   peer-address 4.4.4.4 source-address 2.2.2.2
  #
  interface Eth-Trunk10
   esi 0000.1111.2222.4444.5555
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 10
  #
  interface Eth-Trunk20
   esi 0000.2222.2222.3333.4444
   e-trunk 1
   e-trunk mode force-master
  #
  interface Eth-Trunk20.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   eth-trunk 10
  #
  interface gigabitethernet 0/3/0
   undo shutdown
   eth-trunk 20
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.2.1.0 0.0.0.255
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
  igmp-snooping enable
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
   inclusive-provider-tunnel
    leaf
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
   igmp-snooping enable
   igmp-snooping proxy
   igmp-snooping signal-synch enable
   evi vpn-target 100:1 export-extcommunity
   evi vpn-target 100:1 import-extcommunity
  #
  mpls ldp
   mldp p2mp
  #
  e-trunk 1
   peer-address 2.2.2.2 source-address 4.4.4.4
  #
  interface Eth-Trunk10
   esi 0000.1111.3333.4444.5555
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 10
  #
  interface Eth-Trunk20
   esi 0000.2222.3333.3333.4444
   e-trunk 1
   e-trunk mode force-master
  #
  interface Eth-Trunk20.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   eth-trunk 10
  #
  interface gigabitethernet 0/3/0
   undo shutdown
   eth-trunk 20
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #              
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  evpn source-address 4.4.4.4
  #
  return
  ```
* RR configuration file
  
  ```
  #
  sysname RR
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 4.4.4.4 enable
    peer 4.4.4.4 reflect-client
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  bridge-domain 10
  #
  interface Eth-Trunk10
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  bridge-domain 10
  #
  interface Eth-Trunk10
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  return
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  bridge-domain 10
  #
  interface Eth-Trunk10
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  return
  ```