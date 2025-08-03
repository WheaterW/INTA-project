Example for Configuring OSPF Load Balancing
===========================================

This section describes how to configure OSPF load balancing, including enabling load balancing and setting priorities for equal-cost routes.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365661__fig_dc_vrp_ospf_cfg_009801):

* DeviceA, DeviceB, DeviceC, DeviceD, and DeviceE are connected to each other through OSPF.
* DeviceA, DeviceB, DeviceC, DeviceD, and DeviceE belong to Area 0.
* Load balancing is configured so that the traffic from DeviceA to DeviceE is load-balanced by DeviceC and DeviceD.

**Figure 1** Networking for configuring OSPF load balancing![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/1, respectively.


  
![](images/fig_dc_vrp_ospf_cfg_009801.png "Click to enlarge")

#### Precautions

To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security". OSPF area authentication is used as an example. For details, see Example for Configuring Basic OSPF Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions on each Router for interconnection.
2. Configure load balancing on DeviceA.
3. Set the priority for equal-cost routes on DeviceA.
4. Configure per-packet load balancing on DeviceA.

#### Data Preparation

To complete the configuration, you need the following data:

* Data of DeviceA, including router ID (1.1.1.1), OSPF process ID (1), and network segment addresses of Area 0 (10.1.1.0/24, 10.1.2.0/24 and 10.1.3.0/24)
* Data of DeviceB, including router ID (2.2.2.2), OSPF process ID (1), and network segment addresses of area 0 (10.1.1.0/24 and 192.168.0.0/24)
* Data of DeviceC, including router ID (3.3.3.3), OSPF process ID (1), and network segment addresses of area 0 (10.1.2.0/24 and 192.168.1.0/24)
* Data of DeviceD, including router ID (4.4.4.4), OSPF process ID (1), and network segment addresses of area 0 (10.1.3.0/24 and 192.168.2.0/24)
* Data of DeviceE, including router ID (5.5.5.5), OSPF process ID (1), and network segment addresses of area 0 (192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, and 172.17.1.0/24)
* Number of equal-cost routes for load balancing on DeviceA (2)
* Next hop weights of the routes from DeviceA to DeviceB, DeviceC, and DeviceD (2, 1, and 1, respectively)

#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365661__section_dc_vrp_ospf_cfg_009806) in this section.
2. Configure basic OSPF functions. For details, see [Example for Configuring Basic OSPF Functions](dc_vrp_ospf_cfg_0094.html).
3. Display the routing table of DeviceA.
   
   
   
   DeviceA has three valid next hops: DeviceB (10.1.1.2), DeviceC (10.1.2.2), and DeviceD (10.1.3.2) because the default maximum number of equal-cost routes is 64.
   
   ```
   <DeviceA> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ----------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 15       Routes : 15
   
   Destination/Mask    Proto  Pre  Cost  Flags     NextHop         Interface
   
          10.1.1.0/24  Direct 0    0       D        10.1.1.1         GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0       D        127.0.0.1        GigabitEthernet0/1/0
          10.1.1.2/32  Direct 0    0       D        10.1.1.2         GigabitEthernet0/1/0
          10.1.2.0/24  Direct 0    0       D        10.1.2.1         GigabitEthernet0/2/0
          10.1.2.1/32  Direct 0    0       D        127.0.0.1        GigabitEthernet0/2/0
          10.1.2.2/32  Direct 0    0       D        10.1.2.2         GigabitEthernet0/2/0
          10.1.3.0/24  Direct 0    0       D        10.1.2.1         GigabitEthernet0/3/0
          10.1.3.1/32  Direct 0    0       D        127.0.0.1        GigabitEthernet0/3/0
          10.1.3.2/32  Direct 0    0       D        10.1.2.2         GigabitEthernet0/3/0
       127.0.0.0/8     Direct 0    0       D        127.0.0.1        InLoopBack0
       127.0.0.1/32    Direct 0    0       D        127.0.0.1        InLoopBack0
       192.168.0.0/24  OSPF   10   2       D        10.1.1.2         GigabitEthernet0/1/0
       192.168.1.0/24  OSPF   10   2       D        10.1.2.2         GigabitEthernet0/2/0
       192.168.2.0/24  OSPF   10   2       D        10.1.2.2         GigabitEthernet0/3/0
        172.17.1.0/24  OSPF   10   3       D        10.1.1.2         GigabitEthernet0/1/0
                       OSPF   10   3       D        10.1.2.2         GigabitEthernet0/2/0
                       OSPF   10   3       D        10.1.3.2         GigabitEthernet0/3/0
   ```
4. Set the maximum number of routes for load balancing to 2 on DeviceA.
   
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] maximum load-balancing 2
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
   ```
   [~DeviceA-ospf-1] quit
   ```
   
   # Check the routing table of DeviceA. The command output shows that DeviceA has two routes for load balancing. The maximum number of equal-cost routes is 2. Therefore, the next hops 10.1.1.2 (DeviceB) and 10.1.2.2 (DeviceC) are valid routes.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ----------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 15       Routes : 15
   
   Destination/Mask    Proto  Pre  Cost  Flags     NextHop         Interface
   
          10.1.1.0/24  Direct 0    0       D        10.1.1.1         GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0       D        127.0.0.1        GigabitEthernet0/1/0
          10.1.1.2/32  Direct 0    0       D        10.1.1.2         GigabitEthernet0/1/0
          10.1.2.0/24  Direct 0    0       D        10.1.2.1         GigabitEthernet0/2/0
          10.1.2.1/32  Direct 0    0       D        127.0.0.1        GigabitEthernet0/2/0
          10.1.2.2/32  Direct 0    0       D        10.1.2.2         GigabitEthernet0/2/0
          10.1.3.0/24  Direct 0    0       D        10.1.2.1         GigabitEthernet0/3/0
          10.1.3.1/32  Direct 0    0       D        127.0.0.1        GigabitEthernet0/3/0
          10.1.3.2/32  Direct 0    0       D        10.1.2.2         GigabitEthernet0/3/0
       127.0.0.0/8     Direct 0    0       D        127.0.0.1        InLoopBack0
       127.0.0.1/32    Direct 0    0       D        127.0.0.1        InLoopBack0
       192.168.0.0/24  OSPF   10   2       D        10.1.1.2         GigabitEthernet0/1/0
       192.168.1.0/24  OSPF   10   2       D        10.1.2.2         GigabitEthernet0/2/0
       192.168.2.0/24  OSPF   10   2       D        10.1.2.2         GigabitEthernet0/3/0
        172.17.1.0/24  OSPF   10   3       D        10.1.1.2         GigabitEthernet0/1/0
                       OSPF   10   3       D        10.1.2.2         GigabitEthernet0/2/0
   ```
5. Set the priority for equal-cost routes on DeviceA.
   
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] nexthop 10.1.1.2 weight 2
   ```
   ```
   [*DeviceA-ospf-1] nexthop 10.1.2.2 weight 1
   ```
   ```
   [*DeviceA-ospf-1] nexthop 10.1.3.2 weight 1
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
   ```
   [*DeviceA-ospf-1] quit
   ```
6. Verify the configuration.
   
   
   
   # Check the routing table of DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ----------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 15       Routes : 15
   
   Destination/Mask    Proto  Pre  Cost  Flags     NextHop         Interface
   
          10.1.1.0/24  Direct 0    0       D        10.1.1.1         GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0       D        127.0.0.1        GigabitEthernet0/1/0
          10.1.1.2/32  Direct 0    0       D        10.1.1.2         GigabitEthernet0/1/0
          10.1.2.0/24  Direct 0    0       D        10.1.2.1         GigabitEthernet0/2/0
          10.1.2.1/32  Direct 0    0       D        127.0.0.1        GigabitEthernet0/2/0
          10.1.2.2/32  Direct 0    0       D        10.1.2.2         GigabitEthernet0/2/0
          10.1.3.0/24  Direct 0    0       D        10.1.2.1         GigabitEthernet0/3/0
          10.1.3.1/32  Direct 0    0       D        127.0.0.1        GigabitEthernet0/3/0
          10.1.3.2/32  Direct 0    0       D        10.1.2.2         GigabitEthernet0/3/0
       127.0.0.0/8     Direct 0    0       D        127.0.0.1        InLoopBack0
       127.0.0.1/32    Direct 0    0       D        127.0.0.1        InLoopBack0
       192.168.0.0/24  OSPF   10   2       D        10.1.1.2         GigabitEthernet0/1/0
       192.168.1.0/24  OSPF   10   2       D        10.1.2.2         GigabitEthernet0/2/0
       192.168.2.0/24  OSPF   10   2       D        10.1.2.2         GigabitEthernet0/3/0
        172.17.1.0/24  OSPF   10   3       D        10.1.2.2         GigabitEthernet0/2/0
                       OSPF   10   3       D        10.1.3.2         GigabitEthernet0/3/0
   ```
   
   As shown in the routing table, the priority of the route with 10.1.2.2 and 10.1.3.2 as the next hop addresses is higher than that of the route with 10.1.1.2 as the next hop address. Therefore, DeviceA has only two valid next hops, DeviceC (10.1.2.2) and DeviceD (10.1.3.2).

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
  router id 1.1.1.1
  ```
  ```
   #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.3.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   maximum load-balancing 2
  ```
  ```
   nexthop 10.1.1.2 weight 2
  ```
  ```
   nexthop 10.1.2.2 weight 1
  ```
  ```
   nexthop 10.1.3.2 weight 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
    network 10.1.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  router id 2.2.2.2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.0.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 192.168.0.0 0.0.255.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  router id 3.3.3.3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.1.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceD
  ```
  ```
  #
  ```
  ```
  router id 4.4.4.4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.3.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.3.0 0.0.0.255
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceE configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceE
  ```
  ```
  #
  ```
  ```
  router id 5.5.5.5
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.0.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.17.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.0.0 0.0.255.255
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 172.17.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```