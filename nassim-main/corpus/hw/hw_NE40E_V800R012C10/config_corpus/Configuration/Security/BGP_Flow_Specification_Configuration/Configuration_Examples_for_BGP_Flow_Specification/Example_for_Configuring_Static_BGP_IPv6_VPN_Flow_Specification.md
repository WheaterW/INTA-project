Example for Configuring Static BGP IPv6 VPN Flow Specification
==============================================================

In an IPv6 VPN domain, you can manually configure BGP IPv6 VPN Flow Specification routes to implement static BGP IPv6 VPN Flow Specification for DoS/DDoS attacks whose characteristics can be predicted, ensuring device security in the VPN.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372378__fig_dc_vrp_flowspec_cfg_002501), in the IPv6 VPN, CE1 belongs to AS 100; PE1 belongs to AS 200. CE1 and PE1 are in the same VPN domain. PE1 is the ingress of the VPN domain in AS 200. AS 200 can communicate with AS 100 through PE1.

If an attack source appears in AS 100, attack traffic flows into AS 200 through PE1, which severely affects the VPN performance of AS 200.

Static BGP IPv6 VPN Flow Specification can be configured to resolve this problem. Specifically, you can manually configure a BGP IPv6 Flow Specification route, and establish a BGP IPv6 VPN Flow Specification peer relationship to allow the BGP IPv6 VPN Flow Specification route to be sent to PE1. In this way, the attack traffic is discarded, or its rate is limited.

**Figure 1** Configuring static BGP IPv6 VPN Flow Specification![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE0/1/0.


  
![](images/fig_dc_vrp_flowspec_cfg_002501.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses.
2. Create a VPN instance on PE1 and bind the VPN instance to each interface.
3. Configure a BGP IPv6 VPN Flow Specification route named FlowSpec1 on PE1 to discard the attack traffic with the source port number being 159.

#### Data Preparation

To complete the configuration, you need the following data:

* AS number (100) of CE1 and the AS number (200) of PE1
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
   [*PE1-vpn-instance-vpna] ipv6-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv6] route-distinguisher 2:2
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv6] vpn-target 2:2 export-extcommunity
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv6] vpn-target 2:2 import-extcommunity
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv6] commit
   ```
   ```
   [~PE1-vpn-instance-vpna-af-ipv6] quit
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
   [*PE1-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2 64
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
3. Configure a BGP IPv6 VPN Flow Specification route.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] flow-route FlowSpec1 ipv6 vpn-instance vpna
   ```
   ```
   [*PE1-flow-route-ipv6-vpna] if-match source-port equal 159
   ```
   ```
   [*PE1-flow-route-ipv6-vpna] apply deny
   ```
   ```
   [*PE1-flow-route-ipv6-vpna] commit
   ```
   ```
   [~PE1-flow-route-ipv6-vpna] quit
   ```
4. Establish a BGP IPv6 VPN Flow Specification peer relationship.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1]bgp 200
   ```
   ```
   [*PE1-bgp] vpn-instance vpna
   ```
   ```
   [*PE1-bgp-instance-vpna] peer 2001:db8:1::2 as-number 100
   ```
   ```
   [*PE1-bgp-instance-vpna] quit
   ```
   ```
   [*PE1-bgp] ipv6-flow vpn-instance vpna
   ```
   ```
   [*PE1-bgp-flow-6-vpna] peer 2001:db8:1::2 enable
   ```
   ```
   [*PE1-bgp-flow-6-vpna] commit
   ```
   ```
   [~PE1-bgp-flow-6-vpna] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
5. Verify the configuration.
   
   
   
   # Check the status of the BGP IPv6 VPN Flow Specification peer relationship on PE1. The command output shows that the BGP IPv6 VPN Flow Specification peer relationship has been successfully established.
   
   ```
   <PE1> display bgp flow vpnv6 vpn-instance vpna peer
   ```
   ```
    
    BGP local router ID : 0.0.0.0
    Local AS number : 200
    Total number of peers : 1                 Peers in established state : 0
   
     VPN-Instance vpna, Router ID 0.0.0.0:
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:1::1   4         200        0        0     0 00:06:15        Idle        0
   ```
   
   # Check the information about the BGP IPv6 VPN Flow Specification routes received by PE1.
   
   ```
   <PE1> display bgp flow vpnv6 vpn-instance vpna routing-table
   ```
   ```
    
    BGP Local router ID is 0.0.0.0
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
       
    VPN-Instance vpna, Router ID 0.0.0.0:
   
    Total Number of Routes: 1
    * >  ReIndex : 1
         Dissemination Rules:
          Src. Port      : eq 159
          MED      : 0                   PrefVal  : 0                   
          LocalPref:                           
          Path/Ogn :  i
   ```
   
   # Check the traffic filtering rule carried in each BGP IPv6 VPN Flow Specification route based on the value of **ReIndex** in the preceding command output.
   
   ```
   <PE1> display bgp flow vpnv6 vpn-instance vpna routing-table 1
   ```
   ```
    
    BGP local router ID : 0.0.0.0
    Local AS number : 200
    ReIndex : 1
    Order   : 0
    Dissemination Rules :
      Src. Port      : eq 159
    
    BGP flow-ipv6 routing table entry information of 1:
    Local : FlowSpec1
    Match action :
      apply deny
    Route Duration: 0d00h07m04s
    AS-path Nil, origin igp, MED 0, pref-val 0, valid, local, best, pre 0
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
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
  #               
  bgp 100         
   peer 2001:db8:1::2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family flow
    peer 2001:db8:1::2 enable
  #               
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 2:2
    apply-label per-instance
    vpn-target 2:2 export-extcommunity
    vpn-target 2:2 import-extcommunity
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip binding vpn-instance vpna
   ipv6 enable    
   ipv6 address 2001:db8:1::2/64
  #               
  bgp 200         
   #
   ipv4-family unicast
    undo synchronization
   #              
   vpn-instance vpna
    peer 2001:db8:1::1 as-number 200
   #              
   ipv6-flow vpn-instance vpna
    peer 2001:db8:1::1 enable
  #
  flow-route FlowSpec1 ipv6 vpn-instance vpna
   if-match source-port equal 159
   apply deny
  #               
  return
  ```