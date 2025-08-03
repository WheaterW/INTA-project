Example for Configuring OSPF-BGP Synchronization
================================================

This section describes how to configure OSPF-BGP synchronization to minimize the impact of Router restart on BGP services on the network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365674__fig_dc_vrp_ospf_cfg_010301), all Routers run BGP. An EBGP connection is set up between DeviceD and DeviceE. IBGP connections are set up between devices in AS 10, and OSPF is used as an IGP protocol.

OSPF-BGP synchronization is required on DeviceB so that the restart of DeviceB does not interrupt the traffic from DeviceA to AS 20.

**Figure 1** Networking for configuring OSPF-BGP synchronization![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_ospf_cfg_010301.png)  


#### Precautions

To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security". OSPF area authentication is used as an example. For details, see Example for Configuring Basic OSPF Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable OSPF on DeviceA, DeviceB, DeviceC, and DeviceD (except 10.2.1.1/30) and specify the same area for all OSPF interfaces.
2. Set up IBGP connections between DeviceA, DeviceB, DeviceC, and DeviceD (except 10.2.1.1/30).
3. Configure the OSPF cost on DeviceC.
4. Set up EBGP connections between DeviceD and DeviceE.
5. Configure BGP to import direct routes and OSPF processes on DeviceD.
6. Configure BGP on DeviceE.

#### Data Preparation

To complete the configuration, you need the following data:

* Data of DeviceA, including the router ID (1.1.1.1), number of the AS to which DeviceA belongs (10), OSPF process ID (1), network segment addresses of area 0 (10.1.1.0/30 and 10.1.2.0/30), and loopback0 IP address (1.1.1.1/32)
* Data of DeviceB, including the router ID (2.2.2.2), number of the AS to which DeviceB belongs (10), OSPF process ID (1), network segment addresses of area 0 (10.1.1.0/30 and 10.1.3.0/30), and loopback0 IP address (2.2.2.2/32)
* Data of DeviceC, including the router ID (3.3.3.3), number of the AS to which DeviceC belongs (10), OSPF process ID (1), network segment addresses of area 0 (10.1.2.0/30 and 10.1.4.0/30), and loopback0 IP address (3.3.3.3/32)
* Data of DeviceD, including the router ID (4.4.4.4), number of the AS to which DeviceD belongs (10), OSPF process ID (1), network segment addresses of area 0 (10.1.3.0/30 and 10.1.4.0/30), and loopback0 IP address (4.4.4.4/32)
* Data of DeviceE, including the router ID (5.5.5.5), number of the AS to which DeviceE belongs (20), and loopback0 IP address (5.5.5.5/32)

