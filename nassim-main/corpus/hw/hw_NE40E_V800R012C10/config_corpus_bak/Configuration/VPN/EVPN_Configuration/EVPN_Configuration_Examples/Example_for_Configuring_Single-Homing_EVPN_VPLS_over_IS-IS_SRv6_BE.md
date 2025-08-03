Example for Configuring Single-Homing EVPN VPLS over IS-IS SRv6 BE
==================================================================

This section provides an example for configuring SRv6 BE to carry EVPN E-LAN services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001200848291__en-us_task_0176648717_fig_dc_vrp_srv6_cfg_all_002201), PE1, the P, and PE2 belong to the same AS and need to run IS-IS for IPv6 network connectivity. In addition, a bidirectional SRv6 BE path needs to be deployed between PE1 and PE2 to carry EVPN E-LAN services.

**Figure 1** EVPN VPLS over SRv6 BE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000002043457890.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title on PE1, the P, and PE2.
3. Configure an EVPN instance in BD mode on each PE and bind the EVPN instance to an access-side sub-interface.
4. Establish a BGP EVPN peer relationship between PEs.
5. Configure SRv6 BE on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* RD and RT of the EVPN instance
* BD ID: 100
* Names of locators on PE1: PE1\_ARG and PE1; names of locators on PE2: PE2\_ARG and PE2; dynamically generated opcodes
* Length of the locators PE1\_ARG and PE2\_ARG: 10 (as specified in the args parameter)

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
   
   Configure an IPv4 address for the loopback interface because the EVPN source address needs to be an IPv4 address. The preceding example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For detailed configurations, see Configuration Files.
2. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*PE1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface loopback1
   ```
   ```
   [*PE1-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE1-LoopBack1] commit
   ```
   ```
   [~PE1-LoopBack1] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] isis 1 
   ```
   ```
   [*P-isis-1] is-level level-1
   ```
   ```
   [*P-isis-1] cost-style wide
   ```
   ```
   [*P-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*P-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P-isis-1] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] interface loopback1
   ```
   ```
   [*P-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P-LoopBack1] commit
   ```
   ```
   [~P-LoopBack1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-1
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*PE2-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface loopback1
   ```
   ```
   [*PE2-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE2-LoopBack1] commit
   ```
   ```
   [~PE2-LoopBack1] quit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured:
   
   # Display IS-IS neighbor information. PE1 is used as an example.
   
   ```
   [~PE1] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
                            
     System Id     Interface         Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/1/0           0000.0000.0002.01  Up   8s       L1       64 
   
   Total Peer(s): 1
   ```
   
   # Display IS-IS routing table information. PE1 is used as an example.
   
   ```
   [~PE1] display isis route
   ```
   ```
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
   
    IPV6 Dest.        ExitInterface      NextHop                    Cost     Flags    
   --------------------------------------------------------------------------------
   2001:DB8:1::1/128  GE0/1/0            Direct                     10       D/-/L/-  
   2001:DB8:2::2/128  GE0/1/0            FE80::3A5D:67FF:FE31:307   10       A/-/-/-
   2001:DB8:3::3/128  GE0/1/0            FE80::3A5D:67FF:FE31:307   20       A/-/-/-  
   2001:DB8:10::/64   GE0/1/0            Direct                     20       D/-/L/-  
   2001:DB8:20::/64   GE0/1/0            FE80::3A5D:67FF:FE31:307   20       A/-/-/-  
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut, 
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
3. Configure an EVPN instance in BD mode on each PE and bind the EVPN instance to an access-side sub-interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] bridge-domain 100
   ```
   ```
   [*PE1-bd100] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-bd100] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] encapsulation dot1q vid 1
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] rewrite pop single
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] bridge-domain 100
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 3.3.3.3
   ```
   ```
   [*PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] route-distinguisher 200:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] bridge-domain 100
   ```
   ```
   [*PE2-bd100] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE2-bd100] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] encapsulation dot1q vid 1
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] rewrite pop single
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] bridge-domain 100
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
4. Establish a BGP EVPN peer relationship between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   ```
   ```
   [*PE1-bgp-af-evpn] quit
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
   [*PE2-bgp] router-id 3.3.3.3
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs and check whether BGP EVPN peer relationships have been established between the PEs. If the **Established** state is displayed in the command output, the BGP EVPN peer relationships have been established successfully.
5. Deploy SRv6 BE between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*PE1-segment-routing-ipv6] locator PE1_ARG ipv6-prefix 2001:DB8:12:: 64 args 10
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] isis 1
   [*PE1-isis-1] segment-routing ipv6 locator PE1_ARG auto-sid-disable
   [*PE1-isis-1] quit
   [*PE1] evpn vpn-instance evrf1 bd-mode
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 locator PE1_ARG unicast-locator PE1
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE1-evpn-instance-evrf1] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*PE2-segment-routing-ipv6] locator PE2_ARG ipv6-prefix 2001:DB8:22:: 64 args 10
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] isis 1
   [*PE2-isis-1] segment-routing ipv6 locator PE2_ARG auto-sid-disable
   [*PE2-isis-1] quit
   [*PE2] evpn vpn-instance evrf1 bd-mode
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 locator PE2_ARG unicast-locator PE2
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE2-evpn-instance-evrf1] quit
   [*PE2] commit
   ```
6. Verify the configuration.
   
   
   
   Run the **display segment-routing ipv6 local-sid** { **end-dt2u** | **end-dt2ul** | **end-dt2m** } **forwarding** command on each PE to check information about the SRv6 BE local SID table. PE1 is used as an example.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt2m forwarding
   ```
   ```
                       My Local-SID End.DT2M Forwarding Table
                        --------------------------------------
   SID             : 2001:DB8:12::400/118                         FuncType    : End.DT2M
   Bridge-domain ID: 100                                          
   LocatorName     : PE1_ARG                                      LocatorID   : 5
   Flavor          : NO-FLAVOR                                    SidCompress : NO
   UpdateTime      : 2023-05-10 01:46:05.713
   
   Total SID(s): 1
   ```
   
   Run the **display bgp evpn all routing-table** command on each PE. The command output shows the EVPN route sent from the peer end. PE1 is used as an example.
   
   ```
   [~PE1] display bgp evpn all routing-table
   ```
   ```
    Local AS number : 100
   
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    EVPN address family:
    Number of Inclusive Multicast Routes: 2
    Route Distinguisher: 100:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1                                    
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3                                
   
   
    EVPN-Instance evrf1:
    Number of Inclusive Multicast Routes: 2
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1                                    
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE1_ARG unicast-locator PE1 
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bridge-domain 100
   evpn binding vpn-instance evrf1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:1::1
   locator PE1_ARG ipv6-prefix 2001:DB8:12:: 64 args 10
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1_ARG auto-sid-disable
   #              
  # 
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
   rewrite pop single
   bridge-domain 100
  #
  interface LoopBack1
   ipv6 enable    
   ip address 1.1.1.1 255.255.255.255
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* P configuration file
  ```
  #
  sysname P
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   #              
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable    
   ip address 2.2.2.2 255.255.255.255
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 200:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE2_ARG unicast-locator PE2 
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bridge-domain 100
   evpn binding vpn-instance evrf1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:3::3
   locator PE2_ARG ipv6-prefix 2001:DB8:22:: 64 args 10
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2_ARG auto-sid-disable
   #              
  # 
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
   rewrite pop single
   bridge-domain 100
  #
  interface LoopBack1
   ipv6 enable    
   ip address 3.3.3.3 255.255.255.255
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 3.3.3.3
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
  # 
  evpn source-address 3.3.3.3
  #
  return
  ```