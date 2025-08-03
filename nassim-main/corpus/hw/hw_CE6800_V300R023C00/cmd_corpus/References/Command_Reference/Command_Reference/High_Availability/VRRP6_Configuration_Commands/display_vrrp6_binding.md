display vrrp6 binding
=====================

display vrrp6 binding

Function
--------



The **display vrrp6 binding** command displays the binding between a management Virtual Router Redundancy Protocol for IPv6 (mVRRP6) group and a service VRRP6 backup group.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vrrp6 binding** [ **interface** { *admin-if-name* | *admin-if-type* *admin-if-num* } ] [ **vrid** *admin-vrid-value* ] [ **member-vrrp** [ **interface** { *member-if-name* | *member-if-type* *member-if-num* } ] [ **vrid** *member-vrid-value* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *member-if-name* *member-if-type* *member-if-num* | Specifies the type and number of an interface on which an mVRRP6 group is configured. | - |
| **interface** *admin-if-name* *admin-if-type* *admin-if-num* | Specifies the type and number of an interface on which a service VRRP6 backup group is configured. | - |
| **vrid** *member-vrid-value* | Specifies the ID of an mVRRP6 group. | The value is an integer ranging from 1 to 255. |
| **vrid** *admin-vrid-value* | Specifies the ID of a service VRRP6 group. | The value is an integer ranging from 1 to 255. |
| **member-vrrp** | Specifies the VRRP member group. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After a service VRRP6 group is bound to an mVRRP6 group or the status of a service VRRP6 group is abnormal, run the display vrrp6 binding admin-vrrp6 command to view the binding between the mVRRP6 group and service VRRP6 group. The binding includes the following information:

* Interfaces on which the mVRRP6 backup group and service VRRP6 backup group are configured
* Master/Backup status of the mVRRP6 backup group and service VRRP6 backup groupThe information helps you rapidly locate faults.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the bindings between all mVRRP6 and service VRRP6 backup groups.
```
<HUAWEI> display vrrp6 binding member-vrrp
Interface: 100GE1/0/1, admin-vrrp vrid: 1, state: Master
  Member-vrrp number: 2
    Interface: 100GE1/0/1, vrid: 2, state: Master
    Interface: 100GE1/0/2, vrid: 3, state: Master

```

**Table 1** Description of the **display vrrp6 binding** command output
| Item | Description |
| --- | --- |
| admin-vrrp vrid | ID of the mVRRP6 group. |
| Member-vrrp number | Number of service VRRP6 groups bound to the mVRRP6 backup group. |
| Interface | Interface on which the service VRRP6 group is configured. |
| state | Status of the service VRRP6 group:   * Master. * Backup. * Initialize. |
| vrid | ID of the service VRRP6 group. |