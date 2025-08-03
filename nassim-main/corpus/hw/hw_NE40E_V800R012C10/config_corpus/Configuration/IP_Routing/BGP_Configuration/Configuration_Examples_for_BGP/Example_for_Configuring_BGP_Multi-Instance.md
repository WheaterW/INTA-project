Example for Configuring BGP Multi-Instance
==========================================

This section provides an example for configuring BGP multi-instance to achieve instance-specific management and maintenance of routes.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0217031277__fig568519487491), the public network BGP-IPv4 unicast address family is enabled in base BGP instances on DeviceA and DeviceB, and a public network IBGP peer relationship is established between them to transmit public network routes. In addition, the VPN address family is enabled in the BGP multi-instance on DeviceB and in the base BGP instance on DeviceC, and an IBGP-VPN peer relationship is established between them to transmit VPN routes. In this way, routes can be managed and maintained separately.

**Figure 1** BGP multi-instance networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0217522978.png)

#### Precautions

To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the public network BGP-IPv4 unicast address family in base BGP instances on DeviceA and DeviceB, and establish a public network IBGP peer relationship in this address family.
2. Enable the VPN address family in the BGP multi-instance on DeviceB and in the base instance on DeviceC, and establish an IBGP-VPN peer relationship in this address family.

#### Data Preparation

To complete the configuration, you need the following data:

* DeviceA's AS number: 100
* DeviceB's AS numbers: 100 and 200
* DeviceC's AS number: 200

#### Procedure

1. Enable the public network BGP-IPv4 unicast address family in base BGP instances on DeviceA and DeviceB, and establish a public network IBGP peer relationship in this address family.
   
   
   
   # Configure DeviceA.
   
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 10.1.1.2 as-number 100
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] peer 10.1.1.1 as-number 100
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   After the configuration is complete, check the connectivity between DeviceA and DeviceB. Then, run the **display bgp peer** command. The command output shows that the public network IBGP peer relationship between DeviceA and DeviceB is **Established**.
   
   DeviceB is used as an example.
   
   ```
   <DeviceB> ping 10.1.1.1
     PING 10.1.1.1: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.1: bytes=56 Sequence=1 ttl=255 time=30 ms
       Reply from 10.1.1.1: bytes=56 Sequence=2 ttl=255 time=16 ms
       Reply from 10.1.1.1: bytes=56 Sequence=3 ttl=255 time=7 ms
       Reply from 10.1.1.1: bytes=56 Sequence=4 ttl=255 time=6 ms
       Reply from 10.1.1.1: bytes=56 Sequence=5 ttl=255 time=9 ms
   
     --- 10.1.1.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 6/13/30 ms
   ```
   ```
   <DeviceB> display bgp peer
    BGP local router ID : 10.1.1.2
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.1.1        4         100        5        5     0 00:00:20 Established        0
   ```
