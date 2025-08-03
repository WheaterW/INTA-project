access-limit user-name max-num
==============================

access-limit user-name max-num

Function
--------



The **access-limit user-name max-num** command configures the maximum number of users that can access the network using the same user name.

The **undo access-limit user-name max-num** command restores the default configuration.



By default, the device does not limit the number of access users with the same user name. The number of access users depends on the maximum number of access users supported by the device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**access-limit user-name max-num** *number*

**undo access-limit user-name max-num**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Maximum number of users with the same user name. | The value is an integer that ranges from 0 to 4225. |



Views
-----

Service scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, the device does not limit the number of access users with the same user name. To limit the number of access users using the same user name, run the **access-limit user-name max-num** command. For example, in a home Internet access scenario, all home Internet access users share bandwidth. To facilitate maintenance, the server delivers the same user name to replace the user name entered by the user. In this case, the number of users that can access the network must be limited based on the user name to ensure user experience.

For RADIUS authentication users, the attribute corresponding to the user name is HW-UserName-Access-Limit (26-18).

**Precautions**

Only authenticated users can access the network using the same user name, and pre-connection users cannot.


Example
-------

# In service scheme s1, set the maximum number of users who are allowed to access the network using the same user name to 15.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] service-scheme s1
[~HUAWEI-aaa-service-s1] access-limit user-name max-num 15

```