display vrrp load-balance
=========================

display vrrp load-balance

Function
--------



The **display vrrp load-balance** command displays the information about a load-balance redundancy group (LBRG) and its member groups.




Format
------

**display vrrp load-balance** [ **interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id* ] [ **member-vrrp** [ **vrid** *member-vrrp-virtual-router-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |
| **vrid** *member-vrrp-virtual-router-id* | Specifies the ID of an LBRG member group. | The value is an integer ranging from 1 to 255. |
| **vrid** *virtual-router-id* | Specifies the ID of an LBRG. | The value is an integer ranging from 1 to 255. |
| **member-vrrp** | Displays the information about LBRG member groups. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After you add a VRRP backup group to an LBRG, run the **display vrrp load-balance** command to check whether the VRRP backup group is successfully added to the LBRG. If an LBRG member group is abnormal, run the **display vrrp load-balance** command to view the information about the LBRG and its member groups. The information includes the interface on which the LBRG and its member groups are located and the statuses of the LBRG and its member groups. You can use the information to locate faults.

**Precautions**

If you specify neither the ID of an LBRG nor the ID of an LBRG member group, the **display vrrp load-balance** command displays the information about all LBRGs and their member groups.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the information about all LBRGs and their member groups.
```
<HUAWEI> display vrrp load-balance member-vrrp
Interface: 100GE1/0/1, load-balance-vrrp vrid: 1, state: Master
Member-vrrp number: 2
    Member-vrrp vrid: 2, state: Backup
    Member-vrrp vrid: 3, state: Master

```

**Table 1** Description of the **display vrrp load-balance** command output
| Item | Description |
| --- | --- |
| load-balance-vrrp vrid | ID of an LBRG. |
| Member-vrrp number | Number of member groups in the LBRG. |
| Member-vrrp vrid | Number of the member group in the LBRG. |
| Interface | Interface on which the LBRG is configured. |
| state | Status of the member group in the LBRG.   * Master. * Backup. * Initialize. |