Example for Configuring OSPF DR Election
========================================

This section describes how to set the DR priority on an interface for DR election on a broadcast network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365658__fig_dc_vrp_ospf_cfg_009701), the interface of DeviceA has the highest priority of 100 on the network and is elected as the DR; DeviceC has the second highest priority and is elected as the BDR. DeviceB has the priority of 0 and cannot be elected as a DR or a BDR; no priority is configured for DeviceD and therefore, DeviceD uses the default value (1).

**Figure 1** Networking for configuring OSPF DR election![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_vrp_ospf_cfg_009701.png)  


#### Precautions

Reconfiguring the DR priority for a router does not change the DR or BDR on a network. You can use either of the following methods to re-elect a DR or BDR. However, the following methods will disconnect OSPF neighbors. Therefore, use the following methods only when necessary.

* Restart the OSPF processes on all Routers.
* Configure the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands on the interfaces where the OSPF neighboring relationships are established.
* To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security". OSPF area authentication is used as an example. For details, see Example for Configuring Basic OSPF Functions.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions on each Router for interconnection.
2. Configure a router ID for each Router.
3. Check the DR or BDR status on each Router when the default priority is used.
4. Configure the DR priority on an interface and check whether the device is the DR or BDR.

#### Data Preparation

To complete the configuration, you need the following data:

* Router ID (1.1.1.1) and priority (100) of DeviceA
* Router ID (2.2.2.2) and priority (0) of DeviceB
* Router ID (3.3.3.3) and priority (2) of DeviceC
* Router ID (4.4.4.4) and priority (1) of DeviceD

