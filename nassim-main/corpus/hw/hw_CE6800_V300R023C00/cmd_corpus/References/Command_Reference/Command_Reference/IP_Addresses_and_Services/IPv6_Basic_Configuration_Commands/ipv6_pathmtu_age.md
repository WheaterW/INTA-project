ipv6 pathmtu age
================

ipv6 pathmtu age

Function
--------



The **ipv6 pathmtu age** command sets the aging time for a dynamic PMTU.

The **undo ipv6 pathmtu age** command restores the default aging time.



By default, the aging time of the dynamic PMTU is 10 minutes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 pathmtu age** *age-time*

**undo ipv6 pathmtu age**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *age-time* | Specifies the aging time of the dynamic PMTU. | The value is an integer ranging from 10 to 100, in minutes. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can change the lifetime of a PMTU by setting an aging time for the PMTU.If you want to slow down PMTU aging, run the **ipv6 pathmtu age** command to change the aging time of the PMTU to a larger value.

**Configuration Impact**

This command can be used to change only the aging time of dynamic PMTUs. It is not applicable to static PMTUs because static PMTUs cannot age.

**Precautions**

The priority of a static PMTU is higher than that of a dynamic PMTU. If the static PMTU exists, the dynamic PMTU does not take effect.The aging time for the PMTU is valid only for the dynamic PMTU entries generated after this configuration, instead of the PMTU entries generated before this configuration.


Example
-------

# Set the aging time for a dynamic PMTU to 40 minutes.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 pathmtu age 40

```