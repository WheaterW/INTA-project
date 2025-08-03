if-match ipv6 route-source acl
==============================

if-match ipv6 route-source acl

Function
--------



The **if-match ipv6 route-source acl** command configures a filtering rule that is based on IPv6 addresses of the source devices from which routes are received.

The **undo if-match ipv6 route-source acl** command cancels the configuration.



By default, no filtering rule based on IPv6 addresses of the source devices from which routes are received is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match ipv6 route-source acl** { *acl-number* | *acl-name* }

**undo if-match ipv6 route-source acl** { *acl-number* | *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **acl** | Specifies the ACL for route filtering. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When you run the **if-match ipv6 route-source acl** command to match the address of the source from which IPv6 routes are received, an ACL must also be configured for the matching rule to take effect. For example:

* If if-match ipv6 route-source acl 2000 is configured but acl ipv6 name 2000 is not configured, all routes are permitted.
* If if-match ipv6 route-source acl 2000 and acl ipv6 name 2000 are configured, and the ACL rule is rule 1 permit source 2001:db8:1::1 128, the routes with the next hop address 2001:db8:1::1 are permitted.

The IPv6 address of the source device from which a route is received is the peer address.

**Prerequisites**

A route-policy has been configured using the route-policy command.An ACL has been configured using the **acl** command.

**Configuration Impact**

When you filter routes based on the source addresses of IPv6 routes, the routes that match the filtering rule are permitted and the route that do not match the filtering rule are denied.

**Precautions**

If the next hop address or source address of a route to be filtered is 0::0, by default, the system matches the route and considers its mask length as 0.If the next hop address or source address of a route to be filtered is not 0::0, by default, the system matches the route and considers its mask length as 128.For a named ACL, when the **rule** command is used to configure a filtering rule, only the source address range specified in source and the time period specified in time-range take effect on the filtering rule.


Example
-------

# Define a rule to match the routes with the IPv6 routing information in ACL 2000.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2000
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match ipv6 route-source acl 2000

```