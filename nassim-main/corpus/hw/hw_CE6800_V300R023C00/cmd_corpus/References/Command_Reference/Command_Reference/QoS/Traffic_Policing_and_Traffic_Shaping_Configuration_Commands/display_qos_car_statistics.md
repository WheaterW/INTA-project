display qos car statistics
==========================

display qos car statistics

Function
--------



The **display qos car statistics** command displays statistics on forwarded and discarded packets in the inbound direction to a specified interface where a QoS CAR profile is applied.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display qos car statistics interface** { *interface-name* | *interface-type* *interface-number* } **inbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **inbound** | Inbound configuration. | - |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display qos car statistics command to check statistics on forwarded and discarded packets in the inbound direction of an interface where a QoS CAR profile is applied. The command output helps you locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on packets in the inbound direction of 10GE1/0/1 to which a QoS CAR profile is applied.
```
<HUAWEI> display qos car statistics interface 10GE 1/0/1 inbound
 Slot : 1 
 Passed packets  :  15284 58733
 Passed bytes     : 403513105512 
 Discarded packets: 1527338616 
 Discarded bytes  : 403217394624

```

**Table 1** Description of the **display qos car statistics** command output
| Item | Description |
| --- | --- |
| Slot | Slot id. |
| Passed packets | Number of forwarded packets on the interface to which a QoS CAR profile is applied. |
| Passed bytes | Number of bytes in forwarded packets on the interface to which a QoS CAR profile is applied. |
| Discarded packets | Number of discarded packets on the interface to which a QoS CAR profile is applied. |
| Discarded bytes | Number of bytes in discarded packets on the interface to which a QoS CAR profile is applied. |