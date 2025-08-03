Example for Configuring VE Access Through an EVPN VPLS over SRv6 BE Path
========================================================================

This section provides an example for configuring an SRv6 BE path to carry EVPN E-LAN services for PPPoE users to implement BRAS user access.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0212448010__fig25401857173015), PE1, P, and PE2 are in the same AS and run IS-IS to implement IPv6 network connectivity. A bidirectional SRv6 BE path is established between PE1 and PE2 to carry EVPN E-LAN services. The BRAS user accesses the Internet in PPPoE mode through the VE 1/0/1.1 sub-interface on PE2. VE 0/1/0 is used to terminate the VLL, and VE 0/1/1 functions as a BAS interface to provide authentication for the access user.

**Figure 1** Configuring VE access through an EVPN VPLS over SRv6 BE path![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0212478889.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address for each interface.
2. Enable IS-IS, configure a level, and specify a network entity on each device.
3. Configure an EVPN instance in BD mode on each PE and bind the EVPN instance to an access-side sub-interface.
4. Establish a BGP EVPN peer relationship between PEs.
5. Configure an SRv6 BE path on each PE.
6. Configure BRAS access on PE2 and configure VE 0/1/1.1 as the BAS interface.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* RD and RT values of the EVPN instance: 100:1 and 1:1
* BD ID: 100
* Names of SID node route locators on PE1: PE1\_ARG, PE1; names of SID node route locators on PE2: PE2\_ARG, PE2; dynamically generated opcodes
* Length of the SID node route locators PE1\_ARG and PE2\_ARG: 10 (as specified in the args parameter)
* VE-group number
* Virtual template number
* RADIUS authentication and accounting schemes and their names
* RADIUS server group name, and IP addresses and port numbers of the RADIUS authentication and accounting servers
* Local address pool name
* Domain name

#### Procedure

1. Enable IPv6 forwarding on each interface and configure an IPv6 address for each interface.
   
   Configure an IPv4 address for the loopback interface because the EVPN source address needs to be an IPv4 address. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see the configuration file.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:db8:10::1 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:db8:1::1 64
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
2. Configure IS-IS.
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   [*PE1-isis-1] is-level level-1
   [*PE1-isis-1] cost-style wide
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   [*PE1-isis-1] ipv6 enable topology ipv6
   [*PE1-isis-1] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/1/0] commit
   [~PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] isis ipv6 enable 1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] isis 1
   [*P-isis-1] is-level level-1
   [*P-isis-1] cost-style wide
   [*P-isis-1] network-entity 10.0000.0000.0002.00
   [*P-isis-1] ipv6 enable topology ipv6
   [*P-isis-1] quit
   [*P] interface gigabitethernet 0/1/0
   [*P-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*P-GigabitEthernet0/1/0] commit
   [~P-GigabitEthernet0/1/0] quit
   [*P] interface gigabitethernet 0/2/0
   [*P-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*P-GigabitEthernet0/2/0] commit
   [~P-GigabitEthernet0/2/0] quit
   [*P] interface loopback1
   [*P-LoopBack1] isis ipv6 enable 1
   [*P-LoopBack1] commit
   [~P-LoopBack1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   [*PE2-isis-1] is-level level-1
   [*PE2-isis-1] cost-style wide
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   [*PE2-isis-1] ipv6 enable topology ipv6
   [*PE2-isis-1] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/1/0] commit
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] isis ipv6 enable 1
   [*PE2-LoopBack1] commit
   [~PE2-LoopBack1] quit
   ```
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured:
   
   # Display IS-IS neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
                             Peer information for ISIS(1) 
                             
     System Id     Interface         Circuit Id        State HoldTime Type     PRI 
   -------------------------------------------------------------------------------- 
   0000.0000.0002  GE0/1/0           0000.0000.0002.01  Up   8s       L1       64  
    
   Total Peer(s): 1
   ```
   
   # Display IS-IS routing table information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis route
                            Route information for ISIS(1) 
                            ----------------------------- 
    
                           ISIS(1) Level-1 Forwarding Table 
                           -------------------------------- 
    
    IPV6 Dest.        ExitInterface      NextHop                    Cost     Flags     
   -------------------------------------------------------------------------------- 
   2001:db8:1::/64    GE0/1/0            Direct                     10       D/-/L/-   
   2001:db8:2::/64    GE0/1/0            FE80::3A5D:67FF:FE31:307   10       A/-/-/- 
   2001:db8:3::/64    GE0/1/0            FE80::3A5D:67FF:FE31:307   20       A/-/-/-   
   2001:db8:10::/64   GE0/1/0            Direct                     20       D/-/L/-   
   2001:db8:20::/64   GE0/1/0            FE80::3A5D:67FF:FE31:307   20       A/-/-/-   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,  
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
3. Configure an EVPN instance in BD mode on each PE and bind the EVPN instance to an access-side sub-interface.
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 bd-mode
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   [*PE1-evpn-instance-evrf1] quit
   [*PE1] evpn source-address 1.1.1.1
   [*PE1] bridge-domain 100
   [*PE1-bd100] evpn binding vpn-instance evrf1
   [*PE1-bd100] quit
   [*PE1] evpn vpn-instance evrf2 bd-mode
   [*PE1-evpn-instance-evrf2] route-distinguisher 200:1
   [*PE1-evpn-instance-evrf2] vpn-target 2:2
   [*PE1-evpn-instance-evrf2] quit
   [*PE1] bridge-domain 200
   [*PE1-bd200] evpn binding vpn-instance evrf2
   [*PE1-bd200] quit
   [*PE1] interface gigabitethernet0/2/0.1 mode l2
   [*PE1-Gigabitethernet0/2/0.1] encapsulation dot1q vid 100
   [*PE1-Gigabitethernet0/2/0.1] rewrite pop single
   [*PE1-Gigabitethernet0/2/0.1] bridge-domain 100
   [*PE1-Gigabitethernet0/2/0.1] quit
   [*PE1] commit
   [~PE1] interface gigabitethernet0/2/0.2 mode l2
   [*PE1-Gigabitethernet0/2/0.2] encapsulation dot1q vid 200
   [*PE1-Gigabitethernet0/2/0.2] rewrite pop single
   [*PE1-Gigabitethernet0/2/0.2] bridge-domain 200
   [*PE1-Gigabitethernet0/2/0.2] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 bd-mode
   [*PE2-evpn-instance-evrf1] route-distinguisher 100:1
   [*PE2-evpn-instance-evrf1] vpn-target 1:1
   [*PE2-evpn-instance-evrf1] quit
   [*PE2] evpn source-address 3.3.3.3
   [*PE2] bridge-domain 100
   [*PE2-bd100] evpn binding vpn-instance evrf1
   [*PE2-bd100] quit
   [*PE2] evpn vpn-instance evrf2 bd-mode
   [*PE2-evpn-instance-evrf2] route-distinguisher 200:1
   [*PE2-evpn-instance-evrf2] vpn-target 2:2
   [*PE2-evpn-instance-evrf2] quit
   [*PE2] bridge-domain 200
   [*PE2-bd200] evpn binding vpn-instance evrf2
   [*PE2-bd200] quit
   [*PE2] commit
   [~PE2] interface virtual-ethernet0/1/0
   [*PE2-Virtual-Ethernet0/1/0] ve-group 1 l2-terminate
   [*PE2-Virtual-Ethernet0/1/0] quit
   [*PE2] commit
   [~PE2] interface virtual-ethernet0/1/1
   [*PE2-Virtual-Ethernet0/1/1] ve-group 1 l3-access
   [*PE2-Virtual-Ethernet0/1/1] quit
   [*PE2] commit
   [~PE2] interface virtual-ethernet0/1/0.1 mode l2
   [*PE2-Virtual-Ethernet0/1/0.1] encapsulation dot1q vid 100
   [*PE2-Virtual-Ethernet0/1/0.1] bridge-domain 100
   [*PE2-Virtual-Ethernet0/1/0.1] quit
   [~PE2] interface virtual-ethernet0/1/0.2 mode l2
   [*PE2-Virtual-Ethernet0/1/0.2] encapsulation dot1q vid 200
   [*PE2-Virtual-Ethernet0/1/0.2] bridge-domain 200
   [*PE2-Virtual-Ethernet0/1/0.2] quit
   [*PE2] commit
   ```
4. Establish a BGP EVPN peer relationship between PEs.
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [*PE1-bgp] route-id 1.1.1.1
   [*PE1-bgp] peer 2001:db8:3::3 as-number 100
   [*PE1-bgp] peer 2001:db8:3::3 connect-interface loopback 1
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:db8:3::3 enable
   [*PE1-bgp-af-evpn] peer 2001:db8:3::3 advertise encap-type srv6
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [*PE2-bgp] route-id 3.3.3.3
   [*PE2-bgp] peer 2001:db8:1::1 as-number 100
   [*PE2-bgp] peer 2001:db8:1::1 connect-interface loopback 1
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:db8:1::1 enable
   [*PE2-bgp-af-evpn] peer 2001:db8:1::1 advertise encap-type srv6
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] quit
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs and check whether a BGP EVPN peer relationship has been established between the PEs. If the **Established** state is displayed in the command output, the BGP EVPN peer relationship has been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer   
   BGP local router ID : 1.1.1.1  
   Local AS number : 100  
   Total number of peers : 1                 Peers in established state : 1    
   Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv   
   3.3.3.3         4         100        9        9     0 00:00:02 Established        5
   ```
