Example for Configuring Static BGP VPN Flow Specification
=========================================================

In a VPN domain, you can manually configure BGP VPN Flow Specification routes to implement static BGP VPN Flow Specification for DoS/DDoS attacks whose characteristics can be predicted, ensuring device security in the VPN.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372372__fig_dc_vrp_flowspec_cfg_000901), in the VPN, CE1 belongs to AS 100; PE1 and PE2 belong to AS 200; all devices are in the same VPN domain. PE1 is the ingress of the VPN domain in AS 200. AS 200 can communicate with AS 100 through PE1.

If an attack source appears in AS 100, attack traffic flows into AS 200 through PE1, which severely affects the VPN performance of AS 200.

Static BGP VPN Flow Specification can be configured to resolve this problem. Specifically, you can manually configure a BGP Flow Specification route, and establish a BGP Flow Specification peer relationship to allow the BGP VPN Flow Specification route to be sent to PE1. In this way, the attack traffic is discarded, or its rate is limited.

**Figure 1** Configuring static BGP VPN Flow Specification![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_flowspec_cfg_000901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses.
2. Create a VPN instance on PE1 and PE2 and bind it to their interfaces.
3. Configure a BGP VPN Flow Specification route named FlowSpec1 on PE2 to discard the attack traffic with the source port number being 159.
4. Establish a BGP VPN Flow Specification peer relationship between PE1 and PE2 so that the created BGP VPN Flow Specification route can be sent to PE1 to form a traffic filtering policy.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs of CE1, PE1, and PE2: 1.1.1.1, 2.2.2.2, and 3.3.3.3, respectively
* AS number of CE1: 100; AS number of PE1 and PE2: 200
* VPN instance name: vpna


#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   For configuration details, see the configuration files.
2. Create a VPN instance and bind it to each interface.
   
   
   
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
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpna
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
   [*PE2-GigabitEthernet0/1/0] ip binding vpn-instance vpna
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
4. Establish a BGP VPN Flow Specification peer relationship.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1]bgp 200
   ```
   ```
   [*PE1-bgp] router-id 2.2.2.2
   ```
   ```
   [*PE1-bgp] commit
   ```
   ```
   [~PE1-bgp] vpn-instance vpna
   ```
   ```
   [*PE1-bgp-instance-vpna] peer 10.1.1.1 as-number 100
   ```
   ```
   [*PE1-bgp-instance-vpna] peer 10.2.1.2 as-number 200
   ```
   ```
   [*PE1-bgp-instance-vpna] quit
   ```
   ```
   [*PE1-bgp] ipv4-flow vpn-instance vpna
   ```
   ```
   [*PE1-bgp-flow-vpna] peer 10.1.1.1 enable
   ```
   ```
   [*PE1-bgp-flow-vpna] peer 10.2.1.2 enable
   ```
   ```
   [*PE1-bgp-flow-vpna] commit
   ```
   ```
   [~PE1-bgp-flow-vpna] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2]bgp 200
   ```
   ```
   [*PE2-bgp] router-id 3.3.3.3
   ```
   ```
   [*PE2-bgp] commit
   ```
   ```
   [~PE2-bgp] vpn-instance vpna
   ```
   ```
   [*PE2-bgp-instance-vpna] peer 10.2.1.1 as-number 200
   ```
   ```
   [*PE2-bgp-instance-vpna] quit
   ```
   ```
   [*PE2-bgp] ipv4-flow vpn-instance vpna
   ```
   ```
   [*PE2-bgp-flow-vpna] peer 10.2.1.1 enable
   ```
   ```
   [*PE2-bgp-flow-vpna] commit
   ```
   ```
   [~PE2-bgp-flow-vpna] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
5. Verify the configuration.
   
   
   
   # Check the status of BGP VPN Flow Specification peer relationships on PE1. The command output shows that the BGP VPN Flow Specification peer relationships have been successfully established.
   
   ```
   <PE1> display bgp flow vpnv4 vpn-instance vpna peer
   ```
   ```
    
    BGP local router ID : 2.2.2.2
    Local AS number : 200
   
    VPN-Instance vpna, Router ID 2.2.2.2:
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.1.1        4         100        3        5     0 00:00:06 Established        0
     10.2.1.2        4         200     9523     9530     0 0138h31m Established        1
   ```
   
   # Check information about the BGP VPN Flow Specification routes received by PE1.
   
   ```
   <PE1> display bgp flow vpnv4 vpn-instance vpna routing-table
   ```
   ```
    Total Number of Routes: 1
    * >  ReIndex : 1
         Dissemination Rules:
          Src. Port      : eq 159
          MED      : 0                   PrefVal  : 0                   
          LocalPref: 100                       
          Path/Ogn :  i
   ```
   
   # Check the traffic filtering rule carried in each BGP VPN Flow Specification route based on the value of **ReIndex** in the preceding command output.
   
   ```
   <PE1> display bgp flow vpnv4 vpn-instance vpna routing-table 1
   ```
   ```
    ReIndex : 1
    Order   : 0
    Dissemination Rules :
      Src. Port      : eq 159
    
    BGP flow-ipv4 routing table entry information of 1:
    Match action :
      apply deny
    From: 10.2.1.2 (3.3.3.3) 
    Route Duration: 0d15h13m20s
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, valid, internal, best, pre 255
    Advertised to such 1 peers:
       10.1.1.1
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
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 10.1.1.2 as-number 200
   #              
   ipv4-family unicast
    undo synchronization 
    peer 10.1.1.2 enable
   #              
   ipv4-family flow
    peer 10.1.1.2 enable
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
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
  #               
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #               
  bgp 200         
   router-id 2.2.2.2
   #              
   ipv4-family unicast
    undo synchronization 
   #              
   vpn-instance vpna
    peer 10.1.1.1 as-number 100
    peer 10.2.1.2 as-number 200
   #              
   ipv4-flow vpn-instance vpna
    peer 10.1.1.1 enable
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
   ip binding vpn-instance vpna
   ip address 10.2.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #               
  bgp 200         
   router-id 3.3.3.3
   #              
   ipv4-family unicast
    undo synchronization 
   #              
   vpn-instance vpna
    peer 10.2.1.1 as-number 200
   #              
   ipv4-flow vpn-instance vpna
    peer 10.2.1.1 enable
  #               
  flow-route FlowSpec1 vpn-instance vpna
   if-match source-port equal 159
   apply deny     
  #               
  return          
  ```