2. Enable the VPN address family in the BGP multi-instance on DeviceB and in the base instance on DeviceC, and establish an IBGP-VPN peer relationship in this address family.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ip vpn-instance vpn1
   ```
   ```
   [*DeviceB-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:3
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 export-extcommunity
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 import-extcommunity
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*DeviceB-vpn-instance-vpn1] quit
   ```
   ```
   [*DeviceB] bgp 200 instance vpn1
   ```
   ```
   [~DeviceB-bgp-instance-aa] ipv4-family vpn-instance vpn1
   ```
   ```
   [*DeviceB-bgp-instance-aa-vpn1] peer 10.1.2.3 as-number 200
   ```
   ```
   [*DeviceB-bgp-instance-aa-vpn1] quit
   ```
   ```
   [*DeviceB-bgp-instance-aa] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ip address 10.1.2.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] ip vpn-instance vpn1
   ```
   ```
   [*DeviceC-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*DeviceC-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:3
   ```
   ```
   [*DeviceC-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 export-extcommunity
   ```
   ```
   [*DeviceC-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 import-extcommunity
   ```
   ```
   [*DeviceC-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*DeviceC-vpn-instance-vpn1] quit
   ```
   ```
   [*DeviceC] bgp 200
   ```
   ```
   [*DeviceC-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*DeviceC-bgp-vpn1] peer 10.1.2.2 as-number 200
   ```
   ```
   [*DeviceC-bgp-vpn1] quit
   ```
   ```
   [*DeviceC-bgp] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ip address 10.1.2.3 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   
   After the configuration is complete, check the connectivity between DeviceB and DeviceC. Then, run the **display bgp instance aa vpnv4 all peer** command. The command output shows that the IBGP-VPN peer relationship between DeviceB and DeviceC is **Established**.
   
   DeviceB is used as an example.
   
   ```
   <DeviceB> ping -vpn-instance vpn1 10.1.2.3
     PING 10.1.2.3: 56  data bytes, press CTRL_C to break
       Reply from 10.1.2.3: bytes=56 Sequence=1 ttl=255 time=35 ms
       Reply from 10.1.2.3: bytes=56 Sequence=2 ttl=255 time=25 ms
       Reply from 10.1.2.3: bytes=56 Sequence=3 ttl=255 time=12 ms
       Reply from 10.1.2.3: bytes=56 Sequence=4 ttl=255 time=8 ms
       Reply from 10.1.2.3: bytes=56 Sequence=5 ttl=255 time=9 ms
   
     --- 10.1.2.3 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 8/17/35 ms
   ```
   ```
   <DeviceB> display bgp instance aa vpnv4 all peer
    BGP local router ID : 10.1.1.2
    Local AS number : 200
    Total number of peers : 1                 Peers in established state : 1
   
   
     Peer of IPv4-family for vpn instance :
   
     VPN-Instance vpn1, Router ID 10.1.1.2:
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.2.3        4         200        3        3     0 00:00:03 Established        0
   ```
3. Configure a static route and import it into the BGP routing table on DeviceA and DeviceC.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ip route-static 192.168.1.1 255.255.255.255 NULL0
   ```
   ```
   [*DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] import-route static
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ip route-static vpn-instance vpn1 192.168.3.3 255.255.255.255 NULL0
   ```
   ```
   [*DeviceC] bgp 200
   ```
   ```
   [*DeviceC-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*DeviceC-bgp-vpn1] import-route static
   ```
   ```
   [*DeviceC-bgp-vpn1] commit
   ```
4. Verify the configuration.
   
   
   
   After the preceding configurations are complete, only public network routes can be found on DeviceA.
   
   ```
   <DeviceA> display bgp routing-table
   
    BGP Local router ID is 10.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 1
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     192.168.1.1/32     0.0.0.0                        0                     0       ?
   ```
   
   Both public network and VPN routes can be found on DeviceB.
   
   ```
   <DeviceB> display bgp routing-table
   
    BGP Local router ID is 10.1.1.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 1
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     192.168.1.1/32     10.1.1.1                      0                     0       ?
   ```
   ```
   <DeviceB> display bgp instance aa vpnv4 all routing-table
   
    BGP Local router ID is 10.1.1.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total number of routes from all PE: 1
    Route Distinguisher: 100:44
   
   
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     192.168.3.3/32     10.1.2.3                       0                     0      100?
   
    VPN-Instance vpn1, Router ID 10.1.1.2:
   
    Total Number of Routes: 1
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     192.168.3.3/32     10.1.2.3                       0                     0      100?
   ```
   
   Only a VPN route can be found on DeviceC.
   
   ```
   <DeviceC> display bgp vpnv4 all routing-table
   
    BGP Local router ID is 0.0.0.0
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total number of routes from all PE: 1
    Route Distinguisher: 100:44
   
   
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     192.168.3.3/32     0.0.0.0                        0                     0       ?
   
    VPN-Instance vpn1, Router ID 10.1.2.3:
   
    Total Number of Routes: 1
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     192.168.3.3/32     0.0.0.0                        0                     0       ?
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  bgp 100
   peer 10.1.1.2 as-number 100
   ipv4-family unicast
    undo synchronization
    import-route static
    peer 10.1.1.2 enable
  #
  ip route-static 192.168.1.1 255.255.255.255 NULL0
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:3
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.1.2.2 255.255.255.0
  #
  bgp 100
   peer 10.1.1.1 as-number 100
   ipv4-family unicast
    undo synchronization
    peer 10.1.1.1 enable
  #
  bgp 200 instance vpn1
   ipv4-family vpn-instance vpn1
    peer 10.1.2.3 as-number 200
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:3
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.1.2.3 255.255.255.0
  #
  bgp 200
   ipv4-family unicast
    undo synchronization
   ipv4-family vpn-instance vpn1
    import-route static
    peer 10.1.2.2 as-number 200
  #
  ip route-static vpn-instance vpn1 192.168.3.3 255.255.255.255 NULL0
  #
  return
  ```