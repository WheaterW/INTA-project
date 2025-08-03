Example for Configuring a 6to4 Tunnel
=====================================

This section provides an example for configuring a 6to4 tunnel.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365299__fig_dc_vrp_6o4tnl_cfg_001001), two IPv6 networks are both 6to4 networks; both DeviceA and DeviceB connect to a 6to4 network and the IPv4 backbone network. To interconnect the two 6to4 networks, a 6to4 tunnel needs to be configured between DeviceA and DeviceB.

To allow interworking of 6to4 networks, a 6to4 address needs to be configured for the host, with the prefix of **2002:IPv4 address:** and prefix length of 48 bits. As shown in [Figure 1](#EN-US_TASK_0172365299__fig_dc_vrp_6o4tnl_cfg_001001), the IPv4 address of the interface connecting DeviceA and the IPv4 network is 1.1.1.1. Then, the 6to4 address for the 6to4 network where DeviceA resides should have a prefix of 2002:101:101:: and a prefix length of 64 bits.

**Figure 1** Networking diagram for configuring a 6to4 tunnel![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_6o4tnl_cfg_001001.png)

#### Precautions

When configuring a 6to4 tunnel, note the following points:

* Create a tunnel interface and set parameters for the tunnel interface.
* Configure only the source IPv4 address of the tunnel. The destination IP address of the tunnel is the same as the destination IP address contained in the original IPv6 packet. The source IP address of a 6to4 tunnel must be unique.
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
   [~DeviceA-GigabitEthernet0/1/0] ip address 1.1.1.1 8
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
   [~DeviceB-GigabitEthernet0/1/0] ip address 1.1.1.2 8
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
   [*DeviceB-GigabitEthernet0/1/1] ipv6 address 2002:101:102:1::1 64
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
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A reachable route must exist between DeviceA and DeviceB. In this example, the two Routers are directly connected. Therefore, no routing protocol is configured.
3. # Configure a route to the 6to4 network on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA] ipv6 route-static 2002:: 16 Tunnel 10
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [*DeviceB] ipv6 route-static 2002:: 16 Tunnel 10
   ```
   ```
   [*DeviceB] commit
   ```
4. Verify the configuration.
   
   
   
   # Check the IPv6 status of Tunnel 10 on DeviceA. The command output shows that the tunnel is **UP**.
   
   ```
   [~DeviceA] display ipv6 interface Tunnel 10
   ```
   ```
   Tunnel10 current state : UP
   ```
   ```
   IPv6 protocol current state : UP
   ```
   ```
   link-local address is FE80::101:101
   ```
   ```
     Global unicast address(es):
   ```
   ```
       2002:101:101::1, subnet is 2002:101:101::/64
   ```
   ```
     Joined group address(es):
   ```
   ```
       FF02::1:FF01:101
   ```
   ```
       FF02::1:FF00:1
   ```
   ```
       FF02::2
   ```
   ```
       FF02::1
   ```
   ```
     MTU is 1500 bytes
   ```
   ```
     ND DAD is enabled, number of DAD attempts: 1.
   ```
   ```
     ND reachable time is 1200000 milliseconds.
   ```
   ```
     ND retransmit interval is 1000 milliseconds.
   ```
   ```
     Hosts use stateless autoconfig for addresses.
   ```
   
   # Ping the 6to4 address of GE 0/1/1 on DeviceB from DeviceA. The command output shows the ping is successful.
   
   ```
   [~DeviceA] ping ipv6 2002:101:102:1::1
   ```
   ```
     PING 2002:101:102:1::1 : 56  data bytes, press CTRL_C to break 
   ```
   ```
       Reply from 2002:101:102:1::1
   ```
   ```
       bytes=56 Sequence=1 hop limit=64 time=10 ms
   ```
   ```
       Reply from 2002:101:102:1::1
   ```
   ```
       bytes=56 Sequence=2 hop limit=64 time=2 ms
   ```
   ```
       Reply from 2002:101:102:1::1
   ```
   ```
       bytes=56 Sequence=3 hop limit=64 time=2 ms
   ```
   ```
       Reply from 2002:101:102:1::1
   ```
   ```
       bytes=56 Sequence=4 hop limit=64 time=2 ms
   ```
   ```
       Reply from 2002:101:102:1::1
   ```
   ```
       bytes=56 Sequence=5 hop limit=64 time=2 ms
   ```
   ```
     ---2002:101:102:1::1 ping statistics---
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
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 1.1.1.2 255.0.0.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2002:101:102:1::1/64
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