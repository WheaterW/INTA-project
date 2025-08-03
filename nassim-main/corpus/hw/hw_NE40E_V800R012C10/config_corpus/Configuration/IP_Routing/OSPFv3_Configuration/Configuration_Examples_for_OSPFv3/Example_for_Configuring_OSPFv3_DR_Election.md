Example for Configuring OSPFv3 DR Election
==========================================

This section describes how to set the DR priority on an interface for DR election on a broadcast network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365803__fig_dc_vrp_ospfv3_cfg_206401), DeviceA has the highest priority (100) on the network and is elected as the DR; DeviceC has the second highest priority and is elected as the BDR. DeviceB has the priority of 0 and cannot be elected as a DR or a BDR; no priority is configured for DeviceD, and therefore, and DeviceD uses the default value (1).

**Figure 1** Networking for configuring OSPFv3 DR election![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_vrp_ospfv3_cfg_206401.png)  


#### Configuration Notes

Reconfiguring the DR priority for the Router does not change the DR or BDR on a network. You can use either of the following methods to re-elect a DR or BDR. However, the following methods will disconnect OSPFv3 adjacencies and therefore are not recommended.

* Restart the OSPFv3 processes on all Routers.
* Configure the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands on the interfaces where the OSPFv3 neighbor relationships are established.

To improve security, you are advised to deploy OSPFv3 authentication. For details, see "Configuring OSPFv3 Authentication". OSPFv3 IPSec is used as an example. For details, see "Example for Configuring IPSec for OSPFv3".


#### Configuration Roadmap

1. Configure the router ID on each Router, enable OSPFv3, and specify the network segment.
2. Check the DR/BDR status with the default priority.
3. Configure the DR priority on the interface and check the DR/BDR status.

#### Data Preparation

To complete the configuration, you need the following data:

* Router ID (1.1.1.1) and DR priority (100) of Device A
* Router ID (2.2.2.2) and DR priority (0) of Device B
* Router ID (3.3.3.3) and DR priority (2) of Device C
* Router ID (4.4.4.4) and DR priority (1, default value) of Device D

#### Procedure

1. Assign an IPv6 address to each interface.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172365803__section_dc_vrp_ospfv3_cfg_206406) in this section.
2. Configure basic OSPFv3 functions.
   
   
   
   # Configure DeviceA, enable OSPFv3, and set its router ID to 1.1.1.1.
   
   ```
   [*DeviceA] ospfv3
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospfv3-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB, enable OSPFv3, and set its router ID to 2.2.2.2.
   
   ```
   [*DeviceB] ospfv3
   ```
   ```
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-ospfv3-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC, enable OSPFv3, and set its router ID to 3.3.3.3.
   
   ```
   [*DeviceC] ospfv3
   ```
   ```
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-ospfv3-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD, enable OSPFv3, and set its router ID to 4.4.4.4.
   
   ```
   [*DeviceD] ospfv3
   ```
   ```
   [*DeviceD-ospfv3-1] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-ospfv3-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Display the neighbors of DeviceA. You can view the DR priority and the neighbor status. By default, the DR priority is 1. DeviceD is the DR, and DeviceC is the BDR.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The Router with the greatest router ID is the DR when Routers have the same priority. If an Ethernet interface of the Router becomes a DR, the other broadcast interfaces of the Router have the highest priority in DR election. That is, the DR cannot be preempted.
   
   ```
   [~DeviceA] display ospfv3 peer
   ```
   ```
       OSPFv3 Process (1)
       Total number of peer(s): 3
        Peer(s) in full state: 2
       OSPFv3 Area (0.0.0.0)
       Neighbor ID     Pri   State            Dead Time   Interface  Instance ID
       2.2.2.2       1   2-Way/DROther    00:00:32    GE0/1/0         0
       3.3.3.3       1   Full/Backup      00:00:36    GE0/1/0         0
       4.4.4.4       1   Full/DR          00:00:38    GE0/1/0         0
   ```
   
   # Display the neighbors of DeviceD. The command output shows that all neighbors of DeviceD are in the Full state.
   
   ```
   [~DeviceD] display ospfv3 peer
   ```
   ```
       OSPFv3 Process (1)
       Total number of peer(s): 3
        Peer(s) in full state: 3
       OSPFv3 Area (0.0.0.0)
       Neighbor ID     Pri   State            Dead Time   Interface  Instance ID
       1.1.1.1       1   Full/DROther     00:00:32    GE0/1/0         0
       2.2.2.2       1   Full/DROther     00:00:35    GE0/1/0         0
       3.3.3.3       1   Full/Backup      00:00:30    GE0/1/0         0
   ```
