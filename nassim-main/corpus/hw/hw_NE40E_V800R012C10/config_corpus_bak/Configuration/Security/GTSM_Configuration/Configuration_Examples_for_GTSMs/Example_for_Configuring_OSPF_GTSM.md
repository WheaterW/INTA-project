Example for Configuring OSPF GTSM
=================================

This section provides an example for configuring OSPF GTSM in order to protect devices on an OSPF network against CPU utilization attacks.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372052__fig_dc_vrp_gtsm_cfg_001001), OSPF runs between Routers, and GTSM needs to be enabled on DeviceC.

According to the network diagram, the valid TTL ranges of the packets sent from the Routers to DeviceC are as follows:

* For packets sent from neighbors DeviceA and DeviceE to DeviceC, the valid TTL range is [255, 255].
* For packets sent from DeviceB, DeviceD, and DeviceF to DeviceC, the valid TTL ranges are [254, 255], [253, 255], and [252, 255], respectively.

**Figure 1** Network diagram of configuring OSPF GTSM![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_gtsm_cfg_001001.png)  


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions.
2. Enable GTSM on each Router and specify valid TTL ranges.

#### Data Preparation

To complete the configuration, you need the following data:

* OSPF process ID of each Router
* Valid TTL range for packets transmitted between the Routers

#### Procedure

1. Configure IP addresses for interfaces. For detailed configurations, see Configuration Files.
2. Configure basic OSPF functions. For detailed configurations, see Configuration Files.
3. Configure OSPF GTSM.
   
   
   
   # Set the valid TTL range of packets sent from DeviceC to other Routers to [252, 255].
   
   ```
   [~DeviceC] ospf valid-ttl-hops 4
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Set the valid TTL range of packets sent from DeviceA to DeviceC to [255, 255].
   
   ```
   [~DeviceA] ospf valid-ttl-hops 1
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Set the valid TTL range of packets sent from DeviceB to DeviceC to [254, 255].
   
   ```
   [~DeviceB] ospf valid-ttl-hops 2
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Set the valid TTL range of packets sent from DeviceD to DeviceC to [253, 255].
   
   ```
   [~DeviceD] ospf valid-ttl-hops 3
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Set the valid TTL range of packets sent from DeviceE to DeviceC to [255, 255].
   
   ```
   [~DeviceE] ospf valid-ttl-hops 1
   ```
   ```
   [*DeviceE] commit
   ```
   
   # Set the valid TTL range of packets sent from DeviceF to DeviceC to [252, 255].
   
   ```
   [~DeviceF] ospf valid-ttl-hops 4
   ```
   ```
   [*DeviceF] commit
   ```
4. Verify the configuration.
   
   
   
   # Check whether OSPF neighbor relationships are properly established between the Routers. Take DeviceA as an example. The value of **State** in the command output is **Full**, indicating that the neighbor relationship has been properly established.
   
   ```
   [~DeviceA] display ospf peer
   ```
   ```
             OSPF Process 1 with Router ID 1.1.1.1
   ```
   ```
                     Neighbors
   ```
   ```
    Area 0.0.0.0 interface 192.168.0.1(GigabitEthernet0/1/0)'s neighbors
   ```
   ```
   Router ID: 2.2.2.2      Address: 192.168.0.2
   ```
   ```
   State: Full  Mode:Nbr is  Master  Priority: 1
   ```
   ```
      DR: None   BDR: None   MTU: 0
   ```
   ```
      Dead timer due in 36  sec
   ```
   ```
      Retrans timer interval: 5
   ```
   ```
      Neighbor is up for 00:15:04
   ```
   ```
      Authentication Sequence: [ 0 ]
   ```
   ```
                     Neighbors
   ```
   ```
    Area 0.0.0.1 interface 192.168.1.1(GigabitEthernet0/2/0)'s neighbors
   ```
   ```
   Router ID: 3.3.3.3       Address: 192.168.1.2
   ```
   ```
   State: Full  Mode:Nbr is  Master  Priority: 1
   ```
   ```
      DR: None   BDR: None   MTU: 0
   ```
   ```
      Dead timer due in 39  sec
   ```
   ```
      Retrans timer interval: 5
   ```
   ```
      Neighbor is up for 00:07:32
   ```
   ```
      Authentication Sequence: [ 0 ]
   ```
   
   # Run the **display gtsm statistics all** command on DeviceC to check GTSM statistics. If the default action is set to pass for the packets that do not match the specified GTSM policy and no invalid packets exist, the number of dropped packets is 0.
   
   ```
   <DeviceC> display gtsm statistics all
   ```
   ```
   GTSM Statistics Table
   ```
   ```
   ----------------------------------------------------------------
   ```
   ```
   SlotId  Protocol  Total Counters  Drop Counters  Pass Counters
   ```
   ```
   ----------------------------------------------------------------
   ```
   ```
    1      BGP       0               0              0
    1      BGPv6     0               0              0
    1      OSPF      0               0              0
    1      LDP       0               0              0
    1      OSPFv3    0               0              0 
    1      RIP       0               0              0 
    2      BGP       0               0              0
    2      BGPv6     0               0              0
    2      OSPF      0               0              0
    2      LDP       0               0              0
    2      OSPFv3    0               0              0 
    2      RIP       0               0              0 
    3      BGP       0               0              0
    3      BGPv6     0               0              0
    3      OSPF      0               0              0
    3      LDP       0               0              0
    3      OSPFv3    0               0              0 
    3      RIP       0               0              0 
    4      BGP       0               0              0
    4      BGPv6     0               0              0
    4      OSPF      0               0              0
    4      LDP       0               0              0
    4      OSPFv3    0               0              0 
    4      RIP       0               0              0 
    5      BGP       0               0              0
    5      BGPv6     0               0              0
    5      OSPF      0               0              0
    5      LDP       0               0              0
    5      OSPFv3    0               0              0 
    5      RIP       0               0              0 
    7      BGP       0               0              0
    7      BGPv6     0               0              0
    7      OSPF      0               0              0
    7      LDP       0               0              0
    7      OSPFv3    0               0              0 
    7      RIP       0               0              0 
   
   ```
   ```
   ----------------------------------------------------------------
   ```
   
   In this case, if the PC simulates the OSPF packets of DeviceA to attack DeviceC, the packets are dropped when they reach DeviceC. This is because the TTL value is not 255. As a result, the number of dropped packets increases in the GTSM statistics about DeviceC.

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
  ip address 192.168.0.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
  ip address 192.168.1.1 255.255.255.0
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
    network 192.168.0.0 0.0.0.255
  ```
  ```
   area 0.0.0.1
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ospf valid-ttl-hops 1
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
   ip address 192.168.0.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
  ip address 192.168.2.1 255.255.255.0
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
    network 192.168.0.0 0.0.0.255
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ospf valid-ttl-hops 2
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
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.1 255.255.255.0
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
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.1
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    network 172.16.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ospf valid-ttl-hops 4
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
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.17.1.1 255.255.255.0
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
  ip address 192.168.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 172.17.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ospf valid-ttl-hops 3
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceE configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceE
  ```
  ```
  #
  ```
  ```
  router id 5.5.5.5
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.1
  ```
  ```
    network 172.16.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ospf valid-ttl-hops 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceF configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceF
  ```
  ```
  #
  ```
  ```
  router id 6.6.6.6
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.17.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 172.17.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ospf valid-ttl-hops 4
  ```
  ```
  #
  ```
  ```
  return
  ```