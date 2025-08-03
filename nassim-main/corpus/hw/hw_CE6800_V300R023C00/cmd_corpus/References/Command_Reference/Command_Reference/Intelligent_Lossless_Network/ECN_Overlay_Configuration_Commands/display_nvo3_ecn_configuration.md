display nvo3 ecn configuration
==============================

display nvo3 ecn configuration

Function
--------



The **display nvo3 ecn configuration** command displays whether functions of the ECN Overlay feature are enabled.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display nvo3 ecn configuration**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The ECN Overlay feature includes the function of mapping the outer ECN field to the inner ECN field during VXLAN decapsulation and the inner ECN marking function on a transit node. You can run this command to check whether the two functions are enabled.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display whether functions of the ECN Overlay feature are enabled.
```
<HUAWEI> display nvo3 ecn configuration
---------------------------------------------------------------------------------------
 Slot                   Mark inner ECN                      Copy outer ECN
---------------------------------------------------------------------------------------
  1                         Enable                              Disable
---------------------------------------------------------------------------------------

```

**Table 1** Description of the **display nvo3 ecn configuration** command output
| Item | Description |
| --- | --- |
| Slot | Slot number. |
| Mark inner ECN | Whether the inner ECN marking function is enabled on a transit node. |
| Copy outer ECN | Whether the function of mapping the outer ECN field to the inner ECN field during VXLAN decapsulation is enabled. |