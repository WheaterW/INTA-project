Example for Configuring QinQ VLAN Tag Termination Sub-Interfaces to Statically Join Multicast Groups
====================================================================================================

Example_for_Configuring_QinQ_VLAN_Tag_Termination_Sub-Interfaces_to_Statically_Join_Multicast_Groups

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363327__fig_dc_vrp_qinq_cfg_004501), configure a QinQ VLAN tag termination sub-interface on PE1 to statically join multicast groups, to make the Receiver receive multicast data sent from the Source.

**Figure 1** Configuring QinQ VLAN tag termination sub-interfaces to statically join multicast groups![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 and sub-interface2.1 represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/2/0.1, respectively.


  
![](images/fig_dc_vrp_qinq_cfg_004501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure Open Shortest Path First (OSPF) on the backbone network to implement interworking between PEs.
2. Configure the basic Multiprotocol Label Switching (MPLS) functions and MPLS Label Distribution Protocol (LDP) on the PEs and establish the MPLS Label Switched Paths (LSPs) between the PEs.
3. Configure the VPN instance on the PE and bind VPN instance with the interface to Source and the interface to Receiver.
4. Configure Multiprotocol Internal Border Gateway Protocol (MP-IBGP) to exchange the VPN routing information between the PEs.
5. Configure QinQ VLAN tag termination sub-interfaces to statically join multicast groups.

#### Data Preparation

To configure QinQ VLAN tag termination sub-interfaces to statically join multicast groups, you need the following data:

* PE's MPLS LSR-ID: 1.1.1.9; P's MPLS LSR-ID: 2.2.2.9,3.3.3.9
* VPN instance name: vpna; RDs: 100:1 and 100:2; VPN-Target: 111:1
* VLAN ID in an outer VLAN tag of the QinQ VLAN tag termination sub-interface: 1; VLAN ID in an inner VLAN tag of the QinQ VLAN tag termination sub-interface: 1 or 2

#### Procedure

1. Configure basic BGP/MPLS IP VPN.
   
   
   
   The specific configuration procedures are omitted here.
2. Configure a VPN instance on each PE, configure a QinQ VLAN tag termination sub-interface, and bind the interface to the VPN instance.
   
   
   
   # Configure PE1.
   
   # Configure a VPN instance.
   
   ```
   [*PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] commit
   ```
   ```
   [~PE1-vpn-instance-vpna] quit
   ```
   
   # Bind the VPN instance with the interface to the Source.
   
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   
   # Create a QinQ VLAN tag termination sub-interface, bind the VPN instance to the QinQ VLAN tag termination sub-interface.
   
   ```
   [*PE1] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/0.1] quit
   ```
   
   # Configure VLAN ID on the QinQ VLAN tag termination sub-interface.
   
   ```
   [*PE1] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] control-vid 10 qinq-termination
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] qinq termination pe-vid 1 ce-vid 1 to 2
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] ip address 10.2.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/0.1] quit
   ```
   
   # Configure PE2.
   
   # Configure a VPN instance.
   
   ```
   [*PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 100:2
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpna] commit
   ```
   ```
   [~PE2-vpn-instance-vpna] quit
   ```
   
   # Bind the VPN instance with the GE 0/1/0 of PE2.
   
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.3.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] quit
   ```
3. Add the routes of the source and receiver to the VPN routing table on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] import-route direct
   ```
   ```
   [*PE1-bgp-vpna] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] import-route direct
   ```
   ```
   [*PE2-bgp-vpna] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration above, run the **display ip routing-table vpn-instance** command on PE1. The route of the Source and the route of the Receiver are added to VPN routing-table.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpna
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpna
            Destinations : 8        Routes : 8
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
          10.1.1.0/24  Direct  0    0             D  10.1.1.2        GigabitEthernet0/1/0
          10.1.1.2/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
        10.1.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
          10.2.1.0/24  Direct  0    0             D  10.2.1.2        GigabitEthernet0/2/0.1
          10.2.1.2/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0.1
        10.2.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0.1
          10.3.1.0/24  IBGP    255  0             RD 3.3.3.9         LDP LSP
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```
4. Enable IP multicast routing on the public network on PE1, the P, and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] multicast routing-enable
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure P.
   
   ```
   [*P] multicast routing-enable
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] multicast routing-enable
   ```
   ```
   [*PE2] commit
   ```
5. Configure multicast basic function.
   
   
   
   # Configure PIM-SM in the public network.
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] pim sm
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure P.
   
   ```
   [~P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] interface loopback 1
   ```
   ```
   [*P-LoopBack1] pim sm
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] pim sm
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure RP in the public network instance.
   
   ```
   [~P] pim
   ```
   ```
   [*P] c-bsr loopback 1
   ```
   ```
   [*P] c-rp loopback 1
   ```
   ```
   [*P] commit
   ```
   
   # Configure IGMP on the main interface to the Receiver.
   
   ```
   [~PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
6. Configure QinQ VLAN tag termination sub-interfaces to statically join multicast groups.
   
   
   ```
   [~PE1] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] igmp static-group 225.0.0.1 inc-step-mask 0.0.0.1 number 17 qinq pe-vid 1 ce-vid 1 to 2
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
7. Verify the configuration.
   
   
   
   After the configuration, run the **display pim vpn-instance vpna routing-table** command on PE1 to check the multicast routing-table information.
   
   Run the **display igmp-snooping qinq-port-info interface gigabitethernet 0/2/0.1** to check the multicast group information on the QinQ VLAN tag termination sub-interface.
   
   ```
   <PE1> display igmp-snooping qinq-port-info interface gigabitethernet 0/2/0.1
    Interface GigabitEthernet0/2/0.1, 17 Group(s)
    (Source,Group)                            PE-VID/CE-VID LiveTime           Flag
    -------------------------------------------------------------------------------
    (*,225.0.0.1)                             1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.2)                             1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.3)                             1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.4)                             1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.5)                             1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.6)                             1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.7)                             1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.8)                             1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.9)                             1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.10)                            1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.11)                            1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.12)                            1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.13)                            1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.14)                            1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.15)                            1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.16)                            1/1           --------           S--
                                              1/2           --------           S--
    (*,225.0.0.17)                            1/1           --------           S--
                                              1/2           --------           S--
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  router id 1.1.1.9
  #
  multicast routing-enable
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
    multicast routing-enable
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   pim sm
   igmp enable
   dcn
  #
  interface GigabitEthernet0/2/0.1
   ip binding vpn-instance vpna
   ip address 10.2.1.2 255.255.255.0
   encapsulation qinq-termination
   qinq termination pe-vid 1 ce-vid 1 to 2
   igmp static-group 225.0.0.1 inc-step-mask 0.0.0.1 number 17 qinq pe-vid 1 ce-vid 1 to 2
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
   pim sm
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   pim sm
  #
  bgp 100
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
   undo synchronization
   peer 3.3.3.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.9 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  router id 2.2.2.9
  #
  multicast routing-enable
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.17.1.1 255.255.255.0
   pim sm
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
   pim sm
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 172.17.1.0 0.0.0.255
  #
  pim
   c-bsr LoopBack1
   c-rp LoopBack1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  router id 3.3.3.9
  #
  multicast routing-enable
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
    multicast routing-enable
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.3.1.2 255.255.255.0
   pim sm
   undo dcn
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 172.17.1.2 255.255.255.0
   pim sm
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   pim sm
  #
  bgp 100
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.9 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    peer 10.3.1.1 as-number 65430
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 172.17.1.0 0.0.0.255
  #
  return
  ```