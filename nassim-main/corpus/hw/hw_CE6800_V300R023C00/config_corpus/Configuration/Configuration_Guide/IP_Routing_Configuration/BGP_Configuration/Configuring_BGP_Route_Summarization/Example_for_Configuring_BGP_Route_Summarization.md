Example for Configuring BGP Route Summarization
===============================================

Example for Configuring BGP Route Summarization

#### Networking Requirements

BGP routes can be locally imported or learned from peers. The locally imported routes take precedence over those learned from peers during BGP route selection. In real-world networking, there is a low probability that both locally imported routes and those learned from BGP peers are destined for the same destination address. In most cases, a local device imports routes in different ways. Locally imported routes include routes imported using the [**network**](cmdqueryname=network) or [**import-route**](cmdqueryname=import-route) command, as well as manually and automatically generated summary routes. BGP selects such routes in descending order of priority:

1. Prefers a summary route to a non-summary route.
2. Prefers a summary route manually generated using the [**aggregate**](cmdqueryname=aggregate) command to a summary route automatically generated using the [**summary automatic**](cmdqueryname=summary+automatic) command.
3. Prefers a route imported using the [**network**](cmdqueryname=network) command to a route imported using the [**import-route**](cmdqueryname=import-route) command.

Take the network shown in [Figure 1](#EN-US_TASK_0000001130783884__fig_dc_vrp_bgp_path_selection_000701) as an example. An EBGP peer relationship is established between DeviceA and DeviceB, and an IBGP peer relationship is established between each pair of DeviceB, DeviceC, and DeviceD.**Figure 1** Network diagram of BGP route summarization  
![](figure/en-us_image_0000001176663723.png)


#### Precautions

During the configuration, note the following:

* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Authentication." Keychain authentication is used as an example. For details, see Example for Configuring Keychain Authentication for BGP.

#### Procedure

1. Configure DeviceC.
   
   
   ```
   #
   bgp 65001
    #
    ipv4-family unicast
     network 10.1.2.0 255.255.255.252                       //Configure the device to advertise routes to 10.1.2.0/30.
     network 10.1.4.0 255.255.255.252                       //Configure the device to advertise routes to 10.1.4.0/30.
     import-route direct                                    //Configure the device to import direct routes.
   #
   ```
2. Configure DeviceD.
   
   
   ```
   #
   bgp 65001
    #
    ipv4-family unicast
     network 10.1.3.0 255.255.255.252                       //Configure the device to advertise routes to 10.1.3.0/30.
     network 10.1.4.0 255.255.255.252                       //Configure the device to advertise routes to 10.1.4.0/30.
     import-route direct                                    //Configure the device to import direct routes.
   #
   ```

#### Verifying the Configuration

Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *ip-address*] command to verify the configurations.

# Check the routing table of DeviceD.

```
[~DeviceD] display bgp routing-table
 BGP Local router ID is 10.1.3.2
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 10
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>i  10.1.2.0/30        10.1.4.2        0          100        0      i
 *>   10.1.3.0/30        0.0.0.0         0                     0      i
 *                       0.0.0.0         0                     0      ?
 *>   10.1.3.2/32        0.0.0.0         0                     0      ?
 *>   10.1.4.0/30        0.0.0.0         0                     0      i
 *                       0.0.0.0         0                     0      ?
   i                     10.1.4.2        0          100        0      ?
 *>   10.1.4.1/32        0.0.0.0         0                     0      ?
 *>   127.0.0.0          0.0.0.0         0                     0      ?
 *>   127.0.0.1/32       0.0.0.0         0                     0      ?
```

The preceding command output shows that three routes pointing to the 10.1.4.0/30 segment are available in the routing table. The route with the next hop address 10.1.4.2 is learned from DeviceC, and therefore BGP ignores the route first during route selection.

