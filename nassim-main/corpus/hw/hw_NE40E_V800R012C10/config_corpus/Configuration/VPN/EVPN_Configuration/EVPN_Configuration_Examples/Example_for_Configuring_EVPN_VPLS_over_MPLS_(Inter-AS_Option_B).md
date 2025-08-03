Example for Configuring EVPN VPLS over MPLS (Inter-AS Option B)
===============================================================

This section provides an example for configuring EVPN VPLS over MPLS. A single-hop MP-EBGP peer relationship is established between ASBRs to exchange EVPN routes.

#### Networking Requirements

As shown in the following figure, CE1 and CE2 belong to the same EVPN. CE1 is connected to PE1 in AS 100, and CE2 is connected to PE2 in AS 200. It is required that an MP-EBGP peer relationship be established between the ASBRs to transmit EVPN routes, implementing inter-AS EVPN Option B.

**Figure 1** Configuring EVPN VPLS over MPLS (inter-AS Option B)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_evpn_mpls_optionB_03.png)  


#### Configuration Precautions

During the configuration process, note the following:

* Configure an MP-EBGP peer relationship between ASBR1 and ASBR2, and disable the ASBRs from filtering received EVPN routes based on VPN targets.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the MPLS backbone network to implement interworking between the ASBRs and PEs in each AS, and establish an MPLS LDP LSP between the ASBRs and PEs in each AS.
2. Configure the CE access function on the PE and establish an MP-IBGP peer relationship between the PE and ASBR in each AS.
3. Configure EVPN instances on PEs (no EVPN instance needs to be configured on ASBRs).
4. Enable MPLS on the ASBR interfaces connected to each other. Establish an MP-EBGP peer relationship between ASBRs and configure ASBRs not to filter EVPN routes based on VPN targets.

#### Data Preparation

To complete the configuration, you need the following data:

* Interfaces and their IP addresses
* MPLS LSR IDs of the PEs and ASBRs
* Names, RDs, and VPN targets of the EVPN instances on PE1 and PE2

#### Procedure

1. On the MPLS backbone networks in AS 100 and AS 200, configure an IGP for communication between the PEs on each network.
   
   
   
   In this example, OSPF is used. For detailed configurations, see Configuration Files.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Configure OSPF to advertise the 32-bit loopback interface addresses used as LSR IDs.
   
   After completing the preceding configurations, run the **display ospf peer** command on the ASBR and PE in each AS. The command output shows that the OSPF neighbor relationship is in the **Full** state, which indicates that the OSPF neighbor relationship has been established between the ASBR and PE in the same AS.
   
   The ASBR and PE in the same AS can learn the loopback interface address of each other and successfully ping each other.
2. Configure basic MPLS capabilities and MPLS LDP on the MPLS backbone networks of AS 100 and AS 200 to establish LDP LSPs.
   
   
   
   For detailed configurations, see Configuration Files.
3. Configure basic EVPN functions on PE1 and PE2.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   PE1's EVPN instance import and export VPN targets must match PE2's EVPN instance export and import VPN targets, respectively.
   
   For detailed configurations, see Configuration Files.
4. Configure inter-AS EVPN Option B.
   
   # On ASBR1, enable MPLS on GE0/2/0 connected to ASBR2.
   ```
   [~ASBR1] interface GigabitEthernet 0/2/0
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] ip address 192.168.1.1 24
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
   
   On ASBR1, specify ASBR2 as an MP-EBGP peer, and disable ASBR1 from filtering received EVPN routes based on VPN targets.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 192.168.1.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
   ```
   ```
   [*ASBR1-bgp-af-EVPN] peer 192.168.1.2 enable
   ```
   ```
   [*ASBR1-bgp-af-EVPN] undo policy vpn-target
   ```
   ```
   [*ASBR1-bgp-af-EVPN] commit
   ```
   ```
   [~ASBR1-bgp-af-EVPN] quit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
   
   The configuration of ASBR2 is similar to that of ASBR1. For detailed configurations, see Configuration Files.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf_1 bd-mode
    route-distinguisher 100:1
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf_1
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.21.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  bgp 100
   peer 2.2.2.9 as-number 100
   peer 2.2.2.9 connect-interface LoopBack1
   #
   ipv4-family unicast
   undo synchronization
   peer 2.2.2.9 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2.2.2.9 enable
    peer 2.2.2.9 esad-route-compatible enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 172.21.1.0 0.0.0.255
  #
  evpn source-address 1.1.1.9
  #
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.21.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  bgp 100
   peer 192.168.1.2 as-number 200
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.2 enable
    peer 1.1.1.9 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.9 enable
    peer 1.1.1.9 esad-route-compatible enable
    peer 192.168.1.2 enable
    peer 192.168.1.2 esad-route-compatible enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 172.21.1.0 0.0.0.255
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.22.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
  #
  bgp 200
   peer 192.168.1.1 as-number 100
   peer 4.4.4.9 as-number 200
   peer 4.4.4.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.1 enable
    peer 4.4.4.9 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 4.4.4.9 enable
    peer 4.4.4.9 esad-route-compatible enable
    peer 192.168.1.1 enable
    peer 192.168.1.1 esad-route-compatible enable
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 172.22.1.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  evpn vpn-instance evrf_1 bd-mode
    route-distinguisher 200:1
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 4.4.4.9
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf_1
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.22.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
  #
  bgp 200
   peer 3.3.3.9 as-number 200
   peer 3.3.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
   undo synchronization
   peer 3.3.3.9 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.9 enable
    peer 3.3.3.9 esad-route-compatible enable
  #
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.9 0.0.0.0
    network 172.22.1.0 0.0.0.255
  #
  evpn source-address 4.4.4.9
  #
  return
  ```