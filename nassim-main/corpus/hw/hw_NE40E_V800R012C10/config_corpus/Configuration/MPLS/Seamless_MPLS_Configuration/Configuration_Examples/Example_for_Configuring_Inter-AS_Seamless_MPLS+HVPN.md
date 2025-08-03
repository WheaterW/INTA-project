Example for Configuring Inter-AS Seamless MPLS+HVPN
===================================================

In the inter-AS seamless MPLS+HVPN networking, an HVPN connection between a CSG and AGG is established, and an inter-AS seamless MPLS LSP between an AGG and MASG is established. The inter-AS seamless MPLS+HVPN networking obtains the collective advantages of the inter-AS seamless MPLS network and HVPN.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172368692__fig_dc_vrp_seamless_mpls_cfg_003302), the access and aggregation layers belong to AS 100, and the core layer belongs to AS 200. To provision VPN services, the inter-AS seamless MPLS+HVPN networking can be deployed. This networking allows base stations and the MME/SGW to communicate with each other and cuts networking construction costs with the use of HVPN. An HVPN connection for each CSG-and-AGG pair is established, and an inter-AS seamless MPLS LSP for each AGG-and-MASG pair is established.

**Figure 1** Inter-AS seamless MPLS+HVPN networking (1)  
![](images/fig_dc_vrp_seamless_mpls_cfg_003302.png "Click to enlarge")

