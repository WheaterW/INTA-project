Example for Configuring BFD for OSPF
====================================

Example for Configuring BFD for OSPF

#### Networking Requirements

An OSPF device periodically sends Hello packets to its neighbors for fault detection, and actually detecting a fault takes more than 1 second. As related technologies mature and develop, voice, video, and video on demand (VOD) services are now more widely used than ever before. Such services are sensitive to the packet loss rate and delay, and when the traffic rate reaches gigabit per second (Gbit/s), time-consuming fault detection results in the loss of a large number of packets. As such, the high reliability requirements of carrier-class networks cannot be met. To address this problem, configure BFD for OSPF to implement fault detection within milliseconds, maximizing OSPF convergence speeds in the case of link status changes.

For example, on the network shown in [Figure 1](#EN-US_TASK_0000001130623436__fig_dc_vrp_ospf_cfg_010201), the primary link (DeviceA -> DeviceB) and backup link (DeviceA -> DeviceC -> DeviceB) are deployed. In normal scenarios, service traffic is transmitted along the primary link. If the primary link goes faulty, DeviceA is expected to rapidly detect the fault and efficiently switch traffic to the backup link.

You can configure BFD for OSPF to monitor the OSPF neighbor relationship between DeviceA and DeviceB. If the link between DeviceA and DeviceB fails, BFD can rapidly detect the failure and report it to OSPF. This allows traffic to be switched to the backup link.

**Figure 1** Network diagram of BFD for OSPF![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130783290.png)

#### Configuration Precautions

To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security." OSPF area authentication is used as an example. For details, see "Example for Configuring Basic OSPF Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions on each device to ensure routing reachability.
2. Enable BFD globally.
3. Configure BFD for OSPF in the specified process on DeviceA, DeviceB, and DeviceC.

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address to each interface as shown in [Figure 1](#EN-US_TASK_0000001130623436__fig_dc_vrp_ospf_cfg_010201). For configuration details, see configuration scripts.
2. Configure basic OSPF functions.
   
   
   
   For detailed configurations, see the configuration scripts.
3. Configure BFD for OSPF in the specified process.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] bfd all-interfaces enable
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] bfd all-interfaces enable
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bfd
   [*DeviceC-bfd] quit
   [*DeviceC] ospf 1
   [*DeviceC-ospf-1] bfd all-interfaces enable
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Run the **display ospf bfd session all** command on any of DeviceA, DeviceB, or DeviceC. Check whether the **BFDState** field is displayed as **up** in the command output.

The following example uses the command output on DeviceA.

```
[~DeviceA] display ospf bfd session all
          OSPF Process 1 with Router ID 1.1.1.1
  Area 0.0.0.0 interface 1.1.1.1(100GE1/0/1)'s BFD Sessions

 NeighborId:2.2.2.2          AreaId:0.0.0.0          Interface: 100GE1/0/1
 BFDState:up                 rx    :1000             tx       :1000
 Multiplier:3                BFD Local Dis:0         LocalIpAdd:1.1.1.1
 RemoteIpAdd:1.1.1.2         Diagnostic Info:0

  Area 0.0.0.0 interface 3.3.3.1(100GE1/0/2)'s BFD Sessions

 NeighborId:3.3.3.3          AreaId:0.0.0.0          Interface: 100GE1/0/2
 BFDState:up                 rx    :1000             tx       :1000
 Multiplier:3                BFD Local Dis:0         LocalIpAdd:3.3.3.1
 RemoteIpAdd:3.3.3.2         Diagnostic Info:0
```

# Run the [**shutdown**](cmdqueryname=shutdown) command on DeviceB's 100GE1/0/2 to simulate a fault on the primary link.

```
[~DeviceB] interface 100ge 1/0/2
```
```
[~DeviceB-100GE1/0/2] shutdown
```

# Check information about the routing table on DeviceA. The routing path is switched to the backup link DeviceA -> DeviceC -> DeviceB after the primary link fails, and you can see that the next hop address of the route to 172.16.1.0/24 is 1.1.1.2.

```
[~DeviceA] display ospf routing
```
```
          OSPF Process 1 with Router ID 1.1.1.1
                   Routing Tables

 Routing for Network
 Destination        Cost       Type       NextHop         AdvRouter       Area
 2.2.2.0/24         2          Stub       1.1.1.2         3.3.3.3         0.0.0.0
 172.16.1.0/24      3          Stub       1.1.1.2         2.2.2.2         0.0.0.0

 Total Nets: 2
 Intra Area: 2  Inter Area: 0  ASE: 0  NSSA: 0
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  router id 1.1.1.1
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 1.1.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 3.3.3.1 255.255.255.0
  #
  ospf 1
   bfd all-interfaces enable
   area 0.0.0.0
    network 3.3.3.0 0.0.0.255
    network 1.1.1.0 0.0.0.255
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  router id 2.2.2.2
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 2.2.2.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 3.3.3.2 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  ospf 1
   bfd all-interfaces enable
   area 0.0.0.0
    network 3.3.3.0 0.0.0.255
    network 2.2.2.0 0.0.0.255
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  router id 3.3.3.3
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 1.1.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 2.2.2.1 255.255.255.0
  #
  ospf 1
   bfd all-interfaces enable
   area 0.0.0.0
    network 1.1.1.0 0.0.0.255
    network 2.2.2.0 0.0.0.255
  #
  return
  ```