display bgp ipv6 group
======================

display bgp ipv6 group

Function
--------



The **display bgp unnumbered ipv6 group** command displays information about BGP unnumbered IPv6 peer groups.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 group**

**display bgp ipv6 group** *group-name*

**display bgp ipv6 unnumbered group**

**display bgp ipv6 unnumbered group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Displays information about IPv6 peer groups. | - |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Using the **display bgp ipv6 unnumbered group** command, you can view information about BGP unnumbered IPv6 peer groups, including the members of the peer groups and the configurations of the peer groups. This command is used in the following scenarios:

* After running the **group unnumbered** command to configure a peer group, check whether the configuration is successful.
* After running the **peer unnumbered-interface** command to add a peer to a peer group, check whether the configuration is successful.
* Run the **undo peer unnumbered-interface** command to delete a peer and check whether the peer is successfully deleted.
* After modifying the configuration of the peer group, check whether the modification is successful.

**Precautions**

BGP has multiple address families, each of which is configured independently. Information about peer groups in address families can be displayed by specifying different parameters.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all BGP IPv6 peer groups.
```
<HUAWEI> display bgp ipv6 group
BGP peer-group is in
 Remote AS 100
 Type               : internal
 PeerSession Members:
   2001:DB8:2::1
 
 Peer Members:
   2001:DB8:1::1               2001:DB8:2::1
 ***********************
 
 BGP peer-group is ex
 Remote AS number not specified
 Type               : external
 PeerSession Members:
   2001:DB8:20::1
 Peer Members:
   2001:DB8:10::1              2001:DB8:20::1

```

# Display information about all BGP IPv6 unnumbered peer groups.
```
<HUAWEI> display bgp ipv6 unnumbered group
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

**Table 1** Description of the **display bgp ipv6 group** command output
| Item | Description |
| --- | --- |
| BGP peer-group | BGP peer group name. |
| Remote AS | Number of the AS where a peer group resides. |
| Remote AS number not specified | This item is displayed when the peer group is a mixed EBGP peer group. |
| Type | Type of a peer group:   * internal: IBGP peer group. * external: EBGP peer group. |
| PeerSession Members | Peers with which sessions have been established. |
| PeerSession Members(Interface) | Members and outbound interfaces that set up session connections with each other. |
| Peer Members | The following information is about peers. |
| Peer Members(Interface) | The following information is about peers and outbound interfaces. |
| Authentication type configured | BGP authentication type: The options are as follows:   * MD5. * None: No BGP authentication is configured. |