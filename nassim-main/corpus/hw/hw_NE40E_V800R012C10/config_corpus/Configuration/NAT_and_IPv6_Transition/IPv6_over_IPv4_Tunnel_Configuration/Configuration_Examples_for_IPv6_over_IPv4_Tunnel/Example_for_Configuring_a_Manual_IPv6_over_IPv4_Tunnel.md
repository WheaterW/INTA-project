Example for Configuring a Manual IPv6 over IPv4 Tunnel
======================================================

This section provides an example for configuring a manual IPv6 over IPv4 tunnel.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365296__fig_dc_vrp_6o4tnl_cfg_000901), two IPv6 networks are connected to DeviceB on the IPv4 backbone network through DeviceA and DeviceC. To interconnect the two IPv6 networks, configure a manual IPv6 over IPv4 tunnel between DeviceA and DeviceC.

**Figure 1** Networking diagram for configuring a manual IPv6 over IPv4 tunnel![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_6o4tnl_cfg_000901.png)

#### Precautions

When configuring a manual IPv6 over IPv4 tunnel, note the following points:

* Create a tunnel interface and set parameters for the tunnel interface.
* Perform the following configuration on the Routers at both ends of the tunnel. The source IP address of the local end is the destination IP address of the remote end of the tunnel. Similarly, the destination IP address of the local end is the source IP address of the remote end.
* Configure an IP address for the tunnel interface to support routing protocols.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each physical interface.
2. Configure IPv6 addresses for tunnel interfaces and source and destination addresses for the involved tunnel.
3. Set the protocol type to IPv6-IPv4.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* IPv6 addresses of the tunnel interfaces, and source and destination addresses of the tunnel

#### Procedure

1. Configure IPv6 addresses for interfaces on DeviceA, DeviceB, and DeviceC.
   
   
   
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
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ip address 192.168.50.2 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
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
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ip address 192.168.50.1 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ip address 192.168.51.1 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] ip address 192.168.51.2 255.255.255.0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
2. Create tunnel interfaces, and configure a tunnel mode, IPv6 addresses for the tunnel interfaces, and source and destination addresses for the tunnel.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA] interface Tunnel 10
   ```
   ```
   [*DeviceA-Tunnel10] tunnel-protocol ipv6-ipv4
   ```
   ```
   [*DeviceA-Tunnel10] ipv6 enable
   ```
   ```
   [*DeviceA-Tunnel10] ipv6 address 2001:db8::1 64
   ```
   ```
   [*DeviceA-Tunnel10] source 192.168.50.2
   ```
   ```
   [*DeviceA-Tunnel10] destination 192.168.51.2
   ```
   ```
   [*DeviceA-Tunnel10] quit
   ```
   
   
   
   # Configure DeviceC.
   
   ```
   [*DeviceC] interface Tunnel 10
   ```
   ```
   [*DeviceC-Tunnel10] tunnel-protocol ipv6-ipv4
   ```
   ```
   [*DeviceC-Tunnel10] ipv6 enable
   ```
   ```
   [*DeviceC-Tunnel10] ipv6 address 2001:db8::2 64
   ```
   ```
   [*DeviceC-Tunnel10] source 192.168.51.2
   ```
   ```
   [*DeviceC-Tunnel10] destination 192.168.50.2
   ```
   ```
   [*DeviceC-Tunnel10] quit
   ```
3. Configure static routes to ensure that DeviceA and DeviceC are reachable.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA] ip route-static 192.168.51.0 255.255.255.0 192.168.50.1
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [*DeviceC] ip route-static 192.168.50.0 255.255.255.0 192.168.51.1
   ```
   ```
   [*DeviceC] commit
   ```
4. Verify the configuration.
   
   
   
   # Ping the IPv4 address of GE 0/1/0 on DeviceA from DeviceC. Device C can receive return packets from DeviceA.
   
   ```
   [~DeviceC] ping 192.168.50.2
   ```
   ```
     PING 192.168.50.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 192.168.50.2: bytes=56 Sequence=1 ttl=254 time=84 ms
   ```
   ```
       Reply from 192.168.50.2: bytes=56 Sequence=2 ttl=254 time=27 ms
   ```
   ```
       Reply from 192.168.50.2: bytes=56 Sequence=3 ttl=254 time=25 ms
   ```
   ```
       Reply from 192.168.50.2: bytes=56 Sequence=4 ttl=254 time=3 ms
   ```
   ```
       Reply from 192.168.50.2: bytes=56 Sequence=5 ttl=254 time=24 ms
   ```
   ```
     --- 192.168.50.2 ping statistics ---
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
       round-trip min/avg/max = 3/32/84 ms
   ```
   
   # Ping the IPv6 address of Tunnel 10 on DeviceA from DeviceC. DeviceC can receive return packets from DeviceA.
   
   ```
   [~DeviceC] ping ipv6 2001:db8::1
   ```
   ```
     PING 2001:db8::1 : 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=1 hop limit=64  time = 28 ms
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=2 hop limit=64  time = 27 ms
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=3 hop limit=64  time = 26 ms
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=4 hop limit=64  time = 27 ms
   ```
   ```
       Reply from 2001:db8::1
   ```
   ```
       bytes=56 Sequence=5 hop limit=64  time = 26 ms
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
   round-trip min/avg/max = 26/26/28 ms
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.50.2 255.255.255.0
  #
  interface Tunnel 10
   ipv6 enable
   ipv6 address 2001:db8::1/64
   tunnel-protocol ipv6-ipv4
   source 192.168.50.2
   destination 192.168.51.2
  #
  ip route-static 192.168.51.0 255.255.255.0 192.168.50.1
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
   ip address 192.168.50.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.51.1 255.255.255.0
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
   sysname DeviceC
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.51.2 255.255.255.0
  #
  interface Tunnel 10
   ipv6 enable
   ipv6 address 2001:db8::2/64
   tunnel-protocol ipv6-ipv4
   source 192.168.51.2
   destination 192.168.50.2
  #
  ip route-static 192.168.50.0 255.255.255.0 192.168.51.1
  #
  return
  ```