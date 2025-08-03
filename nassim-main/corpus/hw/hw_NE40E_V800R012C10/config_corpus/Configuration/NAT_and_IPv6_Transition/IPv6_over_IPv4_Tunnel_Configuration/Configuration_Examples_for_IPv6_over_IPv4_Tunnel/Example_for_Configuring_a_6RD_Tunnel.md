Example for Configuring a 6RD Tunnel
====================================

This section provides an example for configuring a 6RD tunnel to allow the clients or devices in different 6RD domains to communicate.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365305__fig_dc_vrp_cfg_00244201), both DeviceA and DeviceB support the IPv4/IPv6 dual stack, and they are connected to an IPv6 network and an IPv4 network. Both DeviceA and DeviceB are 6RD CEs. The IPv6 networks are 6RD networks. A 6RD tunnel needs to be established between DeviceA and DeviceB so that the hosts on the two IPv6 networks can communicate.

**Figure 1** Networking diagram for configuring a 6RD tunnel to allow the clients and devices in different 6RD domains to communicate![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_ipv6_cfg_00244201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. On DeviceA and DeviceB, configure IPv4 addresses for the physical interfaces connected to the IPv4 network and enable IPv6 packet forwarding.
2. On DeviceA and DeviceB, configure the source IPv4 address, 6RD prefix, IPv6 prefix length, and IPv4 prefix length for a 6RD tunnel so that the devices can calculate the 6RD delegated prefix based on a combination of these parameters.
3. On DeviceA and DeviceB, configure IPv6 addresses for the physical interfaces connected to the 6RD domains based on the 6RD delegated prefix.
4. Configure the IPv6 addresses on PC1 and PC2, with the IPv6 prefix set to a 64-bit address prefix that contains the 6RD prefix and subnet ID.
5. On DeviceA, configure a static route destined for the 6RD domain in which DeviceB resides. On DeviceB, configure a static route destined for the 6RD domain in which DeviceA resides.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv4 addresses of interfaces
* Source IPv4 addresses of 6RD tunnel interfaces
* 6RD prefix of the 6RD tunnel
* IPv4 prefix length of the 6RD tunnel

#### Procedure

1. Configure IPv4 addresses for interfaces that connect devices to the IPv4 network.
   
   
   
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
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
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
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
2. Configure a 6RD tunnel.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface Tunnel 1
   ```
   ```
   [*DeviceA-Tunnel1] tunnel-protocol ipv6-ipv4 6rd
   ```
   ```
   [*DeviceA-Tunnel1] ipv6 enable
   ```
   ```
   [*DeviceA-Tunnel1] source GigabitEthernet 0/1/1
   ```
   ```
   [*DeviceA-Tunnel1] ipv6-prefix 2001:db8::/32
   ```
   ```
   [*DeviceA-Tunnel1] ipv4-prefix length 8
   ```
   ```
   [*DeviceA-Tunnel1] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface Tunnel 1
   ```
   ```
   [*DeviceB-Tunnel1] tunnel-protocol ipv6-ipv4 6rd
   ```
   ```
   [*DeviceB-Tunnel1] ipv6 enable
   ```
   ```
   [*DeviceB-Tunnel1] source GigabitEthernet 0/1/1
   ```
   ```
   [*DeviceB-Tunnel1] ipv6-prefix 2001:db8::/32
   ```
   ```
   [*DeviceB-Tunnel1] ipv4-prefix length 8
   ```
   ```
   [*DeviceB-Tunnel1] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The 6RD delegated prefix can be automatically calculated based on the configured source tunnel IPv4 address or source interface name, 6RD prefix, IPv6 prefix length, and IPv4 prefix length. You can run the **display this interface** command to view the 6RD delegated prefix and then configure an IPv6 address for the tunnel interface.
   
   In this example, the IPv4 prefix length of the 6RD tunnel is set to 8 bits. To generate a 56-bit 6RD delegated prefix, the device removes the left-most 8 bits from the tunnel source address (IPv4 address of GE **0/1/1**) and adds the 6RD prefix 2001:db8::/32 before the remaining 24 bits (in hexadecimal notation) of the tunnel source address.
3. Query the calculated 6RD delegated prefix.
   
   
   
   # Query the calculated 6RD delegated prefix on DeviceA.
   
   ```
   [~DeviceA-Tunnel1] display this interface
   ```
   ```
   Tunnel1 current state : UP (ifindex: 9)
   Line protocol current state : DOWN 
   Description: 
   Route Port,The Maximum Transmit Unit is 1500
   Internet protocol processing : disabled
   Encapsulation is TUNNEL, loopback not set
   Tunnel source 10.1.1.1, destination unknown
   Tunnel protocol/transport IPv6 over IPv4 (6rd)
   ipv6 prefix 2001:DB8::/32 
   ipv4 prefix length 8 
   6RD Operational, Delegated Prefix is 2001:DB8:101:100::/56
   Current system time: 2017-09-02 10:14:49
     300 seconds input rate 0 bits/sec, 0 packets/sec
     300 seconds output rate 0 bits/sec, 0 packets/sec
     0 seconds input rate 0 bits/sec, 0 packets/sec
     0 seconds output rate 0 bits/sec, 0 packets/sec
     0 packets input,  0 bytes
     0 input error
     0 packets output,  0 bytes                                
     0 output error
     Input:
       Unicast: 0 packets, Multicast: 0 packets
     Output:
       Unicast: 0 packets, Multicast: 0 packets
       Last 300 seconds input utility rate:  --
       Last 300 seconds output utility rate: --
   ```
   
   # Query the calculated 6RD delegated prefix on DeviceB.
   
   ```
   [~DeviceB-Tunnel1] display this interface
   ```
   ```
   Tunnel1 current state : UP (ifindex: 10)
   Line protocol current state : DOWN 
   Description: 
   Route Port,The Maximum Transmit Unit is 1500
   Internet protocol processing : disabled
   Encapsulation is TUNNEL, loopback not set
   Tunnel source 10.1.1.2, destination unknown
   Tunnel protocol/transport IPv6 over IPv4 (6rd)
   ipv6 prefix 2001:DB8::/32 
   ipv4 prefix length 8 
   6RD Operational, Delegated Prefix is 2001:db8:101:200::/56
   Current system time: 2017-09-02 10:22:13
     300 seconds input rate 0 bits/sec, 0 packets/sec
     300 seconds output rate 0 bits/sec, 0 packets/sec
     0 seconds input rate 0 bits/sec, 0 packets/sec
     0 seconds output rate 0 bits/sec, 0 packets/sec
     0 packets input,  0 bytes
     0 input error
     0 packets output,  0 bytes                                
     0 output error
     Input:
       Unicast: 0 packets, Multicast: 0 packets
     Output:
       Unicast: 0 packets, Multicast: 0 packets
       Last 300 seconds input utility rate:  --
       Last 300 seconds output utility rate: --
   ```
4. Configure IPv6 addresses for the tunnel interfaces based on the 6RD delegated prefix.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA-Tunnel1] ipv6 address 2001:db8:101:100::1 56
   ```
   ```
   [*DeviceA-Tunnel1] commit
   ```
   ```
   [~DeviceA-Tunnel1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB-Tunnel1] ipv6 address 2001:db8:101:200::1 56
   ```
   ```
   [*DeviceB-Tunnel1] commit
   ```
   ```
   [~DeviceB-Tunnel1] quit
   ```
5. Configure an IPv6 address for GE 0/1/2.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ipv6 address 2001:db8:101:101::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] ipv6 address 2001:db8:101:201::1 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/2] quit
   ```
