display bgp unnumbered peer verbose
===================================

display bgp unnumbered peer verbose

Function
--------



The **display bgp unnumbered peer verbose** command displays detailed information about unnumbered BGP peers.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp unnumbered peer verbose**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp ipv6 unnumbered peer verbose**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp unnumbered peer verbose** command displays detailed information about unnumbered BGP peers.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about BGP unnumbered peers.
```
<HUAWEI> display bgp unnumbered peer verbose

 BGP Peer is FE80::3A01:FF:FE21:301(100GE1/0/1),  remote AS 100
 Type: IBGP link
 Unnumbered peer
 Belong to peer-group: i
 BGP version 4, Remote router ID 10.1.1.2
 Update-group ID: 7
 BGP current state: Established, Up for 00h01m40s
 BGP current event: RecvKeepalive
 BGP last state: OpenConfirm
 BGP Peer Up count: 1
 Received total routes: 2
 Received active routes total: 0
 Advertised total routes: 3
 Port: Local - 179        Remote - 64844
 Configured: Connect-retry Time: 32 sec
 Configured: Min Hold Time: 0 sec
 Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Received  : Active Hold Time: 180 sec
 Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Peer optional capabilities:
  Peer supports bgp multi-protocol extension
  Peer supports bgp route refresh capability
  Peer supports bgp 4-byte-as capability
  Address family IPv4 Unicast: advertised and received
  Address family IPv6 Unicast: advertised and received
 Received:      
                  Total  messages                8
                  Update messages                4
                  Open messages                  1
                  KeepAlive messages             3
                  Notification messages          0
                  Refresh messages               0
 Sent    :      
                  Total  messages                14
                  Update messages                9
                  Open messages                  2
                  KeepAlive messages             3
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
  Last keepalive received: 2021-07-15 12:42:31+00:00
  Last keepalive sent    : 2021-07-15 12:42:24+00:00
  Last update received   : 2021-07-15 12:40:53+00:00
  Last update sent       : 2021-07-15 12:41:08+00:00
  No refresh received since peer has been configured
  No refresh sent since peer has been configured
 Minimum route advertisement interval is 15 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 Extended Next Hop Encoding capability has been enabled
 4-byte-as capability has been enabled
 Nexthop self has been configured
 Soft-Reconfiguration has been enabled
 Send community has been configured
 Send extend community has been configured
 Send large community has been configured
 It's route-reflector-client
 Default route advertise has been configured 
 Connect-interface has been configured
 Peer Preferred Value: 0
 Routing policy configured:
 No import update filter list
 No export update filter list
 No import prefix list
 No export prefix list
 Import route policy is: import
 Export route policy is: a
 No import distribute policy
 No export distribute policy
 No import route filter
 No export route filter

```

# Display detailed information about BGP IPv6 unnumbered peers.
```
<HUAWEI> display bgp ipv6 unnumbered peer verbose

 BGP Peer is FE80::3A01:FF:FE21:301(100GE1/0/1),  remote AS 100
 Type: IBGP link
 Unnumbered peer
 Belong to peer-group: i
 BGP version 4, Remote router ID 10.1.1.2
 Update-group ID: 5
 BGP current state: Established, Up for 03h59m14s
 BGP current event: RecvKeepalive
 BGP last state: OpenConfirm
 BGP Peer Up count: 1
 Received total routes: 2
 Received active routes total: 1
 Advertised total routes: 2
 Port: Local - 49918        Remote - 179
 Configured: Connect-retry Time: 32 sec
 Configured: Min Hold Time: 0 sec
 Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Received  : Active Hold Time: 180 sec
 Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Peer optional capabilities:
  Peer supports bgp multi-protocol extension
  Peer supports bgp route refresh capability
  Peer supports bgp 4-byte-as capability
  Address family IPv4 Unicast: advertised and received
  Address family IPv6 Unicast: advertised and received
 Received:      
                  Total  messages                282
                  Update messages                4
                  Open messages                  1
                  KeepAlive messages             277
                  Notification messages          0
                  Refresh messages               0
 Sent    :      
                  Total  messages                289
                  Update messages                10
                  Open messages                  2
                  KeepAlive messages             276
                  Notification messages          1
                  Refresh messages               0
 Authentication type configured: None
  Last keepalive received: 2021-07-20 07:37:07+00:00
  Last keepalive sent    : 2021-07-20 07:36:54+00:00
  Last update received   : 2021-07-20 03:38:31+00:00
  Last update sent       : 2021-07-20 03:38:50+00:00
  No refresh received since peer has been configured
  No refresh sent since peer has been configured
 Minimum route advertisement interval is 15 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 4-byte-as capability has been enabled
 Soft-Reconfiguration has been enabled
 Default route advertise has been configured 
 Connect-interface has been configured
 Peer Preferred Value: 0
 Routing policy configured:
 No import update filter list
 No export update filter list
 No import prefix list
 No export prefix list
 Import route policy is: import
 Export route policy is: a
 No import distribute policy
 No export distribute policy
 No import route filter
 No export route filter

```

