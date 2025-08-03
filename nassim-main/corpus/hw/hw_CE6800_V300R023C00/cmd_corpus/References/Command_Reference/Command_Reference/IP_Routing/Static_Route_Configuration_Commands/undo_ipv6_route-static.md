undo ipv6 route-static
======================

undo ipv6 route-static

Function
--------



The **undo ipv6 route-static** command deletes the configured static routes.



By default, no IPv6 static routes are configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**undo ipv6 route-static** *dest-ipv6-address* *prefix-length* [ *nexthop-ipv6-address* | { *interface-name* | *interface-type* *interface-number* } [ *nexthop-ipv6-address* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dest-ipv6-address* | Specifies the destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the length of an IPv6 prefix. | It is an integer ranging from 0 to 128. |
| *nexthop-ipv6-address* | Specifies the next-hop IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a simple network or when the device cannot use a dynamic routing protocol to establish a device to a destination, you can configure static routes.To easily view and maintain a static route, specify description to configure a description for the static route. To check the configured description, run the **display this** command in the system view or run the display current-configuration command.




Example
-------

# Delete IPv6 static routes on the public network.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route-static 2001:db8:2::1 128 2001:db8:1::1
[~HUAWEI] undo ipv6 route-static 2001:db8:2::1 128

```