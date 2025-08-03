display dot1x-access-profile configuration
==========================================

display dot1x-access-profile configuration

Function
--------



The **display dot1x-access-profile configuration** command displays the configuration of an 802.1X access profile.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display dot1x-access-profile configuration** [ **name** *access-profile-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *access-profile-name* | Displays the configuration of an 802.1X access profile with a specified name.  If name is not specified, the device displays all the 802.1X access profiles configured on the device. If name is specified, the device displays the configuration of a specified 802.1X access profile. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring an 802.1X access profile, you can run this command to check whether the configuration is correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all the 802.1X access profiles configured on the device.
```
<HUAWEI> display dot1x-access-profile configuration
Total of dot1x-access-profile: 5
-------------------------------------------------------------------------------
 ID             Dot1x-Access-Profile Name
-------------------------------------------------------------------------------
 0              dot1x_access_profile
 1              d1
 2              d2
 3              d3
 4              d4
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display dot1x-access-profile configuration** command output
| Item | Description |
| --- | --- |
| ID | 802.1X access profile ID. |
| Dot1x-Access-Profile Name | 802.1X access profile name. |