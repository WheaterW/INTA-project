display bgp graceful-restart status
===================================

display bgp graceful-restart status

Function
--------



The **display bgp graceful-restart status** command displays GR information on a BGP speaker.

The **display bgp local-graceful-restart status** command displays information about local GR on a BGP speaker.




Format
------

**display bgp** [ **instance** *instance-name* ] **graceful-restart** **status**

**display bgp** [ **instance** *instance-name* ] **local-graceful-restart** **status**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check GR information on a BGP speaker, including whether GR is enabled and time parameters, run the **display bgp graceful-restart status** command.To check information about local GR on a BGP speaker, including whether GR is enabled and time parameters, run the **display bgp local-graceful-restart status** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display GR information on a BGP speaker.
```
<HUAWEI> display bgp graceful-restart status
  BGP protocol GR information: GR is configured
  GR timer configuration: 
    Restarter           : 150
    Wait-for-EOR        : 600
    Selection-deferral  : 600
    Wait-all-peer-up    : 120
    Protection          : 300
    Force-quit          : 3600
-------------------------------------------------------
IPv4-UNC (_public_)
Restarter Status                     : Init
Number of helpers                    : 1
Number of peers in established state : 1
Number of EORs expected from peer    : 0
 Peer information :(* - Dynamic Peer, R - Restarter, H - Helper, r - received, s - sent)
 Peer                               State   Role EOR  Running Timer(lefts)
 10.1.1.2                          UP      -    -    None

```

# Display information about local GR on a BGP speaker.
```
<HUAWEI> display bgp local-graceful-restart status
-------------------------------------------------------
IPv4-UNC (_public_)
Peers:
   10.1.1.1
     Peer state: Active
     GR state: false
-------------------------------------------------------
IPv4-UNC (_public_)
Peers:
   10.1.1.1
     Peer state: Established
     GR state: false

```

**Table 1** Description of the **display bgp graceful-restart status** command output
| Item | Description |
| --- | --- |
| BGP protocol GR information | * "GR is configured" indicates that the GR capability of the BGP speaker is enabled. * "GR is NOT configured" indicates that the GR capability of the BGP speaker is not enabled. |
| GR timer configuration | Value of the timer. |
| GR state | Status of the peer:   * true: The peer is in the GR state. * false: The peer is not in the GR state. |
| Restarter | Time for waiting for a peer relationship to be reestablished, in seconds. |
| Restarter Status | Current status of the Restarter.   * Init: indicates that the device does not enter GR. * Connecting: indicates that the device enters the GR state and waits for the peer to establish a connection. * Receiving: indicates that the route and EOR flag are received. * Querying: queries the status of the next hop. * Selecting indicates the routing status. * Distributing: released. * Normal: indicates that the device exits the GR state. |
| Wait-for-EOR | Period during which a BGP speaker waits for the End-Of-RIB flag, in seconds. |
| Selection-deferral | Time for waiting for route selection delay, in seconds. |
| Wait-all-peer-up | Time for waiting for all peers to be re-established, in seconds. |
| Protection | Time taken to prevent all peers from being re-established, in seconds. |
| Force-quit | Time for forcibly exiting from GR, in seconds. |
| IPv4-UNC (\_public\_) | Public unicast address family. |
| Number of helpers | Number of helpers. |
| Number of peers in established state | Number of peers that have established connections. |
| Number of EORs expected from peer | Number of peers that wait to receive EOR messages. |
| Peer information | Peer information. |
| Peer state | Peer status:   * Idle: indicates that BGP denies any connection request. This is the initial status of BGP. * Active: BGP tries to set up a TCP connection. This is the intermediate status of BGP. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * Connect: BGP is waiting for the TCP connection to be established before performing further actions. * OpenSent: BGP is waiting for an Open message from the peer. * OpenConfirm: BGP is waiting for a Notification message and a Keepalive message. |
| State | Status of the peers.   * DOWN. * DOWN-GR. * UP. |
| Role | Peer role.   * R Restarter. * H Helper. |
| EOR | EOR receiving and sending status:   * r: received. * s: sent. |
| Running Timer(lefts) | Remaining running time of the timer. |
| Peers | Peers. |