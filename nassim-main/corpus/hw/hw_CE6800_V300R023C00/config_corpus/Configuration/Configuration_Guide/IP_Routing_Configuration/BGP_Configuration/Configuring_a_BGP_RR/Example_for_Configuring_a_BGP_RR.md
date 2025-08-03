Example for Configuring a BGP RR
================================

Example for Configuring a BGP RR

#### Networking Requirements

On a large-scale network, multiple BGP-enabled devices exist in an AS and need to use BGP to exchange routes. In this case, IBGP peer relationships need to be established between all devices. Establishing full-mesh logical relationships between all devices, however, imposes a heavy configuration burden and increases the link cost on devices. In addition, the full-mesh logical connections are difficult to maintain. Customers require to simplify network configuration, reduce the overhead on devices, and ensure efficient route advertisement.

The use of RRs meets all these requirements. As shown in [Figure 1](#EN-US_TASK_0000001130624156__fig_dc_vrp_bgp_cfg_407501), in AS 65010, the AS is divided into two clusters, Cluster 1 and Cluster 2. DeviceB is configured as the RR of Cluster 1, and DeviceD and DeviceE are two clients in Cluster 1. DeviceC is configured as an RR in Cluster 2, and DeviceF, DeviceG, and DeviceH are clients in Cluster 2. DeviceA is the non-client of DeviceB and DeviceC. DeviceB and DeviceC are non-clients of each other. It is required that peer groups be configured to facilitate configuration and management.

**Figure 1** Network diagram of configuring a BGP RR![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, and interface 5 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, 100GE1/0/4, and 100GE1/0/5, respectively.


  
![](figure/en-us_image_0000001130624228.png "Click to enlarge")

#### Precautions

During the configuration, note the following:

* If a cluster has multiple RRs, run the **reflector cluster-id** command to set the same cluster ID for these RRs to prevent routing loops.
* When referencing a peer group, note that the peer group name is case sensitive.
* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Authentication." Keychain authentication is used as an example. For details, see Example for Configuring Keychain Authentication for BGP.

#### Procedure

1. Assign an IP address to each involved interface. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130624156__postreq17364171716277).
2. Configure an IBGP connection between an RR and each of clients and non-clients in each cluster. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130624156__postreq17364171716277).
3. Configure RRs.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 65010
   [*DeviceB-bgp] router-id 2.2.2.2
   [*DeviceB-bgp] group in_rr internal
   [*DeviceB-bgp] peer 10.1.4.2 group in_rr
   [*DeviceB-bgp] peer 10.1.5.2 group in_rr
   [*DeviceB-bgp] ipv4-family unicast
   [*DeviceB-bgp-af-ipv4] peer in_rr reflect-client
   [*DeviceB-bgp-af-ipv4] undo reflect between-clients
   [*DeviceB-bgp-af-ipv4] reflector cluster-id 1
   [*DeviceB-bgp-af-ipv4] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 65010
   [*DeviceC-bgp] router-id 3.3.3.3
   [*DeviceC-bgp] group in_rr internal
   [*DeviceC-bgp] peer 10.1.7.2 group in_rr 
   [*DeviceC-bgp] peer 10.1.8.2 group in_rr
   [*DeviceC-bgp] peer 10.1.9.2 group in_rr
   [*DeviceC-bgp] ipv4-family unicast
   [*DeviceC-bgp-af-ipv4] peer in_rr reflect-client
   [*DeviceC-bgp-af-ipv4] reflector cluster-id 2
   [*DeviceC-bgp-af-ipv4] quit
   [*DeviceC-bgp] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Check the routing table of DeviceD.

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

The preceding command output shows that DeviceD has learned from DeviceB the route advertised by DeviceA. The Originator and Cluster\_ID attributes of this route are displayed.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  bgp 65010
   router-id 1.1.1.1
   peer 10.1.1.1 as-number 65010
   peer 10.1.3.1 as-number 65010
   #
   ipv4-family unicast
    undo synchronization 
    network 172.16.1.0 255.255.255.0
    peer 10.1.1.1 enable
    peer 10.1.3.1 enable
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
   ip address 10.1.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.4.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.5.1 255.255.255.0
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #
  bgp 65010
   router-id 2.2.2.2
   peer 10.1.1.2 as-number 65010
   peer 10.1.2.2 as-number 65010
   group in_rr internal
   peer 10.1.4.2 as-number 65010
   peer 10.1.4.2 group in_rr
   peer 10.1.5.2 as-number 65010
   peer 10.1.5.2 group in_rr
   #
   ipv4-family unicast
    undo synchronization 
    undo reflect between-clients
    reflector cluster-id 1
    peer 10.1.1.2 enable
    peer 10.1.2.2 enable
    peer in_rr enable
    peer in_rr reflect-client
    peer 10.1.4.2 enable
    peer 10.1.4.2 group in_rr
    peer 10.1.5.2 enable
    peer 10.1.5.2 group in_rr  
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
   ip address 10.1.2.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.7.1 255.255.255.0
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.1.8.1 255.255.255.0
  #
  interface 100GE1/0/5
   undo portswitch
   ip address 10.1.9.1 255.255.255.0
  #
  bgp 65010
   router-id 3.3.3.3
   peer 10.1.2.1 as-number 65010
   peer 10.1.3.2 as-number 65010
   group in_rr internal
   peer 10.1.7.2 as-number 65010
   peer 10.1.7.2 group in_rr
   peer 10.1.8.2 as-number 65010
   peer 10.1.8.2 group in_rr
   peer 10.1.9.2 as-number 65010
   peer 10.1.9.2 group in_rr
   #
   ipv4-family unicast
    undo synchronization 
    reflector cluster-id 2
    peer 10.1.2.1 enable
    peer 10.1.3.2 enable
    peer in_rr enable
    peer in_rr reflect-client
    peer 10.1.7.2 enable
    peer 10.1.7.2 group in_rr
    peer 10.1.8.2 enable
    peer 10.1.8.2 group in_rr
    peer 10.1.9.2 enable
    peer 10.1.9.2 group in_rr
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
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.6.1 255.255.255.0
  #
  bgp 65010
   router-id 4.4.4.4
   peer 10.1.4.1 as-number 65010
   peer 10.1.6.2 as-number 65010
   #
   ipv4-family unicast
    undo synchronization 
    peer 10.1.4.1 enable
    peer 10.1.6.2 enable
  #
  return
  ```

![](public_sys-resources/note_3.0-en-us.png) 

The configuration scripts of other devices are similar to the configuration script of DeviceD.