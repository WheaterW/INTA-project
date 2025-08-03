Example for Configuring OSPF GTSM
=================================

Example for Configuring OSPF GTSM

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130623446__fig_dc_vrp_gtsm_cfg_001001), OSPF runs on each device, and GTSM is enabled on each device. The valid TTL ranges of the packets sent from each device to DeviceC are as follows:

* DeviceA and DeviceE are directly connected to DeviceC; therefore, the valid TTL ranges in the packets are both [255, 255].
* The valid TTL ranges in the packets sent from DeviceB, DeviceD, and DeviceF to DeviceC are [254, 255], [253, 255], and [252, 255], respectively.

**Figure 1** Network diagram of OSPF GTSM![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130623510.png)

#### Configuration Precautions

To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security." OSPF area authentication is used as an example. For details, see "Example for Configuring Basic OSPF Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions.
2. Enable GTSM on each device and specify a valid TTL range.

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address to each interface as shown in [Figure 1](#EN-US_TASK_0000001130623446__fig_dc_vrp_gtsm_cfg_001001). For detailed configurations, see the configuration scripts.
2. Configure basic OSPF functions.
   
   
   
   See [Example for Configuring Basic OSPF Functions](vrp_ospf_cfg_0018.html). For detailed configurations, see Configuration Scripts in this section.
3. Configure OSPF GTSM.
   
   
   
   # Set the valid TTL range in packets from DeviceC to the other devices to [252, 255].
   
   ```
   [~DeviceC] ospf valid-ttl-hops 4
   [*DeviceC] commit
   ```
   
   # Set the valid TTL range in packets from DeviceA to DeviceC to [255, 255].
   
   ```
   [~DeviceA] ospf valid-ttl-hops 1
   [*DeviceA] commit
   ```
   
   # Set the valid TTL range in packets from DeviceB to DeviceC to [254, 255].
   
   ```
   [~DeviceB] ospf valid-ttl-hops 2
   [*DeviceB] commit
   ```
   
   # Set the valid TTL range in packets from DeviceD to DeviceC to [253, 255].
   
   ```
   [~DeviceD] ospf valid-ttl-hops 3
   [*DeviceD] commit
   ```
   
   # Set the valid TTL range in packets from DeviceE to DeviceC to [255, 255].
   
   ```
   [~DeviceE] ospf valid-ttl-hops 1
   [*DeviceE] commit
   ```
   
   # Set the valid TTL range in packets from DeviceF to DeviceC to [252, 255].
   
   ```
   [~DeviceF] ospf valid-ttl-hops 4
   [*DeviceF] commit
   ```

#### Verifying the Configuration

# Check whether the OSPF neighbor relationships are established properly between the devices. The following uses the command output on DeviceA as an example. The command output shows that the status of each neighbor relationship is Full, that is, the neighbor relationships are established properly.

```
[~DeviceA] display ospf peer
          OSPF Process 1 with Router ID 1.1.1.1
                  Neighbors

 Area 0.0.0.0 interface 192.168.0.1(100GE1/0/1)'s neighbors
 Router ID: 2.2.2.2      Address: 192.168.0.2
 State: Full  Mode:Nbr is  Master  Priority: 1
   DR: None   BDR: None   MTU: 0
   Dead timer due in 36  sec
   Retrans timer interval: 5
   Neighbor is up for 00:15:04
   Authentication Sequence: [ 0 ]

                  Neighbors

 Area 0.0.0.1 interface 192.168.1.1(100GE1/0/2)'s neighbors
 Router ID: 3.3.3.3       Address: 192.168.1.2
 State: Full  Mode:Nbr is  Master  Priority: 1
   DR: None   BDR: None   MTU: 0
   Dead timer due in 39  sec
   Retrans timer interval: 5
   Neighbor is up for 00:07:32
   Authentication Sequence: [ 0 ]
```

# Run the **display gtsm statistics all** command on DeviceC to check GTSM statistics. If the default action taken on packets that do not match the specified GTSM policy is set to pass and all the packets are valid, no packet is dropped.

```
[~DeviceC] display gtsm statistics all
GTSM Statistics Table
----------------------------------------------------------------
SlotId  Protocol  Total Counters  Drop Counters  Pass Counters
----------------------------------------------------------------
 1      BGP       0               0              0
 1      BGPv6     0               0              0
 1      OSPF      0               0              0
 1      OSPFv3    0               0              0 
 1      RIP       0               0              0 
----------------------------------------------------------------
```

If the host PC simulates the OSPF packets of DeviceA to attack DeviceC, the packets are dropped when they reach DeviceC because the TTL value is not 255. As a result, in the GTSM statistics on DeviceC, the number of dropped packets also increases.


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
   ip address 192.168.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.0.0 0.0.0.255
   area 0.0.0.1
    network 192.168.1.0 0.0.0.255
  #
  ospf valid-ttl-hops 1
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
   ip address 192.168.2.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.0.0 0.0.0.255
   area 0.0.0.2
    network 192.168.2.0 0.0.0.255
  #
  ospf valid-ttl-hops 2
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
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.1
    network 192.168.1.0 0.0.0.255
    network 172.16.1.0 0.0.0.255
  #
  ospf valid-ttl-hops 4
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  router id 4.4.4.4
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.17.1.1 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.2
    network 192.168.2.0 0.0.0.255
    network 172.17.1.0 0.0.0.255
  #
  ospf valid-ttl-hops 3
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  router id 5.5.5.5
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.1
    network 172.16.1.0 0.0.0.255
  #
  ospf valid-ttl-hops 1
  #
  return
  ```
* DeviceF
  
  ```
  #
  sysname DeviceF
  #
  router id 6.6.6.6
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.17.1.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.2
    network 172.17.1.0 0.0.0.255
  #
  ospf valid-ttl-hops 4
  #
  return
  ```