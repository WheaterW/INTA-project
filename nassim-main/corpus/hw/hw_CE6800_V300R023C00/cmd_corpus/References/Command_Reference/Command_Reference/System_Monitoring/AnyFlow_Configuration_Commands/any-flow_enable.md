any-flow enable
===============

any-flow enable

Function
--------



The **any-flow enable** command configures an action of enabling the AnyFlow function in a traffic behavior.

The **undo any-flow enable** command deletes the configuration.



By default, an action of enabling the AnyFlow function is not configured in a traffic behavior.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**any-flow enable**

**undo any-flow enable**


Parameters
----------

None

Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can configure the MQC function and enable the AnyFlow action in the traffic behavior to monitor and analyze specified TCP, UDP, and VXLAN traffic.


Example
-------

# Enable the AnyFlow function in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] any-flow enable

```