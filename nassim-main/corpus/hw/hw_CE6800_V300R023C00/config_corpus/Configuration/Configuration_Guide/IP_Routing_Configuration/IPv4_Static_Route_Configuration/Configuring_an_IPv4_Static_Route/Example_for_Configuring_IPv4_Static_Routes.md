Example for Configuring IPv4 Static Routes
==========================================

Example for Configuring IPv4 Static Routes

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176742421__fig15651201057), static routes need to be configured on DeviceA, DeviceB, and DeviceC to enable any two hosts to communicate.

**Figure 1** Network diagram of IPv4 static routes![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001176742471.png)

#### Precautions

Note the following during the configuration:

* If a broadcast interface is used as the outbound interface of an IPv4 static route, a next-hop IP address must be specified.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each device.
2. Configure IPv4 static routes destined for specified destination IP addresses or a default IPv4 static route on each device.


#### Procedure

1. Configure IPv4 addresses for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.4.1 30
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Configure IPv4 static routes on each device.
   
   
   
   # On DeviceA, configure a default IPv4 static route with DeviceB as a next hop.
   
   ```
   [~DeviceA] ip route-static 0.0.0.0 0.0.0.0 10.1.4.2
   [*DeviceA] commit
   ```
   
   # On DeviceB, configure one IPv4 static route with DeviceA as a next hop and the other one with DeviceC as a next hop.
   
   ```
   [~DeviceB] ip route-static 10.1.1.0 255.255.255.0 10.1.4.1
   [*DeviceB] ip route-static 10.1.3.0 255.255.255.0 10.1.4.6
   [*DeviceB] commit
   ```
   
   # On DeviceC, configure a default IPv4 static route with DeviceB as a next hop.
   
   ```
   [~DeviceC] ip route-static 0.0.0.0 0.0.0.0 10.1.4.5
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Check the IP routing table of DeviceA.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table: Public
         Destinations : 12        Routes : 12

Destination/Mask    Proto  Pre  Cost   Flags     NextHop         Interface

        0.0.0.0/0   Static 60   0         RD      10.1.4.2        100GE1/0/1
       10.1.1.0/24  Direct 0    0         D       10.1.1.1        100GE1/0/2
       10.1.1.1/32  Direct 0    0         D       127.0.0.1       100GE1/0/2
     10.1.1.255/32  Direct 0    0         D       127.0.0.1       100GE1/0/2
       10.1.4.0/30  Direct 0    0         D       10.1.4.1        100GE1/0/1
       10.1.4.1/32  Direct 0    0         D       127.0.0.1       100GE1/0/1
       10.1.4.2/32  Direct 0    0         D       10.1.4.2        100GE1/0/1
     10.1.4.255/32  Direct 0    0         D       127.0.0.1       100GE1/0/1
      127.0.0.0/8   Direct 0    0         D       127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct 0    0         D       127.0.0.1       InLoopBack0
127.255.255.255/32  Direct 0    0         D       127.0.0.1       InLoopBack0
255.255.255.255/32  Direct 0    0         D       127.0.0.1       InLoopBack0
```

The preceding command output shows that DeviceA's routing table contains a default IPv4 static route with the destination IP address set to 0.0.0.0/0 and the next-hop IP address set to 10.1.4.2.

# Perform a ping to verify device connectivity.

```
[~DeviceA] ping 10.1.3.1
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

PC1, PC2, and PC3 can ping each other.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.4.1 255.255.255.252
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  ip route-static 0.0.0.0 0.0.0.0 10.1.4.2
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
   ip address 10.1.4.2 255.255.255.252
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.4.5 255.255.255.252
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #
  ip route-static 10.1.1.0 255.255.255.0 10.1.4.1
  ip route-static 10.1.3.0 255.255.255.0 10.1.4.6
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
   ip address 10.1.4.6 255.255.255.252
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
  #
  ip route-static 0.0.0.0 0.0.0.0 10.1.4.5
  #
  return
  ```