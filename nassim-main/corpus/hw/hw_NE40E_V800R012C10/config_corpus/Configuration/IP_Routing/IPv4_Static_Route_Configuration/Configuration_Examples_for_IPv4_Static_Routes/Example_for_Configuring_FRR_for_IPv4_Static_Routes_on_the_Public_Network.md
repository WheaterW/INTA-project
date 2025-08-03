Example for Configuring FRR for IPv4 Static Routes on the Public Network
========================================================================

FRR for IPv4 static routes on the public network can fast detect link failures.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365467__fig_dc_vrp_static-route_disjoin_cfg_002101), it is required that two IPv4 static routes with Device A and Device B as the next hops be configured on Device T and that Link B function as the backup of Link A. If Link A fails, traffic is switched to Link B immediately.

**Figure 1** Configuring FRR for IPv4 static routes on the public network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_002101.png)  


#### Precautions

When configuring FRR for IPv4 static routes on the public network, ensure that there are at least two IPv4 static routes to the same destination address.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure two IPv4 static routes with Device A and Device B as the next hops on Device T.
2. Set a lower preference value for Link A on Device T so that Link A is preferentially selected.
3. Enable FRR for IPv4 static routes on Device T, and check the backup outbound interface and the backup next hop.
4. Configure static BFD for IPv4 static routes to speed up fault detection.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To speed up fault detection, configure dynamic or static BFD for IPv4 static routes. Static BFD for IPv4 static routes is used as an example because it is more common than dynamic BFD for IPv4 static routes on the live network.
5. Disable FRR for IPv4 static routes, and check the backup outbound interface and the backup next hop.

#### Data Preparation

To complete the configuration, you need preference values of IPv4 static routes.


#### Procedure

1. Configure IP addresses for interfaces. For detailed configurations, see Configuration Files.
2. Configure IPv4 static routes.
   
   
   
   # On Device A, configure IPv4 static routes.
   
   ```
   [~DeviceA] ip route-static 172.16.1.0 24 GigabitEthernet0/1/0 192.168.10.1
   ```
   ```
   [*DeviceA] ip route-static 172.17.1.0 24 GigabitEthernet0/2/0 192.168.11.1
   ```
   ```
   [*DeviceA] commit
   ```
   
   # On Device B, configure static routes.
   
   ```
   [~DeviceB] ip route-static 172.16.1.0 24 GigabitEthernet0/1/0 192.168.20.1
   ```
   ```
   [*DeviceB] ip route-static 172.17.1.0 24 GigabitEthernet0/2/0 192.168.21.1
   ```
   ```
   [*DeviceB] commit
   ```
   
   # On Device C, configure IPv4 static routes.
   
   ```
   [~DeviceC] ip route-static 172.16.1.0 24 GigabitEthernet0/2/0 192.168.11.2
   ```
   ```
   [*DeviceC] ip route-static 172.16.1.0 24 GigabitEthernet0/3/0 192.168.21.2
   ```
   ```
   [*DeviceC] ip route-static 192.168.10.0 24 GigabitEthernet0/2/0 192.168.11.2
   ```
   ```
   [*DeviceC] ip route-static 192.168.20.0 24 GigabitEthernet0/3/0 192.168.21.2
   ```
   ```
   [*DeviceC] commit
   ```
   
   # On Device T, configure IPv4 static routes.
   
   ```
   [~DeviceT] ip route-static 172.17.1.0 24 GigabitEthernet0/2/0 192.168.10.2
   ```
   ```
   [*DeviceT] ip route-static 172.17.1.0 24 GigabitEthernet0/3/0 192.168.20.2
   ```
   ```
   [*DeviceT] ip route-static 192.168.11.0 24 GigabitEthernet0/2/0 192.168.10.2
   ```
   ```
   [*DeviceT] ip route-static 192.168.21.0 24 GigabitEthernet0/3/0 192.168.20.2
   ```
   ```
   [*DeviceT] commit
   ```
   ```
   [~DeviceT] quit
   ```
   
   # Check the IP routing table of Device T. The following command output shows that load balancing is performed between the two IPv4 static routes.
   
   ```
   <DeviceT> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 16       Routes : 16
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
        172.16.1.0/24  Direct  0    0             D   172.16.1.1      GigabitEthernet0/1/0
        172.16.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0
      172.16.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0
      172.17.1.0/24  Static 60  0             D  192.168.10.2    GigabitEthernet0/2/0
                     Static 60  0             D  192.168.20.2    GigabitEthernet0/3/0
      192.168.10.0/24  Direct  0    0             D   192.168.10.1    GigabitEthernet0/2/0
      192.168.10.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
    192.168.10.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
      192.168.11.0/24  Static  60   0             D   192.168.10.2    GigabitEthernet0/2/0
      192.168.20.0/24  Direct  0    0             D   192.168.20.1    GigabitEthernet0/3/0
      192.168.20.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/3/0
    192.168.20.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/3/0
      192.168.21.0/24  Static  60   0             D   192.168.20.2    GigabitEthernet0/3/0
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
   ```