5. Establish an SRv6 BE tunnel between PEs.
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:db8:1::1
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:db8:11:: 64
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] locator PE1_ARG ipv6-prefix 2001:db8:12:: 64 args 10
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] isis 1
   [*PE1-isis-1] segment-routing ipv6 locator PE1
   [*PE1-isis-1] segment-routing ipv6 locator PE1_ARG auto-sid-disable
   [*PE1-isis-1] quit
   [*PE1] evpn vpn-instance evrf1 bd-mode
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 locator PE1_ARG unicast-locator PE1
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE1-evpn-instance-evrf1] quit
   [*PE1] evpn vpn-instance evrf2 bd-mode
   [*PE1-evpn-instance-evrf2] segment-routing ipv6 locator PE1_ARG unicast-locator PE1
   [*PE1-evpn-instance-evrf2] segment-routing ipv6 best-effort
   [*PE1-evpn-instance-evrf2] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:db8:3::3
   [*PE2-segment-routing-ipv6] locator PE2 ipv6-prefix 2001:db8:21:: 64
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] locator PE2_ARG ipv6-prefix 2001:db8:22:: 64 args 10
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] isis 1
   [*PE2-isis-1] segment-routing ipv6 locator PE2
   [*PE2-isis-1] segment-routing ipv6 locator PE2_ARG auto-sid-disable
   [*PE2-isis-1] quit
   [*PE2] evpn vpn-instance evrf1 bd-mode
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 locator PE2_ARG unicast-locator PE2
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE2-evpn-instance-evrf1] quit
   [*PE2] evpn vpn-instance evrf2 bd-mode
   [*PE2-evpn-instance-evrf2] segment-routing ipv6 locator PE2_ARG unicast-locator PE2
   [*PE2-evpn-instance-evrf2] segment-routing ipv6 best-effort
   [*PE2-evpn-instance-evrf2] quit
   [*PE2] commit
   ```
6. Configure BRAS access on PE2 and configure VE 0/1/1.1 as the BAS interface.
   
   # Configure a virtual template.
   
   ```
   [~PE2] interface virtual-template 1
   [*PE2-Virtual-Template1] ppp authentication-mode chap
   [*PE2-Virtual-Template1] quit
   [*PE2] commit
   ```
   
   # Configure an authentication scheme.
   
   ```
   [~PE2] aaa
   [~PE2-aaa] authentication-scheme auth1
   [*PE2-aaa-authen-auth1] authentication-mode radius
   [*PE2-aaa-authen-auth1] quit
   [*PE2-aaa] commit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~PE2-aaa] accounting-scheme acct1
   [*PE2-aaa-accounting-acct1] accounting-mode radius
   [*PE2-aaa-accounting-acct1] quit
   [*PE2-aaa] quit
   [*PE2] commit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~PE2] radius-server group rd1
   [*PE2-radius-rd1] radius-server authentication 192.168.7.249 1812
   [*PE2-radius-rd1] radius-server accounting 192.168.7.249 1813
   [*PE2-radius-rd1] commit
   [~PE2-radius-rd1] radius-server type plus11
   [~PE2-radius-rd1] radius-server shared-key itellin
   [*PE2-radius-rd1] commit
   [~PE2-radius-rd1] quit
   ```
   
   # Configure a local address pool.
   
   ```
   [~PE2] ip pool pool1 bas local
   [*PE2-ip-pool-pool1] gateway 172.30.1.1 255.255.255.0
   [*PE2-ip-pool-pool1] commit
   [~PE2-ip-pool-pool1] section 0 172.30.1.2 172.30.1.200
   [~PE2-ip-pool-pool1] dns-server 192.168.7.252
   [*PE2-ip-pool-pool1] commit
   [~PE2-ip-pool-pool1] quit
   ```
   
   # Configure a domain named **isp1**.
   
   ```
   [~PE2] aaa
   [*PE2-aaa] domain isp1
   [*PE2-aaa-domain-isp1] commit
   [~PE2-aaa-domain-isp1] ip-pool pool1
   [~PE2-aaa-domain-isp1] authentication-scheme auth1
   [*PE2-aaa-domain-isp1] accounting-scheme acct1
   [*PE2-aaa-domain-isp1] radius-server group rd1
   [*PE2-aaa-domain-isp1] commit
   [~PE2-aaa-domain-isp1] quit
   [~PE2-aaa] quit
   ```
   
   # Bind the virtual template to VE 0/1/1.1.
   
   ```
   [~PE2] interface virtual-ethernet0/1/1.1
   [*PE2-Virtual-Ethernet0/1/1.1] commit
   [~PE2-Virtual-Ethernet0/1/1.1] pppoe-server bind virtual-template 1
   [*PE2-Virtual-Ethernet0/1/1.1] commit
   ```
   
   # Configure a BAS interface.
   
   ```
   [~PE2-Virtual-Ethernet0/1/1.1] user-vlan 1 2 qinq 100
   [~PE2-Virtual-Ethernet0/1/1.1-vlan-1-2-QinQ-100] quit
   [~PE2-Virtual-Ethernet0/1/1.1] bas
   [~PE2-Virtual-Ethernet0/1/1.1-bas] access-type layer2-subscriber
   [*PE2-Virtual-Ethernet0/1/1.1-bas] authentication-method ppp
   [*PE2-Virtual-Ethernet0/1/1.1-bas] commit
   [~PE2-Virtual-Ethernet0/1/1.1-bas] quit
   [~PE2-Virtual-Ethernet0/1/1.1] quit
   ```
   
   # Configure an upstream interface.
   
   ```
   [~PE2] interface GigabitEthernet 0/2/0
   [~PE2-GigabitEthernet0/2/0] ip address 10.1.1.2 255.255.255.0
   [*PE2-GigabitEthernet0/2/0] commit
   [~PE2-GigabitEthernet0/2/0] quit
   ```
7. Verify the configuration.
   
   Run the **[**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid)** { ****end-dt2u**** | ****end-dt2ul**** | ****end-dt2m**** } **[**forwarding**](cmdqueryname=forwarding)** command on PEs to check information about the local SID table of an SRv6 VE interface. The following example uses the command output on PE1.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt2m forwarding
                       My Local-SID End.DT2M Forwarding Table 
                        -------------------------------------- 
   SID             : 2001:db8:12::400/118                         FuncType : End.DT2M 
   Bridge-domain ID: 100                                           
   LocatorName     : PE1_ARG                                      LocatorID: 5 
   Flavor          : NO-FLAVOR                                    SidCompress : NO 
   UpdateTime      : 2023-05-10 01:46:05.713
   
   Total SID(s): 1
   
   [~PE1] display segment-routing ipv6 local-sid end-dt2u forwarding 
                        My Local-SID End.DT2U Forwarding Table 
                       -------------------------------------- 
    
   SID             : 2001:db8:11::3D/128                          FuncType : End.DT2U 
   Bridge-domain ID: 100                                          
   LocatorName     : PE1                                          LocatorID: 4 
   Flavor          : NO-FLAVOR                                    SidCompress : NO 
   UpdateTime      : 2023-05-10 01:46:05.713
   
   Total SID(s): 1
   ```
   
   Run the **[**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table)** command on PEs. The command output shows the EVPN route sent from the peer device. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn all routing-table
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
    *>i   0:32:3.3.3.3                                           2001:db8:3::3                                 
    
    
    EVPN-Instance evrf1: 
    Number of Inclusive Multicast Routes: 2 
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop 
    *>    0:32:1.1.1.1                                           127.0.0.1                                     
    *>i   0:32:3.3.3.3                                           2001:db8:3::3
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
  evpn vpn-instance evrf2 bd-mode  
   route-distinguisher 200:1  
   segment-routing ipv6 best-effort  
   segment-routing ipv6 locator PE1_ARG unicast-locator PE1   
   vpn-target 2:2 export-extcommunity  
   vpn-target 2:2 import-extcommunity 
  #
  bridge-domain 100
   evpn binding vpn-instance evrf1
  #
  bridge-domain 200
   evpn binding vpn-instance evrf2
  #
  segment-routing ipv6
   encapsulation source-address 2001:db8:1::1 
   locator PE1 ipv6-prefix 2001:db8:11:: 64 
   locator PE1_ARG ipv6-prefix 2001:db8:12:: 64 args 10 
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00 
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1
   segment-routing ipv6 locator PE1_ARG auto-sid-disable 
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:10::1/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 100
  #
  interface GigabitEthernet0/2/0.2 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 200
  #
  interface LoopBack1
   ipv6 enable
   ip address 1.1.1.1 255.255.255.255
   ipv6 address 2001:db8:1::1/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 1.1.1.1
   peer 2001:db8:3::3 as-number 100
   peer 2001:db8:3::3 connect-interface LoopBack1
  #
  ipv4-family unicast
   undo synchronization
   #               
   l2vpn-family evpn 
    policy vpn-target 
    peer 2001:db8:3::3 enable 
    peer 2001:db8:3::3 advertise encap-type srv6 
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
  interface GigabitEthernet0/1/0
   undo shutdown   
   ipv6 enable     
   ipv6 address 2001:db8:10::2/64 
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/0 
   undo shutdown   
   ipv6 enable     
   ipv6 address 2001:db8:20::1/64 
   isis ipv6 enable 1 
  # 
  interface LoopBack1 
   ipv6 enable     
   ip address 2.2.2.2 255.255.255.255 
   ipv6 address 2001:db8:2::2/64 
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
   route-distinguisher 100:1 
   segment-routing ipv6 best-effort 
   segment-routing ipv6 locator PE2_ARG unicast-locator PE2  
   vpn-target 1:1 export-extcommunity 
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode 
   route-distinguisher 200:1 
   segment-routing ipv6 best-effort 
   segment-routing ipv6 locator PE2_ARG unicast-locator PE2  
   vpn-target 2:2 export-extcommunity 
   vpn-target 2:2 import-extcommunity 
  # 
  radius-server group rd1
   radius-server shared-key %^%#oNUw%i-|"WcBgt8=fSVID7F<=K_N+.(ip[H\:a{D%^%#
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server type plus11
   radius-server traffic-unit kbyte
  #    
  ip pool pool1 bas local
   gateway 172.30.1.1 255.255.255.0
   section 0 172.30.1.2 172.30.1.200
   dns-server 192.168.7.252
  # 
  bridge-domain 100 
   evpn binding vpn-instance evrf1
  # 
  bridge-domain 200 
   evpn binding vpn-instance evrf2
  #
  aaa
   #
   authentication-scheme auth1
   accounting-scheme acct1
   #
   domain isp1
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    ip-pool pool1
  #                
  segment-routing ipv6 
   encapsulation source-address 2001:db8:3::3 
   locator PE2 ipv6-prefix 2001:db8:21:: 64 
   locator PE2_ARG ipv6-prefix 2001:db8:22:: 64 args 10 
  #                
  isis 1           
   is-level level-1 
   cost-style wide 
   network-entity 10.0000.0000.0003.00 
   #               
   ipv6 enable topology ipv6 
   segment-routing ipv6 locator PE2  
   segment-routing ipv6 locator PE2_ARG auto-sid-disable 
  #  
  interface Virtual-Template1
   ppp authentication-mode chap
  #
  interface GigabitEthernet0/1/0 
   undo shutdown   
   ipv6 enable     
   ipv6 address 2001:db8:20::2/64 
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/0 
   undo shutdown 
   ip address 10.1.1.2 255.255.255.0
  # 
  interface Virtual-Ethernet0/1/0
   ve-group 1 l2-terminate
  #  
  interface Virtual-Ethernet0/1/0.1 mode l2
   encapsulation dot1q vid 100  
   bridge-domain 100 
  #  
  interface Virtual-Ethernet0/1/0.2 mode l2
   encapsulation dot1q vid 200  
   bridge-domain 200 
  #
  interface Virtual-Ethernet0/1/1
   ve-group 1 l3-access
  #
  interface Virtual-Ethernet0/1/1.1
   user-vlan 1 2 qinq 100
   bas
    #
    access-type layer2-subscriber
  #
  interface LoopBack1 
   ipv6 enable     
   ip address 3.3.3.3 255.255.255.255 
   ipv6 address 2001:db8:3::3/64 
   isis ipv6 enable 1 
  #           
  bgp 100          
   router-id 3.3.3.3 
   peer 2001:db8:1::1 as-number 100 
   peer 2001:db8:1::1 connect-interface LoopBack1 
   #               
   ipv4-family unicast 
    undo synchronization 
   #               
   l2vpn-family evpn 
    policy vpn-target 
    peer 2001:db8:1::1 enable 
    peer 2001:db8:1::1 advertise encap-type srv6 
  #  
  evpn source-address 3.3.3.3 
  # 
  return
  ```