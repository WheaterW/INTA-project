Example for Configuring BGP VPLS
================================

BGP VPLS applies to scenarios where PEs can use BGP as the VPLS signaling. BGP VPLS allows automatic discovery of VPLS PEs based on VPN targets.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370226__fig_dc_vrp_vpls_cfg_601901), VPLS is enabled on PE1 and PE2. CE1 and CE2 are connected to PE1 and PE2, respectively. CE1 and CE2 belong to the same VPLS network.

To implement communication between CE1 and CE2, BGP is used as the VPLS signaling to establish PWs and VPN targets are configured to automatically discover VPLS PEs.

**Figure 1** Configuring BGP VPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1, subinterface1.1, interface2, and subinterface2.1 represent GE0/1/0, GE0/1/0.1, GE0/2/0, and GE0/2/0.1, respectively.

  
![](images/fig_dc_vrp_vpls_cfg_601901.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. On the backbone network, configure a routing protocol to implement connectivity between devices and configure basic MPLS functions.
2. Establish LSPs between PEs.
3. Enable MPLS L2VPN on PEs.
4. Configure PEs to exchange VPLS information with BGP peers.
5. Create a VSI on each PE, specify BGP as the signaling protocol, and specify the RD, VPN targets, and site IDs.
6. Bind AC interfaces to VSIs.

#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP addresses
* VSI names on PE1 and PE2
* BGP AS numbers on PE1 and PE2
* VSI signaling protocol (BGP)
* RDs, VPN targets, and site IDs of VSIs on PEs
* Names and VLAN IDs of the interfaces to be bound to VSIs

#### Procedure

1. Configure IP addresses for involved devices on the backbone network.
   
   
   
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
   [*PE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
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
   [~P] interface loopback1
   ```
   ```
   [*P-Loopback1] ip address 2.2.2.2 32
   ```
   ```
   [*P-Loopback1] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] ip address 192.168.1.2 24
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] ip address 192.168.10.1 24
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
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
   [~PE2] interface loopback1
   ```
   ```
   [*PE2-Loopback1] ip address 3.3.3.3 32
   ```
   ```
   [*PE2-Loopback1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] 192.168.10.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
2. Configure an IGP. In this example, OSPF is used.
   
   
   
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
   [*P-ospf-1] area 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 192.168.10.0 0.0.0.255
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
   [*PE2-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
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
   
   # Configure the P.
   
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
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
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
4. Enable BGP peers to exchange VPLS information.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback1
   ```
   ```
   [*PE1-bgp] l2vpn-ad-family
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] peer 3.3.3.3 signaling vpls
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
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 connect-interface loopback1
   ```
   ```
   [*PE2-bgp] l2vpn-ad-family
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] peer 1.1.1.1 signaling vpls
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
5. Enable MPLS L2VPN on PEs.
   
   
   
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
6. Configure a VSI on each PE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The site IDs on both ends of a VPLS PW must be different.
   
   # Configure PE1.
   
   ```
   [~PE1] vsi bgp1
   ```
   ```
   [*PE1-vsi-bgp1] pwsignal bgp
   ```
   ```
   [*PE1-vsi-bgp1-bgp] route-distinguisher 192.168.1.1:1
   ```
   ```
   [*PE1-vsi-bgp1-bgp] vpn-target 100:1 import-extcommunity
   ```
   ```
   [*PE1-vsi-bgp1-bgp] vpn-target 100:1 export-extcommunity
   ```
   ```
   [*PE1-vsi-bgp1-bgp] site 1 range 5 default-offset 0
   ```
   ```
   [*PE1-vsi-bgp1-bgp] quit
   ```
   ```
   [*PE1-vsi-bgp1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] vsi bgp1
   ```
   ```
   [*PE2-vsi-bgp1] pwsignal bgp
   ```
   ```
   [*PE2-vsi-bgp1-bgp] route-distinguisher 192.168.10.2:1
   ```
   ```
   [*PE2-vsi-bgp1-bgp] vpn-target 100:1 import-extcommunity
   ```
   ```
   [*PE2-vsi-bgp1-bgp] vpn-target 100:1 export-extcommunity
   ```
   ```
   [*PE2-vsi-bgp1-bgp] site 2 range 5 default-offset 0
   ```
   ```
   [*PE2-vsi-bgp1-bgp] quit
   ```
   ```
   [*PE2-vsi-bgp1] quit
   ```
   ```
   [*PE2] commit
   ```
