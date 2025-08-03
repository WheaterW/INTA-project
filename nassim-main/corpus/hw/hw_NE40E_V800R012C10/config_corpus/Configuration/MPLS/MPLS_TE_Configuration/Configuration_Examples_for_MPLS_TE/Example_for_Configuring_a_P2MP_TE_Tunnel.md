Example for Configuring a P2MP TE Tunnel
========================================

This section provides an example for configuring a P2MP TE tunnel on an IP/MPLS backbone network.

#### Networking Requirements

The IP multicast service bearer technology used on the current IP/MPLS backbone network relies on the IP unicast technology. Like IP unicast, IP multicast fails to provide sufficient bandwidth, QoS capabilities, reliability and high real-time performance for multicast services such as IPTV and massively multiplayer online role-playing games (MMORPGs). A P2MP TE tunnel can solve this problem. A P2MP TE tunnel can be configured on a live IP/MPLS backbone network, and supports the P2MP TE FRR function, meeting multicast service requirements.

A P2MP TE tunnel is established on the network shown in [Figure 1](#EN-US_TASK_0172368372__fig_dc_vrp_te-p2p_cfg_013901). LSRA is the tunnel ingress. LSRC, LSRE, and LSRF are leaf nodes, and the tunnel bandwidth is 1000 kbit/s.

**Figure 1** P2MP TE tunnel networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_te-p2p_cfg_013901.png)

#### Precautions

