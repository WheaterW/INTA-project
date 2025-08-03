Example for Configuring OSPF Multi-Area Adjacency
=================================================

Example for Configuring OSPF Multi-Area Adjacency

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130783242__fig_dc_vrp_ospf_cfg_207101), all the devices run OSPF, and the entire AS is divided into two areas. In area 1, the link between DeviceA and DeviceB is a high-speed link. According to OSPF, an intra-area path takes precedence over an inter-area path. Therefore, traffic from DeviceA to DeviceB in area 2 is forwarded along the intra-area path DeviceA->DeviceC->DeviceD->DeviceB, meaning that traffic cannot be transmitted over the high-speed link between DeviceA and DeviceB. To address this problem, configure OSPF multi-area adjacency by creating multi-area adjacency interfaces on DeviceA and DeviceB and specifying area 2 for these interfaces so that they belong to this area. In this way, traffic from DeviceA to DeviceB in area 2 can be forwarded along the high-speed link.

**Figure 1** Network diagram of configuring OSPF multi-area adjacency![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176742979.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions.
2. Enable OSPF for an interface.
3. Enable OSPF for a multi-area adjacency interface.


#### Precautions

To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security." OSPF area authentication is used as an example. For details, see "Example for Configuring Basic OSPF Functions."


#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0000001130783242__fig_dc_vrp_ospf_cfg_207101). For detailed configurations, see Configuration Scripts.
2. Configure basic OSPF functions.
   
   
   
   See [Example for Configuring Basic OSPF Functions](vrp_ospf_cfg_0018.html). For detailed configurations, see Configuration Scripts.
3. Enable OSPF for a multi-area adjacency interface.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100GE1/0/1
   [~DeviceA-100GE1/0/1] ospf enable multi-area 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100GE1/0/1
   [~DeviceB-100GE1/0/1] ospf enable multi-area 2
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Run the [**display ospf peer brief**](cmdqueryname=display+ospf+peer+brief) command on DeviceA to check brief information about OSPF neighbors. The command output shows that DeviceA has established OSPF neighbor relationships with DeviceB and DeviceC. It also shows that the multi-area adjacency between DeviceA and DeviceB has been established.

```
[~DeviceA] display ospf peer brief
```
```
(M) Indicates MADJ neighbor

          OSPF Process 1 with Router ID 1.1.1.1
                   Peer Statistic Informations
  Total number of peer(s): 3
  Peer(s) in full state: 3
-------------------------------------------------------------------------
 Area Id         Interface      Neighbor id      State
 0.0.0.1         100GE1/0/1      10.1.1.2          Full
 0.0.0.2         100GE1/0/1      10.1.1.2(M)      Full
 0.0.0.2         100GE1/0/2      10.1.2.2          Full
-------------------------------------------------------------------------
```

# Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on DeviceA to check IP routing information. The command output shows that a route to the destination address 1.1.1.1 exists and its outbound interface is 100GE 0/1/0.

```
[~DeviceA] display ip routing-table
```
```
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 13       Routes : 13        

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

        1.1.1.1/32  OSPF    10   1             D   10.1.1.2        100GE1/0/1
       10.1.1.0/24  Direct  0    0             D   10.1.1.1        100GE1/0/1
       10.1.1.1/32  Direct  0    0             D   127.0.0.1       100GE1/0/1
     10.1.1.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/1
       10.1.2.0/24  Direct  0    0             D   10.1.2.1        100GE1/0/2
       10.1.2.1/32  Direct  0    0             D   127.0.0.1       100GE1/0/2
     10.1.2.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/2
       10.1.3.0/24  OSPF    10   2             D   10.1.1.2        100GE1/0/1
       10.1.4.0/24  OSPF    10   2             D   10.1.2.2        100GE1/0/2
      127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0
127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
```
#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #               
  interface 100GE1/0/1 
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   ospf enable 1 area 0.0.0.1
   ospf enable multi-area 0.0.0.2
  #               
  interface 100GE1/0/2 
   
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
   ospf enable 1 area 0.0.0.2
  #               
  ospf 1          
   area 0.0.0.1   
   area 0.0.0.2   
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
   ip address 10.1.1.2 255.255.255.0
   ospf enable 1 area 0.0.0.1
   ospf enable multi-area 0.0.0.2
  #               
  interface 100GE1/0/2 
   
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
   ospf enable 1 area 0.0.0.2
  #               
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   ospf enable 1 area 0.0.0.2
  #               
  ospf 1          
   area 0.0.0.1   
   area 0.0.0.2   
  #               
  return         
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #               
  interface 100GE1/0/1  
   undo portswitch
   ip address 10.1.4.1 255.255.255.0
   ospf enable 1 area 0.0.0.2
  #               
  interface 100GE1/0/2  
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   ospf enable 1 area 0.0.0.2
  #               
  ospf 1          
   area 0.0.0.2   
  #               
  return      
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #               
  interface 100GE1/0/1  
   undo portswitch
   ip address 10.1.4.2 255.255.255.0
   ospf enable 1 area 0.0.0.2
  #
  interface 100GE1/0/2 
   
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
   ospf enable 1 area 0.0.0.2
  #               
  ospf 1          
   area 0.0.0.2   
  #               
  return          
  ```