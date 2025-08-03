display bgp group
=================

display bgp group

Function
--------



The **display bgp group** command displays information about BGP peer groups, excluding the BGP unnumbered peer groups.

The **display bgp unnumbered group** command displays information about BGP unnumbered peer groups.




Format
------

**display bgp group**

**display bgp vpnv4 all group** [ *group-name* ]

**display bgp group** *group-name*

**display bgp instance** *instance-name* **vpnv4** **all** **group** [ *group-name* ]

**display bgp unnumbered group**

**display bgp unnumbered group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpnv4** | Displays information about BGP VPNv4 peer groups. | - |
| **all** | Displays information about all BGP VPNv4 peer groups. | - |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *instance-name* | Specifies a BGP instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Configuring BGP peer groups simplifies BGP network configuration and improves BGP route advertisement efficiency.The **display bgp group** command displays information about peer groups, including the members in the peer groups and the configuration of the peer groups. This command is used in the following scenarios:

* The **group** command is run to configure a peer group, and you want to check whether the configuration is successful.
* The **peer group** command is run to add a peer to a peer group, and you want to check whether the configuration is successful.
* The **undo peer group** command is run to delete a peer from a peer group, and you want to check whether the peer group is successfully deleted.
* After modifying the configuration of the peer group, check whether the modification is successful.

The **display bgp unnumbered group** command displays information about a BGP unnumbered peer group, including members in the peer group and configurations of the peer group. This command is used in the following scenarios:

* The **group unnumbered** command is run to configure a peer group and you want to check whether the configuration is successful.
* The **peer unnumbered-interface** command is run to add a peer to a peer group and you want to check whether the configuration is successful.
* The **undo peer unnumbered-interface** command is run to delete the peer and you want to check whether the peer is successfully deleted.
* After modifying the configuration of the peer group, check whether the modification is successful.

**Precautions**

BGP has multiple address families, each of which is configured independently. Information about peer groups in address families can be displayed by specifying different parameters.If no parameter is specified, the **display bgp group** command displays default information about peer groups in the IPv4 unicast address family.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the BGP unnumbered peer group.
```
<HUAWEI> display bgp unnumbered group
 BGP peer-group                       : i
 Remote AS                            : 100
 Authentication type configured       : None
 Type                                 : unnumbered internal
 PeerSession Members(Interface)       :
 FE80::3A76:9CFF:FE21:300(100GE1/0/1.1)
 FE80::3A76:9CFF:FE21:301(100GE1/0/1.2)

 Peer Members(Interface):
 FE80::3A76:9CFF:FE21:300(100GE1/0/1.1)
 FE80::3A76:9CFF:FE21:301(100GE1/0/1.2)

```

# Display information about the BGP VPNv4 peer group named rr1.
```
<HUAWEI> display bgp vpnv4 all group rr1
Group in VPNV4:
 No such a peer-group 

Group in VPN-Instance:

 BGP peer-group             : rr1
 Remote AS number isn't specified
 VPN-Instance               : 1

 Type                       : external 
 Configured hold timer value: 180
 Keepalive timer value      : 60
 Minimum route advertisement interval is 30 seconds
 PeerSession Members        :
  NONE 

 Peer Preferred Value       : 0
 No routing policy is configured
 Peer Members:
  No Peer Exists

```

# Display information about the dynamic EBGP peer group named dyn-peer.
```
<HUAWEI> display bgp group dyn-peer

 BGP peer-group                : dyn-peer
 Remote AS                     : Dynamic
 Authentication type configured: None
 Type                          : listen external
 Configured hold timer value   : 180
 Keepalive timer value         : 60
 Connect-retry timer value     : 32
 Minimum route advertisement interval is 30 seconds
 PeerSession Members:
  NONE
  
 Peer Preferred Value          : 0
 No routing policy is configured
 Peer Members:
 Info: No peer exists.

```

# Display information about all BGP VPNv4 peer groups.
```
<HUAWEI> display bgp vpnv4 all group
Group in VPNV4:
 
 BGP peer-group           : aa
 Remote AS number isn't specified
 Type : external
 PeerSession Members      :
   10.3.3.3
 
 Peer Members:
   10.3.3.3
 ***********************

 BGP peer-group           : bb
 Remote AS 100
 Type                     : internal
 PeerSession Members      :
  NONE

 Peer Members:
   10.4.4.4
 
Group in VPN-Instance:
 
 BGP peer-group           : cc
 Remote AS number isn't specified
 VPN-Instance(IPv4-family): vpn1
 
 Type                     : external
 PeerSession Members:
   10.2.2.1

 Peer Members:
   10.2.2.1

```

