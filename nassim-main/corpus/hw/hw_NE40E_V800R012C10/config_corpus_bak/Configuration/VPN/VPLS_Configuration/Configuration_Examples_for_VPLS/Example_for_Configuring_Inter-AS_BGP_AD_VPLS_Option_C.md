Example for Configuring Inter-AS BGP AD VPLS Option C
=====================================================

In inter-AS BGP AD VPLS Option C, ASBRs do not need to create or maintain VCs. This solution is recommended for scenarios where large numbers of inter-AS VPLS PWs are required.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370245__fig_dc_vrp_vpls_cfg_605301), CE1 and CE2 access the backbone network through PE1 in AS100 and PE2 in AS200, respectively.

Inter-AS BGP AD VPLS Option C needs to be deployed for CE1 and CE2 to communicate. In inter-AS BGP AD VPLS Option C, PEs directly exchange VPLS label blocks, and ASBRs do not maintain VPLS label blocks.

**Figure 1** Configuring inter-AS BGP AD VPLS Option C![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, subinterface1.1, interface2, and subinterface2.1 represent GE0/1/0, GE0/1/0.1, GE0/2/0, and GE0/2/0.1, respectively.


  
![](images/fig_dc_vrp_vpls_cfg_605301.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP for each AS on the MPLS backbone network to ensure IP connectivity within the same AS.
2. Configure basic MPLS functions on the MPLS backbone network and establish a dynamic LSP between the PE and ASBR in the same AS. (ASBR interfaces also need to have basic MPLS functions configured.)
3. Establish an IBGP peer relationship between the PE and ASBR in the same AS.
4. Specify EBGP peers, configure route-policies, and enable label-based routing on ASBRs. Establish an MP-EBGP peer relationship between PE1 and PE2.
5. Configure VSIs on PEs and bind the corresponding AC interfaces to these VSIs.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the PEs and ASBRs
* Name, RD, and VPN targets of each VSI
* AC interfaces bound to VSIs
* Route-policies used by ASBRs

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
   [~CE1] interface gigabitethernet 0/1/0.1
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
   [*PE1] interface gigabitethernet 0/2/0
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
   [*ASBR1-GigabitEthernet0/1/0] ip address 10.10.1.2 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] ip address 10.20.1.1 24
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
   [*ASBR2] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] ip address 10.20.1.2 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] ip address 10.30.1.1 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
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
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.30.1.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
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
   [~CE2] interface gigabitethernet 0/1/0.1
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
2. Configure IGP on the backbone network.
   
   
   
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
   [*ASBR2] ospf 1
   ```
   ```
   [*ASBR2-ospf-1] area 0.0.0.0
   ```
   ```
   [*ASBR2-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*ASBR2-ospf-1-area-0.0.0.0] network 10.30.1.0 0.0.0.255
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
   [*PE2-ospf-1-area-0.0.0.0] network 10.30.1.0 0.0.0.255
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
3. Configure basic MPLS functions and establish LSPs.
   
   
   
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
   [*ASBR1] mpls lsr-id 2.2.2.2
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
   [*ASBR1] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] mpls ldp
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
   [*PE2] interface gigabitethernet 0/1/0
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
4. Enable inter-AS MPLS on ASBRs.
   
   
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] interface gigabitethernet 0/1/0
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
5. Establish an MP-IBGP peer relationship between the PE and ASBR in the same AS, set up an MP-EBGP peer relationship between ASBRs, and configure route-policies on ASBRs. For routes received from PEs in the same AS, the ASBR allocates MPLS labels to the routes before advertising them to the peer ASBR. When an ASBR advertises labeled IPv4 routes to a PE in the same AS, the ASBR reallocates MPLS labels to the routes.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 label-route-capability
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 connect-interface LoopBack 1
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [*ASBR1] route-policy policy1 permit node 1
   ```
   ```
   [*ASBR1-route-policy] if-match mpls-label
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [*ASBR1] route-policy policy2 permit node 1
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [*ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] network 1.1.1.1 255.255.255.255
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 route-policy policy1 export
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 label-route-capability
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*ASBR1-bgp] peer 10.20.1.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] peer 10.20.1.2 route-policy policy2 export
   ```
   ```
   [*ASBR1-bgp] peer 10.20.1.2 label-route-capability
   ```
   ```
   [*ASBR1-bgp] peer 10.20.1.2 connect-interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR1-bgp]quit
   ```
   ```
   [*ASBR1]commit
   ```
   
   # Configure ASBR2.
   
   ```
   [*ASBR2] route-policy policy1 permit node 1
   ```
   ```
   [*ASBR2-route-policy] if-match mpls-label
   ```
   ```
   [*ASBR2-route-policy] apply mpls-label
   ```
   ```
   [*ASBR2-route-policy] quit
   ```
   ```
   [*ASBR2] route-policy policy2 permit node 1
   ```
   ```
   [*ASBR2-route-policy] apply mpls-label
   ```
   ```
   [*ASBR2-route-policy] quit
   ```
   ```
   [*ASBR2] bgp 200
   ```
   ```
   [*ASBR2-bgp] network 4.4.4.4 255.255.255.255
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 as-number 200
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 route-policy policy1 export
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 label-route-capability
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 connect-interface loopback 1
   ```
   ```
   [*ASBR2-bgp] peer 10.20.1.1 as-number 100
   ```
   ```
   [*ASBR2-bgp] peer 10.20.1.1 route-policy policy2 export
   ```
   ```
   [*ASBR2-bgp] peer 10.20.1.1 label-route-capability
   ```
   ```
   [*ASBR2-bgp] peer 10.20.1.1 connect-interface gigabitethernet 0/1/0
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
   [*PE2-bgp] peer 3.3.3.3 label-route-capability
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   Run the **display tunnel-info all** command on each ASBR. The command output shows that a tunnel with the type being **mpls local ifnet** has been established. The following example uses the command output on ASBR1.
   
   ```
   [~ASBR1] display tunnel-info all
   ```
   ```
   Tunnel ID                     Type                Destination         Status
   -----------------------------------------------------------------------------
   0x0000000001004c6b42          ldp                 1.1.1.1             UP  
   0x000000000c00030000          mpls local ifnet    10.20.1.2           UP  
   ```
   
   Run the **display tunnel-info all** command on each PE. The command output shows that an inter-AS LSP has been established between PE1 and PE2. The following example uses the command output on PE1.
   
   ```
   [~PE1] display tunnel-info all
   ```
   ```
   Tunnel ID                     Type                Destination         Status
   -----------------------------------------------------------------------------
   0x0000000001004c6b42          ldp                 2.2.2.2             UP  
   0x000000000201040000          bgp                 4.4.4.4             UP
   ```
