Example for Configuring an NG MVPN (PIM-SM RPT Setup Across the Public Network) with (\*, G) Join to Carry Multicast Traffic over an RSVP-TE P2MP Tunnel
========================================================================================================================================================

This section provides an example for configuring an NG MVPN (PIM-SM RPT setup across the public network) with (\*, G) Join to carry multicast traffic over an RSVP-TE P2MP tunnel.

#### Networking Requirements

On the single-AS NG MVPN shown in [Figure 1](#EN-US_TASK_0000001270153521__fig_dc_vrp_cfg_ngmvpn_001801), RSVP-TE tunnels have been deployed to carry BGP/MPLS IP VPN services. In this NG MVPN configuration example, users join a multicast group through PIM-SM (\*, G) Join messages, and PIM-SM RPTs are set up across the public network.

**Figure 1** Configuring an NG MVPN (PIM-SM RPT setup across the public network) with (\*, G) Join to carry multicast traffic over an RSVP-TE P2MP tunnel![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001270193689.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BGP/MPLS IP VPN to ensure that the unicast VPN is running properly.
2. Enable P2MP TE globally and configure a P2MP TE template on PEs so that the PEs can use RSVP-TE to establish P2MP tunnels.
3. Establish BGP MVPN peer relationships between the PEs so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes (C is short for customer, and C-multicast routes are advertised by a CE).
4. Configure PE1 to use RSVP-TE to establish an I-PMSI tunnel so that an RSVP-TE P2MP tunnel is established. Configure PIM-SM RPTs to be set up across the public network.
5. Configure PIM-SM on the PEs' interfaces bound to a VPN instance and on the CEs' interfaces connected to the PEs so that VPN multicast routing entries are generated for multicast traffic forwarding.
6. Configure a static RP for a VPN instance.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In an NG MVPN scenario, if PIM-SM RPT setup is across the public network and triggered by (\*, G) Join messages, a static RP must be configured, either on a PE or CE.
7. Configure IGMP on the interfaces connecting a multicast device to a user network segment to allow the device to manage multicast group members on the network segment.

#### Data Preparation

To complete the configuration, you need the following data:

* Loopback1 interface addresses of PE1, PE2, PE3, and CE3 (1.1.1.1, 2.2.2.2, 3.3.3.3, and 4.4.4.4)
* OSPF process on the public network (process 1) in Area 0; OSPF multi-process (process 2) in Area 0
* MPLS LSR IDs of PE1, PE2, and PE3 (1.1.1.1, 2.2.2.2, and 3.3.3.3)
* AS number of PEs (AS 100)
* MVPN IDs of PE1, PE2, and PE3 (1.1.1.1, 2.2.2.2, and 3.3.3.3)
* VPN instance name (VPNA), RDs (100:1, 200:1, and 300:1), and VPN targets (3:3) of PE1, PE2, and PE3

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Assign an IP address to each interface of devices on the VPN backbone network and VPN sites.
      
      
      
      Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0000001270153521__fig_dc_vrp_cfg_ngmvpn_001801). For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
   2. Configure an IGP for interworking on the BGP/MPLS IP VPN backbone network.
      
      
      
      OSPF is used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      To use OSPF in an RSVP-TE P2MP tunnel scenario, you must [configure IGP TE (OSPF or IS-IS)](dc_vrp_te-p2p_cfg_0005.html).
   3. Configure basic MPLS functions and enable MPLS TE to establish MPLS TE tunnels on the MPLS backbone network.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] mpls lsr-id 1.1.1.1
      ```
      ```
      [*PE1] mpls
      ```
      ```
      [*PE1-mpls] mpls te
      ```
      ```
      [*PE1-mpls] mpls rsvp-te
      ```
      ```
      [*PE1-mpls] mpls te cspf
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
      [*PE1-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE1] commit
      ```
      
      The configuration of PE2 and PE3 is similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
   4. Establish an MP-IBGP peer relationship between PEs.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] bgp 100
      ```
      ```
      [*PE1-bgp] peer 3.3.3.3 as-number 100
      ```
      ```
      [*PE1-bgp] peer 3.3.3.3 connect-interface LoopBack1
      ```
      ```
      [*PE1-bgp] peer 2.2.2.2 as-number 100
      ```
      ```
      [*PE1-bgp] peer 2.2.2.2 connect-interface LoopBack1
      ```
      ```
      [*PE1-bgp] ipv4-family vpnv4
      ```
      ```
      [*PE1-bgp-af-vpnv4] peer 3.3.3.3 enable
      ```
      ```
      [*PE1-bgp-af-vpnv4] peer 2.2.2.2 enable
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
      
      The configuration of PE2 and PE3 is similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
   5. Configure a VPN instance on each PE and bind the VPN instance on each PE to its interface connecting to a CE.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] ip vpn-instance VPNA
      ```
      ```
      [*PE1-vpn-instance-VPNA] ipv4-family
      ```
      ```
      [*PE1-vpn-instance-VPNA-af-ipv4] route-distinguisher 100:1
      ```
      ```
      [*PE1-vpn-instance-VPNA-af-ipv4] vpn-target 3:3 both
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
      
      The configuration of PE2 and PE3 is similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
   6. Configure OSPF multi-instance on each PE to import VPN routes.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] ospf 2 vpn-instance VPNA
      ```
      ```
      [*PE1-ospf-2] import-route bgp
      ```
      ```
      [*PE1-ospf-2] area 0
      ```
      ```
      [*PE1-ospf-2-area-0.0.0.0] network 192.168.1.0 0.0.0.255
      ```
      ```
      [*PE1-ospf-2-area-0.0.0.0] quit
      ```
      ```
      [*PE1-ospf-2] quit
      ```
      ```
      [*PE1] bgp 100
      ```
      ```
      [*PE1-bgp] ipv4-family vpn-instance VPNA
      ```
      ```
      [*PE1-bgp-VPNA] import-route ospf 2
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
      
      The configuration of PE2 and PE3 is similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
   7. # Configure OSPF on each CE.
      
      
      
      # Configure CE1.
      
      ```
      [~CE1] ospf 2
      ```
      ```
      [*CE1-ospf-2] area 0
      ```
      ```
      [*CE1-ospf-2-area-0.0.0.0] network 10.1.3.0 0.0.0.255
      ```
      ```
      [*CE1-ospf-2-area-0.0.0.0] network 10.1.4.0 0.0.0.255
      ```
      ```
      [*CE1-ospf-2-area-0.0.0.0] network 192.168.1.0 0.0.0.255
      ```
      ```
      [*CE1-ospf-2-area-0.0.0.0] quit
      ```
      ```
      [*CE1-ospf-2] quit
      ```
      ```
      [*CE1] commit
      ```
      
      The configuration of CE2 and CE3 is similar to the configuration of CE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
      
      After the configurations are complete, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on CE2. The command outputs show that CE2 has routes to CE1. Run the [**ping**](cmdqueryname=ping) command on CE2 to ping CE1. The command output shows that the ping operation succeeds.
      
      ```
      [~CE2] display ip routing-table
      ```
      ```
      Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
      ------------------------------------------------------------------------------
      Routing Table : _public_
               Destinations : 15       Routes : 15
      
      Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
      
              4.4.4.4/32  OSPF    10   3             D   192.168.2.1     Gigabitethernet0/1/0
             10.1.3.0/24  OSPF    10   4             D   192.168.2.1     Gigabitethernet0/1/0
             10.1.4.0/24  OSPF    10   4             D   192.168.2.1     Gigabitethernet0/1/0
             10.1.5.0/24  Direct  0    0             D   10.1.5.1        Gigabitethernet0/1/1
             10.1.5.1/32  Direct  0    0             D   127.0.0.1       Gigabitethernet0/1/1
           10.1.5.255/32  Direct  0    0             D   127.0.0.1       Gigabitethernet0/1/1
            127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
            127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0
      127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
          192.168.1.0/24  OSPF    10   3             D   192.168.2.1     Gigabitethernet0/1/0
          192.168.2.0/24  Direct  0    0             D   192.168.2.2     Gigabitethernet0/1/0
          192.168.2.2/32  Direct  0    0             D   127.0.0.1       Gigabitethernet0/1/0
        192.168.2.255/32  Direct  0    0             D   127.0.0.1       Gigabitethernet0/1/0
          192.168.3.0/24  OSPF    10   3             D   192.168.2.1     Gigabitethernet0/1/0
      255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
      ```
      ```
      [~CE2] ping 10.1.3.1
      ```
      ```
        PING 10.1.3.1: 56  data bytes, press CTRL_C to break
          Reply from 10.1.3.1: bytes=56 Sequence=1 ttl=253 time=5 ms
          Reply from 10.1.3.1: bytes=56 Sequence=2 ttl=253 time=2 ms
          Reply from 10.1.3.1: bytes=56 Sequence=3 ttl=253 time=2 ms
          Reply from 10.1.3.1: bytes=56 Sequence=4 ttl=253 time=2 ms
          Reply from 10.1.3.1: bytes=56 Sequence=5 ttl=253 time=1 ms
      
        --- 10.1.3.1 ping statistics ---
          5 packet(s) transmitted
          5 packet(s) received
          0.00% packet loss
          round-trip min/avg/max = 1/2/5 ms                 
      ```
2. Enable P2MP TE globally and configure a P2MP TE template.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls
   ```
   ```
   [*PE1-mpls] mpls te p2mp-te
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] mpls te p2mp-template t1
   ```
   ```
   [*PE1-te-p2mp-template-t1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls
   ```
   ```
   [*PE2-mpls] mpls te p2mp-te
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] mpls te p2mp-template t1
   ```
   ```
   [*PE2-te-p2mp-template-t1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls
   ```
   ```
   [*PE3-mpls] mpls te p2mp-te
   ```
   ```
   [*PE3-mpls] quit
   ```
   ```
   [*PE3] commit
   ```
