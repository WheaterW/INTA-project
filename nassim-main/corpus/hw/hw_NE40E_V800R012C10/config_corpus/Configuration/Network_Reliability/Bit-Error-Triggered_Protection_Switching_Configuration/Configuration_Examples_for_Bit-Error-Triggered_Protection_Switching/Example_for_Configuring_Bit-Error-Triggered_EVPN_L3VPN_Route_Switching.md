Example for Configuring Bit-Error-Triggered EVPN L3VPN Route Switching
======================================================================

This section provides an example for configuring bit-error-triggered EVPN L3VPN route switching.

#### Networking Requirements

On an IP RAN, if RSVP-TE tunnels carry EVPN L3VPN services, you can configure the RSVP-TE tunnels to work in TE hot standby mode and VPN FRR to protect the EVPN L3VPN services. However, these protection mechanisms cannot trigger protection switching based on random bit errors caused by optical fiber aging or optical signal jitter. As a result, random bit errors may degrade services on the IP RAN or even interrupt services in extreme cases.

To resolve this problem, configure bit-error-triggered RSVP-TE tunnel switching and EVPN L3VPN route switching. If a bit error event occurs, the system first attempts to perform bit-error-triggered RSVP-TE tunnel switching. If the primary and backup CR-LSPs of the RSVP-TE tunnel are both in the excessive BER state, bit-error-triggered RSVP-TE tunnel switching cannot protect services against bit errors. In this situation, the system performs bit-error-triggered EVPN L3VPN route switching to trigger EVPN route convergence and divert traffic from the link that has encountered the bit error event.

