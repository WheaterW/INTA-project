Example for Configuring Dynamic BGP VPNv4 Flow Specification
============================================================

This section provides an example for configuring dynamic BGP VPNv4 Flow Specification to allow BGP VPNv4 Flow Specification routes to be transmitted and traffic filtering policies to be generated. The policies improve security of devices in VPNs.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372381__fig_dc_vrp_flowspec_cfg_002101), in a VPN, the CE belongs to AS 100; PE1 and Server belong to AS 200; PE1 is a network ingress of AS 200. AS 200 can communicate with AS 100 through PE1.

When an attack source appears in AS 100, attack traffic flows into AS 200 through PE1, posing a threat to AS 200. To ensure VPN security, configure dynamic BGP VPNv4 Flow Specification. Specifically, deploy a traffic analysis server on the network and establish a BGP VPNv4 Flow Specification peer relationship between the traffic analysis server and PE1. PE1 periodically samples traffic and sends sampled traffic to the traffic analysis server. The traffic analysis server generates a BGP VPNv4 Flow Specification route based on the characteristics of sampled attack traffic and sends the route to PE1. PE1 then converts the route into a traffic filtering policy to filter and control attack traffic, ensuring the security of VPN services in AS 200.

**Figure 1** Configuring dynamic BGP VPNv4 Flow Specification![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_flowspec_cfg_001701.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses.
2. Create a VPN instance on PE1 and Server and bind the VPN instance to PE1's interface that is connected to CE1.
3. Configure PE1 to establish a BGP VPNv4 Flow Specification peer relationship with Server so that the automatically generated BGP VPNv4 Flow Specification route can be sent to PE1 to form a traffic filtering policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The traffic analysis server is a third-party device and must be able to establish BGP VPNv4 Flow Specification peer relationships.

#### Data Preparation

To complete the configuration, you need the following data:

* AS number (100) of CE1 and the AS number (200) of PE1 and Server
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
3. Establish a BGP VPNv4 Flow Specification peer relationship.
   
   
   
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
4. Verify the configuration.
   
   
   
   # Check whether the BGP VPNv4 Flow Specification peer relationship with the server is established on PE1. The command output shows that the peer relationship is established. In addition, the BGP VPN Flow Specification peer relationship is established between CE1 and PE1.
   
   ```
   <PE1> display bgp flow vpnv4 all peer
   ```
   ```
    
    BGP local router ID : 10.1.1.2
    Local AS number : 200
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.2.1.2        4         200     1076     1067     0 15:30:19 Established        1
      
     Peer of  for vpn instance :
   
     VPN-Instance vpna, Router ID 10.1.1.2:
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.1.1        4         100     1057     1058     0 15:19:07 Established        0
   ```
   
   # Check information about the BGP VPNv4 Flow Specification routes received by PE1. The command output also shows information about the received BGP VPN Flow Specification routes.
   
   ```
   <PE1> display bgp flow vpnv4 all routing-table
   ```
   ```
    BGP Local router ID is 10.1.1.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    
    Total number of routes from all PE: 1
    * >  ReIndex : 536870913
         Dissemination Rules:
          Src. Port      : eq 159
          MED      : 0                   PrefVal  : 0                   
          LocalPref: 100                       
          Path/Ogn :  i
       
    VPN-Instance vpna, Router ID 10.1.1.2:
   
    Total Number of Routes: 1
    * >  ReIndex : 1
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
    
    BGP local router ID : 10.1.1.2
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
  bgp 100         
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