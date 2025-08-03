display bgp vpn-instance group
==============================

display bgp vpn-instance group

Function
--------



The **display bgp vpn-instance group** command displays information about BGP peer groups in a specified VPN instance.




Format
------

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **group**

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **group** *group-name*

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **group**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpnv4** | Displays information about BGP VPNv4 peer groups. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about BGP peer groups in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Configuring BGP peer groups simplifies BGP network configuration and improves route advertisement efficiency.The**display bgp vpn-instance group** command displays information about BGP peer groups in a specified VPN instance, including peers in the peer group and configuration information about the peer group. The**display bgp vpn-instance group** command is used in the following scenarios:

* Verify the configuration after a peer group is configured using the **group** command.
* Verify the configuration after a peer is added to a peer group using the **peer group** command.
* Verify the configuration after a peer is deleted from a peer group using the **undo peer group** command.
* Verify the configuration after modifying the configuration of a peer group.

**Precautions**



BGP has multiple address families, each of which is configured independently. Information about peer groups in address families can be displayed by specifying different parameters.If no parameter is specified, the **display bgp vpn-instance group** command displays default information about peer groups in the IPv4 unicast address family.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about a BGP peer group in a specified VPN instance.
```
<HUAWEI> display bgp instance aaa vpnv4 vpn-instance vpn3 group

 BGP peer-group: ccc
 Remote AS number isn't specified
 VPN-Instance(IPv4-family): vpn3
 
 Authentication type configured: None
 Type : external
 PeerSession Members: 
 10.1.1.2                                 

 Peer Members: 
 10.1.1.2

```

**Table 1** Description of the **display bgp vpn-instance group** command output
| Item | Description |
| --- | --- |
| BGP peer-group | BGP peer group name. |
| Remote AS | Number of the AS where a peer group resides. |
| AS | Number of the AS where a member of a peer group resides. |
| Authentication type configured | BGP authentication type:   * MD5. * None: indicates that no BGP authentication is configured. |
| Type | Type of a peer group:   * internal: IBGP peer group. * external: EBGP peer group. |
| PeerSession Members | Peers with which sessions have been established. |
| Peer Members | The following information is about peers. |
| Peer | IP addresses of the peer. |
| V | BGP version. |