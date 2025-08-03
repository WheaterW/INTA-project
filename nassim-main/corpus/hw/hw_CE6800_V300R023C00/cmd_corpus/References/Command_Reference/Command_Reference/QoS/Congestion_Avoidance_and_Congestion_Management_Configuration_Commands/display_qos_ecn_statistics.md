display qos ecn statistics
==========================

display qos ecn statistics

Function
--------



The **display qos ecn statistics** command displays statistics on packets with the ECN flag on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display qos ecn statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run the display qos ecn statistics command to display statistics on packets with the ECN flag on an interface.

**Precautions**

After ECN is disabled,statistics about packets with the ECN flag are cleared


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on packets with the ECN flag on a specified interface.
```
<HUAWEI> display qos ecn statistics interface 10GE 1/0/1
Interface          ECN-marked packets                                                                                                
------------------------------------                                                                                                
10GE1/0/1                    0                                                                                                
------------------------------------

```

**Table 1** Description of the **display qos ecn statistics** command output
| Item | Description |
| --- | --- |
| Interface | Type and number of the interface. |
| ECN-marked packets | Number of packets with the ECN flag on an interface. |