3. Establish a BGP MVPN peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family mvpn
   ```
   ```
   [*PE1-bgp-af-mvpn] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-mvpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-mvpn] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration of PE2 and PE3 is similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
   
   After completing the configurations, run the [**display bgp mvpn all peer**](cmdqueryname=display+bgp+mvpn+all+peer) command on the PEs. The command output shows that PE3 has established a BGP MVPN peer relationship with PE1 and PE2. The following example uses the command output on PE3:
   
   ```
   [~PE3] display bgp mvpn all peer
   ```
   ```
    BGP local router ID : 10.1.1.2
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     1.1.1.1         4         100      159      227     0 02:52:24 Established    1
     2.2.2.2         4         100      148      226     0 02:52:26 Established    1
   ```
4. Configure devices to use RSVP-TE to establish an I-PMSI tunnel, and configure PIM-SM RPTs to be set up across the public network.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure PIM-SM RPTs to be set up across the public network, run the [**rpt-spt mode**](cmdqueryname=rpt-spt+mode) command. PEs in the same VPN instance must use the same PIM-SM RPT setup mode.
   
   * # Configure PE1.
     
     ```
     [~PE1] multicast mvpn 1.1.1.1
     ```
     ```
     [*PE1] ip vpn-instance VPNA
     ```
     ```
     [*PE1-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4] multicast routing-enable
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] sender-enable
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] ipmsi-tunnel
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] mpls te
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] p2mp-template t1
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] quit
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
   * # Configure PE2.
     
     ```
     [~PE2] multicast mvpn 2.2.2.2
     ```
     ```
     [*PE2] ip vpn-instance VPNA
     ```
     ```
     [*PE2-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4] multicast routing-enable
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] sender-enable
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] ipmsi-tunnel
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] mpls te
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] p2mp-template t1
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] quit
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
   * # Configure PE3.
     
     ```
     [~PE3] multicast mvpn 3.3.3.3
     ```
     ```
     [*PE3] ip vpn-instance VPNA
     ```
     ```
     [*PE3-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv4] multicast routing-enable
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] quit
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
5. Configure PIM-SM.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] interface gigabitethernet0/1/1
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
     
     The configuration of PE2 and PE3 is similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
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
     
     The configuration of CE2 and CE3 is similar to the configuration of CE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153521__example_dc_vrp_cfg_ngmvpn_001801) in this section.
6. Configure a static RP for the VPN instance.
   
   
   * # Configure CE1.
     
     ```
     [~CE1] pim
     ```
     ```
     [*CE1-pim] static-rp 4.4.4.4
     ```
     ```
     [*CE1-pim] quit
     ```
     ```
     [*CE1] commit
     ```
   * # Configure CE3.
     
     ```
     [~CE3] interface LoopBack1
     ```
     ```
     [*CE3-LoopBack1] ip address 4.4.4.4 255.255.255.255
     ```
     ```
     [*CE3-LoopBack1] pim sm
     ```
     ```
     [*CE3-LoopBack1] quit
     ```
     ```
     [*CE3] pim
     ```
     ```
     [*CE3-pim] static-rp 4.4.4.4
     ```
     ```
     [*CE3-pim] quit
     ```
     ```
     [*CE3] commit
     ```
   * # Configure PE1.
     
     ```
     [~PE1] pim vpn-instance VPNA
     ```
     ```
     [*PE1-pim-VPNA] static-rp 4.4.4.4
     ```
     ```
     [*PE1-pim-VPNA] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] pim vpn-instance VPNA
     ```
     ```
     [*PE2-pim-VPNA] static-rp 4.4.4.4
     ```
     ```
     [*PE2-pim-VPNA] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure PE3.
     
     ```
     [~PE3] pim vpn-instance VPNA
     ```
     ```
     [*PE3-pim-VPNA] static-rp 4.4.4.4
     ```
     ```
     [*PE3-pim-VPNA] quit
     ```
     ```
     [*PE3] commit
     ```
   * # Configure CE2.
     
     ```
     [~CE2] pim
     ```
     ```
     [*CE2-pim] static-rp 4.4.4.4
     ```
     ```
     [*CE2-pim] quit
     ```
     ```
     [*CE2] commit
     ```
