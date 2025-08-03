local-preference enhanced
=========================

local-preference enhanced

Function
--------



The **local-preference enhanced** command enables the function to preferentially forward traffic through a local chip.

The **undo local-preference enhanced** command restores the default configuration.



By default, the function to preferentially forward traffic through a local chip is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K.



Format
------

**local-preference enhanced**

**undo local-preference enhanced**


Parameters
----------

None

Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a device has multiple chips for traffic forwarding, the hash algorithm may select an inter-chip outbound interface, increasing the consumption of inter-chip bandwidth resources.To resolve this issue, run this command so that traffic is preferentially forwarded from a local chip. Specifically, a chip preferentially forwards received traffic through its outbound interface. This effectively saves inter-chip bandwidth resources and improves the forwarding efficiency of traffic.

**Precautions**

1. This command and the **load-balance ecmp stateful enable** command are mutually exclusive.
2. This command and the **vxlan-overlay all local-preference enable** command are mutually exclusive.
3. This command and the **vxlan-overlay network local-preference enable** command are mutually exclusive.

Example
-------

# Enable the function to preferentially forward traffic through a local chip.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] local-preference enhanced

```