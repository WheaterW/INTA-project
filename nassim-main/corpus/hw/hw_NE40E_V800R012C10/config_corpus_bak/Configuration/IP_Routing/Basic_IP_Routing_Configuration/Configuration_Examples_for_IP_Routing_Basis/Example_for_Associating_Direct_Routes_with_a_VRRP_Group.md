Example for Associating Direct Routes with a VRRP Group
=======================================================

Associating direct routes with a Virtual Router Redundancy Protocol (VRRP) group prevents user-to-network traffic and network-to-user traffic that traverse the VRRP group from being transmitted on different paths.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365385__fig_dc_vrp_ip-route_cfg_003301), the VRRP group consisting of Device1 and Device2 functions as the user-side gateway. User-to-network traffic is forwarded through the master device (Device1) of the VRRP group. In addition, the Open Shortest Path First (OSPF) protocol runs on Device 1, Device 2, and Device 3 so that these devices can communicate with one another at the IP layer. Network-to-user traffic travels on the path that OSPF selects. Device 3 has two equal-cost routes destined for the user network segment 10.1.1.0/24 that OSPF selects. Therefore, the two routes load-balance the network-to-user traffic. User-to-network traffic and network-to-user traffic travel on different paths.

**Figure 1** Association between direct routes and a VRRP group![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_ip-route_cfg_003301.png)

To resolve this problem, associate direct routes with the VRRP group on VRRP-enabled interfaces of Device1 and Device2 to increase the cost of the direct route to the virtual IP network segment of the VRRP group, import the direct route to OSPF, and configure OSPF to inherit the costs of the imported external routes. Because the cost of the OSPF route passing through Device1 is smaller, Device3 preferentially selects this route to forward downstream traffic. In this manner, upstream and downstream traffic is transmitted along the same path.


#### Precautions

During the configuration, pay attention to the following points:

* OSPF cannot run on Device 1's and Device 2's VRRP-enabled interfaces. If both VRRP and OSPF run on Device 1's and Device 2's interfaces, OSPF cannot inherit the costs from the imported direct routes after the association.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VRRP group on Device 1 and Device 2.
2. Configure OSPF on Device 1, Device 2, and Device 3.
3. Associate direct routes with the VRRP group on Device 1 and Device 2.
4. Enable OSPF to import direct routes on Device 1 and Device 2 and to inherit the costs of the imported direct routes.

#### Data Preparation

To complete the configuration, you need the following data:

