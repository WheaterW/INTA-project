Example for Configuring BGP VPWS FRR (Symmetric Access of CEs to PEs)
=====================================================================

In a BGP VPWS FRR scenario where two CEs are symmetrically dual-homed to PEs, the two CEs can communicate over a pair of primary and secondary VPWS connections.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369957__fig_dc_vrp_vpws_cfg_607001), CE1 is dual-homed to PE1 and PE2, and CE2 is dual-homed to PE3 and PE4. A primary BGP VPWS connection needs to be established between PE1 and PE3, and a secondary BGP VPWS connection needs to be established between PE2 and PE4, so that when the primary path CE1 <-> PE1 <-> PE3 <-> CE2 fails, VPWS traffic can be quickly switched to the backup path CE1 <-> PE2 <-> PE4 <-> CE2.

**Figure 1** Configuring BGP VPWS FRR â symmetric access of CEs to PEs![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1, sub-interface1.1, and interface2 represent GE0/1/0, GE0/1/0.1, and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_vpws_cfg_607001.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on the PEs of the backbone network to ensure IP connectivity and configure basic MPLS functions and LDP.
2. Configure devices to exchange VPWS information as BGP peers.
3. Enable MPLS L2VPN on PEs and create a remote BGP VPWS connection between PE1 and PE3 and between PE2 and PE4.
4. Configure AC OAM detection and notification and enable OAM mapping on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* BGP AS number
* Names of MPLS-L2VPN instances on PEs
* RDs and VPN targets of MPLS-L2VPN instances on PEs
* CE names and IDs on PEs

#### Procedure

1. Configure IP addresses.
   
   
   
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
   [~CE1] vlan 10
   ```
   ```
   [*CE1-vlan10] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] port trunk allow-pass vlan 10
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*CE1] interface vlanif 10
   ```
   ```
   [*CE1-Vlanif10] ip address 10.1.1.1 24
   ```
   ```
   [*CE1-Vlanif10] quit
   ```
   ```
   [*CE1] cfm enable
   ```
   ```
   [*CE1] cfm md md1
   ```
   ```
   [*CE1-md-md1] ma ma1
   ```
   ```
   [*CE1-md-md1-ma-ma1] map vlan 10
   ```
   ```
   [*CE1-md-md1-ma-ma1] mep mep-id 2 interface GigabitEthernet0/1/0 outward
   ```
   ```
   [*CE1-md-md1-ma-ma1] mep ccm-send mep-id 2 enable
   ```
   ```
   [*CE1-md-md1-ma-ma1] remote-mep mep-id 1
   ```
   ```
   [*CE1-md-md1-ma-ma1] remote-mep ccm-receive mep-id 1 enable
   ```
   ```
   [*CE1-md-md1-ma-ma1] quit
   ```
   ```
   [*CE1-md-md1] quit
   ```
   ```
   [*CE1] cfm md md2
   ```
   ```
   [*CE1-md-md2] ma ma2
   ```
   ```
   [*CE1-md-md2-ma-ma2] map vlan 10
   ```
   ```
   [*CE1-md-md2-ma-ma2] mep mep-id 4 interface gigabitethernet0/2/0 outward
   ```
   ```
   [*CE1-md-md2-ma-ma2] mep ccm-send mep-id 4 enable
   ```
   ```
   [*CE1-md-md2-ma-ma2] remote-mep mep-id 3
   ```
   ```
   [*CE1-md-md2-ma-ma2] remote-mep ccm-receive mep-id 3 enable
   ```
   ```
   [*CE1-md-md2-ma-ma2] quit
   ```
   ```
   [*CE1-md-md2] quit
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
   [~CE2] vlan 10
   ```
   ```
   [*CE2-vlan10] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*CE2-GigabitEthernet0/2/0] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/2/0] port trunk allow-pass vlan 10
   ```
   ```
   [*CE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*CE2] interface vlanif 10
   ```
   ```
   [*CE2-Vlanif10] ip address 10.1.1.2 24
   ```
   ```
   [*CE2-Vlanif10] quit
   ```
   ```
   [*CE2] cfm enable
   ```
   ```
   [*CE2] cfm md md1
   ```
   ```
   [*CE2-md-md1] ma ma1
   ```
   ```
   [*CE2-md-md1-ma-ma1] map vlan 10
   ```
   ```
   [*CE2-md-md1-ma-ma1] mep mep-id 2 interface GigabitEthernet0/1/0 outward
   ```
   ```
   [*CE2-md-md1-ma-ma1] mep ccm-send mep-id 2 enable
   ```
   ```
   [*CE2-md-md1-ma-ma1] remote-mep mep-id 1
   ```
   ```
   [*CE2-md-md1-ma-ma1] remote-mep ccm-receive mep-id 1 enable
   ```
   ```
   [*CE2-md-md1-ma-ma1] quit
   ```
   ```
   [*CE2-md-md1] quit
   ```
   ```
   [*CE2] cfm md md2
   ```
   ```
   [*CE2-md-md2] ma ma2
   ```
   ```
   [*CE2-md-md2-ma-ma2] map vlan 10
   ```
   ```
   [*CE2-md-md2-ma-ma2] mep mep-id 4 interface GigabitEthernet0/1/0 outward
   ```
   ```
   [*CE2-md-md2-ma-ma2] mep ccm-send mep-id 4 enable
   ```
   ```
   [*CE2-md-md2-ma-ma2] remote-mep mep-id 3
   ```
   ```
   [*CE2-md-md2-ma-ma2] remote-mep ccm-receive mep-id 3 enable
   ```
   ```
   [*CE2-md-md2-ma-ma2] quit
   ```
   ```
   [*CE2-md-md2] quit
   ```
   ```
   [*CE2] commit
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
   [~PE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] ip address 1.1.1.9 32
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 192.168.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
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
   [~PE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] ip address 2.2.2.9 32
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 192.168.10.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE3
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE3] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE3] interface loopback 1
   ```
   ```
   [*PE3-LoopBack1] ip address 3.3.3.9 24
   ```
   ```
   [*PE3-LoopBack1] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ip address 192.168.1.2 24
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE4
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE4] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE4-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE4-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE4] interface loopback 1
   ```
   ```
   [*PE4-LoopBack1] ip address 4.4.4.9 24
   ```
   ```
   [*PE4-LoopBack1] quit
   ```
   ```
   [*PE4] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE4-GigabitEthernet0/2/0] ip address 192.168.10.2 24
   ```
   ```
   [*PE4-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE4] commit
   ```
2. Configure IGP. In this example, OSPF is used.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] area 0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.9 0.0.0.0
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
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 2.2.2.9 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 192.168.10.0 0.0.0.255
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
   
   # Configure PE3.
   
   ```
   [~PE3] ospf 1
   ```
   ```
   [*PE3-ospf-1] area 0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 3.3.3.9 0.0.0.0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE3-ospf-1] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   [~PE4] ospf 1
   ```
   ```
   [*PE4-ospf-1] area 0
   ```
   ```
   [*PE4-ospf-1-area-0.0.0.0] network 4.4.4.9 0.0.0.0
   ```
   ```
   [*PE4-ospf-1-area-0.0.0.0] network 192.168.10.0 0.0.0.255
   ```
   ```
   [*PE4-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE4-ospf-1] quit
   ```
   ```
   [*PE4] commit
   ```
3. Configure basic MPLS functions and establish LSPs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.9
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
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 2.2.2.9
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
   
   # Configure PE3.
   
   ```
   [~PE3] mpls lsr-id 3.3.3.9
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
   [*PE3] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   [~PE4] mpls lsr-id 4.4.4.9
   ```
   ```
   [*PE4] mpls
   ```
   ```
   [*PE4-mpls] quit
   ```
   ```
   [*PE4] mpls ldp
   ```
   ```
   [*PE4-mpls-ldp] quit
   ```
   ```
   [*PE4] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE4-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE4-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE4-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE4] commit
   ```
4. Configure devices to exchange VPWS information as BGP peers.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.9 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.9 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-ad-family
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] peer 3.3.3.9 enable
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] peer 3.3.3.9 signaling vpws
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
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] peer 1.1.1.9 as-number 100
   ```
   ```
   [*PE3-bgp] peer 1.1.1.9 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] l2vpn-ad-family
   ```
   ```
   [*PE3-bgp-af-l2vpn-ad] peer 1.1.1.9 enable
   ```
   ```
   [*PE3-bgp-af-l2vpn-ad] peer 1.1.1.9 signaling vpws
   ```
   ```
   [*PE3-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 4.4.4.9 as-number 100
   ```
   ```
   [*PE2-bgp] peer 4.4.4.9 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-ad-family
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] peer 4.4.4.9 enable
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] peer 4.4.4.9 signaling vpws
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
   
   # Configure PE4.
   
   ```
   [~PE4] bgp 100
   ```
   ```
   [*PE4-bgp] peer 2.2.2.9 as-number 100
   ```
   ```
   [*PE4-bgp] peer 2.2.2.9 connect-interface loopback 1
   ```
   ```
   [*PE4-bgp] l2vpn-ad-family
   ```
   ```
   [*PE4-bgp-af-l2vpn-ad] peer 2.2.2.9 enable
   ```
   ```
   [*PE4-bgp-af-l2vpn-ad] peer 2.2.2.9 signaling vpws
   ```
   ```
   [*PE4-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*PE4-bgp] quit
   ```
   ```
   [*PE4] commit
   ```
5. Configure remote BGP VPWS connections.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   ```
   [*PE1] mpls l2vpn vpn1 encapsulation vlan control-word
   ```
   ```
   [*PE1-mpls-l2vpn-vpn1] route-distinguisher 100:1
   ```
   ```
   [*PE1-mpls-l2vpn-vpn1] vpn-target 200:1 both
   ```
   ```
   [*PE1-mpls-l2vpn-vpn1] ce ce1 id 1 range 10
   ```
   ```
   [*PE1-mpls-l2vpn-vpn1-ce-ce1] connection ce-offset 3 interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE1-mpls-l2vpn-vpn1-ce-ce1] quit
   ```
   ```
   [*PE1-mpls-l2vpn-vpn1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
   ```
   [*PE2] mpls l2vpn vpn1 encapsulation vlan control-word
   ```
   ```
   [*PE2-mpls-l2vpn-vpn1] route-distinguisher 100:1
   ```
   ```
   [*PE2-mpls-l2vpn-vpn1] vpn-target 200:1 both
   ```
   ```
   [*PE2-mpls-l2vpn-vpn1] ce ce2 id 2 range 10
   ```
   ```
   [*PE2-mpls-l2vpn-vpn1-ce-ce2] connection ce-offset 4 interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE2-mpls-l2vpn-vpn1-ce-ce2] quit
   ```
   ```
   [*PE2-mpls-l2vpn-vpn1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls l2vpn
   ```
   ```
   [*PE3-l2vpn] quit
   ```
   ```
   [*PE3] mpls l2vpn vpn1 encapsulation vlan control-word
   ```
   ```
   [*PE3-mpls-l2vpn-vpn1] route-distinguisher 100:1
   ```
   ```
   [*PE3-mpls-l2vpn-vpn1] vpn-target 200:1 both
   ```
   ```
   [*PE3-mpls-l2vpn-vpn1] ce ce3 id 3 range 10
   ```
   ```
   [*PE3-mpls-l2vpn-vpn1-ce-ce3] connection ce-offset 1 interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE3-mpls-l2vpn-vpn1-ce-ce3] quit
   ```
   ```
   [*PE3-mpls-l2vpn-vpn1] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   [~PE4] mpls l2vpn
   ```
   ```
   [*PE4-l2vpn] quit
   ```
   ```
   [*PE4] mpls l2vpn vpn1 encapsulation vlan control-word
   ```
   ```
   [*PE4-mpls-l2vpn-vpn1] route-distinguisher 100:1
   ```
   ```
   [*PE4-mpls-l2vpn-vpn1] vpn-target 200:1 both
   ```
   ```
   [*PE4-mpls-l2vpn-vpn1] ce ce4 id 4 range 10
   ```
   ```
   [*PE4-mpls-l2vpn-vpn1-ce-ce4] connection ce-offset 2 interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE4-mpls-l2vpn-vpn1-ce-ce4] quit
   ```
   ```
   [*PE4-mpls-l2vpn-vpn1] quit
   ```
   ```
   [*PE4] commit
   ```
6. Configure BFD for PW.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
   ```
   ```
   [*PE1] bfd 1to3 bind pw interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE1-bfd-lsp-session-1to3] discriminator local 13
   ```
   ```
   [*PE1-bfd-lsp-session-1to3] discriminator remote 31
   ```
   ```
   [*PE1-bfd-lsp-session-1to3] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bfd
   ```
   ```
   [*PE3-bfd] quit
   ```
   ```
   [*PE3] bfd 3to1 bind pw interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE3-bfd-lsp-session-3to1] discriminator local 31
   ```
   ```
   [*PE3-bfd-lsp-session-3to1] discriminator remote 13
   ```
   ```
   [*PE3-bfd-lsp-session-3to1] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] quit
   ```
   ```
   [*PE2] bfd 2to4 bind pw interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE2-bfd-lsp-session-2to4] discriminator local 24
   ```
   ```
   [*PE2-bfd-lsp-session-2to4] discriminator remote 42
   ```
   ```
   [*PE2-bfd-lsp-session-2to4] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE4.
   
   ```
   [~PE4] bfd
   ```
   ```
   [*PE4-bfd] quit
   ```
   ```
   [*PE4] bfd 4to2 bind pw interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE4-bfd-lsp-session-4to2] discriminator local 42
   ```
   ```
   [*PE4-bfd-lsp-session-4to2] discriminator remote 24
   ```
   ```
   [*PE4-bfd-lsp-session-4to2] quit
   ```
   ```
   [*PE4] commit
   ```
