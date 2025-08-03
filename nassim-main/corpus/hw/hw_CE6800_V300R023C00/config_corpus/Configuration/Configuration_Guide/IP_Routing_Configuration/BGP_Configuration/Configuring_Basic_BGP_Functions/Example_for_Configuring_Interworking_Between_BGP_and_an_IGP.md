Example for Configuring Interworking Between BGP and an IGP
===========================================================

Example for Configuring Interworking Between BGP and an IGP

#### Networking Requirements

As communications services grow, devices in different ASs require mutual access, data must be reliably transmitted, and the traffic interruption time must be minimized. Such demands require routing information to be widely transmitted and route convergence to be accelerated. While BGP can transmit routing information widely and efficiently, it does not calculate routes by itself. In contrast, an IGP can implement rapid route convergence, but transmits routing information with low efficiency and with limited scope. After interworking between BGP and an IGP is configured, IGP routes can be imported into the BGP routing table and then transmitted efficiently and widely. BGP routes can also be imported into the IGP routing table so that the local AS can access other ASs.

The network shown in [Figure 1](#EN-US_TASK_0000001130783886__fig_dc_vrp_bgp_cfg_407301) is divided into AS 65008 and AS 65009. In AS 65009, an IGP is deployed to calculate routes. In this example, OSPF is used. To implement communication between the ASs, configure BGP between them and configure interworking between BGP and the IGP on edge devices of the ASs.

**Figure 1** Network diagram of interworking between BGP and an IGP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001130783974.png)

#### Precautions

During the configuration, note the following:

* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Authentication." Keychain authentication is used as an example. For details, see Example for Configuring Keychain Authentication for BGP.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF on DeviceB and DeviceC.
2. Establish an EBGP connection between DeviceA and DeviceB.
3. Configure BGP and OSPF to import routes from each other on DeviceB, and then check the routing information.
4. Configure BGP route summarization on DeviceB to reduce the size of the BGP routing table.

#### Procedure

1. Assign an IP address to each interface. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130783886__postreq186481836141010).
2. Configure OSPF.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospf 1
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
3. Configure an EBGP connection.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 65008
   [*DeviceA-bgp] router-id 1.1.1.1
   [*DeviceA-bgp] peer 172.16.1.1 as-number 65009
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] network 192.168.1.0 255.255.255.0
   [*DeviceA-bgp-af-ipv4] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 65009
   [*DeviceB-bgp] router-id 2.2.2.2
   [*DeviceB-bgp] peer 172.16.1.2 as-number 65008
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
4. Configure interworking between BGP and the IGP.
   
   
   
   # Configure BGP to import OSPF routes on DeviceB.
   
   ```
   [~DeviceB] bgp 65009
   [~DeviceB-bgp] ipv4-family unicast
   [*DeviceB-bgp-af-ipv4] import-route ospf 1
   [*DeviceB-bgp-af-ipv4] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Check the routing table of DeviceA.
   
   ```
   [~DeviceA] display bgp routing-table
   
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 3
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
    *>   192.168.1.0/24     0.0.0.0         0                     0      i
    *>   10.1.1.0/24        172.16.1.1      1                     0      65009?
    *>   10.1.2.0/24        172.16.1.1      2                     0      65009?
   ```
   
   # Configure OSPF to import BGP routes on DeviceB.
   
   ```
   [~DeviceB] ospf
   [*DeviceB-ospf-1] import-route bgp
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Check the IP routing table of DeviceC.
   
   ```
   [~DeviceC] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 12        Routes : 12
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
       192.168.1.0/24  O_ASE  150  1             D  10.1.1.1        100GE1/0/1
          10.1.1.0/24  Direct 0    0             D  10.1.1.2        100GE1/0/1
          10.1.1.1/32  Direct 0    0             D  10.1.1.1        100GE1/0/1
          10.1.1.2/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
        10.1.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
          10.1.2.0/24  Direct 0    0             D  10.1.2.1        100GE1/0/2
          10.1.2.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
        10.1.2.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
5. Configure automatic route summarization.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 65009
   [~DeviceB-bgp] ipv4-family unicast
   [~DeviceB-bgp-af-ipv4] summary automatic
   [*DeviceB-bgp-af-ipv4] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the BGP routing table of DeviceA.

```
[~DeviceA] display bgp routing-table

 BGP Local router ID is 1.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 2
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>   192.168.1.0/24     0.0.0.0         0                     0      i
 *>   10.0.0.0           172.16.1.1                            0      65009?
```

# Verify the configuration using the **ping** command.

```
[~DeviceA] ping -a 192.168.1.1 10.1.2.1
  PING 10.1.2.1: 56  data bytes, press CTRL_C to break
    Reply from 10.1.2.1: bytes=56 Sequence=1 ttl=254 time=15 ms
    Reply from 10.1.2.1: bytes=56 Sequence=2 ttl=254 time=31 ms
    Reply from 10.1.2.1: bytes=56 Sequence=3 ttl=254 time=47 ms
    Reply from 10.1.2.1: bytes=56 Sequence=4 ttl=254 time=46 ms
    Reply from 10.1.2.1: bytes=56 Sequence=5 ttl=254 time=47 ms
  --- 10.1.2.1 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 15/37/47 ms
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.2 255.255.255.0
  #
  bgp 65008
   router-id 1.1.1.1
   peer 172.16.1.1 as-number 65009
   #
   ipv4-family unicast
    network 192.168.1.0 255.255.255.0
    peer 172.16.1.1 enable
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  bgp 65009
   router-id 2.2.2.2
   peer 172.16.1.2 as-number 65008
   #
   ipv4-family unicast
    summary automatic
    import-route ospf 1
    peer 172.16.1.2 enable
  #
  ospf 1
   import-route bgp
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
  #
  return
  ```