None.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface and configure a loopback interface address as an LSR ID on each node.
2. Configure Intermediate System to Intermediate System (IS-IS) to advertise the route to each network segment to which each interface is connected and the host route to each loopback interface address that is an LSR ID.
3. Enable MPLS, MPLS TE, P2MP TE, and MPLS RSVP-TE globally on each node and constraint shortest path first (CSPF) on the ingress to enable all nodes to have MPLS forwarding capabilities.
4. Enable the IGP TE capability to ensure that MPLS TE can advertise information about link status.
5. Enable the MPLS TE capability on the interfaces of each node and configure link attributes for the interfaces so that the interfaces can send RSVP signaling packets.
6. Configure explicit paths and a leaf list on the ingress LSRA to specify the leaf nodes on the P2MP TE tunnel.
7. Configure a P2MP TE tunnel interface on LSRA to ensure that the ingress establishes a P2MP TE tunnel based on all configuration information on the interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of all interfaces shown in [Figure 1](#EN-US_TASK_0172368372__fig_dc_vrp_te-p2p_cfg_013901)
* IS-IS (used as an IGP protocol), IS-IS process ID (1), IS-IS system ID of each node (obtained by translating the IP address of loopback1 of each node), and IS-IS level (Level-2)
* MPLS LSR ID of each node using the corresponding loopback interface address
* Maximum reservable bandwidth (10000 kbit/s) of the outbound interface along the path and BC0 bandwidth (10000 kbit/s)
* Name of an explicit path used by each leaf node (toLSRB, toLSRE, and toLSRF), name of the leaf list (iptv1), and addresses of each leaf node (MPLS LSR ID of each leaf node)
* Tunnel interface number (Tunnel 10), tunnel ID (100), loopback interface address used as the IP address of the tunnel interface, and tunnel bandwidth (1000 kbit/s)

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0172368372__fig_dc_vrp_te-p2p_cfg_013901) and create a loopback interface on each node. For configuration details, see [Configuration Files](#EN-US_TASK_0172368372__section_dc_vrp_te-p2p_cfg_013105) in this section.
2. Configure IS-IS to advertise the route to each network segment to which each interface is connected and to advertise the host route to each LSR ID.
   
   
   
   Configure IS-IS on each node to implement network layer connectivity. For configuration details, see [Configuration Files](#EN-US_TASK_0172368372__section_dc_vrp_te-p2p_cfg_013105) in this section.
3. Enable MPLS, MPLS TE, P2MP TE, and MPLS RSVP-TE globally on each node and CSPF on the ingress.
   
   
   
   # Configure LSRA.
   
   ```
   <LSRA> system-view 
   ```
   ```
   [~LSRA] mpls lsr-id 1.1.1.1
   ```
   ```
   [*LSRA] mpls
   ```
   ```
   [*LSRA-mpls] mpls te
   ```
   ```
   [*LSRA-mpls] mpls te p2mp-te 
   ```
   ```
   [*LSRA-mpls] mpls rsvp-te
   ```
   ```
   [*LSRA-mpls] mpls te cspf
   ```
   ```
   [*LSRA-mpls] commit
   ```
   ```
   [~LSRA-mpls] quit
   ```
   
   # Configure LSRB.
   
   ```
   <LSRB> system-view 
   ```
   ```
   [~LSRB] mpls lsr-id 2.2.2.2
   ```
   ```
   [*LSRB] mpls
   ```
   ```
   [*LSRB-mpls] mpls te
   ```
   ```
   [*LSRB-mpls] mpls te p2mp-te 
   ```
   ```
   [*LSRB-mpls] mpls rsvp-te
   ```
   ```
   [*LSRB-mpls] commit
   ```
   ```
   [~LSRB-mpls] quit
   ```
   
   # Configure LSRC.
   
   ```
   <LSRC> system-view 
   ```
   ```
   [~LSRC] mpls lsr-id 3.3.3.3
   ```
   ```
   [*LSRC] mpls
   ```
   ```
   [*LSRC-mpls] mpls te
   ```
   ```
   [*LSRC-mpls] mpls te p2mp-te 
   ```
   ```
   [*LSRC-mpls] mpls rsvp-te
   ```
   ```
   [*LSRC-mpls] commit
   ```
   ```
   [~LSRC-mpls] quit
   ```
   
   # Configure LSRD.
   
   ```
   <LSRD> system-view 
   ```
   ```
   [~LSRD] mpls lsr-id 4.4.4.4
   ```
   ```
   [*LSRD] mpls
   ```
   ```
   [*LSRD-mpls] mpls te
   ```
   ```
   [*LSRD-mpls] mpls te p2mp-te 
   ```
   ```
   [*LSRD-mpls] mpls rsvp-te
   ```
   ```
   [*LSRD-mpls] commit
   ```
   ```
   [~LSRD-mpls] quit
   ```
   
   # Configure LSRE.
   
   ```
   <LSRE> system-view 
   ```
   ```
   [~LSRE] mpls lsr-id 5.5.5.5
   ```
   ```
   [*LSRE] mpls
   ```
   ```
   [*LSRE-mpls] mpls te
   ```
   ```
   [*LSRE-mpls] mpls te p2mp-te 
   ```
   ```
   [*LSRE-mpls] mpls rsvp-te
   ```
   ```
   [*LSRE-mpls] commit
   ```
   ```
   [~LSRE-mpls] quit
   ```
   
   # Configure LSRF.
   
   ```
   <LSRF> system-view 
   ```
   ```
   [~LSRF] mpls lsr-id 6.6.6.6
   ```
   ```
   [*LSRF] mpls
   ```
   ```
   [*LSRF-mpls] mpls te
   ```
   ```
   [*LSRF-mpls] mpls te p2mp-te 
   ```
   ```
   [*LSRF-mpls] mpls rsvp-te
   ```
   ```
   [*LSRF-mpls] commit
   ```
   ```
   [~LSRF-mpls] quit
   ```
4. Enable IGP TE on each node.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] isis 1
   ```
   ```
   [~LSRA-isis-1] cost-style wide
   ```
   ```
   [*LSRA-isis-1] traffic-eng level-2
   ```
   ```
   [*LSRA-isis-1] commit
   ```
   ```
   [~LSRA-isis-1] quit
   ```
   
   # Configure LSRB.
   
   ```
   [~LSRB] isis 1
   ```
   ```
   [~LSRB-isis-1] cost-style wide
   ```
   ```
   [*LSRB-isis-1] traffic-eng level-2
   ```
   ```
   [*LSRB-isis-1] commit
   ```
   ```
   [~LSRB-isis-1] quit
   ```
   
   # Configure LSRC.
   
   ```
   [~LSRC] isis 1
   ```
   ```
   [~LSRC-isis-1] cost-style wide
   ```
   ```
   [*LSRC-isis-1] traffic-eng level-2
   ```
   ```
   [*LSRC-isis-1] commit
   ```
   ```
   [~LSRC-isis-1] quit
   ```
   
   # Configure LSRD.
   
   ```
   [~LSRD] isis 1
   ```
   ```
   [~LSRD-isis-1] cost-style wide
   ```
   ```
   [*LSRD-isis-1] traffic-eng level-2
   ```
   ```
   [*LSRD-isis-1] commit
   ```
   ```
   [~LSRD-isis-1] quit
   ```
   
   # Configure LSRE.
   
   ```
   [~LSRE] isis 1
   ```
   ```
   [~LSRE-isis-1] cost-style wide
   ```
   ```
   [*LSRE-isis-1] traffic-eng level-2
   ```
   ```
   [*LSRE-isis-1] commit
   ```
   ```
   [~LSRE-isis-1] quit
   ```
   
   # Configure LSRF.
   
   ```
   [~LSRF] isis 1
   ```
   ```
   [~LSRF-isis-1] cost-style wide
   ```
   ```
   [*LSRF-isis-1] traffic-eng level-2
   ```
   ```
   [*LSRF-isis-1] commit
   ```
   ```
   [~LSRF-isis-1] quit
   ```
5. Enable the MPLS TE capability on the interface of each node, and configure link attributes for the interfaces.
   
   
   
   # Configure LSRA.
   
   ```
   <LSRA> system-view 
   ```
   ```
   [~LSRA] interface gigabitethernet 0/1/1
   ```
   ```
   [~LSRA-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls te
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls rsvp-te
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls te bandwidth bc0 10000
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~LSRA-GigabitEthernet0/1/1] quit
   ```
   
   # Configure LSRB.
   
   ```
   <LSRB> system-view 
   ```
   ```
   [~LSRB] interface gigabitethernet 0/1/0
   ```
   ```
   [~LSRB-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [~LSRB-GigabitEthernet0/1/0] mpls te bandwidth bc0 10000
   ```
   ```
   [~LSRB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/1/2
   ```
   ```
   [*LSRB-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/2] mpls te
   ```
   ```
   [*LSRB-GigabitEthernet0/1/2] mpls rsvp-te
   ```
   ```
   [*LSRB-GigabitEthernet0/1/2] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [*LSRB-GigabitEthernet0/1/2] mpls te bandwidth bc0 10000
   ```
   ```
   [*LSRB-GigabitEthernet0/1/2] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls te
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls rsvp-te
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls te bandwidth bc0 10000
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~LSRB-GigabitEthernet0/1/1] quit
   ```
   
   # Configure LSRC.
   
   ```
   <LSRC> system-view 
   ```
   ```
   [~LSRC] interface gigabitethernet 0/1/2
   ```
   ```
   [~LSRC-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] mpls te
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] mpls rsvp-te
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] mpls te bandwidth bc0 10000
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] commit
   ```
   ```
   [~LSRC-GigabitEthernet0/1/2] quit
   ```
   
   # Configure LSRD.
   
   ```
   <LSRD> system-view 
   ```
   ```
   [~LSRD] interface gigabitethernet 0/1/0
   ```
   ```
   [~LSRD-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls te bandwidth bc0 10000
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRD] interface gigabitethernet 0/1/2
   ```
   ```
   [*LSRD-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*LSRD-GigabitEthernet0/1/2] mpls te
   ```
   ```
   [*LSRD-GigabitEthernet0/1/2] mpls rsvp-te
   ```
   ```
   [*LSRD-GigabitEthernet0/1/2] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [*LSRD-GigabitEthernet0/1/2] mpls te bandwidth bc0 10000
   ```
   ```
   [*LSRD-GigabitEthernet0/1/2] quit
   ```
   ```
   [*LSRD] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRD-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRD-GigabitEthernet0/1/1] mpls te
   ```
   ```
   [*LSRD-GigabitEthernet0/1/1] mpls rsvp-te
   ```
   ```
   [*LSRD-GigabitEthernet0/1/1] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [*LSRD-GigabitEthernet0/1/1] mpls te bandwidth bc0 10000
   ```
   ```
   [*LSRD-GigabitEthernet0/1/1] commit
   ```
   ```
   [~LSRD-GigabitEthernet0/1/1] quit
   ```
   
   # Configure LSRE.
   
   ```
   <LSRE> system-view 
   ```
   ```
   [~LSRE] interface gigabitethernet 0/1/0
   ```
   ```
   [~LSRE-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] mpls te bandwidth bc0 10000
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRE-GigabitEthernet0/1/0] quit
   ```
   
   # Configure LSRF.
   
   ```
   <LSRF> system-view 
   ```
   ```
   [~LSRF] interface gigabitethernet 0/1/1
   ```
   ```
   [~LSRF-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRF-GigabitEthernet0/1/1] mpls te
   ```
   ```
   [*LSRF-GigabitEthernet0/1/1] mpls rsvp-te
   ```
   ```
   [*LSRF-GigabitEthernet0/1/1] mpls te bandwidth max-reservable-bandwidth 10000
   ```
   ```
   [*LSRF-GigabitEthernet0/1/1] mpls te bandwidth bc0 10000
   ```
   ```
   [*LSRF-GigabitEthernet0/1/1] commit
   ```
   ```
   [~LSRF-GigabitEthernet0/1/1] quit
   ```
6. Configure explicit paths and a leaf list on the ingress LSRA.
   
   
   
   # Configure explicit paths on LSRA to LSRC, LSRE, and LSRF.
   
   ```
   [~LSRA] explicit-path tolsrc
   ```
   ```
   [*LSRA-explicit-path-tolsrc] next hop 10.1.1.2
   ```
   ```
   [*LSRA-explicit-path-tolsrc] next hop 10.3.1.2
   ```
   ```
   [*LSRA-explicit-path-tolsrc] quit
   ```
   ```
   [*LSRA] explicit-path tolsrf
   ```
   ```
   [*LSRA-explicit-path-tolsrf] next hop 10.1.1.2
   ```
   ```
   [*LSRA-explicit-path-tolsrf] next hop 10.2.1.2
   ```
   ```
   [*LSRA-explicit-path-tolsrf] next hop 10.5.1.2
   ```
   ```
   [*LSRA-explicit-path-tolsrf] quit
   ```
   ```
   [*LSRA] explicit-path tolsre
   ```
   ```
   [*LSRA-explicit-path-tolsre] next hop 10.1.1.2
   ```
   ```
   [*LSRA-explicit-path-tolsre] next hop 10.2.1.2
   ```
   ```
   [*LSRA-explicit-path-tolsre] next hop 10.4.1.2
   ```
   ```
   [*LSRA-explicit-path-tolsre] commit
   ```
   ```
   [~LSRA-explicit-path-tolsre] quit
   ```
   
   # Configure a leaf list **iptv1** on LSRA and add leaf node addresses to the leaf list.
   
   ```
   [~LSRA] mpls te leaf-list iptv1
   ```
   ```
   [*LSRA-mpls-te-leaf-list-iptv1] destination 3.3.3.3
   ```
   ```
   [*LSRA-mpls-te-leaf-list-iptv1-destination-3.3.3.3] path explicit-path tolsrc
   ```
   ```
   [*LSRA-mpls-te-leaf-list-iptv1-destination-3.3.3.3] quit
   ```
   ```
   [*LSRA-mpls-te-leaf-list-iptv1] destination 5.5.5.5
   ```
   ```
   [*LSRA-mpls-te-leaf-list-iptv1-destination-5.5.5.5] path explicit-path tolsre
   ```
   ```
   [*LSRA-mpls-te-leaf-list-iptv1-destination-5.5.5.5] quit
   ```
   ```
   [*LSRA-mpls-te-leaf-list-iptv1] destination 6.6.6.6
   ```
   ```
   [*LSRA-mpls-te-leaf-list-iptv1-destination-6.6.6.6] path explicit-path tolsrf
   ```
   ```
   [*LSRA-mpls-te-leaf-list-iptv1-destination-6.6.6.6] commit
   ```
   ```
   [~LSRA-mpls-te-leaf-list-iptv1-destination-6.6.6.6] quit
   ```
7. Configure the P2MP TE tunnel interface on the ingress LSRA.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] interface Tunnel 10
   ```
   ```
   [*LSRA-Tunnel10] ip address unnumbered interface loopback 1
   ```
   ```
   [*LSRA-Tunnel10] tunnel-protocol mpls te
   ```
   ```
   [*LSRA-Tunnel10] mpls te p2mp-mode
   ```
   ```
   [*LSRA-Tunnel10] mpls te tunnel-id 100
   ```
   ```
   [*LSRA-Tunnel10] mpls te leaf-list iptv1
   ```
   ```
   [*LSRA-Tunnel10] mpls te bandwidth ct0 1000
   ```
   ```
   [*LSRA-Tunnel10] commit
   ```
   ```
   [~LSRA-Tunnel10] quit
   ```
   
   The P2MP TE tunnel configuration is complete after this step is performed.