7. Configure IGMP.
   
   
   ```
   [~CE2] interface gigabitethernet0/1/1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] igmp enable
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] igmp static-group 225.0.0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] commit
   ```
8. Verify the configuration.
   
   
   
   After the configurations are complete, an NG MVPN with (\*, G) join is configured. In this example, multicast source (10.1.3.0/24) in the PIM-SM domain sends multicast traffic to multicast group G (225.0.0.1). The receiver joins multicast group G and receives multicast traffic from this group. Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command to check whether multicast routing entries are correctly generated and whether the NG MVPN with (\*, G) join is successfully configured.
   
   Run the [**display pim vpn-instance**](cmdqueryname=display+pim+vpn-instance) **routing-table** command on the PEs to check their PIM routing tables of the VPN instance.
   
   ```
   [~PE1] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.1.3.100, 225.0.0.1)
        RP: 4.4.4.4
        Protocol: pim-sm, Flag: SPT ACT SG_RCVR 2BGP
        UpTime: 02:05:57
        Upstream interface: GigabitEthernet0/1/1
            Upstream neighbor: 192.168.1.1
            RPF prime neighbor: 192.168.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: pseudo
                Protocol: BGP, UpTime: 00:02:08, Expires: -          
   ```
   ```
   [~PE2] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 1 (*, G) entry; 1 (S, G) entry
   
    (*, 225.0.0.1)
        RP: 4.4.4.4
        Protocol: pim-sm, Flag: WC
        UpTime: 00:03:28
        Upstream interface: GigabitEthernet0/1/1
            Upstream neighbor: 192.168.3.1
            RPF prime neighbor: 192.168.3.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: pseudo
                Protocol: BGP, UpTime: 00:03:28, Expires: -
   
    (10.1.3.100, 225.0.0.1)
        RP: 4.4.4.4
        Protocol: pim-sm, Flag: RPT ACT BGP
        UpTime: 02:04:15
        Upstream interface: GigabitEthernet0/1/1
            Upstream neighbor: 192.168.3.1
            RPF prime neighbor: 192.168.3.1
        Downstream interface(s) information: none
   
   ```
   ```
   [~PE3] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 1 (*, G) entry; 1 (S, G) entry
   
    (*, 225.0.0.1)
        RP: 4.4.4.4
        Protocol: pim-sm, Flag: WC
        UpTime: 00:02:48
        Upstream interface: through-BGP
            Upstream neighbor: 2.2.2.2
            RPF prime neighbor: 2.2.2.2
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:02:48, Expires: 00:02:12
   
    (10.1.3.100, 225.0.0.1)
        RP: 4.4.4.4
        Protocol: pim-sm, Flag: RPT SPT ACT BGP
        UpTime: 00:02:45
        Upstream interface: through-BGP
            Upstream neighbor: 1.1.1.1
            RPF prime neighbor: 1.1.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:02:45, Expires: 00:02:14     
   ```
   
   Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command on the CEs to check the PIM routing tables.
   
   ```
   [~CE1] display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.1.3.100, 225.0.0.1)
        RP: 4.4.4.4
        Protocol: pim-sm, Flag: SPT LOC ACT
        UpTime: 04:07:50
        Upstream interface: GigabitEthernet0/1/0
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:04:15, Expires: 00:03:02
                                                                           
   ```
   ```
   [~CE2] display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 1 (*, G) entry; 1 (S, G) entry
   
    (*, 225.0.0.1)
        RP: 4.4.4.4
        Protocol: pim-sm, Flag: WC
        UpTime: 03:53:23
        Upstream interface: GigabitEthernet0/1/0
            Upstream neighbor: 192.168.2.1
            RPF prime neighbor: 192.168.2.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: static, UpTime: 03:53:23, Expires: -
   
    (10.1.3.100, 225.0.0.1)
        RP: 4.4.4.4
        Protocol: pim-sm, Flag: SPT ACT
        UpTime: 00:04:50
        Upstream interface: GigabitEthernet0/1/0
            Upstream neighbor: 192.168.2.1
            RPF prime neighbor: 192.168.2.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:04:50, Expires: -   
   ```
   ```
   [~CE3] display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 1 (*, G) entry; 1 (S, G) entry
   
    (*, 225.0.0.1)
        RP: 4.4.4.4 (local)
        Protocol: pim-sm, Flag: WC
        UpTime: 00:08:31
        Upstream interface: Register
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:05:08, Expires: 00:03:22
   
    (10.1.3.100, 225.0.0.1)
        RP: 4.4.4.4 (local)
        Protocol: pim-sm, Flag: RPT 2MSDP ACT
        UpTime: 04:02:03
        Upstream interface: Register
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information: none   
   ```
   
   The command output shows that PE2 connected to the RP has received a Join message from PE3 connected to a receiver, created a (\*, G) entry, and implemented a switchover from an RPT to an SPT. (S, G) PIM routing entries have been created successfully, and the receiver can receive multicast data from the multicast source 10.1.3.100.
   
   Run the [**display mvpn vpn-instance**](cmdqueryname=display+mvpn+vpn-instance) *vpn-instance-name* **ipmsi verbose** command on the PEs to check I-PMSI tunnel establishment. The following example uses the command output on PE3:
   
   ```
   [~PE3] display mvpn vpn-instance VPNA ipmsi verbose
   ```
   ```
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: RSVP-TE P2MP LSP
   Tunnel state: --
   P2MP ID: 0x1010101
   Tunnel ID: 32769
   Extended tunnel ID: 1.1.1.1
   Root: 1.1.1.1
   Leaf:
     1: 3.3.3.3 (local)
   Total number of (S, G): 1
       1. (10.1.3.100, 225.0.0.1)
   
   Tunnel type: RSVP-TE P2MP LSP
   Tunnel state: --
   P2MP ID: 0x2020202
   Tunnel ID: 32769
   Extended tunnel ID: 2.2.2.2
   Root: 2.2.2.2
   Leaf:
     1: 3.3.3.3 (local)  
   ```
   
   The command outputs show that two RSVP-TE P2MP tunnels have been established, with PE1 and PE2 as the root nodes and PE3 as a leaf node.

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   pim sm
  #
  ospf 2
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 10.1.4.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
  #
  pim
   static-rp 4.4.4.4
  #
  return
  
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.3.1 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   pim sm
  #
  ospf 2
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.1.4.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
  #
  pim
   static-rp 4.4.4.4
  #
  return
  
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  multicast mvpn 1.1.1.1
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     rpt-spt mode
     ipmsi-tunnel
      mpls te
       p2mp-template t1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
   mpls te cspf
  #
  mpls te p2mp-template t1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
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
   ipv4-family mvpn
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance VPNA
    import-route ospf 2
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
    mpls-te enable
  #
  ospf 2 vpn-instance VPNA
   import-route bgp
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  pim vpn-instance VPNA
   static-rp 4.4.4.4
  #
  return
  
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  multicast mvpn 2.2.2.2
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     rpt-spt mode
     ipmsi-tunnel
      mpls te
       p2mp-template t1
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
   mpls te cspf
  #
  mpls te p2mp-template t1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.3.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
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
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance VPNA
    import-route ospf 2
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.2.0 0.0.0.255
    mpls-te enable
  #
  ospf 2 vpn-instance VPNA
   import-route bgp
   area 0.0.0.0
    network 192.168.3.0 0.0.0.255
  #
  pim vpn-instance VPNA
   static-rp 4.4.4.4
  #
  return
  
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
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
    mvpn
     c-multicast signaling bgp
     rpt-spt mode
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
   mpls te cspf
  #
  mpls ldp
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
   ip binding vpn-instance VPNA
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
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
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance VPNA
    import-route ospf 2
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    mpls-te enable
  #
  ospf 2 vpn-instance VPNA
   import-route bgp
   area 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  pim vpn-instance VPNA
   static-rp 4.4.4.4
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.5.1 255.255.255.0
   pim sm
   igmp enable
   igmp static-group 225.0.0.1
  #
  ospf 2
   area 0.0.0.0
    network 10.1.5.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  pim
   static-rp 4.4.4.4 
  #
  return
  ```