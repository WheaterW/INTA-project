Example for Configuring BGP Hierarchical Routing
================================================

Example for Configuring BGP Hierarchical Routing

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176743533__fig168879525502), DeviceA and DeviceB interwork through BGP. DeviceA may import a large number of external routes. To ensure fast route convergence in the case of a device or link failure, it is required that BGP hierarchical routing be deployed on DeviceA and hierarchical routing convergence be deployed on the other node. In this example, the route 1.1.1.1/32 is configured as a base route, and the route 2.2.2.2/32 is configured as a hierarchical route on DeviceA.

**Figure 1** Networking diagram of BGP hierarchical routing![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001130783956.png)

#### Precautions

During the configuration, note the following:

* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Authentication." Keychain authentication is used as an example. For details, see Example for Configuring Keychain Authentication for BGP.

#### Configuration Roadmap

1. Configure an EBGP connection between DeviceA and DeviceB.
2. Configure the base route and hierarchical route on DeviceA.
3. Enable hierarchical convergence on DeviceB.

#### Procedure

1. Assign IP addresses to interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100GE1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.10.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface loopback1
   [*DeviceA-LoopBack1] ip address 1.1.1.1 32
   [*DeviceA-LoopBack1] quit
   [*DeviceA] interface loopback2
   [*DeviceA-LoopBack2] ip address 2.2.2.2 32
   [*DeviceA-LoopBack2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <~HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100GE1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.10.1.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
2. Configure EBGP.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] router-id 11.11.11.11
   [*DeviceA-bgp] peer 10.10.1.2 as-number 200
   [*DeviceA-bgp] peer 10.10.1.2 ebgp-max-hop 255
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   [*DeviceB-bgp] router-id 22.22.22.22
   [*DeviceB-bgp] peer 10.10.1.1 as-number 100
   [*DeviceB-bgp] peer 10.10.1.1 ebgp-max-hop 255
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Check the status of BGP connections.
   
   ```
   [~DeviceA] display bgp peer
   
    BGP local router ID : 11.11.11.11
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.10.1.2                        4         200        5        6     0 00:00:17 Established       0
   ```
3. Run the **network** command on DeviceA to import local routes and use BGP to advertise the routes to its peers.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] network 1.1.1.1 32
   [*DeviceA-bgp-af-ipv4] network 2.2.2.2 32
   [*DeviceA-bgp-af-ipv4] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
4. Configure the base route and hierarchical route on DeviceA.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] hierarchy-convergence base-route 1.1.1.1 32 hierarchy-route all
   [*DeviceA-bgp-af-ipv4] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
5. Enable hierarchical convergence on DeviceB.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   [*DeviceB-bgp] ipv4-family unicast
   [*DeviceB-bgp-af-ipv4] hierarchy-convergence enable
   [*DeviceB-bgp-af-ipv4] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the BGP routing table of DeviceB. The following command output shows that the route 1.1.1.1/32 is a base route.
```
[~DeviceB] display bgp routing-table 1.1.1.1 32

 BGP local router ID : 22.22.22.22
 Local AS number : 200
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 1.1.1.1/32:
 From: 10.10.1.1 (11.11.11.11)
 Route Duration: 0d00h30m53s
 Relay IP Nexthop: 10.10.1.1
 Relay IP Out-Interface: 100GE1/0/1
 Original nexthop: 10.10.1.1
 Qos information : 0x0
 AS-path 100, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
 Hierarchy convergence: base-route
 Advertised to such 1 peers:
    10.10.1.1
```

# Display the BGP routing table of DeviceB. The command output shows that the route 2.2.2.2/32 is a hierarchical route and depends on the base route 1.1.1.1/32.
```
[~DeviceB] display bgp routing-table 2.2.2.2 32

 BGP local router ID : 22.22.22.22
 Local AS number : 200
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 1.1.1.1/32:
 From: 10.10.1.1 (1.1.1.1)
 Route Duration: 0d00h30m53s
 Relay IP Nexthop: 10.10.1.1
 Relay IP Out-Interface: 100GE1/0/1
 Original nexthop: 10.10.1.1
 Qos information : 0x0
 AS-path 100, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
 Hierarchy convergence: hierarchy-route, rely-base-route 1.1.1.1/32
 Advertised to such 1 peers:
    10.10.1.1
```


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.10.1.1 24
  #
  interface LoopBack1
   ip address 1.1.1.1 32
  #
  interface LoopBack2
   ip address 2.2.2.2 32
  #
  bgp 100
   router-id 11.11.11.11
   peer 10.10.1.2 as-number 200
   peer 10.10.1.2 ebgp-max-hop 255
   #
   ipv4-family unicast
    undo synchronization
    network 1.1.1.1 255.255.255.255
    network 2.2.2.2 255.255.255.255
    hierarchy-convergence base-route 1.1.1.1 32 hierarchy-route all
    peer 10.10.1.2 enable
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
   ip address 10.10.1.2 24
  #
  bgp 200
   router-id 22.22.22.22
   peer 10.10.1.1 as-number 100
   peer 10.10.1.1 ebgp-max-hop 255
   #
   ipv4-family unicast
    undo synchronization
    hierarchy-convergence enable
    peer 10.10.1.1 enable
  #
  return
  ```