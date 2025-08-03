Example for Configuring Inter-AS BGP VPLS in Option B Mode
==========================================================

This solution can be used when there are only a few links between ASBRs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0187745854__fig_dc_vrp_vpls_cfg_602101), CE1 and CE2 belong to the same VPLS network and access the backbone network through PE1 in AS100 and PE2 in AS200, respectively.

In this example, inter-AS BGP VPLS in Option B mode is used because there are few links between ASBRs. The PE interface is bound to the VSI as an AC interface to implement interworking between CE1 and CE2.

**Figure 1** Configuring inter-AS BGP VPLS in option B mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, subinterface1.1, interface2, and subinterface2.1 represent GE0/2/0, GE0/2/0.1, GE0/1/0, and GE0/1/0.1, respectively.


  
![](figure/en-us_image_0195465233.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish an EBGP peer relationship between ASBRs, enable the L2VPN-AD address family, and trigger the establishment of a local IFNET tunnel.
2. Establish an MP-IBGP peer relationship between each PE and its ASBR in each AS.
3. On PE1 and PE2, configure a common BGP VPLS service and bind the corresponding AC interface to the service.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of each PE and ASBR
* IP addresses of CE interfaces connecting to PEs (no IP addresses need to be configured for PE interfaces connecting to CEs)
* RDs, VPN targets, and site IDs of VSIs on PEs
* VPN-target filtering enabled on PEs and disabled on ASBRs

#### Procedure

1. Configure interface IP addresses.
   
   
   
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
   [~CE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 10.1.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] commit
   ```
   
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
   [~PE1] interface loopback1
   ```
   ```
   [*PE1-Loopback1] ip address 1.1.1.1 32
   ```
   ```
   [*PE1-Loopback1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.10.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname ASBR1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~ASBR1] interface loopback1
   ```
   ```
   [*ASBR1-Loopback1] ip address 2.2.2.2 32
   ```
   ```
   [*ASBR1-Loopback1] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] ip address 10.10.2.2 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] ip address 10.10.1.2 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname ASBR2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~ASBR2] interface loopback1
   ```
   ```
   [*ASBR2-Loopback1] ip address 3.3.3.3 32
   ```
   ```
   [*ASBR2-Loopback1] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.10.3.3 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] ip address 10.10.2.3 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR2] commit
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
   [~PE2] interface loopback1
   ```
   ```
   [*PE2-Loopback1] ip address 4.4.4.4 32
   ```
   ```
   [*PE2-Loopback1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.10.3.4 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] commit
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
   [~CE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 10.1.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] commit
   ```
2. Configure an IGP on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255 
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
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] ospf 1
   ```
   ```
   [*ASBR1-ospf-1] area 0.0.0.0
   ```
   ```
   [*ASBR1-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*ASBR1-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   ```
   ```
   [*ASBR1-ospf-1-area-0.0.0.0] network 10.10.2.0 0.0.0.255
   ```
   ```
   [*ASBR1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*ASBR1-ospf-1] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] ospf 1
   ```
   ```
   [*ASBR2-ospf-1] area 0.0.0.0
   ```
   ```
   [*ASBR2-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*ASBR2-ospf-1-area-0.0.0.0] network 10.10.2.0 0.0.0.255
   ```
   ```
   [*ASBR2-ospf-1-area-0.0.0.0] network 10.10.3.0 0.0.0.255
   ```
   ```
   [*ASBR2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*ASBR2-ospf-1] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 4.4.4.4 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.10.3.0 0.0.0.255
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
3. Enable MPLS and establish LSPs.
   
   
   
   # Configure PE1.
   
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
   [*PE1] interface gigabitethernet 0/2/0
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
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls lsr-id 2.2.2.2
   ```
   ```
   [*ASBR1] mpls
   ```
   ```
   [*ASBR1-mpls] quit
   ```
   ```
   [*ASBR1] mpls ldp
   ```
   ```
   [*ASBR1-mpls-ldp] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] mpls lsr-id 3.3.3.3
   ```
   ```
   [*ASBR2] mpls
   ```
   ```
   [*ASBR2-mpls] quit
   ```
   ```
   [*ASBR2] mpls ldp
   ```
   ```
   [*ASBR2-mpls-ldp] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
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
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
4. Configure BGP VPLS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   ```
   [*PE1] tunnel-policy p1
   ```
   ```
   [*PE1-tunnel-policy-p1] tunnel select-seq bgp ldp load-balance-number 1
   ```
   ```
   [*PE1-tunnel-policy-p1] quit
   ```
   ```
   [*PE1] tunnel-selector s1 permit node 10
   ```
   ```
   [*PE1-tunnel-selector] apply tunnel-policy p1
   ```
   ```
   [*PE1-tunnel-selector] quit
   ```
   ```
   [*PE1] vsi v1
   ```
   ```
   [*PE1-vsi-v1] pwsignal bgp
   ```
   ```
   [*PE1-vsi-v1-bgp] route-distinguisher 10.10.1.1:1
   ```
   ```
   [*PE1-vsi-v1-bgp] vpn-target 100:1 import-extcommunity
   ```
   ```
   [*PE1-vsi-v1-bgp] vpn-target 100:1 export-extcommunity
   ```
   ```
   [*PE1-vsi-v1-bgp] site 1 range 10 default-offset 0
   ```
   ```
   [*PE1-vsi-v1-bgp] quit
   ```
   ```
   [*PE1-vsi-v1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] l2 binding vsi v1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls l2vpn
   ```
   ```
   [*ASBR1-l2vpn] quit
   ```
   ```
   [*ASBR1] tunnel-policy p1
   ```
   ```
   [*ASBR1-tunnel-policy-p1] tunnel select-seq ldp bgp load-balance-number 1
   ```
   ```
   [*ASBR1-tunnel-policy-p1] quit
   ```
   ```
   [*ASBR1] tunnel-selector s1 permit node 10
   ```
   ```
   [*ASBR1-tunnel-selector] apply tunnel-policy p1
   ```
   ```
   [*ASBR1-tunnel-selector] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] mpls l2vpn
   ```
   ```
   [*ASBR2-l2vpn] quit
   ```
   ```
   [*ASBR2] tunnel-policy p1
   ```
   ```
   [*ASBR2-tunnel-policy-p1] tunnel select-seq ldp bgp load-balance-number 1
   ```
   ```
   [*ASBR2-tunnel-policy-p1] quit
   ```
   ```
   [*ASBR2] tunnel-selector s1 permit node 10
   ```
   ```
   [*ASBR2-tunnel-selector] apply tunnel-policy p1
   ```
   ```
   [*ASBR2-tunnel-selector] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
   ```
   [*PE2] tunnel-policy p1
   ```
   ```
   [*PE2-tunnel-policy-p1] tunnel select-seq bgp ldp load-balance-number 1
   ```
   ```
   [*PE2-tunnel-policy-p1] quit
   ```
   ```
   [*PE2] tunnel-selector s1 permit node 10
   ```
   ```
   [*PE2-tunnel-selector] apply tunnel-policy p1
   ```
   ```
   [*PE2-tunnel-selector] quit
   ```
   ```
   [*PE2] vsi v1
   ```
   ```
   [*PE2-vsi-v1] pwsignal bgp
   ```
   ```
   [*PE2-vsi-v1-bgp] route-distinguisher 10.10.3.4:1
   ```
   ```
   [*PE2-vsi-v1-bgp] vpn-target 100:1 import-extcommunity
   ```
   ```
   [*PE2-vsi-v1-bgp] vpn-target 100:1 export-extcommunity
   ```
   ```
   [*PE2-vsi-v1-bgp] site 2 range 10 default-offset 0
   ```
   ```
   [*PE2-vsi-v1-bgp] quit
   ```
   ```
   [*PE2-vsi-v1]  quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] l2 binding vsi v1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