3. Change the priorities of the IPv4 static routes.
   
   
   
   # Change the priorities of static routes on Device T.
   
   ```
   <DeviceT> system-view
   ```
   ```
   [~DeviceT] ip route-static 172.17.1.0 24 GigabitEthernet0/2/0 192.168.10.2  preference 40
   ```
   ```
   [*DeviceT] commit
   ```
   ```
   [~DeviceT] quit
   ```
   
   # Check the IP routing table of Device T. The following command output shows that the preference value of the IPv4 static route has been changed.
   
   ```
   <DeviceT> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 16       Routes : 16
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
        172.16.1.0/24  Direct  0    0             D   172.16.1.1      GigabitEthernet0/1/0
        172.16.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0
      172.16.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0
      172.17.1.0/24  Static 40   0             D  192.168.10.2    GigabitEthernet0/2/0
      192.168.10.0/24  Direct  0    0             D   192.168.10.1    GigabitEthernet0/2/0
      192.168.10.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
    192.168.10.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
      192.168.11.0/24  Static  60   0             D   192.168.10.2    GigabitEthernet0/2/0
      192.168.20.0/24  Direct  0    0             D   192.168.20.1    GigabitEthernet0/3/0
      192.168.20.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/3/0
    192.168.20.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/3/0
      192.168.21.0/24  Static  60   0             D   192.168.20.2    GigabitEthernet0/3/0
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
   ```
4. Enable FRR for IPv4 static routes.
   
   
   
   # Enable FRR for static route on Device T.
   
   ```
   <DeviceT> system-view
   ```
   ```
   [~DeviceT] ip route-static frr
   ```
   ```
   [*DeviceT] commit
   ```
   ```
   [~DeviceT] quit
   ```
   
   # Check the backup outbound interface and the backup next hop on Device T.
   
   ```
   <DeviceT> display ip routing-table 172.17.1.0 verbose
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination: 172.17.1.0/24
        Protocol: Static          Process ID: 0
      Preference: 40                    Cost: 0
         NextHop: 192.168.10.2     Neighbour: 0.0.0.0
           State: Active Adv             Age: 00h00m03s
             Tag: 0                 Priority: medium
           Label: NULL               QoSInfo: 0x0
      IndirectID: 0x31000032
    RelayNextHop: 0.0.0.0          Interface: GigabitEthernet0/2/0
        TunnelID: 0x0                  Flags: D
       BkNextHop: 192.168.20.2   BkInterface: GigabitEthernet0/3/0
         BkLabel: NULL           SecTunnelID: 0x0
    BkPETunnelID: 0x0        BkPESecTunnelID: 0x0
    BkIndirectID: 0x32000033
   ```
