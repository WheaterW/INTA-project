Example for Configuring mLDP In-Band MVPN Dual-Root 1+1 Protection
==================================================================

This section provides an example for configuring mLDP in-band MVPN dual-root 1+1 protection.

#### Networking Requirements

If a sender PE fails in a scenario where mLDP in-band MVPN is configured, C-multicast services are interrupted. Multicast services can rely only on unicast convergence for recovery. However, unicast convergence takes a long time, which is unacceptable to the multicast services that have high reliability requirements. To resolve this problem, you can configure dual-root 1+1 protection. On the network shown in [Figure 1](#EN-US_TASK_0000001270434277__fig_dc_vrp_cfg_ngmvpn_002201), a primary mLDP P2MP tunnel is established with PE1 as the root node, and a backup mLDP P2MP tunnel is established with PE2 as the root node. When links are working properly, multicast traffic is forwarded through both the primary and backup tunnels bidirectionally. The leaf node PE3 selects the multicast traffic received from the primary tunnel and discards the multicast traffic received from the backup tunnel. If the root node PE1 fails, the leaf node selects the data received from the backup tunnel through the C-multicast FRR function. This speeds up the convergence of multicast services and improves reliability.

**Figure 1** mLDP in-band MVPN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001225514448.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BGP/MPLS IP VPN and ensure that the unicast VPN works properly and unicast routes between the sender PE and receiver PEs are reachable.
2. Enable mLDP globally on all PEs so that they can use mLDP to establish P2MP tunnels.
3. Enable mLDP in-band MVPN on PE3 to trigger mLDP P2MP tunnel establishment.
4. Configure VPN FRR on PE3.
5. Configure PIM on the PEs' interfaces bound to a VPN instance and on the CEs' interfaces connected to the PEs so that VPN multicast routing entries are generated for multicast traffic forwarding.
6. Configure IGMP on the multicast device's interface that is connected to the user network segment to manage multicast group members on that network segment.

#### Data Preparation

To complete the configuration, you need the following data.

* IS-IS process ID: 1
* VPN instance name on PE1 and PE2: VPNA; other data shown in [Table 1](#EN-US_TASK_0000001270434277__table_dc_vrp_cfg_ngmvpn_002201)
  
  **Table 1** Data needed for each device
  | Device | Address of Loopback 1 | MPLS LSR-ID | MVPN ID | RD | VPN-Target | AS Number |
  | --- | --- | --- | --- | --- | --- | --- |
  | CE1 | 1.1.1.1 | - | - | - | - | AS 65001 |
  | PE1 | 2.2.2.2 | 2.2.2.2 | 2.2.2.2 | 200:1 | 3:3 | AS 100 |
  | PE2 | 3.3.3.3 | 3.3.3.3 | 3.3.3.3 | 300:1 | 3:3 | AS 100 |
  | PE3 | 4.4.4.4 | 4.4.4.4 | 4.4.4.4 | 400:1 | 3:3 | AS 100 |
  | CE2 | 5.5.5.5 | - | - | - | - | AS 65002 |

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Assign an IP address to each interface of devices on the backbone network and VPN sites.
      
      
      
      Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0000001270434277__fig_dc_vrp_cfg_ngmvpn_002201). For configuration details, see [Configuration Files](#EN-US_TASK_0000001270434277__example_dc_vrp_cfg_ngmvpn_002201) in this section.
   2. Configure an IGP for interworking on the BGP/MPLS IP VPN backbone network.
      
      
      
      IS-IS is used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270434277__example_dc_vrp_cfg_ngmvpn_002201) in this section.
   3. Configure basic MPLS functions and MPLS LDP on the MPLS backbone network to establish LDP LSPs.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] mpls lsr-id 2.2.2.2
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
        [*PE1] interface gigabitethernet0/1/0
        ```
        ```
        [*PE1-GigabitEthernet0/1/0] mpls
        ```
        ```
        [*PE1-GigabitEthernet0/1/0] mpls ldp
        ```
        ```
        [*PE1-GigabitEthernet0/1/0] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] mpls lsr-id 3.3.3.3
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
        [*PE2] interface gigabitethernet0/1/1
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] mpls
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] mpls ldp
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure PE3.
        
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
        [*PE3-mpls-ldp] quit
        ```
        ```
        [*PE3] interface gigabitethernet0/1/1
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] mpls
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] mpls ldp
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE3] interface gigabitethernet0/1/2
        ```
        ```
        [*PE3-GigabitEthernet0/1/2] mpls
        ```
        ```
        [*PE3-GigabitEthernet0/1/2] mpls ldp
        ```
        ```
        [*PE3-GigabitEthernet0/1/2] quit
        ```
        ```
        [*PE3] commit
        ```
   4. Establish an MP-IBGP peer relationship between the PEs.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] bgp 100
        ```
        ```
        [*PE1-bgp] peer 4.4.4.4 as-number 100
        ```
        ```
        [*PE1-bgp] peer 4.4.4.4 connect-interface LoopBack1
        ```
        ```
        [*PE1-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE1-bgp-af-vpnv4] peer 4.4.4.4 enable
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
      * # Configure PE2.
        
        ```
        [~PE2] bgp 100
        ```
        ```
        [*PE2-bgp] peer 4.4.4.4 as-number 100
        ```
        ```
        [*PE2-bgp] peer 4.4.4.4 connect-interface LoopBack1
        ```
        ```
        [*PE2-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE2-bgp-af-vpnv4] peer 4.4.4.4 enable
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
      * # Configure PE3.
        
        ```
        [~PE3] bgp 100
        ```
        ```
        [*PE3-bgp] peer 2.2.2.2 as-number 100
        ```
        ```
        [*PE3-bgp] peer 2.2.2.2 connect-interface LoopBack1
        ```
        ```
        [*PE3-bgp] peer 3.3.3.3 as-number 100
        ```
        ```
        [*PE3-bgp] peer 3.3.3.3 connect-interface LoopBack1
        ```
        ```
        [*PE3-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE3-bgp-af-vpnv4] peer 2.2.2.2 enable
        ```
        ```
        [*PE3-bgp-af-vpnv4] peer 3.3.3.3 enable
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
   5. Configure a VPN instance on the PEs.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] ip vpn-instance VPNA
        ```
        ```
        [*PE1-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv4] route-distinguisher 200:1
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv4] vpn-target 3:3
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv4] quit
        ```
        ```
        [*PE1-vpn-instance-VPNA] quit
        ```
        ```
        [*PE1] interface gigabitethernet0/1/1
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] ip address 192.168.1.2 24
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] ip vpn-instance VPNA
        ```
        ```
        [*PE2-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv4] route-distinguisher 300:1
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv4] vpn-target 3:3
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv4] quit
        ```
        ```
        [*PE2-vpn-instance-VPNA] quit
        ```
        ```
        [*PE2] interface gigabitethernet0/1/2
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] ip binding vpn-instance VPNA
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] ip address 192.168.2.2 24
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure PE3.
        
        ```
        [~PE3] ip vpn-instance VPNA
        ```
        ```
        [*PE3-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*PE3-vpn-instance-VPNA-af-ipv4] route-distinguisher 400:1
        ```
        ```
        [*PE3-vpn-instance-VPNA-af-ipv4] vpn-target 3:3
        ```
        ```
        [*PE3-vpn-instance-VPNA-af-ipv4] quit
        ```
        ```
        [*PE3-vpn-instance-VPNA] quit
        ```
        ```
        [*PE3] interface gigabitethernet0/1/0
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] ip binding vpn-instance VPNA
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] ip address 192.168.3.1 24
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] quit
        ```
        ```
        [*PE3] commit
        ```
   6. Configure IS-IS on the PEs and import IS-IS routes into the BGP VPN instance.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] isis 1 vpn-instance VPNA
        ```
        ```
        [*PE1-isis-1] is-level level-2
        ```
        ```
        [*PE1-isis-1] network-entity 10.0000.0000.0002.00
        ```
        ```
        [*PE1-isis-1] import-route bgp
        ```
        ```
        [*PE1-isis-1] quit
        ```
        ```
        [*PE1] isis 2
        ```
        ```
        [*PE1-isis-2] is-level level-2
        ```
        ```
        [*PE1-isis-2] network-entity 10.0000.0000.0006.00
        ```
        ```
        [*PE1-isis-2] quit
        ```
        ```
        [*PE1] interface gigabitethernet0/1/1
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] isis enable 1
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE1] bgp 100
        ```
        ```
        [*PE1-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*PE1-bgp-VPNA] import-route isis 1
        ```
        ```
        [*PE1-bgp-VPNA] quit
        ```
        ```
        [*PE1-bgp] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] isis 1 vpn-instance VPNA
        ```
        ```
        [*PE2-isis-1] is-level level-2
        ```
        ```
        [*PE2-isis-1] network-entity 10.0000.0000.0003.00
        ```
        ```
        [*PE2-isis-1] import-route bgp
        ```
        ```
        [*PE2-isis-1] quit
        ```
        ```
        [*PE2] isis 2
        ```
        ```
        [*PE2-isis-2] is-level level-2
        ```
        ```
        [*PE2-isis-2] network-entity 10.0000.0000.0007.00
        ```
        ```
        [*PE2-isis-2] quit
        ```
        ```
        [*PE2] interface GigabitEthernet0/1/1
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] isis enable 1
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE2] bgp 100
        ```
        ```
        [*PE2-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*PE2-bgp-VPNA] import-route isis 1
        ```
        ```
        [*PE2-bgp-VPNA] quit
        ```
        ```
        [*PE2-bgp] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure PE3.
        
        ```
        [~PE3] isis 1 vpn-instance VPNA
        ```
        ```
        [*PE3-isis-1] is-level level-2
        ```
        ```
        [*PE3-isis-1] network-entity 10.0000.0000.0004.00
        ```
        ```
        [*PE3-isis-1] import-route bgp
        ```
        ```
        [*PE3-isis-1] quit
        ```
        ```
        [*PE3] isis 2
        ```
        ```
        [*PE3-isis-2] is-level level-2
        ```
        ```
        [*PE3-isis-2] network-entity 10.0000.0000.0008.00
        ```
        ```
        [*PE3-isis-2] quit
        ```
        ```
        [*PE3] bgp 100
        ```
        ```
        [*PE3-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*PE3-bgp-VPNA] import-route isis 1
        ```
        ```
        [*PE3-bgp-VPNA] quit
        ```
        ```
        [*PE3-bgp] quit
        ```
        ```
        [*PE3] commit
        ```
   7. Configure VPN FRR on PE3. After this step is performed, traffic can be immediately switched to the backup link if the primary link fails.
      
      
      ```
      [~PE3] bgp 100
      [*PE3-bgp] ipv4-family vpn-instance VPNA
      [*PE3-bgp-VPNA] auto-frr
      [*PE3-bgp-VPNA] quit
      [*PE3-bgp] quit
      [*PE3] commit
      ```
   8. Configure IS-IS on the CEs.
      
      
      * # Configure CE1.
        
        ```
        [~CE1] isis 1
        ```
        ```
        [*CE1-isis-1] is-level level-2
        ```
        ```
        [*CE1-isis-1] network-entity 10.0000.0000.0001.00
        ```
        ```
        [*CE1-isis-1] quit
        ```
        ```
        [*CE1] interface gigabitethernet0/1/1
        ```
        ```
        [*CE1-GigabitEthernet0/1/1] isis enable 1
        ```
        ```
        [*CE1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*CE1] interface gigabitethernet0/1/2
        ```
        ```
        [*CE1-GigabitEthernet0/1/2] isis enable 1
        ```
        ```
        [*CE1-GigabitEthernet0/1/2] quit
        ```
        ```
        [*CE1] commit
        ```
      * # Configure CE2.
        
        ```
        [~CE2] isis 1
        ```
        ```
        [*CE2-isis-1] is-level level-2
        ```
        ```
        [*CE2-isis-1] network-entity 10.0000.0000.0005.00
        ```
        ```
        [*CE2-isis-1] quit
        ```
        ```
        [*CE2] interface gigabitethernet0/1/0
        ```
        ```
        [*CE2-GigabitEthernet0/1/0] isis enable 1
        ```
        ```
        [*CE2-GigabitEthernet0/1/0] quit
        ```
        ```
        [*CE2] commit
        ```
      
      After the preceding configurations are completed, run the [**display ip routing-table vpn-instance verbose**](cmdqueryname=display+ip+routing-table+vpn-instance+verbose) command on PE3. The command output shows a backup unicast route to the multicast source.
      
      ```
      [~PE3] display ip routing-table vpn-instance VPNA 10.1.3.0 verbose
      ```
      ```
      Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
      ------------------------------------------------------------------------------
      Routing Table : VPNA
      Summary Count : 1
      
      Destination: 10.1.3.0/24
           Protocol: IBGP            Process ID: 0
         Preference: 255                   Cost: 0
            NextHop: 2.2.2.2          Neighbour: 0.0.0.0
              State: Active Adv Relied      Age: 00h14m34s
                Tag: 0                 Priority: low
              Label: 32829              QoSInfo: 0x0
         IndirectID: 0xF60000B5       Instance:         
       RelayNextHop: 0.0.0.0          Interface: GigabitEthernet0/1/1
           TunnelID: 0x000000000300000001 Flags: RD
        RouterColor: 0
          BkNextHop: 3.3.3.3        BkInterface: GigabitEthernet0/1/2
            BkLabel: 32829          SecTunnelID: 0x0
       BkPETunnelID: 0x000000000300000002 BkPESecTunnelID: 0x0
       BkIndirectID: 0xF60000B6                            
      ```
2. Enable mLDP globally.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] mpls ldp
     ```
     ```
     [*PE1-mpls-ldp] mldp p2mp
     ```
     ```
     [*PE1-mpls-ldp] commit
     ```
     ```
     [~PE1-mpls-ldp] quit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] mpls ldp
     ```
     ```
     [*PE2-mpls-ldp] mldp p2mp
     ```
     ```
     [*PE2-mpls-ldp] commit
     ```
     ```
     [~PE2-mpls-ldp] quit
     ```
   * # Configure PE3.
     
     ```
     [~PE3] mpls ldp
     ```
     ```
     [*PE3-mpls-ldp] mldp p2mp
     ```
     ```
     [*PE3-mpls-ldp] commit
     ```
     ```
     [~PE3-mpls-ldp] quit
     ```
