display mux-vlan
================

display mux-vlan

Function
--------



The **display mux-vlan** command displays information about a MUX VLAN.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mux-vlan**


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

To know whether traffic on different interfaces in a VLAN is isolated from each other, run the **display mux-vlan** command to view configurations of the interfaces and VLANs. The command output helps you locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about a MUX VLAN.
```
<HUAWEI> display mux-vlan
Principal Subordinate    Type         Interface
-----------------------------------------------------------------------------
        2          --    principal    100GE1/0/1
        2           4    separate     100GE1/0/4 100GE1/0/5
        2           3    group        100GE1/0/2 100GE1/0/3
-----------------------------------------------------------------------------

```

**Table 1** Description of the **display mux-vlan** command output
| Item | Description |
| --- | --- |
| Principal | Principal VLAN ID. |
| Subordinate | Subordinate VLAN ID, including:   * Separate ID. * Group ID. |
| Type | VLAN type:   * principal. * separate. * group. |
| Interface | Interfaces in different types of VLANs. |