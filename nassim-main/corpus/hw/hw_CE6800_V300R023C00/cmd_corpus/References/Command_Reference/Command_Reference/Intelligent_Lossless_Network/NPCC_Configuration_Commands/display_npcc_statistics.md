display npcc statistics
=======================

display npcc statistics

Function
--------



The **display npcc statistics** command displays statistics about CNPs proactively sent by an NPCC-enabled forwarder.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display npcc statistics interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays statistics about CNPs on a specified interface.   * interface-type specifies the interface type. * interface-number specifies the interface number. | - |
| **interface** *interface-name* | Displays statistics about CNPs on a specified interface.  interface-name specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to view statistics about CNPs proactively sent by an NPCC-enabled forwarder.

**Precautions**

When the number of CNPs reaches the maximum value, the value is reversed to 0 and the count restarts. The maximum number of CNPs collected on the interface is different from that collected by the chip. If the value is reversed, the number of CNPs collected on the interface is different from that collected by the chip.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about CNPs sent by an NPCC-enabled forwarder (for the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM).
```
<HUAWEI> display npcc statistics interface 100GE1/0/1
Chip Statistics:
  Total Resent CNP Number: 601
  IPv4 Resent CNP Number: 300
  IPv6 Resent CNP Number: 301
  Used Total Flow Entries: 1025
  Used IPv4 Flow Entries: 500
  Used IPv6 Flow Entries: 525

Interface Statistics:
  Average Queue Length: 25KB
  Total Resent CNP Number: 200
  Associated Total Flow Entries: 2
  IPv4 Info:
    Resent CNP Number: 100
    Associated Flow Entries: 1
    -----------------------------------------------------------------------------------------
    DIP                                      SIP                                      SQP
    -----------------------------------------------------------------------------------------
    192.168.20.27                            192.168.10.29                            156243
    -----------------------------------------------------------------------------------------
  IPv6 Info:
    Resent CNP Number: 100
    Associated Flow Entries: 1
    -----------------------------------------------------------------------------------------
    DIP                                      SIP                                      SQP
    -----------------------------------------------------------------------------------------
    2001:DB8:1::2                            2001:DB8:2::3                            156243
    -----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display npcc statistics** command output
| Item | Description |
| --- | --- |
| Chip Statistics | Chip statistics. |
| Total Resent CNP Number | Total number of CNPs sent by the device for proactive compensation. |
| Resent CNP Number | Number of CNPs sent by the device for proactive compensation. |
| IPv4 Resent CNP Number | Number of CNPs triggered by IPv4 traffic that the device proactively sends for compensation. |
| IPv4 Info | IPv4 information. |
| IPv6 Resent CNP Number | Number of CNPs triggered by IPv6 traffic that the device proactively sends for proactive compensation. |
| IPv6 Info | IPv6 information. |
| Used Total Flow Entries | Total number of used flow tables. |
| Used IPv4 Flow Entries | Number of used IPv4 flow tables. |
| Used IPv6 Flow Entries | Number of used IPv6 flow tables. |
| Interface Statistics | Interface statistics. |
| Average Queue Length | Average queue length of unicast packets in NPCC-enabled queues on an interface. |
| Associated Flow Entries | Number of associated flow tables. |
| Associated Total Flow Entries | Total number of associated flow tables. |
| DIP | Destination IP address. |
| SIP | Source IP address. |
| SQP | Source queue pair (QP) value. It can be used to identify an RoCEv2 flow. |