Example for Configuring OSPF-BGP Synchronization
================================================

Example for Configuring OSPF-BGP Synchronization

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176662993__fig_dc_vrp_ospf_cfg_010301), all devices run BGP, and an EBGP connection is set up between DeviceD and DeviceE. IBGP connections are set up between devices in AS 10, and OSPF is used as the IGP.

OSPF-BGP synchronization is required on DeviceB so that a restart of DeviceB does not interrupt the traffic from DeviceA to AS 20.

**Figure 1** Network diagram of OSPF-BGP synchronization![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130783310.png)

#### Precautions

To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security." OSPF area authentication is used as an example. For details, see "Example for Configuring Basic OSPF Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable OSPF on DeviceA, DeviceB, DeviceC, and DeviceD (except the interface 10.2.1.1/30), and specify the same area for the network segments where the OSPF interfaces reside.
2. Set up IBGP connections between DeviceA, DeviceB, DeviceC, and DeviceD (except the interface 10.2.1.1/30).
3. Set the OSPF cost on DeviceC.
4. Configure an EBGP connection between DeviceD and DeviceE.
5. Configure BGP to import direct routes and routes from the OSPF process on DeviceD.
6. Configure BGP on DeviceE.

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address to each interface as shown in [Figure 1](#EN-US_TASK_0000001176662993__fig_dc_vrp_ospf_cfg_010301). For configuration details, see configuration scripts.
2. Configure basic OSPF functions.
   
   
   
   For detailed configurations, see the configuration scripts.
3. Configure IBGP full-mesh connections.
   
   
   
   # Configure DeviceA.
   
   ```
   <DeviceA> system-view
   [~DeviceA] interface loopback 0
   [*DeviceA-LoopBack0] ip address 10.10.1.1 32
   [*DeviceA-LoopBack0] quit
   [*DeviceA] bgp 10
   [*DeviceA-bgp] router-id 10.10.1.1
   [*DeviceA-bgp] peer 10.10.2.2 as-number 10
   [*DeviceA-bgp] peer 10.10.2.2 connect-interface LoopBack 0
   [*DeviceA-bgp] peer 10.10.3.3 as-number 10
   [*DeviceA-bgp] peer 10.10.3.3 connect-interface LoopBack 0
   [*DeviceA-bgp] peer 10.10.4.4 as-number 10
   [*DeviceA-bgp] peer 10.10.4.4 connect-interface LoopBack 0
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <DeviceB> system-view
   [~DeviceB] interface loopback 0
   [*DeviceB-LoopBack0] ip address 10.10.2.2 32
   [*DeviceB-LoopBack0] quit
   [*DeviceB] bgp 10
   [*DeviceB-bgp] router-id 10.10.2.2
   [*DeviceB-bgp] peer 10.10.1.1 as-number 10
   [*DeviceB-bgp] peer 10.10.1.1 connect-interface LoopBack 0
   [*DeviceB-bgp] peer 10.10.3.3 as-number 10
   [*DeviceB-bgp] peer 10.10.3.3 connect-interface LoopBack 0
   [*DeviceB-bgp] peer 10.10.4.4 as-number 10
   [*DeviceB-bgp] peer 10.10.4.4 connect-interface LoopBack 0
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <DeviceC> system-view
   [~DeviceC] interface loopback 0
   [*DeviceC-LoopBack0] ip address 10.10.3.3 32
   [*DeviceC-LoopBack0] quit
   [*DeviceC] bgp 10
   [*DeviceC-bgp] router-id 10.10.3.3
   [*DeviceC-bgp] peer 10.10.1.1 as-number 10
   [*DeviceC-bgp] peer 10.10.1.1 connect-interface LoopBack 0
   [*DeviceC-bgp] peer 10.10.2.2 as-number 10
   [*DeviceC-bgp] peer 10.10.2.2 connect-interface LoopBack 0
   [*DeviceC-bgp] peer 10.10.4.4 as-number 10
   [*DeviceC-bgp] peer 10.10.4.4 connect-interface LoopBack 0
   [*DeviceC-bgp] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   <DeviceD> system-view
   [~DeviceD] interface loopback 0
   [*DeviceD-LoopBack0] ip address 10.10.4.4 32
   [*DeviceD-LoopBack0] quit
   [*DeviceD] bgp 10
   [*DeviceD-bgp] router-id 10.10.4.4
   [*DeviceD-bgp] peer 10.10.1.1 as-number 10
   [*DeviceD-bgp] peer 10.10.1.1 connect-interface LoopBack 0
   [*DeviceD-bgp] peer 10.10.2.2 as-number 10
   [*DeviceD-bgp] peer 10.10.2.2 connect-interface LoopBack 0
   [*DeviceD-bgp] peer 10.10.3.3 as-number 10
   [*DeviceD-bgp] peer 10.10.3.3 connect-interface LoopBack 0
   [*DeviceD-bgp] quit
   [*DeviceD] commit
   ```
4. Configure an EBGP connection.
   
   
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 10
   [~DeviceD-bgp] peer 10.2.1.2 as-number 20
   [*DeviceD-bgp] import-route direct
   [*DeviceD-bgp] import-route ospf 1
   [*DeviceD-bgp] quit
   [*DeviceD] commit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] bgp 20
   [*DeviceE-bgp] peer 10.2.1.1 as-number 10
   [*DeviceE-bgp] ipv4-family unicast
   [*DeviceE-bgp-af-ipv4] network 10.3.1.0 30
   [*DeviceE-bgp-af-ipv4] quit
   [*DeviceE-bgp] quit
   [*DeviceE] commit
   ```
5. Set the OSPF cost on DeviceC.
   
   
   ```
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] ospf cost 2
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] ospf cost 2
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   After the OSPF cost is set to 2 on DeviceC, DeviceA selects only DeviceB as the intermediate device to the network segment 10.2.1.0, and DeviceC becomes a backup of DeviceB.
   
   # Check information about the routing table on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relied, D - download to fib
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 20       Routes : 20
   
       Destination/Mask       Proto    Pre  Cost    Flags NextHop         Interface
   
           10.10.1.1/32         Direct   0    0       D     127.0.0.1       InLoopBack0
           10.10.1.255/32       Direct   0    0       D     127.0.0.1       InLoopBack0
           10.10.2.2/32         OSPF     10   3       D     10.1.1.2        100GE1/0/1
           10.4.4.0/24         BGP      255  0       RD    10.10.4.4         100GE1/0/1
           10.10.4.4/32         OSPF     10   3       D     10.1.1.2        100GE1/0/1
           10.5.5.0/24         BGP      255  0       RD    10.2.1.2        100GE1/0/1
          10.1.1.0/30         Direct   0    0       D     10.1.1.1        100GE1/0/1
          10.1.1.3/32         Direct   0    0       D     10.1.1.1        100GE1/0/1
          10.1.1.1/32         Direct   0    0       D     127.0.0.1       InLoopBack0
          10.1.1.255/32       Direct   0    0       D     127.0.0.1       InLoopBack0
          10.1.1.255/32       Direct   0    0       D     10.1.1.2        100GE1/0/1
          10.1.1.2/32         Direct   0    0       D     10.1.1.2        100GE1/0/1
          10.1.1.255/32       Direct   0    0       D     10.1.1.2        100GE1/0/1
          10.1.2.0/30         Direct   0    0       D     10.1.2.1        100GE1/0/2
          10.1.2.3/32         Direct   0    0       D     10.1.2.1        100GE1/0/2
          10.1.2.1/32         Direct   0    0       D     127.0.0.1       InLoopBack0
          10.1.2.255/32       Direct   0    0       D     127.0.0.1       InLoopBack0
          10.1.2.2/32         Direct   0    0       D     10.1.2.2        100GE1/0/2
          10.1.2.255/32       Direct   0    0       D     10.1.2.2        100GE1/0/2
         127.0.0.0/8          Direct   0    0       D     127.0.0.1       InLoopBack0
         127.0.0.1/32         Direct   0    0       D     127.0.0.1       InLoopBack0
         127.0.0.255/32       Direct   0    0       D     127.0.0.1       InLoopBack0
       10.3.1.0/30       OSPF    10   2       D     10.1.1.2        100GE1/0/1
          10.1.3.1/32         BGP      255  0       RD    10.10.4.4         100GE1/0/1
          10.1.4.0/30         OSPF     10   3       D     10.1.1.2        100GE1/0/1
                              OSPF     10   3       D     10.1.2.2        100GE1/0/2
          10.1.4.1/32         BGP      255  0       RD    10.10.4.4         100GE1/0/1
          10.2.1.0/30         BGP      255  0       RD    10.10.4.4         100GE1/0/1
          10.2.1.2/32         BGP      255  0       RD    10.10.4.4         100GE1/0/1
          10.3.1.0/30         BGP      255  0       RD    10.10.4.4         100GE1/0/1
          255.255.255.255/32  Direct   0    0       D     127.0.0.1       InLoopBack0
   ```
   
   The command output shows that BGP has learned the route to 10.3.1.0, with the outbound interface being 100GE1/0/1.
   
   # Check information about the routing table on DeviceB.
   
   ```
   [~DeviceB] display ip routing-table
   ```
   ```
   Route Flags: R - relied, D - download to fib
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 19       Routes : 19
   
       Destination/Mask       Proto    Pre  Cost      Flags NextHop         Interface
   
           10.10.2.2/32         Direct   0    0           D   127.0.0.1        InLoopBack0
           10.10.2.255/32       Direct   0    0           D   127.0.0.1        InLoopBack0
           10.10.1.1/32         OSPF     10   2           D   10.1.1.1         100GE1/0/1
           10.4.4.0/24         BGP      255  0           RD  10.1.3.2         100GE1/0/2
           10.10.4.4/32         OSPF     10   2           D   10.1.3.2         100GE1/0/2
           10.5.5.0/24         BGP      255  0           RD  10.2.1.2         100GE1/0/2
          10.1.1.0/30         Direct   0    0           D   10.1.1.2         100GE1/0/1
          10.1.1.3/32         Direct   0    0           D   10.1.1.2         100GE1/0/1
          10.1.1.1/32         Direct   0    0           D   10.1.1.1         100GE1/0/1
          10.1.1.255/32       Direct   0    0           D   10.1.1.1         100GE1/0/1
          10.1.1.2/32         Direct   0    0           D   127.0.0.1        InLoopBack0
          10.1.1.255/32       Direct   0    0           D   127.0.0.1        InLoopBack0
          10.1.2.0/30         OSPF     10   2           D   10.1.1.1         100GE1/0/1
          10.1.3.0/30         Direct   0    0           D   10.1.3.1         100GE1/0/2
          10.1.3.3/32         Direct   0    0           D   10.1.3.1         100GE1/0/2
          10.1.3.1/32         Direct   0    0           D   127.0.0.1        InLoopBack0
          10.1.3.255/32       Direct   0    0           D   127.0.0.1        InLoopBack0
          10.1.3.2/32         Direct   0    0           D   10.1.3.2         100GE1/0/2
          10.1.3.255/32       Direct   0    0           D   10.1.3.2         100GE1/0/2
         127.0.0.0/8          Direct   0    0           D   127.0.0.1        InLoopBack0
         127.0.0.1/32         Direct   0    0           D   127.0.0.1        InLoopBack0
         127.0.0.255/32       Direct   0    0           D   127.0.0.1        InLoopBack0
          10.1.4.0/30         OSPF     10   2           D   10.1.3.2         100GE1/0/2
          10.1.4.1/32         BGP      255  0           RD  10.1.3.2         100GE1/0/2
          10.2.1.0/30         BGP      255  0           RD  10.1.3.2         100GE1/0/2
          10.2.1.2/32         BGP      255  0           RD  10.1.3.2         100GE1/0/2
        10.3.1.0/30      BGP    255  0           RD  10.1.3.2         100GE1/0/2
          255.255.255.255/32  Direct   0    0           D     127.0.0.1       InLoopBack0
   ```
   
   The command output shows that DeviceB has learned the route to 10.3.1.0 through BGP, with the outbound interface being 100GE1/0/2. OSPF has learned the routes to 10.1.2.0 and 10.1.4.0, and the costs are both 2.
6. Enable OSPF-BGP synchronization on DeviceB.
   
   
   ```
   [~DeviceB] ospf 1
   [*DeviceB-ospf-1] stub-router on-startup
   [*DeviceB-ospf-1] [safe-sync enable](cmdqueryname=safe-sync+enable)
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Restart DeviceB.

