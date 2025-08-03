Example for Configuring the IPv4 NFVI Distributed Gateway Function (Segmented SR Tunnels)
=========================================================================================

This section provides an example for configuring the IPv4 NFVI distributed gateway function to carry service traffic over segmented SR tunnels.

#### Networking Requirements

The NFVI telco cloud solution uses the DCI + DCN networking. A large amount of IPv4 UE traffic is sent to vUGWs and vMSEs on the DCN. After being processed by the vUGWs and vMSEs, the UE traffic is forwarded over the DCN to destination devices on the Internet. The destination devices send traffic to UEs in similar ways. To meet the preceding requirements and ensure that the UE traffic is load-balanced within the DCN, you need to deploy the NFVI distributed gateway function on DCN devices.

[Figure 1](#EN-US_TASK_0172370673__fig1559717412288) shows NFVI distributed gateway networking (segmented SR tunnels). DC GWs, which are the border gateways of the DCN, exchange Internet routes with external devices through PEs. L2GW/L3GW1 and L2GW/L3GW2 connect to VNFs. VNF1 and VNF2 that function as virtualized NEs are deployed to implement the vUGW and vMSE functions, respectively. VNF1 and VNF2 each connect to L2GW/L3GW1 and L2GW/L3GW2 through IPUs. SR tunnels are established between PEs and DC GWs and between DC GWs and L2GWs/L3GWs to carry IPv4 service traffic.

**Figure 1** Configuring IPv4 NFVI distributed gateways (segmented SR tunnels)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 6 in this example represent GigabitEthernet0/1/1, GigabitEthernet0/1/2, GigabitEthernet0/1/3, GigabitEthernet0/1/4, GigabitEthernet0/1/5, and GigabitEthernet0/1/6, respectively.


  
![](figure/en-us_image_0000001364238173.png)  

**Table 1** IP address planning
| Device | Interface | IP Address |
| --- | --- | --- |
| PE1 | GigabitEthernet 0/1/1 | 10.6.7.1/24 |
| GigabitEthernet 0/1/2 | 10.6.5.2/24 |
| GigabitEthernet 0/1/3 | 10.7.1.1/24 |
| LoopBack1 | 7.7.7.7 |
| PE2 | GigabitEthernet 0/1/1 | 10.6.7.2/24 |
| GigabitEthernet 0/1/2 | 10.6.6.2/24 |
| GigabitEthernet 0/1/3 | 10.8.1.1/24 |
| LoopBack1 | 8.8.8.8 |
| DCGW1 | GigabitEthernet 0/1/1 | 10.6.1.1/24 |
| GigabitEthernet 0/1/2 | 10.6.2.1/24 |
| GigabitEthernet 0/1/3 | 10.6.5.1/24 |
| LoopBack1 | 3.3.3.3/32 |
| LoopBack2 | 33.33.33.33/32 |
| DCGW2 | GigabitEthernet 0/1/1 | 10.6.1.2/24 |
| GigabitEthernet 0/1/2 | 10.6.3.1/24 |
| GigabitEthernet 0/1/3 | 10.6.6.1/24 |
| LoopBack1 | 4.4.4.4/32 |
| LoopBack2 | 44.44.44.44/32 |
| L2GW/L3GW1 | GigabitEthernet 0/1/1 | 10.6.4.1/24 |
| GigabitEthernet 0/1/2 | 10.6.2.2/24 |
| GigabitEthernet 0/1/3 | - |
| GigabitEthernet 0/1/4 | - |
| GigabitEthernet 0/1/5 | - |
| GigabitEthernet 0/1/6 | - |
| LoopBack1 | 1.1.1.1/32 |
| L2GW/L3GW2 | GigabitEthernet 0/1/1 | 10.6.4.2/24 |
| GigabitEthernet 0/1/2 | 10.6.3.2/24 |
| GigabitEthernet 0/1/3 | - |
| GigabitEthernet 0/1/4 | - |
| GigabitEthernet 0/1/5 | - |
| GigabitEthernet 0/1/6 | - |
| LoopBack1 | 2.2.2.2/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol for the PEs, DC GWs, and L2GWs/L3GWs to communicate at Layer 3 within each AS.
2. Establish EBGP peer relationships between PEs and DC GWs and IBGP peer relationships between DC GWs and L2GWs/L3GWs.
3. Configure SR-MPLS TE tunnels between PEs and DC GWs and between DC GWs and L2GWs/L3GWs.
4. Configure EVPN instances on DC GWs and L2GWs/L3GWs and bind BDs to these EVPN instances.
5. Configure L3VPN instances on DC GWs and L2GWs/L3GWs and bind VBDIF interfaces to these L3VPN instances.
6. Configure a tunnel policy on PEs, DC GWs, and L2GWs/L3GWs.
7. Configure BGP EVPN on DC GWs and L2GWs/L3GWs.
8. Configure BGP VPNv4 on DC GWs and PEs.
9. Configure Layer 2 sub-interfaces on DC GWs and L2GWs/L3GWs and configure the static VPN routes destined for VNFs on L2GWs/L3GWs.
10. Configure L2GWs/L3GWs to import static VPN routes through BGP EVPN. Configure and apply a route-policy for L3VPN instances so that the static VPN routes can retain the original next hops.
11. Configure static default VPN routes and loopback addresses on DC GWs. The loopback addresses are used to establish BGP VPN peer relationships with VNFs. Configure and apply a route-policy for L3VPN instances so that DC GWs can advertise static default VPN routes and VPN loopback routes only through BGP EVPN.
12. Establish BGP VPN peer relationships between DC GWs and VNFs.
13. Configure load balancing on PEs, DC GWs, and L2GWs/L3GWs.

#### Procedure

1. Configure IP addresses for all interfaces, including loopback interfaces, on PEs, DC GWs, and L2GWs/L3GWs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
2. Configure a routing protocol between PEs, DC GWs, and L2GWs/L3GWs to ensure Layer 3 connectivity within each AS.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
3. Establish EBGP peer relationships between PEs and DC GWs and IBGP peer relationships between DC GWs and L2GWs/L3GWs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
4. Configure SR-MPLS TE tunnels between PEs and L2GWs/L3GWs and between DC GWs and L2GWs/L3GWs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
5. Configure EVPN instances on DC GWs and L2GWs/L3GWs and bind BDs to these EVPN instances.
   
   
   
   # Configure DC-GW1.
   
   ```
   [~DCGW1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*DCGW1-evpn-instance-evrf1] route-distinguisher 1:1
   ```
   ```
   [*DCGW1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*DCGW1-evpn-instance-evrf1] quit
   ```
   ```
   [*DCGW1] evpn vpn-instance evrf2 bd-mode
   ```
   ```
   [*DCGW1-evpn-instance-evrf2] route-distinguisher 2:2
   ```
   ```
   [*DCGW1-evpn-instance-evrf2] vpn-target 2:2
   ```
   ```
   [*DCGW1-evpn-instance-evrf2] quit
   ```
   ```
   [*DCGW1] evpn vpn-instance evrf3 bd-mode
   ```
   ```
   [*DCGW1-evpn-instance-evrf3] route-distinguisher 3:3
   ```
   ```
   [*DCGW1-evpn-instance-evrf3] vpn-target 3:3
   ```
   ```
   [*DCGW1-evpn-instance-evrf3] quit
   ```
   ```
   [*DCGW1] evpn vpn-instance evrf4 bd-mode
   ```
   ```
   [*DCGW1-evpn-instance-evrf4] route-distinguisher 4:4
   ```
   ```
   [*DCGW1-evpn-instance-evrf4] vpn-target 4:4
   ```
   ```
   [*DCGW1-evpn-instance-evrf4] quit
   ```
   ```
   [*DCGW1] bridge-domain 10
   ```
   ```
   [*DCGW1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*DCGW1-bd10] quit
   ```
   ```
   [*DCGW1] bridge-domain 20
   ```
   ```
   [*DCGW1-bd20] evpn binding vpn-instance evrf2
   ```
   ```
   [*DCGW1-bd20] quit
   ```
   ```
   [*DCGW1] bridge-domain 30
   ```
   ```
   [*DCGW1-bd30] evpn binding vpn-instance evrf3
   ```
   ```
   [*DCGW1-bd30] quit
   ```
   ```
   [*DCGW1] bridge-domain 40
   ```
   ```
   [*DCGW1-bd40] evpn binding vpn-instance evrf4
   ```
   ```
   [*DCGW1-bd40] quit
   ```
   ```
   [*DCGW1] commit
   ```
   
   The configurations of DC-GW2 and L2GWs/L3GWs are similar to that of DC-GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
6. Configure L3VPN instances on DC GWs and L2GWs/L3GWs.
   
   
   
   # Configure DC-GW1.
   
   ```
   [~DCGW1] ip vpn-instance vpn1
   ```
   ```
   [*DCGW1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*DCGW1-vpn-instance-vpn1-af-ipv4] route-distinguisher 33:33
   ```
   ```
   [*DCGW1-vpn-instance-vpn1-af-ipv4] vpn-target 11:1 evpn
   ```
   ```
   [*DCGW1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*DCGW1-vpn-instance-vpn1] evpn mpls routing-enable
   ```
   ```
   [*DCGW1-vpn-instance-vpn1] quit
   ```
   ```
   [*DCGW1] interface vbdif10
   ```
   ```
   [*DCGW1-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*DCGW1-Vbdif10] ip address 10.1.1.1 24
   ```
   ```
   [*DCGW1-Vbdif10] arp generate-rd-table enable
   ```
   ```
   [*DCGW1-Vbdif10] anycast-gateway enable
   ```
   ```
   [*DCGW1-Vbdif10] mac-address 00e0-fc00-0003
   ```
   ```
   [*DCGW1-Vbdif10] quit
   ```
   ```
   [*DCGW1] interface vbdif20
   ```
   ```
   [*DCGW1-Vbdif20] ip binding vpn-instance vpn1
   ```
   ```
   [*DCGW1-Vbdif20] ip address 10.2.1.1 24
   ```
   ```
   [*DCGW1-Vbdif20] arp generate-rd-table enable
   ```
   ```
   [*DCGW1-Vbdif20] anycast-gateway enable
   ```
   ```
   [*DCGW1-Vbdif20] mac-address 00e0-fc00-0004
   ```
   ```
   [*DCGW1-Vbdif20] quit
   ```
   ```
   [*DCGW1] interface vbdif30
   ```
   ```
   [*DCGW1-Vbdif30] ip binding vpn-instance vpn1
   ```
   ```
   [*DCGW1-Vbdif30] ip address 10.3.1.1 24
   ```
   ```
   [*DCGW1-Vbdif30] arp generate-rd-table enable
   ```
   ```
   [*DCGW1-Vbdif30] anycast-gateway enable
   ```
   ```
   [*DCGW1-Vbdif30] mac-address 00e0-fc00-0001
   ```
   ```
   [*DCGW1-Vbdif30] quit
   ```
   ```
   [*DCGW1] interface vbdif40
   ```
   ```
   [*DCGW1-Vbdif40] ip binding vpn-instance vpn1
   ```
   ```
   [*DCGW1-Vbdif40] ip address 10.4.1.1 24
   ```
   ```
   [*DCGW1-Vbdif40] arp generate-rd-table enable
   ```
   ```
   [*DCGW1-Vbdif40] anycast-gateway enable
   ```
   ```
   [*DCGW1-Vbdif40] mac-address 00e0-fc00-0005
   ```
   ```
   [*DCGW1-Vbdif40] quit
   ```
   ```
   [*DCGW1] commit
   ```
   
   The configuration of DC-GW2 is similar to that of DC-GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
   
   # Configure L2GW/L3GW1.
   
   ```
   [~L2GW/L3GW1] ip vpn-instance vpn1
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1-af-ipv4] route-distinguisher 11:11
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1-af-ipv4] vpn-target 11:1 evpn
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1] evpn mpls routing-enable
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1] quit
   ```
   ```
   [*L2GW/L3GW1] interface vbdif10
   ```
   ```
   [*L2GW/L3GW1-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*L2GW/L3GW1-Vbdif10] ip address 10.1.1.1 24
   ```
   ```
   [*L2GW/L3GW1-Vbdif10] arp generate-rd-table enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif10] anycast-gateway enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif10] mac-address 00e0-fc00-0003
   ```
   ```
   [*L2GW/L3GW1-Vbdif10] arp collect host enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif10] quit
   ```
   ```
   [*L2GW/L3GW1] interface vbdif20
   ```
   ```
   [*L2GW/L3GW1-Vbdif20] ip binding vpn-instance vpn1
   ```
   ```
   [*L2GW/L3GW1-Vbdif20] ip address 10.2.1.1 24
   ```
   ```
   [*L2GW/L3GW1-Vbdif20] arp generate-rd-table enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif20] anycast-gateway enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif20] mac-address 00e0-fc00-0004
   ```
   ```
   [*L2GW/L3GW1-Vbdif20] arp collect host enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif20] quit
   ```
   ```
   [*L2GW/L3GW1] interface vbdif30
   ```
   ```
   [*L2GW/L3GW1-Vbdif30] ip binding vpn-instance vpn1
   ```
   ```
   [*L2GW/L3GW1-Vbdif30] ip address 10.3.1.1 24
   ```
   ```
   [*L2GW/L3GW1-Vbdif30] arp generate-rd-table enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif30] anycast-gateway enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif30] mac-address 00e0-fc00-0001
   ```
   ```
   [*L2GW/L3GW1-Vbdif30] arp collect host enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif30] quit
   ```
   ```
   [*L2GW/L3GW1] interface vbdif40
   ```
   ```
   [*L2GW/L3GW1-Vbdif40] ip binding vpn-instance vpn1
   ```
   ```
   [*L2GW/L3GW1-Vbdif40] ip address 10.4.1.1 24
   ```
   ```
   [*L2GW/L3GW1-Vbdif40] arp generate-rd-table enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif40] anycast-gateway enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif40] mac-address 00e0-fc00-0005
   ```
   ```
   [*L2GW/L3GW1-Vbdif40] arp collect host enable
   ```
   ```
   [*L2GW/L3GW1-Vbdif40] quit
   ```
   ```
   [*L2GW/L3GW1] commit
   ```
   
   The configuration of L2GW/L3GW2 is similar to that of L2GW/L3GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
7. Configure a tunnel policy on PEs, DC GWs, and L2GWs/L3GWs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] tunnel-policy srte
   ```
   ```
   [*PE1-tunnel-policy-srte] tunnel select-seq sr-te load-balance-number 3
   ```
   ```
   [*PE1-tunnel-policy-srte] quit
   ```
   ```
   [*PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] tnl-policy srte
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration of PE2 is similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
   
   # Configure DC-GW1.
   
   ```
   [~DCGW1] tunnel-policy srte
   ```
   ```
   [*DCGW1-tunnel-policy-srte] tunnel select-seq sr-te load-balance-number 3
   ```
   ```
   [*DCGW1-tunnel-policy-srte] quit
   ```
   ```
   [*DCGW1] ip vpn-instance vpn1
   ```
   ```
   [*DCGW1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*DCGW1-vpn-instance-vpn1-af-ipv4] tnl-policy srte evpn
   ```
   ```
   [*DCGW1-vpn-instance-vpn1-af-ipv4] tnl-policy srte
   ```
   ```
   [*DCGW1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*DCGW1-vpn-instance-vpn1] quit
   ```
   ```
   [*DCGW1] commit
   ```
   
   The configuration of DC-GW2 is similar to that of DC-GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
   
   # Configure L2GW/L3GW1.
   
   ```
   [~L2GW/L3GW1] tunnel-policy srte
   ```
   ```
   [*L2GW/L3GW1-tunnel-policy-srte] tunnel select-seq sr-te load-balance-number 3
   ```
   ```
   [*L2GW/L3GW1-tunnel-policy-srte] quit
   ```
   ```
   [*L2GW/L3GW1] ip vpn-instance vpn1
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1-af-ipv4] tnl-policy srte evpn
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*L2GW/L3GW1-vpn-instance-vpn1] quit
   ```
   ```
   [*L2GW/L3GW1] commit
   ```
   
   The configuration of L2GW/L3GW2 is similar to that of L2GW/L3GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
