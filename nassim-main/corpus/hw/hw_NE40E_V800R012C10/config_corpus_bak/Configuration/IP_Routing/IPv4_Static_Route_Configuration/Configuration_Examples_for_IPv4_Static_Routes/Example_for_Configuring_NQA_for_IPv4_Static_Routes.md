Example for Configuring NQA for IPv4 Static Routes
==================================================

NQA for IPv4 static routes can fast detect network faults and control the advertisement of static routes.

#### Networking Requirements

On a simple network or when the Router cannot use a dynamic routing protocol to generate routes, you can configure static routes. Unlike dynamic routing protocols, static routes do not have a detection mechanism. If a link fails, a network administrator must manually delete the corresponding static route from the IP routing table, which delays link switchovers and causes a lengthy service interruption.

Bidirectional Forwarding Detection (BFD) for static routes is adaptable to link changes but requires that both ends of a link support BFD. If either end of a link does not support BFD, configure NQA for IPv4 static routes. If an NQA test instance detects a link fault, it instructs the routing management module to delete the associated static route from the IPv4 routing table. Then traffic is switched to a backup route to prevent lengthy service interruptions.

In [Figure 1](#EN-US_TASK_0172365461__fig_dc_vrp_static-route_disjoin_cfg_004101), backup links are deployed on the IP metropolitan area network (MAN).

* Static routes are configured on DeviceB and DeviceC. DeviceB is the active device, while DeviceC is the standby device.
* In most cases, traffic is transmitted over the primary link (DeviceB -> SwitchA).
* If the primary link fails, traffic switches to the backup link (DeviceC -> SwitchA).

**Figure 1** NQA for IPv4 static routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 5 in this example represent GE 0/1/0, GE 0/1/1, GE 0/1/2, GE 0/1/3, and GE 0/2/3, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_004101.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, switches A and B are used for user access. In actual networking, users can also access the network through the OLT, DSLAM, MSAN, or xDSL. The configurations on DeviceA, DeviceB, and DeviceC are the same.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Internet Control Message Protocol (ICMP) NQA test instance to monitor the status of the primary link.
   
   Create an ICMP NQA test instance on the NQA client DeviceB to test whether the primary link is running properly.
2. Configure static routes and associate the static route along the primary link with the ICMP NQA test instance.
   
   Configure static routes on DeviceB and DeviceC, and associate the static route configured on DeviceB with the ICMP NQA test instance. If the ICMP NQA test instance detects a link fault, it instructs the routing management module to delete the associated static route from the IPv4 routing table.
3. Configure a dynamic routing protocol.
   
   Configure a dynamic routing protocol on DeviceA, DeviceB, and DeviceC so that they can learn routes from one another.
4. Configure OSPF to import static routes and set a smaller cost for the static route along the primary link than for the one along the backup link.
   
   Configure OSPF on DeviceB and DeviceC to import static routes, and set a higher cost for the static route imported by DeviceC than for the one imported by DeviceB. This configuration allows DeviceA to preferentially select the link (DeviceB -> SwitchA).

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface
* NQA item values (for details, see [Table 1](#EN-US_TASK_0172365461__table_02))
  
  **Table 1** NQA item values
  | Item | Value |
  | --- | --- |
  | Administrator name | user |
  | Name of the test instance | test |
  | Test type | ICMP |
  | Destination address | 172.16.1.2 |
  | Interval at which the NQA test automatically runs | 10 seconds |
  | Number of probes | 2 |
  | Interval at which probe packets are sent | 5 seconds |
  | Timeout period | 4 seconds |
* OSPF backbone area (Area 0) of DeviceA, DeviceB, and DeviceC, and their router IDs (1.1.1.1, 2.2.2.2, and 3.3.3.3)

#### Procedure

1. Configure interface IPv4 addresses. For configuration details, see [Configuration Files](#EN-US_TASK_0172365461__title_01) in this section.
2. Create an NQA test instance on DeviceB to test the link between DeviceB and SwitchA.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] nqa test-instance user test
   ```
   ```
   [*DeviceB-nqa-user-test] test-type icmp
   ```
   ```
   [*DeviceB-nqa-user-test] destination-address ipv4 172.16.1.2
   ```
   ```
   [*DeviceB-nqa-user-test] frequency 10
   ```
   ```
   [*DeviceB-nqa-user-test] probe-count 2
   ```
   ```
   [*DeviceB-nqa-user-test] interval seconds 5
   ```
   ```
   [*DeviceB-nqa-user-test] timeout 4
   ```
   ```
   [*DeviceB-nqa-user-test] start now
   ```
   ```
   [*DeviceB-nqa-user-test] commit
   ```
   ```
   [~DeviceB-nqa-user-test] quit
   ```
3. Configure IPv4 static routes.
   
   
   
   # Configure an IPv4 static route on DeviceB and associate it with the NQA test instance.
   
   ```
   [~DeviceB] ip route-static 172.16.7.0 255.255.255.0 GigabitEthernet 0/1/1 172.16.1.2 track nqa user test
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure an IPv4 static route on DeviceC.
   
   ```
   [~DeviceC] ip route-static 172.16.7.0 255.255.255.0 GigabitEthernet 0/1/0 172.16.6.2
   ```
   ```
   [*DeviceC] commit
   ```
4. Configure a dynamic routing protocol on DeviceA, DeviceB, and DeviceC. OSPF is used in this example.
   
   
   
   # Configure OSPF on DeviceA.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0.0.0.0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.16.3.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.16.4.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospf-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure OSPF on DeviceB.
   
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0.0.0.0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 172.16.3.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospf-1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure OSPF on DeviceC.
   
   ```
   [~DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] area 0.0.0.0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 172.16.4.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceC-ospf-1] quit
   ```
   ```
   [*DeviceC] commit
   ```
5. Configure OSPF on DeviceB and DeviceC to import static routes.
   
   
   
   # Configure OSPF on DeviceB to import a static route, and set the cost to 10 for the static route.
   
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] import-route static cost 10
   ```
   ```
   [*DeviceB-ospf-1] commit
   ```
   ```
   [~DeviceB-ospf-1] quit
   ```
   
   # Configure OSPF on DeviceC to import a static route, and set the cost to 20 for the static route.
   
   ```
   [~DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] import-route static cost 20
   ```
   ```
   [*DeviceC-ospf-1] commit
   ```
   ```
   [~DeviceC-ospf-1] quit
   ```
6. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display current-configuration | include nqa** command on DeviceB in the system view. The command output shows that the IPv4 static route has been associated with the NQA test instance. Run the **display nqa results** command. The command output shows that an NQA test instance has been created.
   
   # Display configurations of NQA for IPv4 static routes.
   
   ```
   [~DeviceB] display current-configuration | include nqa
   ```
   ```
    ip route-static 172.16.7.0 255.255.255.0 GigabitEthernet 0/1/1 172.16.1.2 track nqa user test
    nqa test-instance user test
   ```
   
   # Display NQA test results.
   
   ```
   [~DeviceB] display nqa results test-instance user test
   ```
   ```
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
   
   The command output shows "Lost packet ratio 0 %," indicating that the link is running properly.
   
   # Display the routing table on DeviceB.
   
   ```
   [~DeviceB] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 15       Routes : 15
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
        172.16.1.0/24  Direct  0    0             D  172.16.1.1      GigabitEthernet0/1/1
        172.16.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/1
      172.16.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/1
        172.16.3.0/24  Direct  0    0             D  172.16.3.2      GigabitEthernet0/1/0
        172.16.3.2/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
      172.16.3.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
        172.16.4.0/24  OSPF    10   2             D  172.16.3.1      GigabitEthernet0/1/0
        172.16.5.0/24  Direct  0    0             D  172.16.5.1      GigabitEthernet0/1/3
        172.16.5.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/3
      172.16.5.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/3
      172.16.7.0/24  Static  60   0             D  172.16.1.2      GigabitEthernet0/1/1
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```
   
   The command output shows that the static route exists in the routing table.
   
   # Display the routing table on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 11       Routes : 11
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
        172.16.3.0/24  Direct  0    0             D  172.16.3.1      GigabitEthernet0/1/0
        172.16.3.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
      172.16.3.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
        172.16.4.0/24  Direct  0    0             D  172.16.4.1      GigabitEthernet0/2/3
        172.16.4.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/3
      172.16.4.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/3
        172.16.7.0/24  O_ASE   150  10            D  172.16.3.2     GigabitEthernet0/1/0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```
   
   The command output shows that a route to 172.16.7.0/24 exists in the routing table. The route's next hop address is 172.16.3.2 and the cost is 10. Traffic is preferentially transmitted along the link DeviceB -> SwitchA.
   
   # Shut down GE 0/1/1 on DeviceB to simulate a link fault.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB] quit
   ```
   
   # Display NQA test results.
   
   ```
   [~DeviceB] display nqa results test-instance user test
   ```
   ```
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
   
   The command output shows "Completion:failed" and "Lost packet ratio is 100 %," indicating that the link is faulty.
   
   # Display the routing table on DeviceB.
   
   ```
   [~DeviceB] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 12       Routes : 12
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
        172.16.3.0/24  Direct  0    0             D  172.16.3.2      GigabitEthernet0/1/0
        172.16.3.2/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
      172.16.3.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
        172.16.4.0/24  OSPF    10   2             D  172.16.3.1      GigabitEthernet0/1/0
        172.16.5.0/24  Direct  0    0             D  172.16.5.1      GigabitEthernet0/1/3
        172.16.5.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/3
      172.16.5.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/3
        172.16.7.0/24  O_ASE   150  20            D  172.16.3.1      GigabitEthernet0/1/0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```
   
   The command output shows that the static route has been deleted.
   
   # Display the routing table on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 11       Routes : 11
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
        172.16.3.0/24  Direct  0    0             D  172.16.3.1      GigabitEthernet0/1/0
        172.16.3.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
      172.16.3.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
        172.16.4.0/24  Direct  0    0             D  172.16.4.1      GigabitEthernet0/2/3
        172.16.4.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/3
      172.16.4.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/3
        172.16.7.0/24  O_ASE   150  20            D  172.16.4.2     GigabitEthernet0/2/3
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   
   
   ```
   
   The static route has been associated with the NQA test instance on DeviceB. If NQA detects a link fault, it rapidly notifies DeviceB that the associated static route is unavailable. DeviceA cannot learn the route to 172.16.7.0/24 from DeviceB. However, DeviceA can learn the route to 172.16.7.0/24 from DeviceC. The route's next hop address is 172.16.4.2, and the cost is 20. Traffic switches to the link DeviceC -> SwitchA.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  router id 1.1.1.1
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 172.16.3.1 255.255.255.0
  #
  interface GigabitEthernet 0/2/3
   undo shutdown
   ip address 172.16.4.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 172.16.3.0 0.0.0.255
    network 172.16.4.0 0.0.0.255
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  router id 2.2.2.2
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 172.16.3.2 255.255.255.0
  #
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
  #
  interface GigabitEthernet 0/1/3
   undo shutdown
   ip address 172.16.5.1 255.255.255.0
  #
  ospf 1
   import-route static cost 10
   area 0.0.0.0
    network 172.16.3.0 0.0.0.255
  #
  ip route-static 172.16.7.0 255.255.255.0 GigabitEthernet0/1/1 172.16.1.2 track nqa user test
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
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  router id 3.3.3.3
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 172.16.6.1 255.255.255.0
  #
  interface GigabitEthernet 0/1/2
   undo shutdown
   ip address 172.16.2.1 255.255.255.0
  #
  interface GigabitEthernet 0/2/3
   undo shutdown
   ip address 172.16.4.2 255.255.255.0
  #
  ospf 1
   import-route static cost 20
   area 0.0.0.0
    network 172.16.4.0 0.0.0.255
  #
  ip route-static 172.16.7.0 255.255.255.0 GigabitEthernet0/1/0 172.16.6.2
  #
  return
  ```