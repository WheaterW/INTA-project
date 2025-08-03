ipv6 route-static default-preference
====================================

ipv6 route-static default-preference

Function
--------



The **ipv6 route-static default-preference** command sets the default priority for IPv6 static routes.

The **undo ipv6 route-static default-preference** command restores the default priority of IPv6 static routes.



By default, the default priority of static routes is 60.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 route-static default-preference** *preference*

**undo ipv6 route-static default-preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *preference* | Specifies the default priority for IPv6 static routes. | The value is an integer ranging from 1 to 255. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can change the status of a route by changing its priority. To change the default priority of new IPv6 static routes, run the **ipv6 route-static default-preference** command.

**Configuration Impact**

After the **ipv6 route-static default-preference** command is used, the new priority takes effect on new IPv6 static routes that use the default priority.


Example
-------

# Set the default priority of IPv6 static routes to 70.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route-static default-preference 70

```