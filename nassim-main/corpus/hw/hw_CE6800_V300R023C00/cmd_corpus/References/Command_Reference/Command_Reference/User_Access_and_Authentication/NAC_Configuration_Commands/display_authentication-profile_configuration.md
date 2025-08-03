display authentication-profile configuration
============================================

display authentication-profile configuration

Function
--------



The **display authentication-profile configuration** command displays the configuration of an authentication profile.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display authentication-profile configuration** [ **name** *authentication-profile-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *authentication-profile-name* | Displays the configuration of a specified authentication profile.  If name authentication-profile-name is not specified, the device displays all the authentication profiles configured on the device. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring an authentication profile, you can run this command to check whether the configuration is correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all the authentication profiles configured on the device.
```
<HUAWEI> display authentication-profile configuration
Total of authentication-profile: 4
-------------------------------------------------------------------------------
    ID        Auth-profile name
-------------------------------------------------------------------------------
     0        default_authen_profile
     1        dot1x_authen_profile
     2        mac_authen_profile
     3        dot1xmac_authen_profile
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display authentication-profile configuration** command output
| Item | Description |
| --- | --- |
| ID | Authentication profile ID. |
| Auth-profile name | Authentication profile name. |