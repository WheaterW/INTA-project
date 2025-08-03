display bgp mvpn all peer verbose
=================================

display bgp mvpn all peer verbose

Function
--------



The **display bgp mvpn all peer verbose** command displays detailed information about peers in the BGP-MVPN address family.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp mvpn all peer** [ *ipv4-address* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specify an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Users can run this command to view detailed information about MVPN BGP neighbors, such as BGP timer information, number of sent and received routes, capabilities supported by neighbors, number of sent and received BGP messages, and enabled configurations.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about peers in the BGP-MVPN address family.
```
<HUAWEI> display bgp mvpn all peer verbose

         BGP Peer is 10.1.2.3,  remote AS 100
         Type: IBGP link
         BGP version 4, Remote router ID 10.1.2.3
         Update-group ID: 4
         BGP current state: Established, Up for 02h34m25s
         BGP current event: KATimerExpired
         BGP last state: OpenConfirm
         BGP Peer Up count: 8
         Received total routes: 2
         Received active routes total: 2
         Advertised total routes: 1
         Port: Local - 179        Remote - 57720
         Configured: Connect-retry Time: 32 sec
         Configured: Min Hold Time: 0 sec
         Configured: Active Hold Time: 15 sec   Keepalive Time:5 sec
         Received  : Active Hold Time: 15 sec
         Negotiated: Active Hold Time: 15 sec   Keepalive Time:5 sec
         Peer optional capabilities:
         Peer supports bgp multi-protocol extension
         Peer supports bgp route refresh capability
         Peer supports bgp 4-byte-as capability
         Address family IPv4 Unicast: advertised and received
         Address family IPv4 MVPN: advertised and received
         Address family VPNv4 Unicast: advertised and received
 Received: Total 2396 messages
                  Update messages                10
                  Open messages                  1
                  KeepAlive messages             2385
                  Notification messages          0
                  Refresh messages               0
 Sent: Total 2405 messages
                  Update messages                5
                  Open messages                  1
                  KeepAlive messages             2399
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
 Last keepalive received: 2020-09-11 17:51:44+00:00
 Last keepalive sent    : 2020-09-11 17:51:45+00:00
 Last update    received: 2020-09-11 15:17:22+00:00
 Last update    sent    : 2020-09-11 15:17:22+00:00
 No refresh received since peer has been configured
 No refresh sent since peer has been configured
 Minimum route advertisement interval is 15 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 4-byte-as capability has been enabled
 Connect-interface has been configured
 Peer Preferred Value: 0
 Memory Priority: medium
 Routing policy configured:
 No routing policy is configured

```

**Table 1** Description of the **display bgp mvpn all peer verbose** command output
| Item | Description |
| --- | --- |
| BGP version | BGP version. |
| BGP current state | State of BGP:   * Idle: indicates that BGP denies any request of entering. This is the initiatory status of BGP.   Upon receiving a Start event, BGP initiates a TCP connection request to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: indicates that BGP is waiting for the TCP connection to be set up before it determines whether to perform other operations. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value, initiates a TCP connection request to the remote BGP peer, and stays in the Connect state. * Active: indicates that BGP tries to set up a TCP connection. This is the intermediate status of BGP. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value and changes its state to Connect. * If BGP initiates a TCP connection request with an unknown IP address, the TCP connection fails. When this occurs, BGP restarts the ConnectRetry Timer with the initial value and stays in the Active state. * OpenSent: indicates that BGP has sent one Open message to its peer and is waiting for the other Open message from the peer. * If there are no errors in the Open message received, BGP changes its state to OpenConfirm. * If there are errors in the Open message received, BGP sends a Notification message to the remote peer and changes its state to Idle. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * OpenConfirm: indicates that BGP is waiting for a Notification or Keepalive message. * If BGP receives a Notification message, or the TCP connection fails, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP changes its state to Established. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or a Keepalive message, its state stays in Established. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| BGP current event | Current BGP event. |
| BGP last state | State of last BGP stage, The possible states are Idle, Connect, Active, OpenSent, OpenConfirm, Established, and No neg. |
| BGP Peer Up count | Number of times the BGP peer flaps. |
| Peer optional capabilities | Optional capabilities supported by the peer. |
| Peer Preferred Value | PrefVal of the peer. |
| Remote router ID | Router ID of a peer. |
| Update-group ID | ID of the Update group to which a peer belongs. |
| Received total routes | Number of received route prefixes. |
| Received active routes total | Number of active route prefixes received. |
| Received | Active Hold Time indicates the hold time of the peer.  Number of messages received from the peer:   * Total: total number of records. * Update messages: number of Update messages. * Open messages: number of Open messages. * KeepAlive messages: number of Keepalive messages. * Notification messages: number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Advertised total routes | Number of route prefixes sent. |
| Address family IPv4 Unicast | IPv4 unicast address family. |
| Address family IPv4 MVPN | MVPN address family. |
| Address family VPNv4 Unicast | VPNv4 address family. |
| Authentication type configured | Authentication type that is configured. |
| Last keepalive received | Time when a Keepalive message was last received. |
| Last keepalive sent | Time when a Keepalive message was last sent. |
| No routing policy is configured | No routing policy is configured. |
| Minimum route advertisement interval is 15 seconds | Minimum interval at which routes are advertised. |
| Optional capabilities | Optional capabilities of the peer. |
| Route refresh capability has been enabled | Route-refresh enabled. |
| Memory Priority | The priority for a BGP peer relationship to be disconnected if memory overload occurs. |
| Routing policy configured | Configured routing policy. |
| Type | BGP link type (IBGP or EBGP). |
| Port | Port number.   * Local: local port number. BGP uses TCP as the transport layer protocol and uses the fixed port number 179. * Remote: indicates the port number of the peer. |
| Configured | Locally configured timers:   * Active Hold Time: If BGP does not receive any Keepalive message from a peer within the Hold Time, BGP considers the peer Down and instructs other peers to withdraw the routes received from the peer in the Down state. * Keepalive Time: indicates the interval for sending Keepalive messages to the peer. BGP peers send Keepalive messages to each other periodically to notify each other that they are working properly. |
| Negotiated | * Active Hold Time indicates the hold time determined by BGP peers after capability negotiation. * Keepalive Time: indicates the interval for sending Keepalive messages to the peer. BGP peers send Keepalive messages to each other periodically to notify each other that they are working properly. |
| Sent | Number of messages sent to a peer.   * Total: indicates the total number of messages sent to a peer. * Update messages: indicates the number of Update messages sent to a peer. * Open messages: indicates the number of Open messages sent to a peer. * KeepAlive messages: indicates the number of Keepalive messages sent to a peer. * Notification messages: indicates the number of Notification messages sent to a peer. * Refresh messages: indicates the number of route-refresh messages sent to a peer. |