* VLAN ID 10 configured on the Switch
* VRRP ID 1 and a virtual IP address 10.1.1.111 of the VRRP group
* Device 1's VRRP priority 120
* Cost of direct routes to the virtual IP network segment on Device 2 (300)

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration File](#EN-US_TASK_0172365385__section_dc_vrp_ip-route_cfg_003306) in this section.
2. Configure a VRRP group.
   
   
   
   # Configure a VLAN with VLAN ID 10 on the Switch. Add GE 0/1/0 and GE 0/1/1 to VLAN 10 so that the Switch transparently transmits VRRP packets sent by Device 1 or Device 2.
   
   ```
   <Switch> system-view
   ```
   ```
   [~Switch] interface gigabitethernet 0/1/0
   ```
   ```
   [~Switch-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*Switch-GigabitEthernet0/1/0] commit
   ```
   ```
   [*Switch-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Switch] interface gigabitethernet 0/1/1
   ```
   ```
   [~Switch-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*Switch-GigabitEthernet0/1/1] commit
   ```
   ```
   [~Switch-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Switch] vlan 10
   ```
   ```
   [*Switch-vlan10] port gigabitethernet 0/1/0
   ```
   ```
   [*Switch-vlan10] port gigabitethernet 0/1/1
   ```
   ```
   [*Switch-vlan10] commit
   ```
   ```
   [~Switch-vlan10] quit
   ```
   
   # Create VRRP group 1 on Device 1, and set the priority of Device 1 in the VRRP group to 120 so that Device 1 functions as the master device.
   
   ```
   <Device1> system-view
   ```
   ```
   [~Device1] interface gigabitethernet 0/1/0
   ```
   ```
   [*Device1-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.111
   ```
   ```
   [*Device1-GigabitEthernet0/1/0] vrrp vrid 1 priority 120
   ```
   ```
   [*Device1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~Device1-GigabitEthernet0/1/0] quit
   ```
   
   # Create VRRP group 1 on Device 2
   
   ```
   <Device2> system-view
   ```
   ```
   [~Device2] interface gigabitethernet 0/1/0
   ```
   ```
   [*Device2-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.111
   ```
   ```
   [*Device2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~Device2-GigabitEthernet0/1/0] quit
   ```
3. Configure OSPF.
   
   
   
   # Configure OSPF on Device 1.
   
   ```
   [~Device1] ospf 1
   ```
   ```
   [*Device1-ospf-1] area 0
   ```
   ```
   [*Device1-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255
   ```
   ```
   [*Device1-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~Device1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~Device1-ospf-1] quit
   ```
   
   # Configure OSPF on Device 2.
   
   ```
   [~Device2] ospf 1
   ```
   ```
   [*Device2-ospf-1] area 0
   ```
   ```
   [*Device2-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*Device2-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~Device2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~Device2-ospf-1] quit
   ```
   
   # Configure OSPF on Device 3.
   
   ```
   <Device3> system-view
   ```
   ```
   [~Device3] ospf 1
   ```
   ```
   [*Device3-ospf-1] area 0
   ```
   ```
   [*Device3-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*Device3-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255
   ```
   ```
   [*Device3-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~Device3-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~Device3-ospf-1] quit
   ```
4. Associate direct routes with the VRRP group.
   
   
   
   # Configure Device1.
   
   ```
   [~Device1] interface gigabitethernet 0/1/0
   ```
   ```
   [*Device1-GigabitEthernet0/1/0] direct-route track vrrp vrid 1 degrade-cost 300
   ```
   ```
   [*Device1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~Device1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Device2.
   
   ```
   [~Device2] interface gigabitethernet 0/1/0
   ```
   ```
   [*Device2-GigabitEthernet0/1/0] direct-route track vrrp vrid 1 degrade-cost 300
   ```
   ```
   [*Device2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~Device2-GigabitEthernet0/1/0] quit
   ```
5. Configure OSPF to import direct routes.
   
   
   
   # Configure OSPF on Device 1.
   
   ```
   [~Device1] ospf 1
   ```
   ```
   [*Device1-ospf-1] import-route direct
   ```
   ```
   [*Device1-ospf-1] default cost inherit-metric
   ```
   ```
   [*Device1-ospf-1] commit
   ```
   ```
   [~Device1-ospf-1] quit
   ```
   
   # Configure OSPF on Device 2.
   
   ```
   [~Device2] ospf 1
   ```
   ```
   [*Device2-ospf-1] import-route direct
   ```
   ```
   [*Device2-ospf-1] default cost inherit-metric
   ```
   ```
   [*Device2-ospf-1] commit
   ```
   ```
   [~Device2-ospf-1] quit
   ```
6. Check the configuration.
   
   
   
   # Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on Device2 to view information about the IP routing table. The command output shows that the cost of the direct route to the VRRP virtual IP network segment is 300.
   
   ```
   <Device2> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 12       Routes : 12        
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
        10.1.1.0/24  Direct 0    300           D  10.1.1.2        GigabitEthernet0/1/0
          10.1.1.2/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
        10.1.1.111/32  O_ASE  150  0             D  10.1.2.2        GigabitEthernet0/1/1
        10.1.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
          10.1.2.0/24  Direct 0    0             D  10.1.2.1        GigabitEthernet0/1/1
          10.1.2.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/1
        10.1.2.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/1
          10.1.3.0/24  OSPF   10   2             D  10.1.2.2        GigabitEthernet0/1/1
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   
   # Run the [**display ip routing-table 10.1.1.0**](cmdqueryname=display+ip+routing-table+10.1.1.0) command on Device3 to view information about the route destined for the network segment. The command output shows that Device3 selects the route with next-hop address 10.1.3.1 (passing through VRRP master device Device1) for downstream traffic to the user.
   
   ```
   <Device3> display ip routing-table 10.1.1.0
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
          10.1.1.0/24  O_ASE  150  0             D  10.1.3.1        GigabitEthernet0/1/0
   ```

#### Configuration Files

* Switch configuration file
  
  ```
  #
  sysname Switch
  #
  vlan batch 10
  #               
  interface GigabitEthernet0/1/0
   portswitch     
   undo shutdown  
   port default vlan 10
  #               
  interface GigabitEthernet0/1/1
   portswitch     
   undo shutdown  
   port default vlan 10
  #
  ```
* Device 1 configuration file
  
  ```
  #
  sysname Device1
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 priority 120
   direct-route track vrrp vrid 1 degrade-cost 300
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
  #               
  ospf 1          
   default cost inherit-metric
   import-route direct
   area 0.0.0.0   
    network 10.1.3.0 0.0.0.255
  #
  ```
* Device 2 configuration file
  
  ```
  #
  sysname Device2
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   direct-route track vrrp vrid 1 degrade-cost 300
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
  #               
  ospf 1          
   default cost inherit-metric
   import-route direct
   area 0.0.0.0   
    network 10.1.2.0 0.0.0.255
  #
  ```
* Device 3 configuration file
  
  ```
  #
  sysname Device3
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
  #               
  ospf 1          
   area 0.0.0.0   
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  ```