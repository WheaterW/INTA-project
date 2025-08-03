Example for Configuring NG MVPN Extranet in the Local Route Leaking Scenario Where the Source and Receiver VPN Instances Reside on the Same PE
==============================================================================================================================================

This section provides an example for configuring NG MVPN extranet in the local route leaking scenario.

#### Networking Requirements

In NG MVPN applications, a service provider in a VPN may need to provide multicast services for users in other VPNs. Therefore, multicast services need to be distributed across VPNs.

In the local route leaking scenario of single-AS NG MVPN shown in [Figure 1](#EN-US_TASK_0000001270153557__fig_dc_vrp_cfg_ngmvpn_012301), the receiver in VPN RED requires multicast data from the source in VPN BLUE. To meet this requirement, deploy NG MVPN extranet.

**Figure 1** Configuring NG MVPN extranet in the local route leaking scenario where the source and receiver VPN instances reside on the same PE![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001225833724.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic single-AS NG MVPN functions.
2. Configure a rendezvous point (RP) to serve the NG MVPN extranet.

#### Data Preparation

To complete the configuration, you need the following data:

* RD of VPN BLUE: 100:1; VPN target of VPN BLUE: 100:1
* RD of VPN RED: 200:1; VPN targets of VPN RED: 200:1 and 100:1
* Multicast group address used by the NG MVPN extranet: 228.0.0.1

#### Procedure

1. Configure basic single-AS NG MVPN functions.
   1. Configure basic MPLS functions and MPLS LDP and set up LDP LSPs on the public network.
      
      
      
      # Configure PE2.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname PE2
      ```
      ```
      [*HUAWEI] commit
      ```
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
      [*PE2] interface gigabitethernet 0/1/1
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
   2. Configure unicast OSPF and multicast on the public network to ensure that the multicast routes on the network are reachable.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] multicast routing-enable
      ```
      ```
      [*PE2] interface loopback 1
      ```
      ```
      [*PE2-LoopBack1] ip address 3.3.3.3 32
      ```
      ```
      [*PE2-LoopBack1] pim sm
      ```
      ```
      [*PE2-LoopBack1] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE2-Gigabitethernet0/1/1] ip address 192.168.2.2 24
      ```
      ```
      [*PE2-Gigabitethernet0/1/1] pim sm
      ```
      ```
      [*PE2-Gigabitethernet0/1/1] quit
      ```
      ```
      [*PE2] ospf 1
      ```
      ```
      [*PE2-ospf-1] area 0
      ```
      ```
      [*PE2-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
      ```
      ```
      [*PE2-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
      ```
      ```
      [*PE2-ospf-1-area-0.0.0.0] quit
      ```
      ```
      [*PE2-ospf-1] quit
      ```
      ```
      [*PE2] commit
      ```
   3. On PE2, configure a VPN instance, enable the IPv4 address family for the VPN instance, and bind the interface that connects PE2 to the corresponding CE to the VPN instance.
      
      
      
      # On PE2, create VPN BLUE, enable multicast globally and the IPv4 address family for VPN BLUE, and bind PE2's GE 0/1/0 connected to CE1 to VPN BLUE.
      
      ```
      [~PE2] ip vpn-instance BLUE
      ```
      ```
      [*PE2-vpn-instance-BLUE] ipv4-family
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4] route-distinguisher 100:1
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4] vpn-target 100:1 both
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4] multicast routing-enable
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4] mvpn
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn] sender-enable
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn] c-multicast signaling bgp
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn] rpt-spt mode
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn] ipmsi-tunnel
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn-ipmsi] mldp
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn-ipmsi] quit
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn] quit
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4] quit
      ```
      ```
      [*PE2-vpn-instance-BLUE] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/0
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] ip binding vpn-instance BLUE
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] ip address 10.1.2.2 24
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
      
      # On PE2, create VPN RED, enable multicast globally and the IPv4 address family for VPN RED, and bind PE2's GE 0/1/2 connected to CE2 to VPN RED. Import routes from VPN BLUE into VPN RED.
      
      ```
      [~PE2] ip vpn-instance RED
      ```
      ```
      [*PE2-vpn-instance-RED] ipv4-family
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4] route-distinguisher 200:1
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4] vpn-target 200:1 both
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4] vpn-target 100:1 import-extcommunity
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4] multicast routing-enable
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4] mvpn
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4-mvpn] c-multicast signaling bgp
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4-mvpn] multicast extranet select-rpf vpn-instance BLUE group 228.0.0.1 24
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4] quit
      ```
      ```
      [*PE2-vpn-instance-RED] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] ip binding vpn-instance RED
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] ip address 10.1.3.1 24
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
   4. Configure a unicast routing protocol and enable the multicast function for VPN BLUE and VPN RED to ensure that multicast routes of the VPN instances are reachable.
      
      
      
      # Configure CE1.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname CE1
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~CE1] interface gigabitethernet 0/1/0
      ```
      ```
      [*CE1-GigabitEthernet0/1/0] ip address 10.1.2.1 24
      ```
      ```
      [*CE1-GigabitEthernet0/1/0] pim sm
      ```
      ```
      [*CE1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*CE1] interface gigabitethernet 0/1/1
      ```
      ```
      [*CE1-GigabitEthernet0/1/1] ip address 10.1.1.1 24
      ```
      ```
      [*CE1-GigabitEthernet0/1/1] pim sm
      ```
      ```
      [*CE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*CE1] interface loopback 1
      ```
      ```
      [*CE1-LoppBack1] ip address 4.4.4.4 32
      ```
      ```
      [*CE1-LoppBack1] pim sm
      ```
      ```
      [*CE1-LoppBack1] quit
      ```
      ```
      [*CE1] ospf 3
      ```
      ```
      [*CE1-ospf-3] area 0
      ```
      ```
      [*CE1-ospf-3-area-0.0.0.0] network 10.1.1.0 0.0.0.255
      ```
      ```
      [*CE1-ospf-3-area-0.0.0.0] network 10.1.2.0 0.0.0.255
      ```
      ```
      [*CE1-ospf-3-area-0.0.0.0] network 4.4.4.4 0.0.0.0
      ```
      ```
      [*CE1-ospf-3-area-0.0.0.0] quit
      ```
      ```
      [*CE1-ospf-3] quit
      ```
      ```
      [*CE1] commit
      ```
      
      # Configure CE2.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname CE2
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~CE2] interface gigabitethernet 0/1/2
      ```
      ```
      [*CE2-GigabitEthernet0/1/2] ip address 10.1.3.2 24
      ```
      ```
      [*CE2-GigabitEthernet0/1/2] pim sm
      ```
      ```
      [*CE2-GigabitEthernet0/1/2] quit
      ```
      ```
      [*CE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*CE2-GigabitEthernet0/1/1] ip address 10.1.4.1 24
      ```
      ```
      [*CE2-GigabitEthernet0/1/1] pim sm
      ```
      ```
      [*CE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*CE2] ospf 2
      ```
      ```
      [*CE2-ospf-2] area 0
      ```
      ```
      [*CE2-ospf-2-area-0.0.0.0] network 10.1.3.0 0.0.0.255
      ```
      ```
      [*CE2-ospf-2-area-0.0.0.0] network 10.1.4.0 0.0.0.255
      ```
      ```
      [*CE2-ospf-2-area-0.0.0.0] quit
      ```
      ```
      [*CE2-ospf-2] quit
      ```
      ```
      [*CE2] commit
      ```
   5. Establish MP-IBGP peer relationships between PEs, and configure a unicast routing protocol between PEs and corresponding CEs to ensure routing between the PEs and CEs.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] bgp 100
      ```
      ```
      [*PE2-bgp] peer 1.1.1.1 as-number 100
      ```
      ```
      [*PE2-bgp] peer 1.1.1.1 connect-interface LoopBack 1
      ```
      ```
      [*PE2-bgp] ipv4-family vpn-instance BLUE
      ```
      ```
      [*PE2-bgp-BLUE] import-route ospf 3
      ```
      ```
      [*PE2-bgp-BLUE] import-route direct
      ```
      ```
      [*PE2-bgp-BLUE] quit
      ```
      ```
      [*PE2-bgp] ipv4-family vpn-instance RED
      ```
      ```
      [*PE2-bgp-RED] import-route ospf 2
      ```
      ```
      [*PE2-bgp-RED] import-route direct
      ```
      ```
      [*PE2-bgp-RED] quit
      ```
      ```
      [*PE2-bgp] ipv4-family vpnv4
      ```
      ```
      [*PE2-bgp-af-vpnv4] peer 1.1.1.1 enable
      ```
      ```
      [*PE2-bgp-af-vpnv4] quit
      ```
      ```
      [*PE2-bgp] quit
      ```
      ```
      [*PE2] ospf 2 vpn-instance RED
      ```
      ```
      [*PE2-ospf-2] import-route bgp
      ```
      ```
      [*PE2-ospf-2] area 0.0.0.0
      ```
      ```
      [*PE2-ospf-2-area-0.0.0.0] network 10.1.3.0 0.0.0.255
      ```
      ```
      [*PE2-ospf-2-area-0.0.0.0] quit
      ```
      ```
      [*PE2-ospf-2] quit
      ```
      ```
      [*PE2] ospf 3 vpn-instance BLUE
      ```
      ```
      [*PE2-ospf-3] import-route bgp
      ```
      ```
      [*PE2-ospf-3] area 0.0.0.0
      ```
      ```
      [*PE2-ospf-3-area-0.0.0.0] network 10.1.2.0 0.0.0.255
      ```
      ```
      [*PE2-ospf-3-area-0.0.0.0] quit
      ```
      ```
      [*PE2-ospf-3] quit
      ```
      ```
      [*PE2] commit
      ```
2. Configure an RP to serve the NG MVPN extranet.
   
   
   * # In the VPN BLUE and VPN RED views on CE1, CE2, and PE2, configure CE1's loopback 1 as a static RP to serve the NG MVPN extranet.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Source and receiver VPN instances support only static RPs. The routes to a static RP and source must be in the same VPN instance.
     
     # Configure CE1.
     
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
     
     # Configure PE2.
     
     ```
     [~PE2] pim vpn-instance BLUE
     ```
     ```
     [*PE2-pim-BLUE] static-rp 4.4.4.4
     ```
     ```
     [*PE2-pim-BLUE] quit
     ```
     ```
     [*PE2] pim vpn-instance RED
     ```
     ```
     [*PE2-pim-RED] static-rp 4.4.4.4
     ```
     ```
     [*PE2-pim-RED] quit
     ```
     ```
     [*PE2] commit
     ```
     
     # Configure CE2.
     
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
3. Verify the configuration.
   
   
   
   By checking the configuration, you can view that the receiver in VPN RED can receive multicast data from the source in VPN BLUE.
   
   Run the **display pim routing-table** command on PE2 to check information about the PIM routing table. The following command output shows that the upstream interface of the RPF route selected by the PIM entry with 228.0.0.1 as the group address belongs to VPN BLUE.
   
   ```
   [~PE2] display pim vpn-instance RED routing-table extranet source-vpn-instance vpn-instance BLUE
   ```
   ```
    VPN-Instance: RED
    Total 1 (*, G) entry; 1 (S, G) entry
    
    Total matched 1 (*, G) entry; 1 (S, G) entry
   
    (*, 228.0.0.1)
        RP: 4.4.4.4 
        Protocol: pim-sm, Flag: WC 
        UpTime: 00:03:05
        Upstream interface: MCAST_Extranet(BLUE), Refresh time: 00:03:05
            Upstream neighbor: 10.1.2.1
            RPF prime neighbor: 10.1.2.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/2
                Protocol: pim-sm, UpTime: 00:03:05, Expires: 00:03:26
    
    (10.1.1.2, 228.0.0.1)
        RP: 4.4.4.4 
        Protocol: pim-sm, Flag: SPT ACT 
        UpTime: 00:00:02
        Upstream interface: MCAST_Extranet(BLUE), Refresh time: 00:00:02
            Upstream neighbor: 10.1.2.1
            RPF prime neighbor: 10.1.2.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/2
                Protocol: pim-sm, UpTime: 00:00:06, Expires: -
   ```
   
   The following command output shows that the multicast extranet receiver of VPN BLUE belongs to VPN RED.
   
   ```
   [~PE2] display pim vpn-instance BLUE routing-table extranet receive-vpn-instance vpn-instance RED
   ```
   ```
    VPN-Instance: BLUE
    Total 1 (*, G) entry; 1 (S, G) entry
    
    Total matched 1 (*, G) entry; 1 (S, G) entry
   
    (*, 228.0.0.1)
        RP: 4.4.4.4 
        Protocol: pim-sm, Flag: WC EXTRANET 
        UpTime: 00:06:16
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:06:16
            Upstream neighbor: 10.1.2.1
            RPF prime neighbor: 10.1.2.1
        Downstream interface(s) information: none
   
        Extranet receiver(s): 1
           1: RED
    
    (10.1.1.2, 228.0.0.1)
        RP: 4.4.4.4 
        Protocol: pim-sm, Flag: SPT ACT 
        UpTime: 00:03:13
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:03:13
            Upstream neighbor: 10.1.2.1
            RPF prime neighbor: 10.1.2.1
        Downstream interface(s) information: none
   
        Extranet receiver(s): 1
           1: RED
   ```
   
   Run the **display multicast routing-table** command on PE2 to check information about the multicast routing table. The following command output shows that the upstream interface of the RPF route selected by the multicast route entry with 228.0.0.1 as the group address belongs to VPN BLUE.
   
   ```
   [~PE2] display multicast vpn-instance RED routing-table extranet source-vpn-instance vpn-instance BLUE
   ```
   ```
   Multicast routing table of VPN instance: RED
    Total 0 (*, G) entry; 1 (S, G) entry, 1 matched
    
    00001: (10.1.1.2, 228.0.0.1)
          Uptime: 05:39:09     
          Upstream Interface: MCAST_Extranet(BLUE)
          List of 1 downstream interface
              1: GigabitEthernet0/3/0
   ```
   
   Run the **display multicast rpf-info** command on PE2 to check information about the RPF route with 10.1.1.2 as the multicast source address. The following command output shows that the upstream interface of the RPF route selected by the multicast route entry with 228.0.0.1 as the group address belongs to VPN BLUE.
   
   ```
   [~PE2] display multicast vpn-instance RED rpf-info 10.1.1.2 228.0.0.1
   ```
   ```
    VPN-Instance: RED
    RPF information about source 10.1.1.2 and group 228.0.0.1
        RPF interface: MCAST_Extranet
        RPF Source VPN-Instance: BLUE
        Referenced route/mask: 10.1.1.0/24
        Referenced route type: unicast
        Route selection rule: preference-preferred
        Load splitting rule: disable
   ```
   
   After the preceding configurations are complete, the receiver can receive multicast data from the source. Run the **display pim routing-table** command on CE2 to check information about the PIM routing table. The following command output shows that multicast data has reached CE2 and has been forwarded to the receiver.
   
   ```
   [~CE2] display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 1 (*, G) entry; 1 (S, G) entry
   
    (*, 228.0.0.1)
        RP: 4.4.4.4 
        Protocol: pim-sm, Flag: WC 
        UpTime: 00:00:09     
        Upstream interface: GigabitEthernet0/1/2, Refresh time: 00:00:09
            Upstream neighbor: 10.1.3.1
            RPF prime neighbor: 10.1.3.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: static, UpTime: 00:00:09, Expires: - 
   
    (10.1.1.2, 228.0.0.1)
        RP: 4.4.4.4 
        Protocol: pim-sm, Flag: SPT ACT 
        UpTime: 00:04:06     
        Upstream interface: GigabitEthernet0/1/2, Refresh time: 00:04:06
            Upstream neighbor: 10.1.3.1
            RPF prime neighbor: 10.1.3.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:00:09, Expires: - 
   ```

#### Configuration Files

* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  multicast routing-enable
  #
  ip vpn-instance BLUE
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     rpt-spt mode
     ipmsi-tunnel
      mldp
  #
  ip vpn-instance RED
   ipv4-family
    route-distinguisher 200:1
    vpn-target 200:1 export-extcommunity
    vpn-target 200:1 import-extcommunity
    vpn-target 100:1 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     multicast extranet select-rpf vpn-instance BLUE group 228.0.0.1 24
  #
  mpls lsr-id 3.3.3.3
  #
  mpls 
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance BLUE
   ip address 10.1.2.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance RED
   ip address 10.1.3.1 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   pim sm
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance BLUE
    import-route direct
    import-route ospf 3
   #
   ipv4-family vpn-instance RED
    import-route direct
    import-route ospf 2
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  ospf 2 vpn-instance RED
   import-route bgp
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
  #
  ospf 3 vpn-instance BLUE
   import-route bgp
   area 0.0.0.0
    network 10.1.2.0 0.0.0.255
  #
  pim
  #
  pim vpn-instance BLUE
   static-rp 4.4.4.4
  #
  pim vpn-instance RED
   static-rp 4.4.4.4
  #
  return 
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   pim sm
  #
  ospf 3
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    network 4.4.4.4 0.0.0.0
  #
  pim
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
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   pim sm
   igmp enable
   igmp static-group 228.0.0.1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   pim sm
  #
  ospf 2
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 10.1.4.0 0.0.0.255
  #
  pim
   static-rp 4.4.4.4
  #
  return 
  
  ```