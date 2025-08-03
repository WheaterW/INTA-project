Example for Configuring BGP4+ Hierarchical Routing
==================================================

Example for Configuring BGP4+ Hierarchical Routing

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130782204__fig168879525502), DeviceA and DeviceB interwork through BGP. DeviceA may import a large number of external routes. To ensure fast route convergence in the case of a device or link failure, it is required that BGP4+ hierarchical routing be deployed on DeviceA and hierarchical routing convergence be deployed on the other node. In this example, DeviceA uses the route 2001:db8:3::3/128 as a base route and the route 2001:db8:5::5/128 as a hierarchical route.

**Figure 1** Networking diagram of BGP4+ hierarchical routing![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001176741901.png)

#### Precautions

Note the following during the configuration:

* To improve security, you are advised to deploy BGP4+ security measures. For details, see "Configuring BGP4+ Authentication." Keychain authentication is used as an example. For details, see Example for Configuring Keychain Authentication for BGP4+.

#### Configuration Roadmap

1. Configure an EBGP connection between DeviceA and DeviceB.
2. Configure the base route and hierarchical routes on DeviceA.
3. Enable hierarchical routing convergence on DeviceB.

#### Procedure

1. Assign IP addresses to interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <~HUAWEI> system-view
   [*HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100GE1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:1::1 96
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface loopback1
   [*DeviceA-LoopBack1] ipv6 enable
   [*DeviceA-LoopBack1] ipv6 address 2001:db8:3::3 128
   [*DeviceA-LoopBack1] quit
   [*DeviceA] interface loopback2
   [*DeviceA-LoopBack2] ipv6 enable
   [*DeviceA-LoopBack2] ipv6 address 2001:db8:5::5 32
   [*DeviceA-LoopBack2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <~HUAWEI> system-view
   [*HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100GE1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:1::2 96
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
2. Configure EBGP.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] router-id 11.11.11.11
   [*DeviceA-bgp] peer 2001:db8:1::2 as-number 200
   [*DeviceA-bgp] peer 2001:db8:1::2 ebgp-max-hop 255
   [*DeviceA-bgp] ipv6-family unicast
   [*DeviceA-bgp-af-ipv6] network 2001:db8:3::3 128
   [*DeviceA-bgp-af-ipv6] network 2001:db8:5::5 128
   [*DeviceA-bgp-af-ipv6] peer 2001:db8:1::2 enable
   [*DeviceA-bgp] quit
   [*DeviceA] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   [*DeviceB-bgp] router-id 22.22.22.22
   [*DeviceB-bgp] peer 2001:db8:1::1 as-number 100
   [*DeviceB-bgp] peer 2001:db8:1::1 ebgp-max-hop 255
   [*DeviceB-bgp] ipv6-family unicast
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:1::1 enable
   [*DeviceB-bgp] quit
   [*DeviceB] quit
   [*DeviceB] commit
   ```
   
   # Check the status of the BGP4+ peer connection.
   
   ```
   [~DeviceA] display bgp ipv6 peer
   
    BGP local router ID : 11.11.11.11
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:db8:1::2                    4         200        5        6     0 00:00:17 Established       0
   ```
3. Configure the base route and hierarchical route on DeviceA.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] ipv6-family unicast
   [*DeviceA-bgp-af-ipv6] hierarchy-convergence base-route 2001:db8:3::3 128 hierarchy-route all
   [*DeviceA-bgp-af-ipv6] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
4. Enable hierarchical routing convergence on DeviceB.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   [*DeviceB-bgp] ipv6-family unicast
   [*DeviceB-bgp-af-ipv6] hierarchy-convergence enable
   [*DeviceB-bgp-af-ipv6] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the BGP IPv6 routing table of DeviceB. The command output shows that the route 2001:db8:3::3/128 is a base route.
```
[~DeviceB] display bgp ipv6 routing-table 2001:db8:3::3 128

 BGP local router ID : 22.22.22.22
 Local AS number : 200
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 1.1.1.1/32:
 From: 2001:db8:1::1 (11.11.11.11)
 Route Duration: 0d00h30m53s
 Relay IP Nexthop: 2001:db8:1::1
 Relay IP Out-Interface: 100GE1/0/1
 Original nexthop: 2001:db8:1::1
 Qos information : 0x0
 AS-path 100, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
 Hierarchy convergence: base-route
 Advertised to such 1 peers:
    2001:db8:1::1
```

# Check the BGP IPv6 routing table of DeviceB. The command output shows that the route 2001:db8:5::5/128 is a hierarchical route and depends on the base route 2001:db8:3::3/128.
```
[~DeviceB] display bgp ipv6 routing-table 2001:db8:5::5 128

 BGP local router ID : 22.22.22.22
 Local AS number : 200
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 1.1.1.1/32:
 From: 2001:db8:1::1 (11.11.11.11)
 Route Duration: 0d00h30m53s
 Relay IP Nexthop: 2001:db8:1::1
 Relay IP Out-Interface: 100GE1/0/1
 Original nexthop: 2001:db8:1::1
 Qos information : 0x0
 AS-path 100, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
 Hierarchy convergence: hierarchy-route, rely-base-route 2001:db8:3::3/128
 Advertised to such 1 peers:
    2001:db8:1::1
```


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::1 96
  #
  interface LoopBack1
   ipv6 address 2001:db8:3::3 128
  #
  interface LoopBack2
   ipv6 address 2001:db8:5::5 128
  #
  bgp 100
   router-id 11.11.11.11
   peer 2001:DB8:1::2 as-number 200
   peer 2001:DB8:1::2 ebgp-max-hop 255
   #
   ipv6-family unicast
    undo synchronization
    network 2001:db8:3::3 128
    network 2001:db8:5::5 128
    hierarchy-convergence base-route 2001:db8:3::3 128 hierarchy-route all
    peer 2001:DB8:1::2 enable
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
   ipv6 enable
   ipv6 address 2001:DB8:1::2 96
  #
  bgp 200
   router-id 22.22.22.22
   peer 2001:DB8:1::1 as-number 200
   peer 2001:DB8:1::1 ebgp-max-hop 255
   #
   ipv6-family unicast
    undo synchronization
    hierarchy-convergence enable
    peer 2001:DB8:1::1 enable
  #
  return
  ```