7. Bind AC interfaces to VSIs on PEs.
   
   
   
   # Create a sub-interface on PE1, add this sub-interface to VLAN 10, and bind this sub-interface to the VSI.
   
   ```
   [~PE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [~PE1-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] l2 binding vsi bgp1
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
   
   # Create a sub-interface on PE2, add this sub-interface to VLAN 10, and bind this sub-interface to the VSI.
   
   ```
   [~PE2] interface gigabitethernet0/2/0.1
   ```
   ```
   [~PE2-GigabitEthernet0/2/0.1] shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] l2 binding vsi bgp1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
8. Configure CEs.
   
   
   
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
   [~CE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
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
   [~CE2] interface gigabitethernet0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] commit
   ```
9. Verify the configuration.
   
   
   
   After the configuration is complete, run the [**display vsi name bgp1 verbose**](cmdqueryname=display+vsi+name+bgp1+verbose) command on PE1. The command output shows that a VSI named **bgp1** has set up a PW to PE2 and **VSI State** is **up**.
   
   ```
   [~PE1] display vsi name bgp1 verbose
   ```
   ```
    ***VSI Name               : bgp1
       Work Mode              : normal 
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 0
       PW Signaling           : bgp
       Member Discovery Style : auto
       PW MAC Learn Style     : unqualify
       Encapsulation Type     : vlan
       MTU                    : 1500
       Diffserv Mode          : uniform
       Service Class          : --
       Color                  : --
       DomainId               : 255
       Domain Name            :
       Ignore AcState         : disable
       Create Time            : 0 days, 0 hours, 6 minutes, 52 seconds
       VSI State              : up
       Resource Status        : Valid
   
       BGP RD                 : 192.168.1.1:1
       SiteID/Range/Offset    : 1/5/0
       Import vpn target      : 100:1
       Export vpn target      : 100:1
       Remote Label Block     : 25600/5/0
       Local Label Block      : 0/25600/5/0
   
       Interface Name         : GigabitEthernet0/1/0.1
       State                  : up
       Access Port            : false
       Last Up Time           : 2013/01/17 10:29:49
       Total Up Time          : 0 days, 0 hours, 18 minutes, 20 seconds
   
      **PW Information:
   
      *Peer Ip Address        : 3.3.3.3
       PW State               : up
       Local VC Label         : 25602
       Remote VC Label        : 25601
       PW Type                : label
       Tunnel ID              : 0x800006
       Broadcast Tunnel ID    : 0x800006
       Broad BackupTunnel ID  : 0x0
       Ckey                   : 0x2
       Nkey                   : 0x1
       Main PW Token          : 0x800006
       Slave PW Token         : 0x0
       Tnl Type               : LSP
       OutInterface           : GigabitEthernet0/2/0
       Backup OutInterface    :
       Stp Enable             : 0
       Mac Flapping           : 0   
       PW Last Up Time        : 2013/01/17 10:31:05
       PW Total Up Time       : 0 days, 0 hours, 17 minutes, 4 seconds
   ```
   
   # Configure CE1 (10.1.1.1) to ping CE2 (10.1.1.2). The ping is successful.
   
   ```
   [~CE1] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=90 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=77 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=34 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=46 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=94 ms
   ```
   ```
     --- 10.1.1.2 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 34/68/94 ms 
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   ip address 10.1.1.1 255.255.255.0
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   ip address 10.1.1.2 255.255.255.0
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
  vsi bgp1
   pwsignal bgp
    route-distinguisher 192.168.1.1:1
    vpn-target 100:1 import-extcommunity
    vpn-target 100:1 export-extcommunity
    site 1 range 5 default-offset 0
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   l2 binding vsi bgp1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   l2vpn-ad-family
    policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 signaling vpls
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
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
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.10.0 0.0.0.255
    network 2.2.2.2 0.0.0.0
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  vsi bgp1
   pwsignal bgp
    route-distinguisher 192.168.10.2:1
    vpn-target 100:1 import-extcommunity
    vpn-target 100:1 export-extcommunity
    site 2 range 5 default-offset 0
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.10.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0.1
   undo shutdown
   vlan-type dot1q 10
   l2 binding vsi bgp1
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   l2vpn-ad-family
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 signaling vpls
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 192.168.10.0 0.0.0.255
  #
  return
  ```