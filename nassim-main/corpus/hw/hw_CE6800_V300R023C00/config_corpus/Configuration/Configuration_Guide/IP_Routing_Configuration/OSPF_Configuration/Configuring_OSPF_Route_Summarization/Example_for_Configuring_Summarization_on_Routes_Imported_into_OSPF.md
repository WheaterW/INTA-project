Example for Configuring Summarization on Routes Imported into OSPF
==================================================================

Example for Configuring Summarization on Routes Imported into OSPF

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001586805721__fig_dc_vrp_ospf_cfg_009401), DeviceA, DeviceB, and DeviceC run OSPF to communicate with each other. DeviceA runs in area 0, and DeviceC runs in area 1. DeviceB is an ABR and runs in both areas. DeviceA is an ASBR. DeviceA is configured to summarize the imported direct routes and advertise the summary routes to other devices in the area. This reduces the number of routing entries on DeviceA.

**Figure 1** Networking diagram of configuring summarization on routes imported into OSPF![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001535886170.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable OSPF on each device and configure basic OSPF functions to ensure that the devices can communicate with each other using OSPF.
2. Configure OSPF route summarization.

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 192.168.0.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 192.168.2.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 192.168.3.1 24
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface loopback0
   [*DeviceA-loopback0] ip address 1.1.1.1 32
   [*DeviceA-loopback0] quit
   [*DeviceA] commit
   ```
   
   
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Configure basic OSPF functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] router id 1.1.1.1
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.0.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] router id 2.2.2.2
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.0.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] area 1
   [*DeviceB-ospf-1-area-0.0.0.1] network 192.168.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.1] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] router id 3.3.3.3
   [*DeviceC] ospf 1
   [*DeviceC-ospf-1] area 1
   [*DeviceC-ospf-1-area-0.0.0.1] network 192.168.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.1] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
3. Configure the ASBR to summarize imported routes.
   
   
   ```
   [~DeviceA] ospf 1
   [*DeviceA-ospf-1] import-route direct
   [*DeviceA-ospf-1] asbr-summary 192.168.2.0 255.255.254.0
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the routing table of DeviceC.

```
[~DeviceC] display ip routing-table
Proto: Protocol        Pre: Preference
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 11        Routes : 11         

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

        1.1.1.1/32  O_ASE   150  1             D   192.168.1.2     100GE1/0/1
        3.3.3.3/32  Direct  0    0             D   127.0.0.1       LoopBack0
      127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0
127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    192.168.0.0/24  OSPF    10   2             D   192.168.1.2     100GE1/0/1
    192.168.1.0/24  Direct  0    0             D   192.168.1.1     100GE1/0/1
    192.168.1.1/32  Direct  0    0             D   127.0.0.1       100GE1/0/1
  192.168.1.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/1
    192.168.2.0/23 O_ASE   150  2              D   192.168.1.2     100GE1/0/1
255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
```

The command output shows information about the summary route to 192.168.2.0/23 advertised by DeviceA.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  router id 1.1.1.1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.0.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 1
   asbr-summary 192.168.2.0 255.255.254.0
   import-route direct
   area 0.0.0.0
    network 192.168.0.0 0.0.0.255
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
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.0.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 192.168.0.0 0.0.0.255
   area 0.0.0.1
    network 192.168.1.0 0.0.0.255
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
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1
   area 0.0.0.1
    network 192.168.1.0 0.0.0.255
  #
  return
  ```