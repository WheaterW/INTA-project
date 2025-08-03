Example for Configuring IPv4 Static Route FRR
=============================================

Example for Configuring IPv4 Static Route FRR

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176742411__fig1431681518820), two IPv4 static routes are configured on DeviceD. The next hop in one static route is set to DeviceA and that in the other static route is set to DeviceB. Link B backs up link A. If link A fails, traffic is rapidly switched to link B.

**Figure 1** Network diagram of IPv4 static route FRR![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176662557.png)

#### Precautions

Note the following during the configuration:

* Ensure that there are at least two IPv4 static routes to the same destination address when configuring IPv4 static route FRR.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each device.
2. Configure IPv4 static routes on each device. Configure two IPv4 static routes with the next hops set to DeviceA and DeviceB, respectively, on DeviceD.
3. Set a smaller preference value for link A on DeviceD so that DeviceD preferentially selects link A.
4. Enable IPv4 static route FRR on DeviceD.
5. Configure static BFD for IPv4 static route to speed up fault detection.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To speed up fault detection, configure dynamic or static BFD for IPv4 static route. In this example, static BFD for IPv4 static route is used. This is because it is more common than dynamic BFD for IPv4 static route on the live network.

#### Procedure

1. Configure IPv4 addresses for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 192.168.10.2 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 192.168.11.2 255.255.255.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176742411__postreq24192593172748).
2. Configure an IPv4 static route on each device, and configure two IPv4 static routes with next hops set to DeviceA and DeviceB on DeviceD.
   
   
   
   # Configure IPv4 static routes on DeviceA.
   
   ```
   [~DeviceA] ip route-static 172.16.1.0 24 100ge 1/0/1 192.168.10.1
   [*DeviceA] ip route-static 172.17.1.0 24 100ge 1/0/2 192.168.11.1
   [*DeviceA] commit
   ```
   
   # Configure IPv4 static routes on DeviceB.
   
   ```
   [~DeviceB] ip route-static 172.16.1.0 24 100ge 1/0/1 192.168.20.1
   [*DeviceB] ip route-static 172.17.1.0 24 100ge 1/0/2 192.168.21.1
   [*DeviceB] commit
   ```
   
   # Configure IPv4 static routes on DeviceC.
   
   ```
   [~DeviceC] ip route-static 172.16.1.0 24 100ge 1/0/2 192.168.11.2
   [*DeviceC] ip route-static 172.16.1.0 24 100ge 1/0/3 192.168.21.2
   [*DeviceC] ip route-static 192.168.10.0 24 100ge 1/0/2 192.168.11.2
   [*DeviceC] ip route-static 192.168.20.0 24 100ge 1/0/3 192.168.21.2
   [*DeviceC] commit
   ```
   
   # Configure IPv4 static routes on DeviceD.
   
   ```
   [~DeviceD] ip route-static 172.17.1.0 24 100ge 1/0/2 192.168.10.2 
   [*DeviceD] ip route-static 172.17.1.0 24 100ge 1/0/3 192.168.20.2 
   [*DeviceD] ip route-static 192.168.11.0 24 100ge 1/0/2 192.168.10.2
   [*DeviceD] ip route-static 192.168.21.0 24 100ge 1/0/3 192.168.20.2
   [*DeviceD] commit
   ```
   
   # Check the IP routing table of DeviceD.
   
   ```
   [~DeviceD] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 16       Routes : 16
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
        172.16.1.0/24  Direct  0    0             D   172.16.1.1      100GE1/0/1
        172.16.1.1/32  Direct  0    0             D   127.0.0.1       100GE1/0/1
      172.16.1.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/1
      172.17.1.0/24  Static 60   0             D  192.168.10.2   100GE1/0/2
                       Static 60   0             D  192.168.20.2   100GE1/0/3
      192.168.10.0/24  Direct  0    0             D   192.168.10.1    100GE1/0/2
      192.168.10.1/32  Direct  0    0             D   127.0.0.1       100GE1/0/2
    192.168.10.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/2
      192.168.11.0/24  Static  60   0             D   192.168.10.2    100GE1/0/2
      192.168.20.0/24  Direct  0    0             D   192.168.20.1    100GE1/0/3
      192.168.20.1/32  Direct  0    0             D   127.0.0.1       100GE1/0/3
    192.168.20.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/3
      192.168.21.0/24  Static  60   0             D   192.168.20.2    100GE1/0/3
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
   ```
   
   The command output shows that two routes from DeviceD to 172.17.1.0/24 are working in load balancing mode.
3. On DeviceD, set a smaller preference value for link A so that DeviceD preferentially selects link A.
   
   
   
   # Change the preference value of one of the routes to 172.17.1.0.24 to 40 on DeviceD.
   
   ```
   [~DeviceD] ip route-static 172.17.1.0 24 100ge 1/0/2 192.168.10.2 preference 40
   [*DeviceD] commit
   ```
   
   # Check the routing table of DeviceD.
   
   ```
   [~DeviceD] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 16       Routes : 16
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
        172.16.1.0/24  Direct  0    0             D   172.16.1.1      100GE1/0/1
        172.16.1.1/32  Direct  0    0             D   127.0.0.1       100GE1/0/1
      172.16.1.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/1
      172.17.1.0/24  Static 40   0             D  192.168.10.2    100GE1/0/2
      192.168.10.0/24  Direct  0    0             D   192.168.10.1    100GE1/0/2
      192.168.10.1/32  Direct  0    0             D   127.0.0.1       100GE1/0/2
    192.168.10.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/2
      192.168.11.0/24  Static  60   0             D   192.168.10.2    100GE1/0/2
      192.168.20.0/24  Direct  0    0             D   192.168.20.1    100GE1/0/3
      192.168.20.1/32  Direct  0    0             D   127.0.0.1       100GE1/0/3
    192.168.20.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/3
      192.168.21.0/24  Static  60   0             D   192.168.20.2    100GE1/0/3
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
   ```
   
   The command output shows that there is only one route from DeviceD to 172.17.1.0/24 and that the preference value of the route is 40.
