Example for Configuring a BGP Community Attribute
=================================================

Example for Configuring a BGP Community Attribute

#### Networking Requirements

Enterprises A, B, and C belong to different ASs, and enterprise B's network communicates with the networks of the other two enterprises through EBGP connections. Enterprises A and C compete with each other. To improve security, enterprise A requires that the routes sent from enterprise A's AS to enterprise B's network be advertised only within enterprise B's network. To tackle this issue, configure the community attribute function on the device that sends routes from enterprise A to enterprise B.

As shown in [Figure 1](#EN-US_TASK_0000001176663687__fig_dc_vrp_bgp_cfg_407701), EBGP connections are established between DeviceB and each of DeviceA and DeviceC. It is required that the BGP routes imported by DeviceA in AS 10 and then advertised to DeviceB in AS 20 be transmitted only in AS 20 instead of being advertised by AS 20 to other ASs. In this case, you can configure DeviceA to encapsulate the No\_Export community attribute for the BGP routes to be advertised to DeviceB.

**Figure 1** Network diagram of configuring a BGP community attribute![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001130783990.png)

#### Precautions

During the configuration, note the following:

* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Authentication." Keychain authentication is used as an example. For details, see Example for Configuring Keychain Authentication for BGP.

#### Procedure

1. Assign an IP address to each involved interface. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176663687__postreq17364171716277).
2. Configure EBGP.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 10
   [*DeviceA-bgp] router-id 1.1.1.1
   [*DeviceA-bgp] peer 10.1.2.2 as-number 20
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] network 10.5.1.0 255.255.255.0
   [*DeviceA-bgp-af-ipv4] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 20
   [*DeviceB-bgp] router-id 2.2.2.2
   [*DeviceB-bgp] peer 10.1.2.1 as-number 10
   [*DeviceB-bgp] peer 10.1.3.2 as-number 30
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 30
   [*DeviceC-bgp] router-id 3.3.3.3 
   [*DeviceC-bgp] peer 10.1.3.1 as-number 20
   [*DeviceC-bgp] quit
   [*DeviceC] commit
   ```
   
   # Check the routing table of DeviceB.
   
   ```
   [~DeviceB] display bgp routing-table 10.5.1.0
   
   BGP local router ID : 2.2.2.2
    Local AS number : 20
    Paths:   1 available, 1 best, 1 select
    BGP routing table entry information of 10.5.1.0/24:
    From: 10.1.2.1 (1.1.1.1)
    Route Duration: 0d00h00m37s
    Direct Out-interface: 100GE1/0/2
    Original nexthop: 10.1.2.1
    Qos information : 0x0
    AS-path 10, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
    Advertised to such 2 peers:
       10.1.2.1
       10.1.3.2
   ```
   
   The preceding command output shows that DeviceB has advertised the accepted route to DeviceC in AS 30.
   
   # Check the routing table of DeviceC.
   
   ```
   [~DeviceC] display bgp routing-table
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 1
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   10.5.1.0/24        10.1.3.1                             0      20 10i
   ```
   
   The preceding command output shows that DeviceC has learned the route to 10.5.1.0/24 from DeviceB.
3. Configure a BGP community attribute.
   
   
   
   # Configure a route-policy on DeviceA to ensure that the routes advertised by DeviceA to DeviceB are not advertised by DeviceB to any other AS.
   
   ```
   [~DeviceA] route-policy comm_policy permit node 10
   [*DeviceA-route-policy] apply community no-export
   [*DeviceA-route-policy] quit
   [*DeviceA] commit
   ```
   
   # Apply the route-policy.
   
   ```
   [~DeviceA] bgp 10
   [~DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] peer 10.1.2.2 route-policy comm_policy export
   [*DeviceA-bgp-af-ipv4] peer 10.1.2.2 advertise-community
   [*DeviceA-bgp-af-ipv4] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the routing table of DeviceB.

```
[*DeviceB] display bgp routing-table 10.5.1.0
BGP local router ID : 2.2.2.2
 Local AS number : 20
 Paths:   1 available, 1 best, 1 select
 BGP routing table entry information of 10.5.1.0/24:
 From: 10.1.2.1 (1.1.1.1)
 Route Duration: 0d00h00m12s
 Direct Out-interface: 100GE1/0/2
 Original nexthop: 10.1.2.1
 Qos information : 0x0
 Community:no-export
 AS-path 10, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
 Not advertised to any peers yet
```

The BGP routing table of DeviceB contains the configured community attribute. Then, there is no route to 10.5.1.0/24 in the BGP routing table of DeviceC.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.5.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #
  bgp 10
   router-id 1.1.1.1
   peer 10.1.2.2 as-number 20
   #
   ipv4-family unicast
    undo synchronization 
    network 10.5.1.0 255.255.255.0
    peer 10.1.2.2 enable
    peer 10.1.2.2 route-policy comm_policy export
    peer 10.1.2.2 advertise-community
  #
  route-policy comm_policy permit node 10
   apply community no-export
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
   ip address 10.1.3.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
  #
  bgp 20
   router-id 2.2.2.2
   peer 10.1.2.1 as-number 10
   peer 10.1.3.2 as-number 30
   #
   ipv4-family unicast
    undo synchronization 
    peer 10.1.2.1 enable
    peer 10.1.3.2 enable
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
   ip address 10.1.3.2 255.255.255.0
  #
  bgp 30
   router-id 3.3.3.3
   peer 10.1.3.1 as-number 20
   #
   ipv4-family unicast
    undo synchronization 
    peer 10.1.3.1 enable
  #
  return
  ```