![](../public_sys-resources/note_3.0-en-us.png) 

Here, the device is restarted based on the assumption that the device is faulty. In normal cases, do not run the **reboot** command because it may lead to a temporary network outage. In addition, check that the configuration script of the device has been saved before you restart the device.

```
[~DeviceB] reboot
System will reboot! Continue?[Y/N] y
```

# Check information about the routing table on DeviceA.

```
[~DeviceA] display ip routing-table
```
```
Route Flags: R - relied, D - download to fib
------------------------------------------------------------------------------
Routing Table: _public_
         Destinations : 20       Routes : 20

Destination/Mask    Proto  Pre  Cost      Flags NextHop         Interface

        10.10.1.1/32  Direct 0    0           D   127.0.0.1        InLoopBack0
        10.10.2.2/32  OSPF   10   4           D   10.1.2.2         100GE1/0/2
        10.4.4.0/24  BGP    255  0           RD  10.10.4.4          100GE1/0/2
        10.10.4.4/32  OSPF   10   4           D   10.1.2.2         100GE1/0/2
        10.5.5.0/24  BGP    255  0           RD  10.2.1.2         100GE1/0/2
       10.1.1.0/30  Direct 0    0           D   10.1.1.1         100GE1/0/1
       10.1.1.1/32  Direct 0    0           D   127.0.0.1        InLoopBack0
       10.1.1.2/32  Direct 0    0           D   10.1.1.2         100GE1/0/1
       10.1.2.0/30  Direct 0    0           D   10.1.2.1         100GE1/0/2
       10.1.2.1/32  Direct 0    0           D   127.0.0.1        InLoopBack0
       10.1.2.2/32  Direct 0    0           D   10.1.2.2         100GE1/0/2
      127.0.0.0/8   Direct 0    0           D   127.0.0.1        InLoopBack0
      127.0.0.1/32  Direct 0    0           D   127.0.0.1        InLoopBack0
       10.1.3.0/30  OSPF   10   2           D   10.1.1.2         100GE1/0/1
       10.1.3.1/32  BGP    255  0           RD  10.10.4.4          100GE1/0/2
       10.1.4.0/30  OSPF   10   3           D   10.1.2.2         100GE1/0/2
       10.1.4.1/32  BGP    255  0           RD  10.10.4.4          100GE1/0/2
       10.2.1.0/30  BGP    255  0           RD  10.10.4.4          100GE1/0/2
       10.2.1.2/32  BGP    255  0           RD  10.10.4.4          100GE1/0/2
      10.3.1.0/30   BGP    255  0           RD  10.10.4.4          100GE1/0/2
```

