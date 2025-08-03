display bgp vpn-instance peer verbose
=====================================

display bgp vpn-instance peer verbose

Function
--------

The **display bgp vpn-instance peer verbose** command displays detailed information about BGP peers.



Format
------

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **peer** **verbose**

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **peer** *ipv4-address* **verbose**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **peer** **verbose**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **peer** *ipv4-address* **verbose**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed information about peers. | - |
| **vpnv4** | Displays information about peers in a VPNv4 instance. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *ipv4-address* | Specify an IPv4 peer address. | The value is in dotted decimal notation. |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

The **display bgp peer verbose** command displays BGP peer detailed information. You can implement the following operations based on the command output:

* To check the status of BGP connections
* To check information about a BGP peer
* To check whether a BGP peer is configured using the **peer as-number** command
* To check whether a BGP peer is deleted using the **undo peer as-number** command

**Precautions**

BGP has multiple address and sub-address families. By default, the **display bgp peer** command displays information about BGP peers in IPv4 unicast address family only. If you want to view information about BGP peers in another address family, specify its address family parameter.

To view detailed information about a BGP peer, such as information about BGP timers, the number of sent and received routes, capacities supported, the number of sent and received BGP messages, and enabled functions, specify verbose in the command.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display detailed information about the peer 10.1.1.2.
```
<HUAWEI> display bgp vpnv4 vpn-instance vrf peer 10.1.1.2 verbose

         BGP Peer is 10.1.1.2,  remote AS 200
         Type: EBGP link
         BGP version 4, Remote router ID 10.1.1.2
         Update-group ID: 5
         BGP current state: Established, Up for 00h03m46s
         BGP current event: KATimerExpired
         BGP last state: OpenConfirm
         BGP Peer Up count: 1
         Received total routes: 0
         Received active routes total: 0
         Advertised total routes: 0
         Port: Local - 179        Remote - 50525
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
 Received: Total 7 messages
                  Update messages                1
                  Open messages                  1
                  KeepAlive messages             5
                  Notification messages          0
                  Refresh messages               0
 Sent: Total 7 messages
                  Update messages                1
                  Open messages                  1
                  KeepAlive messages             5
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
 Last keepalive received: 2020-01-28 13:39:53+00:00
 Last keepalive sent    : 2020-01-28 13:40:21+00:00
 Last update    received: 2020-01-28 13:36:41+00:00
 Last update    sent    : 2020-01-28 13:36:41+00:00
 No refresh received since peer has been configured
 No refresh sent since peer has been configured
 Minimum route advertisement interval is 30 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 4-byte-as capability has been enabled
 Peer Preferred Value: 0
 Routing policy configured:
 No routing policy is configured

```

# Display detailed information about the BGP peer of the VPN instance vrf.
```
<HUAWEI> display bgp vpnv4 vpn-instance vrf peer verbose

         BGP Peer is 10.1.1.2,  remote AS 200
         Type: EBGP link
         BGP version 4, Remote router ID 10.1.1.2
         Update-group ID: 5
         BGP current state: Established, Up for 00h00m52s
         BGP current event: KATimerExpired
         BGP last state: OpenConfirm
         BGP Peer Up count: 1
         Received total routes: 0
         Received active routes total: 0
         Advertised total routes: 0
         Port: Local - 179        Remote - 50525
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
 Received: Total 4 messages
                  Update messages                1
                  Open messages                  1
                  KeepAlive messages             2
                  Notification messages          0
                  Refresh messages               0
 Sent: Total 4 messages
                  Update messages                1
                  Open messages                  1
                  KeepAlive messages             2
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
 Last keepalive received: 2020-01-28 13:37:29+00:00
 Last keepalive sent    : 2020-01-28 13:37:32+00:00
 Last update    received: 2020-01-28 13:36:41+00:00
 Last update    sent    : 2020-01-28 13:36:41+00:00
 No refresh received since peer has been configured
 No refresh sent since peer has been configured
 Minimum route advertisement interval is 30 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 4-byte-as capability has been enabled
 Peer Preferred Value: 0
 Routing policy configured:
 No routing policy is configured

```


**Table 1** Description of the
**display bgp vpn-instance peer verbose** command output

