flow-matrix
===========

flow-matrix

Function
--------



The **flow-matrix** command enables the Flow Matrix function and displays the Flow Matrix view.

The **undo flow-matrix** command disables the Flow Matrix function.



By default, the Flow Matrix function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**flow-matrix**

**undo flow-matrix**


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

You can run this command to enable the Flow Matrix function, enter the Flow Matrix view, and add flow path planning rules in the Flow Matrix view.

**Precautions**

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-T, CE6885-LL (standard forwarding mode), and CE6863E-48S8CQ:

* The **flow-matrix** command and the **dpfr enable** command in the system view cannot be both configured.
* The **flow-matrix** command and the **system resource large-mac** command in the system view cannot be both configured.

For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:

* The flow-matrix and vxlan-overlay local-preference enable commands cannot be both configured.
* The **flow-matrix** command and two **traffic-policy global inbound** commands in the system view cannot be both configured.


Example
-------

# Enable the Flow Matrix function and enter the Flow Matrix view.
```
<HUAWEI> system-view
[~HUAWEI] flow-matrix
[*HUAWEI-flow-matrix]

```