The command output shows that BGP has learned the route to 10.3.1.0 and the outbound interface is changed to 100GE1/0/2.

# Check information about the routing table on DeviceB.

```
[~DeviceB] display ip routing-table
```
```
Route Flags: R - relied, D - download to fib
------------------------------------------------------------------------------
Routing Table: _public_
         Destinations : 15       Routes : 15

Destination/Mask    Proto  Pre  Cost      Flags NextHop        Interface

        10.10.1.1/32  OSPF   10   65536       D  10.1.1.1        100GE1/0/1
        10.10.2.2/32  Direct 0    0           D  127.0.0.1       InLoopBack0
        10.10.4.4/32  OSPF   10   65536       D  10.1.3.2        100GE1/0/2
       10.1.1.0/30  Direct 0    0           D  10.1.1.2        100GE1/0/1
       10.1.1.1/32  Direct 0    0           D  10.1.1.1        100GE1/0/1
       10.1.1.2/32  Direct 0    0           D  127.0.0.1       InLoopBack0
       10.1.2.0/30  OSPF   10   65536       D  10.1.1.1        100GE1/0/1
       10.1.3.0/30  Direct 0    0           D  10.1.3.1        100GE1/0/2
       10.1.3.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
       10.1.3.2/32  Direct 0    0           D  10.1.3.2        100GE1/0/2
      127.0.0.0/8   Direct 0    0           D   127.0.0.1      InLoopBack0
      127.0.0.1/32  Direct 0    0           D   127.0.0.1      InLoopBack0
       10.1.4.0/30  OSPF   10   65536       D  10.1.3.2        100GE1/0/2
      127.0.0.0/8   Direct 0    0           D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
```

