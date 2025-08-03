Example for Configuring PBB VPLS with Multiple I-VSIs Bound to the Same B-VSI
=============================================================================

This section provides an example for configuring PBB VPLS on a network where PE1, PE2, and PE3 are fully meshed, and CEs are single-homed to PEs. PE1 needs to communicate with PE2 and PE3, requiring two I-VSIs to be configured and bound to the same B-VSI.

#### Networking Requirements

On the PBB VPLS network shown in [Figure 1](#EN-US_TASK_0172370806__fig_dc_vrp_pbb-vpls_cfg_001401), PE1, PE2, and PE3 are fully meshed, and CEs are single-homed to PEs. To enable CE1, CE2, and CE3 to communicate over the PBB VPLS network, configure a B-VSI and two I-VSIs on each PE and bind the I-VSIs on each PE to the B-VSI on that PE. Different I-VSIs can be used to isolate broadcast domains.

**Figure 1** Network diagram of configuring PBB VPLS with multiple I-VSIs bound to the same B-VSI![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1, subinterface1.1, subinterface1.2, interface2, and interface3 represent GE0/1/0, GE0/1/0.1, GE0/1/0.2, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_pbb-vpls_cfg_001401.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and an IGP for each involved interface to ensure IP connectivity.
2. Configure MPLS and MPLS LDP.
3. Enable MPLS L2VPN and configure PBB VPLS.

#### Data Preparation

* IP addresses and masks of interfaces on the backbone network
* I-VSI and B-VSI names, VSI IDs, B-SMAC addresses, B-DMAC addresses, and I-tags

#### Procedure

1. Configure IP addresses for CEs and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370806__dc_vrp_pbb-vpls_cfg_001401).
2. Configure an IGP (OSPF in this example) on each PE.
   
   
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
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
   [*PE1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
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
   <PE2> system-view
   ```
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
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
   <PE3> system-view
   ```
   ```
   [~PE3] ospf 1
   ```
   ```
   [*PE3-ospf-1] area 0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
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
   
   # After the configuration is complete, check OSPF route information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ospf routing
   ```
   ```
    OSPF Process 1 with Router ID 10.1.1.1
      Routing Tables
   
    Routing for Network
    Destination        Cost     Type       NextHop         AdvRouter       Area           
    1.1.1.1/32         0        Direct     1.1.1.1         10.1.1.1        0.0.0.0
    2.2.2.2/32         1        Stub       10.1.1.2        10.1.1.2        0.0.0.0
    3.3.3.3/32         1        Stub       10.2.1.2        10.2.1.2        0.0.0.0
    10.1.1.0/24        1        Direct     10.1.1.1        10.1.1.1        0.0.0.0
    10.2.1.0/24        1        Direct     10.2.1.1        10.1.1.1        0.0.0.0
    10.3.1.0/24        2        Stub       10.2.1.2        10.2.1.2        0.0.0.0
   
    Total Nets: 6
    Intra Area: 6  Inter Area: 0  ASE: 0  NSSA: 0
   
   ```
3. Configure MPLS and MPLS LDP and establish LSPs.
   
   
   
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
   [*PE1] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 2.2.2.2
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
   [*PE2] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls lsr-id 3.3.3.3
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
   [*PE3] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # After the configuration is complete, check LDP LSP information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
   --------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
   --------------------------------------------------------------------------
    2.2.2.2:0          Operational DU   Passive  0000:00:00   4/4
    3.3.3.3:0          Operational DU   Passive  0000:00:00   1/1
   --------------------------------------------------------------------------
   TOTAL: 2 Session(s) Found.
   ```
4. Configure PBB VPLS.
   1. Enable MPLS L2VPN.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] mpls l2vpn
      ```
      ```
      [*PE1-l2vpn] quit
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
      [*PE3] commit
      ```
   2. Configure I-VSIs.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] vsi ivsi1 i-vsi p2p
      ```
      ```
      [*PE1-vsi-ivsi1] pwsignal ldp
      ```
      ```
      [*PE1-vsi-ivsi1-ldp] vsi-id 10
      ```
      ```
      [*PE1-vsi-ivsi1] pbb i-tag 100
      ```
      ```
      [*PE1-vsi-ivsi1] pbb backbone-destination-mac 00e0-fc34-5678 static
      ```
      ```
      [*PE1-vsi-ivsi1] quit
      ```
      ```
      [*PE1] vsi ivsi2 i-vsi p2p
      ```
      ```
      [*PE1-vsi-ivsi2] pwsignal ldp
      ```
      ```
      [*PE1-vsi-ivsi2-ldp] vsi-id 20
      ```
      ```
      [*PE1-vsi-ivsi2] pbb i-tag 101
      ```
      ```
      [*PE1-vsi-ivsi2] pbb backbone-destination-mac 00e0-fc12-3456 static
      ```
      ```
      [*PE1-vsi-ivsi2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] vsi ivsi1 i-vsi p2p
      ```
      ```
      [*PE2-vsi-ivsi1] pwsignal ldp
      ```
      ```
      [*PE2-vsi-ivsi1-ldp] vsi-id 10
      ```
      ```
      [*PE2-vsi-ivsi1-ldp] quit
      ```
      ```
      [*PE2-vsi-ivsi1] pbb i-tag 101
      ```
      ```
      [*PE2-vsi-ivsi1] pbb backbone-destination-mac 00e0-fc00-1234 static
      ```
      ```
      [*PE2-vsi-ivsi1] quit
      ```
      ```
      [*PE2] vsi ivsi2 i-vsi p2p
      ```
      ```
      [*PE2-vsi-ivsi2] pwsignal ldp
      ```
      ```
      [*PE2-vsi-ivsi2-ldp] vsi-id 20
      ```
      ```
      [*PE2-vsi-ivsi2-ldp] quit
      ```
      ```
      [*PE2-vsi-ivsi2] pbb i-tag 102
      ```
      ```
      [*PE2-vsi-ivsi2] pbb backbone-destination-mac 00e0-fc34-5678 static
      ```
      ```
      [*PE2-vsi-ivsi2] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] vsi ivsi1 i-vsi p2p
      ```
      ```
      [*PE3-vsi-ivsi1] pwsignal ldp
      ```
      ```
      [*PE3-vsi-ivsi1-ldp] vsi-id 10
      ```
      ```
      [*PE3-vsi-ivsi1-ldp] quit
      ```
      ```
      [*PE3-vsi-ivsi1] pbb i-tag 100
      ```
      ```
      [*PE3-vsi-ivsi1] pbb backbone-destination-mac 00e0-fc00-1234 static
      ```
      ```
      [*PE3-vsi-ivsi1] quit
      ```
      ```
      [*PE3] vsi ivsi2 i-vsi p2p
      ```
      ```
      [*PE3-vsi-ivsi2] pwsignal ldp
      ```
      ```
      [*PE3-vsi-ivsi2-ldp] vsi-id 20
      ```
      ```
      [*PE3-vsi-ivsi2-ldp] quit
      ```
      ```
      [*PE3-vsi-ivsi2] pbb i-tag 102
      ```
      ```
      [*PE3-vsi-ivsi2] pbb backbone-destination-mac 00e0-fc12-3456 static
      ```
      ```
      [*PE3-vsi-ivsi2] quit
      ```
      ```
      [*PE3] commit
      ```
   3. Configure B-VSIs and specify peers for these B-VSIs.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] vsi bvsi1 b-vsi
      ```
      ```
      [*PE1-vsi-bvsi1] pwsignal ldp
      ```
      ```
      [*PE1-vsi-bvsi1-ldp] vsi-id 100
      ```
      ```
      [*PE1-vsi-bvsi1-ldp] peer 2.2.2.2
      ```
      ```
      [*PE1-vsi-bvsi1-ldp] peer 3.3.3.3
      ```
      ```
      [*PE1-vsi-bvsi1-ldp] quit
      ```
      ```
      [*PE1-vsi-bvsi1] pbb backbone-source-mac 00e0-fc00-1234
      ```
      ```
      [*PE1-vsi-bvsi1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] vsi bvsi1 b-vsi
      ```
      ```
      [*PE2-vsi-bvsi1] pwsignal ldp
      ```
      ```
      [*PE2-vsi-bvsi1-ldp] vsi-id 100
      ```
      ```
      [*PE2-vsi-bvsi1-ldp] peer 1.1.1.1
      ```
      ```
      [*PE2-vsi-bvsi1-ldp] peer 3.3.3.3
      ```
      ```
      [*PE2-vsi-bvsi1-ldp] quit
      ```
      ```
      [*PE2-vsi-bvsi1] pbb backbone-source-mac 00e0-fc12-3456
      ```
      ```
      [*PE2-vsi-bvsi1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] vsi bvsi1 b-vsi
      ```
      ```
      [*PE3-vsi-bvsi1] pwsignal ldp
      ```
      ```
      [*PE3-vsi-bvsi1-ldp] vsi-id 100
      ```
      ```
      [*PE3-vsi-bvsi1-ldp] peer 1.1.1.1
      ```
      ```
      [*PE3-vsi-bvsi1-ldp] peer 2.2.2.2
      ```
      ```
      [*PE3-vsi-bvsi1-ldp] quit
      ```
      ```
      [*PE3-vsi-bvsi1] pbb backbone-source-mac 00e0-fc34-5678
      ```
      ```
      [*PE3-vsi-bvsi1] quit
      ```
      ```
      [*PE3] commit
      ```
   4. Bind each I-VSI to the corresponding B-VSI.
      
      # Configure PE1.
      ```
      [~PE1] vsi ivsi1
      ```
      ```
      [*PE1-vsi-ivsi1] pbb binding b-vsi bvsi1
      ```
      ```
      [*PE1-vsi-ivsi1] quit
      ```
      ```
      [*PE1] vsi ivsi2
      ```
      ```
      [*PE1-vsi-ivsi2] pbb binding b-vsi bvsi1
      ```
      ```
      [*PE1-vsi-ivsi2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      ```
      [~PE2] vsi ivsi1
      ```
      ```
      [*PE2-vsi-ivsi1] pbb binding b-vsi bvsi1
      ```
      ```
      [*PE2-vsi-ivsi1] quit
      ```
      ```
      [*PE2] vsi ivsi2
      ```
      ```
      [*PE2-vsi-ivsi2] pbb binding b-vsi bvsi1
      ```
      ```
      [*PE2-vsi-ivsi2] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      ```
      [~PE3] vsi ivsi1
      ```
      ```
      [*PE3-vsi-ivsi1] pbb binding b-vsi bvsi1
      ```
      ```
      [*PE3-vsi-ivsi1] quit
      ```
      ```
      [*PE3] vsi ivsi2
      ```
      ```
      [*PE3-vsi-ivsi2] pbb binding b-vsi bvsi1
      ```
      ```
      [*PE3-vsi-ivsi2] quit
      ```
      ```
      [*PE3] commit
      ```
   5. Bind an AC interface to each I-VSI.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] interface gigabitethernet0/1/0.1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] l2 binding vsi ivsi1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE1] interface gigabitethernet0/1/0.2
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] vlan-type dot1q 20
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] l2 binding vsi ivsi2
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface gigabitethernet0/1/0.1
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.1] vlan-type dot1q 20
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.1] l2 binding vsi ivsi1
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE2] interface gigabitethernet0/1/0.2
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.2] vlan-type dot1q 30
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.2] l2 binding vsi ivsi2
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.2] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface gigabitethernet0/1/0.1
      ```
      ```
      [*PE3-GigabitEthernet0/1/0.1] vlan-type dot1q 10
      ```
      ```
      [*PE3-GigabitEthernet0/1/0.1] l2 binding vsi ivsi1
      ```
      ```
      [*PE3-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE3] interface gigabitethernet0/1/0.2
      ```
      ```
      [*PE3-GigabitEthernet0/1/0.2] vlan-type dot1q 30
      ```
      ```
      [*PE3-GigabitEthernet0/1/0.2] l2 binding vsi ivsi2
      ```
      ```
      [*PE3-GigabitEthernet0/1/0.2] quit
      ```
      ```
      [*PE3] commit
      ```
      
      # After the configuration is complete, check I-VSI and B-VSI information. The following example uses the command output on PE1. The command output shows that the I-VSI and B-VSI are both up.
      
      ```
      [~PE1] display vsi
      ```
      ```
      Total VSI number is 3, 3 is up, 0 is down, 3 is LDP mode, 0 is BGP mode, 0 is BGPAD mode, 0 is mixed mode, 0 is unspecified mode
      --------------------------------------------------------------------------
      Vsi                             Mem    PW    Mac       Encap     Mtu   Vsi
      Name                            Disc   Type  Learn     Type      Value State
      --------------------------------------------------------------------------
      bvsi1                           --     ldp   unqualify vlan      1500  up   
      ivsi1                           --     ldp   unqualify vlan      1500  up   
      ivsi2                           --     ldp   unqualify vlan      1500  up
      ```
5. Configure CE1 and CE2 to access PEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 10.10.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/0.2
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.2] vlan-type dot1q 20
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 10.20.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 20
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 10.20.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/0.2
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.2] vlan-type dot1q 30
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.2] ip address 10.30.1.1 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.2] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   [~CE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 10.10.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/0.2
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.2] vlan-type dot1q 30
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.2] ip address 10.30.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.2] quit
   ```
   ```
   [*CE2] commit
   ```
