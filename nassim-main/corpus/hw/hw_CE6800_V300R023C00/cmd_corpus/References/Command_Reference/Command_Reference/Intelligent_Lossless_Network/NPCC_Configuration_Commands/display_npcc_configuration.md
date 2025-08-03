display npcc configuration
==========================

display npcc configuration

Function
--------



The **display npcc configuration** command displays the configuration of the NPCC function.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display npcc configuration slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the configuration of the NPCC function.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of the NPCC function.
```
<HUAWEI> display npcc configuration slot 1
NPCC mode: High-throughput
NPCC Enabled Queue: 4
NPCC Enabled Interface:
100GE1/0/1  100GE1/0/2
IPv6 NPCC Enabled Interface:
100GE1/0/1  100GE1/0/2

```

**Table 1** Description of the **display npcc configuration** command output
| Item | Description |
| --- | --- |
| NPCC Enabled Queue | Lossless queue for which the NPCC function is enabled. |
| NPCC Enabled Interface | Interface on which the NPCC function is enabled. |
| NPCC mode | Mode in which NPCC is enabled:   * High-throughput: high-throughput mode. * Low-latency: low-latency mode. * -: The NPCC function is disabled. |
| IPv6 NPCC Enabled Interface | Interface on which IPv6 NPCC is enabled. |