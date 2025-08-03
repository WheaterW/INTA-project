Example for Configuring BGP RRs
===============================

With BGP RRs, IBGP peers do not have to be fully meshed, which reduces configuration workload and facilitates network maintenance.

#### Networking Requirements

On a large-scale network, multiple Routers that run BGP are deployed within an AS. These Routers need to use BGP to advertise routes to each other. To meet this need, IBGP peer relationships need to be set up between all the Routers. However, fully meshed connections between all Routers increase Router costs and the configuration workload and are difficult to maintain. A solution that can simplify network configuration and reduce Router costs without affecting route transmission is required.

To address this issue, configure RRs. In [Figure 1](#EN-US_TASK_0172366373__fig_dc_vrp_bgp_cfg_407501), AS 65010 is divided into two clusters: Cluster 1 and Cluster 2. DeviceB is configured as an RR in Cluster 1, and DeviceD and DeviceE are its clients. DeviceC is configured as an RR in Cluster 2, and DeviceF, DeviceG, and DeviceH are its clients. DeviceA is the non-client of DeviceB and DeviceC. DeviceB and DeviceC are non-clients of each other.

**Figure 1** Configuring BGP RRs![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 5 in this example represent GE 0/1/0, GE 0/2/0, GE 0/3/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_407501.png)  

**Table 1** IP addresses of the interfaces
| Device | Interface | IP Address | Device | Interface | IP Address |
| --- | --- | --- | --- | --- | --- |
| Device A | GE 0/3/0 | 172.16.1.1/24 | Device C | GE 0/1/1 | 10.1.8.1/24 |
| GE 0/1/0 | 10.1.1.2/24 | GE 0/1/2 | 10.1.9.1/24 |
| GE 0/2/0 | 10.1.3.2/24 | Device D | GE 0/1/0 | 10.1.4.2/24 |
| Device B | GE 0/1/0 | 10.1.1.1/24 | GE 0/2/0 | 10.1.6.1/24 |
| GE 0/2/0 | 10.1.4.1/24 | Device E | GE 0/2/0 | 10.1.6.2/24 |
| GE 0/3/0 | 10.1.5.1/24 | GE 0/3/0 | 10.1.5.2/24 |
| GE 0/1/1 | 10.1.2.1/24 | Device F | GE 0/1/0 | 10.1.7.2/24 |
| Device C | GE 0/1/0 | 10.1.2.2/24 | Device G | GE 0/1/0 | 10.1.8.2/24 |
| GE 0/2/0 | 10.1.3.1/24 | Device H | GE 0/2/0 | 10.1.9.2/24 |
| GE 0/3/0 | 10.1.7.1/24 |



#### Precautions

When configuring a BGP RR, note the following rules:

* If a cluster has multiple RRs, run the **reflector cluster-id** command to set the same cluster ID for these RRs to prevent routing loops.
* The name of a peer group is case sensitive.
* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IBGP connections between the clients and the RR, and between the non-client and the RR.
2. Configure Device B and Device C as RRs, specify their clients, and check routes.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs and AS numbers of Device A, Device B, Device C, Device D, Device E, Device F, Device G, and Device H
* Cluster ID of Device B

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366373__section_dc_vrp_bgp_cfg_407505) in this section.
2. Configure IBGP connections between the clients and the RR, and between the non-client and the RR.
3. Configure RRs.
   
   
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 65010
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] group in_rr internal
   ```
   ```
   [*DeviceB-bgp] peer 10.1.4.2 group in_rr
   ```
   ```
   [*DeviceB-bgp] peer 10.1.5.2 group in_rr
   ```
   ```
   [*DeviceB-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv4] peer in_rr reflect-client
   ```
   ```
   [*DeviceB-bgp-af-ipv4] undo reflect between-clients
   ```
   ```
   [*DeviceB-bgp-af-ipv4] reflector cluster-id 1
   ```
   ```
   [*DeviceB-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv4] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] bgp 65010
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-bgp] group in_rr internal
   ```
   ```
   [*DeviceC-bgp] peer 10.1.7.2 group in_rr 
   ```
   ```
   [*DeviceC-bgp] peer 10.1.8.2 group in_rr
   ```
   ```
   [*DeviceC-bgp] peer 10.1.9.2 group in_rr
   ```
   ```
   [*DeviceC-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv4] peer in_rr reflect-client
   ```
   ```
   [*DeviceC-bgp-af-ipv4] reflector cluster-id 2
   ```
   ```
   [*DeviceC-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceC-bgp-af-ipv4] quit
   ```
   
   # Check the routing table of Device D.
   
   ```
   [~DeviceD] display bgp routing-table 172.16.1.0
   
   BGP local router ID : 4.4.4.4
    Local AS number : 65010
    Paths:   1 available, 0 best, 0 select
    BGP routing table entry information of 172.16.1.0/24:
    From: 10.1.4.1 (2.2.2.2)
    Route Duration: 00h00m14s
    Relay IP Nexthop: 0.0.0.0
    Relay IP Out-Interface:
    Original nexthop: 10.1.1.2
    Qos information : 0x0
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, internal, pre 255
    Originator:  1.1.1.1
    Cluster list: 0.0.0.1
    Not advertised to any peer yet
   ```
   
   The command output shows that Device D has learned from Device B the route advertised by Device A and that the Originator and Cluster\_ID attributes of this route are displayed.

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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
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
   ip address 10.1.3.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
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
  bgp 65010
  ```
  ```
   router-id 1.1.1.1
  ```
  ```
   peer 10.1.1.1 as-number 65010
  ```
  ```
   peer 10.1.3.1 as-number 65010
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    network 172.16.1.0 255.255.255.0
  ```
  ```
    peer 10.1.1.1 enable
  ```
  ```
    peer 10.1.3.1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
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
   ip address 10.1.1.1 255.255.255.0
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
   ip address 10.1.4.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.5.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65010
  ```
  ```
   router-id 2.2.2.2
  ```
  ```
   peer 10.1.1.2 as-number 65010
  ```
  ```
   peer 10.1.2.2 as-number 65010
  ```
  ```
   group in_rr internal
  ```
  ```
   peer 10.1.4.2 as-number 65010
  ```
  ```
   peer 10.1.4.2 group in_rr
  ```
  ```
   peer 10.1.5.2 as-number 65010
  ```
  ```
   peer 10.1.5.2 group in_rr
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    undo reflect between-clients
  ```
  ```
    reflector cluster-id 1
  ```
  ```
    peer 10.1.1.2 enable
  ```
  ```
    peer 10.1.2.2 enable
  ```
  ```
    peer in_rr enable
  ```
  ```
    peer in_rr reflect-client
  ```
  ```
    peer 10.1.4.2 enable
  ```
  ```
    peer 10.1.4.2 group in_rr
  ```
  ```
    peer 10.1.5.2 enable
  ```
  ```
    peer 10.1.5.2 group in_rr  
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device C configuration file
  
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
   ip address 10.1.2.2 255.255.255.0
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
   ip address 10.1.3.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.7.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.8.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.9.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65010
  ```
  ```
   router-id 3.3.3.3
  ```
  ```
   peer 10.1.2.1 as-number 65010
  ```
  ```
   peer 10.1.3.2 as-number 65010
  ```
  ```
   group in_rr internal
  ```
  ```
   peer 10.1.7.2 as-number 65010
  ```
  ```
   peer 10.1.7.2 group in_rr
  ```
  ```
   peer 10.1.8.2 as-number 65010
  ```
  ```
   peer 10.1.8.2 group in_rr
  ```
  ```
   peer 10.1.9.2 as-number 65010
  ```
  ```
   peer 10.1.9.2 group in_rr
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    reflector cluster-id 2
  ```
  ```
    peer 10.1.2.1 enable
  ```
  ```
    peer 10.1.3.2 enable
  ```
  ```
    peer in_rr enable
  ```
  ```
    peer in_rr reflect-client
  ```
  ```
    peer 10.1.7.2 enable
  ```
  ```
    peer 10.1.7.2 group in_rr
  ```
  ```
    peer 10.1.8.2 enable
  ```
  ```
    peer 10.1.8.2 group in_rr
  ```
  ```
    peer 10.1.9.2 enable
  ```
  ```
    peer 10.1.9.2 group in_rr
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device D configuration file
  
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
   ip address 10.1.4.2 255.255.255.0
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
   ip address 10.1.6.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65010
  ```
  ```
   router-id 4.4.4.4
  ```
  ```
   peer 10.1.4.1 as-number 65010
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 10.1.4.1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Configuration files of other Routers are similar to the Device D configuration file.