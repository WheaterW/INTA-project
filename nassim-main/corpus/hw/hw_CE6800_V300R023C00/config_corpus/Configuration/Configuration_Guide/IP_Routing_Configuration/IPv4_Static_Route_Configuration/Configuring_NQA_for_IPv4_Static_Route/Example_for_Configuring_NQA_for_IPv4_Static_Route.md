Example for Configuring NQA for IPv4 Static Route
=================================================

Example for Configuring NQA for IPv4 Static Route

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130622970__fig5524221141413), an OSPF neighbor relationship is established between DeviceA and each of DeviceB and DeviceC. Static routes are configured on DeviceB and DeviceC. OSPF imports static routes on DeviceB and DeviceC. Preference values are set for the imported routes on DeviceB and DeviceC so that DeviceB functions as the master device, and DeviceC functions as the backup device. If no fault occurs, service traffic is transmitted through the active link A. If the active link fails, service traffic is quickly switched to the standby link B. BFD for static route cannot be deployed on the network. Therefore, NQA is used to monitor the IPv4 static routes. DeviceA, DeviceB, and DeviceC reside in the OSPF backbone area (area 0), and their router IDs are 1.1.1.1, 2.2.2.2, and 3.3.3.3, respectively.**Figure 1** Network diagram of NQA for IPv4 static route![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130782788.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each device.
2. Create an ICMP NQA test instance to monitor the active link.
   
   Create an ICMP NQA test instance on the NQA client DeviceB to test whether the active link to SwitchA is running properly.
3. Configure static routes and associate the static route along the active link with the ICMP NQA test instance.
   
   Configure static routes on DeviceB and DeviceC, and associate the static route configured on DeviceB with the ICMP NQA test instance. If the ICMP NQA test instance detects a link fault, it instructs the routing management module to delete the associated static route from the IPv4 routing table.
4. Configure OSPF.
   
   Configure OSPF on DeviceA, DeviceB, and DeviceC so that they can learn routes from one another.
5. Configure OSPF to import static routes and set a smaller cost for the static route along the primary link than for the one along the backup link.
   
   Configure OSPF on DeviceB and DeviceC to import static routes, and set a higher cost for the static route imported by DeviceC than for the static route imported by DeviceB. After DeviceA learns routes to the same destination from DeviceB and DeviceC, DeviceA preferentially selects the link DeviceB -> SwitchA with a lower cost.

#### Procedure

1. Configure IPv4 addresses for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 172.16.3.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 172.16.4.1 255.255.255.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130622970__postreq24192593172748).
2. Create an ICMP NQA test instance to monitor the active link.
   
   
   
   # Create an NQA test instance on DeviceB to monitor the link between DeviceB and SwitchA.
   
   ```
   [~DeviceB] nqa test-instance user test
   [*DeviceB-nqa-user-test] test-type icmp
   [*DeviceB-nqa-user-test] destination-address ipv4 172.16.1.2
   [*DeviceB-nqa-user-test] frequency 10
   [*DeviceB-nqa-user-test] probe-count 2
   [*DeviceB-nqa-user-test] interval seconds 5
   [*DeviceB-nqa-user-test] timeout 4
   [*DeviceB-nqa-user-test] start now
   [*DeviceB-nqa-user-test] quit
   [*DeviceB] commit
   ```
3. Configure static routes and associate the static route along the active link with the ICMP NQA test instance.
   
   
   
   # On DeviceB, configure an IPv4 static route with SwitchA as a next hop and associate the IPv4 static route with the NQA test instance named **test**.
   
   ```
   [~DeviceB] ip route-static 172.16.7.0 255.255.255.0 100ge 1/0/2 172.16.1.2 track nqa user test
   [*DeviceB] commit
   ```
   
   # On DeviceC, configure an IPv4 static route to SwitchA.
   
   ```
   [~DeviceC] ip route-static 172.16.7.0 255.255.255.0 100ge 1/0/1 172.16.6.2
   [*DeviceC] commit
   ```
