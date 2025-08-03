peer filter-policy export (BGP-IPv6 unicast address family view)(IPv4)
======================================================================

peer filter-policy export (BGP-IPv6 unicast address family view)(IPv4)

Function
--------



The **peer filter-policy export** command configures an ACL-based policy for filtering BGP routes to be advertised to a specified peer.

The **undo peer filter-policy export** command cancels this configuration.



By default, no filtering policy is configured for the routes to be advertised to peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **filter-policy** *acl-number* **export**

**peer** *ipv4-address* **filter-policy** **acl6-name** *acl6-name* **export**

**undo peer** *ipv4-address* **filter-policy** *acl-number* **export**

**undo peer** *ipv4-address* **filter-policy** **acl6-name** *acl6-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in the dotted decimal format. |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **export** | Filters advertised routes. | - |
| **acl6-name** *acl6-name* | Specifies the name of a named basic ACL6. | The value is a string of 1 to 64 case-sensitive characters starting with a letter. It cannot contain spaces. |



Views
-----

BGP-IPv6 unicast address family view


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
[~HUAWEI] acl ipv6 2001
[*HUAWEI-acl6-basic-2001] rule permit
[*HUAWEI-acl6-basic-2001] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-ipv6] peer 10.1.1.1 filter-policy 2001 export

```