8. Configure BGP EVPN on DC GWs and L2GWs/L3GWs.
   
   
   
   # Configure DC-GW1.
   
   ```
   [~DCGW1] ip ip-prefix uIP index 10 permit 10.10.10.10 32
   ```
   ```
   [*DCGW1] route-policy stopuIP deny node 10
   ```
   ```
   [*DCGW1-route-policy] if-match ip-prefix uIP
   ```
   ```
   [*DCGW1-route-policy] quit
   ```
   ```
   [*DCGW1] route-policy stopuIP permit node 20
   ```
   ```
   [*DCGW1-route-policy] quit
   ```
   ```
   [*DCGW1] bgp 100
   ```
   ```
   [*DCGW1-bgp] l2vpn-family evpn
   ```
   ```
   [*DCGW1-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*DCGW1-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*DCGW1-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*DCGW1-bgp-af-evpn] peer 4.4.4.4 route-policy stopuIP export
   ```
   ```
   [*DCGW1-bgp-af-evpn] quit
   ```
   ```
   [*DCGW1-bgp] quit
   ```
   ```
   [*DCGW1] commit
   ```
   
   The configuration of DC-GW2 is similar to that of DC-GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
   
   # Configure L2GW/L3GW1.
   
   ```
   [~L2GW/L3GW1] bgp 100
   ```
   ```
   [*L2GW/L3GW1-bgp] l2vpn-family evpn
   ```
   ```
   [*L2GW/L3GW1-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*L2GW/L3GW1-bgp-af-evpn] peer 2.2.2.2 advertise arp
   ```
   ```
   [*L2GW/L3GW1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*L2GW/L3GW1-bgp-af-evpn] peer 3.3.3.3 advertise arp
   ```
   ```
   [*L2GW/L3GW1-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*L2GW/L3GW1-bgp-af-evpn] peer 4.4.4.4 advertise arp
   ```
   ```
   [*L2GW/L3GW1-bgp-af-evpn] quit
   ```
   ```
   [*L2GW/L3GW1-bgp] quit
   ```
   ```
   [*L2GW/L3GW1] evpn source-address 1.1.1.1
   ```
   ```
   [*L2GW/L3GW1] evpn
   ```
   ```
   [*L2GW/L3GW1-evpn] vlan-extend private enable
   ```
   ```
   [*L2GW/L3GW1-evpn] vlan-extend redirect enable
   ```
   ```
   [*L2GW/L3GW1-evpn] local-remote frr enable
   ```
   ```
   [*L2GW/L3GW1-evpn] quit
   ```
   ```
   [*L2GW/L3GW1] commit
   ```
   
   The configuration of L2GW/L3GW2 is similar to that of L2GW/L3GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