6. Establish an MP-EBGP peer relationship between PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 as-number 200
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 ebgp-max-hop 255
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-ad-family
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] peer 4.4.4.4 enable
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
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 ebgp-max-hop 255
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-ad-family
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] peer 1.1.1.1 enable
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
   
   After completing the configurations, run the **display bgp l2vpn-ad peer** command on PE1 or PE2. The command output shows that the status of the MP-EBGP peer relationship between PE1 and PE2 is **Established**. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp l2vpn-ad peer
   ```
   ```
    
    BGP local router ID : 10.10.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     4.4.4.4         4         200        5        6     0 00:00:41 Established       0
   ```
7. Configure VSIs on PEs and bind the corresponding AC interfaces to these VSIs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1] quit
   ```
   ```
   [*PE1] vsi vplsad1
   ```
   ```
   [*PE1-vsi-vplsad1] bgp-ad
   ```
   ```
   [*PE1-vsi-vplsad1-bgpad] vpls-id 100:1
   ```
   ```
   [*PE1-vsi-vplsad1-bgpad] vpn-target 200:1 import-extcommunity
   ```
   ```
   [*PE1-vsi-vplsad1-bgpad] vpn-target 200:1 export-extcommunity
   ```
   ```
   [*PE1-vsi-vplsad1-bgpad] quit
   ```
   ```
   [*PE1-vsi-vplsad1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] l2 binding vsi vplsad1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] mpls l2vpn
   ```
   ```
   [*PE2] quit
   ```
   ```
   [*PE2] vsi vplsad1
   ```
   ```
   [*PE2-vsi-vplsad1] bgp-ad
   ```
   ```
   [*PE2-vsi-vplsad1-bgpad] vpls-id 100:1
   ```
   ```
   [*PE2-vsi-vplsad1-bgpad] vpn-target 200:1 import-extcommunity
   ```
   ```
   [*PE2-vsi-vplsad1-bgpad] vpn-target 200:1 export-extcommunity
   ```
   ```
   [*PE2-vsi-vplsad1-bgpad] quit
   ```
   ```
   [*PE2-vsi-vplsad1] quit
   ```
   ```
   [~PE2] interface gigabitethernet0/2/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] l2 binding vsi vplsad1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
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
   Check VSI information on PEs. The command output shows that the VSI status is up. The PW to the remote PE is also up. The following example uses the command output on PE1.
   ```
   [~PE1] display vsi
   ```
   ```
   Total VSI number is 1, 1 is up, 0 is down, 0 is LDP mode, 0 is BGP mode, 1 is BGPAD mode, 0 is mixed mode, 0 is unspecified mode
   --------------------------------------------------------------------------
   Vsi                             Mem    PW    Mac       Encap     Mtu   Vsi
   Name                            Disc   Type  Learn     Type      Value State
   --------------------------------------------------------------------------
   vplsad1                         --     bgpad unqualify vlan      1500  up
   ```
8. Verify the configuration.
   
   
   
   After the preceding configurations are complete, CE1 and CE2 can ping each other. The following example uses the command output on CE1.
   
   ```
   [~CE1] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=19 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=3 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=4 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=3 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=3 ms
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 3/6/19 ms
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
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vplsad1
   bgp-ad
    vpls-id 100:1
    vpn-target 200:1 import-extcommunity
    vpn-target 200:1 export-extcommunity
  #               
  mpls ldp        
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
  #               
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi vplsad1
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
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 ebgp-max-hop 255
   peer 4.4.4.4 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 2.2.2.2 label-route-capability  
    peer 4.4.4.4 enable
   #              
   l2vpn-ad-family
    policy vpn-target
    peer 4.4.4.4 enable
  #               
  ospf 1          
   area 0.0.0.0   
    network 1.1.1.1 0.0.0.0
    network 10.10.1.0 0.0.0.255
  #               
  return 
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.20.1.1 255.255.255.0
   mpls           
  #               
  interface GigabitEthernet0/1/0
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
   peer 10.20.1.2 as-number 200
   peer 10.20.1.2 connect-interface GigabitEthernet0/2/0
   #              
   ipv4-family unicast
    undo synchronization
    network 1.1.1.1 255.255.255.255
    peer 1.1.1.1 enable
    peer 1.1.1.1 route-policy policy1 export
    peer 1.1.1.1 label-route-capability  
    peer 10.20.1.2 enable
    peer 10.20.1.2 route-policy policy2 export
    peer 10.20.1.2 label-route-capability  
  #               
  ospf 1          
   area 0.0.0.0   
    network 2.2.2.2 0.0.0.0
    network 10.10.1.0 0.0.0.255
  #               
  route-policy policy1 permit node 1
   if-match mpls-label
   apply mpls-label
  #               
  route-policy policy2 permit node 1
   apply mpls-label
  #               
  return  
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.30.1.1 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.20.1.2 255.255.255.0
   mpls           
  #               
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #               
  bgp 200         
   peer 4.4.4.4 as-number 200
   peer 10.20.1.1 as-number 100
   peer 10.20.1.1 connect-interface GigabitEthernet0/1/0
   #              
   ipv4-family unicast
    undo synchronization
    network 4.4.4.4 255.255.255.255
    peer 4.4.4.4 enable
    peer 4.4.4.4 route-policy policy1 export
    peer 4.4.4.4 label-route-capability  
    peer 10.20.1.1 enable
    peer 10.20.1.1 route-policy policy2 export
    peer 10.20.1.1 label-route-capability  
  #               
  ospf 1          
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 10.30.1.0 0.0.0.255
  #               
  route-policy policy1 permit node 1
   if-match mpls-label
   apply mpls-label
  #               
  route-policy policy2 permit node 1
   apply mpls-label
  #               
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vplsad1
   bgp-ad
    vpls-id 100:1
    vpn-target 200:1 import-extcommunity
    vpn-target 200:1 export-extcommunity
  #               
  mpls ldp        
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.30.1.2 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
  #               
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 10
   l2 binding vsi vplsad1
  #               
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #               
  bgp 200         
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 ebgp-max-hop 255
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 3.3.3.3 label-route-capability  
   #              
   l2vpn-ad-family
    policy vpn-target
    peer 1.1.1.1 enable
  #               
  ospf 1          
   area 0.0.0.0   
    network 4.4.4.4 0.0.0.0
    network 10.30.1.0 0.0.0.255
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