#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365674__section_dc_vrp_ospf_cfg_010306) in this section.
2. Configure basic OSPF functions. For details, see [Example for Configuring Basic OSPF Functions](dc_vrp_ospf_cfg_0094.html).
3. Set up IBGP connections.
   
   
   
   # Configure DeviceA.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface loopback 0
   ```
   ```
   [~DeviceA-LoopBack0] ip address 1.1.1.1 32
   ```
   ```
   [*DeviceA-LoopBack0] quit
   ```
   ```
   [*DeviceA] bgp 10
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 2.2.2.2 as-number 10
   [*DeviceA-bgp] peer 2.2.2.2 connect-interface LoopBack 0
   [*DeviceA-bgp] peer 3.3.3.3 as-number 10
   [*DeviceA-bgp] peer 3.3.3.3 connect-interface LoopBack 0
   [*DeviceA-bgp] peer 4.4.4.4 as-number 10
   [*DeviceA-bgp] peer 4.4.4.4 connect-interface LoopBack 0
   ```
   ```
   [*DeviceA-bgp] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface loopback 0
   ```
   ```
   [~DeviceB-LoopBack0] ip address 2.2.2.2 32
   ```
   ```
   [*DeviceB-LoopBack0] quit
   ```
   ```
   [*DeviceB] bgp 10
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 1.1.1.1 as-number 10
   [*DeviceB-bgp] peer 1.1.1.1 connect-interface LoopBack 0
   [*DeviceB-bgp] peer 3.3.3.3 as-number 10
   [*DeviceB-bgp] peer 3.3.3.3 connect-interface LoopBack 0
   [*DeviceB-bgp] peer 4.4.4.4 as-number 10
   [*DeviceB-bgp] peer 4.4.4.4 connect-interface LoopBack 0
   ```
   ```
   [*DeviceB-bgp] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] interface loopback 0
   ```
   ```
   [~DeviceC-LoopBack0] ip address 3.3.3.3 32
   ```
   ```
   [*DeviceC-LoopBack0] quit
   ```
   ```
   [*DeviceC] bgp 10
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-bgp] peer 1.1.1.1 as-number 10
   [*DeviceC-bgp] peer 1.1.1.1 connect-interface LoopBack 0
   [*DeviceC-bgp] peer 2.2.2.2 as-number 10
   [*DeviceC-bgp] peer 2.2.2.2 connect-interface LoopBack 0
   [*DeviceC-bgp] peer 4.4.4.4 as-number 10
   [*DeviceC-bgp] peer 4.4.4.4 connect-interface LoopBack 0
   ```
   ```
   [*DeviceC-bgp] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   <DeviceD> system-view
   ```
   ```
   [~DeviceD] interface loopback 0
   ```
   ```
   [~DeviceD-LoopBack0] ip address 4.4.4.4 32
   ```
   ```
   [*DeviceD-LoopBack0] quit
   ```
   ```
   [*DeviceD] bgp 10
   ```
   ```
   [*DeviceD-bgp] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-bgp] peer 1.1.1.1 as-number 10
   [*DeviceD-bgp] peer 1.1.1.1 connect-interface LoopBack 0
   [*DeviceD-bgp] peer 2.2.2.2 as-number 10
   [*DeviceD-bgp] peer 2.2.2.2 connect-interface LoopBack 0
   [*DeviceD-bgp] peer 3.3.3.3 as-number 10
   [*DeviceD-bgp] peer 3.3.3.3 connect-interface LoopBack 0
   ```
   ```
   [*DeviceD-bgp] quit
   ```
   ```
   [*DeviceD] commit
   ```
4. Set up EBGP connections.
   
   
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 10
   ```
   ```
   [*DeviceD-bgp] peer 10.2.1.2 as-number 20
   ```
   ```
   [*DeviceD-bgp] import-route direct
   ```
   ```
   [*DeviceD-bgp] import-route ospf 1
   ```
   ```
   [*DeviceD-bgp] quit
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] bgp 20
   ```
   ```
   [*DeviceE-bgp] peer 10.2.1.1 as-number 10
   ```
   ```
   [*DeviceE-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceE-bgp-af-ipv4] network 10.3.1.0 30
   ```
   ```
   [*DeviceE-bgp-af-ipv4] quit
   ```
   ```
   [*DeviceE-bgp] commit
   ```
