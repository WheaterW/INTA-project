pim ipv6
========

pim ipv6

Function
--------



The **pim ipv6** command enables IPv6 PIM and displays the IPv6 PIM view.

The **undo pim ipv6** command deletes the configuration in the IPv6 PIM view.



By default, IPv6 PIM is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6**

**undo pim ipv6**


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

Global parameters related to IPv6 PIM must be configured in the IPv6 PIM view.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the public network instance view.

**Configuration Impact**

Running the **undo pim ipv6** command interrupts IPv6 PIM services. Therefore, exercise caution when using this command.


Example
-------

# Enter the IPv6 PIM view.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6]

```