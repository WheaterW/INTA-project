display dot1x quiet-user
========================

display dot1x quiet-user

Function
--------



The **display dot1x quiet-user** command displays information about 802.1X authentication users who are quieted.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display dot1x quiet-user** { **all** | **mac-address** *mac-address* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays information about all 802.1X authentication users in quiet state. | - |
| **mac-address** *mac-address* | Displays information about an 802.1X authentication user in quiet state with a specified MAC address. | The value is in the H-H-H format. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to view information about 802.1X authentication users who are quieted.

**Precautions**



The quiet function for 802.1X users is enabled by default and cannot be configured.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all 802.1X authentication users who are quieted.
```
<HUAWEI> display dot1x quiet-user all
1 silent mac address(es) found, 1 printed.
-------------------------------------------------------------------------------
 MacAddress                                             Quiet Remain Time(Sec) 
-------------------------------------------------------------------------------
00-e0-fc-12-00-03                                       50
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display dot1x quiet-user** command output
| Item | Description |
| --- | --- |
| MacAddress | MAC address of an 802.1X authentication user who is quieted. |
| Quiet Remain Time(Sec) | Remaining quiet time of an 802.1X authentication user in quiet state, in seconds. |