5. Configure the OSPF cost on DeviceC.
   
   
   ```
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ospf cost 2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ospf cost 2
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the OSPF cost is set to 2 on DeviceC, DeviceA selects only DeviceB as the intermediate device to the network segment 10.2.1.0, and DeviceC becomes a backup of DeviceB.
   
   # Display the routing table on DeviceA. As shown in the routing table, the route to the network segment 10.3.1.0 is learned through BGP, and the outbound interface is GigabitEthernet0/1/0.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 20       Routes : 20
   
       Destination/Mask       Proto    Pre  Cost    Flags NextHop         Interface
   
           1.1.1.1/32         Direct   0    0       D     127.0.0.1       InLoopBack0
         1.1.1.255/32         Direct   0    0       D     127.0.0.1       InLoopBack0
           2.2.2.2/32         OSPF     10   3       D     10.1.1.2        GigabitEthernet0/1/0
           4.4.4.0/24         BGP      255  0       RD    4.4.4.4         GigabitEthernet0/1/0
           4.4.4.4/32         OSPF     10   3       D     10.1.1.2        GigabitEthernet0/1/0
           5.5.5.0/24         BGP      255  0       RD    10.2.1.2        GigabitEthernet0/1/0
          10.1.1.0/30         Direct   0    0       D     10.1.1.1        GigabitEthernet0/1/0
          10.1.1.3/32         Direct   0    0       D     10.1.1.1        GigabitEthernet0/1/0
          10.1.1.1/32         Direct   0    0       D     127.0.0.1       InLoopBack0
        10.1.1.255/32         Direct   0    0       D     127.0.0.1       InLoopBack0
        10.1.1.255/32         Direct   0    0       D     10.1.1.2        GigabitEthernet0/1/0
          10.1.1.2/32         Direct   0    0       D     10.1.1.2        GigabitEthernet0/1/0
        10.1.1.255/32         Direct   0    0       D     10.1.1.2        GigabitEthernet0/1/0
          10.1.2.0/30         Direct   0    0       D     10.1.2.1        GigabitEthernet0/2/0
          10.1.2.3/32         Direct   0    0       D     10.1.2.1        GigabitEthernet0/2/0
          10.1.2.1/32         Direct   0    0       D     127.0.0.1       InLoopBack0
        10.1.2.255/32         Direct   0    0       D     127.0.0.1       InLoopBack0
          10.1.2.2/32         Direct   0    0       D     10.1.2.2        GigabitEthernet0/2/0
        10.1.2.255/32         Direct   0    0       D     10.1.2.2        GigabitEthernet0/2/0
         127.0.0.0/8          Direct   0    0       D     127.0.0.1       InLoopBack0
         127.0.0.1/32         Direct   0    0       D     127.0.0.1       InLoopBack0
       127.0.0.255/32         Direct   0    0       D     127.0.0.1       InLoopBack0
         10.3.1.0/30          OSPF     10   2       D     10.1.1.2        GigabitEthernet0/1/0
          10.1.3.1/32         BGP      255  0       RD    4.4.4.4         GigabitEthernet0/1/0
          10.1.4.0/30         OSPF     10   3       D     10.1.1.2        GigabitEthernet0/1/0
                              OSPF     10   3       D     10.1.2.2        GigabitEthernet0/2/0
          10.1.4.1/32         BGP      255  0       RD    4.4.4.4         GigabitEthernet0/1/0
          10.2.1.0/30         BGP      255  0       RD    4.4.4.4         GigabitEthernet0/1/0
          10.2.1.2/32         BGP      255  0       RD    4.4.4.4         GigabitEthernet0/1/0
          10.3.1.0/30         BGP      255  0       RD    4.4.4.4         GigabitEthernet0/1/0
   255.255.255.255/32         Direct   0    0       D     127.0.0.1       InLoopBack0
   ```
   
   # Display the routing table on DeviceB.
   
   ```
   [~DeviceB] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 19       Routes : 19
   
       Destination/Mask       Proto    Pre  Cost      Flags NextHop         Interface
   
           2.2.2.2/32         Direct   0    0           D   127.0.0.1        InLoopBack0
         2.2.2.255/32         Direct   0    0           D   127.0.0.1        InLoopBack0
           1.1.1.1/32         OSPF     10   2           D   10.1.1.1         GigabitEthernet0/1/0
           4.4.4.0/24         BGP      255  0           RD  10.1.3.2         GigabitEthernet0/2/0
           4.4.4.4/32         OSPF     10   2           D   10.1.3.2         GigabitEthernet0/2/0
           5.5.5.0/24         BGP      255  0           RD  10.2.1.2         GigabitEthernet0/2/0
          10.1.1.0/30         Direct   0    0           D   10.1.1.2         GigabitEthernet0/1/0
          10.1.1.3/32         Direct   0    0           D   10.1.1.2         GigabitEthernet0/1/0
          10.1.1.1/32         Direct   0    0           D   10.1.1.1         GigabitEthernet0/1/0
        10.1.1.255/32         Direct   0    0           D   10.1.1.1         GigabitEthernet0/1/0
          10.1.1.2/32         Direct   0    0           D   127.0.0.1        InLoopBack0
        10.1.1.255/32         Direct   0    0           D   127.0.0.1        InLoopBack0
          10.1.2.0/30         OSPF     10   2           D   10.1.1.1         GigabitEthernet0/1/0
          10.1.3.0/30         Direct   0    0           D   10.1.3.1         GigabitEthernet0/2/0
          10.1.3.3/32         Direct   0    0           D   10.1.3.1         GigabitEthernet0/2/0
          10.1.3.1/32         Direct   0    0           D   127.0.0.1        InLoopBack0
        10.1.3.255/32         Direct   0    0           D   127.0.0.1        InLoopBack0
          10.1.3.2/32         Direct   0    0           D   10.1.3.2         GigabitEthernet0/2/0
        10.1.3.255/32         Direct   0    0           D   10.1.3.2         GigabitEthernet0/2/0
         127.0.0.0/8          Direct   0    0           D   127.0.0.1        InLoopBack0
         127.0.0.1/32         Direct   0    0           D   127.0.0.1        InLoopBack0
       127.0.0.255/32         Direct   0    0           D   127.0.0.1        InLoopBack0
          10.1.4.0/30         OSPF     10   2           D   10.1.3.2         GigabitEthernet0/2/0
          10.1.4.1/32         BGP      255  0           RD  10.1.3.2         GigabitEthernet0/2/0
          10.2.1.0/30         BGP      255  0           RD  10.1.3.2         GigabitEthernet0/2/0
          10.2.1.2/32         BGP      255  0           RD  10.1.3.2         GigabitEthernet0/2/0
         10.3.1.0/30         BGP       255  0          RD  10.1.3.2         GigabitEthernet0/2/0
   255.255.255.255/32         Direct   0    0           D   127.0.0.1        InLoopBack0
   ```
   
   As shown in the routing table, DeviceB learns the route to 10.3.1.0 through BGP, and the outbound interface is GE 0/2/0. The routes to 10.1.2.0 and 10.1.4.0 can be learned through OSPF. The costs of these routes are both 2.
