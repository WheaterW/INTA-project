Example for Configuring Static BGP VPNv4 Flow Specification
===========================================================

This section provides an example for configuring static BGP VPNv4 Flow Specification to allow BGP VPNv4 Flow Specification routes to be transmitted and traffic filtering policies to be generated. The policies improve security of devices in VPNs.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372382__fig_dc_vrp_flowspec_cfg_002001), in the VPN, CE1 belongs to AS 100; PE1 and PE2 belong to AS 200, all devices are in the same VPN domain. PE1 is the ingress of the VPN domain in AS 200. AS 200 can communicate with AS 100 through PE1.

If an attack source appears in AS 100, attack traffic flows into AS 200 through PE1, which severely affects the VPN performance of AS 200.

Static BGP VPNv4 Flow Specification can be configured to resolve this problem. Specifically, configure a BGP VPN Flow Specification route on PE2 and enable the BGP-Flow VPNv4 address family so that a BGP VPNv4 Flow Specification route can be generated automatically. Then, establish a BGP VPNv4 Flow Specification peer relationship between PE1 and PE2 to transmit the BGP VPNv4 Flow Specification route and form a traffic policy. Then attack traffic is filtered and controlled.

**Figure 1** Configuring static BGP VPNv4 Flow Specification![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_flowspec_cfg_000901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses.
2. Create a VPN instance on PE1 and PE2 and bind it to the interface connecting PE1 to CE1.
3. Configure a BGP VPN Flow Specification route named FlowSpec1 on PE2 to discard the attack traffic with the source port number being 159.
4. Establish a BGP VPNv4 Flow Specification peer relationship between PE1 and PE2 so that the generated BGP VPNv4 Flow Specification route can be sent to PE1 to form traffic policy.

#### Data Preparation

To complete the configuration, you need the following data:

* AS number of CE1: 100; AS number of PE1 and PE2: 200
* VPN instance name: vpna


#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   For configuration details, see the configuration files.
2. Create a VPN instance and bind the VPN instance to the PE1's interface that is connected to CE1.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 export-extcommunity
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 import-extcommunity
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE1-vpn-instance-vpna] quit
   ```
   ```
   [~PE1] interface GigabitEthernet0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [~PE1] interface GigabitEthernet0/2/0
   ```
   ```
   [~PE1-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.2.1.1 255.255.255.0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 export-extcommunity
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 import-extcommunity
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE2-vpn-instance-vpna] quit
   ```
   ```
   [~PE2] interface GigabitEthernet0/1/0
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.2.1.2 255.255.255.0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] quit
   ```
3. Configure a BGP VPN Flow Specification route.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] flow-route FlowSpec1 vpn-instance vpna
   ```
   ```
   [*PE2-flow-route-vpna] if-match source-port equal 159
   ```
   ```
   [*PE2-flow-route-vpna] apply deny
   ```
   ```
   [*PE2-flow-route-vpna] commit
   ```
   ```
   [~PE2-flow-route-vpna] quit
   ```
4. Establish a BGP VPNv4 Flow Specification peer relationship.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1]bgp 200
   ```
   ```
   [*PE1-bgp] peer 10.2.1.2 as-number 200
   ```
   ```
   [*PE1-bgp] vpn-instance vpna
   ```
   ```
   [*PE1-bgp-instance-vpna] quit
   ```
   ```
   [*PE1-bgp] ipv4-flow vpn-instance vpna
   ```
   ```
   [*PE1-bgp-flow-vpna] quit
   ```
   ```
   [*PE1-bgp] ipv4-flow vpnv4
   ```
   ```
   [*PE1-bgp-af-flow-vpnv4] peer 10.2.1.2 enable
   ```
   ```
   [*PE1-bgp-af-flow-vpnv4] commit
   ```
   ```
   [~PE1-bgp-af-flow-vpnv4] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2]bgp 200
   ```
   ```
   [*PE2-bgp] peer 10.2.1.1 as-number 200
   ```
   ```
   [*PE2-bgp] vpn-instance vpna
   ```
   ```
   [*PE2-bgp-instance-vpna] quit
   ```
   ```
   [*PE2-bgp] ipv4-flow vpn-instance vpna
   ```
   ```
   [*PE2-bgp-flow-vpna] quit
   ```
   ```
   [*PE2-bgp] ipv4-flow vpnv4
   ```
   ```
   [*PE2-bgp-af-flow-vpnv4] peer 10.2.1.1 enable
   ```
   ```
   [*PE2-bgp-af-flow-vpnv4] commit
   ```
   ```
   [~PE2-bgp-af-flow-vpnv4] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
5. Verify the configuration.
   
   
   
   # Check the status of the BGP VPNv4 Flow Specification peer relationship on PE2. The command output shows that the BGP VPNv4 Flow Specification peer relationship has been successfully established.
   
   ```
   <PE2> display bgp flow vpnv4 all peer
   ```
   ```
    
    BGP local router ID : 10.2.1.2
    Local AS number : 200
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.2.1.1        4         200     1042     1051     0 15:07:49 Established        0
   ```
   
   # Check information about the BGP VPNv4 Flow Specification routes received by PE1.
   
   ```
   <PE1> display bgp flow vpnv4 route-distinguisher 200:1 routing-table
   ```
   ```
    
    BGP Local router ID is 10.2.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Route Distinguisher: 200:1
    
    Total Number of Routes: 1
    * >  ReIndex : 536870913
         Dissemination Rules:
          Src. Port      : eq 159
          MED      : 0                   PrefVal  : 0                   
          LocalPref: 100                       
          Path/Ogn :  i
   ```
   
   # Check the traffic filtering rule carried in each BGP VPNv4 Flow Specification route based on the value of **ReIndex** in the preceding command output.
   
   ```
   <PE1> display bgp flow vpnv4 all routing-table 536870913
   ```
   ```
    
    BGP local router ID : 10.2.1.1
    Local AS number : 200
    ReIndex : 536870913
    Order   : 0
    Dissemination Rules :
      Src. Port      : eq 159
    
    BGP flow-vpnv4 routing table entry information of 536870913:
    Route Distinguisher: 200:1
    Match action :
      apply deny
    From: 10.2.1.2 (10.2.1.2) 
    Route Duration: 0d13h59m46s
    Ext-Community: RT <111 : 1>
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, valid, internal, best, pre 255
    Not advertised to any peer yet
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0              
  #               
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.2.1.1 255.255.255.0
  #               
  bgp 200         
   peer 10.2.1.2 as-number 200
   #              
   ipv4-family unicast
    undo synchronization 
    peer 10.2.1.2 enable
   #              
   vpn-instance vpna
   #              
   ipv4-flow vpn-instance vpna
   #              
   ipv4-flow vpnv4
    policy vpn-target
    peer 10.2.1.2 enable
  #               
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.2.1.2 255.255.255.0
  #               
  bgp 200         
   peer 10.2.1.1 as-number 200
   #              
   ipv4-family unicast
    undo synchronization 
    peer 10.2.1.1 enable
   #              
   vpn-instance vpna
   #              
   ipv4-flow vpn-instance vpna
   #              
   ipv4-flow vpnv4
    policy vpn-target
    peer 10.2.1.1 enable
  #               
  flow-route FlowSpec1 vpn-instance vpna
   if-match source-port equal 159
   apply deny     
  #               
  return          
  ```