9. Configure BGP VPNv4 on DC GWs and PEs.
   
   
   
   # Configure DC-GW1.
   
   ```
   [~DCGW1] ip vpn-instance vpn1
   ```
   ```
   [~DCGW1-vpn-instance-vpn1] vpn-target 10:1
   ```
   ```
   [*DCGW1-vpn-instance-vpn1] quit
   ```
   ```
   [*DCGW1] bgp 100
   ```
   ```
   [*DCGW1-bgp] ipv4-family vpnv4
   ```
   ```
   [*DCGW1-bgp-af-vpnv4] peer 7.7.7.7 enable
   ```
   ```
   [*DCGW1-bgp-af-vpnv4] peer 8.8.8.8 enable
   ```
   ```
   [*DCGW1-bgp-af-vpnv4] quit
   ```
   ```
   [*DCGW1-bgp] quit
   ```
   ```
   [*DCGW1] commit
   ```
   
   The configuration of DC-GW2 is similar to that of DC-GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 77:77
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] vpn-target 10:1
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] interface GigabitEthernet0/1/3
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] ip address 10.7.1.1 255.255.255.0
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] quit
   ```
   ```
   [*PE1] bgp 200
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 4.4.4.4 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] import-route direct
   ```
   ```
   [*PE1-bgp-vpn1] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration of PE2 is similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
