display pim ipv6 invalid-packet verbose
=======================================

display pim ipv6 invalid-packet verbose

Function
--------



The **display pim ipv6 invalid-packet verbose** command displays statistics about invalid IPv6 PIM messages received by a device and details of these messages.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 invalid-packet** [ *packet-number* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-number* | Displays details of a specified number of invalid IPv6 PIM messages recently received. | The value is an integer ranging from 1 to 100. By default, details of all the invalid IPv6 PIM messages currently stored are displayed. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If the command output contains statistics about invalid IPv6 PIM messages, you need to run the **display pim ipv6 invalid-packet verbose** command to view details of invalid IPv6 PIM messages to locate the fault.You can run the **display pim ipv6 invalid-packet verbose** command to view details of invalid IPv6 PIM messages recently received. Currently, details of a maximum of 100 invalid IPv6 PIM messages can be displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display details of one invalid IPv6 PIM message recently received in the public network instance.
```
<HUAWEI> display pim ipv6 invalid-packet 1 verbose
       Detailed information of invalid packets
-----------------------------------------------------
Packet information (Index 1):
-----------------------------------------------------
Interface           :  100GE1/0/1
Time                :  2010-6-1 20:04:35 UTC-08:00
Message Length      :  26
Invalid Type        :  Invalid Multicast Source
0000: 25 00 96 77 01 00 00 20 e1 01 01 01 01 00 e0 00
0010: 00 00 80 00 00 64 00 00 00 00
-----------------------------------------------------

```

**Table 1** Description of the **display pim ipv6 invalid-packet verbose** command output
| Item | Description |
| --- | --- |
| Detailed information of invalid packets | Details of the invalid IPv6 PIM message. |
| Packet information (Index 1) | Sequence number of the invalid IPv6 PIM message (numbered in the opposite order that the message is received, for example, the index of the last received message is 1, the index of the last but one message is 2, and so on). |
| Interface | Interface receiving the invalid IPv6 PIM message. |
| Time | Time when the invalid IPv6 PIM message is received, in any of the following formats:   * YYYY-MM-DD HH:MM:SS. * YYYY-MM-DD HH:MM:SS UTC±HH:MM DST. * YYYY-MM-DD HH:MM:SS UTC±HH:MM. * YYYY-MM-DD HH:MM:SS DST.   UTC±HH:MM indicates that a time zone is configured through the clock timezone command; DST indicates that the daylight saving time is configured through clock daylight-saving-time command. |
| Message Length | Length of the invalid IPv6 PIM message. |
| Invalid Type | Type of the invalid IPv6 PIM message. |
| 0000: 25 00 96 77 01 00 00 20 e1 01 01 01 01 00 e0 00 0010: 00 00 80 00 00 64 00 00 00 00 | Contents of the invalid IPv6 PIM message. |