6. Enable OSPF-BGP synchronization on DeviceB.
   
   
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] stub-router on-startup
   ```
   ```
   [*DeviceB-ospf-1] commit
   ```
7. Verify the configuration.
   
   
   
   # Restart Router DeviceB.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Exercise caution when running this command because it may lead to a temporary network crash. In addition, save the configuration file of the Router before restarting it.
   
   ```
   <DeviceB> reboot
   ```
   ```
   System will reboot! Continue?[Y/N] y
   ```
   
   # Display the routing table on DeviceA. As shown in the routing table, BGP learns the route to 10.3.1.0, and the outbound interface is GigabitEthernet0/2/0.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 20       Routes : 20
   
   Destination/Mask    Proto  Pre  Cost      Flags NextHop         Interface
   
           1.1.1.1/32  Direct 0    0           D   127.0.0.1        InLoopBack0
           2.2.2.2/32  OSPF   10   4           D   10.1.2.2         GigabitEthernet0/2/0
           4.4.4.0/24  BGP    255  0           RD  4.4.4.4          GigabitEthernet0/2/0
           4.4.4.4/32  OSPF   10   4           D   10.1.2.2         GigabitEthernet0/2/0
           5.5.5.0/24  BGP    255  0           RD  10.2.1.2         GigabitEthernet0/2/0
          10.1.1.0/30  Direct 0    0           D   10.1.1.1         GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0           D   127.0.0.1        InLoopBack0
          10.1.1.2/32  Direct 0    0           D   10.1.1.2         GigabitEthernet0/1/0
          10.1.2.0/30  Direct 0    0           D   10.1.2.1         GigabitEthernet0/2/0
          10.1.2.1/32  Direct 0    0           D   127.0.0.1        InLoopBack0
          10.1.2.2/32  Direct 0    0           D   10.1.2.2         GigabitEthernet0/2/0
         127.0.0.0/8   Direct 0    0           D   127.0.0.1        InLoopBack0
         127.0.0.1/32  Direct 0    0           D   127.0.0.1        InLoopBack0
          10.1.3.0/30  OSPF   10   2           D   10.1.1.2         GigabitEthernet0/1/0
          10.1.3.1/32  BGP    255  0           RD  4.4.4.4          GigabitEthernet0/2/0
          10.1.4.0/30  OSPF   10   3           D   10.1.2.2         GigabitEthernet0/2/0
          10.1.4.1/32  BGP    255  0           RD  4.4.4.4          GigabitEthernet0/2/0
          10.2.1.0/30  BGP    255  0           RD  4.4.4.4          GigabitEthernet0/2/0
          10.2.1.2/32  BGP    255  0           RD  4.4.4.4          GigabitEthernet0/2/0
         10.3.1.0/30   BGP   255  0            RD  4.4.4.4          GigabitEthernet0/2/0
   ```
   
   # Display the routing table on DeviceB. As shown in the routing table, only OSPF routes exist in the routing table because IGP routes converge faster than BGP routes do. The costs of the OSPF routes are 65535.
   
   ```
   [~DeviceB] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 15       Routes : 15
   
   Destination/Mask    Proto  Pre  Cost      Flags NextHop        Interface
   
          1.1.1.1/32   OSPF   10   65536       D  10.1.1.1        GigabitEthernet0/1/0
           2.2.2.2/32  Direct 0    0           D  127.0.0.1       InLoopBack0
          4.4.4.4/32   OSPF   10   65536       D  10.1.3.2        GigabitEthernet0/2/0
          10.1.1.0/30  Direct 0    0           D  10.1.1.2        GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0           D  10.1.1.1        GigabitEthernet0/1/0
          10.1.1.2/32  Direct 0    0           D  127.0.0.1       InLoopBack0
         10.1.2.0/30   OSPF   10   65536       D  10.1.1.1        GigabitEthernet0/1/0
          10.1.3.0/30  Direct 0    0           D  10.1.3.1        GigabitEthernet0/2/0
          10.1.3.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
          10.1.3.2/32  Direct 0    0           D  10.1.3.2        GigabitEthernet0/2/0
         127.0.0.0/8   Direct 0    0           D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
         10.1.4.0/30   OSPF   10   65536       D  10.1.3.2        GigabitEthernet0/2/0
         127.0.0.0/8   Direct 0    0           D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   
   # Display the routing table on DeviceB again.
   
   ```
   [~DeviceB] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 19       Routes : 19
   
   Destination/Mask    Proto  Pre  Cost       Flags NextHop       Interface
   
           2.2.2.2/32  Direct 0    0           D    127.0.0.1        InLoopBack0
           1.1.1.1/32  OSPF   10   2           D    10.1.1.1         GigabitEthernet0/1/0
           4.4.4.0/24  BGP    255  0           RD   10.1.3.2         GigabitEthernet0/2/0
           4.4.4.4/32  OSPF   10   2           D    10.1.3.2         GigabitEthernet0/2/0
           5.5.5.0/24  BGP    255  0           RD   10.2.1.2         GigabitEthernet0/2/0
          10.1.1.0/30  Direct 0    0           D    10.1.1.2         GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0           D    10.1.1.1         GigabitEthernet0/1/0
          10.1.1.2/32  Direct 0    0           D    127.0.0.1        InLoopBack0
          10.1.2.0/30  OSPF   10   2           D    10.1.1.1         GigabitEthernet0/1/0
          10.1.3.0/30  Direct 0    0           D    10.1.3.1         GigabitEthernet0/2/0
          10.1.3.1/32  Direct 0    0           D    127.0.0.1        InLoopBack0
          10.1.3.2/32  Direct 0    0           D    10.1.3.2         GigabitEthernet0/2/0
         127.0.0.0/8   Direct 0    0           D    127.0.0.1        InLoopBack0
         127.0.0.1/32  Direct 0    0           D    127.0.0.1        InLoopBack0
          10.1.4.0/30  OSPF   10   2           D    10.1.3.2         GigabitEthernet0/2/0
          10.1.4.1/32  BGP    255  0           RD   10.1.3.2         GigabitEthernet0/2/0
          10.2.1.0/30  BGP    255  0           RD   10.1.3.2         GigabitEthernet0/2/0
          10.2.1.2/32  BGP    255  0           RD   10.1.3.2         GigabitEthernet0/2/0
          10.3.1.0/30  BGP    255  0           RD   10.1.3.2         GigabitEthernet0/2/0
   ```
   
   As shown in the routing table, BGP routes on DeviceB have converged, and the routing information is the same as that displayed before the restart.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
  router id 1.1.1.1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.252
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.252
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 10
   router-id 1.1.1.1
   peer 2.2.2.2 as-number 10
   peer 2.2.2.2 connect-interface LoopBack 0
   peer 3.3.3.3 as-number 10
   peer 3.3.3.3 connect-interface LoopBack 0
   peer 4.4.4.4 as-number 10
   peer 4.4.4.4 connect-interface LoopBack 0
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.3
    network 10.1.2.0 0.0.0.3
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  router id 2.2.2.2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.252
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.252
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 10
   router-id 2.2.2.2
   peer 1.1.1.1 as-number 10
   peer 1.1.1.1 connect-interface LoopBack 0
   peer 3.3.3.3 as-number 10
   peer 3.3.3.3 connect-interface LoopBack 0
   peer 4.4.4.4 as-number 10
   peer 4.4.4.4 connect-interface LoopBack 0
  #
  ospf 1
   stub-router on-startup
   area 0.0.0.0
    network 10.1.1.0 0.0.0.3
    network 10.1.3.0 0.0.0.3
    network 2.2.2.2 0.0.0.0
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
   sysname DeviceC
  #
  router id 3.3.3.3
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.1 255.255.255.252
   ospf cost 2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.252
   ospf cost 2
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 10
   router-id 3.3.3.3
   peer 1.1.1.1 as-number 10
   peer 1.1.1.1 connect-interface LoopBack 0
   peer 2.2.2.2 as-number 10
   peer 2.2.2.2 connect-interface LoopBack 0
   peer 4.4.4.4 as-number 10
   peer 4.4.4.4 connect-interface LoopBack 0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.2.0 0.0.0.3
    network 10.1.4.0 0.0.0.3
    network 3.3.3.3 0.0.0.0
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
   sysname DeviceD
  #
  router id 4.4.4.4
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.2 255.255.255.252
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.3.2 255.255.255.252
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.252
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 10
   router-id 4.4.4.4
   peer 10.2.1.2 as-number 20
   peer 1.1.1.1 as-number 10
   peer 1.1.1.1 connect-interface LoopBack 0
   peer 2.2.2.2 as-number 10
   peer 2.2.2.2 connect-interface LoopBack 0
   peer 3.3.3.3 as-number 10
   peer 3.3.3.3 connect-interface LoopBack 0
   #
  ipv4-family unicast
    undo synchronization
    import-route direct
    import-route ospf 1
    peer 10.2.1.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.1.3.0 0.0.0.3
    network 10.1.4.0 0.0.0.3
  #
  return
  ```
* DeviceE configuration file
  
  ```
  #
   sysname DeviceE
  #
  router id 5.5.5.5
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.252
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.252
  #
  interface LoopBack0
   ip address 5.5.5.5 255.255.255.255
  #
  bgp 20
   router-id 5.5.5.5
   peer 10.2.1.1 as-number 10
  #
  ipv4-family unicast
    undo synchronization
    network 10.3.1.0 255.255.255.252
    peer 10.2.1.1 enable
  #
  return
  ```