Addresses of interfaces are planned for the CSGs, AGGs, AGG ASBRs, core ASBRs, and MASGs shown in [Figure 2](#EN-US_TASK_0172368692__fig_dc_vrp_seamless_mpls_cfg_003301).

**Figure 2** Inter-AS seamless MPLS+HVPN networking (2)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example are GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_seamless_mpls_cfg_003301.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP protocols at the access, aggregation, and core layers to implement network connectivity at each layer.
2. Configure MPLS and MPLS LDP and establish MPLS LSPs at the access, aggregation, and core layers.
3. Establish IBGP peer relationships at the aggregation and core layers and enable devices to exchange labeled routes.
4. Configure an EBGP peer relationship for each AGG ASBR-and-core ASBR pair and enable these devices to exchange labeled routes across ASs.
5. Configure a routing policy to control label distribution for a BGP LSP to be established on each device, except CGSs. The egress of the BGP LSP to be established needs to assign an MPLS label to the route advertised to an upstream node. If a transit node receives a labeled IPv4 route from downstream, the downstream node must re-assign an MPLS label to the transit node.
6. Configure an MP-EBGP peer relationship between an AGG and MASG to allow these devices to exchange VPNv4 route information.
7. Configure an MP-IBGP peer relationship between a CSG and AGG to allow these devices to exchange VPNv4 route information.
8. Configure VPN instances on each CSG, AGG, and MASG.
9. Configure a default route and an IP address prefix list on each AGG so that the AGG only advertises the default route to its directly connected CSG.

#### Data Preparation

To complete the configuration, you need the following data:

* OSPF process ID (1) at the access layer, IS-IS process ID (1) at the aggregation layer, and OSPF process ID (2) at the core layer
* MPLS LSR IDs: 1.1.1.1 for the CSG, 2.2.2.2 for the AGG, 3.3.3.3 for the AGG ASBR, 4.4.4.4 for the core ASBR, and 5.5.5.5 for the MASG.
* Name of a routing policy (policy1)

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Configure interface IP addresses and masks; configure a loopback interface address as an LSR ID on every device shown in [Figure 2](#EN-US_TASK_0172368692__fig_dc_vrp_seamless_mpls_cfg_003301); configure OSPF and IS-IS to advertise the route to the network segment of each interface and a host route to each loopback interface address (LSR ID). For configuration details, see Configuration Files in this section.
2. Enable MPLS and LDP globally on each device.
   
   
   
   # Configure the CSG.
   
   ```
   [~CSG] mpls lsr-id 1.1.1.1
   ```
   ```
   [*CSG] mpls
   ```
   ```
   [*CSG-mpls] quit
   ```
   ```
   [*CSG] mpls ldp
   ```
   ```
   [*CSG-mpls-ldp] quit
   ```
   ```
   [*CSG] interface GigabitEthernet 0/1/0
   ```
   ```
   [*CSG-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*CSG-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*CSG-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CSG] commit
   ```
   
   # Configure the AGG.
   
   ```
   [~AGG] mpls lsr-id 2.2.2.2
   ```
   ```
   [*AGG] mpls
   ```
   ```
   [*AGG-mpls] quit
   ```
   ```
   [*AGG] mpls ldp
   ```
   ```
   [*AGG-mpls-ldp] quit
   ```
   ```
   [*AGG] interface GigabitEthernet 0/1/0
   ```
   ```
   [*AGG-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*AGG-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*AGG-GigabitEthernet0/1/0] quit
   ```
   ```
   [*AGG] interface GigabitEthernet 0/2/0
   ```
   ```
   [*AGG-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*AGG-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*AGG-GigabitEthernet0/2/0] quit
   ```
   ```
   [*AGG] commit
   ```
   
   # Configure the AGG ASBR.
   
   ```
   [~AGG ASBR] mpls lsr-id 3.3.3.3
   ```
   ```
   [*AGG ASBR] mpls
   ```
   ```
   [*AGG ASBR-mpls] quit
   ```
   ```
   [*AGG ASBR] mpls ldp
   ```
   ```
   [*AGG ASBR-mpls-ldp] quit
   ```
   ```
   [*AGG ASBR] interface GigabitEthernet 0/1/0
   ```
   ```
   [*AGG ASBR-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*AGG ASBR-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*AGG ASBR-GigabitEthernet0/1/0] quit
   ```
   ```
   [*AGG ASBR] commit
   ```
   
   # Configure the core ASBR.
   
   ```
   [~Core ASBR] mpls lsr-id 4.4.4.4
   ```
   ```
   [*Core ASBR] mpls
   ```
   ```
   [*Core ASBR-mpls] quit
   ```
   ```
   [*Core ASBR] mpls ldp
   ```
   ```
   [*Core ASBR-mpls-ldp] quit
   ```
   ```
   [*Core ASBR] interface GigabitEthernet 0/2/0
   ```
   ```
   [*Core ASBR-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*Core ASBR-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*Core ASBR-GigabitEthernet0/2/0] quit
   ```
   ```
   [*Core ASBR] commit
   ```
   
   # Configure the MASG.
   
   ```
   [~MASG] mpls lsr-id 5.5.5.5
   ```
   ```
   [*MASG] mpls
   ```
   ```
   [*MASG-mpls] quit
   ```
   ```
   [*MASG] mpls ldp
   ```
   ```
   [*MASG-mpls-ldp] quit
   ```
   ```
   [*MASG] interface GigabitEthernet 0/1/0
   ```
   ```
   [*MASG-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*MASG-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*MASG-GigabitEthernet0/1/0] quit
   ```
   ```
   [*MASG] commit
   ```
3. Establish IBGP peer relationships at the aggregation and core layers and enable devices to exchange labeled routes.
   
   
   
   # Configure the AGG.
   
   ```
   [~AGG] bgp 100
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 connect-interface LoopBack 1
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 label-route-capability
   ```
   ```
   [*AGG-bgp] network 2.2.2.2 32
   ```
   ```
   [*AGG-bgp] quit
   ```
   ```
   [*AGG] commit
   ```
   
   # Configure the AGG ASBR.
   
   ```
   [~AGG ASBR] bgp 100
   ```
   ```
   [*AGG ASBR-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*AGG ASBR-bgp] peer 2.2.2.2 connect-interface LoopBack 1
   ```
   ```
   [*AGG ASBR-bgp] peer 2.2.2.2 label-route-capability
   ```
   ```
   [*AGG ASBR-bgp] quit
   ```
   ```
   [*AGG ASBR] commit
   ```
   
   # Configure the core ASBR.
   
   ```
   [~Core ASBR] bgp 200
   ```
   ```
   [*Core ASBR-bgp] peer 5.5.5.5 as-number 200
   ```
   ```
   [*Core ASBR-bgp] peer 5.5.5.5 connect-interface LoopBack 1
   ```
   ```
   [*Core ASBR-bgp] peer 5.5.5.5 label-route-capability
   ```
   ```
   [*Core ASBR-bgp] quit
   ```
   ```
   [*Core ASBR] commit
   ```
   
   # Configure the MASG.
   
   ```
   [~MASG] bgp 200
   ```
   ```
   [*MASG-bgp] peer 4.4.4.4 as-number 200
   ```
   ```
   [*MASG-bgp] peer 4.4.4.4 connect-interface LoopBack 1
   ```
   ```
   [*MASG-bgp] peer 4.4.4.4 label-route-capability
   ```
   ```
   [*MASG-bgp] network 5.5.5.5 32
   ```
   ```
   [*MASG-bgp] quit
   ```
   ```
   [*MASG] commit
   ```
4. Establish an EBGP peer relationship for each AGG ASBR-and-core ASBR pair and enable these devices to exchange labeled routes.
   
   
   
   # Configure the AGG ASBR.
   
   ```
   [~AGG ASBR] interface GigabitEthernet 0/2/0
   ```
   ```
   [~AGG ASBR-GigabitEthernet0/2/0] ip address 10.3.1.1 24
   ```
   ```
   [*AGG ASBR-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*AGG ASBR-GigabitEthernet0/2/0] quit
   ```
   ```
   [*AGG ASBR] bgp 100
   ```
   ```
   [*AGG ASBR-bgp] peer 10.3.1.2 as-number 200
   ```
   ```
   [*AGG ASBR-bgp] peer 10.3.1.2 label-route-capability check-tunnel-reachable
   ```
   ```
   [*AGG ASBR-bgp] quit
   ```
   ```
   [*AGG ASBR] commit
   ```
   
   # Configure the core ASBR.
   
   ```
   [~Core ASBR] interface GigabitEthernet 0/1/0
   ```
   ```
   [~Core ASBR-GigabitEthernet0/1/0] ip address 10.3.1.2 24
   ```
   ```
   [*Core ASBR-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*Core ASBR-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Core ASBR] bgp 200
   ```
   ```
   [*Core ASBR-bgp] peer 10.3.1.1 as-number 100
   ```
   ```
   [*Core ASBR-bgp] peer 10.3.1.1 label-route-capability check-tunnel-reachable
   ```
   ```
   [*Core ASBR-bgp] quit
   ```
   ```
   [*Core ASBR] commit
   ```
5. Configure an MP-EBGP peer relationship for each AGG-and-MASG pair.
   
   
   
   # Configure the AGG.
   
   ```
   [~AGG] bgp 100
   ```
   ```
   [~AGG-bgp] peer 5.5.5.5 as-number 200
   ```
   ```
   [*AGG-bgp] peer 5.5.5.5 connect-interface LoopBack 1
   ```
   ```
   [*AGG-bgp] peer 5.5.5.5 ebgp-max-hop 10
   ```
   ```
   [*AGG-bgp] ipv4-family vpnv4
   ```
   ```
   [*AGG-bgp-af-vpnv4] peer 5.5.5.5 enable
   ```
   ```
   [*AGG-bgp-af-vpnv4] quit
   ```
   ```
   [*AGG-bgp] quit
   ```
   ```
   [*AGG] commit
   ```
   
   # Configure the MASG.
   
   ```
   [~MASG] bgp 200
   ```
   ```
   [~MASG-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*MASG-bgp] peer 2.2.2.2 connect-interface LoopBack 1
   ```
   ```
   [*MASG-bgp] peer 2.2.2.2 ebgp-max-hop 10
   ```
   ```
   [*MASG-bgp] ipv4-family vpnv4
   ```
   ```
   [*MASG-bgp-af-vpnv4] peer 2.2.2.2 enable
   ```
   ```
   [*MASG-bgp-af-vpnv4] quit
   ```
   ```
   [*MASG-bgp] quit
   ```
   ```
   [*MASG] commit
   ```
6. Configure a routing policy to establish a BGP LSP.
   
   
   
   # Configure a routing policy for advertising routes matching Route-Policy conditions to the AGG's BGP peer.
   
   ```
   <AGG> system-view 
   ```
   ```
   [~AGG] route-policy policy1 permit node 1
   ```
   ```
   [*AGG-route-policy] apply mpls-label
   ```
   ```
   [*AGG-route-policy] quit
   ```
   ```
   [*AGG] bgp 100
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 route-policy policy1 export
   ```
   ```
   [*AGG-bgp] quit
   ```
   ```
   [*AGG] commit
   ```
   
   Repeat this step for the MASG. For configuration details, see Configuration Files in this section.
   
   # Configure a routing policy for advertising routes matching Route-Policy conditions to the AGG ASBR's BGP peer.
   
   ```
   [~AGG ASBR] route-policy policy1 permit node 1
   ```
   ```
   [*AGG ASBR-route-policy] if-match mpls-label
   ```
   ```
   [*AGG ASBR-route-policy] apply mpls-label
   ```
   ```
   [*AGG ASBR-route-policy] quit
   ```
   ```
   [*AGG ASBR] bgp 100
   ```
   ```
   [*AGG ASBR-bgp] peer 2.2.2.2 route-policy policy1 export
   ```
   ```
   [*AGG ASBR-bgp] peer 10.3.1.2 route-policy policy1 export
   ```
   ```
   [*AGG ASBR-bgp] quit
   ```
   ```
   [*AGG ASBR] commit
   ```
   
   Repeat this step for the core ASBR. For configuration details, see Configuration Files in this section.
   
   After completing the preceding configurations, run the **ping lsp** command on an AGG or MASG. The command output shows that the AGG and MASG can ping each other. This indicates that the BGP LSP between the AGG and MASG has been established. The following example uses the command output on the AGG.
   ```
   <AGG> ping lsp bgp 5.5.5.5 32
   ```
   ```
     LSP PING FEC: BGP LABLED IPV4 PREFIX 5.5.5.5/32/ : 100  data bytes, press CTRL_C to break
       Reply from 5.5.5.5: bytes=100 Sequence=1 time=870 ms
       Reply from 5.5.5.5: bytes=100 Sequence=2 time=40 ms
       Reply from 5.5.5.5: bytes=100 Sequence=3 time=110 ms
       Reply from 5.5.5.5: bytes=100 Sequence=4 time=80 ms
       Reply from 5.5.5.5: bytes=100 Sequence=5 time=110 ms
   
     --- FEC: BGP LABLED IPV4 PREFIX 5.5.5.5/32 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 40/242/870 ms
   ```
7. Configure an MP-IBGP peer relationship for each CSG-and-AGG pair.
   
   
   
   # Configure the CSG.
   
   ```
   [~CSG] bgp 100
   ```
   ```
   [~CSG-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*CSG-bgp] peer 2.2.2.2 connect-interface LoopBack 1
   ```
   ```
   [*CSG-bgp] network 1.1.1.1 32
   ```
   ```
   [*CSG-bgp] ipv4-family vpnv4
   ```
   ```
   [*CSG-bgp-af-vpnv4] peer 2.2.2.2 enable
   ```
   ```
   [*CSG-bgp-af-vpnv4] quit
   ```
   ```
   [*CSG-bgp] quit
   ```
   ```
   [*CSG] commit
   ```
   
   # Configure the AGG.
   
   ```
   [~AGG] bgp 100
   ```
   ```
   [~AGG-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*AGG-bgp] peer 1.1.1.1 connect-interface LoopBack 1
   ```
   ```
   [*AGG-bgp] ipv4-family vpnv4
   ```
   ```
   [*AGG-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*AGG-bgp] quit
   ```
   ```
   [*AGG] commit
   ```
8. Configure a VPN instance and bind an interface of each device to the VPN instance.
   
   
   
   # Configure the CSG.
   
   ```
   [~CSG] ip vpn-instance vpn1
   ```
   ```
   [*CSG-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*CSG-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*CSG-vpn-instance-vpn1-af-ipv4] vpn-target 1:1
   ```
   ```
   [*CSG-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*CSG-vpn-instance-vpn1] quit
   ```
   ```
   [*CSG] interface GigabitEthernet 0/2/0
   ```
   ```
   [*CSG-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*CSG-GigabitEthernet0/2/0] ip address 10.5.1.1 255.255.255.0
   ```
   ```
   [*CSG-GigabitEthernet0/2/0] quit
   ```
   ```
   [*CSG] bgp 100
   ```
   ```
   [*CSG-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*CSG-bgp-vpn1] import-route direct
   ```
   ```
   [*CSG-bgp-vpn1] quit
   ```
   ```
   [*CSG-bgp] quit
   ```
   ```
   [*CSG] commit
   ```
   ```
   [~CSG] quit
   ```
   
   Repeat this step for the MASG. For configuration details, see Configuration Files in this section.
   
   # Configure the AGG.
   
   ```
   [~AGG] ip vpn-instance vpn1
   ```
   ```
   [*AGG-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*AGG-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*AGG-vpn-instance-vpn1-af-ipv4] vpn-target 1:1
   ```
   ```
   [*AGG-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*AGG-vpn-instance-vpn1] quit
   ```
   ```
   [*AGG] commit
   ```
9. Configure a default route and an IP address prefix list on each AGG so that the AGG only advertises the default route to its directly connected CSG.
   
   
   ```
   [~AGG] ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0 
   ```
   ```
   [*AGG] ip ip-prefix default index 10 permit 0.0.0.0 0
   ```
   ```
   [*AGG] bgp 100
   ```
   ```
   [*AGG-bgp] ipv4-family vpnv4
   ```
   ```
   [*AGG-bgp-af-vpnv4] peer 1.1.1.1 ip-prefix default export
   ```
   ```
   [*AGG-bgp-af-vpnv4] quit
   ```
   ```
   [*AGG-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*AGG-bgp-vpn1] network 0.0.0.0 0
   ```
   ```
   [*AGG-bgp-vpn1] quit
   ```
   ```
   [*AGG-bgp] quit
   ```
   ```
   [*AGG] commit
   ```
10. Verify the configuration.
    
    
    
    After completing the preceding configurations, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on the CSG. The command output shows that the CSG has a default route with its directly connected AGG as the next hop, but does not have a VPN route to the MME or SGW. In addition, the CSG can ping the MME or SGW.
    
    The following example uses the command output on the CSG.
    
    ```
    <CSG> display ip routing-table vpn-instance vpn1
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : vpn1
             Destinations : 5        Routes : 5
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
    
            0.0.0.0/0   IBGP    255  0             RD 2.2.2.2         GigabitEthernet0/2/0
           10.5.1.0/24  Direct  0    0             D  10.5.1.1        GigabitEthernet0/2/0
           10.5.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0
         10.5.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0
    255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
    ```
    ```
    <CSG> ping -vpn-instance vpn1 10.6.1.1
    ```
    ```
      PING 10.6.1.0: 56  data bytes, press CTRL_C to break
        Reply from 10.6.1.0: bytes=56 Sequence=1 ttl=252 time=6 ms
        Reply from 10.6.1.0: bytes=56 Sequence=2 ttl=252 time=3 ms
        Reply from 10.6.1.0: bytes=56 Sequence=3 ttl=252 time=3 ms
        Reply from 10.6.1.0: bytes=56 Sequence=4 ttl=252 time=4 ms
        Reply from 10.6.1.0: bytes=56 Sequence=5 ttl=252 time=2 ms
    
      --- 10.6.1.1 ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 2/3/6 ms
    ```

#### Configuration Files

* CSG configuration file
  
  ```
  #
  sysname CSG
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.5.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* AGG configuration file
  
  ```
  #
  sysname AGG
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0000.0010.00
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
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 5.5.5.5 as-number 200
   peer 5.5.5.5 ebgp-max-hop 10
   peer 5.5.5.5 connect-interface LoopBack1
   #
   ipv4-family unicast
    network 2.2.2.2 255.255.255.255
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 3.3.3.3 route-policy policy1 export
    peer 3.3.3.3 label-route-capability
    peer 5.5.5.5 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 ip-prefix default export
    peer 5.5.5.5 enable
   #
   ipv4-family vpn-instance vpn1
    network 0.0.0.0
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  ip ip-prefix default index 10 permit 0.0.0.0 0
  #
  ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0
  #
  return
  ```
* AGG ASBR configuration file
  
  ```
  #
  sysname AGG ASBR
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0000.0020.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 10.3.1.2 as-number 200
   #
   ipv4-family unicast
    peer 2.2.2.2 enable
    peer 2.2.2.2 route-policy policy1 export
    peer 2.2.2.2 label-route-capability
    peer 10.3.1.2 enable
    peer 10.3.1.2 route-policy policy1 export
    peer 10.3.1.2 label-route-capability check-tunnel-reachable
  #
  route-policy policy1 permit node 1
   if-match mpls-label
   apply mpls-label
  #
  return
  ```
* Core ASBR configuration file
  
  ```
  #
  sysname Core ASBR
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 200
   peer 5.5.5.5 as-number 200
   peer 5.5.5.5 connect-interface LoopBack1
   peer 10.3.1.1 as-number 100
   #
   ipv4-family unicast
    peer 5.5.5.5 enable
    peer 5.5.5.5 route-policy policy1 export
    peer 5.5.5.5 label-route-capability
    peer 10.3.1.1 enable
    peer 10.3.1.1 route-policy policy1 export
    peer 10.3.1.1 label-route-capability check-tunnel-reachable
  #
  ospf 2
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.4.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   if-match mpls-label
   apply mpls-label
  #
  return
  ```
* MASG configuration file
  
  ```
  #
  sysname MASG
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 5.5.5.5
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.6.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.4.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
  #
  bgp 200
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 ebgp-max-hop 10
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    network 5.5.5.5 255.255.255.255
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
    peer 4.4.4.4 route-policy policy1 export
    peer 4.4.4.4 label-route-capability
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
  #
  ospf 2
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
    network 10.4.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  ```