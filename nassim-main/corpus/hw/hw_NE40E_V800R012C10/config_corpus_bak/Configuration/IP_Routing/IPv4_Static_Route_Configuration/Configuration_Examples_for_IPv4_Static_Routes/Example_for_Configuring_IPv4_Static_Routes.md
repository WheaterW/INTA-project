Example for Configuring IPv4 Static Routes
==========================================

You can configure IPv4 static routes to interconnect any two devices on an IPv4 network.

#### Networking Requirements

[Figure 1](#EN-US_TASK_0172365449__fig_dc_vrp_static-route_disjoin_cfg_001701) shows the IP addresses and masks of interfaces and hosts. It is required that any two hosts in [Figure 1](#EN-US_TASK_0172365449__fig_dc_vrp_static-route_disjoin_cfg_001701) communicate through static routes.

**Figure 1** Networking for configuring IPv4 static routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_001701.png)  


#### Precautions

When configuring an IPv4 static route, specify a next-hop address if the outbound interface is of the broadcast type.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each Router.
2. Configure an IPv4 static route and a default route on each Router.
3. Configure the IPv4 default gateway on each host so that any two hosts communicate with each other.

#### Data Preparation

To complete the configuration, you need the following data:

* Default route with 10.1.4.2 as the next hop on Device A
* Static route to 10.1.1.0 with 10.1.4.1 as the next hop on Device B
* Static route to 10.1.3.0 with 10.1.4.6 as the next hop on Device B
* Default route with 10.1.4.5 as the next hop on Device C
* Default gateways of PC1, PC2, and PC3

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365449__section_dc_vrp_static-route_disjoin_cfg_001705) in this section.
2. Configure static routes.
   
   
   
   # Configure an IPv4 default route on Device A.
   
   ```
   [~DeviceA] ip route-static 0.0.0.0 0.0.0.0 10.1.4.2
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure two IPv4 static routes on Device B.
   
   ```
   [~DeviceB] ip route-static 10.1.1.0 255.255.255.0 10.1.4.1
   ```
   ```
   [*DeviceB] ip route-static 10.1.3.0 255.255.255.0 10.1.4.6
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure an IPv4 default route on Device C.
   
   ```
   [~DeviceC] ip route-static 0.0.0.0 0.0.0.0 10.1.4.5
   ```
   ```
   [*DeviceC] commit
   ```
3. Configure a default gateway for each host.
   
   
   
   Configure the default gateways of PC1, PC2, and PC3 as 10.1.1.1, 10.1.2.1, and 10.1.3.1 respectively.
4. Verify the configuration.
   
   
   
   # Check the IP routing table of Device A.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: Public
            Destinations : 12        Routes : 12
   
   Destination/Mask    Proto  Pre  Cost   Flags    NextHop         Interface
   
           0.0.0.0/0   Static 60   0        RD       10.1.4.2        GigabitEthernet0/1/0
          10.1.1.0/24  Direct 0    0         D       10.1.1.1        GigabitEthernet0/2/0
          10.1.1.1/32  Direct 0    0         D       127.0.0.1       GigabitEthernet0/2/0
        10.1.1.255/32  Direct 0    0         D       127.0.0.1       GigabitEthernet0/2/0
          10.1.4.0/30  Direct 0    0         D       10.1.4.1        GigabitEthernet0/1/0
          10.1.4.1/32  Direct 0    0         D       127.0.0.1       GigabitEthernet0/1/0
          10.1.4.2/32  Direct 0    0         D       10.1.4.2        GigabitEthernet0/1/0
        10.1.4.255/32  Direct 0    0         D       127.0.0.1       GigabitEthernet0/1/0
         127.0.0.0/8   Direct 0    0         D       127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0         D       127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0         D       127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0         D       127.0.0.1       InLoopBack0
   ```
   
   # Run the **ping** command to verify the connectivity.
   
   ```
   [~DeviceA] ping 10.1.3.1
   ```
   ```
     PING 10.1.3.1: 56  data bytes, press CTRL_C to break
       Reply from 10.1.3.1: bytes=56 Sequence=1 ttl=254 time=62 ms
       Reply from 10.1.3.1: bytes=56 Sequence=2 ttl=254 time=63 ms
       Reply from 10.1.3.1: bytes=56 Sequence=3 ttl=254 time=63 ms
       Reply from 10.1.3.1: bytes=56 Sequence=4 ttl=254 time=62 ms
       Reply from 10.1.3.1: bytes=56 Sequence=5 ttl=254 time=62 ms
     --- 10.1.3.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 62/62/63 ms
   ```
   
   # Run the **tracert** command to verify the connectivity.
   
   ```
   [~DeviceA] tracert 10.1.3.1
   ```
   ```
    traceroute to  10.1.3.1(10.1.3.1), max hops: 30 ,packet length: 40
    1 10.1.4.2 31 ms  32 ms  31 ms
    2 10.1.4.6 62 ms  63 ms  62 ms
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.1 255.255.255.252
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  ip route-static 0.0.0.0 0.0.0.0 10.1.4.2
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.2 255.255.255.252
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.4.5 255.255.255.252
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
  #
  ip route-static 10.1.1.0 255.255.255.0 10.1.4.1
  ip route-static 10.1.3.0 255.255.255.0 10.1.4.6
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.6 255.255.255.252
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
  #
  ip route-static 0.0.0.0 0.0.0.0 10.1.4.5
  #
  return
  ```