On the EVPN L3VPN HVPN shown in [Figure 1](#EN-US_TASK_0172362308__fig_dc_vrp_cfg_error-code_evpn_000201), RSVP-TE tunnels are established between the UPE and SPEs to carry EVPN L3VPN services, and the tunnels work in TE hot standby mode. VPN FRR is configured on the UPE to protect the EVPN L3VPN services. If GE 0/1/1 on the UPE and GE 0/1/2 on SPE2 both encounter a bit error event, the primary and backup CR-LSPs of the RSVP-TE tunnel that carries the primary EVPN route both enter the excessive BER state. As a result, bit-error-triggered RSVP-TE tunnel switching cannot protect services against bit errors. To resolve this problem, configure bit-error-triggered EVPN L3VPN route switching.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


**Figure 1** Configuring bit-error-triggered EVPN L3VPN route switching  
![](images/fig_dc_vrp_cfg_error-code_evpn_000201.png)

**Table 1** Interface IP address list
| Device | Interface | IP Address |
| --- | --- | --- |
| UPE | Loopback 0 | 1.1.1.1/32 |
| GE 0/1/0 | 10.2.1.1/24 |
| GE 0/1/1 | 10.1.1.1/24 |
| GE 0/1/2 | 10.1.2.1/24 |
| SPE1 | Loopback 0 | 2.2.2.2/32 |
| GE 0/1/0 | 10.1.1.2/24 |
| GE 0/1/1 | 10.1.4.1/24 |
| GE 0/1/2 | 10.1.3.1/24 |
| SPE2 | Loopback 0 | 3.3.3.3/32 |
| GE 0/1/0 | 10.1.5.1/24 |
| GE 0/1/1 | 10.1.2.2/24 |
| GE 0/1/2 | 10.1.3.2/24 |
| NPE | Loopback 0 | 4.4.4.4/32 |
| GE 0/1/0 | 10.1.4.2/24 |
| GE 0/1/1 | 10.1.5.2/24 |
| GE 0/1/2 | 10.3.1.1/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each interface and routing protocols, so that all devices can communicate at the network layer. This example uses OSPF and IS-IS as the routing protocols.
2. Configure BFD on each device on the network.
3. Configure MPLS functions and public network tunnels to carry EVPN L3VPN services. In this example, RSVP-TE tunnels are established between the UPE and SPEs, and LDP LSPs are established between the NPE and SPEs.
4. Create an L3VPN instance on the UPE and NPE and import the local direct routes on the UPE and NPE to their respective VPN instance routing tables.
5. Establish BGP-EVPN peer relationships between the UPE and SPEs, and between the NPE and SPEs.
6. Configure the SPEs as RRs and the UPE as an RR client.
7. Bind the VPN instance on the UPE to the TE tunnels.
8. Configure VPN FRR on the UPE and EVPN FRR on the SPEs.
9. Configure bit-error-triggered RSVP-TE tunnel switching.
10. Configure bit-error-triggered EVPN L3VPN route switching.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Table 1](#EN-US_TASK_0172362308__tab_01).
* OSPF between the UPE and SPEs and IS-IS between the SPEs and NPE, OSPF and IS-IS process IDs (both 1), OSPF area ID (0), IS-IS network entity names (10.0000.0000.0021.00, 10.0000.0000.0022.00, and 10.0000.0000.0003.00).
* LSR IDs of the UPE, SPE1, SPE2, and NPE (1.1.1.1, 2.2.2.2, 3.3.3.3, and 4.4.4.4, respectively)
* Tunnel interface names (Tunnel11), tunnel IDs (20), and tunnel interface addresses (loopback interface addresses) for the bidirectional tunnels between the UPE and SPE1
* Tunnel interface names (Tunnel12), tunnel IDs (200), and tunnel interface addresses (loopback interface addresses) for the bidirectional tunnels between the UPE and SPE2
* Tunnel policy names (policy1) for the unidirectional tunnels between the UPE and SPEs and tunnel selector names (BindTE) on the SPEs
* Names (vpna), RDs (20:1), and VPN targets (1:1) of the VPN instances on the UPE and NPE

#### Procedure

1. Assign an IP address to each interface and configure an IGP.
   
   
   
   Assign an IP address to each interface according to [Table 1](#EN-US_TASK_0172362308__tab_01) and create a loopback interface on each node. For configuration details, see [Configuration Files](#EN-US_TASK_0172362308__section_05) in this section.
   
   
   
   Configure an IGP on each node to allow the nodes to communicate at the network layer. For configuration details, see [Configuration Files](#EN-US_TASK_0172362308__section_05) in this section.
2. Enable BFD globally.
   
   
   
   # Configure the UPE to passively create a BFD session for TE tunnel fault detection.
   
   ```
   [~UPE] bfd
   ```
   ```
   [*UPE-bfd] mpls-passive
   ```
   ```
   [*UPE-bfd] commit
   ```
   ```
   [~UPE-bfd] quit
   ```
   
   Repeat this step for SPE1 and SPE2. For configuration details, see [Configuration Files](#EN-US_TASK_0172362308__section_05) in this section.
3. Configure MPLS functions and public network tunnels.
   1. Enable MPLS, MPLS TE, RSVP-TE, and CSPF.
      
      
      
      # Configure the UPE.
      
      ```
      <UPE> system-view
      ```
      ```
      [~UPE] mpls lsr-id 1.1.1.1
      ```
      ```
      [*UPE] mpls
      ```
      ```
      [*UPE-mpls] mpls te
      ```
      ```
      [*UPE-mpls] mpls rsvp-te
      ```
      ```
      [*UPE-mpls] mpls te cspf
      ```
      ```
      [*UPE-mpls] quit
      ```
      ```
      [*UPE] interface gigabitethernet 0/1/1
      ```
      ```
      [*UPE-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*UPE-GigabitEthernet0/1/1] mpls te
      ```
      ```
      [*UPE-GigabitEthernet0/1/1] mpls rsvp-te
      ```
      ```
      [*UPE-GigabitEthernet0/1/1] quit
      ```
      ```
      [*UPE] interface gigabitethernet 0/1/2
      ```
      ```
      [*UPE-GigabitEthernet0/1/2] mpls
      ```
      ```
      [*UPE-GigabitEthernet0/1/2] mpls te
      ```
      ```
      [*UPE-GigabitEthernet0/1/2] mpls rsvp-te
      ```
      ```
      [*UPE-GigabitEthernet0/1/2] quit
      ```
      ```
      [*UPE] ospf 1
      ```
      ```
      [*UPE-ospf-1] opaque-capability enable
      ```
      ```
      [*UPE-ospf-1] area 0
      ```
      ```
      [*UPE-ospf-1-area-0.0.0.0] mpls-te enable
      ```
      ```
      [*UPE-ospf-1-area-0.0.0.0] quit
      ```
      ```
      [*UPE-ospf-1] quit
      ```
      ```
      [*UPE] commit
      ```
      
      Repeat this step for SPE1 and SPE2. For configuration details, see [Configuration Files](#EN-US_TASK_0172362308__section_05) in this section.
   2. Configure the egress of each unidirectional RSVP-TE tunnel to be created to assign a non-null label to the penultimate hop.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This step is mandatory before you create an RSVP-TE tunnel. If this step is skipped, bit-error-triggered RSVP-TE tunnel switching cannot take effect.
      
      
      # Configure the UPE.
      ```
      [~UPE] mpls
      ```
      ```
      [~UPE-mpls] label advertise non-null
      ```
      ```
      [*UPE-mpls] quit
      ```
      ```
      [*UPE] commit
      ```
      
      # Configure SPE1.
      ```
      <SPE1> system-view
      ```
      ```
      [~SPE1] mpls
      ```
      ```
      [~SPE1-mpls] label advertise non-null
      ```
      ```
      [*SPE1-mpls] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      ```
      <SPE2> system-view
      ```
      ```
      [~SPE2] mpls
      ```
      ```
      [~SPE2-mpls] label advertise non-null
      ```
      ```
      [*SPE2-mpls] quit
      ```
      ```
      [*SPE2] commit
      ```
   3. Configure two unidirectional RSVP-TE tunnels between the UPE and each SPE and configure TE hot standby.
      
      
      
      # Configure the UPE.
      
      ```
      [~UPE] interface Tunnel 11
      ```
      ```
      [*UPE-Tunnel11] ip address unnumbered interface loopback 0
      ```
      ```
      [*UPE-Tunnel11] tunnel-protocol mpls te
      ```
      ```
      [*UPE-Tunnel11] destination 2.2.2.2
      ```
      ```
      [*UPE-Tunnel11] mpls te tunnel-id 20
      ```
      ```
      [*UPE-Tunnel11] mpls te backup hot-standby
      ```
      ```
      [*UPE-Tunnel11] mpls te reserved-for-binding
      ```
      ```
      [*UPE-Tunnel11] mpls te bfd enable
      ```
      ```
      [*UPE-Tunnel11] quit
      ```
      ```
      [*UPE] interface Tunnel 12
      ```
      ```
      [*UPE-Tunnel12] ip address unnumbered interface loopback 0
      ```
      ```
      [*UPE-Tunnel12] tunnel-protocol mpls te
      ```
      ```
      [*UPE-Tunnel12] destination 3.3.3.3
      ```
      ```
      [*UPE-Tunnel12] mpls te tunnel-id 200
      ```
      ```
      [*UPE-Tunnel12] mpls te backup hot-standby
      ```
      ```
      [*UPE-Tunnel12] mpls te reserved-for-binding
      ```
      ```
      [*UPE-Tunnel12] mpls te bfd enable
      ```
      ```
      [*UPE-Tunnel12] quit
      ```
      ```
      [*UPE] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] interface Tunnel 11
      ```
      ```
      [*SPE1-Tunnel11] ip address unnumbered interface loopback 0
      ```
      ```
      [*SPE1-Tunnel11] tunnel-protocol mpls te
      ```
      ```
      [*SPE1-Tunnel11] destination 1.1.1.1
      ```
      ```
      [*SPE1-Tunnel11] mpls te tunnel-id 20
      ```
      ```
      [*SPE1-Tunnel11] mpls te backup hot-standby
      ```
      ```
      [*SPE1-Tunnel11] mpls te reserved-for-binding
      ```
      ```
      [*SPE1-Tunnel11] mpls te bfd enable
      ```
      ```
      [*SPE1-Tunnel11] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] interface Tunnel 12
      ```
      ```
      [*SPE2-Tunnel12] ip address unnumbered interface loopback 0
      ```
      ```
      [*SPE2-Tunnel12] tunnel-protocol mpls te
      ```
      ```
      [*SPE2-Tunnel12] destination 1.1.1.1
      ```
      ```
      [*SPE2-Tunnel12] mpls te tunnel-id 200
      ```
      ```
      [*SPE2-Tunnel12] mpls te backup hot-standby
      ```
      ```
      [*SPE2-Tunnel12] mpls te reserved-for-binding
      ```
      ```
      [*SPE2-Tunnel12] mpls te bfd enable
      ```
      ```
      [*SPE2-Tunnel12] quit
      ```
      ```
      [*SPE2] commit
      ```
   4. Configure a tunnel policy on each device.
      
      
      
      # Configure the UPE.
      
      ```
      [~UPE] tunnel-policy policy1
      ```
      ```
      [*UPE-tunnel-policy-policy1] tunnel binding destination 2.2.2.2 te Tunnel 11
      ```
      ```
      [*UPE-tunnel-policy-policy1] tunnel binding destination 3.3.3.3 te Tunnel 12
      ```
      ```
      [*UPE-tunnel-policy-policy1] quit
      ```
      ```
      [*UPE] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] tunnel-policy policy1
      ```
      ```
      [*SPE1-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel 11
      ```
      ```
      [*SPE1-tunnel-policy-policy1] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] tunnel-policy policy1
      ```
      ```
      [*SPE2-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel 12
      ```
      ```
      [*SPE2-tunnel-policy-policy1] quit
      ```
      ```
      [*SPE2] commit
      ```
   5. Configure LDP LSPs between the NPE and SPEs.
      
      
      
      # Configure SPE1.
      
      ```
      [~SPE1] mpls ldp
      ```
      ```
      [*SPE1-mpls-ldp] commit
      ```
      ```
      [~SPE1-mpls-ldp] quit
      ```
      ```
      [~SPE1] interface gigabitethernet 0/1/2
      ```
      ```
      [~SPE1-GigabitEthernet0/1/2] mpls
      ```
      ```
      [*SPE1-GigabitEthernet0/1/2] mpls ldp
      ```
      ```
      [*SPE1-GigabitEthernet0/1/2] commit
      ```
      ```
      [~SPE1-GigabitEthernet0/1/2] quit
      ```
      
      Repeat this step for SPE2 and the NPE. For configuration details, see [Configuration Files](#EN-US_TASK_0172362308__section_05) in this section.
4. Configure an L3VPN instance on each of the UPE and NPE.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] ip vpn-instance vpna
   ```
   ```
   [*UPE-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] route-distinguisher 20:1
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*UPE-vpn-instance-vpna] evpn mpls routing-enable
   ```
   ```
   [*UPE-vpn-instance-vpna] quit
   ```
   ```
   [*UPE] interface gigabitethernet 0/1/0
   ```
   ```
   [*UPE-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*UPE-GigabitEthernet0/1/0] ip address 10.2.1.1 24
   ```
   ```
   [*UPE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*UPE] bgp 20
   ```
   ```
   [*UPE-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*UPE-bgp-vpna] import-route direct
   ```
   ```
   [*UPE-bgp-vpna] advertise l2vpn evpn
   ```
   ```
   [*UPE-bgp-vpna] quit
   ```
   ```
   [*UPE-bgp] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   <NPE> system-view
   ```
   ```
   [~NPE] ip vpn-instance vpna
   ```
   ```
   [*NPE-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*NPE-vpn-instance-vpna-af-ipv4] route-distinguisher 20:1
   ```
   ```
   [*NPE-vpn-instance-vpna-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*NPE-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*NPE-vpn-instance-vpna] evpn mpls routing-enable
   ```
   ```
   [*NPE-vpn-instance-vpna] quit
   ```
   ```
   [*NPE] interface gigabitethernet 0/1/2
   ```
   ```
   [*NPE-GigabitEthernet0/1/2] ip binding vpn-instance vpna
   ```
   ```
   [*NPE-GigabitEthernet0/1/2] ip address 10.3.1.1 24
   ```
   ```
   [*NPE-GigabitEthernet0/1/2] quit
   ```
   ```
   [*NPE] bgp 20
   ```
   ```
   [*NPE-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*NPE-bgp-vpna] import-route direct
   ```
   ```
   [*NPE-bgp-vpna] advertise l2vpn evpn
   ```
   ```
   [*NPE-bgp-vpna] quit
   ```
   ```
   [*NPE-bgp] quit
   ```
   ```
   [*NPE] commit
   ```
5. Configure BGP-EVPN peer relationships between the UPE and SPEs and between the NPE and SPEs.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] bgp 20
   ```
   ```
   [~UPE-bgp] router-id 1.1.1.1
   ```
   ```
   [*UPE-bgp] peer 2.2.2.2 as-number 20
   ```
   ```
   [*UPE-bgp] peer 2.2.2.2 connect-interface loopback 0
   ```
   ```
   [*UPE-bgp] peer 3.3.3.3 as-number 20
   ```
   ```
   [*UPE-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*UPE-bgp] l2vpn-family evpn
   ```
   ```
   [*UPE-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*UPE-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*UPE-bgp-af-evpn] quit
   ```
   ```
   [*UPE-bgp] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure SPE1.
   
   ```
   [~SPE1] bgp 20
   ```
   ```
   [*SPE1-bgp] router-id 2.2.2.2
   ```
   ```
   [*SPE1-bgp] peer 1.1.1.1 as-number 20
   ```
   ```
   [*SPE1-bgp] peer 1.1.1.1 connect-interface loopback 0
   ```
   ```
   [*SPE1-bgp] peer 3.3.3.3 as-number 20
   ```
   ```
   [*SPE1-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*SPE1-bgp] peer 4.4.4.4 as-number 20
   ```
   ```
   [*SPE1-bgp] peer 4.4.4.4 connect-interface loopback 0
   ```
   ```
   [*SPE1-bgp] l2vpn-family evpn
   ```
   ```
   [*SPE1-bgp-af-evpn] undo policy vpn-target
   ```
   ```
   [*SPE1-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*SPE1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*SPE1-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*SPE1-bgp-af-evpn] quit
   ```
   ```
   [*SPE1-bgp] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   The configuration of SPE2 is similar to the configuration of SPE1. For configuration details, see [Configuration Files](#EN-US_TASK_0172362308__section_05) in this section.
   
   # Configure the NPE.
   
   ```
   [~NPE] bgp 20
   ```
   ```
   [~NPE-bgp] router-id 4.4.4.4
   ```
   ```
   [*NPE-bgp] peer 2.2.2.2 as-number 20
   ```
   ```
   [*NPE-bgp] peer 2.2.2.2 connect-interface loopback 0
   ```
   ```
   [*NPE-bgp] peer 3.3.3.3 as-number 20
   ```
   ```
   [*NPE-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*NPE-bgp] l2vpn-family evpn
   ```
   ```
   [*NPE-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*NPE-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*NPE-bgp-af-evpn] quit
   ```
   ```
   [*NPE-bgp] quit
   ```
   ```
   [*NPE] commit
   ```
6. Configure the SPEs as RRs and specify the UPE and NPE as RR clients.
   
   
   
   # Configure SPE1.
   
   ```
   [~SPE1] bgp 20
   ```
   ```
   [~SPE1-bgp] l2vpn-family evpn
   ```
   ```
   [~SPE1-bgp-af-evpn] peer 1.1.1.1 reflect-client
   ```
   ```
   [*SPE1-bgp-af-evpn] peer 1.1.1.1 next-hop-local
   ```
   ```
   [*SPE1-bgp-af-evpn] peer 4.4.4.4 next-hop-local
   ```
   ```
   [*SPE1-bgp-af-evpn] quit
   ```
   ```
   [*SPE1-bgp] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   The configuration of SPE2 is similar to the configuration of SPE1. For configuration details, see [Configuration Files](#EN-US_TASK_0172362308__section_05) in this section.
7. Apply the tunnel policy to the VPN instance on the UPE and configure a tunnel selector on each SPE (because SPEs do not have VPN instances), so that the UPE and SPEs use RSVP-TE tunnels to transmit traffic.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] ip vpn-instance vpna
   ```
   ```
   [~UPE-vpn-instance-vpna] ipv4-family
   ```
   ```
   [~UPE-vpn-instance-vpna-af-ipv4] route-distinguisher 20:1
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] tnl-policy policy1 evpn
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*UPE-vpn-instance-vpna] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure SPE1.
   
   ```
   [~SPE1] tunnel-selector bindTE permit node 10
   ```
   ```
   [*SPE1-tunnel-selector] apply tunnel-policy policy1
   ```
   ```
   [*SPE1-tunnel-selector] quit
   ```
   ```
   [*SPE1] bgp 20
   ```
   ```
   [*SPE1-bgp] l2vpn-family evpn
   ```
   ```
   [*SPE1-bgp-af-evpn] tunnel-selector bindTE
   ```
   ```
   [*SPE1-bgp-af-evpn] quit
   ```
   ```
   [*SPE1-bgp] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   The configuration of SPE2 is similar to the configuration of SPE1. For configuration details, see [Configuration Files](#EN-US_TASK_0172362308__section_05) in this section.
8. Configure VPN FRR on the UPE and EVPN FRR on the SPEs (because SPEs do not have VPN instances).
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] bgp 20
   ```
   ```
   [~UPE-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [~UPE-bgp-vpna] auto-frr
   ```
   ```
   [*UPE-bgp-vpna] quit
   ```
   ```
   [*UPE-bgp] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure SPE1. Configure EVPN FRR on the SPE (VPN FRR cannot be configured on SPEs, because SPEs do not have VPN instances).
   
   ```
   [~SPE1] bgp 20
   ```
   ```
   [~SPE1-bgp] l2vpn-family evpn
   ```
   ```
   [~SPE1-bgp-af-evpn] bestroute nexthop-resolved tunnel
   ```
   ```
   [*SPE1-bgp-af-evpn] auto-frr
   ```
   ```
   [*SPE1-bgp-af-evpn] quit
   ```
   ```
   [*SPE1-bgp] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   The configuration of SPE2 is similar to the configuration of SPE1. For configuration details, see [Configuration Files](#EN-US_TASK_0172362308__section_05) in this section.
9. Configure bit-error-triggered RSVP-TE tunnel switching.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] interface Tunnel 11
   ```
   ```
   [~UPE-Tunnel11] mpls te bit-error-detection
   ```
   ```
   [*UPE-Tunnel11] mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 2.2.2.2 tunnel-id 20
   ```
   ```
   [*UPE-Tunnel11] quit
   ```
   ```
   [*UPE] interface Tunnel 12
   ```
   ```
   [*UPE-Tunnel12] mpls te bit-error-detection
   ```
   ```
   [*UPE-Tunnel12] mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 3.3.3.3 tunnel-id 200
   ```
   ```
   [*UPE-Tunnel12] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure SPE1.
   
   ```
   [~SPE1] interface Tunnel 11
   ```
   ```
   [~SPE1-Tunnel11] mpls te bit-error-detection
   ```
   ```
   [*SPE1-Tunnel11] mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 1.1.1.1 tunnel-id 20
   ```
   ```
   [*SPE1-Tunnel11] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   # Configure SPE2.
   
   ```
   [~SPE2] interface Tunnel 12
   ```
   ```
   [~SPE2-Tunnel12] mpls te bit-error-detection
   ```
   ```
   [*SPE2-Tunnel12] mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 1.1.1.1 tunnel-id 200
   ```
   ```
   [*SPE2-Tunnel12] quit
   ```
   ```
   [*SPE2] commit
   ```
10. Configure bit-error-triggered EVPN L3VPN route switching.
    
    
    
    # Configure the UPE to reroute traffic when a bit error event occurs.
    
    ```
    [~UPE] bgp 20
    ```
    ```
    [~UPE-bgp] ipv4-family vpn-instance vpna
    ```
    ```
    [~UPE-bgp-vpna] bestroute bit-error-detection
    ```
    ```
    [*UPE-bgp-vpna] quit
    ```
    ```
    [*UPE-bgp] quit
    ```
    ```
    [*UPE] commit
    ```
    
    # Configure SPE1 to decrease the local preference of the EVPN routes that it advertises to the NPE by 50 when a bit error event occurs.
    
    ```
    [~SPE1] bgp 20
    ```
    ```
    [~SPE1-bgp] l2vpn-family evpn
    ```
    ```
    [~SPE1-bgp-af-evpn] nexthop recursive-lookup bit-error-detection local-preference - 50
    ```
    ```
    [*SPE1-bgp-af-evpn] quit
    ```
    ```
    [*SPE1-bgp] quit
    ```
    ```
    [*SPE1] commit
    ```
11. Verify the configuration.
    
    
    
    # Run the **display bgp vpnv4 vpn-instance vpna routing-table** command on the UPE and NPE. The command output shows that the UPE and NPE have both received remote EVPN routes from SPE1 and SPE2 and they have preferentially selected the routes advertised by SPE1.
    
    ```
    [~UPE] display bgp vpnv4 vpn-instance vpna routing-table
    ```
    ```
     BGP Local router ID is 1.1.1.1
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
     RPKI validation codes: V - valid, I - invalid, N - not-found
    
        
     VPN-Instance vpna, Router ID 1.1.1.1:
    
     Total Number of Routes: 5
            Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
    
     *>     10.2.1.0/24        0.0.0.0                        0                     0       ?
     *>     10.2.1.1/32        0.0.0.0                        0                     0       ?
     *>i    10.3.1.0/24        2.2.2.2                        0          100        0       ?
     * i                       3.3.3.3                        0          100        0       ?
     *>     127.0.0.0/8        0.0.0.0                        0                     0       ?
    ```
    ```
    [~NPE] display bgp evpn all routing-table
    ```
    ```
     BGP Local router ID is 4.4.4.4
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
     RPKI validation codes: V - valid, I - invalid, N - not-found
    
        
     VPN-Instance vpna, Router ID 4.4.4.4:
    
     Total Number of Routes: 5
            Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
    
     *>i    10.2.1.0/24        2.2.2.2                        0          100        0       ?
     * i                       3.3.3.3                        0          100        0       ?
     *>     10.3.1.0/24        0.0.0.0                        0                     0       ?
     *>     10.3.1.1/32        0.0.0.0                        0                     0       ?
     *>     127.0.0.0/8        0.0.0.0                        0                     0       ?
    ```
    
    If GE0/1/1 on the UPE and GE0/1/2 on SPE2 both encounter a bit error event, the primary and backup CR-LSPs of the RSVP-TE tunnel that carries the primary VPN route both enter the excessive BER state. As a result, bit-error-triggered RSVP-TE tunnel switching cannot protect services against bit errors. In this situation, the UPE reroutes traffic. SPE1 decreases the local preference of the EVPNv4 routes that it advertises to the NPE by 50 after detecting the bit error event, so that the NPE preferentially selects the EVPNv4 routes advertised by SPE2.
    
    # Run the **display bgp vpnv4 vpn-instance vpna routing-table 10.3.1.0** command on the UPE. The command output shows that the UPE preferentially selects the route advertised by SPE2. The route advertised by SPE1 is not preferentially selected because of **nexthop bit error**.
    
    ```
    [~UPE] display bgp vpnv4 vpn-instance vpna routing-table 10.3.1.0
    ```
    ```
     
     BGP local router ID : 1.1.1.1
     Local AS number : 20
        
     VPN-Instance vpna, Router ID 1.1.1.1:
     Paths:   2 available, 1 best, 1 select, 0 best-external, 0 add-path
     BGP routing table entry information of 10.3.1.0/24:
     Route Distinguisher: 20:1
     Evpn route: Type 5, ip-prefix
     Label information (Received/Applied): 48128/NULL
     From: 3.3.3.3 (3.3.3.3)  
     Route Duration: 0d01h46m34s
     Relay Tunnel Out-Interface: Tunnel12
     Original nexthop: 3.3.3.3
     Qos information : 0x0
     Ext-Community: RT <1 : 1>
     AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
     Originator: 4.4.4.4
     Cluster list: 3.3.3.3
     Not advertised to any peer yet
    
     BGP routing table entry information of 10.3.1.0/24:
     Route Distinguisher: 20:1
     Evpn route: Type 5, ip-prefix
     Label information (Received/Applied): 48129/NULL
     From: 2.2.2.2 (2.2.2.2)  
     Route Duration: 0d02h37m41s
     Relay Tunnel Out-Interface: Tunnel11
     Original nexthop: 2.2.2.2
     Qos information : 0x0
     Ext-Community: RT <1 : 1>
     AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, backup, pre 255, not preferred for nexthop bit error
     Originator: 4.4.4.4
     Cluster list: 2.2.2.2
     Not advertised to any peer yet
    ```
    
    # Run the **display bgp vpnv4 vpn-instance vpna routing-table 10.2.1.0** command on the NPE. The command output shows that the NPE preferentially selects the route advertised by SPE2. The route advertised by SPE1 is not preferentially selected because of **Local\_Pref**.
    
    ```
    [~NPE] display bgp vpnv4 vpn-instance vpna routing-table 10.2.1.0
    ```
    ```
     BGP local router ID : 4.4.4.4
     Local AS number : 20
        
     VPN-Instance vpna, Router ID 4.4.4.4:
     Paths:   2 available, 1 best, 1 select, 0 best-external, 0 add-path
     BGP routing table entry information of 10.2.1.0/24:
     Route Distinguisher: 20:1
     Evpn route: Type 5, ip-prefix
     Label information (Received/Applied): 48125/NULL
     From: 3.3.3.3 (3.3.3.3)  
     Route Duration: 0d00h02m15s
     Relay Tunnel Out-Interface: Ethernet0/1/0
     Original nexthop: 3.3.3.3
     Qos information : 0x0
     Ext-Community: RT <1 : 1>
     AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10
     Originator: 1.1.1.1
     Cluster list: 3.3.3.3
     Not advertised to any peer yet
    
     BGP routing table entry information of 10.2.1.0/24:
     Route Distinguisher: 20:1
     Evpn route: Type 5, ip-prefix
     Label information (Received/Applied): 48128/NULL
     From: 2.2.2.2 (2.2.2.2)  
     Route Duration: 0d00h02m15s
     Relay Tunnel Out-Interface: Ethernet0/1/7
     Original nexthop: 2.2.2.2
     Qos information : 0x0
     Ext-Community: RT <1 : 1>
     AS-path Nil, origin incomplete, MED 0, localpref 50, pref-val 0, valid, internal, pre 255, IGP cost 10, not preferred for Local_Pref
     Originator: 1.1.1.1
     Cluster list: 2.2.2.2
     Not advertised to any peer yet
    ```

#### Configuration Files

* UPE configuration file
  
  ```
  #
  sysname UPE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 20:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy policy1 evpn
    evpn mpls routing-enable
  #               
  bfd
   mpls-passive
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   label advertise non-null
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  interface Tunnel11
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te record-route
   mpls te backup hot-standby
   mpls te reserved-for-binding
   mpls te bit-error-detection
   mpls te bit-error-detection threshold switch 3 4 resume 2 5
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 2.2.2.2 tunnel-id 20
   mpls te tunnel-id 20
   mpls te bfd enable
  #
  interface Tunnel12
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te record-route
   mpls te backup hot-standby
   mpls te reserved-for-binding
   mpls te bit-error-detection
   mpls te bit-error-detection threshold switch 3 4 resume 2 5
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 3.3.3.3 tunnel-id 200
   mpls te tunnel-id 200
   mpls te bfd enable
  #
  bgp 20
   router-id 1.1.1.1
   peer 2.2.2.2 as-number 20
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 20
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance vpna
    bestroute bit-error-detection
    import-route direct
    auto-frr
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    mpls-te enable
  #
  tunnel-policy policy1
   tunnel binding destination 2.2.2.2 te Tunnel 11
   tunnel binding destination 3.3.3.3 te Tunnel 12
  #
  return
  ```
* SPE1 configuration file
  
  ```
  #
  sysname SPE1
  #
  tunnel-selector bindTE permit node 10
   apply tunnel-policy policy1
  #
  bfd
   mpls-passive
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   label advertise non-null
   mpls te        
   mpls rsvp-te
   mpls te cspf
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0021.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  interface Tunnel11
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te record-route
   mpls te backup hot-standby
   mpls te reserved-for-binding
   mpls te bit-error-detection
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 1.1.1.1 tunnel-id 20
   mpls te tunnel-id 20
   mpls te bfd enable
  #
  bgp 20
   router-id 2.2.2.2
   peer 1.1.1.1 as-number 20
   peer 1.1.1.1 connect-interface LoopBack0
   peer 3.3.3.3 as-number 20
   peer 3.3.3.3 connect-interface LoopBack0
   peer 4.4.4.4 as-number 20
   peer 4.4.4.4 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    auto-frr
    nexthop recursive-lookup bit-error-detection local-preference - 50
    tunnel-selector bindTE  
    bestroute nexthop-resolved tunnel
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 1.1.1.1 next-hop-local
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
    peer 4.4.4.4 next-hop-local
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0   
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
    mpls-te enable
  #               
  tunnel-policy policy1
   tunnel binding destination 1.1.1.1 te Tunnel 11
  #
  return#
  ```
* SPE2 configuration file
  
  ```
  #
  sysname SPE2
  #
  tunnel-selector bindTE permit node 10
   apply tunnel-policy policy1
  #
  bfd
   mpls-passive
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   label advertise non-null
   mpls te        
   mpls rsvp-te
   mpls te cspf
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0022.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.5.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #               
  interface Tunnel12
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te record-route
   mpls te backup hot-standby
   mpls te reserved-for-binding
   mpls te bit-error-detection
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 1.1.1.1 tunnel-id 200
   mpls te tunnel-id 200
   mpls te bfd enable
  #
  bgp 20
   router-id 3.3.3.3
   peer 1.1.1.1 as-number 20
   peer 1.1.1.1 connect-interface LoopBack0
   peer 2.2.2.2 as-number 20
   peer 2.2.2.2 connect-interface LoopBack0
   peer 4.4.4.4 as-number 20
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
    auto-frr
    tunnel-selector bindTE  
    bestroute nexthop-resolved tunnel
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 1.1.1.1 next-hop-local
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
    peer 4.4.4.4 next-hop-local
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
    mpls-te enable
  #
  ssh authorization-type default aaa
  #
  tunnel-policy policy1
   tunnel binding destination 1.1.1.1 te Tunnel 12
  #
  return
  ```
* NPE configuration file
  
  ```
  #
  sysname NPE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 20:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #               
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.5.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.3.1.1 255.255.255.0
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
   isis enable 1
  #
  bgp 20
   router-id 4.4.4.4
   peer 2.2.2.2 as-number 20
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 20
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  #
  return
  ```