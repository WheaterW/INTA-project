Example for Configuring a Basic or Advanced VPN-Target Extended Community Filter
================================================================================

Basic or advanced VPN-target extended community filters can be configured to filter VPN or VPNv4 routes.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172366598__fig_dc_vrp_route-policy_cfg_004401), an MP-IBGP peer relationship is established between PE1 and PE2. PE2 receives two BGP VPNv4 routes (3.3.3.3/32 and 4.4.4.4/32) from PE1. It is required that a basic or advanced VPN-target extended community filter be configured to filter out the VPNv4 route 4.4.4.4/32 received by PE2.

**Figure 1** Networking for configuring a basic or advanced VPN-target extended community filter![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_vrp_route-policy_cfg_004401.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each involved interface.
2. Configure basic MPLS and MPLS LDP, and set up MPLS LSPs.
3. Configure VPN instance IPv4 address families on PEs.
4. Establish an MP-IBGP peer relationship between PEs.
5. Configure static routes and import them to VPN instances on PE1.
6. Configure a basic or advanced VPN-target extended community filter on PE2.
7. Configure a route-policy on PE2.
8. Apply the route-policy on PE2 to the routes to be received from PE1.

#### Data Preparation

To complete the configuration, you need the following data:

* VPN instance names: **vpna**, **vpnb**, and **vpnc**
* ID (1) of a basic VPN-target extended community filter or name (**test**) of an advanced VPN-target extended community filter

#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366598__section_dc_vrp_cfg_00304905) in this section.
2. Configure basic MPLS and MPLS LDP, and set up MPLS LSPs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.1
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] commit
   ```
   ```
   [~PE1-mpls] quit
   ```
   ```
   [~PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] commit
   ```
   ```
   [~PE1-mpls-ldp] quit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 2.2.2.2
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] commit
   ```
   ```
   [~PE2-mpls] quit
   ```
   ```
   [~PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] commit
   ```
   ```
   [~PE2-mpls-ldp] quit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] quit
   ```
3. Configure VPN instance IPv4 address families on PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 1:100
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 1:100 both
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] quit
   ```
   ```
   [*PE1] ip vpn-instance vpnb
   ```
   ```
   [*PE1-vpn-instance-vpnb] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] route-distinguisher 2:100
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] vpn-target 2:100 both
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpnb] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpnc
   ```
   ```
   [*PE2-vpn-instance-vpnc] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpnc-af-ipv4] route-distinguisher 1:100
   ```
   ```
   [*PE2-vpn-instance-vpnc-af-ipv4] vpn-target 3:100 export-extcommunity
   ```
   ```
   [*PE2-vpn-instance-vpnc-af-ipv4] vpn-target 1:100 import-extcommunity
   ```
   ```
   [*PE2-vpn-instance-vpnc-af-ipv4] vpn-target 2:100 import-extcommunity
   ```
   ```
   [*PE2-vpn-instance-vpnc-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpnc] quit
   ```
   ```
   [*PE2] commit
   ```
4. Establish an MP-IBGP peer relationship between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] commit
   ```
   ```
   [~PE1-bgp-af-vpnv4] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-vpnv4] commit
   ```
   ```
   [~PE2-bgp-af-vpnv4] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
5. Configure static routes and import them to VPN instances on PE1.
   
   
   ```
   [~PE1] ip route-static vpn-instance vpna 3.3.3.3 32 NULL0
   ```
   ```
   [*PE1] ip route-static vpn-instance vpnb 4.4.4.4 32 NULL0
   ```
   ```
   [*PE1] commit
   ```
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] import-route static
   ```
   ```
   [*PE1-bgp-vpna] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpnb
   ```
   ```
   [*PE1-bgp-vpnb] import-route static
   ```
   ```
   [*PE1-bgp-vpnb] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Run the [**display bgp vpnv4 all routing-table**](cmdqueryname=display+bgp+vpnv4+all+routing-table) command on PE2 to check information about BGP VPNv4 routes. The command output shows that two routes 3.3.3.3/32 and 4.4.4.4/32 exist in **vpnc**.
   
   ```
   [~PE2] display bgp vpnv4 all routing-table 3.3.3.3
   ```
   ```
    
    BGP local router ID : 10.1.1.2
    Local AS number : 100
    
    Total routes of Route Distinguisher(1:100): 1
    BGP routing table entry information of 3.3.3.3/32:
    Label information (Received/Applied): 32905/NULL
    From: 1.1.1.1 (1.1.1.1)  
    Route Duration: 0d00h06m19s
    Relay IP Nexthop: 10.1.1.1
    Relay IP Out-Interface: GigabitEthernet0/1/0
    Relay Tunnel Out-Interface: GigabitEthernet0/1/0
    Original nexthop: 1.1.1.1
    Qos information : 0x0            
    Ext-Community: RT <1 : 100>
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Not advertised to any peer yet
       
    VPN-Instance vpnc, Router ID 10.1.1.2:
   
    Total Number of Routes: 1
    BGP routing table entry information of 3.3.3.3/32:
    Route Distinguisher: 1:100
    Remote-Cross route
    Label information (Received/Applied): 32905/NULL
    From: 1.1.1.1 (1.1.1.1)  
    Route Duration: 0d00h06m19s
    Relay Tunnel Out-Interface: GigabitEthernet0/1/0
    Original nexthop: 1.1.1.1
    Qos information : 0x0            
    Ext-Community: RT <1 : 100>
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Not advertised to any peer yet
   ```
   ```
   [~PE2] display bgp vpnv4 all routing-table 4.4.4.4
   ```
   ```
    
    BGP local router ID : 10.1.1.2
    Local AS number : 100
    
    Total routes of Route Distinguisher(2:100): 1
    BGP routing table entry information of 4.4.4.4/32:
    Label information (Received/Applied): 32906/NULL
    From: 1.1.1.1 (1.1.1.1)  
    Route Duration: 0d00h06m24s
    Relay IP Nexthop: 10.1.1.1
    Relay IP Out-Interface: GigabitEthernet0/1/0
    Relay Tunnel Out-Interface: GigabitEthernet0/1/0
    Original nexthop: 1.1.1.1
    Qos information : 0x0            
    Ext-Community: RT <2 : 100>
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Not advertised to any peer yet
       
    VPN-Instance vpnc, Router ID 10.1.1.2:
   
    Total Number of Routes: 1
    BGP routing table entry information of 4.4.4.4/32:
    Route Distinguisher: 2:100
    Remote-Cross route
    Label information (Received/Applied): 32906/NULL
    From: 1.1.1.1 (1.1.1.1)  
    Route Duration: 0d00h06m24s
    Relay Tunnel Out-Interface: GigabitEthernet0/1/0
    Original nexthop: 1.1.1.1
    Qos information : 0x0            
    Ext-Community: RT <2 : 100>
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Not advertised to any peer yet
   ```
