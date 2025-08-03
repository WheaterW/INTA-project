Example for Configuring BGP Next Hop Recursion Based on a Routing Policy
========================================================================

Configuring BGP next hop recursion based on a routing policy prevents traffic loss in case of route changes.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172366394__fig_dc_vrp_bgp_cfg_308201), OSPF is used as the IGP in AS 100. An IBGP peer relationship is established between loopback0 interfaces of DeviceA and DeviceB, and between loopback0 interfaces of DeviceA and DeviceC. DeviceB and DeviceC advertise the BGP route 10.20.1.0/24 to DeviceA. Because the router ID of Device B is smaller, Device A chooses the route 10.20.1.0/24 that is learned from Device B as the optimal route, with the original next hop of 2.2.2.2/32.

In most cases, Device A recurses the next hop of the BGP route destined for 10.20.1.0/24 to an IGP route destined for 2.2.2.2/32 with GE0/1/0 as the outbound interface. When Device B is faulty, Device A deletes the IGP route destined for 2.2.2.2/32 immediately. However, Device A still considers the BGP route with 2.2.2.2/32 being the original next hop as the optimal route because it does not know the BGP route change before the BGP hold timer expires. Based on the longest matching rule, Device A mistakenly recurses the BGP route destined for 10.20.1.0/24 to the direct route destined for 2.2.2.10/24, with GE0/1/2 as the outbound interface, causing traffic loss.

**Figure 1** Networking diagram for configuring BGP next hop recursion based on a routing policy![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example are GE 0/1/0, GE 0/1/1, GE 0/1/2, Loopback0, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_308201.png)

To prevent traffic loss, configure BGP next hop recursion based on a routing policy on Device A to control the recursive routes. In this example, only the recursive routes with a mask length of 32 bits match the routing policy, and those that do not match the routing policy are considered unreachable. As such, when DeviceB is faulty, DeviceA can rapidly detect the route change and re-select a correct BGP route with the original next hop of 3.3.3.3/32, preventing traffic loss.


#### Precautions

When configuring BGP next hop recursion based on a routing policy, note the following:

