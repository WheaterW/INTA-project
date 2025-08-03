display bgp evpn peer verbose
=============================

display bgp evpn peer verbose

Function
--------



The **display bgp evpn peer verbose** command displays detailed information about BGP EVPN peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn peer** [ *ipv4-address* ] **verbose**

**display bgp** [ **instance** *instance-name* ] **evpn** **peer** [ *ipv4-address* ] **verbose**

**display bgp evpn peer** *ipv6-address* **verbose**

**display bgp** [ **instance** *instance-name* ] **evpn** **peer** *ipv6-address* **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a BGP EVPN peer. | The value is in dotted decimal notation. |
| **instance** *instance-name* | Displays the information about BGP EVPN peers of a specified BGP instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ipv6-address* | Specifies the IPv6 address of a BGP EVPN peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the following detailed information about BGP EVPN peers, run the display bgp evpn peer verbose command:

* Status of connections between BGP EVPN peers
* Configuration information about BGP EVPN peers
* Whether BGP EVPN peers are successfully configured using the **peer enable** command
* Whether BGP EVPN peers are successfully deleted using the **undo peer enable** command

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the peer 10.3.3.3.
```
<HUAWEI> display bgp evpn peer 10.3.3.3 verbose
BGP Peer is 10.3.3.3,  remote AS 100
 Type: IBGP link
 BGP version 4, Remote router ID 192.168.63.130
 Update-group ID: 1
 BGP current state: Established, Up for 06h58m12s
 BGP current event: KATimerExpired
 BGP last state: OpenConfirm
 BGP Peer Up count: 1
 Received total routes: 1
 Received active routes total: 1
 Advertised total routes: 1
 Port: Local - 179        Remote - 65085
 Configured: Connect-retry Time: 32 sec
 Configured: Min Hold Time: 0 sec
 Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Received  : Active Hold Time: 180 sec
 Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Peer optional capabilities:
  Peer supports bgp multi-protocol extension
  Peer supports bgp route refresh capability
  Peer supports bgp add-path capability
    EVPN address-family: both
  Negotiated bgp add-path capability
    EVPN address-family: both
  Peer supports bgp 4-byte-as capability
  Address family IPv4 Unicast: advertised and received
  Address family L2VPN EVPN: advertised and received
 Received:
                  Total  messages                486
                  Update messages                6
                  Open messages                  1
                  KeepAlive messages             479
                  Notification messages          0
                  Refresh messages               0
 Sent    :
                  Total  messages                486
                  Update messages                3
                  Open messages                  1
                  KeepAlive messages             482
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
  Last keepalive received: 2018-06-13 16:34:10+00:00
  Last keepalive sent    : 2018-06-13 16:34:33+00:00
  Last update received   : 2018-06-13 09:36:49+00:00
  Last update sent       : 2018-06-13 09:36:27+00:00
  No refresh received since peer has been configured
  No refresh sent since peer has been configured
 Minimum route advertisement interval is 15 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 4-byte-as capability has been enabled
 Connect-interface has been configured
 Peer Preferred Value: 0
 Split group configured:
 Peer limit state: true
 Pipe limit percent: 10
 Pipe limit count: 3
 Pipe last limit time: 2020-11-21 08:48:36
 Routing policy configured:
 No routing policy is configured

```

