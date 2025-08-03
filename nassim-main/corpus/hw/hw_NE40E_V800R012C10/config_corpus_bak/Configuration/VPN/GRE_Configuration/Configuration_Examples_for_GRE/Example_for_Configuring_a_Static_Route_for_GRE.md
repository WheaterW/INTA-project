Example for Configuring a Static Route for GRE
==============================================

This section provides an example for configuring static routes for GRE. The configuration allows traffic between users to be transmitted over GRE tunnels. Static routes are required between a device and its connected clients.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369095__fig_dc_vrp_gre_cfg_203101), DeviceA, DeviceB, and DeviceC belong to the VPN backbone network, and OSPF runs among them.

It is required that a direct link be established between DeviceA and DeviceC. To meet such a requirement, configure a GRE tunnel between DeviceA and DeviceC and specify the tunnel interface as the outbound interface of a static route, so that PC1 and PC2 can communicate with each other.

PC1 and PC2 respectively use DeviceA and DeviceC as their default gateways.

**Figure 1** Configuring static routes for GRE![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and Tunnel1, respectively.


  
![](images/fig_dc_vrp_gre_cfg_203101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a dynamic routing protocol for Routers to communicate.
2. Create tunnel interfaces on DeviceA and DeviceC, and specify the source and destination addresses of the tunnel interfaces. The tunnel source address is the IP address of the interface that sends packets, and the tunnel destination address is the IP address of the interface that receives packets.
3. To enable the tunnel to support dynamic routing protocols, you also need to configure an IP address for the tunnel interface.
4. To transmit traffic between PC1 and PC2 through the GRE tunnel, configure a static route to PC2 on DeviceA and a static route to PC1 on DeviceC, and specify the local tunnel interface as the outbound interface of the corresponding static route.

#### Data Preparation

To complete the configuration, you need the following data:

* Data required for running OSPF
* Source and destination addresses of the GRE tunnel, and tunnel interface IP addresses

#### Procedure

1. Configure interface IP addresses.
   
   
   
   Configure IP addresses for interfaces as shown in [Figure 1](#EN-US_TASK_0172369095__fig_dc_vrp_gre_cfg_203101). For detailed configurations, see Configuration Files.
2. Configure IGP on the VPN backbone network.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.20.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospf-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 172.20.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 172.21.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospf-1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] area 0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 172.21.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceC-ospf-1] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   After the configuration is complete, run the **display ip routing-table** command on DeviceA and DeviceC. The command output shows that they have learned the OSPF route to the network segment of each other's interconnection interface.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 11       Routes : 11
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
          10.1.1.0/24  Direct  0    0             D  10.1.1.2        GigabitEthernet0/2/0
          10.1.1.2/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0
        10.1.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0
        172.20.1.0/24  Direct  0    0             D  172.20.1.1      GigabitEthernet0/1/0
        172.20.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
      172.20.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
        172.21.1.0/24  OSPF    10   2             D  172.20.1.2      GigabitEthernet0/1/0
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```
3. Configure tunnel interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] binding tunnel gre
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] interface tunnel 1
   ```
   ```
   [*DeviceA-Tunnel1] tunnel-protocol gre
   ```
   ```
   [*DeviceA-Tunnel1] ip address 172.22.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-Tunnel1] source 172.20.1.1
   ```
   ```
   [*DeviceA-Tunnel1] destination 172.21.1.2
   ```
   ```
   [*DeviceA-Tunnel1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] binding tunnel gre
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceC] interface tunnel 1
   ```
   ```
   [*DeviceC-Tunnel1] tunnel-protocol gre
   ```
   ```
   [*DeviceC-Tunnel1] ip address 172.22.1.2 255.255.255.0
   ```
   ```
   [*DeviceC-Tunnel1] source 172.21.1.2
   ```
   ```
   [*DeviceC-Tunnel1] destination 172.20.1.1
   ```
   ```
   [*DeviceC-Tunnel1] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   After the configuration is complete, the tunnel interfaces go up and can ping each other.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] ping -a 172.22.1.1 172.22.1.2
   ```
   ```
     PING 172.22.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 172.22.1.2: bytes=56 Sequence=1 ttl=255 time=24 ms
   ```
   ```
       Reply from 172.22.1.2: bytes=56 Sequence=2 ttl=255 time=33 ms
   ```
   ```
       Reply from 172.22.1.2: bytes=56 Sequence=3 ttl=255 time=48 ms
   ```
   ```
       Reply from 172.22.1.2: bytes=56 Sequence=4 ttl=255 time=33 ms
   ```
   ```
       Reply from 172.22.1.2: bytes=56 Sequence=5 ttl=255 time=36 ms
   ```
   ```
     --- 172.22.1.2 ping statistics ---
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
       round-trip min/avg/max = 24/34/48 ms
   ```
4. Configure static routes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ip route-static 10.2.1.0 255.255.255.0 tunnel1
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ip route-static 10.1.1.0 255.255.255.0 tunnel1
   ```
   ```
   [*DeviceC] commit
   ```
5. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display** **ip routing-table** command on DeviceA and DeviceC. The command output shows the static route from the local tunnel interface to the user-side network segment of the peer.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 15       Routes : 15
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
          10.1.1.0/24  Direct  0    0             D  10.1.1.2        GigabitEthernet0/2/0
          10.1.1.2/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0
        10.1.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0
       10.2.1.0/24  Static  60   0           D  172.22.1.1       Tunnel1
        172.20.1.0/24  Direct  0    0             D  172.20.1.1      GigabitEthernet0/1/0
        172.20.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
      172.20.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
        172.21.1.0/24  OSPF    10   2             D  172.20.1.2      GigabitEthernet0/1/0
        172.22.1.0/24  Direct  0    0             D  172.22.1.1      Tunnel1
        172.22.1.1/32  Direct  0    0             D  127.0.0.1       Tunnel1
      172.22.1.255/32  Direct  0    0             D  127.0.0.1       Tunnel1
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 172.20.1.1 255.255.255.0
   binding tunnel gre
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
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
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 172.20.1.2 255.255.255.0
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip address 172.21.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 172.20.1.0 0.0.0.255
    network 172.21.1.0 0.0.0.255
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 172.21.1.2 255.255.255.0
   binding tunnel gre
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
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