#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365658__section_dc_vrp_ospf_cfg_009706) in this section.
2. Configure basic OSPF functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] router id 1.1.1.1
   ```
   ```
   [*DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] router id 2.2.2.2
   ```
   ```
   [*DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255 
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] router id 3.3.3.3
   ```
   ```
   [*DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] area 0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceC-ospf-1-area-0.0.0.0] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] router id 4.4.4.4
   ```
   ```
   [*DeviceD] ospf 1
   ```
   ```
   [*DeviceD-ospf-1] area 0
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255 
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceD-ospf-1-area-0.0.0.0] quit
   ```
   
   # Display the status of the DR or BDR.
   
   ```
   [~DeviceA] display ospf peer
   ```
   ```
             OSPF Process 1 with Router ID 1.1.1.1
                   Neighbors
   
    Area 0.0.0.0 interface 192.168.1.1 ( GE0/1/0 )'s neighbors
    Router ID: 2.2.2.2         Address: 192.168.1.2
      State: 2-Way  Mode:Nbr is  Slave   Priority: 1
      DR: 192.168.1.4   BDR: 192.168.1.3    MTU: 0
      Dead timer due in  32  sec
      Retrans timer interval: 0
      Neighbor is up for 1h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   
    Area 0.0.0.0 interface 192.168.1.1 ( GE0/1/0 )'s neighbors
    Router ID: 3.3.3.3         Address: 192.168.1.3
      State: Full  Mode:Nbr is  Master   Priority: 1
      DR: 192.168.1.4   BDR: 192.168.1.3    MTU: 0
      Dead timer due in  34  sec
      Retrans timer interval: 5
      Neighbor is up for 1h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   
    Area 0.0.0.0 interface 192.168.1.1 ( GE0/1/0 )'s neighbors
    Router ID: 4.4.4.4         Address: 192.168.1.4
      State: Full  Mode:Nbr is  Master   Priority: 1
      DR: 192.168.1.4   BDR: 192.168.1.3    MTU: 0
      Dead timer due in  32  sec
      Retrans timer interval: 5
      Neighbor is up for 1h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   ```
   
   Check the neighbor information of DeviceA. You can view the DR priority and the neighbor status. By default, the DR priority is 1. Now DeviceD functions as the DR and DeviceC functions as the BDR.
3. Set the DR priority on each interface.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ospf dr-priority 100
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ospf dr-priority 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] ospf dr-priority 2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
   
   # Display the status of the DR or BDR.
   
   ```
   [~DeviceD] display ospf peer
   ```
   ```
             OSPF Process 1 with Router ID 4.4.4.4
                   Neighbors
   
    Area 0.0.0.0 interface 192.168.1.4 ( GE0/1/0 )'s neighbors
    Router ID: 1.1.1.1         Address: 192.168.1.1
      State: Full  Mode:Nbr is  Slave   Priority: 100
      DR: 192.168.1.4   BDR: 192.168.1.3    MTU: 0
      Dead timer due in  38  sec
      Retrans timer interval: 5
      Neighbor is up for 2h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   
    Area 0.0.0.0 interface 192.168.1.4 ( GE0/1/0 )'s neighbors
    Router ID: 2.2.2.2         Address: 192.168.1.2
      State: Full  Mode:Nbr is  Slave   Priority: 0
      DR: 192.168.1.4   BDR: 192.168.1.3    MTU: 0
      Dead timer due in  38  sec
      Retrans timer interval: 5
      Neighbor is up for 2h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   
    Area 0.0.0.0 interface 192.168.1.4 ( GE0/1/0 )'s neighbors
    Router ID: 3.3.3.3         Address: 192.168.1.3
      State: Full  Mode:Nbr is  Slave   Priority: 2
      DR: 192.168.1.4   BDR: 192.168.1.3    MTU: 0
      Dead timer due in  30  sec
      Retrans timer interval: 5
      Neighbor is up for 2h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   ```
4. Restart the OSPF processes.
   
   
   
   In the user view of each Router, run the **reset ospf 1 process** command to restart the OSPF process.
5. Verify the configuration.
   
   
   
   # Display the status of OSPF neighbors.
   
   ```
   [~DeviceD] display ospf peer
   ```
   ```
             OSPF Process 1 with Router ID 4.4.4.4
                   Neighbors
   
    Area 0.0.0.0 interface 192.168.1.4 ( GE0/1/0 )'s neighbors
    Router ID: 1.1.1.1         Address: 192.168.1.1
      State: Full  Mode:Nbr is  Slave   Priority: 100
      DR: 192.168.1.1   BDR: 192.168.1.3    MTU: 0
      Dead timer due in  35  sec
      Retrans timer interval: 5
      Neighbor is up for 3h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   
    Area 0.0.0.0 interface 192.168.1.4 ( GE0/1/0 )'s neighbors
    Router ID: 2.2.2.2         Address: 192.168.1.2
      State: 2-Way  Mode:Nbr is  Slave   Priority: 0
      DR: 192.168.1.1   BDR: 192.168.1.3    MTU: 0
      Dead timer due in  35  sec
      Retrans timer interval: 0
      Neighbor is up for 3h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   
    Area 0.0.0.0 interface 192.168.1.4 ( GE0/1/0 )'s neighbors
    Router ID: 3.3.3.3         Address: 192.168.1.3
      State: Full  Mode:Nbr is  Slave   Priority: 2
      DR: 192.168.1.1   BDR: 192.168.1.3    MTU: 0
      Dead timer due in  37  sec
      Retrans timer interval: 5
      Neighbor is up for 3h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   ```
   
   # Display the status of OSPF interfaces.
   
   ```
   [~DeviceA] display ospf interface
   ```
   ```
   2020-11-21 15:55:20.606
   
   (M) Indicates MADJ interface
             OSPF Process 1 with Router ID 1.1.1.1
                     Interfaces
                     
    Area: 0.0.0.0    (MPLS TE not enabled)
    Interface              IP Address     Type         State    Cost    Pri
    GigabitEthernet0/1/0   192.168.1.1    Broadcast    DR       1       100
   ```
   ```
   [~DeviceB] display ospf interface
   ```
   ```
   2020-11-21 15:55:20.606
   
   (M) Indicates MADJ interface
   
             OSPF Process 1 with Router ID 2.2.2.2
                     Interfaces
                     
    Area: 0.0.0.0    (MPLS TE not enabled)
    Interface              IP Address     Type         State      Cost     Pri
    GigabitEthernet0/1/0   192.168.1.2    Broadcast    DROther    1        100
   ```
   
   If the neighbor is in the Full state, the device has established a neighbor relationship with its neighbor. If the neighbor remains in the 2-Way state, neither of them is the DR or BDR. In this case, they do not need to exchange LSAs.
   
   If the status of the OSPF interface is DROther, the interface is neither DR nor BDR.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
  router id 1.1.1.1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
   ospf dr-priority 100
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
  router id 2.2.2.2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
   ospf dr-priority 0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceC
  ```
  ```
  #
  ```
  ```
  router id 3.3.3.3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.3 255.255.255.0
  ```
  ```
   ospf dr-priority 2
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceD
  ```
  ```
  #
  ```
  ```
  router id 4.4.4.4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.4 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```