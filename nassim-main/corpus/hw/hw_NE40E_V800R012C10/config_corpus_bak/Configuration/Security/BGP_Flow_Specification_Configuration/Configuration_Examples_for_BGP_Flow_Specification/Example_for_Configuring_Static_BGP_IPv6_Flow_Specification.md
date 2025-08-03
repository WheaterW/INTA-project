Example for Configuring Static BGP IPv6 Flow Specification
==========================================================

For DoS/DDoS attacks whose traffic characteristics can be predicted, you can manually configure BGP IPv6 Flow Specification routes to implement static BGP IPv6 Flow Specification, ensuring device security on the network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372367__fig_dc_vrp_flowspec_cfg_001101), DeviceA belongs to AS 100; DeviceB, DeviceC, and DeviceD belong to AS 200; DeviceB is the ingress of AS 200. AS 100 and AS 200 communicate with each other through DeviceB.

If an attack source appears in AS 100, attack traffic flows into AS 200 through DeviceB, which severely affects the network performance of AS 200.

Static BGP IPv6 flow specification can be configured to resolve this problem. Specifically, you can manually configure a BGP IPv6 flow specification route, and establish a BGP IPv6 flow specification peer relationship to allow the BGP IPv6 flow specification route to be sent to DeviceB. In this way, the attack traffic is discarded, or its rate is limited.

**Figure 1** Networking for configuring static BGP IPv6 Flow Specification![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_flowspec_cfg_001101.png)  


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF on DeviceB, DeviceC, and DeviceD in AS 200 for interworking.
2. Configure a BGP IPv6 flow specification route named FlowSpec1 on DeviceC to discard the attack traffic with the source port number being 159.
3. Configure a BGP IPv6 flow specification route named FlowSpec2 on DeviceD to limit the rate of the attack traffic with the source port number being 170.
4. Establish BGP IPv6 flow specification peer relationships between DeviceB and DeviceC and between DeviceB and DeviceD using loopback interfaces so that the BGP IPv6 flow specification routes can be sent to DeviceB to form traffic filtering policies.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs of DeviceA, DeviceB, DeviceC, and DeviceD: 1.1.1.1, 2.2.2.2, 3.3.3.3, and 4.4.4.4
* AS number of DeviceA: 100; AS number of DeviceB, DeviceC, and DeviceD: 200


#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   For detailed configurations, see Configuration Files.
2. Configure OSPF.
   
   
   
   For detailed configurations, see Configuration Files.
3. Establish BGP connections.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 10.10.1.2 as-number 200
   ```
   ```
   [*Device-bgp] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 10.10.1.1 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 3.3.3.3 as-number 200
   ```
   ```
   [*DeviceB-bgp] peer 3.3.3.3 connect-interface LoopBack1
   ```
   ```
   [*DeviceB-bgp] peer 4.4.4.4 as-number 200
   ```
   ```
   [*DeviceB-bgp] peer 4.4.4.4 connect-interface LoopBack1
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 200
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-bgp] peer 2.2.2.2 as-number 200
   ```
   ```
   [*DeviceC-bgp] peer 2.2.2.2 connect-interface LoopBack1
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 200
   ```
   ```
   [*DeviceD-bgp] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-bgp] peer 2.2.2.2 as-number 200
   ```
   ```
   [*DeviceD-bgp] peer 2.2.2.2 connect-interface LoopBack1
   ```
   ```
   [*DeviceD-bgp] commit
   ```
4. Configure BGP IPv6 flow specification routes.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] flow-route FlowSpec1 ipv6
   ```
   ```
   [*DeviceC-flow-route-ipv6] if-match source-port equal 159
   ```
   ```
   [*DeviceC-flow-route-ipv6] apply deny
   ```
   ```
   [*DeviceC-flow-route-ipv6] commit
   ```
   ```
   [~DeviceC-flow-route-ipv6] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] flow-route FlowSpec2 ipv6
   ```
   ```
   [*DeviceD-flow-route-ipv6] if-match source-port equal 170
   ```
   ```
   [*DeviceD-flow-route-ipv6] apply traffic-rate 10000
   ```
   ```
   [*DeviceD-flow-route-ipv6] commit
   ```
   ```
   [~DeviceD-flow-route-ipv6] quit
   ```
