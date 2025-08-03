isolate remote enable
=====================

isolate remote enable

Function
--------



The **isolate remote enable** command configures unidirectional isolation from the access side to the tunnel side in a BD.

The **undo isolate remote enable** command disables unidirectional isolation from the access side to the tunnel side in a BD.



By default, unidirectional isolation from the access side to the tunnel side is disabled in a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isolate remote enable**

**undo isolate remote enable**


Parameters
----------

None

Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a VXLAN network, users in the same BD can directly communicate with each other. To isolate unidirectional traffic from the access side to the tunnel side in a BD, run this command in the BD view.


Example
-------

# Configure isolation from the access side to the tunnel side in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] isolate remote enable

```