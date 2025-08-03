display vrrp binding
====================

display vrrp binding

Function
--------



The **display vrrp binding** command displays the bindings between an mVRRP group and a common VRRP group, between an mVRRP group and a VRRP-disabled interface, and between an mVRRP group and a service PW.




Format
------

**display vrrp binding** [ **interface** { *interface-name1* | *interface-type1* *interface-number1* } ] [ **vrid** *admin-virtual-router-id* ] [ **member-vrrp** [ **interface** { *interface-name2* | *interface-type2* *interface-number2* } ] [ **vrid** *member-vrid-value* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type2* *interface-number2* | Specifies the type and number of an interface on which a member VRRP group is configured. | - |
| **interface** *interface-type1* *interface-number1* | Specifies the type and number of an interface on which an mVRRP group is configured. | - |
| **vrid** *member-vrid-value* | Specifies the ID of a member VRRP group. | The value is an integer that ranges from 1 to 255. |
| **vrid** *admin-virtual-router-id* | Specifies the ID of an mVRRP group. | The value is an integer ranging from 1 to 255. |
| **member-vrrp** | Displays configurations of a specified member VRRP. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring a binding for an mVRRP group, run the **display vrrp binding** command to check the configuration. If the status of an object bound to an mVRRP group becomes abnormal, run the **display vrrp binding** command to check the binding between the object and mVRRP group. The command output includes the bindings between an mVRRP group and a common VRRP group, between an mVRRP group and a VRRP-disabled interface, and between an mVRRP group and a service PW. It also includes the statuses of the mVRRP group, common VRRP group, VRRP-disabled interface, and service PW.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about mVRRP group 1.
```
<HUAWEI> display vrrp binding
Interface: 100GE1/0/1, admin-vrrp vrid: 1, state: Master
  Member-vrrp number: 1
    Interface: 100GE1/0/2, vrid: 1, state: Master

```

**Table 1** Description of the **display vrrp binding** command output
| Item | Description |
| --- | --- |
| admin-vrrp vrid | ID of the mVRRP group. |
| Member-vrrp number | Number of service VRRP groups bound to the mVRRP group. |
| Interface | Type and number of the interface on which the service VRRP group is configured. |
| vrid | ID of the service VRRP group bound to the mVRRP group. |
| state | Status of the service VRRP group bound to the mVRRP group:   * Master. * Backup. * Initialize. |