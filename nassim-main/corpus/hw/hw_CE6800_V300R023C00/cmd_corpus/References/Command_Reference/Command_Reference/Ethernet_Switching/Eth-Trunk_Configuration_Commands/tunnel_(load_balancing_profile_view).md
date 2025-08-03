tunnel (load balancing profile view)
====================================

tunnel (load balancing profile view)

Function
--------



The **tunnel** command configures a load balancing mode for tunnel packets in a load balancing profile.

The **undo tunnel** command restores the default load balancing mode of tunnel packets in a load balancing profile.



By default, tunnel packets are load balanced based on outer-header.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**tunnel** { **outer-header** | **inner-header** }

**undo tunnel** [ **outer-header** | **inner-header** ]

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**tunnel** { **outer-header** | **inner-header** } \*

**undo tunnel** [ **outer-header** | **inner-header** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **outer-header** | Specifies load balancing based on the outer header. | - |
| **inner-header** | Specifies load balancing based on the inner header. | - |



Views
-----

Load balancing profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

For tunnel packets, such as GRE and VXLAN packets, you can run the tunnel command to configure hash calculation based on the outer or inner header in the specified load balancing profile.

**Precautions**



For tunnel packets, route selection involving inner packet factors takes effect only in known unicast scenarios.




Example
-------

# Configure load balancing for tunnel packets based on inner-header in a load balancing profile.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile abc
Warning: The profile default has been used, and this command will rename it. Continue? [Y/N]:y
[*HUAWEI-load-balance-profile-abc] tunnel inner-header

```