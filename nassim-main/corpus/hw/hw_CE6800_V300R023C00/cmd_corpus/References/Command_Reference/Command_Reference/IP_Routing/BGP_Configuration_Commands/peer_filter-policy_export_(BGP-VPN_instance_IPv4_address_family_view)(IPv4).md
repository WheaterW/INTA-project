peer filter-policy export (BGP-VPN instance IPv4 address family view)(IPv4)
===========================================================================

peer filter-policy export (BGP-VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer filter-policy export** command configures an ACL-based policy for filtering BGP routes to be advertised to a specified peer.

The **undo peer filter-policy export** command cancels this configuration.



By default, no filtering policy is configured for the routes to be advertised to peers.


Format
------

**peer** *ipv4-address* **filter-policy** *acl-number* **export**

**peer** *ipv4-address* **filter-policy** **acl-name** *acl-name* **export**

**undo peer** *ipv4-address* **filter-policy** *acl-number* **export**

**undo peer** *ipv4-address* **filter-policy** **acl-name** *acl-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in the dotted decimal format. |
| *acl-number* | Specifies the number of the basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **export** | Filters advertised routes. | - |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces and must start with a letter. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you do not want all routes to be advertised to a peer, you can run the **peer filter-policy export** command to configure an ACL-based filtering policy to filter the routes to be advertised to the peer.

**Precautions**

For a named ACL, when the **rule** command is used to configure a filtering rule, only the configurations specified by source and time-range take effect.Select a correct basic ACL based on the address family type of the peer.For a peer, only one route filtering policy can take effect. If the **peer filter-policy** command is run more than once, the latest configuration takes effect.


Example
-------

# Set the filtering policy for peers.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] acl 2001
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpna] peer 10.1.1.1 filter-policy 2001 export

```