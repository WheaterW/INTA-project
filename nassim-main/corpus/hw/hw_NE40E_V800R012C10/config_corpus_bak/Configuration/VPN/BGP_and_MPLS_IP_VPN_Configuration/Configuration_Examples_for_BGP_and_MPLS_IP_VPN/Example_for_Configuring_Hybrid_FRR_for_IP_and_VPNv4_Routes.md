Example for Configuring Hybrid FRR for IP and VPNv4 Routes
==========================================================

On a network where a CE is dual-homed to two PEs, IP+VPNv4 hybrid FRR can be configured on PEs to protect the link between either PE and the CE. If the link between one PE and the CE fails, traffic destined for the CE can be switched to the other PE for transmission.

#### Networking Requirements

A CE at a VPN site is dual-homed to two PEs, and a VPNv4 peer relationship is set up between the two PEs. To protect one of the PE-CE links, IP+VPNv4 hybrid FRR can be configured.

If one link fails, IP+VPNv4 hybrid FRR can quickly switch traffic destined for the CE to the backup next hop (the other PE).

As shown in [Figure 1](#EN-US_TASK_0172369564__fig_dc_vrp_mpls-l3vpn-v4_cfg_201501), a CE is dual-homed to PE2 and PE3; an MPLS public network tunnel and a VPNv4 peer relationship are set up between PE2 and PE3. OSPF is configured between PE2 and the CE and EBGP is configured between PE3 and the CE to exchange routing information. PE3 learns from the CE a route to the Loopback1 interface on the CE and sends the route to its VPNv4 peer. PE2 then has two BGP routes to the Loopback1 interface on the CE. One is learned using OSPF, and the other is a VPNv4 route sent from PE3 using MP-IBGP. PE2 preferentially selects the OSPF route sent from the CE because OSPF takes precedence over BGP. PE3 selects a route to the loopback interface on the CE from the routes sent from the CE and PE2 in a similar manner.

The company requires that:

* PE2 must be configured to make the VPNv4 route sent from PE3 serve as a backup for the OSPF route sent from the CE.
* PE3 must be configured to preferentially select the EBGP route sent from the CE and use the IBGP route sent from PE2 as a backup route.

Then, if the link between a PE and the CE fails, downstream traffic can be switched to the other PE for transmission.

To meet the requirements, enable VPN IP FRR on PE2 and BGP auto FRR on PE3 to implement IP+VPNv4 hybrid FRR.

**Figure 1** Configuring IP+VPNv4 hybrid FRR![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, and interface3 in this example represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_201501.png)

#### Precautions

In a VPN FRR scenario, after the primary path recovers, traffic switches back to this path. Because the order in which nodes undergo IGP convergence differs, packet loss may occur during the switchback. To resolve this problem, run the [**route-select delay**](cmdqueryname=route-select+delay) *delay-value* command to configure a route selection delay so that traffic is switched back only after forwarding entries on the devices along the primary path are updated. The delay specified using *delay-value* depends on various factors, such as the number of routes on the devices. Set an appropriate delay as needed.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF for PE1, PE2, and PE3 on the MPLS backbone network to communicate.
2. Configure MPLS and MPLS LDP both globally and per interface on each node and establish LDP LSPs on the MPLS backbone network.
3. Establish an MP-IBGP peer relationship between PEs, including between PE2 and PE3.
4. Configure a VPN instance on each PE, and configure CE access to PE2 and PE3.
5. Configure routing protocols between the PEs and the CE.
6. Configure VPN IP FRR on PE2 and BGP auto FRR on PE3.

#### Procedure

1. Configure IP addresses for involved interfaces on the VPN backbone network and at the VPN site.
2. Configure OSPF on the MPLS backbone network for IP connectivity between PEs.
3. Configure basic MPLS functions, enable MPLS LDP, and establish LDP LSPs on the MPLS backbone network.
   
   
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
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
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   <PE2> system-view
   ```
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
   [*PE2-mpls-ldp] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   <PE3> system-view
   ```
   ```
   [~PE3] mpls lsr-id 3.3.3.3
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
   [*PE3-mpls-ldp] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/1/0
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/3/0
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE3] commit
   ```
   
   Run the **display mpls lsp** command on the PEs. The command output shows that LSPs are established between PE1 and PE2 and between PE1 and PE3. The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls lsp
   ----------------------------------------------------------------------
                    LSP Information: LDP LSP
   ----------------------------------------------------------------------
   FEC                In/Out Label  In/Out IF                      Vrf Name
   2.2.2.2/32         NULL/3        -/GE0/2/0
   2.2.2.2/32         1024/3        -/GE0/2/0
   3.3.3.3/32         NULL/3        -/GE0/3/0
   3.3.3.3/32         1025/3        -/GE0/3/0
   ```
4. Set up an MP-IBGP peer relationship between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] quit
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
   [*PE2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 3.3.3.3 enable
   ```
   ```
   [*PE2-bgp-af-vpnv4] quit
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
   [*PE3-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE3-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE3-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE3-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*PE3-bgp-af-vpnv4] peer 2.2.2.2 enable
   ```
   ```
   [*PE3-bgp-af-vpnv4] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   Run the **display bgp vpnv4 all peer** command on the PEs. The command output shows that the status of the MP-IBGP peer relationship between PEs is **Established**.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp vpnv4 all peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
   Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down       State PrefRcv
   
   2.2.2.2         4   100       20       17       0 00:13:26 Established       0
   3.3.3.3         4   100       24       19       0 00:17:18 Established       1
   ```
5. Configure a VPN instance on each PE, and configure CE access to PE2 and PE3.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] vpn-target 111:1
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
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpn1
   ```
   ```
   [*PE2-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:2
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] vpn-target 111:1
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 192.168.1.1 30
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ip vpn-instance vpn1
   ```
   ```
   [*PE3-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE3-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:2
   ```
   ```
   [*PE3-vpn-instance-vpn1-af-ipv4] vpn-target 111:1
   ```
   ```
   [*PE3-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE3-vpn-instance-vpn1] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ip address 192.168.2.1 30
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE3] commit
   ```
6. Configure an OSPF instance on PE2 and the CE and set up an EBGP peer relationship between PE3 and the CE.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 2 vpn-instance vpn1
   ```
   ```
   [*PE2-ospf-2] import-route bgp
   ```
   ```
   [*PE2-ospf-2] area 1
   ```
   ```
   [*PE2-ospf-2-area-0.0.0.1] network 192.168.1.0 0.0.0.3
   ```
   ```
   [*PE2-ospf-2-area-0.0.0.1] quit
   ```
   ```
   [*PE2-ospf-2] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp-vpn1] import-route ospf 2
   ```
   ```
   [*PE2-bgp-vpn1] quit
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
   [*PE3-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE3-bgp-vpn1] peer 192.168.2.2 as-number 65410
   ```
   ```
   [*PE3-bgp-vpn1] peer 192.168.2.2 preferred-value 600
   ```
   ```
   [*PE3-bgp-vpn1] bestroute as-path-ignore
   ```
   ```
   [*PE3-bgp-vpn1] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure the CE.
   
   ```
   [~CE] bgp 65410
   ```
   ```
   [*CE-bgp] peer 192.168.2.1 as-number 100
   ```
   ```
   [*CE-bgp] network 22.22.22.22 32
   ```
   ```
   [*CE-bgp] quit
   ```
   ```
   [*CE] ospf 1
   ```
   ```
   [*CE-ospf-1] area 1
   ```
   ```
   [*CE-ospf-1-area-0.0.0.1] network 192.168.1.0 0.0.0.3
   ```
   ```
   [*CE-ospf-1-area-0.0.0.1] network 22.22.22.22 0.0.0.0
   ```
   ```
   [*CE-ospf-1-area-0.0.0.1] quit
   ```
   ```
   [*CE-ospf-1] quit
   ```
   ```
   [*CE] commit
   ```
   After completing the configuration, run the [**display ip routing-table vpn-instance vpn1 22.22.22.22 verbose**](cmdqueryname=display+ip+routing-table+vpn-instance+vpn1+22.22.22.22+verbose) command on PE2. The command output shows that PE2 has learned routes to the loopback interface on the CE.
   ```
   <PE2> display ip routing-table vpn-instance vpn1 22.22.22.22 verbose
   
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpn1
   Summary Count : 2
   
   Destination: 22.22.22.22/32          
        Protocol: OSPF            Process ID: 2              
      Preference: 10                    Cost: 1              
         NextHop: 192.168.1.2      Neighbour: 0.0.0.0        
           State: Active Adv             Age: 00h11m08s           
             Tag: 0                 Priority: medium         
           Label: NULL               QoSInfo: 0x0            
      IndirectID: 0x76          
    RelayNextHop: 0.0.0.0          Interface: GigabitEthernet0/2/0
        TunnelID: 0x0                  Flags: D              
   
   Destination: 22.22.22.22/32          
        Protocol: IBGP            Process ID: 0              
      Preference: 255                   Cost: 0              
         NextHop: 3.3.3.3          Neighbour: 0.0.0.0        
           State: Inactive Adv           Age: 00h13m25s           
             Tag: 0                 Priority: low            
           Label: 0x23               QoSInfo: 0x0            
      IndirectID: 0xb7          
    RelayNextHop: 10.11.1.2        Interface: GigabitEthernet0/3/0
        TunnelID: 0x0000000001004c4c62 Flags: R   
   ```
   
   The command output shows that PE2 has learned from the CE using OSPF and from PE3 using BGP the routes to the loopback interface on the CE. Because OSPF takes precedence over BGP, PE2 preferentially selects the OSPF route advertised by PE3.
7. Enable IP auto FRR for the VPN instance IPv4 address family on PE2.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpn1
   ```
   ```
   [~PE2-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] ip frr
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] commit
   ```
