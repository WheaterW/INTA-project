evpn-overlay enable
===================

evpn-overlay enable

Function
--------



The **evpn-overlay enable** command enables EVPN.

The **undo evpn-overlay enable** command disables EVPN.



By default, EVPN is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**evpn-overlay enable**

**undo evpn-overlay enable**


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

On a network where EVPN services need to be deployed, run this command.

**Precautions**

Before running the **undo evpn-overlay enable** command, delete other EVPN configurations.


Example
-------

# Enable EVPN.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable

```