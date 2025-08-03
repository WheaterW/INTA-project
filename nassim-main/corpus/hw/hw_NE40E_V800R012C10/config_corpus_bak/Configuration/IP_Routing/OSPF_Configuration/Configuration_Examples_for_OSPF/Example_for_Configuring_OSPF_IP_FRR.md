Example for Configuring OSPF IP FRR
===================================

This section describes how to configure OSPF IP FRR with an example, including how to block FRR on certain interfaces to prevent the links connected to these interfaces from functioning as backup links and how to bind OSPF IP FRR to a BFD session.

#### Networking Requirements

When a fault occurs on the primary link T, traffic is switched to a backup link. In such a scenario, two problems arise:

* It takes hundreds of milliseconds for the traffic to be switched to a backup link. During this period, services are interrupted.
* Traffic may be switched to the link that passes through DeviceA. DeviceA is an ASBR and is not expected to function as a backup device.

If a fault occurs on the network, OSPF IP FRR can fast switch traffic to the backup link without waiting for route convergence. This ensures uninterrupted traffic transmission. In addition, you can also prevent the link which passes through DeviceA from functioning as the FRR backup link.

On the network shown in [Figure 1](#EN-US_TASK_0172365668__fig_dc_vrp_ospf_cfg_200801):

* All Routers run OSPF.
* The link cost meets the OSPF IP FRR traffic protection inequality.
* If the primary link T fails, Device S immediately switches traffic to the backup link which passes through DeviceN.
* Based on the network planning, the link which passes through DeviceA does not function as an FRR backup link.

**Figure 1** Networking for configuring OSPF IP FRR![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GE 0/1/0, GE 0/2/0, GE 0/3/0, and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_ospf_cfg_200801.png)

#### Precautions

During the configuration, pay attention to the following points:

* Before configuring OSPF IP FRR, block FRR on certain interfaces to prevent the links connected to these interfaces from functioning as backup links. After that, the link where the interface resides is not calculated as a backup link during FRR calculation.
* During the configuration of OSPF IP FRR, the lower layer needs to fast respond to a link change so that traffic can be rapidly switched to the backup link. After the [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) **frr-binding** command is run, the BFD session status is bound to the link status of the interface (when the BFD session goes down, the link status of the interface also goes down). In this manner, faults can be rapidly detected.
* To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security". OSPF area authentication is used as an example. For details, see Example for Configuring Basic OSPF Functions.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions on each Router.
2. Configure BFD for OSPF on all the devices in Area 0.
3. Set the costs of links to ensure that link T is selected to transmit traffic.
4. Block FRR on a specified interface of DeviceS.
5. Enable OSPF IP FRR on DeviceS to protect the traffic forwarded by DeviceS.


#### Data Preparation

To complete the configuration, you need the following data:

| Device | Router ID | Interface | IP Address |
| --- | --- | --- | --- |
| DeviceS | 1.1.1.1 | GE0/1/0 | 10.1.1.1/24 |
| GE0/2/0 | 10.1.2.1/24 |
| GE0/3/0 | 10.1.3.1/24 |
| DeviceA | 2.2.2.2 | GE0/1/0 | 10.1.1.2/24 |
| GE0/2/0 | 10.2.1.2/24 |
| DeviceN | 3.3.3.3 | GE0/1/0 | 10.1.3.2/24 |
| GE0/2/0 | 10.2.3.2/24 |
| DeviceE | 4.4.4.4 | GE0/1/0 | 10.2.1.1/24 |
| GE0/2/0 | 10.1.2.2/24 |
| GE0/3/0 | 10.2.3.1/24 |
| GE0/1/1 | 172.17.1.1/24 |



#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365668__section_dc_vrp_ospf_cfg_200806) in this section.
2. Configure basic OSPF functions. For details, see [Example for Configuring Basic OSPF Functions](dc_vrp_ospf_cfg_0094.html).
3. Configure BFD for OSPF on all the devices in Area 0. For details, see [Example for Configuring BFD for OSPF](dc_vrp_ospf_cfg_0102.html).
4. Set the costs of links to ensure that link T is selected to transmit traffic.
   
   
   
   # Configure DeviceS.
   
   ```
   [~DeviceS] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceS-GigabitEthernet0/1/0] ospf cost 10
   ```
   ```
   [*DeviceS-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceS] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceS-GigabitEthernet0/2/0] ospf cost 15
   ```
   ```
   [*DeviceS-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceS] interface gigabitethernet0/3/0
   ```
   ```
   [*DeviceS-GigabitEthernet0/3/0] ospf cost 10
   ```
   ```
   [*DeviceS-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceS] commit
   ```
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ospf cost 15
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   
   
   # Configure DeviceN.
   
   ```
   [~DeviceN] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceN-GigabitEthernet0/2/0] ospf cost 10
   ```
   ```
   [*DeviceN-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceN] commit
   ```
5. Block FRR on a specified interface of DeviceS.
   
   
   ```
   [~DeviceS] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceS-GigabitEthernet0/1/0] ospf frr block
   ```
   ```
   [*DeviceS-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceS] commit
   ```
6. Enable OSPF IP FRR on DeviceS.
   
   
   
   # Enable OSPF IP FRR on DeviceS.
   
   ```
   [~DeviceS] ospf
   ```
   ```
   [*DeviceS-ospf-1] frr
   ```
   ```
   [*DeviceS-ospf-1-frr] loop-free-alternate
   ```
   ```
   [*DeviceS-ospf-1-frr] commit
   ```
7. Verify the configuration.
   
   
   
   # Run the **display ospf routing router-id** command on DeviceS to view routing information.
   
   ```
   [~DeviceS-ospf-1-frr] display ospf routing router-id 4.4.4.4
   ```
   ```
             OSPF Process 1 with Router ID 1.1.1.1
   
    Destination :    4.4.4.4             Route Type :       Intra-area
    Area        :    0.0.0.1             AdvRouter  :       4.4.4.4
    Type        :    ASBR                
    URT Cost    :    59
    NextHop     :    10.1.2.2            Interface  :       GE0/2/0
    Backup Nexthop : 10.1.3.2         Backup Interface : GE0/3/0  Backup Type : LFA LINK 
    BakLabelStack : {48092,48092}       
   ```
   
   The preceding display shows that a backup route is generated on DeviceS.

#### Configuration Files

* Device S configuration file
  
  ```
  #
  sysname DeviceS
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.1.1 255.255.255.0
   ospf frr block
   ospf cost 10
  #
  interface GigabitEthernet0/2/0
   ip address 10.1.2.1 255.255.255.0
   ospf cost 15
  #
  interface GigabitEthernet0/3/0
   ip address 10.1.3.1 255.255.255.0
   ospf cost 10
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 1 router-id 1.1.1.1
   bfd all-interfaces enable
   bfd all-interfaces frr-binding
   frr
    loop-free-alternate
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  return
  ```
* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #  
  bfd
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.1.2 255.255.255.0
   ospf cost 10
  #
  interface GigabitEthernet0/2/0
   ip address 10.2.1.2 255.255.255.0
   ospf cost 15
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1 router-id 2.2.2.2
   bfd all-interfaces enable
   bfd all-interfaces frr-binding
   frr
    loop-free-alternate
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.2.0 0.0.0.255
  #
  return
  ```
* DeviceN configuration file
  
  ```
  #
  sysname DeviceN
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.3.2 255.255.255.0
   ospf cost 10
  #
  interface GigabitEthernet0/2/0
   ip address 10.2.3.2 255.255.255.0
   ospf cost 10
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1 router-id 3.3.3.3
   bfd all-interfaces enable
   bfd all-interfaces frr-binding
   frr
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 10.2.3.0 0.0.0.255
  #
  return
  ```
* DeviceE configuration file
  
  ```
  #
  sysname DeviceE
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   ip address 10.2.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   ip address 10.1.2.2 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   ip address 10.2.3.1 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   ip address 172.17.1.1 255.255.255.0
   ospf cost 5
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  ospf 1 router-id 4.4.4.4
   bfd all-interfaces enable
   bfd all-interfaces frr-binding
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
    network 172.17.1.0 0.0.0.255
  #
  return
  ```