6. Verify the configuration.
   
   
   
   After the configuration is complete, CE1, CE2, and CE3 can ping each other. The following uses the command output on CE1.
   
   ```
   [~CE1] ping 10.30.1.2
   ```
   ```
   PING 10.30.1.2: 56  data bytes, press CTRL_C to break
   Reply from 10.30.1.2: bytes=56 Sequence=1 ttl=255 time=3 ms
   Reply from 10.30.1.2: bytes=56 Sequence=2 ttl=255 time=1 ms
   Reply from 10.30.1.2: bytes=56 Sequence=3 ttl=255 time=2 ms
   Reply from 10.30.1.2: bytes=56 Sequence=4 ttl=255 time=1 ms
   Reply from 10.30.1.2: bytes=56 Sequence=5 ttl=255 time=2 ms
   
     --- 10.30.1.2 ping statistics ---
   5 packet(s) transmitted
   5 packet(s) received
   0.00% packet loss
   round-trip min/avg/max = 1/1/3 ms
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
   vlan-type dot1q 10
   ip address 10.10.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 20
   ip address 10.20.1.1 255.255.255.0
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.1
  mpls
  #
  mpls l2vpn
  #
  vsi bvsi1 b-vsi
   pwsignal ldp
    vsi-id 100
    peer 2.2.2.2
    peer 3.3.3.3
   pbb backbone-source-mac 00e0-fc00-1234
  #
  mpls ldp
  vsi ivsi1 i-vsi p2p
   pwsignal ldp
    vsi-id 10
   pbb i-tag 100
   pbb backbone-destination-mac 00e0-fc34-5678 static
   pbb binding b-vsi bvsi1
  #
  vsi ivsi2 i-vsi p2p
   pwsignal ldp
    vsi-id 20
   pbb i-tag 101
   pbb backbone-destination-mac 00e0-fc12-3456 static
   pbb binding b-vsi bvsi1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi ivsi1 
  #
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 20
   l2 binding vsi ivsi2 
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0  
   mpls   
   mpls ldp   
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255  
  #
  ospf 1 
   area 0.0.0.0   
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
  #
  return  
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 2.2.2.2 
  mpls   
  #
  mpls l2vpn 
  #
  vsi bvsi1 b-vsi
   pwsignal ldp
    vsi-id 100
    peer 1.1.1.1
    peer 3.3.3.3
   pbb backbone-source-mac 00e0-fc12-3456
  #
  vsi ivsi1 i-vsi p2p
   pwsignal ldp
    vsi-id 10
   pbb i-tag 101
   pbb backbone-destination-mac 00e0-fc00-1234 static
   pbb binding b-vsi bvsi1
  #
  vsi ivsi2 i-vsi p2p
   pwsignal ldp
    vsi-id 20
   pbb i-tag 102
   pbb backbone-destination-mac 00e0-fc34-5678 static
   pbb binding b-vsi bvsi1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 20
   l2 binding vsi ivsi1
  #
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 30
   l2 binding vsi ivsi2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls   
   mpls ldp   
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1 
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255 
  #
  return   
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  mpls lsr-id 3.3.3.3
  mpls
  #
  mpls l2vpn 
  #
  vsi bvsi1 b-vsi
   pwsignal ldp
    vsi-id 100
    peer 1.1.1.1
    peer 2.2.2.2
   pbb backbone-source-mac 00e0-fc34-5678
  #
  vsi ivsi1 i-vsi p2p
   pwsignal ldp
    vsi-id 10
   pbb i-tag 100
   pbb backbone-destination-mac 00e0-fc00-1234 static
   pbb binding b-vsi bvsi1
  #
  vsi ivsi2 i-vsi p2p
   pwsignal ldp
    vsi-id 20
   pbb i-tag 102
   pbb backbone-destination-mac 00e0-fc12-3456 static
   pbb binding b-vsi bvsi1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi ivsi1
  #
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 30
   l2 binding vsi ivsi2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1 
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
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
   vlan-type dot1q 20
   ip address 10.20.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 30
   ip address 10.30.1.1 255.255.255.0
  #
  return
  ```
* CE3 configuration file
  
  ```
  #
   sysname CE3
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   ip address 10.10.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 30
   ip address 10.30.1.2 255.255.255.0
  #
  return
  ```