ipv6 nd direct-route enable
===========================

ipv6 nd direct-route enable

Function
--------



The **ipv6 nd direct-route enable** command configures IPv6 NDP Vlink direct route advertisement.

The **undo ipv6 nd direct-route enable** command disables IPv6 NDP Vlink direct route advertisement.



By default, IPv6 NDP Vlink direct routes are not advertised.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd direct-route enable**

**undo ipv6 nd direct-route enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device connects to two IPv6 sites (Site 1 and Site 2). The device and its peer run a dynamic routing protocol. To allow its peer to learn routes destined for Site 1 and Site 2, run the **ipv6 nd direct-route enable** command on the device to configure interfaces to advertise IPv6 NDP Vlink direct routes, and then configure a dynamic routing protocol to import the direct routes.

**Configuration Impact**

If this command is run in the system view, all IPv6-capable interfaces that support Vlink route advertisement are enabled to advertise IPv6 NDP Vlink direct routes.

**Follow-up Procedure**

After configuring IPv6 NDP Vlink direct route advertisement, import the IPv6 NDP Vlink direct routes to a dynamic routing protocol so that they can be advertised.


Example
-------

# Configure IPv6 NDP Vlink direct route advertisement.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd direct-route enable

```