5. Establish BGP IPv6 flow specification peer relationships.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB]bgp 200
   ```
   ```
   [*DeviceB-bgp] ipv6-family flow
   ```
   ```
   [*DeviceB-bgp-af-ipv6-flow] peer 3.3.3.3 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6-flow] peer 4.4.4.4 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6-flow] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv6-flow] quit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC]bgp 200
   ```
   ```
   [*DeviceC-bgp] ipv6-family flow
   ```
   ```
   [*DeviceC-bgp-af-ipv6-flow] peer 2.2.2.2 enable
   ```
   ```
   [*DeviceC-bgp-af-ipv6-flow] commit
   ```
   ```
   [~DeviceC-bgp-af-ipv6-flow] quit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD]bgp 200
   ```
   ```
   [*DeviceD-bgp] ipv6-family flow
   ```
   ```
   [*DeviceD-bgp-af-ipv6-flow] peer 2.2.2.2 enable
   ```
   ```
   [*DeviceD-bgp-af-ipv6-flow] commit
   ```
   ```
   [~DeviceD-bgp-af-ipv6-flow] quit
   ```
   ```
   [~DeviceD-bgp] quit
   ```
6. Verify the configuration.
   
   
   
   # Check the states of the BGP IPv6 flow specification peer relationships on DeviceB. The command output shows that the peer relationships have been successfully established.
   
   ```
   <DeviceB> display bgp flow ipv6 peer
   ```
   ```
    BGP local router ID : 2.2.2.2                                                  
    Local AS number : 200                                                         
    Total number of peers : 2                 Peers in established state : 2                        
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down          State  PrefRcv            
     3.3.3.3         4         200        6        5     0 01:38:07   Established        1            
     4.4.4.4         4         200        5        4     0 01:38:07   Established        1  
   ```
   
   # Check information about the BGP IPv6 flow specification routes received by DeviceB.
   
   ```
   <DeviceB> display bgp flow ipv6 routing-table
   ```
   ```
    BGP Local router ID is 2.2.2.2                                                 
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale            
                  Origin : i - IGP, e - EGP, ? - incomplete                        
    RPKI validation codes: V - valid, I - invalid, N - not-found                   
                                                                                   
    Total Number of Routes: 2                                                      
    * >  ReIndex : 1                                                               
         Dissemination Rules:                                                      
          Src. Port      : eq 170                                                  
          MED      : 0                   PrefVal  : 0                              
          LocalPref: 100                                                           
          Path/Ogn :  i                                                            
    * >  ReIndex : 2                                                               
         Dissemination Rules:                                                      
          Src. Port      : eq 159                                                  
          MED      : 0                   PrefVal  : 0                              
          LocalPref: 100                                                           
          Path/Ogn :  i 
   ```
   
   # Check the traffic filtering rule carried in each BGP IPv6 flow specification route based on the corresponding **ReIndex** shown in the preceding command output.
   
   ```
   <DeviceB> display bgp flow ipv6 routing-table 2
   ```
   ```
    BGP local router ID : 2.2.2.2                                                  
    Local AS number : 200  
    Paths:   1 available, 1 best
    ReIndex : 2                                                                    
    Order   : 0                                                                    
    Dissemination Rules :                                                          
      Src. Port      : eq 159                                                      
                                                                                   
    BGP flow-ipv6 routing table entry information of 2:                            
    Match action :                                                                 
      apply deny                                                                   
    From: 3.3.3.3 (3.3.3.3)                                                        
    Route Duration: 0d00h22m05s                                                    
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, valid, internal, best, pre 255                                                                      
    Not advertised to any peer yet                                                 
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   router-id 1.1.1.1
   peer 10.10.1.2 as-number 200
   ipv4-family unicast
    undo synchronization
    peer 10.10.1.2 enable
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
  undo shutdown
   ip address 10.2.1.1 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 200
   router-id 2.2.2.2
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack1
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack1
   peer 10.10.1.1 as-number 100
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
    peer 10.10.1.1 enable
   #
   ipv6-family flow
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 200
   router-id 3.3.3.3
   peer 2.2.2.2 as-number 200
   peer 2.2.2.2 connect-interface LoopBack1
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 2.2.2.2 enable
   ipv6-family flow
    peer 2.2.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.2.1.0 0.0.0.255
  #
  flow-route FlowSpec1 ipv6
   if-match source-port equal 159
   apply deny
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 200
   router-id 4.4.4.4
   peer 2.2.2.2 as-number 200
   peer 2.2.2.2 connect-interface LoopBack1
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   ipv6-family flow
    peer 2.2.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  flow-route FlowSpec2 ipv6
   if-match source-port equal 170
   apply traffic-rate 10000
  #
  return
  ```