**Table 1** Description of the **display bgp evpn peer verbose** command output
| Item | Description |
| --- | --- |
| BGP Peer is 10.3.3.3 | BGP peer address (10.3.3.3). |
| BGP version | BGP version. |
| BGP current state | Current state of BGP:   * Idle: BGP denies any connection request. This is the initial state of BGP.   Upon receiving a Start event, BGP initiates a TCP connection to the remote BGP peer, starts the ConnectRetry timer with the initial value, and waits for a TCP message from the remote BGP peer. BGP then enters the Connect state.   * Connect: BGP is waiting for the TCP connection to be established before performing subsequent operations. * If the TCP connection is successfully established, BGP stops the ConnectRetry timer and sends an Open message to the peer. BGP then enters the Opensent state. * If the TCP connection fails to be established, BGP restarts the ConnectRetry Timer with the initial value and waits for a TCP connection request from the remote peer. BGP then enters the Active state. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and attempts to establish a TCP connection with the peer again. At this time, BGP remains in the Connect state. * Active: BGP tries to set up a TCP connection. This is the intermediate state of BGP. * If the TCP connection succeeds, BGP restarts the ConnectRetry Timer with the initial value and sends an Open message to the remote peer. BGP then enters the Opensent state. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and enters the Connect state. * If BGP EVPN fails to establish a TCP connection with an unknown IP address, BGP EVPN resets the ConnectRetry timer and remains in the Active state. * OpenSent: BGP has sent an Open message to the peer and is waiting for an Open message from the peer. * If BGP EVPN receives a correct Open message, BGP EVPN enters the OpenConfirm state. * If BGP receives an incorrect Open message, BGP sends a Notification message to the peer and enters the Idle state. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value and waits for a TCP connection request from the remote peer. BGP then enters the Active state. * OpenConfirm: BGP is waiting for a Notification message or a Keepalive message. * If BGP receives a Notification message or a TCP connection teardown message, BGP enters the Idle state. * If BGP receives a Keepalive message, BGP enters the Established state. * Established: BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or Keepalive message, BGP remains in the Established state. * If BGP receives a Notification message, BGP enters the Idle state. * No neg: The address family is not enabled on the peer. In this state, Update messages can be exchanged in other address families that have been successfully negotiated. If the address family is enabled on the peer, the local BGP peer disconnects from the peer after receiving a Notification message. Then, the local BGP peer enters the Idle state and re-establishes a connection with the peer. |
| BGP current event | Current BGP event. |
| BGP last state | State of last BGP stage, The possible states are Idle, Connect, Active, OpenSent, OpenConfirm, Established, and No neg. |
| BGP Peer Up count | Number of times the BGP peer alternates between Up and Down. |
| Peer optional capabilities | Optional capabilities of the peer. |
| Peer Preferred Value | PrefVal of the peer. |
| Peer limit state | Suppression status of the pipe for receiving packets from peers:   * true: suppressed. * false: not suppressed. |
| remote AS | AS number of the BGP peer. |
| Remote router ID | Router ID of a peer. |
| Update-group ID | ID of the Update group to which a peer belongs. |
| Received total routes | Number of received route prefixes. |
| Received active routes total | Number of active route prefixes received. |
| Received : Active Hold Time | Hold time of the peer. |
| Received | Number of packets received from a neighbor:   * Total messages: total number of messages. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Advertised total routes | Number of route prefixes sent. |
| Keepalive Time | Interval for sending Keepalive packets to the peer. |
| Negotiated: Active Hold Time | Hold time negotiated by BGP peers. |
| 4-byte-as capability has been enabled | 4-byte-As is enabled. |
| Sent | Number of packets sent to neighbors:   * Total messages: total number of messages. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Authentication type configured | Authentication type. |
| Last keepalive received | Last time when a Keepalive message is received. |
| Last keepalive sent | Time when a Keepalive message was last sent. |
| Last update received | Time when an Update message is last received. |
| Last update sent | Last time when an Update message is sent. |
| No refresh received since peer has been configured | No Route-Refresh messages are received from the peer after the peer relationship is established. |
| No refresh sent since peer has been configured | No Route-Refresh messages are sent to the peer after the peer relationship is established. |
| No routing policy is configured | No routing policy is configured. |
| Minimum route advertisement interval is 15 seconds | Minimum interval at which routes are advertised:   * EBGP: 30s. * IBGP: 15s. |
| Optional capabilities | Optional capabilities of the peer. |
| Route refresh capability has been enabled | Route-refresh enabled. |
| Connect-interface has been configured | Source interface used to send BGP messages. |
| Split group configured | Whether a split horizon group is configured. |
| Routing policy configured | Whether a routing policy has been configured. |
| Pipe limit percent | Rate limit percentage of the pipe for receiving neighbor packets. |
| Pipe limit count | Number of times rate limiting is performed on the pipe for receiving neighbor packets. |
| Pipe last limit time | Last time when the rate of the pipe for receiving neighbor packets was limited. |
| Type | BGP link type, which can only be IBGP link currently. |
| Port | Port number.:   * Local: local port number. BGP uses TCP as the transport layer protocol. The fixed port number is 179. * Remote: indicates the port number of the peer. |
| Configured | Locally configured timer:   * Active Hold Time: indicates the hold time. If BGP does not receive any Keepalive message from a peer within the hold time, BGP considers that the peer is Down and instructs other peers to withdraw the routes received from the peer. * Keep Alive Time: indicates the interval for sending Keepalive messages to the peer. BGP peers send Keepalive messages to each other periodically to notify each other that they are working normally. * Min Hold Time: indicates the minimum hold time. If the hold time configured on a peer is less than the minimum hold time configured on the local device, the two devices cannot establish a BGP peer relationship. However, if the hold time configured on the peer is 0, the rule does not take effect, and the peer relationship can still be established. * Connect-retry Time: specifies the ConnectRetry interval for a peer. When BGP initiates a TCP connection, the ConnectRetry timer is stopped if the TCP connection is established successfully. If the attempt to establish a TCP connection fails, BGP tries again to establish the TCP connection after the ConnectRetry timer expires. |