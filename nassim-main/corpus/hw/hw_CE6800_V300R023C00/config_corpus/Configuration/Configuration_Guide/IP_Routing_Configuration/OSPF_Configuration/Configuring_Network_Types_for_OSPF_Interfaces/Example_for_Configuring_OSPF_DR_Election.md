Example for Configuring OSPF DR Election
========================================

Example for Configuring OSPF DR Election

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001356100582__fig_dc_cfg_ospf_009101), DeviceA has the highest priority (100) on the network and is elected as the DR; DeviceC has the second highest priority and is elected as the BDR. DeviceB has the priority of 0 and cannot be elected as a DR or a BDR; no priority is configured for DeviceD, and therefore, and DeviceD uses the default value (1).

**Figure 1** Configuring OSPF DR election![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001356101138.png)

#### Precautions

To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security." OSPF area authentication is used as an example. For details, see "Example for Configuring Basic OSPF Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a router ID, enable OSPF, and specify a network segment on each device.
2. Check the DR/BDR status of each device when the default priority is used.
3. Configure DR priorities for interfaces and check the DR/BDR status.

#### Procedure

1. Assign an IP address to each interface. For detailed configurations, see Configuration Scripts.
2. Configure basic OSPF functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] router id 1.1.1.1
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] router id 2.2.2.2
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] router id 3.3.3.3
   [*DeviceC] ospf 1
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.1] network 192.168.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.1] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] router id 4.4.4.4
   [*DeviceD] ospf 1
   [*DeviceD-ospf-1] area 0
   [*DeviceD-ospf-1-area-0.0.0.2] network 192.168.1.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.2] quit
   [*DeviceD-ospf-1] quit
   [*DeviceD] commit
   ```
   
   # Check the DR/BDR status.
   
   ```
   [~DeviceA] display ospf peer
             OSPF Process 1 with Router ID 1.1.1.1
                     Neighbors
    Area 0.0.0.0 interface 192.168.1.1(100GE1/0/1)'s neighbors
    Router ID: 2.2.2.2      Address: 192.168.1.2
   State: 2-Way  Mode:Nbr is  Master  Priority: 1
   DR: 192.168.1.4  BDR: 192.168.1.3  MTU: 0
      Dead timer due in 32  sec
      Retrans timer interval: 5
      Neighbor is up for 00:04:21
      Authentication Sequence: [ 0 ]
    Router ID: 3.3.3.3      Address: 192.168.1.3
   State: Full  Mode:Nbr is  Master  Priority: 1
   DR: 192.168.1.4  BDR: 192.168.1.3  MTU: 0
      Dead timer due in 37  sec
      Retrans timer interval: 5
      Neighbor is up for 00:04:06
      Authentication Sequence: [ 0 ]
    Router ID: 4.4.4.4      Address: 192.168.1.4
   State: Full  Mode:Nbr is  Master  Priority: 1
   DR: 192.168.1.4  BDR: 192.168.1.3  MTU: 0
      Dead timer due in 37  sec
      Retrans timer interval: 5
      Neighbor is up for 00:03:53
      Authentication Sequence: [ 0 ]
   
   ```
   
   Check information about the neighbors of DeviceA, including DR priorities and neighbor status. By default, the DR priority is 1. DeviceD functions as the DR, and DeviceC functions as the BDR.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   When the priorities are the same, the device with the highest router ID is elected as the DR. If a new device is added after the DR and BDR are elected, the new device cannot immediately become the new DR on the network segment even if it has the highest DR priority.
3. Set DR priorities for interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100GE1/0/1 
   [~DeviceA-100GE1/0/1] ospf dr-priority 100
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100GE1/0/1 
   [~DeviceB-100GE1/0/1] ospf dr-priority 0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface 100GE1/0/1 
   [~DeviceC-100GE1/0/1] ospf dr-priority 2
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
   
   # Check the DR/BDR status.
   
   ```
   [~DeviceD] display ospf peer
             OSPF Process 1 with Router ID 4.4.4.4
                     Neighbors
    Area 0.0.0.0 interface 192.168.1.4(100GE1/0/1)'s neighbors
    Router ID: 1.1.1.1      Address: 192.168.1.1
      State: Full  Mode:Nbr is  Slave  Priority: 100
   DR: 192.168.1.4  BDR: 192.168.1.3  MTU: 0
      Dead timer due in 31  sec
      Retrans timer interval: 5
      Neighbor is up for 00:11:17
      Authentication Sequence: [ 0 ]
    Router ID: 2.2.2.2      Address: 192.168.1.2
      State: Full  Mode:Nbr is  Slave  Priority: 0
   DR: 192.168.1.4  BDR: 192.168.1.3  MTU: 0
      Dead timer due in 35  sec
      Retrans timer interval: 5
      Neighbor is up for 00:11:19
      Authentication Sequence: [ 0 ]
    Router ID: 3.3.3.3      Address: 192.168.1.3
      State: Full  Mode:Nbr is  Slave  Priority: 2
   DR: 192.168.1.4  BDR: 192.168.1.3  MTU: 0
      Dead timer due in 33  sec
      Retrans timer interval: 5
      Neighbor is up for 00:11:15
      Authentication Sequence: [ 0 ]
   ```
4. Restart an OSPF process.
   
   
   
   Run the **reset ospf 1 process** command in the user view of each device to restart the OSPF process.

#### Verifying the Configuration

# Check OSPF neighbor information on DeviceD.

```
[~DeviceD] display ospf peer
          OSPF Process 1 with Router ID 4.4.4.4
                  Neighbors
 Area 0.0.0.0 interface 192.168.1.4(100GE1/0/1)'s neighbors
 Router ID: 1.1.1.1      Address: 192.168.1.1
