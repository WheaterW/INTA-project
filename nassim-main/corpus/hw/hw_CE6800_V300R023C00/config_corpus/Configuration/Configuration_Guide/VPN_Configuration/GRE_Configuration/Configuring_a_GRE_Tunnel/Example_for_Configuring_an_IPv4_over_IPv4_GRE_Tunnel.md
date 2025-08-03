Example for Configuring an IPv4 over IPv4 GRE Tunnel
====================================================

Example for Configuring an IPv4 over IPv4 GRE Tunnel

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176742273__fig_dc_vrp_gre_cfg_203101), DeviceA, DeviceB, and DeviceC belong to the IPv4 backbone network and are running OSPF. A direct link needs to be established between DeviceA and DeviceC to ensure that PC1 and PC2 can communicate with each other. To meet such a requirement, a GRE tunnel needs to be established between DeviceA and DeviceC and static routes need to be configured so that packets between PC1 and PC2 can be forwarded through tunnel interfaces on both ends of the tunnel. DeviceA and DeviceC are the default gateways of PC1 and PC2, respectively.

**Figure 1** Configuring an IPv4 over IPv4 GRE tunnel![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176742289.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv4 dynamic routing protocol for communication between the devices.
2. Create tunnel interfaces on DeviceA and DeviceC and specify the tunnel source and destination addresses. The tunnel source address is the IP address of the interface that sends packets, and the tunnel destination address is the IP address of the interface that receives packets.
3. Configure IP addresses for the tunnel interfaces to generate tunnel routes.
4. Configure a static route between DeviceA and PC1 and between DeviceC and PC2 and specify the local tunnel interface as the outbound interface of the static route so that traffic between PC1 and PC2 can be transmitted through the GRE tunnel.

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   Configure an IP address for each interface according to [Figure 1](#EN-US_TASK_0000001176742273__fig_dc_vrp_gre_cfg_203101). For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176742273__postreq9126101612412).
2. Configure an IGP on the VPN backbone network.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.20.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 172.20.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 172.21.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospf 1
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 172.21.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   After the configuration is complete, run the **display ip routing-table** command on DeviceA and DeviceC. The command outputs show that DeviceA and DeviceC can learn the OSPF route to the network segment of the remote interface.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   Proto: Protocol        Pre: Preference
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 11       Routes : 11
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
          10.1.1.0/24  Direct  0    0             D  10.1.1.2        100GE1/0/2
          10.1.1.2/32  Direct  0    0             D  127.0.0.1       100GE1/0/2
        10.1.1.255/32  Direct  0    0             D  127.0.0.1       100GE1/0/2
        172.20.1.0/24  Direct  0    0             D  172.20.1.1      100GE1/0/1
        172.20.1.1/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
      172.20.1.255/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
        172.21.1.0/24  OSPF    10   2             D  172.20.1.2      100GE1/0/1
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```
3. Configure tunnel interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface tunnel 1
   [*DeviceA-Tunnel1] tunnel-protocol gre
   [*DeviceA-Tunnel1] ip address 172.22.1.1 255.255.255.0
   [*DeviceA-Tunnel1] source 172.20.1.1
   [*DeviceA-Tunnel1] destination 172.21.1.2
   [*DeviceA-Tunnel1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface tunnel 1
   [*DeviceC-Tunnel1] tunnel-protocol gre
   [*DeviceC-Tunnel1] ip address 172.22.1.2 255.255.255.0
   [*DeviceC-Tunnel1] source 172.21.1.2
   [*DeviceC-Tunnel1] destination 172.20.1.1
   [*DeviceC-Tunnel1] quit
   [*DeviceC] commit
   ```
   
   After the configuration is complete, the status of tunnel interfaces becomes up and the tunnel interfaces can ping each other successfully.
   
   # The following example uses the command output on DeviceA.
   
   ```
   
   [~DeviceA] ping -a 172.22.1.1 172.22.1.2
     PING 172.22.1.2: 56  data bytes, press CTRL_C to break
       Reply from 172.22.1.2: bytes=56 Sequence=1 ttl=255 time=24 ms
       Reply from 172.22.1.2: bytes=56 Sequence=2 ttl=255 time=33 ms
       Reply from 172.22.1.2: bytes=56 Sequence=3 ttl=255 time=48 ms
       Reply from 172.22.1.2: bytes=56 Sequence=4 ttl=255 time=33 ms
       Reply from 172.22.1.2: bytes=56 Sequence=5 ttl=255 time=36 ms
     --- 172.22.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 24/34/48 ms
   ```
4. Configure static routes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ip route-static 10.2.1.0 255.255.255.0 tunnel1
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ip route-static 10.1.1.0 255.255.255.0 tunnel1
   [*DeviceC] commit
   ```

#### Verifying the Configuration

After the configuration is complete, run the **display** **ip routing-table** command on DeviceA and DeviceC. The command outputs show the static route with the local tunnel interface as the outbound interface and destined for the network segment of the remote end.

# The following example uses the command output on DeviceA.

```
[~DeviceA] display ip routing-table
Proto: Protocol        Pre: Preference
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 15       Routes : 15

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

       10.1.1.0/24  Direct  0    0             D  10.1.1.2        100GE1/0/2
       10.1.1.2/32  Direct  0    0             D  127.0.0.1       100GE1/0/2
     10.1.1.255/32  Direct  0    0             D  127.0.0.1       100GE1/0/2
    10.2.1.0/24  Static  60   0           D  172.22.1.1       Tunnel1
     172.20.1.0/24  Direct  0    0             D  172.20.1.1      100GE1/0/1
     172.20.1.1/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
   172.20.1.255/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
     172.21.1.0/24  OSPF    10   2             D  172.20.1.2      100GE1/0/1
     172.22.1.0/24  Direct  0    0             D  172.22.1.1      Tunnel1
     172.22.1.1/32  Direct  0    0             D  127.0.0.1       Tunnel1
   172.22.1.255/32  Direct  0    0             D  127.0.0.1       Tunnel1
      127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.20.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  interface Tunnel1
   ip address 172.22.1.1 255.255.255.0
   tunnel-protocol gre
   source 172.20.1.1
   destination 172.21.1.2
  #
  ospf 1
   area 0.0.0.0
    network 172.20.1.0 0.0.0.255
  #
  ip route-static 10.2.1.0 255.255.255.0 Tunnel1
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
   ip address 172.20.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.21.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 172.20.1.0 0.0.0.255
    network 172.21.1.0 0.0.0.255
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
   ip address 172.21.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.2 255.255.255.0
  #
  interface Tunnel1
   ip address 172.22.1.2 255.255.255.0
   tunnel-protocol gre
   source 172.21.1.2
   destination 172.20.1.1
  #
  ospf 1
   area 0.0.0.0
   network 172.21.1.0 0.0.0.255
  #
  ip route-static 10.1.1.0 255.255.255.0 Tunnel1
  #
  return
  ```