Example for Configuring Routed Proxy ND
=======================================

This section provides an example for configuring routed proxy ND in a scenario where hosts are on the same network segment but different physical networks and the gateways connected to the hosts have different addresses.

#### Networking Requirements

If hosts that need to communicate are on the same network segment but different physical networks and the gateway connected to the hosts are configured with different IP addresses, enable routed proxy ND on the interfaces connecting the Router and hosts.

In [Figure 1](#EN-US_TASK_0172365191__fig_dc_vrp_nd_feature_002903), DeviceA and DeviceB are connected to different networks. Interface1 and Interface2, belonging to DeviceA and DeviceB, respectively, have different IPv6 addresses. HostA and HostB are used as an example. To communicate with HostB, HostA must first send an NS message to request HostB's MAC address because the destination IPv6 address is on the same network segment as the local IPv6 address. However, as HostA and HostB are located on different physical networks, HostB cannot receive the NS message and therefore does not respond. To solve this problem, enable routed proxy ND on DeviceA's Interface1 and DeviceB's Interface2.**Figure 1** Routed proxy ND![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_nd_feature_003710.png)  



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses for interfaces.
2. Configure an IGP to implement route reachability.
3. Enable routed proxy ND on interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 addresses of interfaces
* IPv6 addresses of hosts

#### Procedure

1. Configure IPv6 addresses for interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2001:db8:300:400::2 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ipv6 address 2001:db8:300:600::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ipv6 address 2001:db8:300:600::2 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] ipv6 address 2001:db8:300:500::2 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceB] commit
   ```
2. Configure an IGP to implement route reachability. OSPFv3 is used as an IGP in this example.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospfv3-1] area 0
   ```
   ```
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospfv3-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ospfv3 1 area 0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ospfv3 1 area 0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospfv3 1
   ```
   ```
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-ospfv3-1] area 0
   ```
   ```
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospfv3-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ospfv3 1 area 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] ospfv3 1 area 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceB] commit
   ```
3. Enable routed proxy ND on interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ipv6 nd proxy route enable 
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/2
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/2] ipv6 nd proxy route enable 
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceB] commit
   ```
4. Configure the IPv6 addresses of hosts.
   
   
   
   # Configure the IPv6 address of HostA as 2001:db8:300:400::1/48.
   
   # Configure the IPv6 address of HostB as 2001:db8:300:500::1/48.
5. Verify the configuration.
   
   
   
   After the configuration is complete, HostA and HostB can ping each other.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:300:400::2/64
   ospfv3 1 area 0.0.0.0
   ipv6 nd proxy route enable
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:300:600::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:300:600::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:300:500::2/64
   ospfv3 1 area 0.0.0.0
   ipv6 nd proxy route enable
  #
  return
  
  ```