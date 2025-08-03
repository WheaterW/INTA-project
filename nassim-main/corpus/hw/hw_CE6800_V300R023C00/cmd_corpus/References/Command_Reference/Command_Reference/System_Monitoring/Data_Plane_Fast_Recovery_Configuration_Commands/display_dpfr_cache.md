display dpfr cache
==================

display dpfr cache

Function
--------



The **display dpfr cache** command displays the fault table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dpfr cache** [ *ip-address* ] **slot** *slot-id* [ **chip** *chip-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies an IPv4 address. | It is in dotted decimal notation. |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |
| **chip** *chip-id* | Specifies a chip ID. | The value is an integer. The default value is 0. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the DPFR fault table on the device in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the DPFR fault table.
```
<HUAWEI> display dpfr cache slot 1
ChipId: 0
------------------------------------------------------------------                                  
Protocol     DestinationIPv4     Interface    Time             
------------------------------------------------------------------
IPv4         1.1.1.1             10GE1/0/1    2022-10-10 19:49:13
------------------------------------------------------------------

```

**Table 1** Description of the **display dpfr cache** command output
| Item | Description |
| --- | --- |
| Protocol | Protocol type. |
| DestinationIPv4 | Destination IPv4 address. |
| Interface | Interface. |
| Time | Flow table update time. |
| ChipId | Chip ID. |