The command output shows that only the OSPF routes exist in the routing table and their costs are greater than 65535. This is because IGP routes converge faster than BGP routes.

# Check information about the routing table on DeviceB again.

```
[~DeviceB] display ip routing-table
```
```
Route Flags: R - relied, D - download to fib
------------------------------------------------------------------------------
Routing Table: _public_
         Destinations : 19       Routes : 19

Destination/Mask    Proto  Pre  Cost       Flags NextHop       Interface

        10.10.2.2/32  Direct 0    0           D    127.0.0.1        InLoopBack0
        10.10.1.1/32  OSPF   10   2           D    10.1.1.1         100GE1/0/1
        10.4.4.0/24  BGP    255  0           RD   10.1.3.2         100GE1/0/2
        10.10.4.4/32  OSPF   10   2           D    10.1.3.2         100GE1/0/2
        10.5.5.0/24  BGP    255  0           RD   10.2.1.2         100GE1/0/2
       10.1.1.0/30  Direct 0    0           D    10.1.1.2         100GE1/0/1
       10.1.1.1/32  Direct 0    0           D    10.1.1.1         100GE1/0/1
       10.1.1.2/32  Direct 0    0           D    127.0.0.1        InLoopBack0
       10.1.2.0/30  OSPF   10   2           D    10.1.1.1         100GE1/0/1
       10.1.3.0/30  Direct 0    0           D    10.1.3.1         100GE1/0/2
       10.1.3.1/32  Direct 0    0           D    127.0.0.1        InLoopBack0
       10.1.3.2/32  Direct 0    0           D    10.1.3.2         100GE1/0/2
      127.0.0.0/8   Direct 0    0           D    127.0.0.1        InLoopBack0
      127.0.0.1/32  Direct 0    0           D    127.0.0.1        InLoopBack0
       10.1.4.0/30  OSPF   10   2           D    10.1.3.2         100GE1/0/2
       10.1.4.1/32  BGP    255  0           RD   10.1.3.2         100GE1/0/2
       10.2.1.0/30  BGP    255  0           RD   10.1.3.2         100GE1/0/2
       10.2.1.2/32  BGP    255  0           RD   10.1.3.2         100GE1/0/2
       10.3.1.0/30  BGP    255  0           RD   10.1.3.2         100GE1/0/2
```

