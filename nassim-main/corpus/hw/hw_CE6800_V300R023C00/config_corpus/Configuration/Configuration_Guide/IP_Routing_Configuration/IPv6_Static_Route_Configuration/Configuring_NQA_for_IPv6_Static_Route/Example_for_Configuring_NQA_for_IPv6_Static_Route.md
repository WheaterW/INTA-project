Example for Configuring NQA for IPv6 Static Route
=================================================

Example for Configuring NQA for IPv6 Static Route

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130783468__fig_dc_vrp_static-route_disjoin_cfg_004201), DeviceA establishes an OSPFv3 neighbor relationship with each of DeviceB and DeviceC. Static routes to users are configured on DeviceB and DeviceC. DeviceB is the master device, and DeviceC is the backup device. Normally, traffic is transmitted over link A. If link A fails, traffic is switched to link B.

**Figure 1** NQA for IPv6 static route![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001931914744.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an ICMP NQA test instance to monitor the active link.
   
   Create an ICMP NQA test instance on the NQA client DeviceB to test whether the active link A to SwitchA is running properly.
2. Configure static routes and associate the static route along the active link with the NQA test instance.
   
   Configure static routes on DeviceB and DeviceC, and associate the static route configured on DeviceB with the NQA test instance. If the NQA test instance detects a link fault, it instructs the routing management module to delete the associated static route from the IPv6 routing table.
3. Configure a dynamic routing protocol.
   
   Configure a dynamic routing protocol on DeviceA, DeviceB, and DeviceC so that they can learn routes from one another.
4. Configure OSPFv3 to import static routes and set a smaller cost for the active link than that for the standby link.
   
   Configure OSPFv3 on DeviceB and DeviceC to import static routes, and set a higher cost for the static route imported by DeviceC than for the static route imported by DeviceB. After DeviceA learns routes to the same destination from DeviceB and DeviceC, it preferentially selects link B, which has a lower cost.

#### Procedure

1. Configure IPv6 addresses for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:1::1 64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:2::1 64
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Create an NQA test instance on DeviceB to monitor the link between DeviceB and SwitchA.
   
   
   ```
   [~DeviceB] nqa test-instance admin test
   [*DeviceB-nqa-admin-test] test-type icmp
   [*DeviceB-nqa-admin-test] destination-address ipv6 2001:db8:3::2
   [*DeviceB-nqa-admin-test] frequency 9
   [*DeviceB-nqa-admin-test] interval seconds 3
   [*DeviceB-nqa-admin-test] start now
   [*DeviceB-nqa-admin-test] quit
   [*DeviceB] commit
   ```
3. Configure IPv6 static routes.
   
   
   
   # Configure an IPv6 static route on DeviceB and associate it with the NQA test instance.
   
   ```
   [~DeviceB] ipv6 route-static 2001:db8:7:: 64 100ge 1/0/1 2001:db8:3::2 track nqa admin test
   [*DeviceB] commit
   ```
   
   # Configure an IPv6 static route on DeviceC.
   
   ```
   [~DeviceC] ipv6 route-static 2001:db8:7:: 64 100ge 1/0/1 2001:db8:6::2
   [*DeviceC] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The next hop address of the IPv6 static route configured on the local end must be the link-local address of the peer end, which can be obtained using the [**display ipv6 interface**](cmdqueryname=display+ipv6+interface) [ *interface-type* *interface-number* ] command on the peer end.
4. Configure a dynamic routing protocol on DeviceA, DeviceB, and DeviceC.
   
   
   
   # Configure OSPFv3 on DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure OSPFv3 on DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure OSPFv3 on DeviceC.
   
   ```
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
5. Configure OSPFv3 on DeviceB and DeviceC to import static routes.
   
   
   
   # Configure OSPFv3 on DeviceB to import a static route and set the cost to 10 for the static route.
   
   ```
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] import-route static cost 10
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] commit
   ```
   
   # Configure OSPFv3 on DeviceC to import a static route and set the cost to 20 for the static route.
   
   ```
   [~DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] import-route static cost 20
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Check NQA test results.

```
[~DeviceB] display nqa results test-instance admin test
 NQA entry(admin, test) : testflag is active ,testtype is icmp
  1 . Test 359 result     The test is finished
   Send operation times: 3                Receive response times: 3
   Completion:success                   RTD OverThresholds number:0
   Attempts number:1                      Drop operation number:0
   Disconnect operation number:0          Operation timeout number:0
   System busy operation number:0         Connection fail number:0
   Operation sequence errors number:0     RTT Stats errors number:0
   Destination ip address:2001:db8:3::2
   Min/Max/Average Completion Time: 1/3/2
   Sum/Square-Sum  Completion Time: 7/19
   Last Good Probe Time: 2012-11-14 12:15:22.3
   Lost packet ratio: 0 %
```

The command output shows "Lost packet ratio 0 %", indicating that the link is running properly.

# Check information about routes in the IPv6 routing table of DeviceB.

```
[~DeviceB] display ipv6 routing-table 2001:db8:7::
Routing Table : _public_
Summary Count : 1

Destination  : 2001:db8:7::                            PrefixLength : 64
NextHop      : 2001:db8:1::1                           Preference   : 60
Cost         : 0                                       Protocol     : Static
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/1                               Flags        : D
```

The command output contains the static route destined for 2001:db8:7::/64.

# Check information about the routing table of DeviceA.

```
[~DeviceA] display ipv6 routing-table 2001:db8:7::
Routing Table : _public_
Summary Count : 1

Destination  : 2001:db8:7::                            PrefixLength : 64
NextHop      : FE80::2200:10FF:FE03:0                  Preference   : 150
Cost         : 10                                      Protocol     : OSPFv3ASE
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/1                              Flags        : D
```

The command output shows that a route to 2001:db8:7::1/128 exists in the routing table. The outbound interface is 100GE 1/0/1 and the cost is 10. In this situation, service traffic is preferentially transmitted over link A.

# Shut down 100GE 1/0/2 on DeviceB to simulate a link fault.

```
[~DeviceB] interface 100ge 1/0/2
[~DeviceB-100GE1/0/2] shutdown
[*DeviceB-100GE1/0/2] quit
[*DeviceB] commit
```

# Check NQA test results.

```
[~DeviceB] display nqa results test-instance admin test
 NQA entry(admin, test) : testflag is active ,testtype is icmp
  1 . Test 1156 result    The test is finished
   Send operation times: 3                Receive response times: 0
   Completion:failed                    RTD OverThresholds number:0
   Attempts number:1                      Drop operation number:0
   Disconnect operation number:0          Operation timeout number:3
   System busy operation number:0         Connection fail number:0
   Operation sequence errors number:0     RTT Stats errors number:0
   Destination ip address:2001:db8:3::2
   Min/Max/Average Completion Time: 0/0/0
   Sum/Square-Sum  Completion Time: 0/0
   Last Good Probe Time: 0000-00-00 00:00:00.0
   Lost packet ratio: 100 %
```

The command output shows "Completion:failed" and "Lost packet ratio is 100 %", indicating that the link is faulty.

# Check information about the routing table of DeviceB.

```
[~DeviceB] display ipv6 routing-table 2001:db8:7::
Routing Table : _public_
Summary Count : 1

Destination  : 2001:db8:7::                            PrefixLength : 64
NextHop      : FE80::3A00:10FF:FE03:0                  Preference   : 150
Cost         : 20                                      Protocol     : OSPFv3ASE
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/1                               Flags        : D
```

The command output shows that the route type of 2001:db8:7::/64 has changed from a static route to an OSPFv3 route.

# Check information about the routing table of DeviceA.

```
[~DeviceA] display ipv6 routing-table 2001:db8:7::
Routing Table : _public_
Summary Count : 1

Destination  : 2001:db8:7::                            PrefixLength : 64
NextHop      : FE80::3A00:10FF:FE03:107                Preference   : 150
Cost         : 20                                      Protocol     : OSPFv3ASE
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/2                              Flags        : D
```

The static route is associated with the NQA test instance on DeviceB. When NQA detects a link fault, it rapidly notifies DeviceB that the associated static route is unavailable. In this case, DeviceA cannot learn the route to 2001:db8:7::/64 from DeviceB. However, DeviceA can learn the route to 2001:db8:7::/64 from DeviceC. The command output shows that the outbound interface of the route to 2001:db8:7::/64 is changed to 100GE1/0/2 and the cost is 20. Service traffic is switched to link B.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  ospfv3 1
   router-id 2.2.2.2
   import-route static cost 10
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
  # 
  ipv6 route-static 2001:db8:7:: 64  100GE1/0/1 2001:db8:3::2 track nqa admin test
  #
  nqa test-instance admin test
   test-type icmp
   destination-address ipv6 2001:db8:3::2
   interval seconds 3
   frequency 9
   start now
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  ospfv3 1
   router-id 3.3.3.3
   import-route static cost 20
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:6::1/64
  # 
  ipv6 route-static 2001:db8:7:: 64  100GE1/0/1 2001:db8:6::2
  #
  return
  ```