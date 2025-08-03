Example for Configuring 6to4 Relay
==================================

This section provides an example for configuring 6to4 relay.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365302__fig_dc_vrp_6o4tnl_cfg_001101), DeviceA functions as a 6to4 router and connects to the 6to4 network; DeviceB is a 6to4 relay router and connects to the IPv6 network (2001:db8::/64); DeviceA connects to DeviceB through the IPv4 backbone network. To interconnect the hosts on the 6to4 and IPv6 networks, a 6to4 tunnel between DeviceA and DeviceB needs to be established.

The method of configuring a tunnel between a 6to4 relay Router and a 6to4 Router is the same as the method of configuring a tunnel between 6to4 Routers. To interconnect a 6to4 network with an IPv6 network, configure a static route to the IPv6 network on each 6to4 Router.

**Figure 1** Networking diagram for configuring 6to4 relay![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_6o4tnl_cfg_001101.png)

#### Precautions

When configuring a 6to4 tunnel, note the following points:

* Create a tunnel interface and set parameters for the tunnel interface.
* Configure only the source IPv4 address of the tunnel. The destination IPv4 address of the tunnel is the same as the destination IPv4 address contained in the original IPv6 packet. The source address of a 6to4 tunnel must be unique.
* Assign a 6to4 address to the interface that connects a border Router to a 6to4 network and an IPv4 address to the interface that connects a border Router to an IPv4 network.
* Configure an IP address for the tunnel interface to support routing protocols.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the IPv4/IPv6 dual stack on the Routers.
2. Configure a 6to4 tunnel on the Routers.
3. Configure static routes on the Routers.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv4 and IPv6 addresses of the interfaces
* Source IP address of the tunnel interface
* Static route to the indirectly connected Router

#### Procedure

1. Configure IP addresses for interfaces on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ip address 1.1.1.1 255.0.0.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2002:101:101:1::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ip address 1.1.1.2 255.0.0.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ipv6 address 2001:db8::1 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
2. # Configure a 6to4 tunnel on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA] interface Tunnel 10
   ```
   ```
   [*DeviceA-Tunnel10] tunnel-protocol ipv6-ipv4 6to4
   ```
   ```
   [*DeviceA-Tunnel10] ipv6 enable
   ```
   ```
   [*DeviceA-Tunnel10] ipv6 address 2002:101:101::1 64
   ```
   ```
   [*DeviceA-Tunnel10] source 1.1.1.1
   ```
   ```
   [*DeviceA-Tunnel10] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [*DeviceB] interface Tunnel 10
   ```
   ```
   [*DeviceB-Tunnel10] tunnel-protocol ipv6-ipv4 6to4
   ```
   ```
   [*DeviceB-Tunnel10] ipv6 enable
   ```
   ```
   [*DeviceB-Tunnel10] ipv6 address 2002:101:102::1 64
   ```
   ```
   [*DeviceB-Tunnel10] source 1.1.1.2
   ```
   ```
   [*DeviceB-Tunnel10] quit
   ```
3. Configure routes on DeviceA and DeviceB.
   
   
   
   # Configure a static route to 2002::/16 on DeviceA.
   
   ```
   [*DeviceA] ipv6 route-static 2002:: 16 Tunnel 10
   ```
   
   # Configure a default route to the IPv6 network on DeviceA.
   
   ```
   [*DeviceA] ipv6 route-static :: 0 2002:101:102::1
   ```
   ```
   [*DeviceA] commit
   ```
   
   
   
   # Configure a static route to 2002::/16 on DeviceB.
   
   ```
   [*DeviceB] ipv6 route-static 2002:: 16 Tunnel 10
   ```
   ```
   [*DeviceB] commit
   ```
4. Verify the configuration.
   
   
   
   # Ping the IPv6 address of GE 0/1/1 on DeviceB from DeviceA. The command output shows the ping is successful.
   
   ```
   [~DeviceA] ping ipv6 2001:db8::1
   ```
   ```
     PING 2001:db8::1 : 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=1 hop limit=64 time=10 ms
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=2 hop limit=64 time=2 ms
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=3 hop limit=64 time=2 ms
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=4 hop limit=64 time=2 ms
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=5 hop limit=64 time=2 ms
   
   
   ```
   ```
     --- 2001:db8::1 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
   round-trip min/avg/max = 5/14/29 ms
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  admin
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 1.1.1.1 255.0.0.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2002:101:101:1::1/64
  #
  interface Tunnel 10
   ipv6 enable
   ipv6 address 2002:101:101::1/64
   tunnel-protocol ipv6-ipv4 6to4
   source 1.1.1.1
  #
  ipv6 route-static :: 0 2002:101:102::1
  #
  ipv6 route-static 2002:: 16 Tunnel 10
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  admin
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 1.1.1.2 255.0.0.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8::1/64
  #
  interface Tunnel 10
   ipv6 enable
   ipv6 address 2002:101:102::1/64
   tunnel-protocol ipv6-ipv4 6to4
   source 1.1.1.2
  #
  ipv6 route-static 2002:: 16 Tunnel 10
  #
  return
  ```