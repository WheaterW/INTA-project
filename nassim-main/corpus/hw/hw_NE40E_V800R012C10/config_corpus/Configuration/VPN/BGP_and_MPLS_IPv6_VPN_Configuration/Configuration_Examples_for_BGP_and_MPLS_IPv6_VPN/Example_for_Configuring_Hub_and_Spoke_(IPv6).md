Example for Configuring Hub and Spoke (IPv6)
============================================

In the networking of Hub and Spoke, an access control device is specified in the VPN, and users communicate with each other through the access control device.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369701__fig_dc_vrp_mpls-l3vpn-v6_cfg_208001), the communications between spoke-CEs is controlled by the hub-CE at a central site. The traffic between spoke-CEs is forwarded through the hub-CE, not only through the hub-PE.

**Figure 1** Hub-spoke networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, interface3, and interface4 in this example represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/1, respectively.


  
![](figure/en-us_image_0285386756.png)

#### Configuration Notes

When configuring hub and spoke, note the following:

* The import target and export target configured on a spoke-PE must be different.
* Two VPN instances (vpn\_in and vpn\_out) are created on the hub-PE. The VPN targets received by vpn\_in are the VPN targets advertised by the two spoke-PEs; the VPN targets advertised by vpn\_out are the VPN targets received by the two spoke-PEs and are different from the VPN targets received by vpn\_in.
* The hub-PE is configured to accept the routes whose AS number is repeated once in the AS\_Path attribute.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish MP-IBGP peer relationships between the hub-PE and spoke-PEs. (There is no need to establish the MP-IBGP peer relationship or exchange VPN route information between the two spoke-PEs.)
2. Create VPN instances and VPN targets on PEs.
3. Configure EBGP connections between CEs and PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR ID of each PE
* Names, RDs, and VPN targets of the VPN instances of the hub-PE and spoke-PEs

#### Procedure

