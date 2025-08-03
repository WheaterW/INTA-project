display bgp vpn-target peer
===========================

display bgp vpn-target peer

Function
--------



The **display bgp vpn-target peer** command displays information about BGP peers.

The **display bgp vpn-target slow-peer** command displays information about slow BGP peers.




Format
------

**display bgp vpn-target** { **peer** | **slow-peer** }


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



The **display bgp vpn-target peer** command can be used to locate faults. For example, when a peer is disconnected, you can view the log information of the specified peer to learn the disconnection time and cause (error code and sub-error code).After slow BGP peer detection is enabled, you can run the **display bgp slow-peer** command to view information about slow BGP peers. The information includes the start time of the slow peer, end time of the last slow peer, number of times that a peer is considered as a slow peer, and the remaining time for a peer to exit the slow peer state.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about peers in the BGP VPN-target address family.
```
<HUAWEI> display bgp vpn-target peer
 
 BGP local router ID : 1.1.1.1
 Local AS number : 100
 Total number of peers : 1                 Peers in established state : 1

  Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
  2.2.2.2         4         200       12       14     0 00:01:15 Established        0

```

# Display information about slow BGP peers in the VPN-Target address family.
```
<HUAWEI> display bgp vpn-target slow-peer

 Total number of peers : 1

  Switchback detection timer: Remaining 3579 Second(s)
  Peer                             LastSlowEndTime              SlowStartTime                SlowCount
  10.1.1.1                         -                            2023-05-22 19:25:00+00:00    1

```

**Table 1** Description of the **display bgp vpn-target peer** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the local device. |
| Local AS number | Local AS number. |
| AS | AS number. |
| Total number of peers | Total number of BGP peers. |
| Peers in established state | Number of BGP peers in Established state. |
| Peer | IP address of the BGP peer. |
| V | BGP version used by the BGP peer. |
| MsgRcvd | Number of received messages. |
| MsgSent | Number of sent messages. |
| OutQ | Number of messages to be sent to a specified peer. |
| Up/Down | Duration of the BGP session staying in the current state.   * If the duration is less than 24 hours, it is displayed in the format of xx:xx:xx, indicating xx hours, xx minutes, and xx seconds. * If the duration is greater than 24 hours, it is displayed in the format of xxxxhxxm, indicating xxxx hours and xx minutes. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | Status of the BGP peer:   * Idle: BGP denies any connection request. This is the initial status of BGP. * Active: BGP tries to establish a TCP connection. This is the intermediate status of BGP. * Connect: BGP is waiting for the establishment of the TCP connection to complete before performing further actions. * OpenSent: BGP is waiting for an Open message from the peer. * OpenConfirm: BGP is waiting for a Notification message or a Keepalive message. * Established: BGP peers can exchange Update, Notification, and Keepalive messages. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| PrefRcv | Number of route prefixes received from a peer. |
| Switchback detection timer | Remaining time for a peer to exit the slow peer state. |
| LastSlowEndTime | Time when a peer last exited the slow peer state. |
| SlowStartTime | Time when a peer began to be identified as a slow peer. |
| SlowCount | Number of times a peer has been identified as a slow peer. |