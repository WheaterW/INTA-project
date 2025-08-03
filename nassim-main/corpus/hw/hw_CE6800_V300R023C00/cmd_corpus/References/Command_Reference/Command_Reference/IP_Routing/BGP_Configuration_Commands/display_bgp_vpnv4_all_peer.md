display bgp vpnv4 all peer
==========================

display bgp vpnv4 all peer

Function
--------



The **display bgp vpnv4 all peer** command displays information about all BGP VPNv4 peers.




Format
------

**display bgp vpnv4 all peer**

**display bgp instance** *instance-name* **vpnv4** **all** **peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv4 all peer** command can be used to locate faults. For example, when a peer is disconnected, you can view the log information of the specified peer to know the time when the peer is disconnected and the cause of the disconnection (error code and sub-error code).After slow BGP peer detection is enabled, you can run the **display bgp vpnv4 all peer** command to view information about slow BGP peers. The information includes the time when a peer began to be identified as a slow peer, the time when a peer last exited the slow peer state, the number of times a peer has been identified as a slow peer, and the remaining time for a peer to exit the slow peer state.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about peers.
```
<HUAWEI> display bgp vpnv4 all peer
 
 BGP local router ID : 10.1.1.1
 Local AS number : 100
 Total number of peers : 1                 Peers in established state : 1

  Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
  10.1.1.2                        4         100        7        7     0 00:03:04 Established        0

```

**Table 1** Description of the **display bgp vpnv4 all peer** command output
| Item | Description |
| --- | --- |
| Total number of peers | Number of current peers or slow peers. |
| Peer | Address of a peer or slow peer. |
| BGP local router ID | Local router ID of BGP. |
| Local AS number | Local AS number. |
| AS | AS number of the BGP peer. |
| Peers in established state | Number of BGP peers in Established state. |
| V | BGP version used on the peer. |
| MsgRcvd | Statistics about messages received from peers. The received messages are defined in BGP, such as Update and Open messages. |
| MsgSent | Statistics about messages sent to the peer. The sent messages are defined in BGP, such as Update and Open messages. |
| OutQ | Number of route prefixes to be sent to the peer after being grouped. The statistics include update and withdraw statistics. |
| Up/Down | Duration of the BGP session staying in the current state. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | Current BGP status:   * Idle: BGP denies any connection request. This is the initial state of BGP.   After receiving a Start event, BGP initiates a TCP connection to the peer, starts the ConnectRetry Timer, listens to TCP messages from the peer, and changes its state to Connect.   * Connect: BGP waits for the TCP connection to be established before performing subsequent operations.  1. If the TCP connection is successfully established, BGP stops the ConnectRetry Timer, sends an Open message to the peer, and changes its state to Opensent. 2. If the TCP connection fails to be established, BGP restarts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the peer, and changes its state to Active. 3. If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and attempts to establish a TCP connection with the peer again. At this time, BGP remains in the Connect state.  * Active: BGP attempts to establish a TCP connection. This is the intermediate state of BGP.  1. If the TCP connection is successfully established, BGP resets the ConnectRetry timer and sends an Open message to the peer. BGP then enters the Opensent state. 2. If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and enters the Connect state. 3. If BGP attempts to establish a TCP session with an unknown IP address, the TCP connection fails, the ConnectRetry Timer is reset, and BGP remains in the Active state.  * OpenSent: BGP has sent an Open message to the peer and is waiting for an Open message from the peer.  1. If BGP receives a correct Open message, BGP enters the OpenConfirm state. 2. If BGP receives an incorrect Open message, BGP sends a Notification message to the peer and enters the Idle state. 3. If BGP receives a TCP connection teardown message, BGP restarts the ConnectRetry Timer with the initial value, listens to a TCP connection initiated by the peer, and changes its state to Active.  * OpenConfirm: BGP is waiting for a Notification or Keepalive message.  1. If BGP receives a Notification message or a TCP connection teardown message, BGP enters the Idle state. 2. If BGP receives a Keepalive message, BGP enters the Established state.  * Established: BGP peers can exchange Update, Notification, and Keepalive messages.  1. If BGP receives an Update or Keepalive message, BGP remains in the Established state. 2. If BGP receives a Notification message, BGP enters the Idle state.  * No neg: The address family is not enabled on the peer BGP peer. In this state, Update messages can be exchanged in other successfully negotiated address families. If the address family is enabled on the peer BGP peer, the local BGP peer receives a Notification message. The peer relationship is disconnected and enters the Idle state. The peer relationship is re-established. |
| PrefRcv | Number of route prefixes received by the local peer from the remote peer. |