10. Configure Layer 2 sub-interfaces on DC GWs and L2GWs/L3GWs and configure the static VPN routes destined for VNFs on L2GWs/L3GWs.
    
    # Configure DC-GW1.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In this example, a sub-interface of the physical interface of DC-GW1 is bound to a BD to ensure that the VBDIF interface is up. In actual situations, bind service-irrelevant interfaces to BDs to ensure network reliability.
    
    
    ```
    [~DCGW1] interface GigabitEthernet0/1/2.1 mode l2
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/2.1] encapsulation dot1q vid 10
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/2.1] rewrite pop single
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/2.1] bridge-domain 10
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/2.1] quit
    ```
    ```
    [*DCGW1] interface GigabitEthernet0/1/2.2 mode l2
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/2.2] encapsulation dot1q vid 30
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/2.2] rewrite pop single
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/2.2] bridge-domain 30
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/2.2] quit
    ```
    ```
    [*DCGW1] interface GigabitEthernet0/1/1.1 mode l2
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/1.1] encapsulation dot1q vid 20
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/1.1] rewrite pop single
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/1.1] bridge-domain 20
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/1.1] quit
    ```
    ```
    [*DCGW1] interface GigabitEthernet0/1/1.2 mode l2
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/1.2] encapsulation dot1q vid 40
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/1.2] rewrite pop single
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/1.2] bridge-domain 40
    ```
    ```
    [*DCGW1-GigabitEthernet0/1/1.2] quit
    ```
    ```
    [*DCGW1] commit
    ```
    
    The configuration of DC-GW2 is similar to that of DC-GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
    
    # Configure L2GW/L3GW1.
    
    ```
    [~L2GW/L3GW1] lacp e-trunk system-id 00e0-fc00-0002
    ```
    ```
    [*L2GW/L3GW1] lacp e-trunk priority 1
    ```
    ```
    [*L2GW/L3GW1] e-trunk 1
    ```
    ```
    [*L2GW/L3GW1-e-trunk-1] peer-address 2.2.2.2 source-address 1.1.1.1
    ```
    ```
    [*L2GW/L3GW1-e-trunk-1] priority 5
    ```
    ```
    [*L2GW/L3GW1-e-trunk-1] quit
    ```
    ```
    [*L2GW/L3GW1] interface Eth-Trunk 10
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk10] mode lacp-static
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk10] e-trunk 1
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk10] e-trunk mode force-master
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk10] esi 0000.1111.1111.1111.1111
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk10] quit
    ```
    ```
    [*L2GW/L3GW1] interface Eth-Trunk 20
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk20] mode lacp-static
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk20] e-trunk 1
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk20] e-trunk mode force-master
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk20] esi 0000.2222.2222.2222.2222
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk20] quit
    ```
    ```
    [*L2GW/L3GW1] interface Eth-Trunk 30
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk30] mode lacp-static
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk30] e-trunk 1
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk30] e-trunk mode force-master
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk30] esi 0000.3333.3333.3333.3333
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk30] quit
    ```
    ```
    [*L2GW/L3GW1] interface Eth-Trunk 40
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk40] mode lacp-static
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk40] e-trunk 1
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk40] e-trunk mode force-master
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk40] esi 0000.4444.4444.4444.4444
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk40] quit
    ```
    ```
    [*L2GW/L3GW1] interface Eth-Trunk 10.1 mode l2
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk10.1] encapsulation dot1q vid 10
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk10.1] rewrite pop single
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk10.1] bridge-domain 10
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk10.1] quit
    ```
    ```
    [*L2GW/L3GW1] interface Eth-Trunk 20.1 mode l2
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk20.1] encapsulation dot1q vid 20
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk20.1] rewrite pop single
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk20.1] bridge-domain 20
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk20.1] quit
    ```
    ```
    [*L2GW/L3GW1] interface Eth-Trunk 30.1 mode l2
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk30.1] encapsulation dot1q vid 30
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk30.1] rewrite pop single
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk30.1] bridge-domain 30
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk30.1] quit
    ```
    ```
    [*L2GW/L3GW1] interface Eth-Trunk 40.1 mode l2
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk40.1] encapsulation dot1q vid 40
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk40.1] rewrite pop single
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk40.1] bridge-domain 40
    ```
    ```
    [*L2GW/L3GW1-Eth-Trunk40.1] quit
    ```
    ```
    [~L2GW/L3GW1] interface GigabitEthernet0/1/3
    ```
    ```
    [*L2GW/L3GW1-GigabitEthernet0/1/3] eth-trunk 10
    ```
    ```
    [*L2GW/L3GW1-GigabitEthernet0/1/3] quit
    ```
    ```
    [*L2GW/L3GW1] interface GigabitEthernet0/1/4
    ```
    ```
    [*L2GW/L3GW1-GigabitEthernet0/1/4] eth-trunk 20
    ```
    ```
    [*L2GW/L3GW1-GigabitEthernet0/1/4] quit
    ```
    ```
    [~L2GW/L3GW1] interface GigabitEthernet0/1/5
    ```
    ```
    [*L2GW/L3GW1-GigabitEthernet0/1/5] eth-trunk 30
    ```
    ```
    [*L2GW/L3GW1-GigabitEthernet0/1/5] quit
    ```
    ```
    [*L2GW/L3GW1] interface GigabitEthernet0/1/6
    ```
    ```
    [*L2GW/L3GW1-GigabitEthernet0/1/6] eth-trunk 40
    ```
    ```
    [*L2GW/L3GW1-GigabitEthernet0/1/6] quit
    ```
    ```
    [*L2GW/L3GW1] ip route-static vpn-instance vpn1 5.5.5.5 255.255.255.255 10.1.1.2 preference 255 tag 1000 inter-protocol-ecmp
    ```
    ```
    [*L2GW/L3GW1] ip route-static vpn-instance vpn1 5.5.5.5 255.255.255.255 10.2.1.2 preference 255 tag 1000 inter-protocol-ecmp
    ```
    ```
    [*L2GW/L3GW1] ip route-static vpn-instance vpn1 6.6.6.6 255.255.255.255 10.3.1.2 preference 255 tag 1000 inter-protocol-ecmp
    ```
    ```
    [*L2GW/L3GW1] ip route-static vpn-instance vpn1 6.6.6.6 255.255.255.255 10.4.1.2 preference 255 tag 1000 inter-protocol-ecmp
    ```
    ```
    [*L2GW/L3GW1] commit
    ```
    
    The configuration of L2GW/L3GW2 is similar to that of L2GW/L3GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
11. Configure L2GWs/L3GWs to import static VPN routes through BGP EVPN. Configure and apply a route-policy for L3VPN instances so that the static VPN routes can retain the original next hops.
    
    
    
    # Configure L2GW/L3GW1.
    
    ```
    [~L2GW/L3GW1] bgp 100
    ```
    ```
    [*L2GW/L3GW1-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*L2GW/L3GW1-bgp-vpn1] import-route static
    ```
    ```
    [*L2GW/L3GW1-bgp-vpn1] advertise l2vpn evpn import-route-multipath
    ```
    ```
    [*L2GW/L3GW1-bgp-vpn1] quit
    ```
    ```
    [*L2GW/L3GW1-bgp] quit
    ```
    ```
    [*L2GW/L3GW1] route-policy sp permit node 10
    ```
    ```
    [*L2GW/L3GW1-route-policy] if-match tag 1000
    ```
    ```
    [*L2GW/L3GW1-route-policy] apply gateway-ip origin-nexthop
    ```
    ```
    [*L2GW/L3GW1-route-policy] quit
    ```
    ```
    [*L2GW/L3GW1] route-policy sp deny node 20
    ```
    ```
    [*L2GW/L3GW1-route-policy] quit
    ```
    ```
    [*L2GW/L3GW1] ip vpn-instance vpn1
    ```
    ```
    [*L2GW/L3GW1-vpn-instance-vpn1] ipv4-family
    ```
    ```
    [*L2GW/L3GW1-vpn-instance-vpn1-ipv4] export route-policy sp evpn
    ```
    ```
    [*L2GW/L3GW1-vpn-instance-vpn1-ipv4] quit
    ```
    ```
    [*L2GW/L3GW1] commit
    ```
    
    The configuration of L2GW/L3GW2 is similar to that of L2GW/L3GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
12. Configure static default VPN routes and loopback addresses on DC GWs. The loopback addresses are used to establish BGP VPN peer relationships with VNFs. Configure and apply a route-policy for L3VPN instances so that DC GWs can advertise static default VPN routes and VPN loopback routes only through BGP EVPN.
    
    
    
    # Configure DC-GW1.
    
    ```
    [~DCGW1] ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0 tag 2000
    ```
    ```
    [*DCGW1] interface LoopBack2
    ```
    ```
    [*DCGW1-LoopBack2] ip binding vpn-instance vpn1
    ```
    ```
    [*DCGW1-LoopBack2] ip address 33.33.33.33 255.255.255.255
    ```
    ```
    [*DCGW1-LoopBack2] quit
    ```
    ```
    [*DCGW1] bgp 100
    ```
    ```
    [*DCGW1-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*DCGW1-bgp-vpn1] advertise l2vpn evpn
    ```
    ```
    [*DCGW1-bgp-vpn1] import-route direct
    ```
    ```
    [*DCGW1-bgp-vpn1] network 0.0.0.0 0
    ```
    ```
    [*DCGW1-bgp-vpn1] quit
    ```
    ```
    [*DCGW1-bgp] quit
    ```
    ```
    [*DCGW1] ip ip-prefix lp index 10 permit 33.33.33.33 32
    ```
    ```
    [*DCGW1] route-policy dp permit node 10
    ```
    ```
    [*DCGW1-route-policy] if-match tag 2000
    ```
    ```
    [*DCGW1-route-policy] quit
    ```
    ```
    [*DCGW1] route-policy dp permit node 15
    ```
    ```
    [*DCGW1-route-policy] if-match ip-prefix lp
    ```
    ```
    [*DCGW1-route-policy] quit
    ```
    ```
    [*DCGW1] ip vpn-instance vpn1
    ```
    ```
    [*DCGW1-vpn-instance-vpn1] ipv4-family
    ```
    ```
    [*DCGW1-vpn-instance-vpn1-af-ipv4] export route-policy dp evpn
    ```
    ```
    [*DCGW1-vpn-instance-vpn1-af-ipv4] quit
    ```
    ```
    [*DCGW1-vpn-instance-vpn1] quit
    ```
    ```
    [*DCGW1] commit
    ```
    
    The configuration of DC-GW2 is similar to that of DC-GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
