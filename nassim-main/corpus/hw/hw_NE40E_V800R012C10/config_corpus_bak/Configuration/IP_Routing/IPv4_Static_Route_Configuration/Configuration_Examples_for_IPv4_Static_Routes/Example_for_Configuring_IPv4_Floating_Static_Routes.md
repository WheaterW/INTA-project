Example for Configuring IPv4 Floating Static Routes
===================================================

IPv4 Floating static routes can be used for the static route backup.

#### Networking Requirements

[Figure 1](#EN-US_TASK_0172365452__fig_dc_vrp_static-route_disjoin_cfg_003201) shows the IP addresses and masks of each Router interface. Two IPv4 static routes to 10.1.5.0/24 are configured on Device A. The primary static route passes through Device B, and the floating static route passes through Device C.

**Figure 1** Networking for configuring IPv4 floating static routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_003201.png)

#### Precautions

When configuring an IPv4 floating static route, a next-hop address of this route must be specified if the outbound interface is of the broadcast type.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv4 address for each interface of each Router.
2. On Devices B and C, configure IPv4 static routes to 10.1.5.0/24.
3. On Device A, configure two IPv4 static routes to 10.1.5.0/24 with different priorities.
4. On Device D, configure IPv4 static routes to 10.1.1.0/24 and 10.1.2.0/24 so that Routers can communicate.

#### Data Preparation

To complete the configuration, you need the following data:

* On Device A, priority values of two static routes (60 for the one with 10.1.1.2 as the next hop address and 100 for the one with 10.1.2.2 as the next-hop address)

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration File](#EN-US_TASK_0172365452__section_dc_vrp_static-route_disjoin_cfg_003205) in this section.
2. Configure IPv4 static routes.
   
   
   
   # Configure IPv4 static routes on Device B.
   
   ```
   [~DeviceB] ip route-static 10.1.5.0 24 10.1.3.2
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure IPv4 static routes on Device C.
   
   ```
   [~DeviceC] ip route-static 10.1.5.0 24 10.1.4.2
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure IPv4 static routes on Device A.
   
   ```
   [*DeviceA] ip route-static 10.1.5.0 24 10.1.1.2
   ```
   ```
   [*DeviceA] ip route-static 10.1.5.0 24 10.1.2.2 preference 100
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure IPv4 static routes on Device D.
   
   ```
   [~DeviceD] ip route-static 10.1.1.0 24 10.1.3.1
   ```
   ```
   [*DeviceD] ip route-static 10.1.2.0 24 10.1.4.1
   ```
   ```
   [*DeviceD] commit
   ```
3. Verify the configuration.
   
   
   
   # View information about static routes in the IP routing table of Device A.
   
   ```
   <DeviceA> display ip routing-table protocol static
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   _public_ Routing Table : Static
   
            Destinations : 1        Routes : 1        Configured Routes : 1      
   Static routing table status : <Active>
            Destinations : 1        Routes : 1         
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
       10.1.5.0/24  Static 60   0             RD 10.1.1.2        GigabitEthernet0/1/1
   
   Static routing table status : <Inactive>
            Destinations : 0        Routes : 0
   ```
   
   # Use the **tracert** command to check the connectivity on Device A.
   
   ```
   <DeviceA> tracert 10.1.5.1
   ```
   ```
     traceroute to  10.1.5.1(10.1.5.1), max hops: 30 ,packet length: 40
    1 10.1.1.2 90 ms  1 ms  1 ms
    2 10.1.5.1 4 ms  1 ms  2 ms
   ```
   
   # Run the **shutdown** command on GE 0/1/1 of Device A to simulate a link fault.
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/1 
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] shutdown 
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] commit 
   ```
   
   # View information about static routes in the IP routing table of Device A. The route to 10.1.5.0/24 switches to the floating static route with next hop 10.1.2.2.
   
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [~DeviceA] quit
   ```
   ```
   <DeviceA> display ip routing-table protocol static
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   _public_ Routing Table : Static
   
            Destinations : 1        Routes : 1        Configured Routes : 1      
   Static routing table status : <Active>
            Destinations : 1        Routes : 1         
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
       10.1.5.0/24  Static 100   0             RD 10.1.2.2        GigabitEthernet0/1/2
   
   Static routing table status : <Inactive>
            Destinations : 0        Routes : 0
   ```
   
   # Use the **tracert** command to check the connectivity on Device A.
   
   ```
   <DeviceA> tracert 10.1.5.1
   ```
   ```
     traceroute to  10.1.5.1(10.1.5.1), max hops: 30 ,packet length: 40
    1 10.1.2.2 100 ms  1 ms  1 ms
    2 10.1.5.1 5 ms  1 ms  2 ms
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
  #
  ip route-static 10.1.5.0 24 10.1.1.2
  ip route-static 10.1.5.0 24 10.1.2.2 preference 100
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
  #
  ip route-static 10.1.5.0 24 10.1.3.2
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
  #
  ip route-static 10.1.5.0 24 10.1.4.2
  #
  return
  ```
* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.4.2 255.255.255.0
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.1.5.1 255.255.255.0
  #
  ip route-static 10.1.1.0 24 10.1.3.1
  ip route-static 10.1.2.0 24 10.1.4.1
  #
  return
  ```