* Ensure that all desirable recursive routes match the routing policy. Otherwise, BGP routes may be considered unreachable, unable to guide traffic forwarding.
* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF on Device A, Device B, and Device C to enable the devices in AS 100 to communicate with each other.
2. Establish an IBGP peer relationship between Loopback 0s of Device A and Device B, and between Loopback 0s of Device A and Device C.
3. Enable Device B and Device C to advertise a BGP route destined for 10.20.1.0/24 to Device A.
4. Configure BGP next hop recursion based on a routing policy on Device A. This configuration allows Device A to know the route change in time when Device B is faulty and re-select a correct BGP route, preventing traffic loss.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs of Device A, Device B, and Device C (1.1.1.1, 2.2.2.2, and 3.3.3.3, respectively) and AS number (100)
* Routing policy (**np-by-rp**) configured on Device A to control route recursion.

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration File](#EN-US_TASK_0172366394__section_dc_vrp_bgp_cfg_308206).
2. Configure OSPF in AS 100.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.0.0 0.0.255.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceA-ospf-1] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceB-ospf-1] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] area 0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceC-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceC-ospf-1] quit
   ```
3. Establish IBGP connections.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*DeviceA-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*DeviceA-bgp] peer 2.2.2.2 connect-interface LoopBack 0
   ```
   ```
   [*DeviceA-bgp] peer 3.3.3.3 connect-interface LoopBack 0
   ```
   ```
   [*DeviceA-bgp] commit
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
   [*DeviceB-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 1.1.1.1 connect-interface LoopBack 0
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*DeviceC-bgp] peer 1.1.1.1 connect-interface LoopBack 0
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
4. Enable Device B and Device C to advertise a BGP route destined for 10.20.1.0/24.
   
   
   
   # Configure Device B.
   
   ```
   [~DeviceB] ip route-static 10.20.1.0 24 NULL 0
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] import-route static
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] ip route-static 10.20.1.0 24 NULL 0
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] import-route static
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
5. Configure BGP next hop recursion based on a routing policy on Device A.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] ip ip-prefix np-by-rp-ip index 10 permit 0.0.0.0 32
   ```
   ```
   [*DeviceA] route-policy np-by-rp permit node 10
   ```
   ```
   [*DeviceA-route-policy] if-match ip-prefix np-by-rp-ip
   ```
   ```
   [*DeviceA-route-policy] quit
   ```
   ```
   [*DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] nexthop recursive-lookup route-policy np-by-rp
   ```
   ```
   [*DeviceA-bgp] quit
   ```
   ```
   [*DeviceA] commit
   ```
6. Verify the configuration.
   
   
   
   # Display detailed information about the BGP route destined for 10.20.1.0/24 on Device A when Device B is running properly.
   
   ```
   [~DeviceA] display bgp routing-table 10.20.1.0 24
   ```
   ```
    
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Paths:   2 available, 1 best, 1 select
    BGP routing table entry information of 10.20.1.0/24:
    From: 2.2.2.2 (2.2.2.2)  Route Duration: 0d00h00m36s
    Relay IP Nexthop: 10.1.1.2
    Relay IP Out-interface: GigabitEthernet0/1/0
    Original nexthop: 2.2.2.2
    Qos information : 0x0            
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Not advertised to any peer yet
   
    BGP routing table entry information of 10.20.1.0/24:
    From: 3.3.3.3 (3.3.3.3)  Route Duration: 0d02h53m45s
    Relay IP Nexthop: 10.1.2.2
    Relay IP Out-interface: GigabitEthernet0/1/1
    Original nexthop: 3.3.3.3
    Qos information : 0x0            
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, pre 255, not preferred for router ID
    Not advertised to any peers yet
   ```
   
   # Run the [**shutdown**](cmdqueryname=shutdown) command on GE 0/1/0 of Device B to simulate a fault on Device B.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   # Display detailed information about the BGP route destined for 10.20.1.0/24 on Device A.
   
   ```
   [~DeviceA] display bgp routing-table 10.20.1.0 24
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Paths:   2 available, 1 best, 1 select
    BGP routing table entry information of 10.20.1.0/24:
    From: 3.3.3.3 (3.3.3.3)  Route Duration: 0d03h10m58s
    Relay IP Nexthop: 10.1.2.2
    Relay IP Out-interface: GigabitEthernet0/1/1
    Original nexthop: 3.3.3.3
    Qos information : 0x0            
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Not advertised to any peer yet
   
    BGP routing table entry information of 10.20.1.0/24:
    From: 2.2.2.2 (2.2.2.2)  Route Duration: 0d00h00m50s
    Relay IP Nexthop: 0.0.0.0
    Relay IP Out-interface: 
    Original nexthop: 2.2.2.2
    Qos information : 0x0            
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, internal, pre 255
    Not advertised to any peers yet
   ```
   
   After DeviceB becomes faulty, the route which is destined for 10.20.1.0/24 and has the original next hop of 2.2.2.2/32 recurses to the direct route destined for 2.2.2.10/24. However, because the direct route destined for 2.2.2.10/24 is not a specific route with a 32-bit mask, this direct route does not match the route-policy **np-by-rp**. As a result, the recursive route is considered unreachable. Then, the correct route with 3.3.3.3/32 as the original next hop is selected by BGP.

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
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
  #               
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.2.1 255.255.255.0
  #          
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 2.2.2.10 255.255.255.0
  #               
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #              
   ipv4-family unicast
    undo synchronization
    nexthop recursive-lookup route-policy np-by-rp
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  #               
  ospf 1          
   area 0.0.0.0   
    network 1.1.1.1 0.0.0.0
    network 10.1.0.0 0.0.255.255
  #               
  ip ip-prefix np-by-rp-ip index 10 permit 0.0.0.0 32
  #               
  route-policy np-by-rp permit node 10
   if-match ip-prefix np-by-rp-ip
  #               
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
  interface GigabitEthernet0/1/0
   undo shutdown       
   ip address 10.1.1.2 255.255.255.0
  #               
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #              
   ipv4-family unicast
    undo synchronization
    import-route static
    peer 1.1.1.1 enable
  #               
  ospf 1          
   area 0.0.0.0   
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #               
  ip route-static 10.20.1.0 24 NULL 0
  #               
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
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.2.2 255.255.255.0
  #               
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #               
  bgp 100         
   router-id 3.3.3.3
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #              
   ipv4-family unicast
    undo synchronization
    import-route static
    peer 1.1.1.1 enable
  #               
  ospf 1          
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 10.1.2.0 0.0.0.255
  #               
  ip route-static 10.20.1.0 24 NULL 0
  #               
  return          
  ```