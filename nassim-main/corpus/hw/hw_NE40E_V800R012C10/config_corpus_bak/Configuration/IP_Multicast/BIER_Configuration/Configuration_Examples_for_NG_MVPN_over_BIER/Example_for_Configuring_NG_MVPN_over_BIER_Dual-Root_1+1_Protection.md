Example for Configuring NG MVPN over BIER Dual-Root 1+1 Protection
==================================================================

This section provides an example for configuring NG MVPN over BIER dual-root 1+1 protection.

#### Networking Requirements

In an NG MVPN over BIER scenario shown in [Figure 1](#EN-US_TASK_0216585636__fig1347875220488), if Root1 fails, the subsequent forwarding of multicast services depends on unicast route convergence. However, this is unacceptable for multicast services that require high reliability, because the convergence takes a long time to complete. To address this problem, configure flow-based dual-root 1+1 protection. When both the primary and secondary links are working properly, the same multicast data flow is forwarded along both the primary tunnel (over the primary link) and the secondary tunnel (over the secondary link). The leaf node accepts the multicast flow received from the primary tunnel (with Root1 as the root) and discards the multicast flow received from the secondary tunnel (with Root2 as the root). If Root1 fails, the leaf node uses flow-based dual-root 1+1 protection to quickly detect the tunnel fault and accepts the multicast flow received from the secondary tunnel. Flow-based dual-root 1+1 protection accelerates the convergence of multicast services and improves reliability.

**Figure 1** NG MVPN over BIER dual-root 1+1 protection![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, and 3 in this example represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0216587215.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BGP/MPLS IP VPN to ensure that unicast VPN services are properly transmitted. In this example, MPLS LDP is configured on the public network, and IS-IS is deployed as the unicast routing protocol. In addition, an IS-IS neighbor relationship is established in a VPN instance between the CE and Root1 and between the CE and Root2.
2. Configure BIER on Root1, Root2, and the leaf node, and configure IS-IS as an underlay protocol of BIER.
3. Establish a BGP MVPN peer relationship between Root1 and the leaf node and between Root2 and the leaf node so that the peers can use BGP to transmit A-D and C-multicast routes.
4. Configure Root1 and Root2 to transmit multicast flows over BIER tunnels.
5. Enable MVPN FRR on the leaf node and set the flow-based detection mode for MVPN FRR.
6. Configure PIM-SM on the interfaces bound to the VPN instance on Root1, Root2, and the leaf node and on CE interfaces.
7. Configure a static rendezvous point (RP).

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces (shown in [Figure 1](#EN-US_TASK_0216585636__fig1347875220488))

* IS-IS process ID (1000) of the public network, and VPN instance name (**bier**) on Root1, Root2, and the leaf node
* BFR-IDs (1, 2, and 3) for Root1, Root2, and the leaf node, respectively, sub-domain ID (0), BSL (256), and Max-SI (2)
* IS-IS process ID (1000) configured on the CE, and IS-IS process ID (100) used by Root1 and Root2 to establish an IS-IS neighbor relationship with the CE in the VPN instance
* IP address (226.0.0.1) of the multicast group that users connected to Receiver join
* IBGP peer AS number (1000)

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Assign an IP address to each interface on the BGP/MPLS IP VPN backbone network and VPN.
      
      
      
      Configure an IP address for each interface. For configuration details, see Configuration Files in this section.
   2. Configure an IGP to interconnect devices on the BGP/MPLS IP VPN backbone network.
      
      
      
      This example uses IS-IS as the IGP. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
   3. Configure basic MPLS functions and enable MPLS LDP on the BGP/MPLS IP VPN backbone network.
      
      
      * # Configure Root1.
        
        ```
        [~Root1] mpls lsr-id 3.3.3.1
        ```
        ```
        [*Root1] mpls
        ```
        ```
        [*Root1-mpls] quit
        ```
        ```
        [*Root1] mpls ldp
        ```
        ```
        [*Root1-mpls-ldp] quit
        ```
        ```
        [*Root1] interface gigabitethernet0/1/1
        ```
        ```
        [*Root1-GigabitEthernet0/1/1] mpls
        ```
        ```
        [*Root1-GigabitEthernet0/1/1] mpls ldp
        ```
        ```
        [*Root1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*Root1] commit
        ```
        
        The configuration of Root2 is similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
      * # Configure the leaf node.
        
        ```
        [~Leaf] mpls lsr-id 2.2.2.1
        ```
        ```
        [*Leaf] mpls
        ```
        ```
        [*Leaf-mpls] quit
        ```
        ```
        [*Leaf] mpls ldp
        ```
        ```
        [*Leaf-mpls-ldp] quit
        ```
        ```
        [*Leaf] interface gigabitethernet0/1/0
        ```
        ```
        [*Leaf-GigabitEthernet0/1/0] mpls
        ```
        ```
        [*Leaf-GigabitEthernet0/1/0] mpls ldp
        ```
        ```
        [*Leaf-GigabitEthernet0/1/0] quit
        ```
        ```
        [*Leaf] interface gigabitethernet0/1/1
        ```
        ```
        [*Leaf-GigabitEthernet0/1/1] mpls
        ```
        ```
        [*Leaf-GigabitEthernet0/1/1] mpls ldp
        ```
        ```
        [*Leaf-GigabitEthernet0/1/1] quit
        ```
        ```
        [*Leaf] commit
        ```
   4. Establish an MP-IBGP peer relationship between Root1 and the leaf node and between Root2 and the leaf node.
      
      
      * # Configure Root1.
        
        ```
        [~Root1] bgp 1000
        ```
        ```
        [*Root1-bgp] peer 2.2.2.1 as-number 1000
        ```
        ```
        [*Root1-bgp] peer 2.2.2.1 connect-interface LoopBack1
        ```
        ```
        [*Root1-bgp] ipv4-family vpnv4
        ```
        ```
        [*Root1-bgp-af-vpnv4] peer 2.2.2.1 enable
        ```
        ```
        [*Root1-bgp-af-vpnv4] quit
        ```
        ```
        [*Root1-bgp] quit
        ```
        ```
        [*Root1] commit
        ```
        
        The configuration of Root2 is similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
      * # Configure the leaf node.
        
        ```
        [~Leaf] bgp 1000
        ```
        ```
        [*Leaf-bgp] peer 3.3.3.1 as-number 1000
        ```
        ```
        [*Leaf-bgp] peer 3.3.3.1 connect-interface LoopBack1
        ```
        ```
        [*Leaf-bgp] peer 4.4.4.1 as-number 1000
        ```
        ```
        [*Leaf-bgp] peer 4.4.4.1 connect-interface LoopBack1
        ```
        ```
        [*Leaf-bgp] ipv4-family vpnv4
        ```
        ```
        [*Leaf-bgp-af-vpnv4] peer 3.3.3.1 enable
        ```
        ```
        [*Leaf-bgp-af-vpnv4] peer 4.4.4.1 enable
        ```
        ```
        [*Leaf-bgp-af-vpnv4] quit
        ```
        ```
        [*Leaf-bgp] quit
        ```
        ```
        [*Leaf] commit
        ```
   5. Configure a VPN instance on Root1, Root2, and the leaf node.
      
      
      * # Configure Root1.
        
        ```
        [~Root1] ip vpn-instance bier
        ```
        ```
        [*Root1-vpn-instance-bier] ipv4-family
        ```
        ```
        [*Root1-vpn-instance-bier-af-ipv4] route-distinguisher 1000:10000
        ```
        ```
        [*Root1-vpn-instance-bier-af-ipv4] vpn-target 1000:1000
        ```
        ```
        [*Root1-vpn-instance-bier-af-ipv4] quit
        ```
        ```
        [*Root1-vpn-instance-bier] quit
        ```
        ```
        [*Root1] interface gigabitethernet0/1/0
        ```
        ```
        [*Root1-GigabitEthernet0/1/0] ip binding vpn-instance bier
        ```
        ```
        [*Root1-GigabitEthernet0/1/0] ip address 10.1.1.2 24
        ```
        ```
        [*Root1-GigabitEthernet0/1/0] quit
        ```
        ```
        [*Root1] commit
        ```
        
        The configurations of the leaf node and Root2 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
   6. Establish an IS-IS neighbor relationship in the VPN instance between the CE and Root1 and between the CE and Root2.
      
      
      * # Configure IS-IS on Root1 to establish an IS-IS neighbor relationship in the VPN instance, and configure IS-IS to import BGP routes.
        ```
        [*Root1] isis 100 vpn-instance bier
        ```
        ```
        [*Root1-isis-100] network-entity 10.1334.6e9f.0001.00
        ```
        ```
        [*Root1-isis-100] import-route bgp
        ```
        ```
        [*Root1-isis-100] quit
        ```
        ```
        [*Root1-bgp] quit
        ```
        ```
        [*Root1] interface gigabitethernet0/1/0
        ```
        ```
        [*Root1-GigabitEthernet0/1/0] isis enable 100
        ```
        ```
        [*Root1-GigabitEthernet0/1/0] quit
        ```
        ```
        [*Root1] commit
        ```
        
        The configuration of Root2 is similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
      * # Configure the CE.
        
        ```
        [*CE] isis 1000
        ```
        ```
        [*CE-isis-1000] network-entity 10.1234.6e9f.0001.00
        ```
        ```
        [*CE-isis-1000] quit
        ```
        ```
        [*CE] interface gigabitethernet0/1/0
        ```
        ```
        [*CE-GigabitEthernet0/1/0] isis enable 1000
        ```
        ```
        [*CE-GigabitEthernet0/1/0] quit
        ```
        ```
        [*CE] interface gigabitethernet0/1/1
        ```
        ```
        [*CE-GigabitEthernet0/1/1] isis enable 1000
        ```
        ```
        [*CE-GigabitEthernet0/1/1] quit
        ```
        ```
        [*CE] interface gigabitethernet0/1/2
        ```
        ```
        [*CE-GigabitEthernet0/1/2] isis enable 1000
        ```
        ```
        [*CE-GigabitEthernet0/1/2] quit
        ```
        ```
        [*CE] commit
        ```
   7. Configure route import on Root1, Root2, and the leaf node.
      
      
      * # Configure Root1 to import direct routes and IS-IS routes into BGP.
        
        ```
        [*Root1] bgp 1000
        ```
        ```
        [*Root1-bgp] ipv4-family vpn-instance bier
        ```
        ```
        [*Root1-bgp-bier] import-route direct
        ```
        ```
        [*Root1-bgp-bier] import-route isis 100
        ```
        ```
        [*Root1-bgp-bier] quit
        ```
        ```
        [*Root1-bgp] quit
        ```
        ```
        [*Root1] commit
        ```
        
        The configurations of the leaf node and Root2 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
2. Configure BIER on Root1, Root2, and the leaf node, and configure IS-IS as an underlay protocol of BIER.
   
   
   * # Configure Root1.
     
     ```
     [~Root1] interface LoopBack1
     ```
     ```
     [*Root1-LoopBack1] ip address 3.3.3.1 32
     ```
     ```
     [*Root1-LoopBack1] isis enable 1000
     ```
     ```
     [*Root1-LoopBack1] commit
     ```
     ```
     [~Root1-LoopBack1] quit
     ```
     ```
     [~Root1] bier
     ```
     ```
     [*Root1-bier] sub-domain 0
     ```
     ```
     [*Root1-bier-sub-domain-0] bfr-id 1
     ```
     ```
     [*Root1-bier-sub-domain-0] bfr-prefix interface loopback1
     ```
     ```
     [*Root1-bier-sub-domain-0] protocol isis
     ```
     ```
     [*Root1-bier-sub-domain-0] encapsulation-type mpls bsl 256 max-si 2
     ```
     ```
     [*Root1-bier-sub-domain-0] quit
     ```
     ```
     [*Root1-bier] quit
     ```
     ```
     [*Root1] isis 1000
     ```
     ```
     [*Root1-isis-1000] cost-style wide
     ```
     ```
     [*Root1-isis-1000] bier enable
     ```
     ```
     [*Root1-isis-1000] quit
     ```
     
     The configurations of the leaf node and Root2 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
3. Establish a BGP MVPN peer relationship between Root1 and the leaf node and between Root2 and the leaf node.
   
   
   * # Configure Root1.
     
     ```
     [~Root1] bgp 1000
     ```
     ```
     [*Root1-bgp] ipv4-family mvpn
     ```
     ```
     [*Root1-bgp-af-mvpn] peer 2.2.2.1 enable
     ```
     ```
     [*Root1-bgp-af-mvpn] commit
     ```
     ```
     [~Root1-bgp-af-mvpn] quit
     ```
     ```
     [~Root1-bgp] quit
     ```
     
     The configurations of the leaf node and Root2 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
   
   After completing the configurations, run the [**display bgp mvpn all peer**](cmdqueryname=display+bgp+mvpn+all+peer) command on the leaf node to check information about BGP MVPN peer relationships. The command output shows that the leaf node has established a BGP MVPN peer relationship with Root1 and Root2.
   
   ```
   [~Leaf] display bgp mvpn all peer
   ```
   ```
    BGP local router ID : 2.2.2.1
    Local AS number : 1000
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     3.3.3.1         4        1000      163      165     0 02:10:22 Established        4
     4.4.4.1         4        1000      288      289     0 03:44:42 Established        4
   
   ```
4. Configure Root1 and Root2 to transmit multicast flows over BIER tunnels.
   
   
   * # Configure Root1.
     
     ```
     [~Root1] multicast mvpn 3.3.3.1
     ```
     ```
     [*Root1] ip vpn-instance bier
     ```
     ```
     [*Root1-vpn-instance-bier] ipv4-family
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4] multicast routing-enable
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4] mvpn
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4-mvpn] sender-enable
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4-mvpn] rpt-spt mode
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4-mvpn] ipmsi-tunnel
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4-mvpn-ipmsi] bier
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4-mvpn-ipmsi] quit
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4-mvpn] quit
     ```
     ```
     [*Root1-vpn-instance-bier-af-ipv4] quit
     ```
     ```
     [*Root1-vpn-instance-bier] quit
     ```
     ```
     [*Root1] commit
     ```
     
     The configuration of Root2 is similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
5. Enable MVPN FRR on the leaf node and set the flow-based detection mode for MVPN FRR.
   
   
   * # Configure the leaf node.
     
     ```
     [~Leaf] ip vpn-instance bier 
     ```
     ```
     [~Leaf-vpn-instance-bier] ipv4-family 
     ```
     ```
     [~Leaf-vpn-instance-bier-af-ipv4] vpn frr 
     ```
     ```
     [*Leaf-vpn-instance-bier-af-ipv4] quit 
     ```
     ```
     [*Leaf-vpn-instance-bier] quit 
     ```
     ```
     [*Leaf] commit
     ```
     ```
     [~Leaf] acl number 2166
     ```
     ```
     [*Leaf-acl4-basic-2166] rule 5 permit
     ```
     ```
     [*Leaf-acl4-basic-2166] quit
     ```
     ```
     [*Leaf] multicast mvpn 2.2.2.1
     ```
     ```
     [*Leaf] ip vpn-instance bier
     ```
     ```
     [*Leaf-vpn-instance-bier] ipv4-family
     ```
     ```
     [*Leaf-vpn-instance-bier-af-ipv4] multicast routing-enable
     ```
     ```
     [*Leaf-vpn-instance-bier-af-ipv4] mvpn
     ```
     ```
     [*Leaf-vpn-instance-bier-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*Leaf-vpn-instance-bier-af-ipv4-mvpn] c-multicast frr
     ```
     ```
     [*Leaf-vpn-instance-bier-af-ipv4-mvpn] c-multicast frr flow-detection-based 2166
     ```
     ```
     [*Leaf-vpn-instance-bier-af-ipv4-mvpn] rpt-spt mode
     ```
     ```
     [*Leaf-vpn-instance-bier-af-ipv4-mvpn] quit
     ```
     ```
     [*Leaf-vpn-instance-bier-af-ipv4] quit
     ```
     ```
     [*Leaf-vpn-instance-bier] quit
     ```
     ```
     [*Leaf] commit
     ```
6. Configure PIM-SM on the interfaces bound to the VPN instance on Root1, Root2, and the leaf node and on CE interfaces.
   
   
   * # Configure Root1.
     
     ```
     [~Root1] interface gigabitethernet0/1/0
     ```
     ```
     [*Root1-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*Root1-GigabitEthernet0/1/0] quit
     ```
     ```
     [*Root1] commit
     ```
     
     The configurations of the leaf node and Root2 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
   * # Configure the CE.
     
     ```
     [~CE] interface gigabitethernet0/1/0
     ```
     ```
     [*CE-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*CE-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE] interface gigabitethernet0/1/1
     ```
     ```
     [*CE-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*CE-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE] interface gigabitethernet0/1/2
     ```
     ```
     [*CE-GigabitEthernet0/1/2] pim sm
     ```
     ```
     [*CE-GigabitEthernet0/1/2] quit
     ```
     ```
     [*CE] commit
     ```
7. Configure a static RP.
   
   
   * # Configure Root1.
     ```
     [~Root1] pim vpn-instance bier
     ```
     ```
     [*Root1-pim-bier] static-rp 10.1.5.2
     ```
     ```
     [*Root1-pim-bier] quit
     ```
     ```
     [*Root1-pim-bier] commit
     ```
     
     The configurations of the leaf node and Root2 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0216585636__example_dc_vrp_cfg_ngmvpn_001301) in this section.
   
   
   * # Configure the CE.
     ```
     [~CE] pim 
     ```
     ```
     [*CE-pim] static-rp 10.1.5.2
     ```
     ```
     [*CE-pim] quit
     ```
     ```
     [*CE-pim] commit
     ```
8. Verify the configuration.
   
   
   
   If users connected to Receiver join the multicast group, Source uses the BGP/MPLS IP VPN to forward multicast data to the users.
   
   Run the [**display pim vpn-instance**](cmdqueryname=display+pim+vpn-instance) **routing-table** command on the receiver leaf node to check the PIM routing table of the VPN instance.
   
   ```
   [~Leaf]display pim vpn-instance bier routing-table
    VPN-Instance: bier
    Total 1 (*, G) entry; 1 (S, G) entry
   
    (*, 226.0.0.1)
        RP: 10.1.5.2 
        Protocol: pim-sm, Flag: WC 
        UpTime: 00:42:24
        Upstream interface: GigabitEthernet0/1/2, Refresh time: 00:42:24
            Upstream neighbor: 10.1.5.2
            RPF prime neighbor: 10.1.5.2
        Downstream interface(s) information: none
   
    (10.1.6.100, 226.0.0.1)
        RP: 10.1.5.2 
        Protocol: pim-sm, Flag: RPT SPT ACT BGP 
        UpTime: 00:37:45
        Upstream interface: through-BGP, Refresh time: 00:37:45
            Upstream neighbor: 3.3.3.1
            RPF prime neighbor: 3.3.3.1
        Backup upstream interface: through-BGP
            Backup upstream neighbor: 4.4.4.1
            Backup RPF prime neighbor: 4.4.4.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/2
                Protocol: pim-sm, UpTime: 00:37:45, Expires: -
   ```
   
   The preceding command output shows that the IP address of the upstream neighbor on the primary link and that on the secondary link is 3.3.3.1 and 4.4.4.1, respectively. In normal cases, the leaf node receives a multicast flow from both links and accepts the multicast flow received from the primary link based on its PIM routing table. If the primary link fails, the leaf node accepts the multicast flow received from the secondary link.

#### Configuration Files

* CE configuration file
  
  ```
  #
  sysname CE
  #
  multicast routing-enable
  #
  isis 1000
   network-entity 10.1234.6e9f.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   pim sm
   isis enable 1000
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   pim sm
   isis enable 1000
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.6.1 255.255.255.0
   pim sm
   isis enable 1000
  #
  pim
   static-rp 10.1.5.2
  #
  return
  ```
* Root1 configuration file
  
  ```
  #
  sysname Root1
  #
  multicast mvpn 3.3.3.1
  #
  ip vpn-instance bier
   ipv4-family
    route-distinguisher 1000:10000
    apply-label per-instance
    vpn-target 1000:1000 export-extcommunity
    vpn-target 1000:1000 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     rpt-spt mode
     ipmsi-tunnel
      bier   
  #
  mpls lsr-id 3.3.3.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 100 vpn-instance bier
   network-entity 10.1334.6e9f.0001.00
   import-route bgp
  #
  isis 1000
   cost-style wide
   network-entity 10.1234.8e9f.0001.00
   bier enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance bier
   ip address 10.1.1.2 255.255.255.0
   pim sm
   igmp enable
   isis enable 100
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   isis enable 1000
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.1 255.255.255.255
   isis enable 1000
  #
  bgp 1000
   peer 2.2.2.1 as-number 1000
   peer 2.2.2.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 2.2.2.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.1 enable
   #
   ipv4-family vpn-instance bier
    import-route direct
    import-route isis 100
  #
  pim vpn-instance bier
   static-rp 10.1.5.2
  #
  bier
   sub-domain 0
    bfr-id 1
    bfr-prefix interface LoopBack1
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  return
  ```
* Root2 configuration file
  ```
  #
  sysname Root2
  #
  multicast mvpn 4.4.4.1
  #
  ip vpn-instance bier
   ipv4-family
    route-distinguisher 1000:1000
    apply-label per-instance
    vpn-target 1000:1000 export-extcommunity
    vpn-target 1000:1000 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     rpt-spt mode
     ipmsi-tunnel
      bier   
  #
  mpls lsr-id 4.4.4.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 100 vpn-instance bier
   network-entity 10.1434.6e9f.0001.00
   import-route bgp
  #
  isis 1000
   cost-style wide
   network-entity 10.1234.9e9f.0001.00
   bier enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance bier
   ip address 10.1.2.2 255.255.255.0
   pim sm
   isis enable 100
   undo dcn
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   isis enable 1000
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.1 255.255.255.255
   isis enable 1000
  #
  bgp 1000
   peer 2.2.2.1 as-number 1000
   peer 2.2.2.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 2.2.2.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.1 enable
   #
   ipv4-family vpn-instance bier
    import-route direct
    import-route isis 100
  #
  pim vpn-instance bier
   static-rp 10.1.5.2
  #
  bier
   sub-domain 0
    bfr-id 2
    bfr-prefix interface LoopBack1
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  return
  ```
* Leaf configuration file
  ```
  #
  sysname Leaf
  #
  multicast mvpn 2.2.2.1
  #
  ip vpn-instance bier
   ipv4-family
    vpn frr
    route-distinguisher 72:72
    apply-label per-instance
    vpn-target 1000:1000 export-extcommunity
    vpn-target 1000:1000 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     c-multicast frr
     c-multicast frr flow-detection-based 2166
     rpt-spt mode
  #
  mpls lsr-id 2.2.2.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  acl number 2166
   rule 5 permit
  #
  isis 1000
   cost-style wide
   network-entity 10.1234.7e9f.0001.00
   traffic-eng level-2
   bier enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   isis enable 1000
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.4.2 255.255.255.0
   isis enable 1000
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance bier
   ip address 10.1.5.2 255.255.255.0
   pim sm
   igmp enable
   igmp static-group 226.0.0.1
  #
  interface LoopBack1
   ip address 2.2.2.1 255.255.255.255
   isis enable 1000
  #
  bgp 1000
   peer 3.3.3.1 as-number 1000
   peer 3.3.3.1 connect-interface LoopBack1
   peer 4.4.4.1 as-number 1000
   peer 4.4.4.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.1 enable
    peer 4.4.4.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 3.3.3.1 enable
    peer 4.4.4.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.1 enable
    peer 4.4.4.1 enable
   #
   ipv4-family vpn-instance bier
    import-route direct
    auto-frr
  #
  pim vpn-instance bier
   static-rp 10.1.5.2
  #
  bier
   sub-domain 0
    bfr-id 3
    bfr-prefix interface LoopBack1
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  return
  ```