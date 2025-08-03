display bgp mvpn all group
==========================

display bgp mvpn all group

Function
--------



The **display bgp mvpn all group** command views information about BGP MVPN peer groups.




Format
------

**display bgp mvpn all group** [ *group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Configuring BGP peer groups simplifies BGP network configuration and improves route advertisement efficiency.The **display bgp mvpn all group** command displays mvpn peer group information, including peers in the peer group and configuration information about the peer group. The display bgp **group** command is used in the following scenarios:

* Verify the configuration after a peer group is configured using the **group** command.
* Verify the configuration after a peer is added to a peer group using the **peer group** command.
* Verify the configuration after a peer is deleted from a peer group using the **undo peer group** command.
* Verify the configuration after modifying the configuration of a peer group.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all BGP MVPN peer groups.
```
<HUAWEI> display bgp mvpn all group
Group in MVPN:
 BGP peer-group: a
 Remote AS: 100
 Authentication type configured: None
 Type : internal
 PeerSession Members: 
 2.2.2.2                                  

 Peer Members: 
 2.2.2.2

```

**Table 1** Description of the **display bgp mvpn all group** command output
| Item | Description |
| --- | --- |
| Group in MVPN | All BGP MVPN peer groups. |
| BGP peer-group | Name of an MVPN BGP peer group. |
| Remote AS | Number of the AS where a peer group resides. |
| Authentication type configured | BGP authentication type:   * MD5. * None: indicates that no BGP authentication is configured. |
| Type | Type of a peer group:   * internal: indicates that the peer group is an IBGP peer group. * external: indicates that the peer group is an EBGP peer group. * listen internal: indicates that the peer group is a dynamic IBGP peer group. * listen external: indicates that the peer group is a dynamic EBGP peer group. * listen confederation-external: indicates that the peer group is a dynamic confederation EBGP peer group. |
| PeerSession Members | Peers with which sessions have been established. |
| Peer Members | The following information is about peers. |