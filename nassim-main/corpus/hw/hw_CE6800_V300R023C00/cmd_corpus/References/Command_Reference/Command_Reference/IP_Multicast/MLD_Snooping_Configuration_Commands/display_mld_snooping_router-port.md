display mld snooping router-port
================================

display mld snooping router-port

Function
--------



The **display mld snooping router-port** command displays information about router ports.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld snooping router-port vlan** *vlan-id*

**display mld snooping router-port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays information about router ports in a specified VLAN. | The value is an integer ranging from 1 to 4063. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The information about a router port is displayed only if the port is in the up state.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about router ports in VLAN 10.
```
<HUAWEI> display mld snooping router-port vlan 10
 Port Name                            UpTime        Expires       Flags
 --------------------------------------------------------------------------
 VLAN 10, 1 router-port(s)
 10GE1/0/1                          00h02m48s        --          STATIC

```

**Table 1** Description of the **display mld snooping router-port** command output
| Item | Description |
| --- | --- |
| Port Name | Type and number of the interface. |
| UpTime | Keepalive time of the interface as a router port. |
| Expires | Remaining aging time of the interface as a router port. |
| Flags | Router port type, which can be either or a combination of the following ones:   * STATIC: indicates a static router port. * DYNAMIC: indicates a dynamic router port. |