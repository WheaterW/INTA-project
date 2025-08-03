assign forward nvo3 egress mark-ecn enable
==========================================

assign forward nvo3 egress mark-ecn enable

Function
--------



The **assign forward nvo3 egress mark-ecn enable** command enables the function of mapping the outer ECN field to the inner ECN field during VXLAN decapsulation.

The **undo assign forward nvo3 egress mark-ecn enable** command disables the function of mapping the outer ECN field to the inner ECN field during VXLAN decapsulation.



By default, the function of mapping the outer ECN field to the inner ECN field during VXLAN decapsulation is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**assign forward nvo3 egress mark-ecn enable**

**undo assign forward nvo3 egress mark-ecn enable**


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

On a VXLAN network, if you want the ECN field setting in the inner packet to inherit the ECN field setting in the outer packet after VXLAN decapsulation so that the inner and outer ECN field settings are the same, run the **assign forward nvo3 egress mark-ecn enable** command to enable the function of mapping the outer ECN field to the inner ECN field.


Example
-------

# Enable the function of mapping the outer ECN field to the inner ECN field during VXLAN decapsulation.
```
<HUAWEI> system-view
[~HUAWEI] assign forward nvo3 egress mark-ecn enable

```