1. Configure an IGP on the MPLS backbone network for the interworking between the hub-PE and spoke-PEs.
   
   
   
   In this example, OSPF is used as an IGP. For configuration details, see [Configuration Files](#EN-US_TASK_0172369701__example66634765214051) in this section.
   
   After the configuration, the OSPF neighbor relationships have been set up between the Hub-PE and Spoke-PEs. Run the **display ospf peer** command. The command output shows that the neighbor status is **Full**. Run the **display ip routing-table** command. The command output shows that the Hub-PE and Spoke-PEs have learnt the routes to the loopback interface of each other.
2. Configure basic MPLS functions and MPLS LDP, and set up LDP LSPs on the MPLS backbone network.
   
   
   
   For detailed configurations, see Configuration Files.
   
   After the preceding configurations are complete, LDP peer relationships are set up between the hub-PE and spoke-PEs. Run the **display mpls ldp session** command on Routers. The command output shows that the session status is **Operational**.
3. Configure VPN instances enabled with the IPv6 address family on the PEs and connect the CEs to PEs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The import target list of a VPN on the hub-PE must contain the export targets of all spoke-PEs.
   
   The export target list of another VPN on the hub-PE must contain the import targets of all spoke-PEs.
   
   # Configure Spoke-PE1.
   
   ```
   <Spoke-PE1> system-view
   ```
   ```
   [~Spoke-PE1] ip vpn-instance vpna
   ```
   ```
   [*Spoke-PE1-vpn-instance-vpna] ipv6-family
   ```
   ```
   [*Spoke-PE1-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
   ```
   ```
   [*Spoke-PE1-vpn-instance-vpna-af-ipv6] vpn-target 100:1 export-extcommunity
   ```
   ```
   [*Spoke-PE1-vpn-instance-vpna-af-ipv6] vpn-target 200:1 import-extcommunity
   ```
   ```
   [*Spoke-PE1-vpn-instance-vpna-af-ipv6] quit
   ```
   ```
   [*Spoke-PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*Spoke-PE1-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*Spoke-PE1-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*Spoke-PE1-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2 64
   ```
   ```
   [*Spoke-PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~Spoke-PE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Spoke-PE2.
   
   ```
   <Spoke-PE2> system-view
   ```
   ```
   [~Spoke-PE2] ip vpn-instance vpna
   ```
   ```
   [*Spoke-PE2-vpn-instance-vpna] ipv6-family
   ```
   ```
   [*Spoke-PE2-vpn-instance-vpna-af-ipv6] route-distinguisher 100:3
   ```
   ```
   [*Spoke-PE2-vpn-instance-vpna-af-ipv6] vpn-target 100:1 export-extcommunity
   ```
   ```
   [*Spoke-PE2-vpn-instance-vpna-af-ipv6] vpn-target 200:1 import-extcommunity
   ```
   ```
   [*Spoke-PE2-vpn-instance-vpna-af-ipv6] quit
   ```
   ```
   [*Spoke-PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*Spoke-PE2-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*Spoke-PE2-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*Spoke-PE2-GigabitEthernet0/1/0] ipv6 address 2001:db8:2::2 64
   ```
   ```
   [*Spoke-PE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~Spoke-PE2-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Hub-PE.
   
   ```
   <Hub-PE> system-view
   ```
   ```
   [~Hub-PE] ip vpn-instance vpn_in
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_in] ipv6-family
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_in-af-ipv6] route-distinguisher 100:21
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_in-af-ipv6] vpn-target 100:1 import-extcommunity
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_in-af-ipv6] quit
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_in] quit
   ```
   ```
   [*Hub-PE] ip vpn-instance vpn_out
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_out] ipv6-family
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_out-af-ipv6] route-distinguisher 100:22
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_out-af-ipv6] vpn-target 200:1 export-extcommunity
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_out-af-ipv6] quit
   ```
   ```
   [*Hub-PE-vpn-instance-vpn_out] quit
   ```
   ```
   [*Hub-PE] interface gigabitethernet 0/3/0
   ```
   ```
   [*Hub-PE-GigabitEthernet0/3/0] ip binding vpn-instance vpn_in
   ```
   ```
   [*Hub-PE-GigabitEthernet0/3/0] ipv6 enable
   ```
   ```
   [*Hub-PE-GigabitEthernet0/3/0] ipv6 address 2001:db8:3::2 64
   ```
   ```
   [*Hub-PE-GigabitEthernet0/3/0] quit
   ```
   ```
   [*Hub-PE] interface gigabitethernet 0/1/1
   ```
   ```
   [*Hub-PE-GigabitEthernet0/1/1] ip binding vpn-instance vpn_out
   ```
   ```
   [*Hub-PE-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*Hub-PE-GigabitEthernet0/1/1] ipv6 address 2001:db8:4::2 64
   ```
   ```
   [*Hub-PE-GigabitEthernet0/1/1] commit
   ```
   ```
   [~Hub-PE-GigabitEthernet0/1/1] quit
   ```
   
   # Assign an IP address to each interface on the CEs, as shown in [Figure 1](#EN-US_TASK_0172369701__fig_dc_vrp_mpls-l3vpn-v6_cfg_208001). For configuration details, see the configuration files.
   
   After completing the preceding configuration, run the **display ip vpn-instance verbose** command on PEs. The command output shows VPN instance configurations. Run the **ping ipv6 vpn-instance** *vpn-name ipv6-address* command on each PE. Each PE can successfully ping its connected CE.
4. Set up the EBGP peer relationships between the PEs and CEs to import VPN routes.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Configure Hub-PE to allow the AS number to be repeated once in the AS\_Path attribute to receive the routes advertised by Hub-CE.
   
   You do not need to configure the spoke-PEs to allow the AS number to be repeated once because the Router does not check the AS\_Path attributes in its received routes advertised by IBGP peers.
   
   # Configure Spoke-CE1.
   
   ```
   [~Spoke-CE1] interface loopback 1
   ```
   ```
   [*Spoke-CE1-Loopback1] ipv6 enable
   ```
   ```
   [*Spoke-CE1-Loopback1] ipv6 address 2001:db8:11::1 128
   ```
   ```
   [*Spoke-CE1-Loopback1] quit
   ```
   ```
   [*Spoke-CE1] bgp 65410
   ```
   ```
   [*Spoke-CE1-bgp] ipv6-family unicast
   ```
   ```
   [*Spoke-CE1-bgp-af-ipv6] peer 2001:db8:1::2 as-number 100
   ```
   ```
   [*Spoke-CE1-bgp-af-ipv6] network 2001:db8:11::1 128
   ```
   ```
   [*Spoke-CE1-bgp-af-ipv6] quit
   ```
   ```
   [*Spoke-CE1-bgp] quit
   ```
   ```
   [*Spoke-CE1] commit
   ```
   
   # Configure Spoke-PE1.
   
   ```
   [~Spoke-PE1] bgp 100
   ```
   ```
   [*Spoke-PE1-bgp] ipv6-family vpn-instance vpna
   ```
   ```
   [*Spoke-PE1-bgp-6-vpna] peer 2001:db8:1::1 as-number 65410
   ```
   ```
   [*Spoke-PE1-bgp-6-vpna] commit
   ```
   ```
   [~Spoke-PE1-bgp-6-vpna] quit
   ```
   ```
   [~Spoke-PE1-bgp] quit
   ```
   
   # Configure Spoke-CE2.
   
   ```
   [~Spoke-CE2] interface loopback 1
   ```
   ```
   [*Spoke-CE2-Loopback1] ipv6 enable
   ```
   ```
   [*Spoke-CE2-Loopback1] ipv6 address 2001:db8:12::2 128
   ```
   ```
   [*Spoke-CE2-Loopback1] quit
   ```
   ```
   [*Spoke-CE2] bgp 65420
   ```
   ```
   [*Spoke-CE2-bgp] ipv6-family unicast
   ```
   ```
   [*Spoke-CE2-bgp-af-ipv6] peer 2001:db8:2::2 as-number 100
   ```
   ```
   [*Spoke-CE2-bgp-af-ipv6] network 2001:db8:12::2 128
   ```
   ```
   [*Spoke-CE2-bgp-af-ipv6] quit
   ```
   ```
   [*Spoke-CE2-bgp] quit
   ```
   ```
   [*Spoke-CE2] commit
   ```
   
   # Configure Spoke-PE2.
   
   ```
   [~Spoke-PE2] bgp 100
   ```
   ```
   [*Spoke-PE2-bgp] ipv6-family vpn-instance vpna
   ```
   ```
   [*Spoke-PE2-bgp-6-vpna] peer 2001:db8:2::1 as-number 65420
   ```
   ```
   [*Spoke-PE2-bgp-6-vpna] quit
   ```
   ```
   [*Spoke-PE2-bgp] quit
   ```
   ```
   [*Spoke-PE2] commit
   ```
   
   # Configure Hub-CE.
   
   ```
   [~Hub-CE] interface loopback 1
   ```
   ```
   [*Hub-CE-Loopback1] ipv6 enable
   ```
   ```
   [*Hub-CE-Loopback1] ipv6 address 2001:db8:13::3 128
   ```
   ```
   [*Hub-CE-Loopback1] quit
   ```
   ```
   [*Hub-CE] bgp 65430
   ```
   ```
   [*Hub-CE-bgp] ipv6-family unicast
   ```
   ```
   [*Hub-CE-bgp-af-ipv6] peer 2001:db8:3::2 as-number 100
   ```
   ```
   [*Hub-CE-bgp-af-ipv6] peer 2001:db8:4::2 as-number 100
   ```
   ```
   [*Hub-CE-bgp-af-ipv6] network 2001:db8:13::3 128
   ```
   ```
   [*Hub-CE-bgp-af-ipv6] quit
   ```
   ```
   [*Hub-CE-bgp] quit
   ```
   ```
   [*Hub-CE] commit
   ```
   
   # Configure Hub-PE.
   
   ```
   [~Hub-PE] bgp 100
   ```
   ```
   [*Hub-PE-bgp] ipv6-family vpn-instance vpn_in
   ```
   ```
   [*Hub-PE-bgp-6-vpn_in] peer 2001:db8:3::1 as-number 65430
   ```
   ```
   [*Hub-PE-bgp-6-vpn_in] quit
   ```
   ```
   [*Hub-PE-bgp] ipv6-family vpn-instance vpn_out
   ```
   ```
   [*Hub-PE-bgp-6-vpn_out] peer 2001:db8:4::1 as-number 65430
   ```
   ```
   [*Hub-PE-bgp-6-vpn_out] peer 2001:db8:4::1 allow-as-loop 1
   ```
   ```
   [*Hub-PE-bgp-6-vpn_out] quit
   ```
   ```
   [*Hub-PE-bgp] quit
   ```
   ```
   [*Hub-PE] commit
   ```
   
   After completing the configurations, run the **display bgp vpnv6 all peer** command on the PEs. The command output shows that BGP peer relationships have been established between PEs and CEs.
5. Set up MP-IBGP peer relationships between the PEs.
   
   
   
   # Configure Spoke-PE1.
   
   ```
   [~Spoke-PE1] bgp 100
   ```
   ```
   [*Spoke-PE1-bgp] peer 2.2.2.9 as-number 100
   ```
   ```
   [*Spoke-PE1-bgp] peer 2.2.2.9 connect-interface loopback 1
   ```
   ```
   [*Spoke-PE1-bgp] ipv6-family vpnv6
   ```
   ```
   [*Spoke-PE1-bgp-af-vpnv6] peer 2.2.2.9 enable
   ```
   ```
   [*Spoke-PE1-bgp-af-vpnv6] commit
   ```
   ```
   [~Spoke-PE1-bgp-af-vpnv6] quit
   ```
   
   # Configure Spoke-PE2.
   
   ```
   [~Spoke-PE2] bgp 100
   ```
   ```
   [*Spoke-PE2-bgp] peer 2.2.2.9 as-number 100
   ```
   ```
   [*Spoke-PE2-bgp] peer 2.2.2.9 connect-interface loopback 1
   ```
   ```
   [*Spoke-PE2-bgp] ipv6-family vpnv6
   ```
   ```
   [*Spoke-PE2-bgp-af-vpnv6] peer 2.2.2.9 enable
   ```
   ```
   [*Spoke-PE2-bgp-af-vpnv6] commit
   ```
   ```
   [~Spoke-PE2-bgp-af-vpnv6] quit
   ```
   
   # Configure Hub-PE.
   
   ```
   [~Hub-PE] bgp 100
   ```
   ```
   [*Hub-PE-bgp] peer 1.1.1.9 as-number 100
   ```
   ```
   [*Hub-PE-bgp] peer 1.1.1.9 connect-interface loopback 1
   ```
   ```
   [*Hub-PE-bgp] peer 3.3.3.9 as-number 100
   ```
   ```
   [*Hub-PE-bgp] peer 3.3.3.9 connect-interface loopback 1
   ```
   ```
   [*Hub-PE-bgp] ipv6-family vpnv6
   ```
   ```
   [*Hub-PE-bgp-af-vpnv6] peer 1.1.1.9 enable
   ```
   ```
   [*Hub-PE-bgp-af-vpnv6] peer 3.3.3.9 enable
   ```
   ```
   [*Hub-PE-bgp-af-vpnv6] commit
   ```
   ```
   [~Hub-PE-bgp-af-vpnv6] quit
   ```
   
   After completing the configuration, run the **display bgp peer** or **display bgp vpnv6 all peer** command on the PEs. The command output shows that the BGP peer relationships have been established between the PEs.
6. Verify the configuration.
   
   
   
   After completing the preceding configuration, configure spoke-CEs to ping each other. The command output shows that the Spoke-CEs can successfully ping each other.
   
   The following example uses the command output on Spoke-CE1.
   
   ```
   <Spoke-CE1> ping ipv6 -a 2001:db8:11::1 2001:db8:12::2
   ```
   ```
     PING 2001:db8:12::2 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8:12::2
       bytes=56 Sequence=1 hop limit=59 time=7 ms
       Reply from 2001:db8:12::2
       bytes=56 Sequence=2 hop limit=59 time=3 ms
       Reply from 2001:db8:12::2
       bytes=56 Sequence=3 hop limit=59 time=3 ms
       Reply from 2001:db8:12::2
       bytes=56 Sequence=4 hop limit=59 time=3 ms
       Reply from 2001:db8:12::2
       bytes=56 Sequence=5 hop limit=59 time=3 ms
   
     ---2001:db8:12::2 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=3/3/7 ms
   ```
   
   Run the **display bgp ipv6 routing-table** command on each spoke-CE. The command output shows that repetitive AS numbers are contained in the AS\_Path attributes of the BGP routes destined for peer spoke-CEs.
   
   The following example uses the command output on Spoke-CE1.
   
   ```
   <Spoke-CE1> display bgp ipv6 routing-table
   ```
   ```
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    Total Number of Routes: 3
    *>    Network  : 2001:db8:11::1                           PrefixLen : 128
          NextHop  : ::                                       LocPrf    :
          MED      : 0                                        PrefVal   : 0
          Label    :
          Path/Ogn :  i
    *>    Network  : 2001:db8:12::2                           PrefixLen : 128
          NextHop  : 2001:db8:1::2                            LocPrf    :
          MED      :                                          PrefVal   : 0
          Label    :
          Path/Ogn : 100 65430 100 65420i
    *>    Network  : 2001:db8:13::3                           PrefixLen : 128
          NextHop  : 2001:db8:1::2                            LocPrf    :
          MED      :                                          PrefVal   : 0
          Label    :
          Path/Ogn : 100 65430i
   ```

#### Configuration Files

* Spoke-CE1 configuration file
  
  ```
  #
  sysname Spoke-CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:11::1/128
  #
  bgp 65410
   router-id 1.1.1.1
   peer 2001:db8:1::2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    network 2001:db8:11::1 128
    peer 2001:db8:1::2 enable
  #
  return
  ```
* Spoke-PE1 configuration file
  
  ```
  #
  sysname Spoke-PE1
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 200:1 import-extcommunity
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
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
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
   ipv6-family vpnv6
    policy vpn-target
    peer 2.2.2.9 enable
   #
   ipv6-family vpn-instance vpna
    peer 2001:db8:1::1 as-number 65410
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 10.2.1.0 0.0.0.255
  #
  return
  ```
* Spoke-PE2 configuration file
  
  ```
  #
  sysname Spoke-PE2
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 100:3
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 200:1 import-extcommunity
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
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
  #
  bgp 100
   peer 2.2.2.9 as-number 100
   peer 2.2.2.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.9 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 2.2.2.9 enable
   #
   ipv6-family vpn-instance vpna
    peer 2001:db8:2::1 as-number 65420
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* Spoke-CE2 configuration file
  
  ```
  #
  sysname Spoke-CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:12::2/128
  #
  bgp 65420
   router-id 3.3.3.3
   peer 2001:db8:2::2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    network 2001:db8:12::2 128
    peer 2001:db8:2::2 enable
  #
  return
  ```
* Hub-CE configuration file
  
  ```
  #
  sysname Hub-CE
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:13::3/128
  #
  bgp 65430
   router-id 2.2.2.2
   peer 2001:db8:3::2 as-number 100
   peer 2001:db8:4::2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    network 2001:db8:13::3 128
    peer 2001:db8:3::2 enable
    peer 2001:db8:4::2 enable
  #
  return
  ```
* Hub-PE configuration file
  
  ```
  #
  sysname Hub-PE
  #
  ip vpn-instance vpn_in
   ipv6-family
    route-distinguisher 100:21
    apply-label per-instance
    vpn-target 100:1 import-extcommunity
  #
  ip vpn-instance vpn_out
   ipv6-family
    route-distinguisher 100:22
    apply-label per-instance
    vpn-target 200:1 export-extcommunity
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip binding vpn-instance vpn_in
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance vpn_out
   ipv6 enable
   ipv6 address 2001:db8:4::2/64
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  bgp 100
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
    peer 3.3.3.9 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 1.1.1.9 enable
    peer 3.3.3.9 enable
   #
   ipv6-family vpn-instance vpn_in
    peer 2001:db8:3::1 as-number 65430
   #
   ipv6-family vpn-instance vpn_out
    peer 2001:db8:4::1 as-number 65430
    peer 2001:db8:4::1 allow-as-loop
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 10.2.1.0 0.0.0.255
    network 10.1.1.0 0.0.0.255
  #
  return
  ```