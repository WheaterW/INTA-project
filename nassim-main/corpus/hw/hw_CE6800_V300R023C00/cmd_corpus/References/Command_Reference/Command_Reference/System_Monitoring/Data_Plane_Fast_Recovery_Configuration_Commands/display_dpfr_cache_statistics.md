display dpfr cache statistics
=============================

display dpfr cache statistics

Function
--------



The **display dpfr cache statistics** command displays fault table statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dpfr cache statistics slot** *slot-id* [ **chip** *chip-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **chip** *chip-id* | Specifies a chip ID. | The value is an integer. The default value is 0. |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the DPFR fault table statistics on the device in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display DPFR fault table statistics.
```
<HUAWEI> display dpfr cache statistics slot 1
ChipId: 0
---------------------------------------------------------
Protocol          Current           Aged          Created
---------------------------------------------------------
IPv4                    2               0               2
---------------------------------------------------------

```

**Table 1** Description of the **display dpfr cache statistics**  command output
| Item | Description |
| --- | --- |
| Protocol | Protocol type. |
| Current | Current flow table. The maximum specification is 10k. |
| Aged | Number of aged flow tables. The maximum value is 232-1. |
| Created | Number of created flow entries. The maximum value is 232-1. |
| ChipId | Chip ID. |