display ip large-community-filter
=================================

display ip large-community-filter

Function
--------



The **display ip large-community-filter** command displays detailed configurations of a Large-Community filter.




Format
------

**display ip large-community-filter** [ *lcfName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *lcfName* | Displays detailed configurations of a Large-Community filter with a specified name. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check detailed configurations of a Large-Community filter, run the display ip large-community-filter command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all Large-Community filters.
```
<HUAWEI> display ip large-community-filter
Named Large Community basic filter: aaa
    index: 10            permit     1:1:1
Named Large Community advanced filter: abc
    index: 10            deny       1:1:2

```

**Table 1** Description of the **display ip large-community-filter** command output
| Item | Description |
| --- | --- |
| Named Large Community basic filter | Name of a basic Large-Community attribute. |
| Named Large Community advanced filter | Name of an advanced Large-Community attribute. |
| permit | Matching mode, which is permit. |
| deny | Matching mode, which is deny. |
| index | Index of the Large-Community attribute. |