6. Configure static routes destined for the 6RD domains connected to DeviceA and DeviceB.
   
   
   
   # Configure a static route destined for the 6RD domain connected to DeviceB.
   
   ```
   [~DeviceA] ipv6 route-static 2001:db8:: 32 Tunnel 1
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure a static route destined for the 6RD domain connected to DeviceA.
   
   ```
   [~DeviceB] ipv6 route-static 2001:db8:: 32 Tunnel 1
   ```
   ```
   [*DeviceB] commit
   ```
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The leftmost 56 bits of the IPv6 address of GE **0/1/2** must be the same as the 6RD delegated prefix.
7. Configure IPv6 addresses for PC1 and PC2.
   
   
   
   # Configure PC1.
   
   Configure the IPv6 address 2001:db8:101:101::2/64 for PC1 based on the 6RD delegated prefix. This IPv6 address must be on the same network segment as that of GE 0/1/2 on DeviceA. Configure a static route from PC1 to DeviceA and set the destination address to 2001:db8:: 32. The method of configuring the IPv6 address and static route is related to the operating system running on PC1. The configuration details are not provided.
   
   # Configure PC2.
   
   Configure the IPv6 address 2001:db8:101:201::2/64 for PC2 based on the 6RD delegated prefix. This IPv6 address must be on the same network segment as that of GE 0/1/2 on DeviceB. Configure a static route from PC2 to DeviceB and set the destination address to 2001:db8:: 32. The method of configuring the IPv6 address and static route is related to the operating system running on PC2. The configuration details are not provided.
8. Verify the configuration.
   
   
   
   # After completing the configurations, run the **display interface Tunnel 1** command to check the status of Tunnel1 on DeviceA or DeviceB. The following command output shows that the status of Tunnel 1 is **UP**.
   
   ```
   [~DeviceA] display interface Tunnel 1
   ```
   ```
   Tunnel1 current state : UP (ifindex: 78)
   Line protocol current state : DOWN 
   Description: 
   Route Port,The Maximum Transmit Unit is 1500
   Internet protocol processing : disabled
   Encapsulation is TUNNEL, loopback not set
   Tunnel source 2.1.1.1, destination unknown
   Tunnel protocol/transport IPv6 over IPv4 (6rd)
   ipv6 prefix 2001:DB8::/32 
   ipv4 prefix length 8 
   6RD Operational, Delegated Prefix is 2001:db8:101:100::/56
   Current system time: 2020-12-21 01:41:03
     300 seconds input rate 0 bits/sec, 0 packets/sec
     300 seconds output rate 0 bits/sec, 0 packets/sec
     0 seconds input rate 0 bits/sec, 0 packets/sec
     0 seconds output rate 0 bits/sec, 0 packets/sec
     0 packets input,  0 bytes
     0 input error
     0 packets output,  0 bytes                                
     0 output error
     Input:
       Unicast: 0 packets, Multicast: 0 packets
     Output:
       Unicast: 0 packets, Multicast: 0 packets
       Last 300 seconds input utility rate:  --
       Last 300 seconds output utility rate: --
   ```
   
   # On Device A, ping the IPv6 address of GE 0/1/2 on Device B. The following command output shows that the ping is successful.
   
   ```
   [~DeviceA] ping ipv6 2001:db8:101:201::1
   ```
   ```
     PING 2001:db8:101:201::1 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8:101:201::1
       bytes=56 Sequence=1 hop limit=64  time = 4 ms
       Reply from 2001:db8:101:201::1
       bytes=56 Sequence=2 hop limit=64  time = 3 ms
       Reply from 2001:db8:101:201::1
       bytes=56 Sequence=3 hop limit=64  time = 2 ms
       Reply from 2001:db8:101:201::1
       bytes=56 Sequence=4 hop limit=64  time = 2 ms
       Reply from 2001:db8:101:201::1
       bytes=56 Sequence=5 hop limit=64  time = 2 ms
     --- 2001:db8:101:201::1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 2/2/4 ms
   ```
   
   # On PC1, ping the IPv6 address of PC2. The following command output shows that the ping is successful.
   
   ```
   C:\> ping 2001:db8:101:201::2
   ```
   ```
   Pinging 2001:db8:101:201::2 with 32 bytes of data:
   Reply from 2001:db8:101:201::2: time<1ms
   Reply from 2001:db8:101:201::2: time<1ms
   Reply from 2001:db8:101:201::2: time<1ms
   Reply from 2001:db8:101:201::2: time<1ms
   Ping statistics for 2001:db8:101:201::2:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 0ms, Maximum = 0ms, Average = 0ms
   ```

#### Configuration Files

DeviceA configuration file

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
 ipv6 enable
 ipv6 address 2001:db8:101:101::1 64
#
interface Tunnel 1
 ipv6 enable
 ipv6 address 2001:db8:101:100::1 56
 tunnel-protocol ipv6-ipv4 6rd
 source GigabitEthernet0/1/1
 ipv6-prefix 2001:db8::/32
 ipv4-prefix length 8
#
ipv6 route-static 2001:db8:: 32 Tunnel1
#
return
```

Device B configuration file

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
 ipv6 enable
 ipv6 address 2001:db8:101:201::1 64
#
interface Tunnel 1
 ipv6 enable
 ipv6 address 2001:db8:101:200::1 56
 tunnel-protocol ipv6-ipv4 6rd
 source GigabitEthernet0/1/1
 ipv6-prefix 2001:db8::/32
 ipv4-prefix length 8
#
ipv6 route-static 2001:db8:: 32 Tunnel1
#
return
```