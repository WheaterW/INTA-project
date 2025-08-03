Example for Associating Direct Routes with a VRRP Group
=======================================================

Example for Associating Direct Routes with a VRRP Group

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130782560__fig_dc_vrp_ip-route_cfg_003301), DeviceA and DeviceB form a VRRP group and function as user-side gateways. User traffic is sent to DeviceA, which is the master device in the VRRP group. In addition, DeviceA, DeviceB, and DeviceC run OSPF to implement IP interworking. Network-to-user traffic passes through the path that OSPF selects. DeviceC has two OSPF equal-cost routes destined for the user network segment 10.1.1.0/24. Therefore, the two routes load-balance the network-to-user traffic. User-to-network traffic and network-to-user traffic pass through different paths. To resolve the path inconsistency, configure a VRRP interface on each of DeviceA and DeviceB to associate the VRRP status with the direct route destined for the network segment to which the virtual IP address belongs. The association allows DeviceB to increase the direct route cost. Configure OSPF to import direct routes and inherit the costs of the imported direct routes. As the cost of the OSPF route that passes through DeviceA is smaller, DeviceC selects this route to forward downstream traffic. In this manner, upstream and downstream traffic is transmitted along the same path.

To complete the configuration, you need the following data:

* Virtual local area network (VLAN) ID on Switch: 10
* VRRP group's VRID: 1; virtual IP address: 10.1.1.111
* VRRP priority values of DeviceA and DeviceB: 120 and 100 (default), respectively
* Cost of a direct route to the network segment to which the VRRP virtual IP address belongs: 300

**Figure 1** Association between direct routes and a VRRP group![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001176662339.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each device.
2. Configure a VRRP group on DeviceA and DeviceB.
3. Configure OSPF on DeviceA, DeviceB, and DeviceC to implement IP interworking.
4. Associate direct routes with the VRRP group on DeviceA and DeviceB.
5. Configure OSPF on DeviceA and DeviceB to import direct routes and configure the two devices to inherit the costs of the direct routes.

#### Procedure

1. Configure IPv4 addresses for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.3.1 255.255.255.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Configure a VRRP group.
   
   
   
   # Create VLAN 10 on the Switch and add 100GE 1/0/1 and 100GE 1/0/2 to VLAN 10 so that the Switch can transparently transmit VRRP packets from DeviceA and DeviceB.
   
   
   
   ```
   <~Switch> system-view
   [*Switch] interface 100ge 1/0/1
   [*Switch-100GE1/0/1] portswitch
   [*Switch-100GE1/0/1] quit
   [*Switch] interface 100ge 1/0/2
   [*Switch-100GE1/0/2] portswitch
   [*Switch-100GE1/0/2] quit
   [*Switch] vlan 10
   [*Switch-vlan10] port 100ge 1/0/1
   [*Switch-vlan10] port 100ge 1/0/2
   [*Switch-vlan10] quit
   [*Switch] commit
   ```
   
   # Create VRRP group 1 on DeviceA and set the priority value of DeviceA in the VRRP group to 120 so that DeviceA functions as the master device.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceA-100GE1/0/1] vrrp vrid 1 priority 120
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Create VRRP group 1 on DeviceB and retain the default priority 100 for DeviceB so that DeviceB functions as the backup device.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
3. Configure OSPF. 
   
   
   
   # Configure OSPF on DeviceA.
   
   ```
   [~DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure OSPF on DeviceB.
   
   ```
   [~DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure OSPF on DeviceC.
   
   ```
   [~DeviceC] ospf 1
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
4. Associate direct routes with the VRRP group.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] direct-route track vrrp vrid 1 degrade-cost 300
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] direct-route track vrrp vrid 1 degrade-cost 300
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
5. Configure OSPF to import direct routes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   [*DeviceA-ospf-1] import-route direct
   [*DeviceA-ospf-1] default cost inherit-metric
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf 1
   [*DeviceB-ospf-1] import-route direct
   [*DeviceB-ospf-1] default cost inherit-metric
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on DeviceB to check the IP routing table.

```
[~DeviceB] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
Destinations : 12       Routes : 12

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

10.1.1.0/24       Direct 0    300         D  10.1.1.2      100GE1/0/1
10.1.1.2/32         Direct  0     0             D  127.0.0.1       100GE1/0/1
10.1.1.111/32       O_ASE   150   0             D  10.1.2.2       100GE1/0/2
10.1.1.255/32       Direct  0     0             D  127.0.0.1       100GE1/0/1
10.1.2.0/24         Direct  0     0             D  10.1.2.1        100GE1/0/2
10.1.2.1/32         Direct  0     0             D  127.0.0.1       100GE1/0/2
10.1.2.255/32       Direct  0     0             D  127.0.0.1       100GE1/0/2
10.1.3.0/24         OSPF   10     2             D  10.1.2.2        100GE1/0/2
127.0.0.0/8         Direct  0     0             D  127.0.0.1       InLoopBack0
127.0.0.1/32        Direct  0     0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct  0     0             D  127.0.0.1       InLoopBack0
255.255.255.255/32  Direct  0     0             D  127.0.0.1       InLoopBack0
```

The command output shows that the cost of the direct route to the network segment to which the VRRP virtual IP address belongs is set to 300.

# Run the [**display ip routing-table 10.1.1.0**](cmdqueryname=display+ip+routing-table+10.1.1.0) command on DeviceC to check the routes to the network segment where users reside.

```
[~DeviceC] display ip routing-table 10.1.1.0
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
Summary Count : 1

Destination/Mask    Proto  Pre  Cost    Flags NextHop         Interface

10.1.1.0/24         O_ASE  150    0      D    10.1.3.1      100GE1/0/1
```

The command output shows that DeviceC selects the route with the next-hop IP address of 10.1.3.1 for the network-to-user traffic so that traffic passes through DeviceA, the master device in the VRRP group.


#### Configuration Scripts

* Switch
  
  ```
  #
  sysname Switch
  #
  vlan batch 10
  #               
  interface 100GE1/0/1
   port default vlan 10
  #               
  interface 100GE1/0/2
   port default vlan 10
  #
  ```
* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 priority 120
   direct-route track vrrp vrid 1 degrade-cost 300
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
  #               
  ospf 1          
   default cost inherit-metric
   import-route direct
   area 0.0.0.0   
    network 10.1.3.0 0.0.0.255
  #
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   direct-route track vrrp vrid 1 degrade-cost 300
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #               
  ospf 1          
   default cost inherit-metric
   import-route direct
   area 0.0.0.0   
    network 10.1.2.0 0.0.0.255
  #
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
  #               
  ospf 1          
   area 0.0.0.0   
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  ```