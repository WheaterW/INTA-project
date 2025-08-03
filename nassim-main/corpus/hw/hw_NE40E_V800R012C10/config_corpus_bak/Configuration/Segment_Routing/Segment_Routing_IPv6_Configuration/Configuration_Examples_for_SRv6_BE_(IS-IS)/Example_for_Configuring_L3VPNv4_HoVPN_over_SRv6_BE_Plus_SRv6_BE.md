Example for Configuring L3VPNv4 HoVPN over SRv6 BE Plus SRv6 BE
===============================================================

This section provides an example for configuring L3VPNv4 HoVPN over SRv6 BE plus SRv6 BE.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0226968187__fig_dc_vrp_srv6_cfg_all_001101):

* The UPE, SPE, and NPE all belong to AS 100. They need to run IS-IS to implement IPv6 network connectivity.
* The UPE, SPE, and NPE all belong to IS-IS process 1.

It is required that bidirectional SRv6 BE paths be established between the UPE and NPE to carry L3VPNv4 services.

**Figure 1** L3VPNv4 HoVPN over SRv6 BE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0226997663.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on the UPE, SPE, and NPE.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity on the UPE, SPE, and NPE.
3. Establish an EBGP peer relationship between the UPE and CE1 and another one between the NPE and CE2.
4. Establish an MP-IBGP peer relationship between the UPE and SPE and another one between the NPE and SPE.
5. Configure SRv6 on the UPE, SPE, and NPE.
6. Specify the UPE as the peer of the SPE and configure the SPE to advertise the default route to the UPE.
7. Configure the SPE to advertise regenerated routes to the NPE.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on the UPE, SPE, and NPE
* IS-IS process ID of the UPE, SPE, and NPE
* IS-IS level of the UPE, SPE, and NPE
* VPN instance name, RD, and RT on the SPE and NPE

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of the UPE. The configurations of other devices are similar to the configuration of the UPE. For configuration details, see [Configuration Files](#EN-US_TASK_0226968187__example764102717246) in this section.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname UPE
   [*HUAWEI] commit
   [~UPE] interface GigabitEthernet 0/1/0
   [~UPE-GigabitEthernet0/1/0] ipv6 enable
   [*UPE-GigabitEthernet0/1/0] ipv6 address 2001:DB8:2001::1 96
   [*UPE-GigabitEthernet0/1/0] quit
   [*UPE] interface loopback1
   [*UPE-LoopBack1] ipv6 enable
   [*UPE-LoopBack1] ipv6 address 2001:DB8:1::1/128
   [*UPE-LoopBack1] commit
   [~UPE-LoopBack1] quit
   ```
2. Configure IS-IS.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] isis 1
   [*UPE-isis-1] is-level level-1
   [*UPE-isis-1] cost-style wide
   [*UPE-isis-1] network-entity 10.0000.0000.0001.00
   [*UPE-isis-1] ipv6 enable topology ipv6
   [*UPE-isis-1] quit
   [*UPE] interface GigabitEthernet 0/1/0
   [*UPE-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*UPE-GigabitEthernet0/1/0] quit
   [*UPE] interface loopback1
   [*UPE-LoopBack1] isis ipv6 enable 1
   [*UPE-LoopBack1] commit
   [~UPE-LoopBack1] quit
   ```
   
   # Configure the SPE.
   
   ```
   [~SPE] isis 1 
   [*SPE-isis-1] is-level level-1
   [*SPE-isis-1] cost-style wide
   [*SPE-isis-1] network-entity 10.0000.0000.0002.00
   [*SPE-isis-1] ipv6 enable topology ipv6
   [*SPE-isis-1] quit
   [*SPE] interface GigabitEthernet 0/1/0
   [*SPE-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*SPE-GigabitEthernet0/1/0] quit
   [*SPE] interface GigabitEthernet 0/2/0
   [*SPE-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*SPE-GigabitEthernet0/2/0] quit
   [*SPE] interface loopback1
   [*SPE-LoopBack1] isis ipv6 enable 1
   [*SPE-LoopBack1] commit
   [~SPE-LoopBack1] quit
   ```
   # Configure the NPE.
   ```
   [~NPE] isis 1
   [*NPE-isis-1] is-level level-1
   [*NPE-isis-1] cost-style wide
   [*NPE-isis-1] network-entity 10.0000.0000.0003.00
   [*NPE-isis-1] ipv6 enable topology ipv6
   [*NPE-isis-1] quit
   [*NPE] interface GigabitEthernet 0/1/0
   [*NPE-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*NPE-GigabitEthernet0/1/0] quit
   [*NPE] interface loopback1
   [*NPE-LoopBack1] isis ipv6 enable 1
   [*NPE-LoopBack1] commit
   [~NPE-LoopBack1] quit
   ```
3. On the UPE, SPE, and NPE, configure a VPN instance, enable the IPv4 address family for the instance, and bind the interface that connects the UPE to CE1 to the VPN instance on the UPE as well as the interface that connects the NPE to CE2 to the VPN instance on the NPE.
   
   # Configure the UPE.
   ```
   [~UPE] ip vpn-instance vpna
   [*UPE-vpn-instance-vpna] ipv4-family
   [*UPE-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   [*UPE-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*UPE-vpn-instance-vpna-af-ipv4] quit
   [*UPE-vpn-instance-vpna] quit
   [*UPE] interface GigabitEthernet 0/2/0
   [*UPE-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*UPE-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   [*UPE-GigabitEthernet0/2/0] quit
   [*UPE] commit
   ```
   
   # Configure the SPE.
   ```
   [~SPE] ip vpn-instance vpna
   [*SPE-vpn-instance-vpna] ipv4-family
   [*SPE-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   [*SPE-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*SPE-vpn-instance-vpna-af-ipv4] quit
   [*SPE-vpn-instance-vpna] quit
   [*SPE] commit
   ```
   
   # Configure the NPE.
   ```
   [~NPE] ip vpn-instance vpna
   [*NPE-vpn-instance-vpna] ipv4-family
   [*NPE-vpn-instance-vpna-af-ipv4] route-distinguisher 300:1
   [*NPE-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*NPE-vpn-instance-vpna-af-ipv4] quit
   [*NPE-vpn-instance-vpna] quit
   [*NPE] interface GigabitEthernet 0/2/0
   [*NPE-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*NPE-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   [*NPE-GigabitEthernet0/2/0] quit
   [*NPE] commit
   ```
4. Establish an EBGP peer relationship between the UPE and CE1 and another one between the NPE and CE2.
   
   # Configure CE1.
   ```
   [~CE1] interface loopback 1
   [*CE1-LoopBack1] ip address 11.11.11.11 32
   [*CE1-LoopBack1] quit
   [*CE1] bgp 65410
   [*CE1-bgp] peer 10.1.1.1 as-number 100
   [*CE1-bgp] network 11.11.11.11 32
   [*CE1-bgp] quit
   [*CE1] commit
   ```
   
   # Configure the UPE.
   ```
   [~UPE] bgp 100
   [*UPE-bgp] router-id 1.1.1.1
   [*UPE-bgp] ipv4-family vpn-instance vpna
   [*UPE-bgp-vpna] peer 10.1.1.2 as-number 65410
   [*UPE-bgp-vpna] import-route direct
   [*UPE-bgp-vpna] commit
   [~UPE-bgp-vpna] quit
   [~UPE-bgp] quit
   ```
   
   # Configure CE2.
   ```
   [~CE2] interface loopback 1
   [*CE2-LoopBack1] ip address 22.22.22.22 32
   [*CE2-LoopBack1] quit
   [*CE2] bgp 65420
   [*CE2-bgp] peer 10.2.1.1 as-number 100
   [*CE2-bgp] network 22.22.22.22 32
   [*CE2-bgp] quit
   [*CE2] commit
   ```
   
   # Configure the NPE.
   ```
   [~NPE] bgp 100
   [*NPE-bgp] router-id 3.3.3.3
   [*NPE-bgp] ipv4-family vpn-instance vpna
   [*NPE-bgp-vpna] peer 10.2.1.2 as-number 65420
   [*NPE-bgp-vpna] import-route direct
   [*NPE-bgp-vpna] commit
   [~NPE-bgp-vpna] quit
   [~NPE-bgp] quit
   ```
5. Establish an MP-IBGP peer relationship between the UPE and SPE and another one between the SPE and NPE.
   
   # Configure the UPE.
   ```
   [~UPE] bgp 100
   [~UPE-bgp] peer 2001:DB8:2::2 as-number 100
   [*UPE-bgp] peer 2001:DB8:2::2 connect-interface loopback 1
   [*UPE-bgp] ipv4-family vpnv4
   [*UPE-bgp-af-vpnv4] peer 2001:DB8:2::2 enable
   [*UPE-bgp-af-vpnv4] commit
   [~UPE-bgp-af-vpnv4] quit
   [~UPE-bgp] quit
   ```
   
   # Configure the SPE.
   ```
   [~SPE] bgp 100
   [*SPE-bgp] router-id 2.2.2.2
   [*SPE-bgp] peer 2001:DB8:1::1 as-number 100
   [*SPE-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   [~SPE-bgp] peer 2001:DB8:3::3 as-number 100
   [*SPE-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   [*SPE-bgp] ipv4-family vpnv4
   [*SPE-bgp-af-vpnv4] peer 2001:DB8:1::1 enable
   [*SPE-bgp-af-vpnv4] peer 2001:DB8:3::3 enable
   [*SPE-bgp-af-vpnv4] commit
   [~SPE-bgp-af-vpnv4] quit
   [~SPE-bgp] quit
   ```
   
   # Configure the NPE.
   ```
   [~NPE] bgp 100
   [~NPE-bgp] peer 2001:DB8:2::2 as-number 100
   [*NPE-bgp] peer 2001:DB8:2::2 connect-interface loopback 1
   [*NPE-bgp] ipv4-family vpnv4
   [*NPE-bgp-af-vpnv4] peer 2001:DB8:2::2 enable
   [*NPE-bgp-af-vpnv4] commit
   [~NPE-bgp-af-vpnv4] quit
   [~NPE-bgp] quit
   ```
6. Establish an SRv6 BE path between the UPE and SPE and another one between the SPE and NPE.
   
   # Configure the UPE.
   ```
   [~UPE] segment-routing ipv6
   [*UPE-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*UPE-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32
   [*UPE-segment-routing-ipv6-locator] quit
   [*UPE-segment-routing-ipv6] quit
   [*UPE] bgp 100
   [*UPE-bgp] ipv4-family vpnv4
   [*UPE-bgp-af-vpnv4] peer 2001:DB8:2::2 prefix-sid
   [*UPE-bgp-af-vpnv4] quit
   [*UPE-bgp] ipv4-family vpn-instance vpna
   [*UPE-bgp-vpna] segment-routing ipv6 best-effort
   [*UPE-bgp-vpna] segment-routing ipv6 locator as1
   [*UPE-bgp-vpna] commit
   [~UPE-bgp-vpna] quit
   [~UPE-bgp] quit
   [~UPE] isis 1
   [~UPE-isis-1] segment-routing ipv6 locator as1
   [*UPE-isis-1] commit
   [~UPE-isis-1] quit
   ```
   
   # Configure the SPE.
   ```
   [~SPE] segment-routing ipv6
   [*SPE-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*SPE-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
   [*SPE-segment-routing-ipv6-locator] quit
   [*SPE-segment-routing-ipv6] quit
   [*SPE] bgp 100
   [*SPE-bgp] ipv4-family vpnv4
   [*SPE-bgp-af-vpnv4] peer 2001:DB8:1::1 prefix-sid
   [*SPE-bgp-af-vpnv4] peer 2001:DB8:3::3 prefix-sid
   [~SPE-bgp-af-vpnv4] quit
   [*SPE-bgp] ipv4-family vpn-instance vpna
   [*SPE-bgp-vpna] segment-routing ipv6 best-effort
   [*SPE-bgp-vpna] segment-routing ipv6 locator as1
   [*SPE-bgp-vpna] commit
   [~SPE-bgp-vpna] quit
   [~SPE-bgp] quit
   [~SPE] isis 1
   [~SPE-isis-1] segment-routing ipv6 locator as1
   [*SPE-isis-1] commit
   [~SPE-isis-1] quit
   ```
   
   # Configure the NPE.
   ```
   [~NPE] segment-routing ipv6
   [*NPE-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*NPE-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32
   [*NPE-segment-routing-ipv6-locator] quit
   [*NPE-segment-routing-ipv6] quit
   [*NPE] bgp 100
   [*NPE-bgp] ipv4-family vpnv4
   [*NPE-bgp-af-vpnv4] peer 2001:DB8:2::2 prefix-sid
   [~NPE-bgp-af-vpnv4] quit
   [*NPE-bgp] ipv4-family vpn-instance vpna
   [*NPE-bgp-vpna] segment-routing ipv6 best-effort
   [*NPE-bgp-vpna] segment-routing ipv6 locator as1
   [*NPE-bgp-vpna] commit
   [~NPE-bgp-vpna] quit
   [~NPE-bgp] quit
   [~NPE] isis 1
   [~NPE-isis-1] segment-routing ipv6 locator as1
   [*NPE-isis-1] commit
   [~NPE-isis-1] quit
   ```
7. Specify the UPE as the peer of the SPE, and configure the SPE to advertise the default route to the UPE and regenerated routes to the NPE.
   
   # Configure the SPE.
   ```
   [~SPE] bgp 100
   [~SPE-bgp] ipv4-family vpnv4
   [~SPE-bgp-af-vpnv4] peer 2001:DB8:1::1 upe
   [*SPE-bgp-af-vpnv4] peer 2001:DB8:1::1 default-originate vpn-instance vpna
   [*SPE-bgp-af-vpnv4] peer 2001:DB8:3::3 advertise route-reoriginated vpnv4
   [*SPE-bgp-af-vpnv4] quit
   [*SPE-bgp] ipv4-family vpn-instance vpna
   [*SPE-bgp-vpna] advertise best-route route-reoriginate
   [*SPE-bgp-vpna] commit
   [~SPE-bgp-vpna] quit
   [~SPE-bgp] quit
   ```
8. Verify the configuration.
   
   Run the **display segment-routing ipv6 locator** [ *locator-name* ] **verbose** command to check SRv6 locator information. The following example uses the command output on the UPE.
   ```
   [~UPE] display segment-routing ipv6 locator verbose
                           Locator Configuration Table                          
                           ---------------------------                          
   
   LocatorName   : as1                                       LocatorID     : 5  
   IPv6Prefix    : 2001:DB8:100::                            PrefixLength  : 64 
   Block         : --                                        BlockLength   : 0  
   NodeID        : --                                        NodeIdLength  : 0  
   ComprStaticLen: 0                                         StaticLength  : 32 
   ArgsLength    : 0                                         Reference     : 0  
   Algorithm     : 0                                         ComprDynLength: 0  
   AutoCSIDPoolID: 0
   AutoCSIDBegin : --    
   AutoCSIDEnd   : --    
   StaticCSIDBegin: --   
   StaticCSIDEnd : --    
   AutoSIDPoolID : 8196                                      DynLength     : 32 
   AutoSIDBegin  : 2001:DB8:100::1:0:0                                          
   AutoSIDEnd    : 2001:DB8:100:0:FFFF:FFFF:FFFF:FFFF                           
   StaticSIDBegin: 2001:DB8:100::1                                              
   StaticSIDEnd  : 2001:DB8:100::FFFF:FFFF  
   GIB:LIB       : --                                    
   
   Total Locator(s): 1 
   ```
   
   Check that CEs belonging to the same VPN instance can ping each other. The following example uses the command output on CE1.
   ```
   [~CE1] ping -a 11.11.11.11 22.22.22.22 
     PING 22.22.22.22: 56  data bytes, press CTRL_C to break 
       Reply from 22.22.22.22: bytes=56 Sequence=1 ttl=253 time=7 ms 
       Reply from 22.22.22.22: bytes=56 Sequence=2 ttl=253 time=5 ms 
       Reply from 22.22.22.22: bytes=56 Sequence=3 ttl=253 time=4 ms 
       Reply from 22.22.22.22: bytes=56 Sequence=4 ttl=253 time=5 ms 
       Reply from 22.22.22.22: bytes=56 Sequence=5 ttl=253 time=5 ms 
    
     --- 22.22.22.22 ping statistics --- 
       5 packet(s) transmitted 
       5 packet(s) received 
       0.00% packet loss 
       round-trip min/avg/max = 4/5/7 ms
   ```

#### Configuration Files

* CE1 configuration file
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface loopback1
   ip address 11.11.11.11 255.255.255.255
  #
  bgp 65410
   peer 10.1.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 11.11.11.11 255.255.255.255
    peer 10.1.1.1 enable
  #
  return
  ```
* CE2 configuration file
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #
  interface loopback1
   ip address 22.22.22.22 255.255.255.255
  #
  bgp 65420
   peer 10.2.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 22.22.22.22 255.255.255.255
    peer 10.2.1.1 enable
  #
  return
  ```
* UPE configuration file
  ```
  #
  sysname UPE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2001::1/96
   isis ipv6 enable 1
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
  #
  interface loopback1
   ipv6 enable
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #
  bgp 100
   router-id 1.1.1.1
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface loopback1
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 prefix-sid
   #
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 10.1.1.2 as-number 65410
  #
  return
  ```
* SPE configuration file
  ```
  #
  sysname SPE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2001::2/96
   isis ipv6 enable 1
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2002::1/96
   isis ipv6 enable 1
  #
  interface loopback1
   ipv6 enable
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #
  bgp 100
   router-id 2.2.2.2
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface loopback1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface loopback1
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 upe
    peer 2001:DB8:1::1 default-originate vpn-instance vpna
    peer 2001:DB8:1::1 prefix-sid
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 prefix-sid
    peer 2001:DB8:3::3 advertise route-reoriginated vpnv4
   #
   ipv4-family vpn-instance vpna
    advertise best-route route-reoriginate
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
  #
  return
  ```
* NPE configuration file
  ```
  #
  sysname NPE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 300:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2002::2/96
   isis ipv6 enable 1
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
  #
  interface loopback1
   ipv6 enable
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #
  bgp 100
   router-id 3.3.3.3
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface loopback1
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 prefix-sid
   #
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 10.2.1.2 as-number 65420
  #
  return
  ```