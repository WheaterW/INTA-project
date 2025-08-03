Example for Configuring NG MVPN over BIER
=========================================

This section provides an example for configuring NG MVPN over BIER.

#### Networking Requirements

An NG MVPN is deployed on the service provider's backbone network to solve multicast service issues related to traffic congestion, transmission reliability, and data security. On the network shown in [Figure 1](#EN-US_TASK_0178516032__fig35284409229), MPLS LDP LSPs have been established to carry BGP/MPLS IP VPN services. The service provider wants to provide MVPN services for users based on the existing network. To meet this requirement, configure NG MVPN over BIER.

**Figure 1** NG MVPN over BIER networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0270989598.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BGP/MPLS IP VPN to ensure that unicast VPN services are properly transmitted. In this example, MPLS LDP is configured on the public network.
2. Configure BIER on Root, Leaf 1, Leaf 2, and P, and enable BIER in IS-IS.
3. Enable all PEs to establish BGP MVPN peer relationships and configure BGP to transmit A-D and C-multicast routes.
4. Configure Root, Leaf 1, and Leaf 2 to transmit multicast traffic over BIER tunnels.
5. Configure PIM on the PE interfaces bound to VPN instances on Root, Leaf 1, and Leaf 2 and on CEs' interfaces connected to PEs to allow a VPN multicast routing table to be established to guide multicast traffic forwarding.
6. Configure the address pool range and criteria for switching between I-PMSI and S-PMSI tunnels on Root.
7. Configure IGMP on the interfaces connecting a multicast device to a user network segment to allow the device to manage multicast group members on the network segment.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces (shown in [Figure 1](#EN-US_TASK_0178516032__fig35284409229))

* IS-IS process ID (1) on the public network in a Level-2 area
* VPN instance name (VPNA) on Root, Leaf 1, and Leaf 2
* BFR-IDs of Root, Leaf 1, and Leaf 2 (1, 4, and 5, respectively), sub-domain 0, BSL 256, and Max-SI 2
* Root, Leaf 1, and Leaf 2 as PEs

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Configure the VPN backbone network and the IP address of each interface in each VPN site.
      
      
      
      Configure an IP address for each interface. For configuration details, see Configuration Files in this section.
   2. Configure an IGP to interconnect devices on the BGP/MPLS IP VPN backbone network.
      
      
      
      This example uses IS-IS as the IGP. For configuration details, see Configuration Files in this section.
   3. Configure basic MPLS functions and enable MPLS LDP on the backbone network.
      
      
      * # Configure Root.
        
        ```
        [~Root] mpls lsr-id 1.1.1.1
        ```
        ```
        [*Root] mpls
        ```
        ```
        [*Root-mpls] quit
        ```
        ```
        [*Root] mpls ldp
        ```
        ```
        [*Root-mpls-ldp] quit
        ```
        ```
        [*Root] interface gigabitethernet0/1/0
        ```
        ```
        [*Root-GigabitEthernet0/1/0] mpls
        ```
        ```
        [*Root-GigabitEthernet0/1/0] mpls ldp
        ```
        ```
        [*Root-GigabitEthernet0/1/0] quit
        ```
      * # Configure the P.
        
        ```
        [~P] mpls lsr-id 2.2.2.1
        ```
        ```
        [*P] mpls
        ```
        ```
        [*P-mpls] quit
        ```
        ```
        [*P] mpls ldp
        ```
        ```
        [*P-mpls-ldp] quit
        ```
        ```
        [*P] interface gigabitethernet0/1/0
        ```
        ```
        [*P-GigabitEthernet0/1/0] mpls
        ```
        ```
        [*P-GigabitEthernet0/1/0] mpls ldp
        ```
        ```
        [*P-GigabitEthernet0/1/0] quit
        ```
        ```
        [*P] interface gigabitethernet0/1/1
        ```
        ```
        [*P-Gigabitethernet0/1/1] mpls
        ```
        ```
        [*P-Gigabitethernet0/1/1] mpls ldp
        ```
        ```
        [*P-Gigabitethernet0/1/1] quit
        ```
      * # Configure Leaf 1.
        
        ```
        [~Leaf1] mpls lsr-id 4.4.4.1
        ```
        ```
        [*Leaf1] mpls
        ```
        ```
        [*Leaf1-mpls] quit
        ```
        ```
        [*Leaf1] mpls ldp
        ```
        ```
        [*Leaf1-mpls-ldp] quit
        ```
        ```
        [*Leaf1] interface gigabitethernet0/1/0
        ```
        ```
        [*Leaf1-GigabitEthernet0/1/0] mpls
        ```
        ```
        [*Leaf1-GigabitEthernet0/1/0] mpls ldp
        ```
        ```
        [*Leaf1-GigabitEthernet0/1/0] quit
        ```
        ```
        [*Leaf1] commit
        ```
      * # Configure Leaf 2.
        ```
        [~Leaf2] mpls lsr-id 5.5.5.1
        ```
        ```
        [*Leaf2] mpls
        ```
        ```
        [*Leaf2-mpls] quit
        ```
        ```
        [*Leaf2] mpls ldp
        ```
        ```
        [*Leaf2-mpls-ldp] quit
        ```
        ```
        [*Leaf2] interface gigabitethernet0/1/0
        ```
        ```
        [*Leaf2-GigabitEthernet0/1/0] mpls
        ```
        ```
        [*Leaf2-GigabitEthernet0/1/0] mpls ldp
        ```
        ```
        [*Leaf2-GigabitEthernet0/1/0] quit
        ```
        ```
        [*Leaf2] commit
        ```
   4. Establish an MP-IBGP peer relationship between Root and Leaf 1 and between Root and Leaf 2.
      
      
      * # Configure Root.
        
        ```
        [~Root] bgp 100
        ```
        ```
        [*Root-bgp] peer 5.5.5.1 as-number 100
        ```
        ```
        [*Root-bgp] peer 5.5.5.1 connect-interface LoopBack0
        ```
        ```
        [*Root-bgp] peer 4.4.4.1 as-number 100
        ```
        ```
        [*Root-bgp] peer 4.4.4.1 connect-interface LoopBack0
        ```
        ```
        [*Root-bgp] ipv4-family vpnv4
        ```
        ```
        [*Root-bgp-af-vpnv4] peer 5.5.5.1 enable
        ```
        ```
        [*Root-bgp-af-vpnv4] peer 4.4.4.1 enable
        ```
        ```
        [*Root-bgp-af-vpnv4] quit
        ```
        ```
        [*Root-bgp] quit
        ```
        ```
        [*Root] commit
        ```
      * # Configure Leaf 1.
        
        ```
        [~Leaf1] bgp 100
        ```
        ```
        [*Leaf1-bgp] peer 1.1.1.1 as-number 100
        ```
        ```
        [*Leaf1-bgp] peer 1.1.1.1 connect-interface LoopBack0
        ```
        ```
        [*Leaf1-bgp] ipv4-family vpnv4
        ```
        ```
        [*Leaf1-bgp-af-vpnv4] peer 1.1.1.1 enable
        ```
        ```
        [*Leaf1-bgp-af-vpnv4] quit
        ```
        ```
        [*Leaf1-bgp] quit
        ```
        ```
        [*Leaf1] commit
        ```
      * # Configure Leaf 2.
        
        ```
        [~Leaf2] bgp 100
        ```
        ```
        [*Leaf2-bgp] peer 1.1.1.1 as-number 100
        ```
        ```
        [*Leaf2-bgp] peer 1.1.1.1 connect-interface LoopBack0
        ```
        ```
        [*Leaf2-bgp] ipv4-family vpnv4
        ```
        ```
        [*Leaf2-bgp-af-vpnv4] peer 1.1.1.1 enable
        ```
        ```
        [*Leaf2-bgp-af-vpnv4] quit
        ```
        ```
        [*Leaf2-bgp] quit
        ```
        ```
        [*Leaf2] commit
        ```
   5. Configure a VPN instance on the PEs.
      
      
      * # Configure Root.
        
        ```
        [~Root] ip vpn-instance VPNA
        ```
        ```
        [*Root-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*Root-vpn-instance-VPNA-af-ipv4] route-distinguisher 200:1
        ```
        ```
        [*Root-vpn-instance-VPNA-af-ipv4] vpn-target 3:3 4:4
        ```
        ```
        [*Root-vpn-instance-VPNA-af-ipv4] quit
        ```
        ```
        [*Root-vpn-instance-VPNA] quit
        ```
        ```
        [*Root] interface gigabitethernet0/1/1
        ```
        ```
        [*Root-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
        ```
        ```
        [*Root-GigabitEthernet0/1/1] ip address 192.168.1.1 24
        ```
        ```
        [*Root-GigabitEthernet0/1/1] quit
        ```
        ```
        [*Root] commit
        ```
      * # Configure Leaf 1.
        
        ```
        [~Leaf1] ip vpn-instance VPNA
        ```
        ```
        [*Leaf1-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*Leaf1-vpn-instance-VPNA-af-ipv4] route-distinguisher 300:1
        ```
        ```
        [*Leaf1-vpn-instance-VPNA-af-ipv4] vpn-target 3:3
        ```
        ```
        [*Leaf1-vpn-instance-VPNA-af-ipv4] quit
        ```
        ```
        [*Leaf1-vpn-instance-VPNA] quit
        ```
        ```
        [*Leaf1] interface gigabitethernet0/1/1
        ```
        ```
        [*Leaf1-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
        ```
        ```
        [*Leaf1-GigabitEthernet0/1/1] ip address 192.168.2.1 24
        ```
        ```
        [*Leaf1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*Leaf1] commit
        ```
      * # Configure Leaf 2.
        
        ```
        [~Leaf2] ip vpn-instance VPNA
        ```
        ```
        [*Leaf2-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*Leaf2-vpn-instance-VPNA-af-ipv4] route-distinguisher 400:1
        ```
        ```
        [*Leaf2-vpn-instance-VPNA-af-ipv4] vpn-target 4:4
        ```
        ```
        [*Leaf2-vpn-instance-VPNA-af-ipv4] quit
        ```
        ```
        [*Leaf2-vpn-instance-VPNA] quit
        ```
        ```
        [*Leaf2] interface gigabitethernet0/1/1
        ```
        ```
        [*Leaf2-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
        ```
        ```
        [*Leaf2-GigabitEthernet0/1/1] ip address 192.168.3.1 24
        ```
        ```
        [*Leaf2-GigabitEthernet0/1/1] quit
        ```
        ```
        [*Leaf2] commit
        ```
   6. Configure PEs to import direct routes.
      
      
      * # Configure Root.
        
        ```
        [*Root] bgp 100
        ```
        ```
        [*Root-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*Root-bgp-VPNA] import-route direct
        ```
        ```
        [*Root-bgp-VPNA] quit
        ```
        ```
        [*Root-bgp] quit
        ```
        ```
        [*Root] commit
        ```
      * # Configure Leaf 1.
        
        ```
        [*Leaf1] bgp 100
        ```
        ```
        [*Leaf1-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*Leaf1-bgp-VPNA] import-route direct
        ```
        ```
        [*Leaf1-bgp-VPNA] quit
        ```
        ```
        [*Leaf1-bgp] quit
        ```
        ```
        [*Leaf1] commit
        ```
      * # Configure Leaf 2.
        
        ```
        [*Leaf2] bgp 100
        ```
        ```
        [*Leaf2-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*Leaf2-bgp-VPNA] import-route direct
        ```
        ```
        [*Leaf2-bgp-VPNA] quit
        ```
        ```
        [*Leaf2-bgp] quit
        ```
        ```
        [*Leaf2] commit
        ```
2. Configure BIER and enable BIER in IS-IS on the PEs and P.
   
   
   * # Configure Root.
     
     ```
     [~Root] interface Loopback0
     ```
     ```
     [*Root-LoopBack0] ip address 1.1.1.1 32
     ```
     ```
     [*Root-LoopBack0] isis enable 1 
     ```
     ```
     [*Root-LoopBack0] quit
     ```
     ```
     [*Root] commit
     ```
     ```
     [~Root] bier
     ```
     ```
     [*Root-bier] sub-domain 0
     ```
     ```
     [*Root-bier-sub-domain-0] bfr-id 1
     ```
     ```
     [*Root-bier-sub-domain-0] bfr-prefix interface loopback0
     ```
     ```
     [*Root-bier-sub-domain-0] protocol isis
     ```
     ```
     [*Root-bier-sub-domain-0] encapsulation-type mpls bsl 256 max-si 2
     ```
     ```
     [*Root-bier-sub-domain-0] quit
     ```
     ```
     [*Root-bier] quit
     ```
     ```
     [*Root] isis 1
     ```
     ```
     [*Root-isis-1] cost-style wide
     ```
     ```
     [*Root-isis-1] bier enable
     ```
     ```
     [*Root-isis-1] quit
     ```
   * # Configure the P.
     
     ```
     [~P] interface Loopback0
     ```
     ```
     [*P-LoopBack0] ip address 2.2.2.1 32
     ```
     ```
     [*P-LoopBack0] isis enable 1 
     ```
     ```
     [*P-LoopBack0] quit
     ```
     ```
     [*P] commit
     ```
     ```
     [~P] bier
     ```
     ```
     [*P-bier] sub-domain 0
     ```
     ```
     [*P-bier-sub-domain-0] bfr-prefix interface loopback0
     ```
     ```
     [*P-bier-sub-domain-0] protocol isis
     ```
     ```
     [*P-bier-sub-domain-0] encapsulation-type mpls bsl 256 max-si 2
     ```
     ```
     [*P-bier-sub-domain-0] quit
     ```
     ```
     [*P-bier] quit
     ```
     ```
     [*P] isis 1
     ```
     ```
     [*P-isis-1] cost-style wide
     ```
     ```
     [*P-isis-1] bier enable
     ```
     ```
     [*P-isis-1] quit
     ```
   * # Configure Leaf 1.
     ```
     [~Leaf1] interface Loopback0
     ```
     ```
     [*Leaf1-LoopBack0] ip address 4.4.4.1 32
     ```
     ```
     [*Leaf1-LoopBack0] isis enable 1 
     ```
     ```
     [*Leaf1-LoopBack0] quit
     ```
     ```
     [*Leaf1] commit
     ```
     ```
     [~Leaf1] bier
     ```
     ```
     [*Leaf1-bier] sub-domain 0
     ```
     ```
     [*Leaf1-bier-sub-domain-0] bfr-id 4
     ```
     ```
     [*Leaf1-bier-sub-domain-0] bfr-prefix interface loopback0
     ```
     ```
     [*Leaf1-bier-sub-domain-0] protocol isis
     ```
     ```
     [*Leaf1-bier-sub-domain-0] encapsulation-type mpls bsl 256 max-si 2
     ```
     ```
     [*Leaf1-bier-sub-domain-0] quit
     ```
     ```
     [*Leaf1-bier] quit
     ```
     ```
     [*Leaf1] isis 1
     ```
     ```
     [*Leaf1-isis-1] cost-style wide
     ```
     ```
     [*Leaf1-isis-1] bier enable
     ```
     ```
     [*Leaf1-isis-1] quit
     ```
   * # Configure Leaf 2.
     ```
     [~Leaf2] interface Loopback0
     ```
     ```
     [*Leaf2-LoopBack0] ip address 5.5.5.1 32
     ```
     ```
     [*Leaf2-LoopBack0] isis enable 1
     ```
     ```
     [*Leaf2-LoopBack0] quit
     ```
     ```
     [*Leaf2] commit
     ```
     ```
     [~Leaf2] bier
     ```
     ```
     [*Leaf2-bier] sub-domain 0
     ```
     ```
     [*Leaf2-bier-sub-domain-0] bfr-id 5
     ```
     ```
     [*Leaf2-bier-sub-domain-0] bfr-prefix interface loopback0
     ```
     ```
     [*Leaf2-bier-sub-domain-0] protocol isis
     ```
     ```
     [*Leaf2-bier-sub-domain-0] encapsulation-type mpls bsl 256 max-si 2
     ```
     ```
     [*Leaf2-bier-sub-domain-0] quit
     ```
     ```
     [*Leaf2-bier] quit
     ```
     ```
     [*Leaf2] isis 1
     ```
     ```
     [*Leaf2-isis-1] cost-style wide
     ```
     ```
     [*Leaf2-isis-1] bier enable
     ```
     ```
     [*Leaf2-isis-1] quit
     ```
3. Establish a BGP MVPN peer relationship between Root and Leaf 1 and between Root and Leaf 2.
   
   
   * # Configure Root.
     
     ```
     [~Root] bgp 100
     ```
     ```
     [*Root-bgp] ipv4-family mvpn
     ```
     ```
     [*Root-bgp-af-mvpn] peer 5.5.5.1 enable
     ```
     ```
     [*Root-bgp-af-mvpn] peer 4.4.4.1 enable
     ```
     ```
     [*Root-bgp-af-mvpn] commit
     ```
     ```
     [~Root-bgp-af-mvpn] quit
     ```
     ```
     [~Root-bgp] quit
     ```
   * # Configure Leaf 1.
     
     ```
     [~Leaf1] bgp 100
     ```
     ```
     [*Leaf1-bgp] ipv4-family mvpn
     ```
     ```
     [*Leaf1-bgp-af-mvpn] peer 1.1.1.1 enable
     ```
     ```
     [*Leaf1-bgp-af-mvpn] commit
     ```
     ```
     [~Leaf1-bgp-af-mvpn] quit
     ```
     ```
     [~Leaf1-bgp] quit
     ```
   * # Configure Leaf 2.
     
     ```
     [~Leaf2] bgp 100
     ```
     ```
     [*Leaf2-bgp] ipv4-family mvpn
     ```
     ```
     [*Leaf2-bgp-af-mvpn] peer 1.1.1.1 enable
     ```
     ```
     [*Leaf2-bgp-af-mvpn] commit
     ```
     ```
     [~Leaf2-bgp-af-mvpn] quit
     ```
     ```
     [~Leaf2-bgp] quit
     ```
   
   After completing the configurations, run the [**display bgp mvpn all peer**](cmdqueryname=display+bgp+mvpn+all+peer) command. The command output shows that Root has established a BGP MVPN peer relationship with Leaf 1 and Leaf 2. The following example uses the command output on Root.
   
   ```
   [~Root] display bgp mvpn all peer
   ```
   ```
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     4.4.4.1         4         100       43       42     0 00:29:28 Established        2
     5.5.5.1         4         100       32       35     0 00:21:59 Established        1  
   ```
4. Set the PMSI tunnel type to BIER.
   
   
   * # Configure Root.
     
     ```
     [~Root] multicast mvpn 1.1.1.1
     ```
     ```
     [*Root] ip vpn-instance VPNA
     ```
     ```
     [*Root-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4] multicast routing-enable
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn] sender-enable
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn] ipmsi-tunnel
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] bier
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn] spmsi-tunnel
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] group 224.0.0.0 255.255.255.0 source 192.168.1.2 255.255.255.0 bier limit 16
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] quit
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4-mvpn] quit
     ```
     ```
     [*Root-vpn-instance-VPNA-af-ipv4] quit
     ```
     ```
     [*Root-vpn-instance-VPNA] quit
     ```
     ```
     [*Root] commit
     ```
   * # Configure Leaf 1.
     
     ```
     [~Leaf1] multicast mvpn 4.4.4.1
     ```
     ```
     [*Leaf1] ip vpn-instance VPNA
     ```
     ```
     [*Leaf1-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*Leaf1-vpn-instance-VPNA-af-ipv4] multicast routing-enable
     ```
     ```
     [*Leaf1-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*Leaf1-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*Leaf1-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
     ```
     ```
     [*Leaf1-vpn-instance-VPNA-af-ipv4-mvpn] quit
     ```
     ```
     [*Leaf1-vpn-instance-VPNA-af-ipv4] quit
     ```
     ```
     [*Leaf1-vpn-instance-VPNA] quit
     ```
     ```
     [*Leaf1] commit
     ```
   * # Configure Leaf 2.
     
     ```
     [~Leaf2] multicast mvpn 5.5.5.1
     ```
     ```
     [*Leaf2] ip vpn-instance VPNA
     ```
     ```
     [*Leaf2-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*Leaf2-vpn-instance-VPNA-af-ipv4] multicast routing-enable
     ```
     ```
     [*Leaf2-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*Leaf2-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*Leaf2-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
     ```
     ```
     [*Leaf2-vpn-instance-VPNA-af-ipv4-mvpn] quit
     ```
     ```
     [*Leaf2-vpn-instance-VPNA-af-ipv4] quit
     ```
     ```
     [*Leaf2-vpn-instance-VPNA] quit
     ```
     ```
     [*Leaf2] commit
     ```
   
   After completing the configurations, run the [**display mvpn vpn-instance ipmsi**](cmdqueryname=display+mvpn+vpn-instance+ipmsi) command on the PEs to check I-PMSI tunnel establishment. The following example uses the command output on Root.
   
   ```
   [~Root] display mvpn vpn-instance VPNA ipmsi
   ```
   ```
   MVPN local I-PMSI information for VPN-Instance:VPNA
   Tunnel type: BIER 
   Tunnel state: Up 
   MPLS label: 256
   Sub-domain ID: 0
   BFR-ID: 1
   BFR prefix: 1.1.1.1
   Bit string ID: 1 
   Root: 1.1.1.1 (local) 
   Leaf:
      1: 4.4.4.1 (BFR-ID: 4, BFR prefix: 4.4.4.1)
      2: 5.5.5.1 (BFR-ID: 5, BFR prefix: 5.5.5.1)
   ```
   
   The command output shows that a BIER P2MP tunnel has been established, with Root as the root node and Leaf 1 and Leaf 2 as leaf nodes.
5. Configure PIM.
   
   
   * # Configure Root.
     
     ```
     [~Root] interface gigabitethernet0/1/1
     ```
     ```
     [*Root-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*Root-GigabitEthernet0/1/1] quit
     ```
     ```
     [*Root] commit
     ```
   * # Configure Leaf 1.
     
     ```
     [~Leaf1] interface gigabitethernet0/1/1
     ```
     ```
     [*Leaf1-GigabitEthernet0/1/1] igmp enable
     ```
     ```
     [*Leaf1-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*Leaf1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*Leaf1] commit
     ```
   * # Configure Leaf 2.
     
     ```
     [~Leaf2] interface gigabitethernet0/1/1
     ```
     ```
     [*Leaf2-GigabitEthernet0/1/1] igmp enable
     ```
     ```
     [*Leaf2-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*Leaf2-GigabitEthernet0/1/1] quit
     ```
     ```
     [*Leaf2] commit
     ```
6. Configure a static RP.
   
   
   * # Configure Root.
     ```
     [~Root] interface loopback1
     ```
     ```
     [*Root-LoopBack1] ip binding vpn-instance VPNA
     ```
     ```
     [*Root-LoopBack1]ip address 1.1.1.2 32
     ```
     ```
     [*Root] commit
     ```
     ```
     [~Root] pim vpn-instance VPNA
     ```
     ```
     [*Root-pim-VPNA] static-rp 1.1.1.2
     ```
     ```
     [*Root-pim-VPNA] commit
     ```
     ```
     [~Root-pim-VPNA] quit
     ```
   * # Configure Leaf 1.
     
     ```
     [~Leaf1] pim vpn-instance VPNA
     ```
     ```
     [*Leaf1-pim-VPNA] static-rp 1.1.1.2
     ```
     ```
     [*Leaf1-pim-VPNA] commit
     ```
     ```
     [~Leaf1-pim-VPNA] quit
     ```
   * # Configure Leaf 2.
     
     ```
     [~Leaf2] pim vpn-instance VPNA
     ```
     ```
     [*Leaf2-pim-VPNA] static-rp 1.1.1.2
     ```
     ```
     [*Leaf2-pim-VPNA] commit
     ```
     ```
     [~Leaf2-pim-VPNA] quit
     ```
7. Verify the configuration.
   
   
   
   After the configurations are complete, NG MVPN over BIER has been configured. If Receiver 1 or Receiver 2 has access users, CE1 can use the BGP/MPLS IP VPN to forward multicast data to the users.
   
   Run the [**display pim vpn-instance**](cmdqueryname=display+pim+vpn-instance) **routing-table** command on Leaf 1, Leaf 2, and Root to check the PIM routing tables of the VPN instance.
   
   ```
   [~Leaf1] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (192.168.1.2, 225.1.1.1)
        RP:1.1.1.2
        Protocol: pim-sm, Flag: SPT ACT
        UpTime: 00:48:18
        Upstream interface: through-BGP, Refresh time: 00:48:18
            Upstream neighbor: 1.1.1.1
            RPF prime neighbor: 1.1.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:48:18, Expires: 00:03:12     
   ```
   ```
   [~Leaf2] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (192.168.1.2, 225.1.1.1)
        RP:1.1.1.2
        Protocol: pim-sm, Flag: SPT ACT
        UpTime: 00:02:06
        Upstream interface: through-BGP, Refresh time: 00:02:06
            Upstream neighbor: 1.1.1.1
            RPF prime neighbor: 1.1.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:02:06, Expires: 00:03:26 
   ```
   ```
   [~Root] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 0 (*, G) entry; 1 (S, G) entries
   
    (192.168.1.2, 225.1.1.1)
        RP:1.1.1.2
        Protocol: pim-sm, Flag: SPT SG_RCVR ACT
        UpTime: 00:46:58
        Upstream interface: GigabitEthernet0/1/1, Refresh time: 00:46:58
            Upstream neighbor: 192.168.1.1
            RPF prime neighbor: 192.168.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: pseudo
                Protocol: BGP, UpTime: 00:46:58, Expires: -
   ```

#### Configuration Files

* Root configuration file
  ```
  #
  sysname Root
  #
  multicast mvpn 1.1.1.1
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 4:4 export-extcommunity
    vpn-target 3:3 import-extcommunity
    vpn-target 4:4 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     rpt-spt mode
     ipmsi-tunnel
      bier   
     spmsi-tunnel
      group 224.0.0.0 255.255.255.0 source 192.168.1.0 255.255.255.0 bier limit 16
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0001.00
   bier enable
  #
  interface GigabitEthernet0/1/0 
   undo shutdown
   ip address 192.168.0.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  interface LoopBack1
   ip binding vpn-instance VPNA
   ip address 1.1.1.2 255.255.255.255
  #
  bgp 100
   peer 4.4.4.1 as-number 100
   peer 4.4.4.1 connect-interface LoopBack0
   peer 5.5.5.1 as-number 100
   peer 5.5.5.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.1 enable
    peer 5.5.5.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 4.4.4.1 enable
    peer 5.5.5.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.1 enable
    peer 5.5.5.1 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
  #
  pim vpn-instance VPNA
   static-rp 1.1.1.2
  #
  bier
   sub-domain 0
    bfr-id 1
    bfr-prefix interface LoopBack0
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0004.00
   traffic-eng level-2
   bier enable
  #
  interface GigabitEthernet0/1/0 
   undo shutdown
   ip address 192.168.0.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.45.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.1 255.255.255.255
   isis enable 1
  #
  bier
   sub-domain 0
    bfr-prefix interface LoopBack0
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  return
  ```
* Leaf 1 configuration file
  
  ```
  #
  sysname Leaf1
  #
  multicast mvpn 4.4.4.1
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 300:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     rpt-spt mode
  #
  mpls lsr-id 4.4.4.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0002.00
   traffic-eng level-2
   bier enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.45.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp       
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.2.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface LoopBack0
   ip address 4.4.4.1 255.255.255.255
   isis enable 1
  # 
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
   #
  pim vpn-instance VPNA
   static-rp 1.1.1.2
  #
  bier
   sub-domain 0
    bfr-id 4
    bfr-prefix interface LoopBack0
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  return
  ```
* Leaf 2 configuration file
  
  ```
  #
  sysname Leaf2
  #
  multicast routing-enable
  #
  multicast mvpn 5.5.5.1
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 400:1
    apply-label per-instance
    vpn-target 4:4 export-extcommunity
    vpn-target 4:4 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     rpt-spt mode
  #
  mpls lsr-id 5.5.5.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0003.00
   traffic-eng level-2
   bier enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.45.3 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.3.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface LoopBack0
   ip address 5.5.5.1 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
   #
  pim vpn-instance VPNA
   static-rp 1.1.1.2
  #
  lldp enable
  #
  bier
   sub-domain 0
    bfr-id 5
    bfr-prefix interface LoopBack0
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  return
  ```