```
[~DeviceD] display bgp routing-table 10.1.4.0 30
 BGP local router ID : 10.1.3.2
 Local AS number : 65001
 Paths:   3 available, 1 best, 1 select
 BGP routing table entry information of 10.1.4.0/30:
 Network route.
 From: 0.0.0.0 (0.0.0.0)
 Route Duration: 00h03m51s
 Direct Out-interface: 100GE1/0/1
 Original nexthop: 10.1.4.1
 Qos information : 0x0
 AS-path Nil, origin igp, MED 0, pref-val 0, valid, local, best, select, pre 0
 Advertised to such 2 peers:
    10.1.3.1
    10.1.4.2
 BGP routing table entry information of 10.1.4.0/30:
 Imported route.
 From: 0.0.0.0 (0.0.0.0)
 Route Duration: 00h04m10s
 Direct Out-interface:100GE1/0/1
 Original nexthop: 10.1.4.1
 Qos information : 0x0
 AS-path Nil, origin incomplete, MED 0, pref-val 0, valid, local, pre 0, not preferred for route type
 Not advertised to any peer yet

 BGP routing table entry information of 10.1.4.0/30:
 From: 10.1.4.2 (10.1.2.2)
 Route Duration: 00h02m24s
 Relay IP Nexthop: 0.0.0.0
 Relay IP Out-Interface: 100GE1/0/1
 Original nexthop: 10.1.4.2
 Qos information : 0x0
 AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, internal, pre 255
 Not advertised to any peer yet
```

The preceding command output shows that the route imported using the [**network**](cmdqueryname=network) command is selected as the optimal route.

Configure DeviceB.

```
bgp 65001
 #
 ipv4-family unicast
  summary automatic
  aggregate 10.0.0.0 255.0.0.0
  import-route direct
#
```

Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *ip-address*] command to verify the configurations.

# Check the routing table of DeviceB.

```
[~DeviceB] display bgp routing-table
 BGP Local router ID is 10.1.1.2
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 14
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>   10.0.0.0           127.0.0.1                             0      ?
 *                       127.0.0.1                             0      ?
 s>   10.1.1.0/30        0.0.0.0         0                     0      ?
 *>   10.1.1.2/32        0.0.0.0         0                     0      ?
 s>   10.1.2.0/30        0.0.0.0         0                     0      ?
   i                     10.1.2.2        0          100        0      i
 *>   10.1.2.1/32        0.0.0.0         0                     0      ?
 s>   10.1.3.0/30        0.0.0.0         0                     0      ?
   i                     10.1.3.2        0          100        0      i
 *>   10.1.3.1/32        0.0.0.0         0                     0      ?
 *>i  10.1.4.0/30        10.1.3.2        0          100        0      i
 * i                     10.1.2.2        0          100        0      ?
 *>   127.0.0.0          0.0.0.0         0                     0      ?
 *>   127.0.0.1/32       0.0.0.0         0                     0      ?
```

The preceding command output shows that two summary routes 10.0.0.0 are available in the routing table.

```
[~DeviceB] display bgp routing-table 10.0.0.0
 BGP local router ID : 10.1.1.2
 Local AS number : 65001
 Paths:   2 available, 1 best, 1 select
 BGP routing table entry information of 10.0.0.0/8:
 Aggregated route.
 Route Duration: 00h17m04s
 Direct Out-interface: NULL0
 Original nexthop: 127.0.0.1
 Qos information : 0x0
 AS-path Nil, origin incomplete, pref-val 0, valid, local, best, select, active, pre 255
 Aggregator: AS 65001, Aggregator ID 10.1.1.2
 Advertised to such 3 peers:
    10.1.1.1
    10.1.3.2
    10.1.2.2
 BGP routing table entry information of 10.0.0.0/8:
 Summary automatic route
 Route Duration: 00h17m04s
 Direct Out-interface: NULL0
 Original nexthop: 127.0.0.1
 Qos information : 0x0
 AS-path Nil, origin incomplete, pref-val 0, valid, local, pre 255, not preferred for route type
 Aggregator: AS 65001, Aggregator ID 10.1.1.2
 Not advertised to any peer yet
```

The preceding command output shows that the summary route manually generated using the [**aggregate**](cmdqueryname=aggregate) command is selected as the optimal route.