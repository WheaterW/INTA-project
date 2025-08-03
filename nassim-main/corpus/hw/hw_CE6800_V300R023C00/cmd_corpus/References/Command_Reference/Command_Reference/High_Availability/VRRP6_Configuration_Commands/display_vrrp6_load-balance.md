display vrrp6 load-balance
==========================

display vrrp6 load-balance

Function
--------



The **display vrrp6 load-balance** command displays the information about a Virtual Router Redundancy Protocol for IPv6 (VRRP6) load-balance redundancy group (LBRG) and its member groups.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vrrp6 load-balance** [ **interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id* ] [ **member-vrrp** [ **vrid** *member-vrrp-virtual-router-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |
| **vrid** *member-vrrp-virtual-router-id* | Specifies the ID of a VRRP6 LBRG member group. | The value is an integer ranging from 1 to 255. |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP6 LBRG. | The value is an integer ranging from 1 to 255. |
| **member-vrrp** | Displays the information about VRRP6 LBRG member groups. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After you add a VRRP6 backup group to a VRRP6 LBRG, run the **display vrrp6 load-balance** command to check whether the VRRP6 backup group is successfully added to the VRRP6 LBRG. If a VRRP6 LBRG member group is abnormal, run the **display vrrp6 load-balance** command to view the information about the VRRP6 LBRG and its member groups. The information includes the interface on which the VRRP6 LBRG and its member groups are located and the statuses of the VRRP6 LBRG and its member groups. You can use the information to locate faults.

**Precautions**

If you specify neither lbrg-vrid-value nor mem-vrid-value, the **display vrrp6 load-balance** command displays the information about all VRRP6 LBRGs and their member groups.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the information about all VRRP6 LBRGs and their member groups.
```
<HUAWEI> display vrrp6 load-balance member-vrrp
Interface: 100GE1/0/1, load-balance-vrrp vrid: 1, state: Master
Member-vrrp number: 2
    Member-vrrp vrid: 2, state: Backup
    Member-vrrp vrid: 3, state: Master

```

**Table 1** Description of the **display vrrp6 load-balance** command output
| Item | Description |
| --- | --- |
| load-balance-vrrp vrid | ID of the VRRP6 LBRG. |
| Member-vrrp number | Number of member groups in the VRRP6 LBRG. |
| Member-vrrp vrid | ID of the member group in the VRRP6 LBRG. |
| Interface | Interface on which the VRRP6 LBRG is located. |
| state | Status of the member group in the VRRP6 LBRG:   * Master. * Backup. * Initialize. |