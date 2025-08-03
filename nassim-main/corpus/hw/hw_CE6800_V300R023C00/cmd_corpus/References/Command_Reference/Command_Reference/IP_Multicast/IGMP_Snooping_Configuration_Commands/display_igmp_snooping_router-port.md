display igmp snooping router-port
=================================

display igmp snooping router-port

Function
--------



The **display igmp snooping router-port** command displays information about router ports.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display igmp snooping router-port vlan** *vlanid*

**display igmp snooping router-port**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display igmp snooping router-port bridge-domain** *BdId*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bridge-domain** *BdId* | Displays information about router ports in a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |
| **vlan** *vlanid* | Displays information about router ports in a specified VLAN. | The value is an integer that ranges from 1 to 4094. |



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
<HUAWEI> display igmp snooping router-port vlan 10
Port Name                         UpTime           Expires         Flags
 ---------------------------------------------------------------------
 VLAN 10, 1 router-port(s)
 100GE1/0/1                       00:00:17         --             STATIC

```

**Table 1** Description of the **display igmp snooping router-port** command output
| Item | Description |
| --- | --- |
| Port Name | Type and number of the interface. |
| UpTime | Keepalive time of the interface as a router port. |
| Expires | Remaining aging time of the interface as a router port. |
| Flags | Router port type, which can be either or a combination of the following ones:   * STATIC: indicates a static router port. * DYNAMIC: indicates a dynamic router port. |