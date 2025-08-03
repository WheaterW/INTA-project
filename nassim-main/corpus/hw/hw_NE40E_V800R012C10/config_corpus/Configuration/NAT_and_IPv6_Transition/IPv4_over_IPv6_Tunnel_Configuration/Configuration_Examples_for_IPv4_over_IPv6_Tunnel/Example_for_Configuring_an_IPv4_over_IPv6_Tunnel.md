Example for Configuring an IPv4 over IPv6 Tunnel
================================================

This section provides an example for configuring an IPv4 over IPv6 tunnel.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365253__fig_dc_vrp_4o6tnl_cfg_0002), two IPv4 networks are connected with an IPv6 network through DeviceA and DeviceB. To interconnect the hosts on the two IPv4 networks, configure an IPv4 over IPv6 tunnel between DeviceA and DeviceB.

**Figure 1** Networking diagram of an IPv4 over IPv6 tunnel![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 and interface2 in this example represent GE 0/1/0 and GE0/1/1, respectively.


  
![](images/fig_dc_vrp_4o6tnl_cfg_0002.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv4 over IPv6 tunnel on the edge devices.
2. Configure routes passing through the tunnel interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Source and destination IPv6 addresses of the tunnel interfaces
* IPv4 addresses of tunnel interfaces

#### Procedure

1. Configure IPv6 addresses for interfaces.
   
   
   
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
   [~DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:100::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
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
   [~DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8:100::2 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
2. Configure IPv4 addresses for interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] ip address 1.1.1.2 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
3. Configure loopback interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface LoopBack 1
   ```
   ```
   [~DeviceA-LoopBack1] ipv6 enable
   ```
   ```
   [*DeviceA-LoopBack1] ipv6 address 2001:db8:200::1 64
   ```
   ```
   [*DeviceA-LoopBack1] binding tunnel ipv4-ipv6
   ```
   ```
   [*DeviceA-LoopBack1] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface LoopBack 1
   ```
   ```
   [~DeviceB-LoopBack1] ipv6 enable
   ```
   ```
   [*DeviceB-LoopBack1] ipv6 address 2001:db8:300::2 64
   ```
   ```
   [*DeviceB-LoopBack1] binding tunnel ipv4-ipv6
   ```
   ```
   [*DeviceB-LoopBack1] commit
   ```
4. Configure IPv4 addresses, source interfaces, and destination IPv6 addresses for tunnel interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface tunnel 1
   ```
   ```
   [~DeviceA-Tunnel1] tunnel-protocol ipv4-ipv6
   ```
   ```
   [~DeviceA-Tunnel1] ip address 192.168.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-Tunnel1] source LoopBack 1
   ```
   ```
   [*DeviceA-Tunnel1] destination 2001:db8:300::2
   ```
   ```
   [*DeviceA-Tunnel1] commit
   ```
   ```
   [~DeviceA-Tunnel1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface tunnel 1
   ```
   ```
   [~DeviceB-Tunnel1] tunnel-protocol ipv4-ipv6
   ```
   ```
   [~DeviceB-Tunnel1] ip address 192.168.1.2 255.255.255.0
   ```
   ```
   [*DeviceB-Tunnel1] source LoopBack 1
   ```
   ```
   [*DeviceB-Tunnel1] destination 2001:db8:200::1
   ```
   ```
   [*DeviceB-Tunnel1] commit
   ```
   ```
   [~DeviceB-Tunnel1] quit
   ```
5. Configure the route with the outgoing interface as the tunnel interface.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ipv6 route-static 2001:db8:300::2 64 gigabitethernet 0/1/0 2001:db8:100::2
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ipv6 route-static 2001:db8:200::1 64 gigabitethernet 0/1/0 2001:db8:100::1
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] commit
   ```
6. Configure IP addresses for PC1 and PC2.
   
   
   
   # Configure PC1.
   
   Configure IP address 10.1.1.1/24 for PC1. This IP address must be on the same network segment as that of GE 0/1/1 on DeviceA. The method of configuring an IP address is determined by the operating system of PC1, and therefore is not described.
   
   # Configure PC2.
   
   Configure IP address 172.16.1.1/24 for PC2. This IP address must be on the same network segment as that of GE 0/1/1 on DeviceB. The method of configuring an IP address is determined by the operating system of PC2, and therefore is not described.
7. Verify the configuration.
   
   
   
   # Ping the IPv4 address of the tunnel interface on DeviceB from DeviceA. The command output shows that the ping operation is successful.
   
   ```
   [~DeviceA] ping 192.168.1.2
   ```
   ```
     PING 192.168.1.2: 56  data bytes, press CTRL_C to break
        Reply from 192.168.1.2: bytes=56 Sequence=1 ttl=255 time=108 ms
        Reply from 192.168.1.2: bytes=56 Sequence=2 ttl=255 time=2 ms
        Reply from 192.168.1.2: bytes=56 Sequence=3 ttl=255 time=3 ms
        Reply from 192.168.1.2: bytes=56 Sequence=4 ttl=255 time=3 ms
        Reply from 192.168.1.2: bytes=56 Sequence=5 ttl=255 time=2 ms
   
       --- 192.168.1.2 ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 2/23/108 ms
   ```
   
   # On PC1, ping the IP address of PC2. The following command output shows that the ping operation succeeds.
   
   ```
   C:\> ping 172.16.1.1
   ```
   ```
   Pinging 172.16.1.1 with 32 bytes of data:
   Reply from 172.16.1.1: time<1ms
   Reply from 172.16.1.1: time<1ms
   Reply from 172.16.1.1: time<1ms
   Reply from 172.16.1.1: time<1ms
   Ping statistics for 172.16.1.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 0ms, Maximum = 0ms, Average = 0ms
   ```

#### Configuration Files

* Configuration file of DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:100::1/64
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:200::1/64
   binding tunnel ipv4-ipv6
  #
  interface Tunnel1
   ip address 192.168.1.1 255.255.255.0
   tunnel-protocol ipv4-ipv6
   source LoopBack1
   destination 2001:DB8:300::2
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 10.1.1.0 0.0.0.255
  #
  ipv6 route-static 2001:DB8:300:: 64 GigabitEthernet0/1/0 2001:DB8:100::2
  #
  return
  ```
* Configuration file of DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:100::2/64
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:300::2/64
   binding tunnel ipv4-ipv6
  #
  interface Tunnel1
   ip address 192.168.1.2 255.255.255.0
   tunnel-protocol ipv4-ipv6
   source LoopBack1
   destination 2001:DB8:200::1
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 172.16.1.0 0.0.0.255
  #
  ipv6 route-static 2001:DB8:200:: 64 GigabitEthernet0/1/0 2001:DB8:100::1
  #
  return
  ```