3. Configure mLDP in-band MVPN.
   
   
   
   # Configure PE1.
   
   
   
   ```
   [~PE1] ip vpn-instance VPNA
   ```
   ```
   [*PE1-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4] multicast inband-signaling mldp
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance VPNA
   ```
   ```
   [*PE2-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv4] multicast inband-signaling mldp
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-VPNA] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ip vpn-instance VPNA
   ```
   ```
   [*PE3-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4] multicast inband-signaling mldp frr
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA] quit
   ```
   ```
   [*PE3] commit
   ```
4. Configure PIM.
   
   
   * # Configure PE1.
     
     ```
     [*PE1] interface gigabitethernet0/1/1
     ```
     ```
     [*PE1-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*PE1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure CE1.
     
     ```
     [~CE1] multicast routing-enable
     ```
     ```
     [*CE1] interface gigabitethernet0/1/0
     ```
     ```
     [*CE1-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE1] interface gigabitethernet0/1/1
     ```
     ```
     [*CE1-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE1] interface gigabitethernet0/1/2
     ```
     ```
     [*CE1-GigabitEthernet0/1/2] pim sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/2] quit
     ```
     ```
     [*CE1] commit
     ```
   * # Configure PE2.
     
     ```
     [*PE2] interface gigabitethernet0/1/2
     ```
     ```
     [*PE2-GigabitEthernet0/1/2] pim sm
     ```
     ```
     [*PE2-GigabitEthernet0/1/2] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure CE2.
     
     ```
     [~CE2] multicast routing-enable
     ```
     ```
     [*CE2] interface gigabitethernet0/1/0
     ```
     ```
     [*CE2-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*CE2-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE2] interface gigabitethernet0/1/1
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE2] commit
     ```
   * # Configure PE3.
     
     ```
     [*PE3] interface gigabitethernet0/1/0
     ```
     ```
     [*PE3-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*PE3-GigabitEthernet0/1/0] quit
     ```
     ```
     [*PE3] commit
     ```