8. Verify the configuration.
   
   After completing the configurations, run the **display mpls te p2mp tunnel-interface Tunnel10** command on LSRA. The status of Tunnel 10 on LSRA is **UP**, and the status of all sub-LSPs is **UP**.
   ```
   [~LSRA] display mpls te p2mp tunnel-interface Tunnel10
   ```
   ```
   ------------------------------------------------------------------------------
                         Tunnel10
   ------------------------------------------------------------------------------
   Tunnel State        : UP
   Session ID          : 100
   Ingress LSR ID      : 1.1.1.1           P2MP ID      : 0x1010101
   Admin State         : UP                Oper State   : UP                                            
   Primary LSP State   : UP
   ------------------------------------------------------------------------------
   Main LSP State      : UP                LSP ID        : 8
   ------------------------------------------------------------------------------
   S2L Dest Addr       : 3.3.3.3           State         : UP
   S2L Dest Addr       : 5.5.5.5           State         : UP
   S2L Dest Addr       : 6.6.6.6           State         : UP
   ```

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  sysname LSRA
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
   mpls te cspf
  #
  explicit-path tolsrc
   next hop 10.1.1.2
   next hop 10.3.1.2
  #
  explicit-path tolsrf
   next hop 10.1.1.2
   next hop 10.2.1.2
   next hop 10.5.1.2
  #
  explicit-path tolsre
   next hop 10.1.1.2
   next hop 10.2.1.2
   next hop 10.4.1.2
  #
  mpls te leaf-list iptv1
   #
   destination 3.3.3.3
    path explicit-path tolsrc
   #
   destination 5.5.5.5
    path explicit-path tolsre
   #
   destination 6.6.6.6
    path explicit-path tolsrf
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.0005.0000.0000.0001.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   mpls te p2mp-mode
   mpls te bandwidth ct0 1000
   mpls te leaf-list iptv1
   mpls te tunnel-id 100
  #
  return
  ```
* LSRB configuration file
  
  ```
  #
  sysname LSRB
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.0005.0000.0000.0002.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  return
  ```
* LSRC configuration file
  
  ```
  #
  sysname LSRC
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.0005.0000.0000.0003.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  return
  ```
* LSRD configuration file
  
  ```
  #
  sysname LSRD
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.0005.0000.0000.0004.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.5.1.1 255.255.255.0
   isis enable 1  
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   isis enable 1
  #
  return
  ```
* LSRE configuration file
  
  ```
  #
  sysname LSRE
  #
  mpls lsr-id 5.5.5.5
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.0005.0000.0000.0005.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.4.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #               
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
   isis enable 1
  #
  return
  ```
* LSRF configuration file
  
  ```
  #
  sysname LSRF
  #
  mpls lsr-id 6.6.6.6
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.0005.0000.0000.0006.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.5.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 6.6.6.6 255.255.255.255
   isis enable 1
  #
  return
  ```