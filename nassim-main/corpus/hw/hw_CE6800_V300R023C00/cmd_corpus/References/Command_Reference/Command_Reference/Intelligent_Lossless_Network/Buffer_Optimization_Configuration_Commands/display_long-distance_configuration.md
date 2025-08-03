display long-distance configuration
===================================

display long-distance configuration

Function
--------



The **display long-distance configuration** command displays the long-distance configuration of each interface and the calculation result of distance-based headroom buffer check.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display long-distance configuration slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After distance-based headroom buffer check is enabled, the device measures the headroom buffer size required by long-distance interfaces. You can run this command to check the calculation result of distance-based headroom buffer check.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the recommended headroom value for a long-distance link.
```
<HUAWEI> display long-distance configuration slot 1
-----------------------------------------------------------------------------------------------------------
Buffer unit: KB
Total buffer: 33280
-----------------------------------------------------------------------------------------------------------
Interface         Port       Chip         PFC            Mode       DetectHdrmResult           RequiredHdrm
-----------------------------------------------------------------------------------------------------------
100GE1/0/1          16          0         Enable         level-100             12496                  12500
100GE1/0/2          20          0         Disable        level-100                 -                  12500
-----------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display long-distance configuration** command output
| Item | Description |
| --- | --- |
| Buffer unit | Buffer unit. |
| Total buffer | Total buffer. |
| Interface | Interface. |
| Port | Interface number. |
| Chip | Chip ID. |
| PFC | Whether PFC is enabled on an interface. |
| Mode | Interface long-distance mode set for distance-based headroom buffer check. |
| DetectHdrmResult | Based on the detection packets, distance-based headroom buffer check calculates the headroom space required for zero-packet-loss transmission on the current link.  If - is displayed, the detection fails. |
| RequiredHdrm | Theoretically required headroom buffer space that is calculated using distance-based headroom buffer check based on the configured long-distance mode of the interface. |