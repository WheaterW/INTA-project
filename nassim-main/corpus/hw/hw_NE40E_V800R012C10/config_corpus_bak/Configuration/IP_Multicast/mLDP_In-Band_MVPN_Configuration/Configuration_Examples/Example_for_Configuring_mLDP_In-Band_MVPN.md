Example for Configuring mLDP In-Band MVPN
=========================================

Example_for_Configuring_mLDP_In-Band_MVPN

#### Context

This section provides an example for configuring mLDP in-band MVPN.


#### Networking Requirements

mLDP in-band MVPN is deployed on a service provider's backbone network to solve multicast service issues related to traffic congestion, reliability, and security. In the mLDP in-band MVPN networking shown in [Figure 1](#EN-US_TASK_0000001270154509__fig_dc_vrp_cfg_ngmvpn_002201), BGP/MPLS IP VPN services carried by MPLS LDP tunnels have been deployed. It is required that MVPN services be provided for users over the existing IPv4 network and that users implement access through the IPv4 network.

**Figure 1** mLDP in-band MVPN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0000001270194557.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BGP/MPLS IP VPN and ensure that the unicast VPN works properly and unicast routes between the sender PE and receiver PEs are reachable.
2. Enable mLDP globally on all PEs so that they can use mLDP to establish P2MP tunnels.
3. Enable mLDP in-band MVPN on PE2 to trigger mLDP P2MP tunnel establishment.
4. Configure PIM on the PEs' interfaces bound to a VPN instance and on the CEs' interfaces connected to the PEs so that VPN multicast routing entries are generated for multicast traffic forwarding.
5. Configure IGMP on the multicast device's interface that is connected to the user network segment to manage multicast group members on that network segment.

#### Data Preparation

To complete the configuration, you need the following data.

* IS-IS process ID: 1
* VPN instance name on PE1: VPNA; other data shown in [Table 1](#EN-US_TASK_0000001270154509__table_dc_vrp_cfg_ngmvpn_002201)
  
  **Table 1** Data needed for each device
  | Device | IP Address of Loopback 1 | MPLS LSR-ID | MVPN ID | RD | VPN-Target | AS Number |
  | --- | --- | --- | --- | --- | --- | --- |
  | CE1 | 1.1.1.1 | - | - | - | - | AS 65001 |
  | PE1 | 2.2.2.2 | 2.2.2.2 | 2.2.2.2 | 200:1 | 3:3 | AS 100 |
  | PE2 | 4.4.4.4 | 4.4.4.4 | 4.4.4.4 | 400:1 | 3:3 | AS 100 |
  | CE2 | 5.5.5.5 | - | - | - | - | AS 65002 |

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Assign an IP address to each interface of devices on the backbone network and VPN sites.
      
      
      
      Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0000001270154509__fig_dc_vrp_cfg_ngmvpn_002201). For configuration details, see [Configuration Files](#EN-US_TASK_0000001270154509__example_dc_vrp_cfg_ngmvpn_002201) in this section.
   2. Configure an IGP for interworking on the BGP/MPLS IP VPN backbone network.
      
      
      
      IS-IS is used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270154509__example_dc_vrp_cfg_ngmvpn_002201) in this section.
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
        [~PE2] mpls lsr-id 4.4.4.4
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
        [*PE2] commit
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
        [*PE2-bgp] peer 2.2.2.2 as-number 100
        ```
        ```
        [*PE2-bgp] peer 2.2.2.2 connect-interface LoopBack1
        ```
        ```
        [*PE2-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE2-bgp-af-vpnv4] peer 2.2.2.2 enable
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
        [*PE2-vpn-instance-VPNA-af-ipv4] route-distinguisher 400:1
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
        [*PE2] interface gigabitethernet0/1/0
        ```
        ```
        [*PE2-GigabitEthernet0/1/0] ip binding vpn-instance VPNA
        ```
        ```
        [*PE2-GigabitEthernet0/1/0] ip address 192.168.3.1 24
        ```
        ```
        [*PE2-GigabitEthernet0/1/0] quit
        ```
        ```
        [*PE2] commit
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
        [*PE1] interface gigabitethernet 0/1/1
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
        [*PE2-isis-1] network-entity 10.0000.0000.0004.00
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
        [*PE2-isis-2] network-entity 10.0000.0000.0008.00
        ```
        ```
        [*PE2-isis-2] quit
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
   7. Configure IS-IS on the CEs.
      
      
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
      
      After completing the configurations, run the [**display ip routing-table vpn-instance verbose**](cmdqueryname=display+ip+routing-table+vpn-instance+verbose) command on PE2.
      
      ```
      [~PE2] display ip routing-table vpn-instance VPNA 10.1.3.0 verbose
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
     [*CE1] commit
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
   * # Configure PE2.
     
     ```
     [*PE2] interface gigabitethernet0/1/0
     ```
     ```
     [*PE2-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*PE2-GigabitEthernet0/1/0] quit
     ```
     ```
     [*PE2] commit
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
   
   # Run the **display pim** **vpn-instance** **routing-table** command on PE2 to check its PIM routing table.
   ```
   [~PE2] display pim vpn-instance VPNA routing-table
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
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 400:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    multicast inband-signaling mldp
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
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance VPNA
    import-route isis 1
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