State: Full  Mode:Nbr is  Slave  Priority: 100
DR: 192.168.1.1  BDR: 192.168.1.3  MTU: 0
   Dead timer due in 35  sec
   Retrans timer interval: 5
   Neighbor is up for 00:07:19
   Authentication Sequence: [ 0 ]
 Router ID: 2.2.2.2      Address: 192.168.1.2
State: 2-Way  Mode:Nbr is  Master  Priority: 0
DR: 192.168.1.1  BDR: 192.168.1.3  MTU: 0
   Dead timer due in 35  sec
   Retrans timer interval: 5
   Neighbor is up for 00:07:19
   Authentication Sequence: [ 0 ]
 Router ID: 3.3.3.3      Address: 192.168.1.3
State: Full  Mode:Nbr is  Slave  Priority: 2
DR: 192.168.1.1  BDR: 192.168.1.3  MTU: 0
   Dead timer due in 37  sec
   Retrans timer interval: 5
   Neighbor is up for 00:07:17
   Authentication Sequence: [ 0 ]
```

# Check the status of OSPF interfaces on DeviceA.

```
[~DeviceA] display ospf interface
          OSPF Process 1 with Router ID 1.1.1.1
                  Interfaces
 Area: 0.0.0.0
 IP Address  Type        State    Cost  Pri   DR              BDR
 192.168.1.1 Broadcast   DR     1     100 192.168.1.1 192.168.1.3
OSPF Process 1 with Router ID 1.1.1.1
```

# Check the status of OSPF interfaces on DeviceB.

```
[~DeviceB] display ospf interface
          OSPF Process 1 with Router ID 2.2.2.2
                  Interfaces
 Area: 0.0.0.0
 IP Address      Type         State    Cost  Pri   DR              BDR
 192.168.1.2     Broadcast    DROther  1     0 192.168.1.1 192.168.1.3
```

If the neighbor is in the Full state, an adjacency has been established with the neighbor. If the neighbor remains in the 2-Way state, it is not the DR or BDR, and the two ends do not need to exchange LSAs.

If the status of an OSPF interface is DROther, it indicates that the interface is neither a DR nor a BDR.


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
   ip address 192.168.1.1 255.255.255.0
   ospf dr-priority 100
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
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
   ip address 192.168.1.2 255.255.255.0
   ospf dr-priority 0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceB
  #
  router id 3.3.3.3
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.3 255.255.255.0
   ospf dr-priority 2
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceB
  #
  router id 4.4.4.4
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.4 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  return
  ```