13. Establish BGP VPN peer relationships between DC GWs and VNFs.
    
    
    
    # Configure DC-GW1.
    
    ```
    [~DCGW1] route-policy p1 deny node 10
    ```
    ```
    [*DCGW1-route-policy] quit
    ```
    ```
    [*DCGW1] bgp 100
    ```
    ```
    [*DCGW1-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*DCGW1-bgp-vpn1] peer 5.5.5.5 as-number 100
    ```
    ```
    [*DCGW1-bgp-vpn1] peer 5.5.5.5 connect-interface LoopBack2
    ```
    ```
    [*DCGW1-bgp-vpn1] peer 5.5.5.5 route-policy p1 export
    ```
    ```
    [*DCGW1-bgp-vpn1] peer 6.6.6.6 as-number 100
    ```
    ```
    [*DCGW1-bgp-vpn1] peer 6.6.6.6 connect-interface LoopBack2
    ```
    ```
    [*DCGW1-bgp-vpn1] peer 6.6.6.6 route-policy p1 export
    ```
    ```
    [*DCGW1-bgp-vpn1] quit
    ```
    ```
    [*DCGW1-bgp] quit
    ```
    ```
    [*DCGW1] commit
    ```
    
    # Configure DC-GW2.
    
    ```
    [~DCGW2] route-policy p1 deny node 10
    ```
    ```
    [*DCGW2-route-policy] quit
    ```
    ```
    [*DCGW2] bgp 100
    ```
    ```
    [*DCGW2-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*DCGW2-bgp-vpn1] peer 5.5.5.5 as-number 100
    ```
    ```
    [*DCGW2-bgp-vpn1] peer 5.5.5.5 connect-interface LoopBack2
    ```
    ```
    [*DCGW2-bgp-vpn1] peer 5.5.5.5 route-policy p1 export
    ```
    ```
    [*DCGW2-bgp-vpn1] peer 6.6.6.6 as-number 100
    ```
    ```
    [*DCGW2-bgp-vpn1] peer 6.6.6.6 connect-interface LoopBack2
    ```
    ```
    [*DCGW2-bgp-vpn1] peer 6.6.6.6 route-policy p1 export
    ```
    ```
    [*DCGW2-bgp-vpn1] quit
    ```
    ```
    [*DCGW2-bgp] quit
    ```
    ```
    [*DCGW2] commit
    ```
14. Configure load balancing on PEs, DC GWs, and L2GWs/L3GWs.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] bgp 200
    ```
    ```
    [*PE1-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*PE1-bgp-vpn1] maximum load-balancing 16
    ```
    ```
    [*PE1-bgp-vpn1] quit
    ```
    ```
    [*PE1-bgp] quit
    ```
    ```
    [*PE1] commit
    ```
    
    The configuration of PE2 is similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
    
    # Configure DC-GW1.
    
    ```
    [~DCGW1] bgp 100
    ```
    ```
    [*DCGW1-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*DCGW1-bgp-vpn1] maximum load-balancing 16
    ```
    ```
    [*DCGW1-bgp-vpn1] quit
    ```
    ```
    [*DCGW1-bgp] l2vpn-family evpn
    ```
    ```
    [*DCGW1-bgp-af-evpn] peer 1.1.1.1 capability-advertise add-path both
    ```
    ```
    [*DCGW1-bgp-af-evpn] peer 1.1.1.1 advertise add-path path-number 16
    ```
    ```
    [*DCGW1-bgp-af-evpn] peer 2.2.2.2 capability-advertise add-path both
    ```
    ```
    [*DCGW1-bgp-af-evpn] peer 2.2.2.2 advertise add-path path-number 16
    ```
    ```
    [*DCGW1-bgp-af-evpn] quit
    ```
    ```
    [*DCGW1-bgp] quit
    ```
    ```
    [*DCGW1] commit
    ```
    
    The configuration of DC-GW2 is similar to that of DC-GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
    
    # Configure L2GW/L3GW1.
    
    ```
    [~L2GW/L3GW1] bgp 100
    ```
    ```
    [*L2GW/L3GW1-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*L2GW/L3GW1-bgp-vpn1] maximum load-balancing 16
    ```
    ```
    [*L2GW/L3GW1-bgp-vpn1] quit
    ```
    ```
    [*L2GW/L3GW1-bgp] l2vpn-family evpn
    ```
    ```
    [*L2GW/L3GW1-bgp-af-evpn] bestroute add-path path-number 16
    ```
    ```
    [*L2GW/L3GW1-bgp-af-evpn] peer 3.3.3.3 capability-advertise add-path both
    ```
    ```
    [*L2GW/L3GW1-bgp-af-evpn] peer 3.3.3.3 advertise add-path path-number 16
    ```
    ```
    [*L2GW/L3GW1-bgp-af-evpn] peer 4.4.4.4 capability-advertise add-path both
    ```
    ```
    [*L2GW/L3GW1-bgp-af-evpn] peer 4.4.4.4 advertise add-path path-number 16
    ```
    ```
    [*L2GW/L3GW1-bgp-af-evpn] quit
    ```
    ```
    [*L2GW/L3GW1-bgp] quit
    ```
    ```
    [*L2GW/L3GW1] commit
    ```
    
    The configuration of L2GW/L3GW2 is similar to that of L2GW/L3GW1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370673__dc_vrp_evpn_cfg_012701).
15. Verify the configuration.
    
    
    
    After completing the configurations, run the **display ip routing-table vpn-instance vpn1** command on PEs to view the UE and VNF route information in VPN routing tables.
    
    ```
    [~PE1] display ip routing-table vpn-instance vpn1
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : vpn1
             Destinations : 11       Routes : 14        
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
    
            0.0.0.0/0   Static  60   0             DB  0.0.0.0         NULL0
            5.5.5.5/32  EBGP    255  0             RD  1.1.1.1         Tunnel1
                        EBGP    255  0             RD  2.2.2.2         Tunnel2
            6.6.6.6/32  EBGP    255  0             RD  1.1.1.1         Tunnel1
                        EBGP    255  0             RD  2.2.2.2         Tunnel2
           10.7.1.0/24  Direct  0    0             D   10.7.1.1        GigabitEthernet0/1/3
           10.7.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/3
         10.7.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/3
        10.10.10.10/32  EBGP    255  0             RD  1.1.1.1         Tunnel1
                        EBGP    255  0             RD  2.2.2.2         Tunnel2
        33.33.33.33/32  EBGP    255  0             RD  1.1.1.1         Tunnel1
        44.44.44.44/32  EBGP    255  0             RD  1.1.1.1         Tunnel2
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    ```

#### Configuration Files

* PE1
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 77:77
    apply-label per-instance
    tnl-policy srte
    vpn-target 10:1 export-extcommunity
    vpn-target 10:1 import-extcommunity
  #
  mpls lsr-id 7.7.7.7
  #
  mpls
   mpls te
  #
  explicit-path PtoD74
   next sid label 48092 type adjacency
   next sid label 48091 type adjacency
  #
  explicit-path PtoD73
   next sid label 48090 type adjacency
  #
  segment-routing
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0007.00
   traffic-eng level-2
   segment-routing mpls
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.7.1 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.6.5.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.7.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 7.7.7.7 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 16100 
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 100
   mpls te path explicit-path PtoD73  
  #
  interface Tunnel2
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.4
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 200
   mpls te path explicit-path PtoD74  
  #
  bgp 200
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 ebgp-max-hop 255
   peer 3.3.3.3 connect-interface LoopBack1
   peer 3.3.3.3 egress-engineering
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 ebgp-max-hop 255
   peer 4.4.4.4 connect-interface LoopBack1
   peer 4.4.4.4 egress-engineering
   #
   ipv4-family unicast
    undo synchronization
    network 7.7.7.7 255.255.255.255
    network 10.6.5.0 255.255.255.0
    network 10.6.7.0 255.255.255.0
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   link-state-family unicast
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    import-route static
    maximum load-balancing 16
  #
  ip route-static 3.3.3.3 255.255.255.255 10.6.5.1
  ip route-static 4.4.4.4 255.255.255.255 10.6.7.2
  ip route-static 8.8.8.8 255.255.255.255 10.6.7.2
  ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0 tag 2000
  #
  tunnel-policy srte
   tunnel select-seq sr-te load-balance-number 3
  #
  return
  ```