# Display information about the peer group named my-peer.
```
<HUAWEI> display bgp group my-peer
BGP peer-group                : my-peer
 Remote AS                     : 200
 Authentication type configured: None
 Group's BFD has been enabled
 Type                          : internal
 Maximum allowed route limit   : 150000
 Threshold                     : 75%
 Configured hold timer value   : 180
 Keepalive timer value         : 60
 Minimum route advertisement interval is 15 seconds
 listen-only has been configured
 TCP-MSS configured value      : 200
 PeerSession Members:
   10.2.2.2
 Send best-external has been configured
 Peer Preferred Value          : 0
 No routing policy is configured
 Peer Members:
  Peer             V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
  10.2.2.2          4   200        0        0     0 00:00:47      Active       0

```

**Table 1** Description of the **display bgp group** command output
| Item | Description |
| --- | --- |
| BGP peer-group | Name of a BGP peer group. |
| Remote AS | Number of the AS where the peer group resides.   * Dynamic: The peer group is a dynamic EBGP peer group configured with an AS number. * Specific value: This field is displayed when the peer group is an IBGP peer group or a static EBGP peer group configured with an AS number. |
| Remote AS number isn't specified | This information is displayed when the peer group is an EBGP peer group with no AS number configured. |
| AS | Number of the AS where a peer group member resides. |
| Authentication type configured | BGP authentication type: The options are as follows:   * MD5. * None: No BGP authentication is configured. |
| Type | Types of the peer group:   * internal: The type of the peer group is IBGP. * external: indicates that the type of the peer group is EBGP. * listen internal: indicates that the peer group is a dynamic IBGP peer group. * listen external: indicates that the peer group is a dynamic EBGP peer group. * listen confederation-external: indicates that the peer group is a dynamic confederation EBGP peer group. |
| PeerSession Members | A member that has established a session connection with a peer. |
| PeerSession Members(Interface) | Members and their outbound interfaces that set up a session connection with each other. |
| Peer Preferred Value | Preferred value of the BGP peer. |
| Peer Members | The following information is about peers. |
| Peer | Peer IP address. |
| Peer Members(Interface) | The following information is about peers and outbound interfaces. |
| Group in VPNV4 | All BGP peer groups in the VPNv4 address family view. |
| Group in VPN-Instance | Peer groups in a VPN instance. |
| Configured hold timer value | Hold time. |
| Keepalive timer value | Value of the Keepalive time. |
| Minimum route advertisement interval | Minimum interval at which routes are advertised: |
| VPN-Instance | VPN instance name. |
| Maximum allowed route limit | Maximum number of allowed BGP routes. |
| listen-only has been configured | The device listens to connection requests but does not initiate connection requests. |
| TCP-MSS configured value | TCP MSS value used for setting up the TCP connection with the peer group. |
| Send best-external has been configured | The local device has been enabled to advertise Best External routes to a specified peer group. |
| V | BGP version number. |
| MsgRcvd | BGP version of a peer. |
| MsgSent | Number of messages sent. |
| OutQ | Number of messages to be sent to neighbors. |
| Up/Down | Duration of the BGP session staying in the current state.   * If the duration is less than 24 hours, it is displayed in the format of xx:xx:xx, indicating xx hours, xx minutes, and xx seconds. * If the duration is greater than 24 hours, it is displayed in the format of xxxxhxxm, indicating xxxx hours and xx minutes. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | BGP state:   * Idle: BGP denies any connection request. This is the initial status of BGP. * Active: BGP attempts to establish a TCP connection. This is the intermediate state of BGP. * Established: BGP peers can exchange Update, Notification, and Keepalive messages. * Connect: BGP is waiting for the TCP connection to be established before performing subsequent operations. * OpenSent: BGP is waiting for an Open message from the peer. * OpenConfirm: BGP waits for a Notification or Keepalive message. |
| PrefRcv | Number of route prefixes sent from the peer. |
| Threshold | Alarm threshold, that is, the percentage of the number of BGP routes to the maximum number of routes that can be received. |
| Info | Peer information. |