4. On DeviceD, enable IPv4 static route FRR, and check information about the backup outbound interface and backup next hop.
   
   
   ```
   [~DeviceD] ip route-static frr
   [*DeviceD] commit
   ```
   
   # Check information about the backup outbound interface and backup next hop of the route to 172.17.1.0 on DeviceD.
   
   ```
   [~DeviceD] display ip routing-table 172.17.1.0 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination: 172.17.1.0/24
        Protocol: Static          Process ID: 0
      Preference: 40                    Cost: 0
        NextHop: 192.168.10.2    Neighbour: 0.0.0.0
           State: Active Adv             Age: 00h00m03s
             Tag: 0                 Priority: medium
           Label: NULL               QoSInfo: 0x0
      IndirectID: 0x31000032
    RelayNextHop: 0.0.0.0         Interface: 100GE1/0/2
        TunnelID: 0x0                  Flags: D
      BkNextHop: 192.168.20.2  BkInterface: 100GE1/0/3
         BkLabel: NULL           SecTunnelID: 0x0
    BkPETunnelID: 0x0        BkPESecTunnelID: 0x0
    BkIndirectID: 0x32000033
   ```
   
   On DeviceD, the primary link to 172.17.1.0 is link A, and the backup link is link B.
5. Configure static BFD for IPv4 static route to speed up fault detection.
   
   
   
   # On DeviceD, configure a BFD session named **aa** between DeviceD and DeviceC.
   
   ```
   [~DeviceD] bfd
   [*DeviceD-bfd] quit
   [*DeviceD] bfd aa bind peer-ip 192.168.11.1 source-ip 192.168.10.1
   [*DeviceD-bfd-session-aa] discriminator local 10
   [*DeviceD-bfd-session-aa] discriminator remote 20
   [*DeviceD-bfd-session-aa] quit
   [*DeviceD] commit
   ```
   
   
   
   # On DeviceC, configure a BFD session named **ab** between DeviceC and DeviceD.
   
   ```
   [~DeviceC] bfd
   [*DeviceC-bfd] quit
   [*DeviceC] bfd ab bind peer-ip 192.168.10.1 source-ip 192.168.11.1
   [*DeviceC-bfd-session-ab] discriminator local 20
   [*DeviceC-bfd-session-ab] discriminator remote 10
   [*DeviceC-bfd-session-ab] quit
   [*DeviceC] commit
   ```
   
   
   
   # On DeviceD, bind the static route to the BFD session named **aa**.
   
   ```
   [~DeviceD] ip route-static 172.17.1.0 24 100ge 1/0/2 192.168.10.2 preference 40 track bfd-session aa
   [*DeviceD] commit
   ```
6. Simulate a fault on link A to rapidly switch traffic to link B.
   
   
   
   # Run the **shutdown** command on 100GE 1/0/2 of DeviceD.
   
   ```
   [~DeviceD] interface 100ge 1/0/2
   [~DeviceD-100GE1/0/2] shutdown
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# On DeviceD, check the route to 172.17.1.0/24.

```
[~DeviceD] display ip routing-table 172.17.1.0 verbose
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
Summary Count : 1

Destination: 172.17.1.0/24
     Protocol: Static          Process ID: 0
   Preference: 60                    Cost: 0
     NextHop: 192.168.20.2    Neighbour: 0.0.0.0
        State: Active Adv             Age: 00h00m07s
          Tag: 0                 Priority: medium
        Label: NULL               QoSInfo: 0x0
   IndirectID: 0x32000033
 RelayNextHop: 0.0.0.0         Interface: 100GE1/0/3
     TunnelID: 0x0                  Flags: D
```

After link A becomes faulty, configure DeviceD to ping 172.17.1.1. The command output shows that the packet loss time is within the BFD detection duration.


#### Configuration Scripts

* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.10.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.20.1 255.255.255.0
  #
  bfd aa bind peer-ip 192.168.11.1 source-ip 192.168.10.1
   discriminator local 10
   discriminator remote 20
  #
  ip route-static frr
  ip route-static 172.17.1.0 24 100GE1/0/2 192.168.10.2 preference 40 track bfd-session aa
  ip route-static 172.17.1.0 24 100GE1/0/3 192.168.20.2
  ip route-static 192.168.11.0 24 100GE1/0/2 192.168.10.2
  ip route-static 192.168.21.0 24 100GE1/0/3 192.168.20.2 
  #
  return
  ```
* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.10.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.11.2 255.255.255.0
  #
  ip route-static 172.16.1.0 24 100GE1/0/1 192.168.10.1
  ip route-static 172.17.1.0 24 100GE1/0/2 192.168.11.1
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
   ip address 192.168.20.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.21.2 255.255.255.0
  #
  ip route-static 172.16.1.0 24 100GE1/0/1 192.168.20.1
  ip route-static 172.17.1.0 24 100GE1/0/2 192.168.21.1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.17.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.11.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.21.1 255.255.255.0
  #
  bfd ab bind peer-ip 192.168.10.1 source-ip 192.168.11.1
   discriminator local 20
   discriminator remote 10
  #
  ip route-static 172.16.1.0 24 100GE1/0/2 192.168.11.2
  ip route-static 172.16.1.0 24 100GE1/0/3 192.168.21.2
  ip route-static 192.168.10.0 255.255.255.0 100GE1/0/2 192.168.11.2
  ip route-static 192.168.20.0 255.255.255.0 100GE1/0/3 192.168.21.2 
  #
  return
  ```