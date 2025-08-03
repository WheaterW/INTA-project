Example for Configuring IPv4 FRR
================================

Example for Configuring IPv4 FRR

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001352724596__fig_dc_vrp_ip-route_cfg_002401), it is required that a backup outbound interface and a backup next hop be configured on DeviceT so that Link B functions as the backup of Link A. If Link A fails, traffic is rapidly switched to Link B.

**Figure 1** Configuring public network IPv4 FRR![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1, Interface2, and Interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001404424321.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic OSPF functions on DeviceT, DeviceA, and DeviceC.
2. Enable basic IS-IS functions on DeviceT, DeviceB, and DeviceC.
3. Enable public network IPv4 FRR on DeviceT, and check the backup outbound interface and backup next hop.
4. Disable IPv4 FRR, and check the backup outbound interface and backup next hop.

#### Procedure

1. Assign an IP address to each interface. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001352724596__postreq1748752215419).
2. Configure OSPF on DeviceT, DeviceA, and DeviceC. For details, see [Configuration Scripts](#EN-US_TASK_0000001352724596__postreq1748752215419).
3. Configure IS-IS on DeviceT, DeviceB, and DeviceC. For details, see [Configuration Scripts](#EN-US_TASK_0000001352724596__postreq1748752215419).
4. Check routing information.
   
   
   
   # Check the routes destined for 172.17.1.0 on DeviceT.
   
   ```
   <DeviceT> display ip routing-table 172.17.1.0 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 2
   
   Destination: 172.17.1.0/24
        Protocol: OSPF            Process ID: 1
      Preference: 10                    Cost: 3
         NextHop: 192.168.10.2     Neighbour: 0.0.0.0
           State: Active Adv             Age: 00h00m07s
             Tag: 0                 Priority: low
           Label: NULL               QoSInfo: 0xa98ac7
      IndirectID: 0x40000041
    RelayNextHop: 0.0.0.0          Interface: 100GE1/0/2
        TunnelID: 0x0                  Flags: D
      RouteColor: 0
   
   Destination: 172.17.1.0/24
        Protocol: ISIS            Process ID: 1
      Preference: 15                    Cost: 30
         NextHop: 192.168.20.2     Neighbour: 0.0.0.0
           State: Inactive Adv           Age: 00h01m26s
             Tag: 0                 Priority: high
           Label: NULL               QoSInfo: 0xa98ac7
      IndirectID: 0x80000081
    RelayNextHop: 0.0.0.0          Interface: 100GE1/0/3
        TunnelID: 0x0                  Flags: 0
      RouteColor: 0
   ```
   
   
   
   The command output shows that there are two routes to 172.17.1.0/24. The route with the next hop 192.168.10.2 is the optimal route because the priority of OSPF routes is higher than that of IS-IS routes.
5. Enable public network IPv4 FRR.
   
   
   
   # Enable IPv4 FRR on DeviceT.
   
   ```
   [~DeviceT] ip frr
   [*DeviceT] commit
   ```
   
   # Check the backup outbound interface and the backup next hop on DeviceT.
   
   ```
   <DeviceT> display ip routing-table 172.17.1.0 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 2
   
   Destination: 172.17.1.0/24
        Protocol: OSPF            Process ID: 1
      Preference: 10                    Cost: 3
         NextHop: 192.168.10.2     Neighbour: 0.0.0.0
           State: Active Adv             Age: 00h01m36s
             Tag: 0                 Priority: low
           Label: NULL               QoSInfo: 0xa98ac7
      IndirectID: 0x40000041
    RelayNextHop: 0.0.0.0          Interface: 100GE1/0/2
        TunnelID: 0x0                  Flags: D
      RouteColor: 0
       BkNextHop: 192.168.20.2   BkInterface: 100GE1/0/3
         BkLabel: NULL           SecTunnelID: 0x0
    BkPETunnelID: 0x0        BkPESecTunnelID: 0x0
    BkIndirectID: 0x80000081
   
   Destination: 172.17.1.0/24
        Protocol: ISIS            Process ID: 1
      Preference: 15                    Cost: 30
         NextHop: 192.168.20.2     Neighbour: 0.0.0.0
           State: Inactive Adv           Age: 00h02m55s
             Tag: 0                 Priority: high
           Label: NULL               QoSInfo: 0xa98ac7
      IndirectID: 0x80000081
    RelayNextHop: 0.0.0.0          Interface: 100GE1/0/3
        TunnelID: 0x0                  Flags: 0
      RouteColor: 0
   ```
   
   In the routing table, you can view that the route to 172.17.1.0/24 has a backup outbound interface and a backup next hop. The IS-IS route becomes a backup route.

#### Verifying the Configuration

# Simulate a link fault on DeviceT.

```
[~DeviceT] interface 100GE1/0/2
[~DeviceT-100GE1/0/2] shutdown
[*DeviceT-100GE1/0/2] commit
[~DeviceT-100GE1/0/2] quit
```

# On DeviceT, check the routes to 172.17.1.0/24.

```
<DeviceT> display ip routing-table 172.17.1.0 verbose
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
Summary Count : 1

Destination: 172.17.1.0/24
     Protocol: ISIS            Process ID: 1
   Preference: 15                    Cost: 30
      NextHop: 192.168.20.2     Neighbour: 0.0.0.0
        State: Active Adv             Age: 00h57m30s
          Tag: 0                 Priority: high
        Label: NULL               QoSInfo: 0xa98ac7
   IndirectID: 0x80000081
 RelayNextHop: 0.0.0.0          Interface: 100GE1/0/3
     TunnelID: 0x0                  Flags: D
   RouteColor: 0

```

The preceding command output shows that traffic is switched to Link B after Link A fails.


#### Configuration Scripts

* DeviceT
  
  ```
  #
  sysname DeviceT
  #
  ip frr
  #
  isis 1
   network-entity 10.0000.0000.0001.00
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
   isis enable 1
  #
  ospf 1
   area 0.0.0.0
    network 192.168.10.0 0.0.0.255
   area 0.0.0.1
    network 172.16.1.0 0.0.0.255
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
  ospf 1
   area 0.0.0.0
    network 192.168.10.0 0.0.0.255
    network 192.168.11.0 0.0.0.255
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  isis 1
   network-entity 10.0000.0000.0002.00 
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.20.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.21.2 255.255.255.0
   isis enable 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  isis 1
   network-entity 10.0000.0000.0003.00 
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.17.1.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.11.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.21.1 255.255.255.0
   isis enable 1
  #
  ospf 1
   area 0.0.0.0
    network 192.168.11.0 0.0.0.255
    network 192.168.21.0 0.0.0.255
   area 0.0.0.2
    network 172.17.1.0 0.0.0.255
  #
  return
  ```