display bgp vpn-instance peer
=============================

display bgp vpn-instance peer

Function
--------



The **display bgp vpn-instance peer** command displays information about BGP peers in a specified VPN instance.

The **display bgp vpn-instance slow-peer** command displays information about slow BGP peers in a specified VPN instance.




Format
------

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **peer**

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **slow-peer**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **peer**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **slow-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpnv4** | Specifies a BGP-VPNv4 address family. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *instance-name* | Specifies a BGP multi-instance address family. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpn-instance peer** command displays information about BGP peers in a specified VPN instance. You can implement the following operations based on the command output:

* To check the status of BGP connections
* To check information about a BGP peer
* To check whether a BGP peer is configured using the **peer as-number** command
* To check whether a BGP peer is deleted using the **undo peer as-number** commandThe **display bgp vpn-instance peer** command can be used for troubleshooting, with details as follows: If BGP peers are disconnected, specify log-info in the command to check the log information of the specified peer. In the command output, Date/Time indicates the time when the peers were disconnected, and Error Code and Error Subcode indicate the cause of the disconnection.To check information about slow BGP peers, run the **display bgp vpn-instance slow-peer** command. The information includes the time when a peer began to be identified as a slow peer, the time when a peer last exited from the slow peer state, the number of times a peer has been identified as a slow peer, and the remaining time for a peer to exit from the slow peer state.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the BGP peer of the VPN instance vrf1.
```
<HUAWEI> display bgp vpnv4 vpn-instance vrf1 peer
Status codes: * - Dynamic
 BGP local router ID : 10.1.1.1
 Local AS number : 100
 Total number of peers : 1                 
 Peers in established state : 1
 Total number of dynamic peers : 1
Peer        V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv

  10.1.1.1    4 65410      207      192     0 02:59:49 Established       1

```

**Table 1** Description of the **display bgp vpn-instance peer** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the local BGP device. |
| Local AS number | Local AS number. |
| AS | AS number. |
| Total number of peers | Number of BGP peers. |
| Total number of dynamic peers | Number of dynamic BGP peers. |
| Peers in established state | Number of BGP peers in the Established state. |
| Peer | Peer IP address. |
| V | BGP version used on the peer. |
| MsgRcvd | Number of received messages. |
| MsgSent | Number of sent messages. |
| OutQ | Message to be sent to the specified peer. |
| Up/Down | Duration in which the BGP session remains in the current state:   * If the duration is less than 24 hours, it is displayed in the format of xx:xx:xx, indicating xx hours, xx minutes, and xx seconds. * If the duration is greater than 24 hours, it is displayed in the format of xxxxhxxm, indicating xxxx hours and xx minutes. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | Peer relationship status:   * Idle: BGP denies any connection request, which is BGP's initial state. * Active: BGP attempts to set up a TCP connection, which is BGP's intermediate state. * Established: BGP peers can exchange Update, Notification, and Keepalive messages. * Connect: BGP is waiting for the complete setup of the TCP connection before performing subsequent operations. * OpenSent: BGP is waiting for an Open message from the peer. * OpenConfirm: BGP is waiting for a Notification message or a Keepalive message. |
| PrefRcv | Number of route prefixes sent from the peer. |