7. Configure OAM mapping.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] cfm enable
   ```
   ```
   [*PE1] cfm md md1
   ```
   ```
   [*PE1-md-md1] ma ma1
   ```
   ```
   [*PE1-md-md1-ma-ma1] map vlan 10
   ```
   ```
   [*PE1-md-md1-ma-ma1] mep mep-id 1 interface GigabitEthernet0/1/0.1 outward
   ```
   ```
   [*PE1-md-md1-ma-ma1] mep ccm-send mep-id 1 enable
   ```
   ```
   [*PE1-md-md1-ma-ma1] remote-mep mep-id 2
   ```
   ```
   [*PE1-md-md1-ma-ma1] remote-mep ccm-receive mep-id 2 enable
   ```
   ```
   [*PE1-md-md1-ma-ma1] quit
   ```
   ```
   [*PE1-md-md1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] mpls l2vpn oam-mapping 1ag md md1 ma ma1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] cfm enable
   ```
   ```
   [*PE2] cfm md md2
   ```
   ```
   [*PE2-md-md2] ma ma2
   ```
   ```
   [*PE2-md-md2-ma-ma2] map vlan 10
   ```
   ```
   [*PE2-md-md2-ma-ma2] mep mep-id 3 interface GigabitEthernet0/1/0.1 outward
   ```
   ```
   [*PE2-md-md2-ma-ma2] mep ccm-send mep-id 3 enable
   ```
   ```
   [*PE2-md-md2-ma-ma2] remote-mep mep-id 4
   ```
   ```
   [*PE2-md-md2-ma-ma2] remote-mep ccm-receive mep-id 4 enable
   ```
   ```
   [*PE2-md-md2-ma-ma2] quit
   ```
   ```
   [*PE2-md-md2] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] mpls l2vpn oam-mapping 1ag md md2 ma ma2
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] cfm enable
   ```
   ```
   [*PE3] cfm md md1
   ```
   ```
   [*PE3-md-md1] ma ma1
   ```
   ```
   [*PE3-md-md1-ma-ma1] map vlan 10
   ```
   ```
   [*PE3-md-md1-ma-ma1] mep mep-id 1 interface GigabitEthernet0/1/0.1 outward
   ```
   ```
   [*PE3-md-md1-ma-ma1] mep ccm-send mep-id 1 enable
   ```
   ```
   [*PE3-md-md1-ma-ma1] remote-mep mep-id 2
   ```
   ```
   [*PE3-md-md1-ma-ma1] remote-mep ccm-receive mep-id 2 enable
   ```
   ```
   [*PE3-md-md1-ma-ma1] quit
   ```
   ```
   [*PE3-md-md1] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] mpls l2vpn oam-mapping 1ag md md1 ma ma1
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   [~PE4] cfm enable
   ```
   ```
   [*PE4] cfm md md2
   ```
   ```
   [*PE4-md-md2] ma ma2
   ```
   ```
   [*PE4-md-md2-ma-ma2] map vlan 10
   ```
   ```
   [*PE4-md-md2-ma-ma2] mep mep-id 3 interface GigabitEthernet0/1/0.1 outward
   ```
   ```
   [*PE4-md-md2-ma-ma2] mep ccm-send mep-id 3 enable
   ```
   ```
   [*PE4-md-md2-ma-ma2] remote-mep mep-id 4
   ```
   ```
   [*PE4-md-md2-ma-ma2] remote-mep ccm-receive mep-id 4 enable
   ```
   ```
   [*PE4-md-md2-ma-ma2] quit
   ```
   ```
   [*PE4-md-md2] quit
   ```
   ```
   [*PE4] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE4-GigabitEthernet0/1/0.1] mpls l2vpn oam-mapping 1ag md md2 ma ma2
   ```
   ```
   [*PE4-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE4] commit
   ```
8. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display mpls l2vpn connection interface**](cmdqueryname=display+mpls+l2vpn+connection+interface) command on each PE. The command output shows that BGP VPWS connections have been established. The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls l2vpn connection interface gigabitethernet 0/1/0.1
   ```
   ```
   conn-type: remote
        local vc state:             up
        remote vc state:            up
        local ce-id:                1
        local ce name:              ce1
        remote ce-id:               3
        intf(state,encap):          GigabitEthernet0/1/0.1(up,vlan)
        peer id:                    3.3.3.9
        route-distinguisher:        100:1
        local vc label:             294931
        remote vc label:            294929
        tunnel policy:              default 
        CKey:                       129
        NKey:                       268435580
        primary or secondary:       primary
        forward entry exist or not: true
        forward entry active or not:true
        manual fault set or not:    not set 
        AC OAM state:               up 
        BFD for PW session index:   -- 
        BFD for PW state:           enable 
        BFD for LSP state:          up
        Local C bit is set 
        Remote C bit is set 
        tunnel type:                ldp
        tunnel id:                  0x0000000001004c4b42
   
   ```
   
   CE1 and CE2 can ping each other.
   
   ```
   [~CE1] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=2 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=1 ms
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/1/2 ms
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  vlan batch 10
  #
  cfm enable
  #
  interface Vlanif10
   ip address 10.1.1.1 255.255.255.0
  #               
  interface GigabitEthernet0/1/0
   portswitch     
   undo shutdown  
   port trunk allow-pass vlan 10
  #               
  interface GigabitEthernet0/2/0
   portswitch     
   undo shutdown  
   port trunk allow-pass vlan 10
  #               
  cfm md md1       
   ma ma1          
    map vlan 10    
    mep mep-id 2 interface GigabitEthernet0/1/0 outward
    mep ccm-send mep-id 2 enable
    remote-mep mep-id 1
    remote-mep ccm-receive mep-id 1 enable
  #               
  cfm md md2      
   ma ma2         
    map vlan 10    
    mep mep-id 4 interface GigabitEthernet0/2/0 outward
    mep ccm-send mep-id 4 enable
    remote-mep mep-id 3
    remote-mep ccm-receive mep-id 3 enable
  #               
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  vlan batch 10
  #
  cfm enable
  #
  interface Vlanif10
   ip address 10.1.1.2 255.255.255.0
  #               
  interface GigabitEthernet0/1/0
   portswitch     
   undo shutdown  
   port trunk allow-pass vlan 10
  #               
  interface GigabitEthernet0/2/0
   portswitch     
   undo shutdown  
   port trunk allow-pass vlan 10
  #               
  cfm md md1       
   ma ma1          
    map vlan 10    
    mep mep-id 2 interface GigabitEthernet0/1/0 outward
    mep ccm-send mep-id 2 enable
    remote-mep mep-id 1
    remote-mep ccm-receive mep-id 1 enable
  #               
  cfm md md2      
   ma ma2         
    map vlan 10    
    mep mep-id 4 interface GigabitEthernet0/1/0 outward
    mep ccm-send mep-id 4 enable
    remote-mep mep-id 3
    remote-mep ccm-receive mep-id 3 enable
  #               
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  cfm enable
  #
  bfd
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls l2vpn
  #               
  mpls ldp        
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
  #               
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   mpls l2vpn oam-mapping 1ag md md1 ma ma1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 192.168.1.1 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #               
  mpls l2vpn vpn1 encapsulation vlan control-word
   route-distinguisher 100:1
   vpn-target 200:1 import-extcommunity
   vpn-target 200:1 export-extcommunity
   ce ce1 id 1 range 10 default-offset 0
    connection ce-offset 3 interface GigabitEthernet0/1/0.1
  #               
  bgp 100         
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.9 enable
   #              
   l2vpn-ad-family
    policy vpn-target
    peer 3.3.3.9 enable
    peer 3.3.3.9 signaling vpws
  #               
  ospf 1          
   area 0.0.0.0   
    network 1.1.1.9 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #  
  bfd 1to3 bind pw interface GigabitEthernet0/1/0.1
   discriminator local 13
   discriminator remote 31
  #
  cfm md md1       
   ma ma1          
    map vlan 10    
    mep mep-id 1 interface GigabitEthernet0/1/0.1 outward
    mep ccm-send mep-id 1 enable
    remote-mep mep-id 2
    remote-mep ccm-receive mep-id 2 enable
  #               
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  cfm enable
  #
  bfd
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls l2vpn
  #               
  mpls ldp        
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
  #               
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   mpls l2vpn oam-mapping 1ag md md2 ma ma2
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 192.168.10.1 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #               
  mpls l2vpn vpn1 encapsulation vlan control-word
   route-distinguisher 100:1
   vpn-target 200:1 import-extcommunity
   vpn-target 200:1 export-extcommunity
   ce ce2 id 2 range 10 default-offset 0
    connection ce-offset 4 interface GigabitEthernet0/1/0.1
  #               
  bgp 100         
   peer 4.4.4.9 as-number 100
   peer 4.4.4.9 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.9 enable
   #              
   l2vpn-ad-family
    policy vpn-target
    peer 4.4.4.9 enable
    peer 4.4.4.9 signaling vpws
  #               
  ospf 1          
   area 0.0.0.0   
    network 2.2.2.9 0.0.0.0
    network 192.168.10.0 0.0.0.255
  # 
  bfd 2to4 bind pw interface GigabitEthernet0/1/0.1
   discriminator local 24
   discriminator remote 42
  #
  cfm md md2       
   ma ma2          
    map vlan 10    
    mep mep-id 3 interface GigabitEthernet0/1/0.1 outward
    mep ccm-send mep-id 3 enable
    remote-mep mep-id 4
    remote-mep ccm-receive mep-id 4 enable
  #               
  return   
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  cfm enable
  #
  bfd
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls l2vpn
  #               
  mpls ldp        
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
  #               
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   mpls l2vpn oam-mapping 1ag md md1 ma ma1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 192.168.1.2 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
  #               
  mpls l2vpn vpn1 encapsulation vlan control-word
   route-distinguisher 100:1
   vpn-target 200:1 import-extcommunity
   vpn-target 200:1 export-extcommunity
   ce ce3 id 3 range 10 default-offset 0
    connection ce-offset 1 interface GigabitEthernet0/1/0.1
  #               
  bgp 100         
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
   #              
   l2vpn-ad-family
    policy vpn-target
    peer 1.1.1.9 enable
    peer 1.1.1.9 signaling vpws
  #               
  ospf 1          
   area 0.0.0.0   
    network 3.3.3.9 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #   
  bfd 3to1 bind pw interface GigabitEthernet0/1/0.1
   discriminator local 31
   discriminator remote 13
  #
  cfm md md1       
   ma ma1          
    map vlan 10    
    mep mep-id 1 interface GigabitEthernet0/1/0.1 outward
    mep ccm-send mep-id 1 enable
    remote-mep mep-id 2
    remote-mep ccm-receive mep-id 2 enable
  #               
  return
  ```
