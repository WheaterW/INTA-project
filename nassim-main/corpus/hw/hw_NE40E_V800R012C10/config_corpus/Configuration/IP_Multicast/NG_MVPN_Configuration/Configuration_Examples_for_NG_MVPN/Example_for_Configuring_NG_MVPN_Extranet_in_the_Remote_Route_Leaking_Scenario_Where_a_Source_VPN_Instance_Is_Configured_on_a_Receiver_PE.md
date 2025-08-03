Example for Configuring NG MVPN Extranet in the Remote Route Leaking Scenario Where a Source VPN Instance Is Configured on a Receiver PE
========================================================================================================================================

This section provides an example for configuring NG MVPN extranet in the remote route leaking scenario where a source VPN instance is configured on a receiver PE.

#### Networking Requirements

In NG MVPN applications, a service provider in a VPN may need to provide multicast services for users in other VPNs. Therefore, multicast services need to be distributed across VPNs.

In the remote route leaking scenario of single-AS NG MVPN shown in [Figure 1](#EN-US_TASK_0000001270433341__fig_dc_vrp_cfg_ngmvpn_012101), the receiver in VPN RED requires multicast data from the source in VPN BLUE. To meet this requirement, deploy NG MVPN extranet by configuring the source VPN on the receiver PE. In addition, configure a multicast routing policy for VPN RED on receiver PE2 and specify in the policy that the upstream interface of the RPF route belongs to VPN BLUE.

**Figure 1** Configuring NG MVPN extranet in the remote route leaking scenario where a source VPN instance is configured on a receiver PE![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0000001270193753.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic single-AS NG MVPN functions.
2. Configure VPN BLUE with the IPv4 address family enabled on PE2.
3. Configure a private network RP to serve the NG MVPN extranet.
4. Configure a multicast routing policy for VPN RED on PE2 and specify in the policy that the upstream interface of the RPF route belongs to VPN BLUE.

#### Data Preparation

To complete the configuration, you need the following data:

* RD and VPN target of VPN BLUE: 100:1; VPN target of MVPN routes: 1:1
* RD of VPN RED: 200:1; VPN targets of VPN RED: 2:1 and 100:1

#### Procedure

1. Configure basic single-AS NG MVPN functions.
   1. Configure basic MPLS functions and enable MPLS LDP to establish LDP LSPs on the public network.
      
      
      
      # Configure PE1.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname PE1
      ```
      ```
      [*HUAWEI] commit
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
      [*PE1-mpls-ldp] mldp p2mp
      ```
      ```
      [*PE1-mpls-ldp] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/0
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
      
      # Configure the P.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname P
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~P] mpls lsr-id 2.2.2.2
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
      [*P-mpls-ldp] mldp p2mp
      ```
      ```
      [*P-mpls-ldp] quit
      ```
      ```
      [*P] interface gigabitethernet 0/1/0
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
      [*P] interface gigabitethernet 0/1/1
      ```
      ```
      [*P-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*P-GigabitEthernet0/1/1] mpls ldp
      ```
      ```
      [*P-GigabitEthernet0/1/1] quit
      ```
      ```
      [*P] commit
      ```
      
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
      [*PE2-mpls-ldp] mldp p2mp
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
   2. Configure a unicast routing protocol on the public network to ensure that multicast routes on the public network are reachable.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] ospf 1
      ```
      ```
      [*PE1-ospf-1] area 0
      ```
      ```
      [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
      ```
      ```
      [*PE1-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
      ```
      ```
      [*PE1-ospf-1-area-0.0.0.0] quit
      ```
      ```
      [*PE1-ospf-1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure the P.
      
      ```
      [~P] ospf 1
      ```
      ```
      [*P-ospf-1] area 0
      ```
      ```
      [*P-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
      ```
      ```
      [*P-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
      ```
      ```
      [*P-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
      ```
      ```
      [*P-ospf-1-area-0.0.0.0] quit
      ```
      ```
      [*P-ospf-1] quit
      ```
      ```
      [*P] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] ospf 1
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
   3. Configure a VPN instance on each PE and bind the interface that connects a PE to a CE to the VPN instance on that PE.
      
      
      
      # On PE1, create VPN BLUE, enable multicast globally and the IPv4 address family for VPN BLUE, and perform configurations for I-PMSI and S-PMSI tunnels. Bind GE 0/2/0 connecting PE1 to CE1 to VPN BLUE.
      
      ```
      [~PE1] multicast routing-enable
      ```
      ```
      [*PE1] ip vpn-instance BLUE
      ```
      ```
      [*PE1-vpn-instance-BLUE] ipv4-family
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4] route-distinguisher 100:1
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4] vpn-target 100:1 both
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4] multicast routing-enable
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4] mvpn
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] vpn-target 1:1 both
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] sender-enable
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] c-multicast signaling bgp
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] rpt-spt mode
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] ipmsi-tunnel
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn-ipmsi] mldp
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn-ipmsi] quit
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] spmsi-tunnel
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn-spmsi] group 228.0.0.0 255.255.255.0 mldp limit 1
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn-spmsi] quit
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] quit
      ```
      ```
      [*PE1-vpn-instance-BLUE-af-ipv4] quit
      ```
      ```
      [*PE1-vpn-instance-BLUE] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] ip binding vpn-instance BLUE
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] ip address 10.1.2.2 24
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
      
      # On PE2, create VPN BLUE and VPN RED, enable multicast globally and the IPv4 address family for VPN BLUE and VPN RED, and set relevant parameters. Bind GE 0/1/0 connecting PE2 to CE2 to VPN RED.
      
      ```
      [~PE2] multicast routing-enable
      ```
      ```
      [*PE2] ip vpn-instance BLUE
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
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn] vpn-target 1:1 both
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn] c-multicast signaling bgp
      ```
      ```
      [*PE2-vpn-instance-BLUE-af-ipv4-mvpn] rpt-spt mode
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
      [*PE2] ip vpn-instance RED
      ```
      ```
      [*PE2-vpn-instance-RED] ipv4-family
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4] route-distinguisher 200:1
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4] vpn-target 2:1 both
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
      [*PE2-vpn-instance-RED-af-ipv4-mvpn] quit
      ```
      ```
      [*PE2-vpn-instance-RED-af-ipv4] quit
      ```
      ```
      [*PE2-vpn-instance-RED] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/0
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] ip binding vpn-instance RED
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] ip address 10.1.3.1 24
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
      [~CE1] multicast routing-enable
      ```
      ```
      [*CE1] interface gigabitethernet 0/1/0
      ```
      ```
      [*CE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
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
      [*CE1-GigabitEthernet0/1/1] ip address 10.1.2.1 24
      ```
      ```
      [*CE1-GigabitEthernet0/1/1] pim sm
      ```
      ```
      [*CE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*CE1] ospf 2
      ```
      ```
      [*CE1-ospf-2] area 0
      ```
      ```
      [*CE1-ospf-2-area-0.0.0.0] network 10.1.1.0 0.0.0.255
      ```
      ```
      [*CE1-ospf-2-area-0.0.0.0] network 10.1.2.0 0.0.0.255
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
      [~CE2] interface gigabitethernet 0/1/0
      ```
      ```
      [*CE2-GigabitEthernet0/1/0] ip address 10.1.3.2 24
      ```
      ```
      [*CE2-GigabitEthernet0/1/0] pim sm
      ```
      ```
      [*CE2-GigabitEthernet0/1/0] quit
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
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] bgp 100
      ```
      ```
      [*PE1-bgp] peer 3.3.3.3 as-number 100
      ```
      ```
      [*PE1-bgp] peer 3.3.3.3 connect-interface LoopBack 1
      ```
      ```
      [*PE1-bgp] ipv4-family vpn-instance BLUE
      ```
      ```
      [*PE1-bgp-BLUE] import-route ospf 2
      ```
      ```
      [*PE1-bgp-BLUE] import-route direct
      ```
      ```
      [*PE1-bgp-BLUE] quit
      ```
      ```
      [*PE1-bgp] ipv4-family vpnv4
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
      [*PE1] ospf 2 vpn-instance BLUE
      ```
      ```
      [*PE1-ospf-2] import-route bgp
      ```
      ```
      [*PE1-ospf-2] area 0
      ```
      ```
      [*PE1-ospf-2-area-0.0.0.0] network 10.1.2.0 0.0.0.255
      ```
      ```
      [*PE1-ospf-2-area-0.0.0.0] quit
      ```
      ```
      [*PE1-ospf-2] quit
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
      [*PE2-bgp] peer 1.1.1.1 connect-interface LoopBack 1
      ```
      ```
      [*PE2-bgp] ipv4-family vpn-instance BLUE
      ```
      ```
      [*PE2-bgp-BLUE] import-route ospf 2
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
      [*PE2-ospf-3] import-route bgp
      ```
      ```
      [*PE2-ospf-2] area 0
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
      [*PE2] commit
      ```
2. Configure a private network RP to serve the NG MVPN extranet.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] pim
   ```
   ```
   [*CE1-pim] static-rp 10.1.1.1
   ```
   ```
   [*CE1-pim] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] pim vpn-instance BLUE
   ```
   ```
   [*PE1-pim-BLUE] static-rp 10.1.1.1
   ```
   ```
   [*PE1-pim-BLUE] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] pim vpn-instance BLUE
   ```
   ```
   [*PE2-pim-BLUE] static-rp 10.1.1.1
   ```
   ```
   [*PE2-pim-BLUE] quit
   ```
   ```
   [*PE2] commit
   ```
   ```
   [~PE2] pim vpn-instance RED
   ```
   ```
   [*PE2-pim-RED] static-rp 10.1.1.1
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
   [*CE2-pim] static-rp 10.1.1.1
   ```
   ```
   [*CE2-pim] quit
   ```
   ```
   [*CE2] commit
   ```
