Example for Configuring BGP GTSM
================================

This section provides an example for configuring BGP GTSM in order to protect Routers on a BGP network against CPU utilization attacks.

#### Networking Requirements

Attacks that use bogus messages can consume and overload limited device resources (such as CPU resources). Attackers may simulate BGP messages and continuously send them to a Router. After receiving these messages, the forwarding plane of the Router sends them directly to the control plane for BGP processing, without validating them, if they are destined for the Router. Consequently, the Router becomes extremely busy, and CPU usage is high because the control plane needs to process these unverified messages.

GTSM protects devices against CPU utilization attacks by checking whether the TTL value in the IP header is within a predefined range.

On the network shown in [Figure 1](#EN-US_TASK_0172372055__fig_dc_vrp_gtsm_cfg_001101), DeviceA belongs to AS10, whereas DeviceB, DeviceC, and DeviceD belong to AS20. BGP runs on the network, and BGP GTSM needs to be configured to protect DeviceB against CPU utilization attacks.

**Figure 1** Network diagram of configuring BGP GTSM![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000002020397281.png)

#### Precautions

During the configuration, note the following:

* GTSM must be enabled on both ends of a BGP connection.
* The same *valid-ttl-hops* value must be configured on both ends of the BGP connection.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF on Routers DeviceB, DeviceC, and DeviceD in AS20 to implement interworking.
2. Establish an EBGP connection between DeviceA and DeviceB and IBGP full-mesh connections among DeviceB, DeviceC, and DeviceD through loopback interfaces.
3. Configure GTSM on DeviceA, DeviceB, DeviceC, and DeviceD.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs and AS numbers of DeviceA, DeviceB, DeviceC, and DeviceD
* Numbers of valid TTL hops between DeviceA and DeviceB, between DeviceB and DeviceC, between DeviceC and DeviceD, and between DeviceB and DeviceD

#### Procedure

1. Configure IP addresses for interfaces. For detailed configurations, see Configuration Files.
2. Configure OSPF. For detailed configurations, see Configuration Files.
3. Configure IBGP full-mesh connections.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 20
   ```
   ```
   [*DeviceB-bgp] router-id 10.2.2.9
   ```
   ```
   [*DeviceB-bgp] peer 10.3.3.9 as-number 20
   ```
   ```
   [*DeviceB-bgp] peer 10.3.3.9 connect-interface LoopBack0
   ```
   ```
   [*DeviceB-bgp] peer 10.3.3.9 next-hop-local
   ```
   ```
   [*DeviceB-bgp] peer 10.4.4.9 as-number 20
   ```
   ```
   [*DeviceB-bgp] peer 10.4.4.9 connect-interface LoopBack0
   ```
   ```
   [*DeviceB-bgp] peer 10.4.4.9 next-hop-local
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 20
   ```
   ```
   [*DeviceC-bgp] router-id 10.3.3.9
   ```
   ```
   [*DeviceC-bgp] peer 10.2.2.9 as-number 20
   ```
   ```
   [*DeviceC-bgp] peer 10.2.2.9 connect-interface LoopBack0
   ```
   ```
   [*DeviceC-bgp] peer 10.4.4.9 as-number 20
   ```
   ```
   [*DeviceC-bgp] peer 10.4.4.9 connect-interface LoopBack0
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 20
   ```
   ```
   [*DeviceD-bgp] router-id 10.4.4.9
   ```
   ```
   [*DeviceD-bgp] peer 10.2.2.9 as-number 20
   ```
   ```
   [*DeviceD-bgp] peer 10.2.2.9 connect-interface LoopBack0
   ```
   ```
   [*DeviceD-bgp] peer 10.3.3.9 as-number 20
   ```
   ```
   [*DeviceD-bgp] peer 10.3.3.9 connect-interface LoopBack0
   ```
   ```
   [*DeviceD-bgp] commit
   ```
4. Configure EBGP connections.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 10
   ```
   ```
   [*DeviceA-bgp] router-id 10.1.1.9
   ```
   ```
   [*DeviceA-bgp] peer 10.1.1.2 as-number 20
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [*DeviceB-bgp] peer 10.1.1.1 as-number 10
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   
   # Check the connection status of peers.
   
   ```
   <DeviceB> display bgp peer
   ```
   ```
    BGP local router ID : 10.2.2.9
    Local AS number : 20
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
   
     10.3.3.9        4    20        8        7     0 00:05:06 Established       0
     10.4.4.9        4    20        8       10     0 00:05:33 Established       0
     10.1.1.1        4    10        7        7     0 00:04:09 Established       0
   ```
   
   The command output shows that BGP connections have been established between DeviceB and other Routers.
5. Configure GTSM on DeviceA and DeviceB. Because the two Routers are directly connected, the valid TTL range for the messages between them is [255, 255]. In this case, the value of **valid-ttl-hops** is 1.
   
   
   
   # Configure GTSM on DeviceA.
   
   ```
   [~DeviceA] bgp 10
   ```
   ```
   [*DeviceA-bgp] peer 10.1.1.2 valid-ttl-hops 1
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   
   # Configure GTSM for the EBGP connection on DeviceB.
   
   ```
   [~DeviceB] bgp 20
   ```
   ```
   [*DeviceB-bgp] peer 10.1.1.1 valid-ttl-hops 1
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   
   # Check the GTSM configuration.
   
   ```
   <DeviceB> display bgp peer 10.1.1.1 verbose
   ```
   ```
   BGP Peer is 10.1.1.1,  remote AS 10
            Type: EBGP link
            BGP version 4, Remote router ID 10.1.1.9
   
     Group ID : 2
            BGP current state: Established, Up for 00h49m35s
            BGP current event: RecvKeepalive
            BGP last state: OpenConfirm
            BGP Peer Up count: 1
            Received total routes: 0
            Received active routes total: 0
            Advertised total routes: 0
            Port:  Local - 179      Remote - 52876
            Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Received  : Active Hold Time: 180 sec
            Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Peer optional capabilities:
            Peer supports bgp multi-protocol extension
            Peer supports bgp route refresh capability
            Peer supports bgp 4-byte-as capability
            Address family IPv4 Unicast: advertised and received
    Received: Total 59 messages
                     Update messages                0
                     Open messages                  2
                     KeepAlive messages             57
                     Notification messages          0
                     Refresh messages               0
    Sent: Total 79 messages
                     Update messages                5
                     Open messages                  2
                     KeepAlive messages             71
                     Notification messages          1
                     Refresh messages               0
    Last keepalive received: 2009-02-20 13:54:58
    Minimum route advertisement interval is 30 seconds
    Optional capabilities:
    Route refresh capability has been enabled
    4-byte-as capability has been enabled
    GTSM has been enabled, valid-ttl-hops: 1
    Peer Preferred Value: 0
    Routing policy configured:
    No routing policy is configured
   ```
   
   The command output shows that GTSM has been enabled, the number of valid hops is 1, and the BGP connection state is **Established**.
6. Configure GTSM on DeviceB and DeviceC. Because the two Routers are directly connected, the valid TTL range for the messages between them is [255, 255]. In this case, the value of **valid-ttl-hops** is 1.
   
   
   
   # Configure GTSM on DeviceB.
   
   ```
   [~DeviceB] bgp 20
   ```
   ```
   [*DeviceB-bgp] peer 10.3.3.9 valid-ttl-hops 1
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   
   # Configure GTSM for the IBGP connection on DeviceC.
   
   ```
   [*DeviceC-bgp] peer 10.2.2.9 valid-ttl-hops 1
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   
   # Check the GTSM configuration.
   
   ```
   <DeviceB> display bgp peer 10.3.3.9 verbose
   ```
   ```
   BGP Peer is 10.3.3.9,  remote AS 20
            Type: IBGP link
            BGP version 4, Remote router ID 10.3.3.9
   
     Group ID : 0
            BGP current state: Established, Up for 00h54m36s
            BGP current event: KATimerExpired
            BGP last state: OpenConfirm
            BGP Peer Up count: 1
            Received total routes: 0
            Received active routes total: 0
            Advertised total routes: 0
            Port:  Local - 54998    Remote - 179
            Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Received  : Active Hold Time: 180 sec
            Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Peer optional capabilities:
            Peer supports bgp multi-protocol extension
            Peer supports bgp route refresh capability
            Peer supports bgp 4-byte-as capability
            Address family IPv4 Unicast: advertised and received
    Received: Total 63 messages
                     Update messages                0
                     Open messages                  1
                     KeepAlive messages             62
                     Notification messages          0
                     Refresh messages               0
    Sent: Total 69 messages
                     Update messages                10
                     Open messages                  1
                     KeepAlive messages             58
                     Notification messages          0
                     Refresh messages               0
    Last keepalive received: 2009-02-20 13:57:43
    Minimum route advertisement interval is 15 seconds
    Optional capabilities:
    Route refresh capability has been enabled
    4-byte-as capability has been enabled
    Nexthop self has been configured
    Connect-interface has been configured
    GTSM has been enabled, valid-ttl-hops: 1
    Peer Preferred Value: 0
    Routing policy configured:
    No routing policy is configured
   ```
   
   The command output shows that GTSM has been enabled, the number of valid hops is 1, and the BGP connection state is **Established**.
7. Configure GTSM on DeviceC and DeviceD. Because the two Routers are directly connected, the valid TTL range for the messages between them is [255, 255]. In this case, the value of **valid-ttl-hops** is 1.
   
   
   
   # Configure GTSM for the IBGP connection on DeviceC.
   
   ```
   [~DeviceC] bgp 20
   ```
   ```
   [*DeviceC-bgp] peer 10.4.4.9 valid-ttl-hops 1
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   
   # Configure GTSM for the IBGP connection on DeviceD.
   
   ```
   [*DeviceD] bgp 20
   ```
   ```
   [*DeviceD-bgp] peer 10.3.3.9 valid-ttl-hops 1
   ```
   ```
   [*DeviceD-bgp] commit
   ```
   
   # Check the GTSM configuration.
   
   ```
   <DeviceC> display bgp peer 10.4.4.9 verbose
   ```
   ```
   BGP Peer is 10.4.4.9,  remote AS 20
            Type: IBGP link
            BGP version 4, Remote router ID 10.4.4.9
   
     Group ID : 1
            BGP current state: Established, Up for 00h56m06s
            BGP current event: KATimerExpired
            BGP last state: OpenConfirm
            BGP Peer Up count: 1
            Received total routes: 0
            Received active routes total: 0
            Advertised total routes: 0
            Port:  Local - 179      Remote - 53758
            Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Received  : Active Hold Time: 180 sec
            Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Peer optional capabilities:
            Peer supports bgp multi-protocol extension
            Peer supports bgp route refresh capability
            Peer supports bgp 4-byte-as capability
            Address family IPv4 Unicast: advertised and received
    Received: Total 63 messages
                     Update messages                0
                     Open messages                  1
                     KeepAlive messages             62
                     Notification messages          0
                     Refresh messages               0
    Sent: Total 63 messages
                     Update messages                0
                     Open messages                  2
                     KeepAlive messages             61
                     Notification messages          0
                     Refresh messages               0
    Last keepalive received: 2009-02-20 14:00:06
    Minimum route advertisement interval is 15 seconds
    Optional capabilities:
    Route refresh capability has been enabled
    4-byte-as capability has been enabled
    Connect-interface has been configured
    GTSM has been enabled, valid-ttl-hops: 1
    Peer Preferred Value: 0
    Routing policy configured:
    No routing policy is configured
   ```
   
   The command output shows that GTSM has been enabled, the number of valid hops is 1, and the BGP connection state is **Established**.
8. Configure GTSM on DeviceB and DeviceD. Because the two Routers are connected through DeviceC, the valid TTL range for the messages between the two Routers is [254, 255]. In this case, the value of **valid-ttl-hops** is 2.
   
   
   
   # Configure GTSM for the IBGP connection on DeviceB.
   
   ```
   [~DeviceB-bgp] peer 10.4.4.9 valid-ttl-hops 2
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   
   # Configure GTSM on DeviceD.
   
   ```
   [~DeviceD-bgp] peer 10.2.2.9 valid-ttl-hops 2
   ```
   ```
   [*DeviceD-bgp] commit
   ```
   
   # Check the GTSM configuration.
   
   ```
   <DeviceB> display bgp peer 10.4.4.9 verbose
   ```
   ```
   BGP Peer is 10.4.4.9,  remote AS 20
            Type: IBGP link
            BGP version 4, Remote router ID 10.4.4.9
   
     Group ID : 0
            BGP current state: Established, Up for 00h57m48s
            BGP current event: RecvKeepalive
            BGP last state: OpenConfirm
            BGP Peer Up count: 1
            Received total routes: 0
            Received active routes total: 0
            Advertised total routes: 0
            Port:  Local - 53714    Remote - 179
            Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Received  : Active Hold Time: 180 sec
            Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Peer optional capabilities:
            Peer supports bgp multi-protocol extension
            Peer supports bgp route refresh capability
            Peer supports bgp 4-byte-as capability
            Address family IPv4 Unicast: advertised and received
    Received: Total 72 messages
                     Update messages                0
                     Open messages                  1
                     KeepAlive messages             71
                     Notification messages          0
                     Refresh messages               0
    Sent: Total 82 messages
                     Update messages                10
                     Open messages                  1
                     KeepAlive messages             71
                     Notification messages          0
                     Refresh messages               0
    Last keepalive received: 2009-02-20 14:01:27
    Minimum route advertisement interval is 15 seconds
    Optional capabilities:
    Route refresh capability has been enabled
    4-byte-as capability has been enabled
    Nexthop self has been configured
    Connect-interface has been configured
    GTSM has been enabled, valid-ttl-hops: 2
    Peer Preferred Value: 0
    Routing policy configured:
    No routing policy is configured
   ```
   
   The command output shows that GTSM has been enabled, the number of valid hops is 2, and the BGP connection state is **Established**.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In this example, if the value of **valid-ttl-hops** of either DeviceB or DeviceD is less than 2, the IBGP connection cannot be established.
   * GTSM must be enabled on both ends of a BGP connection.
9. Verify the configuration.
   
   
   
   # Run the **display gtsm statistics all** command on DeviceB to check GTSM statistics. If the default action is set to pass for the messages that do not match the specified GTSM policy and no invalid messages exist, the number of dropped messages is 0.
   
   ```
   <DeviceB> display gtsm statistics all
   ```
   ```
   GTSM Statistics Table
   ----------------------------------------------------------------
   SlotId  Protocol  Total Counters  Drop Counters  Pass Counters
   ----------------------------------------------------------------
    0      BGP       17              0              17
    0      BGPv6     0               0              0
    0      OSPF      0               0              0
    0      LDP       0               0              0
    0      OSPFv3    0               0              0 
    0      RIP       0               0              0 
    1      BGP       0               0              0
    1      BGPv6     0               0              0
    1      OSPF      0               0              0
    1      LDP       0               0              0
    1      OSPFv3    0               0              0 
    1      RIP       0               0              0 
    2      BGP       0               0              0
    2      BGPv6     0               0              0
    2      OSPF      0               0              0
    2      LDP       0               0              0
    2      OSPFv3    0               0              0 
    2      RIP       0               0              0 
    3      BGP       0               0              0
    3      BGPv6     0               0              0
    3      OSPF      0               0              0
    3      LDP       0               0              0
    3      OSPFv3    0               0              0 
    3      RIP       0               0              0 
    4      BGP       32              0              32
    4      BGPv6     0               0              0
    4      OSPF      0               0              0
    4      LDP       0               0              0
    4      OSPFv3    0               0              0 
    4      RIP       0               0              0 
    5      BGP       0               0              0
    5      BGPv6     0               0              0
    5      OSPF      0               0              0
    5      LDP       0               0              0
    5      OSPFv3    0               0              0 
    5      RIP       0               0              0 
    7      BGP       0               0              0
    7      BGPv6     0               0              0
    7      OSPF      0               0              0
    7      LDP       0               0              0
    7      OSPFv3    0               0              0 
    7      RIP       0               0              0 
   ----------------------------------------------------------------
   ```
   
   In this case, if the PC simulates the BGP messages of DeviceA to attack DeviceB, the messages are dropped when they reach DeviceB. This is because the TTL value is not 255. As a result, the number of dropped messages increases in the GTSM statistics about DeviceB.

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
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 10
  ```
  ```
   router-id 10.1.1.9
  ```
  ```
   peer 10.1.1.2 as-number 20
  ```
  ```
   peer 10.1.1.2 valid-ttl-hops 1
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer 10.1.1.2 enable
  ```
  ```
  #
  ```
  ```
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
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   ip address 10.2.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 10.2.2.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 20
  ```
  ```
   router-id 10.2.2.9
  ```
  ```
   peer 10.3.3.9 as-number 20
  ```
  ```
   peer 10.3.3.9 valid-ttl-hops 1
  ```
  ```
   peer 10.3.3.9 connect-interface LoopBack0
  ```
  ```
   peer 10.4.4.9 as-number 20
  ```
  ```
   peer 10.4.4.9 valid-ttl-hops 2
  ```
  ```
   peer 10.4.4.9 connect-interface LoopBack0
  ```
  ```
   peer 10.1.1.1 as-number 10
  ```
  ```
   peer 10.1.1.1 valid-ttl-hops 1
  ```
  ```
  #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
   import-route ospf 1
  ```
  ```
    peer 10.3.3.9 enable
  ```
  ```
    peer 10.3.3.9 next-hop-local
  ```
  ```
    peer 10.4.4.9 enable
  ```
  ```
    peer 10.4.4.9 next-hop-local
  ```
  ```
    peer 10.1.1.1 enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.2.1.0 0.0.0.255
  ```
  ```
    network 10.2.2.9 0.0.0.0
  ```
  ```
  #
  ```
  ```
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
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.2.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   ip address 10.2.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 10.3.3.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 20
  ```
  ```
   router-id 10.3.3.9
  ```
  ```
   peer 10.2.2.9 as-number 20
  ```
  ```
   peer 10.2.2.9 valid-ttl-hops 1
  ```
  ```
   peer 10.2.2.9 connect-interface LoopBack0
  ```
  ```
   peer 10.4.4.9 as-number 20
  ```
  ```
   peer 10.4.4.9 valid-ttl-hops 1
  ```
  ```
   peer 10.4.4.9 connect-interface LoopBack0
  ```
  ```
  #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer 10.2.2.9 enable
  ```
  ```
    peer 10.4.4.9 enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.2.1.0 0.0.0.255
  ```
  ```
    network 10.2.2.0 0.0.0.255
  ```
  ```
    network 10.3.3.9 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceD
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.2.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 10.4.4.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 20
  ```
  ```
   router-id 10.4.4.9
  ```
  ```
   peer 10.2.2.9 as-number 20
  ```
  ```
   peer 10.2.2.9 valid-ttl-hops 2
  ```
  ```
   peer 10.2.2.9 connect-interface LoopBack0
  ```
  ```
   peer 10.3.3.9 as-number 20
  ```
  ```
   peer 10.3.3.9 valid-ttl-hops 1
  ```
  ```
   peer 10.3.3.9 connect-interface LoopBack0
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer 10.2.2.9 enable
  ```
  ```
    peer 10.3.3.9 enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.2.2.0 0.0.0.255
  ```
  ```
    network 10.4.4.9 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```