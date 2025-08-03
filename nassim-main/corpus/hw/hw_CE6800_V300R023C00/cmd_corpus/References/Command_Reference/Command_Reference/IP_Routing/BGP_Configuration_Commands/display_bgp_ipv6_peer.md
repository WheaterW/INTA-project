display bgp ipv6 peer
=====================

display bgp ipv6 peer

Function
--------



The **display bgp ipv6 slow-peer** command displays information about slow BGP IPv6 peers.

The **display bgp ipv6 peer** command displays information about BGP IPv6 peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 peer**

**display bgp ipv6 slow-peer**


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

To check information about slow BGP IPv6 peers, run the **display bgp ipv6 slow-peer** command. The information includes the time when a peer began to be identified as a slow peer, the time when a peer last exited from the slow peer state, the number of times a peer has been identified as a slow peer, and the remaining time for a peer to exit from the slow peer state.The**display bgp ipv6 peer** command displays BGP IPv6 peer information. You can implement the following operations based on the command output:

* To check the status of BGP connections
* To check information about a BGP peer
* To check whether a BGP peer is configured using the **peer as-number** command
* To check whether a BGP peer is deleted using the **undo peer as-number** commandThe display bgp peer command can be used for troubleshooting, with details as follows: If BGP peers are disconnected, specify log-info in the command to check the log information of the specified peer. In the command output, Date/Time indicates the time when the peers were disconnected, and Error Code and Error Subcode indicate the cause of the disconnection.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about IPv6 peers.
```
<HUAWEI> display bgp ipv6 peer

BGP Local router ID : 10.0.0.1
local AS number : 100
Total number of peers : 1                 Peers in established state : 1

Peer              V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
2001:DB8:20::21   4   200       17       19     0 00:09:59 Established       3

```

**Table 1** Description of the **display bgp ipv6 peer** command output
| Item | Description |
| --- | --- |
| BGP Local router ID | Router ID of the BGP local device.  If two ends have the same BGP local router ID, no BGP peer relationship can be established between them. In this situation, run the router id command in the BGP view on either end to change the BGP local router ID. Changing it to the IP address of a loopback interface is recommended. |
| local AS number | Local AS number. |
| AS | Autonomous system number. |
| Total number of peers | Number of BGP peers. |
| Peers in established state | Number of BGP peers in the Established state. |
| Peer | Peer IP address. |
| V | BGP version. |
| MsgRcvd | BGP version of a peer. |
| MsgSent | Number of messages sent. |
| OutQ | Number of messages waiting to be sent to a specified peer. |
| Up/Down | Duration of the BGP session staying in the current state.   * If the duration is less than 24 hours, it is displayed in the format of xx:xx:xx, indicating xx hours, xx minutes, and xx seconds. * If the duration is greater than 24 hours, it is displayed in the format of xxxxhxxm, indicating xxxx hours and xx minutes. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | Current BGP status:   * Idle: BGP denies any connection request. This is the initial status of BGP.   After receiving a Start event, BGP initiates a TCP connection to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: BGP is waiting for the TCP connection to be established before performing subsequent operations. * If the TCP connection is successfully established, BGP stops the ConnectRetry Timer, sends an Open message to the peer, and changes its state to Opensent. * If the TCP connection fails to be established, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and attempts to establish a TCP connection with the peer again. At this time, BGP remains in the Connect state. * Active: BGP attempts to establish a TCP connection. This is the intermediate state of BGP. * If the TCP connection is successfully established, BGP restarts the ConnectRetry Timer with the initial value, sends an Open message to the remote peer, and changes its state to Opensent. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and enters the Connect state. * If BGP attempts to establish a TCP connection with an unknown IP address, the TCP connection fails, the ConnectRetry Timer is reset, and BGP remains in the Active state. * OpenSent: BGP has sent an Open message to the peer and is now waiting for an Open message from the peer. * If BGP receives a correct Open message, BGP enters the OpenConfirm state. * If the Open message received by BGP is incorrect, BGP sends a Notification message to the peer and enters the Idle state. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * OpenConfirm: BGP is waiting for a Notification message or a Keepalive message. * If BGP receives a Notification message or a TCP connection teardown message, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP enters the Established state. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or Keepalive message, BGP remains in the Established state. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other successfully negotiated address families. If the address family is enabled on the remote BGP peer, the local BGP peer receives a Notification message, disconnects from the remote BGP peer, changes to the Idle state, and re-establishes a connection with the remote BGP peer. |
| PrefRcv | Number of route prefixes sent from the peer. |