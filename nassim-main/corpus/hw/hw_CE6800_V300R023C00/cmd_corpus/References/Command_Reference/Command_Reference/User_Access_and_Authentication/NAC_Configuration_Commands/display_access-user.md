display access-user
===================

display access-user

Function
--------



The **display access-user** command displays information about NAC access users.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display access-user service-scheme** *service-scheme*

**display access-user event** { **pre-authen** | **authen-fail** | **client-no-response** | **authen-server-down** }

**display access-user access-type** { **dot1x** | **none** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **service-scheme** *service-scheme* | Displays information about users assigned with a specified service scheme. | The value must be the name of an existing service scheme. |
| **event** | Displays information about users in a specified authentication phase. | - |
| **pre-authen** | Displays information about users in the pre-connection phase. | - |
| **authen-fail** | Displays information about users who fail the authentication and are assigned network access policies when the authentication server sends authentication failure packets to the device. | - |
| **client-no-response** | Displays information about users who fail the authentication and are assigned network access policies when the authentication server is down. | - |
| **authen-server-down** | Displays information about users who fail the authentication and are assigned network access policies when the authentication server is down. | - |
| **access-type** | Displays information about online NAC users using a specified authentication mode. | - |
| **dot1x** | Displays information about online 802.1X authentication users. | - |
| **none** | Displays information about users whose AAA scheme is non-authentication. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check information about online NAC users.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about users who are assigned the service scheme huawei.
```
<HUAWEI> display access-user service-scheme huawei
 ------------------------------------------------------------------------------ 
 UserID Username                IP address       MAC            Status          
 ------------------------------------------------------------------------------ 
 16018  zqm                     10.12.12.254     00e0-fc12-3456 Pre-authen      
 ------------------------------------------------------------------------------ 
 Total: 1, printed: 1

```

**Table 1** Description of the **display access-user** command output
| Item | Description |
| --- | --- |
| UserID | ID that is assigned to a user after the user goes online. |
| Username | User name. |
| IP address | User IP address. |
| MAC | User MAC address. |
| Status | User status. |
| Total: m, printed: n | Total number (m) of entries and number (n) of displayed entries. |