**Table 1** Description of the **display bgp unnumbered peer verbose** command output
| Item | Description |
| --- | --- |
| BGP version | BGP version. |
| BGP current state | Current BGP status:   * Idle: BGP denies any connection request. This is the initial status of BGP.   After receiving a Start event, BGP initiates a TCP connection to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: BGP is waiting for the TCP connection to be established before performing subsequent operations. * If the TCP connection is successfully established, BGP stops the ConnectRetry timer and sends an Open message to the peer. BGP then enters the Opensent state. * If the TCP connection fails to be established, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and attempts to establish a TCP connection with the peer again. At this time, BGP remains in the Connect state. * Active: BGP attempts to establish a TCP connection. This is the intermediate state of BGP. * If the TCP connection is successfully established, BGP restarts the ConnectRetry Timer with the initial value, sends an Open message to the remote peer, and changes its state to Opensent. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and enters the Connect state. * If BGP attempts to establish a TCP connection with an unknown IP address, the TCP connection fails, the ConnectRetry Timer is reset, and BGP remains in the Active state. * OpenSent: BGP has sent an Open message to the peer and is now waiting for an Open message from the peer. * If BGP receives a correct Open message, BGP enters the OpenConfirm state. * If the Open message received by BGP is incorrect, BGP sends a Notification message to the peer and enters the Idle state. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * OpenConfirm: BGP is waiting for a Notification message or a Keepalive message. * If BGP receives a Notification message or a TCP connection teardown message, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP enters the Established state. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or Keepalive message, BGP remains in the Established state. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other successfully negotiated address families. If the address family is enabled on the remote BGP peer, the local BGP peer receives a Notification message, disconnects from the remote BGP peer, changes to the Idle state, and re-establishes a connection with the remote BGP peer. |
| BGP current event | Current BGP event. |
| BGP last state | State of last BGP stage, which can be Idle, Connect, Active, OpenSent, OpenConfirm, Established, or No neg. |
| BGP Peer Up count | Number of times the BGP peer flaps. |
| BGP Peer is | BGP peer. |
| Peer optional capabilities | Optional capabilities supported by the peer. |
| Peer Preferred Value | Preferred value of the peer. |
| Remote router ID | Router ID of the peer. |
| Update-group ID | ID of the update-peer group to which the peer belongs. |
| Received total routes | Number of received route prefixes. |
| Received active routes total | Number of received active route prefixes. |
| Received : Active Hold Time | Hold time of the peer. |
| Received | Number of packets received from the peer:   * Total: total number of records. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Advertised total routes | Number of sent route prefixes. |
| Keepalive Time | Interval for sending Keepalive packets to the peer. |
| Address family IPv4 Unicast | IPv4 unicast address family. |
| Address family IPv6 Unicast | IPv6 unicast address family. |
| Sent | Number of packets sent to the peer:   * Total: total number of records. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Authentication type configured | Authentication type. |
| Last keepalive received | Time when a Keepalive message was last received. |
| Last keepalive sent | Time when a Keepalive message was last sent. |
| Last update received | Last time when an Update message is received. |
| Last update sent | Last time when an Update message is sent. |
| Minimum route advertisement interval is 15 seconds | Minimum interval at which routes are advertised: |
| Optional capabilities | Capabilities supported by the peer (optional). |
| Route refresh capability has been enabled | Route-refresh enabled. |
| Routing policy configured | Configured routing policy. |
| Import route policy is | Import routing policy. |
| Export route policy is | Export routing policy. |
| Type | BGP link type, which can be IBGP Link or EBGP Link. |
| Port | * Local: local port number. BGP uses TCP as the transport layer protocol and uses the fixed port number 179. * Remote: indicates the port number of the peer. |
| Configured | Locally configured timers:   * Active Hold Time: If BGP does not receive any Keepalive message from a peer within the Hold Time, BGP considers that the peer is Down. In this case, BGP instructs other peers to withdraw the routes received from the peer that is Down. * Keep Alive Time: indicates the interval for sending Keepalive messages to the peer. BGP peers send Keepalive messages to each other periodically to advertise their working status. |
| Negotiated : Active Hold Time | Hold time negotiated by BGP peers. |
| Negotiated | Negotiated value of the timer. |