3. Set the DR priority of the interface.
   
   
   
   # Set the DR priority of DeviceA to 100.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ospfv3 dr-priority 100
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Set the DR priority of DeviceB to 0.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ospfv3 dr-priority 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Set the DR priority of DeviceC to 2.
   
   ```
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] ospfv3 dr-priority 2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Display the neighbors of DeviceA. The command output shows that the DR priority is updated and that the DR and BDR remain unchanged.
   
   ```
   [~DeviceA] display ospfv3 peer
   ```
   ```
       OSPFv3 Process (1)
       Total number of peer(s): 2
        Peer(s) in full state: 3
       OSPFv3 Area (0.0.0.0)
       Neighbor ID     Pri   State            Dead Time   Interface  Instance ID
       2.2.2.2       0   2-Way/DROther    00:00:34    GE0/1/0         0
       3.3.3.3       2   Full/Backup      00:00:38    GE0/1/0         0
       4.4.4.4       1   Full/DR          00:00:31    GE0/1/0         0
   ```
   
   # Display the neighbors of DeviceD. The command output shows that DeviceD remains the DR.
   
   ```
   [~DeviceD] display ospfv3 peer
   ```
   ```
       OSPFv3 Process (1)
       Total number of peer(s): 3
        Peer(s) in full state: 3
       OSPFv3 Area (0.0.0.0)
       Neighbor ID     Pri   State            Dead Time   Interface  Instance ID
       1.1.1.1      100   Full/DROther     00:00:36    GE0/1/0         0
       2.2.2.2      0   Full/DROther       00:00:30    GE0/1/0         0
       3.3.3.3      2   Full/Backup        00:00:36    GE0/1/0         0
   ```
4. Re-elect the DR/BDR.
   
   
   
   # Restart all Routers (or run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands on the interface that establishes the OSPFv3 neighbor relationship), and re-elect the DR/BDR.
5. Verify the configuration.
   
   
   
   # Display the neighbors of DeviceA. The command output shows that DeviceC is the BDR.
   
   ```
   [~DeviceA] display ospfv3 peer
   ```
   ```
      OSPFv3 Process (1)
      Total number of peer(s): 3
       Peer(s) in full state: 3
      OSPFv3 Area (0.0.0.0)
      Neighbor ID     Pri   State            Dead Time   Interface  Instance ID
      2.2.2.2       0   Full/DROther     00:00:31    GE0/1/0         0
      3.3.3.3       2   Full/Backup      00:00:36    GE0/1/0         0
      4.4.4.4       1   Full/DROther     00:00:39    GE0/1/0         0
   ```
   
   # Check the neighbors of DeviceD. The command output shows that DeviceA functions as the DR.
   
   ```
   [~DeviceD] display ospfv3 peer
   ```
   ```
      OSPFv3 Process (1)
      Total number of peer(s): 3
       Peer(s) in full state: 2
      OSPFv3 Area (0.0.0.0)
      Neighbor ID     Pri   State            Dead Time   Interface  Instance ID
      1.1.1.1       100   Full/DR        00:00:39    GE0/1/0         0
      2.2.2.2       0   2-Way/DROther    00:00:35    GE0/1/0         0
      3.3.3.3       2   Full/Backup      00:00:39    GE0/1/0         0
   ```

#### Configuration Files

* DeviceA configuration file
  
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1001::1/96
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
   ospfv3 dr-priority 100
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 1.1.1.1
  ```
  ```
   area 0.0.0.0
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1001::2/96
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
   ospfv3 dr-priority 0
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 2.2.2.2
  ```
  ```
   area 0.0.0.0
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1001::3/96
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
   ospfv3 dr-priority 2
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 3.3.3.3
  ```
  ```
   area 0.0.0.0
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1001::4/96
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 4.4.4.4
  ```
  ```
   area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```