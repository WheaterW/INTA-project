display bgp vpnv4 all peer verbose
==================================

display bgp vpnv4 all peer verbose

Function
--------



The **display bgp vpnv4 all peer verbose** command displays detailed information about BGP peers in the BGP-VPNv4 address family.




Format
------

**display bgp vpnv4 all peer** [ *ipv4-address* ] **verbose**

**display bgp instance** *instance-name* **vpnv4** **all** **peer** [ *ipv4-address* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specify an IPv4 peer address. | The value is in dotted decimal notation. |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv4 all peer verbose** command displays information about BGP peers in the BGP-VPNv4 address family. You can run the command as required:

* Check the connection status of BGP peers.
* Check the configuration of BGP peers.
* After running the **peer as-number** command to configure a BGP peer, check whether the configuration is successful.
* After running the **undo peer as-number** command to delete a BGP peer, check whether the BGP peer is successfully deleted.The **display bgp vpnv4 all peer verbose** command can be used to locate faults. For example, when a peer is disconnected, you can view the log information of the specified peer to know the time when the peer is disconnected and the cause of the disconnection (error code and sub-error code).

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about VPNv4 peers.
```
<HUAWEI> display bgp vpnv4 all peer verbose
 BGP Peer is 2.2.2.2,  remote AS 100
 Type: IBGP link
 BGP version 4, Remote router ID 2.2.2.2
 Update-group ID: 3
 BGP current state: Established, Up for 01h12m50s
 BGP current event: RecvKeepalive
 BGP last state: OpenConfirm
 BGP Peer Up count: 1
 Received total routes: 0
 Received active routes total: 0
 Advertised total routes: 1
 Port: Local - 179        Remote - 58368
 Configured: Connect-retry Time: 32 sec
 Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Received  : Active Hold Time: 180 sec
 Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Peer optional capabilities:
  Peer supports bgp multi-protocol extension
  Peer supports bgp route refresh capability
  Peer supports bgp 4-byte-as capability
  Address family IPv4 Unicast: advertised and received
  Address family VPNv4 Unicast: advertised and received
 Received:
                  Total  messages                88
                  Update messages                2
                  Open messages                  1
                  KeepAlive messages             84
                  Notification messages          0
                  Refresh messages               1
 Sent    :
                  Total  messages                97
                  Update messages                11
                  Open messages                  1
                  KeepAlive messages             85
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
  Last keepalive received: 2015-01-07 09:48:41+00:00
  Last keepalive sent    : 2015-01-07 09:48:41+00:00
  Last update received   : 2015-01-07 08:36:31+00:00
  Last update sent       : 2015-01-07 09:34:22+00:00
  Last refresh received  : 2015-01-07 08:37:36+00:00
  No refresh sent since peer has been configured
 Minimum route advertisement interval is 0 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 4-byte-as capability has been enabled
 Connect-interface has been configured
 Send remote-nexthop has been configured
 Peer Preferred Value: 0
 Routing policy configured:
 No routing policy is configured

```

**Table 1** Description of the **display bgp vpnv4 all peer verbose** command output
| Item | Description |
| --- | --- |
| BGP version | BGP version. |
| BGP current state | State of BGP:   * Idle: indicates that BGP denies any request of entering. This is the initiatory status of BGP.   Upon receiving a Start event, BGP initiates a TCP connection request to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: indicates that BGP is waiting for the TCP connection to be set up before it determines whether to perform other operations. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value, initiates a TCP connection request to the remote BGP peer, and stays in the Connect state. * Active: indicates that BGP tries to set up a TCP connection. This is the intermediate status of BGP. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value and changes its state to Connect. * If BGP initiates a TCP connection request with an unknown IP address, the TCP connection fails. When this occurs, BGP restarts the ConnectRetry Timer with the initial value and stays in the Active state. * OpenSent: indicates that BGP has sent one Open message to its peer and is waiting for the other Open message from the peer. * If there are no errors in the Open message received, BGP changes its state to OpenConfirm. * If there are errors in the Open message received, BGP sends a Notification message to the remote peer and changes its state to Idle. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * OpenConfirm: indicates that BGP is waiting for a Notification or Keepalive message. * If BGP receives a Notification message, or the TCP connection fails, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP changes its state to Established. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or a Keepalive message, its state stays in Established. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| BGP current event | Current BGP event. |
| BGP last state | State of last BGP stage, The possible states are Idle, Connect, Active, OpenSent, OpenConfirm, Established, and No neg. |
| BGP Peer Up count | Number of times the BGP peer flaps. |
| BGP Peer | Peer IP address. |
| Peer Preferred Value | PrefVal of the peer. |
| Peer optional capabilities | Optional capabilities supported by the peer. |
| remote AS | AS Number of the peer. |
| Update-group ID | ID of the Update group to which a peer belongs. |
| Received total routes | Number of received route prefixes. |
| Received active routes total | Number of active route prefixes received. |
| Received | Number of messages received from the peerr:   * Total: total number of records. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Received : Active Hold Time | Active Hold Time: Hold time determined by BGP peers after capability negotiation. |
| Advertised total routes | Number of route prefixes sent. |
| Keepalive Time | Interval for sending Keepalive messages to the peer. |
| Address family IPv4 Unicast | IPv4 unicast address family. |
| Address family VPNv4 Unicast | VPNv4 address family. |
| Sent | Number of packets sent to peers:   * Total: total number of records. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Authentication type configured | Configured authentication type. |
| Last keepalive received | Time when a Keepalive message was last received. |
| Last refresh received | Time when a Refresh message was last received. |
| Last update received | Last time when an Update message is received. |
| Last update sent | Last time when an Update message is sent. |
| Last keepalive sent | Time at which the last keepalive message is sent. |
| Optional capabilities | Optional capabilities of the peer. |
| Route refresh capability has been enabled | Route-refresh enabled. |
| Routing policy configured | Configured routing policy. |
| Type | BGP link type (IBGP or EBGP). |
| Port | Port number.   * Local: local port number. BGP uses TCP as the transport layer protocol and uses the fixed port number 179. * Remote: indicates the port number of the peer. |
| Configured | Locally configured timers:   * Active Hold Time: If BGP does not receive any Keepalive message from a peer within the Hold Time, BGP considers the peer Down and instructs other peers to withdraw the routes received from the peer in the Down state. * Keepalive Time: indicates the interval for sending Keepalive messages to the peer. BGP peers send Keepalive messages to each other periodically to notify each other that they are working properly. |
| Negotiated | * Active Hold Time: indicates the hold time of the peer. * Keepalive Time: indicates the interval for sending Keepalive messages to the peer. BGP peers send Keepalive messages to each other periodically to notify each other that they are working properly. |