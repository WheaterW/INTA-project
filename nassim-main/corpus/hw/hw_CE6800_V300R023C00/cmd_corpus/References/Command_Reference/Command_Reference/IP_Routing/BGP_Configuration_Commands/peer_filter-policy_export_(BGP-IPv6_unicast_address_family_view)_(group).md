peer filter-policy export (BGP-IPv6 unicast address family view) (group)
========================================================================

peer filter-policy export (BGP-IPv6 unicast address family view) (group)

Function
--------



The **peer filter-policy export** command configures an ACL-based policy for filtering BGP routes to be advertised to a specified peer group.

The **undo peer filter-policy export** command cancels this configuration.



By default, no filtering policy is configured for the routes to be advertised to a peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **filter-policy** *acl-number* **export**

**peer** *group-name* **filter-policy** **acl6-name** *acl6-name* **export**

**undo peer** *group-name* **filter-policy** *acl-number* **export**

**undo peer** *group-name* **filter-policy** **acl6-name** *acl6-name* **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *acl-number* | Specifies the number of the basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **export** | Filters advertised routes. | - |
| **acl6-name** *acl6-name* | Specifies the name of a basic named ACL6. | The value is a string of 1 to 64 case-sensitive characters starting with a letter. It cannot contain spaces. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you do not want all routes to be advertised to a peer group, you can run the **peer filter-policy export** command to configure an ACL-based filtering policy to filter the routes to be advertised to the peer group.

**Precautions**

For a named ACL, when the **rule** command is used to configure a filtering rule, only the configurations specified by source and time-range take effect.Select a correct basic ACL based on the address family type of the peer group.For a peer group, only one route filtering policy can take effect. If the **peer filter-policy** command is run more than once, the latest configuration takes effect.


Example
-------

# Set the filtering policy for peer group.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2001
[*HUAWEI-acl6-basic-2001] rule permit
[*HUAWEI-acl6-basic-2001] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[~HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test filter-policy 2001 export

```