6. Configure a basic or advanced VPN-target extended community filter on PE2.
   
   
   
   Configure a basic VPN-target extended community filter.
   
   ```
   [~PE2] ip extcommunity-filter 1 index 10 permit rt 1:100
   ```
   ```
   [*PE2] commit
   ```
   
   Configure an advanced VPN-target extended community filter.
   
   ```
   [~PE2] ip extcommunity-filter advanced test index 10 permit ^1:100$
   ```
   ```
   [*PE2] commit
   ```
7. Configure a route-policy on PE2.
   
   
   
   In the case of a basic VPN-target extended community filter:
   
   ```
   [~PE2] route-policy test permit node 10
   ```
   ```
   [*PE2-route-policy] if-match extcommunity-filter 1
   ```
   ```
   [*PE2-route-policy] quit
   ```
   ```
   [*PE2] route-policy test deny node 20
   ```
   ```
   [*PE2] commit
   ```
   
   In the case of an advanced VPN-target extended community filter:
   
   ```
   [~PE2] route-policy test permit node 10
   ```
   ```
   [*PE2-route-policy] if-match extcommunity-filter test
   ```
   ```
   [*PE2-route-policy] quit
   ```
   ```
   [*PE2] route-policy test deny node 20
   ```
   ```
   [*PE2] commit
   ```
8. Apply the route-policy on PE2 to the routes to be received from PE1.
   
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 1.1.1.1 route-policy test import
   ```
   ```
   [*PE2-bgp-af-vpnv4] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Run the [**display bgp vpnv4 all routing-table**](cmdqueryname=display+bgp+vpnv4+all+routing-table) command on PE2 to check information about BGP VPNv4 routes. The command output shows that route 4.4.4.4/32 has been filtered out.
   
   ```
   [~PE2] display bgp vpnv4 all routing-table 3.3.3.3
   ```
   ```
    
    BGP local router ID : 10.1.1.2
    Local AS number : 100
    
    Total routes of Route Distinguisher(1:100): 1
    BGP routing table entry information of 3.3.3.3/32:
    Label information (Received/Applied): 32905/NULL
    From: 1.1.1.1 (1.1.1.1)  
    Route Duration: 0d00h05m41s
    Relay IP Nexthop: 10.1.1.1
    Relay IP Out-Interface: GigabitEthernet0/1/0
    Relay Tunnel Out-Interface: GigabitEthernet0/1/0
    Original nexthop: 1.1.1.1
    Qos information : 0x0            
    Ext-Community: RT <1 : 100>
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Not advertised to any peer yet
       
    VPN-Instance vpnc, Router ID 10.1.1.2:
   
    Total Number of Routes: 1
    BGP routing table entry information of 3.3.3.3/32:
    Route Distinguisher: 1:100
    Remote-Cross route
    Label information (Received/Applied): 32905/NULL
    From: 1.1.1.1 (1.1.1.1)  
    Route Duration: 0d00h37m42s
    Relay Tunnel Out-Interface: GigabitEthernet0/1/0
    Original nexthop: 1.1.1.1
    Qos information : 0x0            
    Ext-Community: RT <1 : 100>
    AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Not advertised to any peer yet
   ```
   ```
   [~PE2] display bgp vpnv4 all routing-table 4.4.4.4
   ```
   ```
   Info: The network does not exist.
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 1:100
    vpn-target 1:100 export-extcommunity
    vpn-target 1:100 import-extcommunity
  #
  ip vpn-instance vpnb
   ipv4-family    
    route-distinguisher 2:100
    vpn-target 2:100 export-extcommunity
    vpn-target 2:100 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance vpna
    import-route static
   #
   ipv4-family vpn-instance vpnb
    import-route static
  #
  ip route-static 2.2.2.2 255.255.255.255 GigabitEthernet0/1/0 10.1.1.2
  ip route-static vpn-instance vpna 3.3.3.3 255.255.255.255 NULL0
  ip route-static vpn-instance vpnb 4.4.4.4 255.255.255.255 NULL0
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpnc
   ipv4-family
    route-distinguisher 1:100
    vpn-target 3:100 export-extcommunity
    vpn-target 1:100 import-extcommunity
    vpn-target 2:100 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 route-policy test import
  #
  ip extcommunity-filter 1 index 10 permit rt 1:100
  #
  route-policy test permit node 10
   if-match extcommunity-filter 1
  #               
  route-policy test deny node 20
  #
  ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet0/1/0 10.1.1.1
  #
  return
  ```