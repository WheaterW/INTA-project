service-type
============

service-type

Function
--------



The **service-type** command sets the access type for a local access user.

The **undo service-type** command restores the default access type for a local access user.



By default, a local access user cannot use any access type.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**service-type dot1x**

**service-type none**

**undo service-type**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **none** | Indicates no access type. | - |
| **dot1x** | Indicates 802.1X users. | - |



Views
-----

aaa-access-user view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The device can manage access types of local users. After you specify the access type of a user, the user can successfully log in only when the configured access type is the same as the actual access type of the user.


Example
-------

# Set the access type of local access user abc to dot1x.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-access-user abc
[*HUAWEI-aaa-access-user-abc] service-type dot1x

```