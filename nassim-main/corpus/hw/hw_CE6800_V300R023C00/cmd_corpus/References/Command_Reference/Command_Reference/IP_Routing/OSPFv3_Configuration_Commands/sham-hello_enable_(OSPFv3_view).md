sham-hello enable (OSPFv3 view)
===============================

sham-hello enable (OSPFv3 view)

Function
--------



The **sham-hello enable** command enables the sham-hello function of OSPFv3.

The **undo sham-hello** command disables the sham-hello function.



By default, the sham-hello function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**sham-hello enable**

**undo sham-hello**


Parameters
----------

None

Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable the OSPFv3 sham-hello function, run the **sham-hello enable** command. After the command is run, the device can maintain neighbor relationships through not only Hello packets but also LSU and LSAck packets, which strengthens OSPF neighbor relationships.


Example
-------

# Enable the OSPFv3 sham-hello function.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] sham-hello enable

```