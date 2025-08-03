display bgp peer (or slow-peer)
===============================

display bgp peer (or slow-peer)

Function
--------



The **display bgp peer** command displays information about BGP peers.

The **display bgp slow-peer** command displays information about slow BGP peers.




Format
------

**display bgp** { **peer** | **slow-peer** }


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

**Usage Scenario**



The **display bgp peer** command displays BGP peer information, excluding unnumbered peers. You can implement the following operations based on the command output:

To check the status of BGP connectionsTo check information about a BGP peerTo check whether a BGP peer is configured using the **peer as-number** commandTo check whether a BGP peer is deleted using the **undo peer as-number** commandTo check information about slow BGP peers, run the **display bgp slow-peer** command. The information includes the time when a peer began to be identified as a slow peer, the time when a peer last exited from the slow peer state, the number of times a peer has been identified as a slow peer, and the remaining time for a peer to exit from the slow peer state.



**Precautions**



When dynamic BGP peer relationships are being established or disconnected, statistics about the BGP peers may be inconsistent with the actual number of BGP peers. Therefore, you are advised to query statistics after the BGP peer status is stable.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP peer information.
```
<HUAWEI> display bgp peer

Status codes: * - Dynamic
 BGP local router ID : 10.2.3.4
 Local AS number : 10
 Total number of peers : 2                 
 Peers in established state : 1
 Total number of dynamic peers : 1

  Peer          V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
  10.1.1.1       4   100        0        0     0 00:00:07        Idle       0
  10.2.2.2       4   200       32       35     0 00:17:49 Established       0

```

**Table 1** Description of the **display bgp peer (or slow-peer)** command output
| Item | Description |
| --- | --- |
| Total number of peers | Total number of BGP peers. |
| Total number of dynamic peers | Number of dynamic BGP peers. |
| Peer | Peer IP address. |
| BGP local router ID | Local router ID of BGP.  If the BGP local router IDs of the two ends conflict, the BGP peer relationship cannot be established. Run the router id command in the BGP view to change the router IDs to different values. Generally, the IP address of the loopback interface is used as the router ID of the local end. |
| Local AS number | Local AS number. |
| AS | AS number. |
| Peers in established state | Number of BGP peers in Established state. |
| V | BGP version used on the peer. |
| MsgRcvd | Number of received messages. |
| MsgSent | Number of messages sent. |
| OutQ | Message to be sent to the specified peer. |
| Up/Down | Duration of the BGP session staying in the current state.   * If the duration is less than 24 hours, it is displayed in the format of xx:xx:xx, indicating xx hours, xx minutes, and xx seconds. * If the duration is greater than 24 hours, it is displayed in the format of xxxxhxxm, indicating xxxx hours and xx minutes. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | Status of the peer:   * Idle: indicates that BGP denies any request of entering. This is the initiatory status of BGP.   Upon receiving a Start event, BGP initiates a TCP connection request to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection request initiated by the remote BGP peer, and changes its state to Connect.   * Connect: indicates that BGP is waiting for the TCP connection to be set up before it determines whether to perform other operations. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value, initiates a TCP connection request to the remote BGP peer, and stays in the Connect state. * Active: indicates that BGP tries to set up a TCP connection. This is the intermediate status of BGP. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value and changes its state to Connect. * If BGP initiates a TCP connection request with an unknown IP address, the TCP connection fails. When this occurs, BGP restarts the ConnectRetry Timer with the initial value and stays in the Active state. * OpenSent: indicates that BGP has sent one Open message to its peer and is waiting for the other Open message from the peer. * If there are no errors in the Open message received, BGP changes its state to OpenConfirm. * If there are errors in the Open message received, BGP sends a Notification message to the remote peer and changes its state to Idle. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * OpenConfirm: indicates that BGP is waiting for a Notification or Keepalive message. * If BGP receives a Notification message, or the TCP connection fails, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP changes its state to Established. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or a Keepalive message, its state stays in Established. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| PrefRcv | Number of route prefixes received by the local peer from the remote peer. |
| Status codes | Status of a peer. |