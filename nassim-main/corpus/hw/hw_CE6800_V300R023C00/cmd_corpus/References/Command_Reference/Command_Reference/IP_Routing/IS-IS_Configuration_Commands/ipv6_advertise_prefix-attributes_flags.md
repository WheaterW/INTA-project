ipv6 advertise prefix-attributes flags
======================================

ipv6 advertise prefix-attributes flags

Function
--------



The **ipv6 advertise prefix-attributes flags** command enables an IPv6 IS-IS process to advertise the extended prefix attribute flag.

The **undo ipv6 advertise prefix-attributes flags** command disables an IPv6 IS-IS process from advertising the extended prefix attribute flag.



By default, an IPv6 IS-IS process does not advertise the extended prefix attribute flag.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 advertise prefix-attributes flags**

**undo ipv6 advertise prefix-attributes flags**


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To view information about the origin of routes in the LSDB, run this command. After the command is run, the IPv6 IS-IS process advertises the extended prefix attribute flag (IPv6 Extended Reachability Attribute Flags) to carry related information in the LSDB.

**Prerequisites**

IPv6 has been enabled for the IS-IS process using the **ipv6 enable** command in the IS-IS view.


Example
-------

# Enable an IPv6 IS-IS process to advertise the extended prefix attribute flag.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 advertise prefix-attributes flags

```