8. Enable BGP auto FRR for the BGP-VPN instance IPv4 address family on PE3.
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [~PE3-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE3-bgp-vpn1] auto-frr
   ```
   ```
   [*PE3-bgp-vpn1] route-select delay 300
   ```
   ```
   [*PE3-bgp-vpn1] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
9. Verify the configuration. 
   
   
   
   After completing the configuration, run the **display ip routing-table vpn-instance verbose** command on PE2 and PE3 to check the VPN instance routing table on each PE.
   
   ```
   <PE2> display ip routing-table vpn-instance vpn1 22.22.22.22 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpn1
   Summary Count : 2
   
   Destination: 22.22.22.22/32          
        Protocol: OSPF            Process ID: 2              
      Preference: 10                    Cost: 1              
         NextHop: 192.168.1.2         Neighbour: 0.0.0.0        
           State: Active Adv             Age: 00h26m40s           
             Tag: 0                 Priority: medium         
           Label: NULL               QoSInfo: 0x0            
      IndirectID: 0x76          
    RelayNextHop: 0.0.0.0          Interface: GigabitEthernet0/2/0
        TunnelID: 0x0                  Flags: D              
       BkNextHop: 3.3.3.3        BkInterface: GigabitEthernet0/3/0
         BkLabel: 0x23           SecTunnelID: 0x0              
    BkPETunnelID: 0x0000000001004c4c62 BkPESecTunnelID: 0x0              
    BkIndirectID: 0xb7          
   
   Destination: 22.22.22.22/32          
        Protocol: IBGP            Process ID: 0              
      Preference: 255                   Cost: 0              
         NextHop: 3.3.3.3          Neighbour: 0.0.0.0        
           State: Inactive Adv           Age: 00h28m57s           
             Tag: 0                 Priority: low            
           Label: 0x23               QoSInfo: 0x0            
      IndirectID: 0xb7          
    RelayNextHop: 10.11.1.2        Interface: GigabitEthernet0/3/0
        TunnelID: 0x0000000001004c4c62 Flags: R 
   ```
   ```
   <PE3> display ip routing-table vpn-instance vpn1 22.22.22.22 verbose 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpn1
   Summary Count : 1
   
   Destination: 22.22.22.22/32          
        Protocol: IBGP            Process ID: 0              
      Preference: 255                   Cost: 0              
         NextHop: 192.168.2.2      Neighbour: 0.0.0.0        
           State: Active Adv Relied      Age: 00h00m31s           
             Tag: 0                 Priority: low            
           Label: NULL               QoSInfo: 0x0            
      IndirectID: 0xa9          
    RelayNextHop: 192.168.2.2      Interface: GigabitEthernet0/2/0
        TunnelID: 0x0                  Flags: RD             
       BkNextHop: 2.2.2.2       BkInterface: GigabitEthernet0/3/0
         BkLabel: 0x27           SecTunnelID: 0x5000098        
    BkPETunnelID: 0x0        BkPESecTunnelID: 0x0              
    BkIndirectID: 0xaa
   ```
   
   The command output shows that after IP FRR is enabled, both PE2 and PE3 have the primary and backup routes to the loopback interface on the CE, and the backup route recurses to an LDP LSP.
   
   Run the [**shutdown**](cmdqueryname=shutdown) and then **display ip routing-table vpn-instance verbose** commands on GE0/2/0 of PE2. The command output shows that the next hop to the loopback interface on the CE is changed to PE3.
   
   ```
   <PE2> display ip routing-table vpn-instance vpn1 22.22.22.22 verbose 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpn1
   Summary Count : 1
   
   Destination: 22.22.22.22/32          
        Protocol: IBGP            Process ID: 0              
      Preference: 255                   Cost: 0              
         NextHop: 3.3.3.3          Neighbour: 0.0.0.0        
           State: Active Adv Relied      Age: 00h33m16s           
             Tag: 0                 Priority: low            
           Label: 0x23               QoSInfo: 0x0            
      IndirectID: 0xb7          
    RelayNextHop: 10.11.1.2        Interface:GigabitEthernet0/3/0
        TunnelID: 0x0000000001004c4c62 Flags: RD
   ```
   
   Perform the same operations on PE3. The command output shows similar information.
   
   It can be concluded that IP+VPNv4 hybrid FRR has taken effect on PE2 and PE3.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.252
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.20.1.1 255.255.255.252
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  interface LoopBack2
   ip binding vpn-instance vpn1
   ip address 11.11.11.11 255.255.255.255
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
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  #
   ipv4-family vpn-instance vpn1
   import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 10.10.1.0 0.0.0.3
    network 10.20.1.0 0.0.0.3
    network 1.1.1.1 0.0.0.0
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
    ip frr
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.252
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 192.168.1.1 255.255.255.252
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.11.1.1 255.255.255.252
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
  #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
  #
   ipv4-family vpn-instance vpn1
     import-route ospf 2
  #
  ospf 1
   area 0.0.0.0
    network 10.10.1.0 0.0.0.3
    network 10.11.1.0 0.0.0.3
    network 2.2.2.2 0.0.0.0
  #
  ospf 2 vpn-instance vpn1
   import-route bgp
   area 0.0.0.1 
    network 192.168.1.0 0.0.0.3
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.20.1.2 255.255.255.252
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 192.168.2.1 255.255.255.252
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.11.1.2 255.255.255.252
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100 
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100 
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
  #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
  #
   ipv4-family vpn-instance vpn1
    bestroute as-path-ignore
    auto-frr
    route-select delay 300
    peer 192.168.2.2 as-number 65410
    peer 192.168.2.2 preferred-value 600
  #
  ospf 1
   area 0.0.0.0
    network 10.20.1.0 0.0.0.3
    network 10.11.1.0 0.0.0.3
    network 3.3.3.3 0.0.0.0
  #
  return
  ```
* CE configuration file
  
  ```
  #
  sysname CE
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.252
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.252
  #
  interface LoopBack1
   ip address 22.22.22.22 255.255.255.255
  #
  bgp 65410
   peer 192.168.2.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 22.22.22.22 255.255.255.255
    peer 192.168.2.1 enable
  #
  ospf 1 
   area 0.0.0.1
    network 22.22.22.22 0.0.0.0
    network 192.168.1.0 0.0.0.3
  #
  return
  ```