4. Configure a dynamic routing protocol.
   
   
   
   # Configure OSPF on DeviceA.
   
   ```
   [~DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0.0.0.0
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.16.3.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.16.4.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130622970__postreq24192593172748).
5. Configure OSPF to import static routes and set a smaller cost for the static route along the primary link than for the one along the backup link.
   
   
   
   # Configure OSPF on DeviceB to import a static route and set the cost to 10 for the static route.
   
   ```
   [~DeviceB] ospf 1
   [*DeviceB-ospf-1] import-route static cost 10
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure OSPF on DeviceC to import a static route and set the cost to 20 for the static route.
   
   ```
   [~DeviceC] ospf 1
   [*DeviceC-ospf-1] import-route static cost 20
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Check the NQA test result on DeviceB.

```
[~DeviceB] display nqa results test-instance user test
 NQA entry(user, test) : testflag is active ,testtype is icmp
  1 . Test 6645 result   The test is finished
   Send operation times: 2                Receive response times: 2
   Completion:success                   RTD OverThresholds number:0
   Attempts number:1                      Drop operation number:0
   Disconnect operation number:0          Operation timeout number:0
   System busy operation number:0         Connection fail number:0
   Operation sequence errors number:0     RTT Stats errors number:0
   Destination ip address:172.16.1.2
   Min/Max/Average Completion Time: 1/1/1
   Sum/Square-Sum  Completion Time: 2/2
   Last Good Probe Time: 2012-11-14 04:20:36.9
   Lost packet ratio: 0 %
```

The command output contains "Lost packet ratio: 0%", indicating that link A is working properly.

# Check the routing table of DeviceA.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 11       Routes : 11

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

      127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
     172.16.3.0/24  Direct  0    0             D  172.16.3.1      100GE1/0/1
     172.16.3.1/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
   172.16.3.255/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
     172.16.4.0/24  Direct  0    0             D  172.16.4.1      100GE1/0/2
     172.16.4.1/32  Direct  0    0             D  127.0.0.1       100GE1/0/2
   172.16.4.255/32  Direct  0    0             D  127.0.0.1       100GE1/0/2
     172.16.7.0/24  O_ASE   150  10       D  172.16.3.2    100GE1/0/1
255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
```

The command output shows that the next hop of the route from DeviceA to SwitchA is DeviceB, and the traffic destined for the users is transmitted over link A.

# Shut down 100GE 1/0/2 on DeviceB to simulate a link fault.

```
[~DeviceB] interface 100ge 1/0/2
[~DeviceB-100GE1/0/2] shutdown
[*DeviceB-100GE1/0/2] quit
[*DeviceB] commit
```

# Check the NQA test result on DeviceB.

```
[~DeviceB] display nqa results test-instance user test
 NQA entry(user, test) : testflag is active ,testtype is icmp
  1 . Test 7160 result   The test is finished
   Send operation times: 2                Receive response times: 0
   Completion:failed                    RTD OverThresholds number:0
   Attempts number:1                      Drop operation number:0
   Disconnect operation number:0          Operation timeout number:2
   System busy operation number:0         Connection fail number:0
   Operation sequence errors number:0     RTT Stats errors number:0
   Destination ip address:172.16.1.2
   Min/Max/Average Completion Time: 0/0/0
   Sum/Square-Sum  Completion Time: 0/0
   Last Good Probe Time: 0000-00-00 00:00:00.0
   Lost packet ratio: 100 %
```

The command output contains "Completion:failed" and "Lost packet ratio is 100 %", indicating that link A is faulty.

# Check the routing table of DeviceA.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 11       Routes : 11

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

      127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
     172.16.3.0/24  Direct  0    0             D  172.16.3.1      100GE1/0/1
     172.16.3.1/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
   172.16.3.255/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
     172.16.4.0/24  Direct  0    0             D  172.16.4.1      100GE1/0/2
     172.16.4.1/32  Direct  0    0             D  127.0.0.1       100GE1/0/2
   172.16.4.255/32  Direct  0    0             D  127.0.0.1       100GE1/0/2
  172.16.7.0/24  O_ASE   150  20          D  172.16.4.2    100GE1/0/2
255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
```

The command output shows that the next hop of the route from DeviceA to SwitchA is DeviceC, and the traffic destined for the users is transmitted over link B.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.3.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.4.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 172.16.3.0 0.0.0.255
    network 172.16.4.0 0.0.0.255
  # 
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  router id 2.2.2.2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.3.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  ospf 1
   import-route static cost 10
   area 0.0.0.0
    network 172.16.3.0 0.0.0.255
  # 
  ip route-static 172.16.7.0 255.255.255.0 100GE1/0/2 172.16.1.2 track nqa user test
  #
  nqa test-instance user test
   test-type icmp
   destination-address ipv4 172.16.1.2
   interval seconds 5
   timeout 4
   probe-count 2
   frequency 10
   start now
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  router id 3.3.3.3
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.6.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.4.2 255.255.255.0
  #
  ospf 1
   import-route static cost 20
   area 0.0.0.0
    network 172.16.4.0 0.0.0.255
  # 
  ip route-static 172.16.7.0 255.255.255.0 100GE1/0/1 172.16.6.2
  #
  return
  ```