3. Configure a multicast routing policy for VPN RED to specify VPN BLUE for the upstream interface of the RPF route selected by the PIM entry with the group address 228.0.0.0/24.
   
   
   ```
   [~PE2] ip vpn-instance RED
   ```
   ```
   [*PE2-vpn-instance-RED] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-RED-af-ipv4] mvpn
   ```
   ```
   [*PE2-vpn-instance-RED-af-ipv4-mvpn] multicast extranet select-rpf vpn-instance BLUE group 228.0.0.0 24
   ```
   ```
   [*PE2-vpn-instance-RED-af-ipv4-mvpn] quit
   ```
   ```
   [*PE2-vpn-instance-RED-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-RED] quit
   ```
   ```
   [*PE2] commit
   ```
4. Verify the configuration.
   
   
   
   By checking the configuration, you can view that the receiver in VPN RED can receive multicast data from the source in VPN BLUE.
   
   Run the **display pim routing-table** command on PE2 to check information about the PIM routing table. The following command output shows that the upstream interface of the RPF route selected by the PIM entry with 228.0.0.1 as the group address belongs to VPN BLUE.
   
   ```
   [~PE2] display pim vpn-instance RED routing-table extranet source-vpn-instance vpn-instance BLUE
   ```
   ```
    VPN-Instance: RED
    Total 1 (*, G) entry; 2 (S, G) entries
    
    Total matched 1 (*, G) entry; 1 (S, G) entry
   
    (*, 228.0.0.1)
        RP: 10.1.4.1 
        Protocol: pim-sm, Flag: WC 
        UpTime: 00:47:55
        Upstream interface: MCAST_Extranet(BLUE), Refresh time: 00:47:55
            Upstream neighbor: 1.1.1.1
            RPF prime neighbor: 1.1.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/0
                Protocol: pim-sm, UpTime: 00:47:55, Expires: 00:02:34
    
    (10.1.1.15, 228.0.0.1)
        RP: 10.1.4.1 
        Protocol: pim-sm, Flag: SPT ACT 
        UpTime: 06:18:43
        Upstream interface: MCAST_Extranet(BLUE), Refresh time: 06:18:43
            Upstream neighbor: 1.1.1.1
            RPF prime neighbor: 1.1.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/0
                Protocol: pim-sm, UpTime: 00:47:57, Expires: 00:02:32
   ```
   
   Run the **display multicast routing-table** command on PE2 to check information about the multicast routing table. The following command output shows that the upstream interface of the RPF route selected by the multicast route entry with 228.0.0.1 as the group address belongs to VPN BLUE.
   
   ```
   [~PE2] display multicast vpn-instance RED routing-table extranet source-vpn-instance vpn-instance BLUE
   ```
   ```
   Multicast routing table of VPN instance: RED
    Total 0 (*, G) entry; 1 (S, G) entry, 1 matched
    
    00001: (10.1.1.15, 228.0.0.1)
          Uptime: 00:42:23     
          Upstream Interface: MCAST_Extranet(BLUE)
          List of 1 downstream interface
              1: GigabitEthernet0/1/0
   ```
   
   Run the **display multicast rpf-info** command on PE2 to check information about the RPF route with 10.1.1.2 as the multicast source address. The following command output shows that the upstream interface of the RPF route selected by the multicast route entry with 228.0.0.1 as the group address belongs to VPN BLUE.
   
   ```
   [~PE2] display multicast vpn-instance RED rpf-info 10.1.1.2 228.0.0.1
   ```
   ```
    VPN-Instance: RED
    RPF information about source 10.1.1.15 and group 228.0.0.1
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
        RP: 10.1.4.1 
        Protocol: pim-sm, Flag: WC 
        UpTime: 00:53:02     
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:53:02
            Upstream neighbor: 10.1.3.1
            RPF prime neighbor: 10.1.3.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: static, UpTime: 00:53:02, Expires: - 
   
    (10.1.1.15, 228.0.0.1)
        RP: 10.1.4.1 
        Protocol: pim-sm, Flag: SPT ACT 
        UpTime: 00:08:02     
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:08:02
            Upstream neighbor: 10.1.3.1
            RPF prime neighbor: 10.1.3.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:08:02, Expires: - 
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  multicast mvpn 1.1.1.1
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
     vpn-target 1:1 export-extcommunity
     vpn-target 1:1 import-extcommunity
     ipmsi-tunnel
      mldp
     spmsi-tunnel
      group 228.0.0.0 255.255.255.0 mldp limit 1
  #
  mpls lsr-id 1.1.1.1
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance BLUE
   ip address 10.1.2.2 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.3 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance BLUE
    import-route direct
    import-route ospf 2
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  ospf 2 vpn-instance BLUE
   import-route bgp
   area 0.0.0.0
    network 10.1.2.2 0.0.0.255
  #
  pim vpn-instance BLUE
   static-rp 10.1.1.1
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
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
     c-multicast signaling bgp
     rpt-spt mode
     vpn-target 1:1 export-extcommunity
     vpn-target 1:1 import-extcommunity
  #
  ip vpn-instance RED
   ipv4-family
    route-distinguisher 200:1
    vpn-target 2:1 export-extcommunity
    vpn-target 2:1 import-extcommunity
    vpn-target 100:1 import-extcommunity
    multicast routing-enable
    mvpn
     multicast extranet select-rpf vpn-instance BLUE group 228.0.0.0 255.255.255.0
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
   ip binding vpn-instance RED
   ip address 10.1.3.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
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
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance BLUE
    import-route direct
    import-route ospf 2
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
  pim
  #
  pim vpn-instance RED
   static-rp 10.1.1.1
  #
  pim vpn-instance BLUE
   static-rp 10.1.1.1
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
   ip address 10.1.1.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   pim sm
  #
  ospf 2
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
  #
  pim
   static-rp 10.1.1.1
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
   ip address 10.1.3.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   pim sm
   igmp enable
   igmp static-group 228.0.0.1 source 10.1.1.15
   #
  ospf 2
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 10.1.4.0 0.0.0.255
  #
  pim
   static-rp 10.1.1.1
  #
  return 
  
  ```