The command output shows that the routing information is restored (to that prior to device restart) after BGP routes converge on DeviceB.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  router id 10.10.1.1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.252
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.252
  #
  interface LoopBack0
   ip address 10.10.1.1 255.255.255.255
  #
  bgp 10
   router-id 10.10.1.1
   peer 10.10.2.2 as-number 10
   peer 10.10.2.2 connect-interface LoopBack 0
   peer 10.10.3.3 as-number 10
   peer 10.10.3.3 connect-interface LoopBack 0
   peer 10.10.4.4 as-number 10
   peer 10.10.4.4 connect-interface LoopBack 0
  #
  ospf 1
   area 0.0.0.0
    network 10.10.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.3
    network 10.1.2.0 0.0.0.3
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  router id 10.10.2.2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.252
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.1 255.255.255.252
  #
  interface LoopBack0
   ip address 10.10.2.2 255.255.255.255
  #
  bgp 10
   router-id 10.10.2.2
   peer 10.10.1.1 as-number 10
   peer 10.10.1.1 connect-interface LoopBack 0
   peer 10.10.3.3 as-number 10
   peer 10.10.3.3 connect-interface LoopBack 0
   peer 10.10.4.4 as-number 10
   peer 10.10.4.4 connect-interface LoopBack 0
  #
  ospf 1
   stub-router on-startup
   area 0.0.0.0
    network 10.1.1.0 0.0.0.3
    network 10.1.3.0 0.0.0.3
    network 10.10.2.2 0.0.0.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  router id 10.10.3.3
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.4.1 255.255.255.252
   ospf cost 2
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.2 255.255.255.252
   ospf cost 2
  #
  interface LoopBack0
   ip address 10.10.3.3 255.255.255.255
  #
  bgp 10
   router-id 10.10.3.3
   peer 10.10.1.1 as-number 10
   peer 10.10.1.1 connect-interface LoopBack 0
   peer 10.10.2.2 as-number 10
   peer 10.10.2.2 connect-interface LoopBack 0
   peer 10.10.4.4 as-number 10
   peer 10.10.4.4 connect-interface LoopBack 0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.2.0 0.0.0.3
    network 10.1.4.0 0.0.0.3
    network 10.10.3.3 0.0.0.0
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  router id 10.10.4.4
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.4.2 255.255.255.252
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.2 255.255.255.252
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.2.1.1 255.255.255.252
  #
  interface LoopBack0
   ip address 10.10.4.4 255.255.255.255
  #
  bgp 10
   router-id 10.10.4.4
   peer 10.2.1.2 as-number 20
   peer 10.10.1.1 as-number 10
   peer 10.10.1.1 connect-interface LoopBack 0
   peer 10.10.2.2 as-number 10
   peer 10.10.2.2 connect-interface LoopBack 0
   peer 10.10.3.3 as-number 10
   peer 10.10.3.3 connect-interface LoopBack 0
   #
   ipv4-family unicast
    import-route direct
    import-route ospf 1
    peer 10.2.1.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.10.4.4 0.0.0.0
    network 10.1.3.0 0.0.0.3
    network 10.1.4.0 0.0.0.3
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  router id 10.5.5.5
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.2.1.2 255.255.255.252
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.3.1.1 255.255.255.252
  #
  interface LoopBack0
   ip address 10.5.5.5 255.255.255.255
  #
  bgp 20
   router-id 10.5.5.5
   peer 10.2.1.1 as-number 10
   #
   ipv4-family unicast
    network 10.3.1.0 255.255.255.252
    peer 10.2.1.1 enable
  #
  return
  ```