5. Configure IGMP.
   
   
   ```
   [~CE2] interface gigabitethernet0/1/1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] igmp enable
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] igmp version 3
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] commit
   ```
6. Verify the configuration.
   
   
   
   After the preceding configurations are completed, mLDP in-band MVPN has been configured. If CE2 has access users, CE1 can use the BGP/MPLS IP VPN to forward multicast data to the users. In this example, a static multicast entry is generated on CE2 for users to join the multicast group 225.1.1.1 and receive data from the multicast source 10.1.3.2. In this case, you can check the multicast routing entries.
   
   # Run the **display pim** **vpn-instance** **routing-table** command on PE3 to check its PIM routing table.
   ```
   [~PE3] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.1.3.2, 225.1.1.1)
        RP: NULL
        Protocol: pim-sm, Flag: SPT SG_RCVR
        UpTime: 03:12:27
        Upstream interface: through-MLDP, Refresh time: 03:12:27
            Upstream neighbor: 2.2.2.2
            RPF prime neighbor: 2.2.2.2
        Backup upstream interface: through-MLDP
            Backup Upstream neighbor: 3.3.3.3
            Backup RPF prime neighbor: 3.3.3.3
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/0
                Protocol: static, UpTime: 03:12:27, Expires: 00:03:05 
   ```