5. Configure MP-IBGP peer relationships in each AS.
   
   
   
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
   [*PE1-bgp] l2vpn-ad-family
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] policy vpn-target
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] tunnel-selector s1
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] signaling vpls
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] peer 2.2.2.2 enable
   ```
   ```
   Warning: This operation will reset the peer session. Continue? [Y/N]:y
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*ASBR1-bgp] peer 10.10.2.3 as-number 200
   ```
   ```
   [*ASBR1-bgp] peer 10.10.2.3 connect-interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR1-bgp] l2vpn-ad-family
   ```
   ```
   [*ASBR1-bgp-af-l2vpn-ad] undo policy vpn-target
   ```
   ```
   [*ASBR1-bgp-af-l2vpn-ad] tunnel-selector s1
   ```
   ```
   [*ASBR1-bgp-af-l2vpn-ad] signaling vpls
   ```
   ```
   [*ASBR1-bgp-af-l2vpn-ad] peer 1.1.1.1 enable
   ```
   ```
   Warning: This operation will reset the peer session. Continue? [Y/N]:y
   ```
   ```
   [*ASBR1-bgp-af-l2vpn-ad] peer 10.10.2.3 enable
   ```
   ```
   Warning: This operation will reset the peer session. Continue? [Y/N]:y
   ```
   ```
   [*ASBR1-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*ASBR1-bgp] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] bgp 200
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 as-number 200
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 connect-interface loopback 1
   ```
   ```
   [*ASBR2-bgp] peer 10.10.2.2 as-number 100
   ```
   ```
   [*ASBR2-bgp] peer 10.10.2.2 connect-interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR2-bgp] l2vpn-ad-family
   ```
   ```
   [*ASBR2-bgp-af-l2vpn-ad] undo policy vpn-target
   ```
   ```
   [*ASBR2-bgp-af-l2vpn-ad] tunnel-selector s1
   ```
   ```
   [*ASBR2-bgp-af-l2vpn-ad] signaling vpls
   ```
   ```
   [*ASBR2-bgp-af-l2vpn-ad] peer 4.4.4.4 enable
   ```
   ```
   Warning: This operation will reset the peer session. Continue? [Y/N]:y
   ```
   ```
   [*ASBR2-bgp-af-l2vpn-ad] peer 10.10.2.2 enable
   ```
   ```
   Warning: This operation will reset the peer session. Continue? [Y/N]:y
   ```
   ```
   [*ASBR2-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*ASBR2-bgp] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 as-number 200
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-ad-family
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] policy vpn-target
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] tunnel-selector s1
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] signaling vpls
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] peer 3.3.3.3 enable
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the [**display bgp l2vpn-ad peer**](cmdqueryname=display+bgp+l2vpn-ad+peer) command on each PE or ASBR. The command output shows that the MP-IBGP peer relationship status is **Established**.
   
   The following example uses the command output on ASBR2.
   
   ```
   [~ASBR2] display bgp l2vpn-ad peer
   ```
   ```
    BGP local router ID : 3.3.3.3                                                  
    Local AS number : 200                                                          
    Total number of peers : 2                  Peers in established state : 2      
     Peer            V         AS       MsgRcvd  MsgSent  OutQ  Up/Down       State          PrefRcv    
     4.4.4.4         4         200      8        8        0     00:02:32      Established    1                      
     10.10.2.2       4         100      189      187      0     02:39:53      Established    1 
   ```