5. Configure static BFD for IPv4 static routes.
   
   
   * Configure a BFD session.
     
     # On Device T, configure a BFD session between Device T and Device C.
     
     ```
     <DeviceT> system-view
     ```
     ```
     [~DeviceT] bfd
     ```
     ```
     [*DeviceT-bfd] quit
     ```
     ```
     [*DeviceT] bfd aa bind peer-ip 192.168.11.1 source-ip 192.168.10.1
     ```
     ```
     [*DeviceT-bfd-session-aa] discriminator local 10
     ```
     ```
     [*DeviceT-bfd-session-aa] discriminator remote 20
     ```
     ```
     [*DeviceT-bfd-session-aa] commit
     ```
     ```
     [~DeviceT-bfd-session-aa] quit
     ```
     
     # On Device C, configure a BFD session between Device C and Device T.
     
     ```
     <DeviceC> system-view
     ```
     ```
     [~DeviceC] bfd
     ```
     ```
     [*DeviceC-bfd] quit
     ```
     ```
     [*DeviceC] bfd ab bind peer-ip 192.168.10.1 source-ip 192.168.11.1
     ```
     ```
     [*DeviceC-bfd-session-ab] discriminator local 20
     ```
     ```
     [*DeviceC-bfd-session-ab] discriminator remote 10
     ```
     ```
     [*DeviceC-bfd-session-ab] commit
     ```
     ```
     [~DeviceC-bfd-session-ab] quit
     ```
   * Configure a static route and bind it to the BFD session.
     
     # On Device T, configure a static route and bind it to the BFD session named **aa**.
     
     ```
     [~DeviceT] ip route-static 172.17.1.0 24 GigabitEthernet0/2/0 192.168.10.2 preference 40 track bfd-session aa
     ```
6. Simulate a fault on Link A.
   
   
   ```
   <DeviceT> system-view
   ```
   ```
   [~DeviceT] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceT-GigabitEthernet0/2/0] shutdown
   ```
   ```
   [~DeviceT-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceT-GigabitEthernet0/2/0] quit
   ```
   ```
   [~DeviceT] quit
   ```
   
   # Check the routes to 172.17.1.0/24 on Device T.
   
   ```
   <DeviceT> display ip routing-table 172.17.1.0 verbose
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination: 172.17.1.0/24
        Protocol: Static          Process ID: 0
      Preference: 60                    Cost: 0
         NextHop: 192.168.20.2     Neighbour: 0.0.0.0
           State: Active Adv             Age: 00h00m07s
             Tag: 0                 Priority: medium
           Label: NULL               QoSInfo: 0x0
      IndirectID: 0x32000033
    RelayNextHop: 0.0.0.0          Interface: GigabitEthernet0/3/0
        TunnelID: 0x0                  Flags: D
   ```

#### Configuration Files

* Device T configuration file
  
  ```
  #
  sysname DeviceT
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 192.168.20.1 255.255.255.0
  #
  bfd aa bind peer-ip 192.168.11.1 source-ip 192.168.10.1
   discriminator local 10
   discriminator remote 20
  #
  ip route-static frr
  ip route-static 172.17.1.0 24 GigabitEthernet0/2/0 192.168.10.2 preference 40 track bfd-session aa
  ip route-static 172.17.1.0 24 GigabitEthernet0/3/0 192.168.20.2
  ip route-static 192.168.11.0 24 GigabitEthernet0/2/0 192.168.10.2
  ip route-static 192.168.21.0 24 GigabitEthernet0/3/0 192.168.20.2 
  #
  return
  ```
* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.10.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.11.2 255.255.255.0
  #
  ip route-static 172.16.1.0 24 GigabitEthernet0/1/0 192.168.10.1
  ip route-static 172.17.1.0 24 GigabitEthernet0/2/0 192.168.11.1
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
   ip address 192.168.20.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.21.2 255.255.255.0
  #
  ip route-static 172.16.1.0 24 GigabitEthernet0/1/0 192.168.20.1
  ip route-static 172.17.1.0 24 GigabitEthernet0/2/0 192.168.10.1
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.17.1.0 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.11.1 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 192.168.21.1 255.255.255.0
  #
  bfd ab bind peer-ip 192.168.10.1 source-ip 192.168.11.1
   discriminator local 20
   discriminator remote 10
  #
  ip route-static 172.16.1.0 24 GigabitEthernet0/2/0 192.168.11.2
  ip route-static 172.16.1.0 24 GigabitEthernet0/3/0 192.168.21.2
  ip route-static 192.168.10.0 255.255.255.0 GigabitEthernet0/2/0 192.168.11.2
  ip route-static 192.168.20.0 255.255.255.0 GigabitEthernet0/3/0 192.168.21.2 
  #
  return
  ```