* PE4 configuration file
  
  ```
  #
  sysname PE4
  #
  cfm enable
  #
  bfd
  #
  mpls lsr-id 4.4.4.9
  #
  mpls
  #
  mpls l2vpn
  #               
  mpls ldp        
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
  #               
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   mpls l2vpn oam-mapping 1ag md md2 ma ma2
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 192.168.10.2 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
  #               
  mpls l2vpn vpn1 encapsulation vlan control-word
   route-distinguisher 100:1
   vpn-target 200:1 import-extcommunity
   vpn-target 200:1 export-extcommunity
   ce ce4 id 4 range 10 default-offset 0
    connection ce-offset 2 interface GigabitEthernet0/1/0.1
  #               
  bgp 100         
   peer 2.2.2.9 as-number 100
   peer 2.2.2.9 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.9 enable
   #              
   l2vpn-ad-family
    policy vpn-target
    peer 2.2.2.9 enable
    peer 2.2.2.9 signaling vpws
  #               
  ospf 1          
   area 0.0.0.0   
    network 4.4.4.9 0.0.0.0
    network 192.168.10.0 0.0.0.255
  #   
  bfd 4to2 bind pw interface GigabitEthernet0/1/0.1
   discriminator local 42
   discriminator remote 24
  #
  cfm md md2       
   ma ma2          
    map vlan 10    
    mep mep-id 3 interface GigabitEthernet0/1/0.1 outward
    mep ccm-send mep-id 3 enable
    remote-mep mep-id 4
    remote-mep ccm-receive mep-id 4 enable
  #               
  return   
  ```