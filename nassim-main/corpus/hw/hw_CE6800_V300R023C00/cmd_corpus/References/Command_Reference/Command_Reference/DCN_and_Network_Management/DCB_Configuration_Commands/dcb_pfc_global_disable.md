dcb pfc global disable
======================

dcb pfc global disable

Function
--------



The **dcb pfc global disable** command disables PFC globally.

The **undo dcb pfc global disable** command enables PFC globally.



By default, PFC is enabled globally.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb pfc global disable**

**undo dcb pfc global disable**


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

Before configuring PFC on an interface, you need to enable PFC globally.When PFC is disabled globally, PFC enabled on an interface is also disabled, and the PFC configuration on the interface cannot be added or changed. However, you can run the **undo dcb pfc enable** command to disable PFC on the interface. After PFC is enabled globally again, PFC will take effect again on the interface if the dcb pfc enable command configuration exists on the interface.


Example
-------

# Disable PFC globally.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc global disable
Warning: This command will disable PFC on all ports. Continue? [Y/N]: y

```