Example for Configuring BGP RPD
===============================

BGP RPD ensures that route-policies are distributed dynamically.

#### Networking Requirements

In a MAN ingress or IGW scenario, uneven link resource utilization or link faults may cause link congestion. To fully use network bandwidth, you can deploy an inbound traffic optimization solution to adjust route priorities so that traffic is diverted to idle links. In such a scenario, the Router functions as a forwarder, and RPD needs to be deployed on it.

In [Figure 1](#EN-US_TASK_0172366415__fig_dc_vrp_bgp_cfg_410501), BGP runs on all Routers. Router A and Router B reside in AS 100, Router C in AS 200, and the controller in AS 300. The traffic that Device C in AS 200 sends to the destination IP address 192.168.1.0 can enter AS 100 through Router A or Router B. However, the controller finds that the link between Router A and Router C is congested. In this case, a traffic optimization policy can be configured so that an RPD route is delivered to divert the traffic to Router B when the traffic enters AS 100.

**Figure 1** Network diagram of configuring BGP RPD![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example stand for GE 0/1/0 and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_410501.png)  


#### Precautions

To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure EBGP connections between Device A and Device C, and between Device B and Device C.
2. On Device A and Device B, enable RPD and establish RPD peer relationships with the controller.
3. Configure IPv4 unicast on Device A, Device B, and Device C so that IPv4 unicast peer relationships are established between Device A and Device C, and between Device B and Device C.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section provides only the configurations and procedures for forwarders. The controller's configurations, such as the BGP, RPD address family, and traffic optimization policy configurations, are not provided here.



#### Data Preparation

To complete the configuration, you need the following data:

* Router ID (4.1.1.1) of Device A, router ID (2.2.2.2) of Device B, and their AS number 100
* Router ID 3.3.3.3 of Device C and its AS number 200

#### Procedure

1. Assign an IP address to each interface. For configuration details, see Configuration Files in this section.
2. Configure BGP connections.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 10.2.1.2 as-number 200
   ```
   ```
   [*DeviceA-bgp] peer 1.1.1.1 as-number 300
   ```
   ```
   [*DeviceA-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv4] network 192.168.1.0 255.255.255.0
   ```
   ```
   [*DeviceA-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceA-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 10.3.1.2 as-number 200
   ```
   ```
   [*DeviceB-bgp] peer 2.1.1.1 as-number 300
   ```
   ```
   [*DeviceB-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv4] network 192.168.1.0 255.255.255.0
   ```
   ```
   [*DeviceB-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] bgp 200
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-bgp] peer 10.2.1.1 as-number 100
   ```
   ```
   [*DeviceC-bgp] peer 10.3.1.1 as-number 100
   ```
   ```
   [*DeviceC-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceC-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
   
   # Check the routing table of Device C.
   
   ```
   [~DeviceC] display bgp routing-table 192.168.1.0 24
   
    BGP local router ID : 3.3.3.3
    Local AS number : 200
    Paths:   2 available, 1 best, 1 select
    BGP routing table entry information of 192.168.1.0/24:
    From: 10.2.1.1 (1.1.1.1)
    Route Duration: 0d00h00m56s
    Direct Out-interface: GigabitEthernet0/1/0
    Original nexthop: 10.2.1.1
    Qos information : 0x0
    AS-path 100, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
    Advertised to such 2 peers:
       10.2.1.1
       10.3.1.1
   
    BGP routing table entry information of 192.168.1.0/24:
    From: 10.3.1.1 (2.2.2.2)
    Route Duration: 0d00h00m06s
    Direct Out-interface: GigabitEthernet0/1/1
    Original nexthop: 10.3.1.1
    Qos information : 0x0
    AS-path 100, origin igp, MED 0, pref-val 0, valid, external, pre 255, not preferred for router ID
    Not advertised to any peers yet
   ```
   
   The preceding command output shows that there are two valid routes to 192.168.1.0/24. The route with the next-hop address of 10.2.1.1 is the optimal route because the router ID of Device A is smaller. In this case, traffic enters AS 100 through Device A.
3. Configure BGP RPD functions on forwarders so that the forwarders receive RPD routes delivered by the controller and execute corresponding route-policies.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 1.1.1.1 as-number 300
   ```
   ```
   [*DeviceA-bgp] rpd-family
   ```
   ```
   [*DeviceA-bgp-af-rpd] peer 1.1.1.1 enable
   ```
   ```
   [*DeviceA-bgp-af-rpd] quit
   ```
   ```
   [*DeviceA-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv4] peer 10.2.1.2 rpd-policy export enable
   ```
   ```
   [*DeviceA-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceA-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] peer 2.1.1.1 as-number 300
   ```
   ```
   [*DeviceB-bgp] rpd-family
   ```
   ```
   [*DeviceB-bgp-af-rpd] peer 2.1.1.1 enable
   ```
   ```
   [*DeviceB-bgp-af-rpd] quit
   ```
   ```
   [*DeviceB-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv4] peer 10.3.1.2 rpd-policy export enable
   ```
   ```
   [*DeviceB-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   # Check information about RPD routes on Device A.
   ```
   [~DeviceA] display bgp rpd routing-table
   
    Total number of Routes : 1
    BGP Local router ID is 4.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
           Network                        Peer           MED        LocPrf    PrefVal Path/Ogn 
    *>     1/10.2.1.2/1                   1.1.1.1        50                   0       100?
   ```
   
   # Check the routing table of Device C.
   ```
   [~DeviceC] display bgp routing-table 192.168.1.0 24
   
    BGP local router ID : 3.3.3.3
    Local AS number : 200
    Paths:   2 available, 1 best, 1 select
    BGP routing table entry information of 192.168.1.0/24:
    From: 10.3.1.1 (2.2.2.2)
    Route Duration: 0d00h00m06s
    Direct Out-interface: GigabitEthernet1/0/1
    Original nexthop: 10.3.1.1
    Qos information : 0x0
    AS-path 100, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
    Advertised to such 2 peers:
       10.2.1.1
       10.3.1.1
   
    BGP routing table entry information of 192.168.1.0/24:
    From: 10.2.1.1 (1.1.1.1)
    Route Duration: 0d00h00m56s
    Direct Out-interface: GigabitEthernet1/0/0
    Original nexthop: 10.2.1.1
    Qos information : 0x0
    AS-path 100, origin igp, MED 50, pref-val 0, valid, external, pre 255, not preferred for MED
    Not advertised to any peers yet
   ```
   
   The preceding command output shows that the route with the next hop of 10.3.1.1 (Device B) is selected by Device C as the optimal route because its MED value 0 is smaller than that (50) of the route with the next hop of 10.2.1.1 (Device A). In this case, the traffic bypasses the congested link.

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
   ip address 10.2.1.1 255.255.255.0
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
   ip address 1.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   router-id 1.1.1.1
  ```
  ```
   peer 1.1.1.1 as-number 300
  ```
  ```
   peer 10.2.1.2 as-number 200
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    network 192.168.1.0 255.255.255.0
  ```
  ```
    peer 10.2.1.2 enable
  ```
  ```
    peer 10.2.1.2 rpd-policy export enable
  ```
  ```
   #
  ```
  ```
   rpd-family
  ```
  ```
    peer 1.1.1.1 enable
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
   ip address 10.3.1.1 255.255.255.0
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
   ip address 2.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   router-id 2.2.2.2
  ```
  ```
   peer 2.1.1.1 as-number 300
  ```
  ```
   peer 10.3.1.2 as-number 200
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    network 192.168.1.0 255.255.255.0
  ```
  ```
    peer 10.3.1.2 enable
  ```
  ```
    peer 10.3.1.2 rpd-policy export enable
  ```
  ```
   #
  ```
  ```
   rpd-family
  ```
  ```
    peer 2.1.1.1 enable
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
   ip address 10.2.1.2 255.255.255.0
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
   ip address 10.3.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 200
  ```
  ```
   router-id 3.3.3.3
  ```
  ```
   peer 10.2.1.1 as-number 100
  ```
  ```
   peer 10.3.1.1 as-number 100
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    peer 10.2.1.1 enable
  ```
  ```
    peer 10.3.1.1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```