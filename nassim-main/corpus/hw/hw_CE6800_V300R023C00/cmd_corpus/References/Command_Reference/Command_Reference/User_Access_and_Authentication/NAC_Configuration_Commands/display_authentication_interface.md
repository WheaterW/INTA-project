display authentication interface
================================

display authentication interface

Function
--------



The **display authentication interface** command displays the configuration of the NAC authentication mode on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display authentication interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Displays 802.1X authentication information of a specified interface. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |
| *interface-type* *interface-number* | Displays the configuration of the NAC authentication mode on a specified interface.  * interface-type specifies the interface type. * interface-number specifies the interface number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring the NAC authentication mode, you can run this command to check the configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of the NAC authentication mode on 10GE1/0/1.
```
<HUAWEI> display authentication interface 10ge 1/0/1
Authentication profile: p1
Authentication access-point: Enable
Authentication access-point max-user: 10
Port authentication order:
                          DOT1X

```

**Table 1** Description of the **display authentication interface** command output
| Item | Description |
| --- | --- |
| Authentication profile | Name of the authentication profile applied to the interface. |
| Authentication access-point | Whether the interface functions as an access control point. |
| Authentication access-point max-user | Maximum number of users who are allowed to log in through an access control point. |
| Port authentication order | Authentication mode configured in the authentication profile applied to the interface:   * DOT1X: 802.1X authentication. |