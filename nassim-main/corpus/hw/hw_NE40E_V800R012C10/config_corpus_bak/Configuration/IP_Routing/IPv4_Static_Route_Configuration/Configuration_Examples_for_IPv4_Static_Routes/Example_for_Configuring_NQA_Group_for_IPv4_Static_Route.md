Example for Configuring NQA Group for IPv4 Static Route
=======================================================

NQA group for IPv4 static route allows an NQA group to be associated with multiple NQA test instances to monitor multiple links, rapidly detect network faults, and control advertisement of IPv4 static routes, thereby implementing service switching.

#### Networking Requirements

NQA group for IPv4 static route monitors the link status of an IPv4 static route through association between the static route and an NQA group that consists of multiple NQA test instances. The RM module determines whether the static route is active based on the test result of the NQA group. If the IPv4 static route is inactive, the RM module deletes it from the IP routing table and selects an available backup link for data forwarding, which prevents lengthy service interruptions.

[Figure 1](#EN-US_TASK_0000001415953677__fig_dc_vrp_static-route_feature_001301) shows a network with redundant links.

* BGP peer relationships are established between Device A and Device B and between Device A and Device C.
* On Device B and Device C, default static routes are configured and imported into BGP, and different PrefVal values are configured so that Device B and Device C function as the master device and backup device, respectively.
* Device B and Device D are connected through two links by way of Device B1 and Device B2.
* In normal cases, traffic is transmitted along the primary link (Device B -> Device D).
* If the primary link fails (the NQA group bound to the default route of Device B considers the IPv4 static route inactive when monitoring the two links from Device B to Device D), traffic is switched to the backup link (Device C -> Device D).

**Figure 1** Network diagram of NQA group for IPv4 static route![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001366083320.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create NQA test instances of the ICMP type to detect faults on the primary link.
   
   Create two NQA test instances of the ICMP type between Device B and Device B1 and between Device B and Device B2 to correspond to the two links between Device B and Device D and to check whether the primary link (Device B -> Device D) is running properly.
2. Create an NQA group.
   
   Bind the two NQA test instances of the ICMP type to the NQA group.
3. Configure static routes and associate the static route along the primary link with the NQA group.
   
   Configure IPv4 static routes to loopback0 interfaces between Device A and Device B, and between Device A and Device C. Configure default IPv4 static routes on Device B and Device C. Associate the IPv4 static route configured on Device B with the NQA group, which collects the detection results of two NQA test instances to determine its status. When the NQA group goes down, the device determines that the current link is faulty and instructs the RM module to delete the IPv4 static route from the IP routing table.
4. Configure BGP.
   
   Configure BGP on Device A, Device B, and Device C so that they can learn routes from each other.
5. Configure BGP to import IPv4 static routes and set a larger PrefVal value for the primary link.
   
   Configure BGP on Device B and Device C to import IPv4 static routes, and set a larger PrefVal value for the IPv4 static route imported by Device B. When Device A learns routes to the same destination from Device B and Device C, it preferentially selects the link (Device B -> Device D), which has a larger PrefVal value.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface
* NQA-related configurations (for details, see [Table 1](#EN-US_TASK_0000001415953677__table_02))
  
  **Table 1** NQA parameter values
  | Item | Value |
  | --- | --- |
  | Administrator name | user1, user2 |
  | Test instance name | test1, test2 |
  | Test type | ICMP |
  | Destination address | 172.16.1.2, 172.16.2.2 |
  | Test interval | 10s |
  | Number of probes | 2 |
  | Interval at which packets are sent | 5s |
  | Timeout period | 4s |
* Operation type between test instances in the NQA group: OR
* BGP AS numbers (the same) and router IDs of Device A, Device B, and Device C (1.1.1.1, 2.2.2.2, and 3.3.3.3, respectively)

#### Procedure

1. Configure IP addresses. For details, see [Configuration Files](#EN-US_TASK_0000001415953677__title_01).
2. On Device B, configure two NQA test instances of the ICMP type between Device B and Device B1 and between Device B and Device B2.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] nqa test-instance user1 test1
   ```
   ```
   [*DeviceB-nqa-user1-test1] test-type icmp
   ```
   ```
   [*DeviceB-nqa-user1-test1] destination-address ipv4 172.16.1.2
   ```
   ```
   [*DeviceB-nqa-user1-test1] frequency 10
   ```
   ```
   [*DeviceB-nqa-user1-test1] probe-count 2
   ```
   ```
   [*DeviceB-nqa-user1-test1] interval seconds 5
   ```
   ```
   [*DeviceB-nqa-user1-test1] timeout 4
   ```
   ```
   [*DeviceB-nqa-user1-test1] start now
   ```
   ```
   [*DeviceB-nqa-user1-test1] commit
   ```
   ```
   [~DeviceB-nqa-user1-test1] quit
   ```
   ```
   [~DeviceB] nqa test-instance user2 test2
   ```
   ```
   [*DeviceB-nqa-user2-test2] test-type icmp
   ```
   ```
   [*DeviceB-nqa-user1-test1] destination-address ipv4 172.16.2.2
   ```
   ```
   [*DeviceB-nqa-user2-test2] frequency 10
   ```
   ```
   [*DeviceB-nqa-user2-test2] probe-count 2
   ```
   ```
   [*DeviceB-nqa-user2-test2] interval seconds 5
   ```
   ```
   [*DeviceB-nqa-user2-test2] timeout 4
   ```
   ```
   [*DeviceB-nqa-user2-test2] start now
   ```
   ```
   [*DeviceB-nqa-user2-test2] commit
   ```
   ```
   [~DeviceB-nqa-user2-test2] quit
   ```
3. Create an NQA group and bind the two NQA test instances of the ICMP type to the group.
   
   
   ```
   [~DeviceB] nqa group group1
   ```
   ```
   [*DeviceB-nqa-group-group1] nqa test-instance user1 test1
   ```
   ```
   [*DeviceB-nqa-group-group1] nqa test-instance user2 test2
   ```
   ```
   [*DeviceB-nqa-group-group1] operator or
   ```
   ```
   [*DeviceB-nqa-group-group1] commit
   ```
   ```
   [~DeviceB-nqa-group-group1] quit
   ```
4. Configure static routes.
   
   
   
   # Configure static routes to loopback interfaces between Device A and Device B, and between Device A and Device C.
   
   ```
   [~DeviceA] ip route-static 2.2.2.2 255.255.255.255 GigabitEthernet 0/1/0 172.16.3.2 
   ```
   ```
   [~DeviceA] ip route-static 3.3.3.3 255.255.255.255 GigabitEthernet 0/1/1 172.16.4.2 
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure a static route to the loopback interface of Device A on Device B.
   
   ```
   [~DeviceB] ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet 0/1/0 172.16.3.1 
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure a static route to the loopback interface of Device A on Device C.
   
   ```
   [~DeviceC] ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet 0/1/1 172.16.4.1 
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure a default static route on Device B and associate it with the NQA group.
   
   ```
   [*DeviceB] ip route-static 0.0.0.0 32 NULL0 track nqa-group group1
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure a default static route on Device C.
   
   ```
   [*DeviceC] ip route-static 0.0.0.0 32 NULL0
   ```
   ```
   [*DeviceC] commit
   ```
5. Configure BGP on Device A, Device B, and Device C.
   
   
   
   # Configure BGP on Device A.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*DeviceA-bgp] peer 2.2.2.2 connect-interface Loopback0
   ```
   ```
   [*DeviceA-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*DeviceA-bgp] peer 3.3.3.3 connect-interface Loopback0
   ```
   ```
   [*DeviceA-bgp] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure BGP on Device B.
   
   ```
   [~DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 1.1.1.1 connect-interface Loopback0
   ```
   ```
   [*DeviceB-bgp] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure BGP on Device C.
   
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*DeviceC-bgp] peer 1.1.1.1 connect-interface Loopback0
   ```
   ```
   [*DeviceC-bgp] quit
   ```
   ```
   [*DeviceC] commit
   ```
6. Configure BGP on Device B and Device C to import IPv4 static routes, and set a larger PrefVal value for the primary link.
   
   
   
   # Configure BGP on Device B to import IPv4 static routes, and set the PrefVal value to 200.
   
   ```
   [~DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] import-route static
   ```
   ```
   [*DeviceB-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv4] peer 1.1.1.1 preferred-value 200
   ```
   ```
   [*DeviceB-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure BGP on Device C to import IPv4 static routes, and set the PrefVal value to 100.
   
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] import-route static
   ```
   ```
   [*DeviceC-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv4] peer 1.1.1.1 preferred-value 100
   ```
   ```
   [*DeviceC-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceC-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
7. Verify the configuration.
   
   
   
   # Check the results of the two NQA test instances on Device B.
   
   ```
   [~DeviceB] display nqa results test-instance user1 test1
   ```
   ```
   NQA entry(user1, test1) :testflag is inactive ,testtype is icmp
     1 . Test 1 result   The test is finished
      Send operation times: 3                Receive response times: 3
      Completion:success                   RTD OverThresholds number:0
      Attempts number:1                      Drop operation number:0
      Disconnect operation number:0          Operation timeout number:0
      System busy operation number:0         Connection fail number:0
      Operation sequence errors number:0     RTT Status errors number:0
      Destination ip address:172.16.1.2
      Min/Max/Average Completion Time: 11/185/69
      Sum/Square-Sum  Completion Time: 207/34467
      Last Good Probe Time: 2022-09-24 15:08:38.6
      Lost packet ratio: 0 %
   ```
   ```
   [~DeviceB] display nqa results test-instance user2 test2
   ```
   ```
   NQA entry(user2, test2) :testflag is inactive ,testtype is icmp
     1 . Test 1 result   The test is finished
      Send operation times: 3                Receive response times: 3
      Completion:success                   RTD OverThresholds number:0
      Attempts number:1                      Drop operation number:0
      Disconnect operation number:0          Operation timeout number:0
      System busy operation number:0         Connection fail number:0
      Operation sequence errors number:0     RTT Status errors number:0
      Destination ip address:172.16.2.2
      Min/Max/Average Completion Time: 9/16/11
      Sum/Square-Sum  Completion Time: 34/418
      Last Good Probe Time: 2022-09-24 15:08:50.3
      Lost packet ratio: 0 %
   ```
   
   The command output shows "Lost packet ratio 0 %," indicating that the link is running properly.
   
   # Check the test result of the NQA group on Device B.
   
   ```
   [~DeviceB] display nqa group
   ```
   ```
   NQA-group information:
   ------------------------------------------------------------------------
   NQA-group group1
   Status: UP         Operator: OR
   ------------------------------------------------------------------------
   Admin-name                       Test-name                        Status
   ------------------------------------------------------------------------
   user1                           test1                             UP
   user2                           test2                             UP
   ```
   
   # Check the routing table of Device A.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 14       Routes : 14
    
   Destination/Mask    Proto   Pre  Cost        Flags NextHop                    Interface
    
           0.0.0.0/32  IBGP    255  0             RD  2.2.2.2                   GigabitEthernet0/1/0
           1.1.1.1/32  Direct  0    0             D   127.0.0.1                  LoopBack0
           2.2.2.2/32  Static  60   0             D   172.16.3.2                 GigabitEthernet0/1/0
           3.3.3.3/32  Static  60   0             D   172.16.4.2                 GigabitEthernet0/1/1
         127.0.0.0/8   Direct  0    0             D   127.0.0.1                  InLoopBack0
         127.0.0.1/32  Direct  0    0             D   127.0.0.1                  InLoopBack0
   127.255.255.255/32  Direct  0    0             D   127.0.0.1                  InLoopBack0
        172.16.3.0/24  Direct  0    0             D   172.16.3.1                 GigabitEthernet0/1/0
        172.16.3.1/32  Direct  0    0             D   127.0.0.1                  GigabitEthernet0/1/0
      172.16.3.255/32  Direct  0    0             D   127.0.0.1                  GigabitEthernet0/1/0
        172.16.4.0/24  Direct  0    0             D   172.16.4.1                 GigabitEthernet0/1/1
        172.16.4.1/32  Direct  0    0             D   127.0.0.1                  GigabitEthernet0/1/1
      172.16.4.255/32  Direct  0    0             D   127.0.0.1                  GigabitEthernet0/1/1
   255.255.255.255/32  Direct  0    0             D   127.0.0.1                  InLoopBack0
   ```
   
   The command output shows that the next hop used to forward user traffic on Device A is Device B, indicating that user traffic is transmitted along the primary link.
   
   # Shut down GigabitEthernet 0/1/1 on Device B to simulate a link fault.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB] quit
   ```
   
   # Check the NQA test result.
   
   ```
   [~DeviceB] display nqa results test-instance user1 test1
   ```
   ```
   NQA entry(user1, test1) :testflag is inactive ,testtype is icmp
     2 . Test 2 result   The test is finished
      Send operation times: 3                Receive response times: 0
      Completion:failed                    RTD OverThresholds number:0
      Attempts number:1                      Drop operation number:0
      Disconnect operation number:0          Operation timeout number:3
      System busy operation number:0         Connection fail number:0
      Operation sequence errors number:0     RTT Status errors number:0
      Destination ip address:172.16.1.2
      Min/Max/Average Completion Time: 0/0/0
      Sum/Square-Sum  Completion Time: 0/0
      Last Good Probe Time: 0000-00-00 00:00:00.0
      Lost packet ratio: 100 %
   ```
   
   "Completion:failed" and "Lost packet ratio: 100%" are displayed, indicating that the link where GigabitEthernet 0/1/1 resides is faulty.
   
   # Check the test result of the NQA group on Device B.
   
   ```
   [~DeviceB] display nqa group
   ```
   ```
   NQA-group information:
   ------------------------------------------------------------------------
   NQA-group group1
   Status: UP         Operator: OR
   ------------------------------------------------------------------------
   Admin-name                       Test-name                        Status
   ------------------------------------------------------------------------
   user1                           test1                             DOWN
   user2                           test2                             UP
   ```
   
   The operation type between test instances in the NQA group is OR. Therefore, the status of the NQA group remains UP.
   
   # Check the routing table of Device A.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 14       Routes : 14
    
   Destination/Mask    Proto   Pre  Cost        Flags NextHop                    Interface
    
           0.0.0.0/32  IBGP    255  0             RD  2.2.2.2                   GigabitEthernet0/1/0
           1.1.1.1/32  Direct  0    0             D   127.0.0.1                  LoopBack0
           2.2.2.2/32  Static  60   0             D   172.16.3.2                 GigabitEthernet0/1/0
           3.3.3.3/32  Static  60   0             D   172.16.4.2                 GigabitEthernet0/1/1
         127.0.0.0/8   Direct  0    0             D   127.0.0.1                  InLoopBack0
         127.0.0.1/32  Direct  0    0             D   127.0.0.1                  InLoopBack0
   127.255.255.255/32  Direct  0    0             D   127.0.0.1                  InLoopBack0
        172.16.3.0/24  Direct  0    0             D   172.16.3.1                 GigabitEthernet0/1/0
        172.16.3.1/32  Direct  0    0             D   127.0.0.1                  GigabitEthernet0/1/0
      172.16.3.255/32  Direct  0    0             D   127.0.0.1                  GigabitEthernet0/1/0
        172.16.4.0/24  Direct  0    0             D   172.16.4.1                 GigabitEthernet0/1/1
        172.16.4.1/32  Direct  0    0             D   127.0.0.1                  GigabitEthernet0/1/1
      172.16.4.255/32  Direct  0    0             D   127.0.0.1                  GigabitEthernet0/1/1
   255.255.255.255/32  Direct  0    0             D   127.0.0.1                  InLoopBack0
   ```
   
   The command output shows that the next hop used to forward user traffic on Device A is still Device B, indicating that user traffic is transmitted along the primary link.
   
   # Shut down GigabitEthernet 0/1/2 on Device B to simulate a link fault.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/1/2
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/2] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceB] quit
   ```
   
   # Check the NQA test result.
   
   ```
   [~DeviceB] display nqa results test-instance user1 test1
   ```
   ```
   NQA entry(user2, test2) : testflag is active ,testtype is icmp
     1 . Test 186 result   The test is finished
      Send operation times: 2                Receive response times: 0
      Completion:failed                    RTD OverThresholds number:0
      Attempts number:1                      Drop operation number:0
      Disconnect operation number:0          Operation timeout number:2
      System busy operation number:0         Connection fail number:0
      Operation sequence errors number:0     RTT Stats errors number:0
      Destination ip address:172.16.2.2
      Min/Max/Average Completion Time: 0/0/0
      Sum/Square-Sum  Completion Time: 0/0
      Last Good Probe Time: 0000-00-00 00:00:00.0
      Lost packet ratio: 100 %
   ```
   
   "Completion:failed" and "Lost packet ratio: 100%" are displayed, indicating that the link where GigabitEthernet 0/1/2 resides is faulty.
   
   # Check the test result of the NQA group on Device B.
   
   ```
   [~DeviceB] display nqa group
   ```
   ```
   NQA-group information:
   ------------------------------------------------------------------------
   NQA-group group1
   Status: DOWN       Operator: OR
   ------------------------------------------------------------------------
   Admin-name                       Test-name                        Status
   ------------------------------------------------------------------------
   user1                           test1                             DOWN
   user2                           test2                             DOWN
   ```
   
   The command output shows that the status of the NQA group changes to DOWN.
   
   # Check the routing table of Device A.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 14       Routes : 14
    
   Destination/Mask    Proto   Pre  Cost        Flags NextHop                     Interface
    
           0.0.0.0/32  IBGP    255  0             RD  3.3.3.3                    GigabitEthernet0/1/1
           1.1.1.1/32  Direct  0    0             D   127.0.0.1                   LoopBack0
           2.2.2.2/32  Static  60   0             D   172.16.3.2                  GigabitEthernet0/1/0
           3.3.3.3/32  Static  60   0             D   172.16.4.2                  GigabitEthernet0/1/1
         127.0.0.0/8   Direct  0    0             D   127.0.0.1                   InLoopBack0
         127.0.0.1/32  Direct  0    0             D   127.0.0.1                   InLoopBack0
   127.255.255.255/32  Direct  0    0             D   127.0.0.1                   InLoopBack0
        172.16.3.0/24  Direct  0    0             D   172.16.3.1                  GigabitEthernet0/1/0
        172.16.3.1/32  Direct  0    0             D   127.0.0.1                   GigabitEthernet0/1/0
      172.16.3.255/32  Direct  0    0             D   127.0.0.1                   GigabitEthernet0/1/0
        172.16.4.0/24  Direct  0    0             D   172.16.4.1                  GigabitEthernet0/1/1
        172.16.4.1/32  Direct  0    0             D   127.0.0.1                   GigabitEthernet0/1/1
      172.16.4.255/32  Direct  0    0             D   127.0.0.1                   GigabitEthernet0/1/1
   255.255.255.255/32  Direct  0    0             D   127.0.0.1                   InLoopBack0
   ```
   
   The command output shows that the next hop used to forward user traffic on Device A changes to Device C, indicating that the traffic is switched to the backup link.
   
   The NQA group on Device B is associated with the IPv4 static route. When the NQA group detects that both links from Device B to Device D fail, the NQA group goes down and rapidly notifies Device B that the associated IPv4 static route is unavailable. Service traffic is then switched to the backup link.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  router id 1.1.1.1
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  interface GigabitEthernet 0/1/0
   ip address 172.16.3.1 255.255.255.0
  #
  interface GigabitEthernet 0/1/1
   ip address 172.16.4.1 255.255.255.0
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0 
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  # 
  ip route-static 2.2.2.2 255.255.255.255 GigabitEthernet 0/1/0 172.16.3.2
  ip route-static 3.3.3.3 255.255.255.255 GigabitEthernet 0/1/1 172.16.4.2
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  router id 2.2.2.2
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  interface GigabitEthernet 0/1/0
   ip address 172.16.3.2 255.255.255.0
  #
  interface GigabitEthernet 0/1/1
   ip address 172.16.1.1 255.255.255.0
  #
  interface GigabitEthernet 0/1/2
   ip address 172.16.2.1 255.255.255.0
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    import-route static
    peer 1.1.1.1 preferred-value 200
  #
  ip route-static 0.0.0.0 32 NULL0 track nqa-group group1
  ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet 0/1/0 172.16.3.1
  #
  nqa test-instance user1 test1
   test-type icmp
   destination-address ipv4 172.16.1.2
   interval seconds 5
   timeout 4
   probe-count 2
   frequency 10
   start now
  #
  nqa test-instance user2 test2
   test-type icmp
   destination-address ipv4 172.16.2.2
   interval seconds 5
   timeout 4
   probe-count 2
   frequency 10
   start now
  #
  nqa group group1
   nqa test-instance user1 test1
   nqa test-instance user2 test2
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  router id 3.3.3.3
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  interface GigabitEthernet0/1/0
   ip address 172.16.6.1 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   ip address 172.16.4.2 255.255.255.0
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    import-route static
    peer 1.1.1.1 preferred-value 100
  #
  ip route-static 0.0.0.0 32 NULL0
  ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet0/1/1 172.16.4.1
  #
  return
  ```