#### Configuration Files

* CE1
  
  ```
  #
  sysname CE1
  #
  multicast routing-enable
  #
  isis 1
    is-level level-2
    network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   isis enable 1
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   isis enable 1
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   isis enable 1
   pim sm
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  return
  ```
* PE1
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    multicast inband-signaling mldp
  #
  mpls lsr-id 2.2.2.2
  #
  mpls ldp
   mldp p2mp
  #
  isis 1 vpn-instance VPNA
   is-level level-2
   network-entity 10.0000.0000.0002.00
   import-route bgp 
  #
  isis 2
    is-level level-2
    network-entity 10.0000.0000.0006.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 2
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.1.2 255.255.255.0
   isis enable 1
   pim sm
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance VPNA
    import-route isis 1
  #
  return
  ```
* PE2
  
  ```
  #
  sysname PE2
  #
  multicast mvpn 3.3.3.3
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 300:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    multicast inband-signaling mldp
  #
  mpls lsr-id 3.3.3.3
  #
  mpls ldp
   mldp p2mp
  #
  isis 1 vpn-instance VPNA
   is-level level-2
   network-entity 10.0000.0000.0003.00
   import-route bgp
  #
  isis 2
    is-level level-2
    network-entity 10.0000.0000.0007.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   isis enable 2
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.2.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance VPNA
    import-route isis 1
  #
  return
  ```
* PE3
  
  ```
  #
  sysname PE3
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 400:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    multicast inband-signaling mldp frr
  #
  mpls lsr-id 4.4.4.4    
  #
  mpls ldp
   mldp p2mp
  #
  isis 1 vpn-instance VPNA
    is-level level-2
    network-entity 10.0000.0000.0004.00
    import-route bgp
  #
  isis 2
    is-level level-2
    network-entity 10.0000.0000.0008.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.3.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   isis enable 2
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   isis enable 2
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
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
   ipv4-family vpn-instance VPNA
    import-route isis 1
    auto-frr
  #
  return
  ```
* CE2
  
  ```
  #
  sysname CE2
  #
  multicast routing-enable
  #
  isis 1
    is-level level-2
    network-entity 10.0000.0000.0005.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.3.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
  #
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
  #
  return
  ```