* PE2
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 88:88
    apply-label per-instance
    tnl-policy srte
    vpn-target 10:1 export-extcommunity
    vpn-target 10:1 import-extcommunity
  #
  mpls lsr-id 8.8.8.8
  #
  mpls
   mpls te
  #
  explicit-path PtoD83
   next sid label 48092 type adjacency
   next sid label 48090 type adjacency
  #
  explicit-path PtoD84
   next sid label 48091 type adjacency
  #
  segment-routing
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0008.00
   traffic-eng level-2
   segment-routing mpls
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.7.2 255.255.255.0
   mpls
   mpls te
  #               
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.6.6.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.8.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 8.8.8.8 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 16200
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 100
   mpls te path explicit-path PtoD83  
  #
  interface Tunnel2
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.4
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 200
   mpls te path explicit-path PtoD84  
  #
  bgp 200
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 ebgp-max-hop 255
   peer 3.3.3.3 connect-interface LoopBack1
   peer 3.3.3.3 egress-engineering
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 ebgp-max-hop 255
   peer 4.4.4.4 connect-interface LoopBack1
   peer 4.4.4.4 egress-engineering
   #
   ipv4-family unicast
    undo synchronization
    network 8.8.8.8 255.255.255.255
    network 10.6.6.0 255.255.255.0
    network 10.6.7.0 255.255.255.0
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   link-state-family unicast
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    import-route static
    maximum load-balancing 16
  #
  ip route-static 3.3.3.3 255.255.255.255 10.6.7.1
  ip route-static 4.4.4.4 255.255.255.255 10.6.6.1
  ip route-static 7.7.7.7 255.255.255.255 10.6.7.1
  ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0 tag 2000
  #
  tunnel-policy srte
   tunnel select-seq sr-te load-balance-number 3
  #
  return
  ```
* DC-GW1 configuration file
  
  ```
  #
  sysname DCGW1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 1:1
   tnl-policy srte
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 2:2
   tnl-policy srte
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 3:3
   tnl-policy srte
   vpn-target 3:3 export-extcommunity
   vpn-target 3:3 import-extcommunity
  #
  evpn vpn-instance evrf4 bd-mode
   route-distinguisher 4:4
   tnl-policy srte
   vpn-target 4:4 export-extcommunity
   vpn-target 4:4 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 33:33
    apply-label per-instance
    tnl-policy srte
    export route-policy dp evpn
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 10:1 export-extcommunity
    vpn-target 11:1 import-extcommunity evpn
    vpn-target 10:1 import-extcommunity
    tnl-policy srte evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #
  bridge-domain 30
   evpn binding vpn-instance evrf3
  #
  bridge-domain 40
   evpn binding vpn-instance evrf4
  #
  explicit-path DtoL31
   next sid label 48003 type adjacency
  #
  explicit-path DtoL32
   next sid label 48002 type adjacency
   next sid label 48003 type adjacency
  #
  explicit-path DtoP37
   next sid label 48121 type adjacency
  #
  explicit-path DtoP38
   next sid label 48002 type adjacency
   next sid label 48121 type adjacency
  #
  segment-routing
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0003
   anycast-gateway enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0004
   anycast-gateway enable
  #
  interface Vbdif30
   ip binding vpn-instance vpn1
   ip address 10.3.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0001
   anycast-gateway enable
  #
  interface Vbdif40
   ip binding vpn-instance vpn1
   ip address 10.4.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0005
   anycast-gateway enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.1.1 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface GigabitEthernet0/1/1.2 mode l2
   encapsulation dot1q vid 40
   rewrite pop single
   bridge-domain 40
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.6.2.1 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/2.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/2.2 mode l2
   encapsulation dot1q vid 30
   rewrite pop single
   bridge-domain 30
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.6.5.1 255.255.255.0
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   ospf prefix-sid index 30
  #
  interface LoopBack2
   ip binding vpn-instance vpn1
   ip address 33.33.33.33 255.255.255.255
  #               
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path DtoL31  
  #
  interface Tunnel2
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 2
   mpls te path explicit-path DtoL32  
  #               
  interface Tunnel7
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 7.7.7.7
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 7
   mpls te path explicit-path DtoP37  
  #
  interface Tunnel8
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 8.8.8.8
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 8
   mpls te path explicit-path DtoP38  
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   peer 7.7.7.7 as-number 200
   peer 7.7.7.7 ebgp-max-hop 255
   peer 7.7.7.7 connect-interface LoopBack1
   peer 7.7.7.7 egress-engineering
   peer 8.8.8.8 as-number 200
   peer 8.8.8.8 ebgp-max-hop 255
   peer 8.8.8.8 connect-interface LoopBack1
   peer 8.8.8.8 egress-engineering
   #
   ipv4-family unicast
    undo synchronization
    network 10.6.1.0 255.255.255.0
    network 10.6.5.0 255.255.255.0
    import-route static
    import-route ospf 100
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
    peer 7.7.7.7 enable
    peer 8.8.8.8 enable
   #              
   link-state-family unicast
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 7.7.7.7 enable
    peer 7.7.7.7 advertise route-reoriginated evpn ip
    peer 8.8.8.8 enable
    peer 8.8.8.8 advertise route-reoriginated evpn ip
   #
   ipv4-family vpn-instance vpn1
    network 0.0.0.0
    import-route direct
    maximum load-balancing 16  
    advertise l2vpn evpn
    peer 5.5.5.5 as-number 100
    peer 5.5.5.5 connect-interface LoopBack2
    peer 5.5.5.5 route-policy p1 export
    peer 6.6.6.6 as-number 100
    peer 6.6.6.6 connect-interface LoopBack2
    peer 6.6.6.6 route-policy p1 export
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 capability-advertise add-path both
    peer 1.1.1.1 advertise add-path path-number 16
    peer 1.1.1.1 import reoriginate
    peer 2.2.2.2 enable
    peer 2.2.2.2 capability-advertise add-path both
    peer 2.2.2.2 advertise add-path path-number 16
    peer 2.2.2.2 import reoriginate
    peer 4.4.4.4 enable
    peer 4.4.4.4 route-policy stopuIP export
  #
  ospf 100
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 160000 161000
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.6.1.0 0.0.0.255
    network 10.6.2.0 0.0.0.255
    mpls-te enable
  #
  ip ip-prefix lp index 10 permit 33.33.33.33 32
  ip ip-prefix uIP index 10 permit 10.10.10.10 32
  #
  route-policy dp permit node 10
   if-match tag 2000
  #
  route-policy dp permit node 15
   if-match ip-prefix lp
  #
  route-policy p1 deny node 10
  #
  route-policy stopuIP deny node 10
   if-match ip-prefix uIP
  #
  route-policy stopuIP permit node 20
  #
  ip route-static 7.7.7.7 255.255.255.255 10.6.5.2
  ip route-static 8.8.8.8 255.255.255.255 10.6.1.2
  ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0 tag 2000
  #
  tunnel-policy srte
   tunnel select-seq sr-te load-balance-number 3
  #
  return
  ```
* DC-GW2 configuration file
  
  ```
  #
  sysname DCGW2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 1:1
   tnl-policy srte
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 2:2
   tnl-policy srte
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 3:3
   tnl-policy srte
   vpn-target 3:3 export-extcommunity
   vpn-target 3:3 import-extcommunity
  #
  evpn vpn-instance evrf4 bd-mode
   route-distinguisher 4:4
   tnl-policy srte
   vpn-target 4:4 export-extcommunity
   vpn-target 4:4 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 44:44
    apply-label per-instance
    tnl-policy srte
    export route-policy dp evpn
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 10:1 export-extcommunity
    vpn-target 11:1 import-extcommunity evpn
    vpn-target 10:1 import-extcommunity
    tnl-policy srte evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
   mpls te
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #
  bridge-domain 30
   evpn binding vpn-instance evrf3
  #
  bridge-domain 40
   evpn binding vpn-instance evrf4
  #
  explicit-path DtoL41
   next sid label 48020 type adjacency
   next sid label 48021 type adjacency
  #
  explicit-path DtoL42
   next sid label 48021 type adjacency
  #
  explicit-path DtoP47
   next sid label 48002 type adjacency
   next sid label 48121 type adjacency
  #
  explicit-path DtoP48
   next sid label 48121 type adjacency
  #
  segment-routing
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0003
   anycast-gateway enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0004
   anycast-gateway enable
  #
  interface Vbdif30
   ip binding vpn-instance vpn1
   ip address 10.3.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0001
   anycast-gateway enable
  #
  interface Vbdif40
   ip binding vpn-instance vpn1
   ip address 10.4.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0005
   anycast-gateway enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.1.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/1.2 mode l2
   encapsulation dot1q vid 30
   rewrite pop single
   bridge-domain 30
  #
  interface GigabitEthernet0/1/2
   undo shutdown  
   ip address 10.6.3.1 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/2.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface GigabitEthernet0/1/2.2 mode l2
   encapsulation dot1q vid 40
   rewrite pop single
   bridge-domain 40
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.6.6.1 255.255.255.0
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   ospf prefix-sid index 40
  #
  interface LoopBack2
   ip binding vpn-instance vpn1
   ip address 44.44.44.44 255.255.255.255
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path DtoL41  
  #
  interface Tunnel2
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 2
   mpls te path explicit-path DtoL42  
  #
  interface Tunnel7
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 7.7.7.7
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 7
   mpls te path explicit-path DtoP47  
  #
  interface Tunnel8
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 8.8.8.8
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 8
   mpls te path explicit-path DtoP48  
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 7.7.7.7 as-number 200
   peer 7.7.7.7 ebgp-max-hop 255
   peer 7.7.7.7 connect-interface LoopBack1
   peer 7.7.7.7 egress-engineering
   peer 8.8.8.8 as-number 200
   peer 8.8.8.8 ebgp-max-hop 255
   peer 8.8.8.8 connect-interface LoopBack1
   peer 8.8.8.8 egress-engineering
   #
   ipv4-family unicast
    undo synchronization
    network 10.6.1.0 255.255.255.0
    network 10.6.5.0 255.255.255.0
    import-route static
    import-route ospf 100
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
    peer 7.7.7.7 enable
    peer 8.8.8.8 enable
   #
   link-state-family unicast
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 7.7.7.7 enable
    peer 7.7.7.7 advertise route-reoriginated evpn ip
    peer 8.8.8.8 enable
    peer 8.8.8.8 advertise route-reoriginated evpn ip
   #
   ipv4-family vpn-instance vpn1
    network 0.0.0.0
    import-route direct
    maximum load-balancing 16  
    advertise l2vpn evpn
    peer 5.5.5.5 as-number 100
    peer 5.5.5.5 connect-interface LoopBack2
    peer 5.5.5.5 route-policy p1 export
    peer 6.6.6.6 as-number 100
    peer 6.6.6.6 connect-interface LoopBack2
    peer 6.6.6.6 route-policy p1 export
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 capability-advertise add-path both
    peer 1.1.1.1 advertise add-path path-number 16
    peer 1.1.1.1 import reoriginate
    peer 2.2.2.2 enable
    peer 2.2.2.2 capability-advertise add-path both
    peer 2.2.2.2 advertise add-path path-number 16
    peer 2.2.2.2 import reoriginate
    peer 3.3.3.3 enable
    peer 3.3.3.3 route-policy stopuIP export
  #
  ospf 100
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 160000 161000
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.6.1.0 0.0.0.255
    network 10.6.3.0 0.0.0.255
    mpls-te enable
  #
  ip ip-prefix lp index 10 permit 44.44.44.44 32
  ip ip-prefix uIP index 10 permit 10.10.10.10 32
  #
  route-policy dp permit node 10
   if-match tag 2000
  #
  route-policy dp permit node 15
   if-match ip-prefix lp
  #
  route-policy p1 deny node 10
  #
  route-policy stopuIP deny node 10
   if-match ip-prefix uIP
  #
  route-policy stopuIP permit node 20
  #
  ip route-static 7.7.7.7 255.255.255.255 10.6.1.1
  ip route-static 8.8.8.8 255.255.255.255 10.6.6.2
  ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0 tag 2000
  #
  tunnel-policy srte
   tunnel select-seq sr-te load-balance-number 3
  #
  return
  ```
* L2GW/L3GW1 configuration file
  
  ```
  #
  sysname L2GW/L3GW1
  #
  lacp e-trunk system-id 00e0-fc00-0002
  lacp e-trunk priority 1
  #
  evpn
   vlan-extend private enable
   vlan-extend redirect enable
   local-remote frr enable
   #
   mac-duplication
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 1:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 2:2
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 3:3
   vpn-target 3:3 export-extcommunity
   vpn-target 3:3 import-extcommunity
  #
  evpn vpn-instance evrf4 bd-mode
   route-distinguisher 4:4
   vpn-target 4:4 export-extcommunity
   vpn-target 4:4 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    apply-label per-instance
    export route-policy sp evpn
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
    tnl-policy srte evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
  #               
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #
  bridge-domain 30
   evpn binding vpn-instance evrf3
  #
  bridge-domain 40
   evpn binding vpn-instance evrf4
  #
  explicit-path LtoD13
   next sid label 48002 type adjacency
  #
  explicit-path LtoD14
   next sid label 48003 type adjacency
   next sid label 48003 type adjacency
  #
  explicit-path LtoL
   next sid label 48003 type adjacency
  #
  e-trunk 1
   priority 5
   peer-address 2.2.2.2 source-address 1.1.1.1
  #
  segment-routing
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0003
   anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0004
   anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif30
   ip binding vpn-instance vpn1
   ip address 10.3.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0001
   anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif40
   ip binding vpn-instance vpn1
   ip address 10.4.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0005
   anycast-gateway enable
   arp collect host enable
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.1111.1111.1111.1111
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface Eth-Trunk20
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.2222.2222.2222.2222
  #
  interface Eth-Trunk20.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface Eth-Trunk30
   mode lacp-static
   e-trunk 1      
   e-trunk mode force-master
   esi 0000.3333.3333.3333.3333
  #
  interface Eth-Trunk30.1 mode l2
   encapsulation dot1q vid 30
   rewrite pop single
   bridge-domain 30
  #
  interface Eth-Trunk40
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.4444.4444.4444.4444
  #
  interface Eth-Trunk40.1 mode l2
   encapsulation dot1q vid 40
   rewrite pop single
   bridge-domain 40
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.4.1 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.6.2.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   eth-trunk 10
  #               
  interface GigabitEthernet0/1/4
   undo shutdown
   eth-trunk 20
  #
  interface GigabitEthernet0/1/5
   undo shutdown
   eth-trunk 30
  #
  interface GigabitEthernet0/1/6
   undo shutdown
   eth-trunk 40
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
   ospf prefix-sid index 10
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path LtoD13  
  #
  interface Tunnel2
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.4
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 2
   mpls te path explicit-path LtoD14  
  #
  interface Tunnel3
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 3
   mpls te path explicit-path LtoL 
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    import-route static
    maximum load-balancing 16  
    advertise l2vpn evpn import-route-multipath
   #
   l2vpn-family evpn
    undo policy vpn-target
    bestroute add-path path-number 16
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise arp
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise arp
    peer 3.3.3.3 capability-advertise add-path both
    peer 3.3.3.3 advertise add-path path-number 16
    peer 4.4.4.4 enable
    peer 4.4.4.4 advertise arp
    peer 4.4.4.4 capability-advertise add-path both
    peer 4.4.4.4 advertise add-path path-number 16
  #
  ospf 100
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 160000 161000
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.6.2.0 0.0.0.255
    network 10.6.4.0 0.0.0.255
    mpls-te enable
  #
  route-policy sp permit node 10
   if-match tag 1000
   apply gateway-ip origin-nexthop
  #
  route-policy sp deny node 20
  #
  ip route-static vpn-instance vpn1 5.5.5.5 255.255.255.255 10.1.1.2 preference 255 tag 1000 inter-protocol-ecmp
  ip route-static vpn-instance vpn1 5.5.5.5 255.255.255.255 10.2.1.2 preference 255 tag 1000 inter-protocol-ecmp
  ip route-static vpn-instance vpn1 6.6.6.6 255.255.255.255 10.3.1.2 preference 255 tag 1000 inter-protocol-ecmp
  ip route-static vpn-instance vpn1 6.6.6.6 255.255.255.255 10.4.1.2 preference 255 tag 1000 inter-protocol-ecmp
  #
  tunnel-policy srte
   tunnel select-seq sr-te load-balance-number 3
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* L2GW/L3GW2 configuration file
  
  ```
  #
  sysname L2GW/L3GW2
  #
  lacp e-trunk system-id 00e0-fc00-0002
  lacp e-trunk priority 1
  #
  evpn
   vlan-extend private enable
   vlan-extend redirect enable
   local-remote frr enable
   #
   mac-duplication
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 1:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 2:2
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 3:3
   vpn-target 3:3 export-extcommunity
   vpn-target 3:3 import-extcommunity
  #
  evpn vpn-instance evrf4 bd-mode
   route-distinguisher 4:4
   vpn-target 4:4 export-extcommunity
   vpn-target 4:4 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 22:22
    apply-label per-instance
    export route-policy sp evpn
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
    tnl-policy srte evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
  #               
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #
  bridge-domain 30
   evpn binding vpn-instance evrf3
  #
  bridge-domain 40
   evpn binding vpn-instance evrf4
  #
  explicit-path LtoD23
   next sid label 48004 type adjacency
   next sid label 48002 type adjacency
  #
  explicit-path LtoD24
   next sid label 48003 type adjacency
  #
  explicit-path LtoL
   next sid label 48004 type adjacency
  #
  e-trunk 1
   priority 5
   peer-address 1.1.1.1 source-address 2.2.2.2
  #
  segment-routing
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0003
   anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0004
   anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif30
   ip binding vpn-instance vpn1
   ip address 10.3.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0001
   anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif40
   ip binding vpn-instance vpn1
   ip address 10.4.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0005
   anycast-gateway enable
   arp collect host enable
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.1111.1111.1111.1111
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface Eth-Trunk20
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.2222.2222.2222.2222
  #
  interface Eth-Trunk20.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface Eth-Trunk30
   mode lacp-static
   e-trunk 1      
   e-trunk mode force-master
   esi 0000.3333.3333.3333.3333
  #
  interface Eth-Trunk30.1 mode l2
   encapsulation dot1q vid 30
   rewrite pop single
   bridge-domain 30
  #
  interface Eth-Trunk40
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.4444.4444.4444.4444
  #
  interface Eth-Trunk40.1 mode l2
   encapsulation dot1q vid 40
   rewrite pop single
   bridge-domain 40
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.4.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.6.3.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   eth-trunk 10
  #               
  interface GigabitEthernet0/1/4
   undo shutdown
   eth-trunk 20
  #
  interface GigabitEthernet0/1/5
   undo shutdown
   eth-trunk 30
  #
  interface GigabitEthernet0/1/6
   undo shutdown
   eth-trunk 40
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   ospf prefix-sid index 20
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path LtoD23  
  #
  interface Tunnel2
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.4
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 2
   mpls te path explicit-path LtoD24  
  #
  interface Tunnel3
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 3
   mpls te path explicit-path LtoL
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    import-route static
    maximum load-balancing 16  
    advertise l2vpn evpn import-route-multipath
   #
   l2vpn-family evpn
    undo policy vpn-target
    bestroute add-path path-number 16
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise arp
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise arp
    peer 3.3.3.3 capability-advertise add-path both
    peer 3.3.3.3 advertise add-path path-number 16
    peer 4.4.4.4 enable
    peer 4.4.4.4 advertise arp
    peer 4.4.4.4 capability-advertise add-path both
    peer 4.4.4.4 advertise add-path path-number 16
  #
  ospf 100
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 160000 161000
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.6.3.0 0.0.0.255
    network 10.6.4.0 0.0.0.255
    mpls-te enable
  #
  route-policy sp permit node 10
   if-match tag 1000
   apply gateway-ip origin-nexthop
  #
  route-policy sp deny node 20
  #
  ip route-static vpn-instance vpn1 5.5.5.5 255.255.255.255 10.1.1.2 preference 255 tag 1000 inter-protocol-ecmp
  ip route-static vpn-instance vpn1 5.5.5.5 255.255.255.255 10.2.1.2 preference 255 tag 1000 inter-protocol-ecmp
  ip route-static vpn-instance vpn1 6.6.6.6 255.255.255.255 10.3.1.2 preference 255 tag 1000 inter-protocol-ecmp
  ip route-static vpn-instance vpn1 6.6.6.6 255.255.255.255 10.4.1.2 preference 255 tag 1000 inter-protocol-ecmp
  #
  tunnel-policy srte
   tunnel select-seq sr-te load-balance-number 3
  #
  evpn source-address 2.2.2.2
  #
  return
  ```
* VNF1 configuration file
  
  For details, see the configuration file of the corresponding product.
* VNF2 configuration file
  
  For details, see the configuration file of the corresponding product.