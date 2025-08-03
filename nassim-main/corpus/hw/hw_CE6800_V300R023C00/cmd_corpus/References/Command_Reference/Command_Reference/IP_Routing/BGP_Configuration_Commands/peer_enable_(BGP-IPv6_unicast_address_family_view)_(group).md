peer enable (BGP-IPv6 unicast address family view) (group)
==========================================================

peer enable (BGP-IPv6 unicast address family view) (group)

Function
--------



The **peer enable** command enables a device to exchange routing information with a specified peer group in the address family view.

The **undo peer enable** command disables a device from exchanging routes with a specified peer group.



By default, a device is disabled from exchanging routing information with a specified peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **enable**

**undo peer** *group-name* **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the device is automatically enabled to exchange routing information only with peer groups in the BGP-IPv4 unicast address family. That is, after the **peer as-number** command is run in the BGP view, the system automatically configures the corresponding **peer enable** command. This function must be manually enabled in other address family views.

**Configuration Impact**

Enabling or disabling a BGP peer group in this address family causes the BGP connections of the peer group in other address families to be disconnected and automatically renegotiated.


Example
-------

# Enable the device to exchange relevant routing information with a specified peer group in the address family view.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[~HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer test enable

```