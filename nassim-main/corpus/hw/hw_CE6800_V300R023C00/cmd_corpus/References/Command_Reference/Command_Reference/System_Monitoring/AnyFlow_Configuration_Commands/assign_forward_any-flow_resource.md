assign forward any-flow resource
================================

assign forward any-flow resource

Function
--------



The **assign forward any-flow resource** command sets the hardware flow table resource allocation mode.

The **undo assign forward any-flow resource** command deletes the hardware flow table resource allocation mode.



By default, the hardware flow table resource allocation mode is standard, that is, half of the hardware flow table resources are allocated to IPv4 traffic and the other half are allocated to IPv6 traffic.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**assign forward any-flow resource** { **large-ipv4** | **large-ipv6** | **standard** }

**undo assign forward any-flow resource** { **large-ipv4** | **large-ipv6** | **standard** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **large-ipv4** | Allocates all hardware flow table resources to IPv4 traffic. | - |
| **large-ipv6** | Allocates all hardware flow table resources to IPv6 traffic. | - |
| **standard** | Evenly allocates hardware flow table resources. That is, half resources are allocated to IPv4 and the other half are allocated to IPv6 traffic. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the AnyFlow function is enabled, the device collects traffic and generates flow entries in the hardware flow table. By default, IPv4 and IPv6 traffic each occupies half of the hardware storage space. If only IPv4 or IPv6 traffic is transmitted on the live network, you can run the assign forward any-flow resource command to adjust the allocation of hardware flow table resources.

**Precautions**

If the assign-forward-anyflow-resource command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Configure the device to allocate all hardware flow table resources to IPv4 traffic.
```
<HUAWEI> system-view
[~HUAWEI] assign forward any-flow resource large-ipv4

```