Example for Configuring Dynamic BGP IPv6 Flow Specification
===========================================================

For DoS/DDoS attacks whose traffic characteristics cannot be predicted, you can deploy a traffic analysis server to implement BGP IPv6 Flow Specification. The server uses Update packets to carry BGP IPv6 Flow Specification routes, ensuring device security on the network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372366__fig_dc_vrp_flowspec_cfg_001201), DeviceA belongs to AS 100, DeviceB and Server belong to AS 200, and DeviceB is the ingress of AS 200. AS 100 and AS 200 communicate with each other through DeviceB.

When an attack source appears in AS 100, attack traffic flows into AS 200 through DeviceB, posing a threat to AS 200. To ensure network security, configure dynamic BGP IPv6 Flow Specification. Specifically, deploy a traffic analysis server on the network and establish a BGP IPv6 Flow Specification peer relationship between the traffic analysis server and DeviceB. DeviceB periodically samples traffic and sends sampled traffic to the traffic analysis server. The traffic analysis server generates a BGP IPv6 Flow Specification route based on the characteristics of sampled attack traffic and sends the route to DeviceB. DeviceB converts the route into a traffic policy to filter and control attack traffic, ensuring the normal running of services in AS 200.

**Figure 1** Configuring dynamic BGP IPv6 Flow Specification![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_flowspec_cfg_001201.png)

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses.
2. Configure DeviceB to establish a BGP IPv6 Flow Specification peer relationship with the traffic analysis server (Server) so that the automatically generated BGP IPv6 Flow Specification route can be sent to DeviceB to form a traffic filtering policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The traffic analysis server is a third-party device and must be able to establish BGP IPv6 Flow Specification peer relationships.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs of DeviceA and DeviceB: 1.1.1.1 and 2.2.2.2, respectively
* AS number of DeviceA: 100; AS number of DeviceB and Server: 200


#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   For detailed configurations, see Configuration Files.
2. Configure an IPv4 peer.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 10.10.1.2 as-number 200
   ```
   ```
   [*Device-bgp] commit
   ```
3. Establish a BGP IPv6 Flow Specification peer relationship and disable route validation.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] peer 10.2.1.2 as-number 200
   ```
   ```
   [*DeviceB-bgp] peer 10.10.1.1 as-number 100
   ```
   ```
   [*DeviceB-bgp] ipv6-family flow
   ```
   ```
   [*DeviceB-bgp-af-ipv6-flow] peer 10.2.1.2 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6-flow] peer 10.2.1.2 validation-disable
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
4. Verify the configuration.
   
   
   
   # Check the state of the BGP IPv6 Flow Specification peer relationship on DeviceB. The command output shows that the peer relationship has been successfully established.
   
   ```
   <DeviceB> display bgp flow ipv6 peer
   ```
   ```
    BGP local router ID : 2.2.2.2
    Local AS number : 200
    Total number of peers : 1                 Peers in established state : 1
     Peer       V       AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.2.1.2   4      200        9       10     0 00:00:35 Established        1
   ```
   
   # Check information about the BGP IPv6 Flow Specification route received by DeviceB.
   
   ```
   <DeviceB> display bgp flow ipv6 routing-table
   ```
   ```
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 1
   
    * >  ReIndex : 2
         Dissemination Rules:
          FragmentType   : match (Don't fragment)
          MED      : 0                   PrefVal  : 0
          LocalPref: 100
          Path/Ogn :  i
   ```
   
   # Check the traffic filtering rule carried in each BGP IPv6 Flow Specification route based on the corresponding **ReIndex** shown in the preceding command output.
   
   ```
   <DeviceB> display bgp flow ipv6 routing-table 2
   ```
   ```
    BGP local router ID : 2.2.2.2
    Local AS number : 200
    Paths:   1 available, 1 best
    ReIndex : 2
    Order   : 2147483647
    Dissemination Rules :
      FragmentType   : match (Don't fragment)
   
    BGP flow-ipv6 routing table entry information of 2:
    Match action :
      apply deny
    From: 10.2.1.2 (10.2.1.2)
    Route Duration: 0d00h02m26s
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, internal, pre 255
    Not advertised to any peers yet
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
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
   peer 10.10.1.2 as-number 200
   #
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
   peer 10.2.1.2 as-number 200
   peer 10.10.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 10.2.1.2 enable
    peer 10.10.1.1 enable
   #
   ipv6-family flow
    peer 10.2.1.2 enable
    peer 10.2.1.2 validation-disable
  #
  return
  ```
* Server configuration file
  
  ```
  #
  sysname Server
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
   ipv6-family flow
    peer 10.2.1.1 enable
  #
  flow-route FlowSpec1
   if-match fragment-type match non-fragment
   apply deny
  #
  return
  ```