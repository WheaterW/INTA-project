assign forward nvo3 transit mark inner-ecn enable
=================================================

assign forward nvo3 transit mark inner-ecn enable

Function
--------



The **assign forward nvo3 transit mark inner-ecn enable** command enables the inner ECN marking function on a transit node on a VXLAN network.

The **undo assign forward nvo3 transit mark inner-ecn enable** command disables the inner ECN marking function on a transit node on a VXLAN network.



By default, the inner ECN marking function is disabled on a transit node on a VXLAN network.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**assign forward nvo3 transit mark inner-ecn enable**

**undo assign forward nvo3 transit mark inner-ecn enable**


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

When a vSwitch functions as an NVE, it performs VXLAN encapsulation and decapsulation. If the server NIC cannot map the outer ECN field of VXLAN packets to the inner ECN field, the ECN marking information on the transit node will be lost.You can run this command to enable the inner ECN marking function on a transit node on a VXLAN network. The transit node then can map the outer ECN field to the inner ECN field to ensure that ECN marking information can be transmitted.


Example
-------

# Enable the inner ECN marking function on a transit node on a VXLAN network.
```
<HUAWEI> system-view
[~HUAWEI] assign forward nvo3 transit mark inner-ecn enable

```