| Item | Description |
| --- | --- |
| BGP version | BGP version. |
| BGP current state | Current BGP status:   * Idle: BGP denies any connection request. This is the initial status of BGP.   After receiving a Start event, BGP initiates a TCP connection to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: BGP is waiting for the TCP connection to be established before performing subsequent operations. * If the TCP connection is successfully established, BGP stops the ConnectRetry timer and sends an Open message to the peer. BGP then enters the Opensent state. * If the TCP connection fails to be established, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and attempts to establish a TCP connection with the peer again. At this time, BGP remains in the Connect state. * Active: BGP attempts to establish a TCP connection. This is the intermediate state of BGP. * If the TCP connection is successfully established, BGP restarts the ConnectRetry Timer with the initial value, sends an Open message to the remote peer, and changes its state to Opensent. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and enters the Connect state. * If BGP attempts to establish a TCP connection with an unknown IP address, the TCP connection fails, the ConnectRetry Timer is reset, and BGP remains in the Active state. * OpenSent: BGP has sent an Open message to the peer and is now waiting for an Open message from the peer. * If BGP receives a correct Open message, BGP enters the OpenConfirm state. * If the Open message received by BGP is incorrect, BGP sends a Notification message to the peer and enters the Idle state. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * OpenConfirm: BGP is waiting for a Notification message or a Keepalive message. * If BGP receives a Notification message or a TCP connection teardown message, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP enters the Established state. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or Keepalive message, BGP remains in the Established state. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other successfully negotiated address families. If the address family is enabled on the remote BGP peer, the local BGP peer receives a Notification message, disconnects from the remote BGP peer, changes to the Idle state, and re-establishes a connection with the remote BGP peer. |
| BGP current event | Current BGP event. |
| BGP last state | State of last BGP stage, The possible states are Idle, Connect, Active, OpenSent, OpenConfirm, Established, and No neg. |
| BGP Peer Up count | Number of times the BGP peer flaps within a specified period. |
| Peer Preferred Value | Preferred value of the BGP peer. |
| Peer optional capabilities | Optional capabilities supported by the peer. |
| Remote router ID | Router ID of the peer. |
| Update-group ID | ID of the Update group to which a peer belongs. |
| Received total routes | Number of route prefixes received. |
| Received active routes total | Number of received active route prefixes. |
| Received : Active Hold Time | Hold time of the peer. |
| Received | Number of packets received from neighbors:   * Total: total number of records. * Update messages: number of Update messages. * Open messages: number of Open messages. * KeepAlive messages: number of Keepalive messages. * Number of Notification messages:Notification packets. * Refresh messages: number of Route-refresh messages. |
| Advertised total routes | Number of route prefixes sent. |
| Keepalive Time | Interval at which Keepalive messages are sent to the peer. |
| Negotiated: Active Hold Time | Hold time agreed between the BGP peers after capability negotiation. |
| Address family IPv4 Unicast | IPv4 unicast address family. |
| Authentication type configured | Configured authentication type. |
| Last keepalive received | Time when a Keepalive message was last received. |
| Last keepalive sent | Time when the last Keepalive message was sent. |
| Minimum route advertisement interval is 30 seconds | Minimum route advertisement interval.   * The minimum interval at which EBGP routes are advertised is 30 seconds. * The minimum interval at which IBGP routes are advertised is 15 seconds. |
| Optional capabilities | Optional capabilities supported by the BGP peer. |
| Route refresh capability has been enabled | Route refreshing has been enabled. |
| Routing policy configured | Indicates the configured routing policy. |
| Type | BGP link type, which can be either IBGP Link or EBGP Link. |
| Port | Port type:   * Local: indicates the local port number, which is always 179. BGP uses TCP at the transport layer. * Remote: indicates the port number used on the peer. |
| Configured | Locally configured timers.   * Active Hold Time: indicates the hold time. If BGP does not receive any Keepalive message from the peer in the hold time, BGP considers that the peer is down and then instructs other peers to remove the routes that are received from the peer. * Keep Alive Time: indicates the interval at which Keepalive messages are sent to the peer. BGP peers exchange Keepalive messages periodically to notify each other that they are in the Active state. |
| Sent | Number of messages sent to a peer.   * Total: indicates the total number of messages sent to a peer. * Update messages: indicates the number of Update messages sent to a peer. * Open messages: indicates the number of Open messages sent to a peer. * KeepAlive messages: indicates the number of Keepalive messages sent to a peer. * Notification messages: indicates the number of Notification messages sent to a peer. * Refresh messages: indicates the number of route-refresh messages sent to a peer. |