6. Configure CEs to permit packets from VLAN 10.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface gigabitethernet0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] commit
   ```
7. Verify the configuration.
   
   
   
   Run the **display vpls connection bgp verbose** command on PEs to check VSI information. The command output shows that **VC State** is **up**.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display vpls connection bgp verbose
   ```
   ```
   VSI Name: v1                               Signaling: bgp                       
     **Remote Site ID     : 2                                                      
       VC State           : up                                                     
       RD                 : 10.10.3.4:1                                            
       Encapsulation      : bgp vpls                                               
       MTU                : 1500                                                   
       Peer Ip Address    : 2.2.2.2                                                
       PW Type            : label                                                  
       Local VC Label     : 368642                                                 
       Remote VC Label    : 368649                                                 
       Tunnel Policy      : --                                                     
       Tunnel ID          : 0x0000000001004c4b42                                   
       Remote Label Block : 368648/8/0                                             
       Export vpn target  : 100:1   
   ```
   
   CE1 and CE2 can ping each other.
   
   ```
   [~CE1] ping 10.1.1.2
   ```
   ```
      PING 10.10.1.2: 56  data bytes, press CTRL_C to break                         
       Reply from 10.10.1.2: bytes=56 Sequence=1 ttl=255 time=149 ms               
       Reply from 10.10.1.2: bytes=56 Sequence=2 ttl=255 time=4 ms                 
       Reply from 10.10.1.2: bytes=56 Sequence=3 ttl=255 time=4 ms                 
       Reply from 10.10.1.2: bytes=56 Sequence=4 ttl=255 time=4 ms                 
       Reply from 10.10.1.2: bytes=56 Sequence=5 ttl=255 time=4 ms                 
   
     --- 10.10.1.2 ping statistics ---                                             
       5 packet(s) transmitted                                                     
       5 packet(s) received                                                        
       0.00% packet loss                                                           
       round-trip min/avg/max = 4/33/149 ms                                        
   
   ```
   
   Run the **display vsi name v1** **verbose** command on a PE or ASBR to view information about the VPLS instance of a specified VSI. The following example uses the command output on PE1.
   
   ```
   [~PE1] display vsi name v1 verbose
   ```
   ```
    ***VSI Name               : v1
       Work Mode              : normal 
       Administrator VSI      : no 
       Isolate Spoken         : disable 
       VSI Index              : 1 
       PW Signaling           : bgp 
       Member Discovery Style : -- 
       Bridge-domain Mode     : disable 
       PW MAC Learn Style     : unqualify 
       Encapsulation Type     : vlan 
       MTU                    : 1500 
       Diffserv Mode          : uniform 
       Service Class          : -- 
       Color                  : -- 
       DomainId               : 255 
       Domain Name            :  
       Ignore AcState         : disable 
       P2P VSI                : disable 
       Multicast Fast Switch  : disable 
       Create Time            : 0 days, 9 hours, 8 minutes, 35 seconds 
       VSI State              : up 
       Resource Status        : -- 
   
       BGP RD                 : 10.10.1.1:1 
       SiteID/Range/Offset    : 1/10/0 
       Import vpn target      : 100:1                   
       Export vpn target      : 100:1                   
       Remote Label Block     : 368648/8/0  
       Local Label Block      : 0/368640/8/0  
   
       Interface Name         : GigabitEthernet0/2/0.1 
       State                  : up 
       Ac Block State         : unblocked 
       Access Port            : false 
       Last Up Time           : 2019/08/26 03:56:35 
       Total Up Time          : 0 days, 8 hours, 51 minutes, 8 seconds 
       Interface Name         : GigabitEthernet0/1/0.1 
       State                  : up 
       Ac Block State         : unblocked 
       Access Port            : false 
       Last Up Time           : 2019/08/26 12:07:53 
       Total Up Time          : 0 days, 0 hours, 39 minutes, 50 seconds 
   
     **PW Information: 
   
      *Peer Ip Address        : 2.2.2.2
       PW State               : up 
       Local VC Label         : 368642 
       Remote VC Label        : 368649 
       Remote Control Word    : disable 
       Negotiated Control Word: disable 
       PW Type                : label 
       Tunnel ID              : 0x0000000001004c4b42  
       Broadcast Tunnel ID    : -- 
       Broad BackupTunnel ID  : -- 
       Ckey                   : 1 
       Nkey                   : 16777327 
       Main PW Token          : 0x0 
       Slave PW Token         : 0x0 
       Tnl Type               : ldp 
       OutInterface           : -- 
       Backup OutInterface    : -- 
       Stp Enable             : 0 
       Mac Flapping           : 0 
       Monitor Group Name     : -- 
       PW Last Up Time        : 2019/08/26 06:06:19 
       PW Total Up Time       : 0 days, 6 hours, 41 minutes, 25 seconds
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   ip address 10.1.1.1 255.255.255.0
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  router id 1.1.1.1
  #
  tunnel-selector s1 permit node 10
   apply tunnel-policy p1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi v1
   pwsignal bgp
    route-distinguisher 10.10.1.1:1
    vpn-target 100:1 import-extcommunity
    vpn-target 100:1 export-extcommunity
    site 1 range 10 default-offset 0
  #
  mpls ldp
  #
   ipv4-family
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi v1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   l2vpn-ad-family
    policy vpn-target
    tunnel-selector s1  
    signaling vpls
    peer 2.2.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.10.1.0 0.0.0.255
  #
  route-policy p1 permit node 10
   apply mpls-label
  #
  tunnel-policy p1
   tunnel select-seq bgp ldp load-balance-number 1
  #
  return
  
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  router id 2.2.2.2
  #
  tunnel-selector s1 permit node 10
   apply tunnel-policy p1
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.2.2 255.255.255.0
   mpls
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 10.10.2.3 as-number 200
   peer 10.10.2.3 connect-interface GigabitEthernet0/1/0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 10.10.2.3 enable
   #
   l2vpn-ad-family
    undo policy vpn-target
    tunnel-selector s1  
    signaling vpls
    peer 1.1.1.1 enable
    peer 10.10.2.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.10.1.0 0.0.0.255
    network 10.10.2.0 0.0.0.255
  #
  tunnel-policy p1
   tunnel select-seq ldp bgp load-balance-number 1
  #
  return
  
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  router id 3.3.3.3
  #
  tunnel-selector s1 permit node 10
   apply tunnel-policy p1
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.2.3 255.255.255.0
   mpls
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.10.3.3 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 200
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack1
   peer 10.10.2.2 as-number 100
   peer 10.10.2.2 connect-interface GigabitEthernet0/1/0
   #
   l2vpn-ad-family
    undo policy vpn-target
    tunnel-selector s1  
    signaling vpls
    peer 4.4.4.4 enable
    peer 10.10.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.10.2.0 0.0.0.255
    network 10.10.3.0 0.0.0.255
  #
  tunnel-policy p1
   tunnel select-seq ldp bgp load-balance-number 1
  #
  return
  
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  router id 4.4.4.4
  #
  tunnel-selector s1 permit node 10
   apply tunnel-policy p1
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls l2vpn
  #
  vsi v1
   pwsignal bgp
    route-distinguisher 10.10.3.4:1
    vpn-target 100:1 import-extcommunity
    vpn-target 100:1 export-extcommunity
    site 2 range 10 default-offset 0
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi v1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.10.3.4 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 200
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack1
   #
   l2vpn-ad-family
    policy vpn-target
    tunnel-selector s1  
    signaling vpls
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.10.3.0 0.0.0.255
  tunnel-policy p1
   tunnel select-seq bgp ldp load-balance-number 1
  #
  return
  
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```