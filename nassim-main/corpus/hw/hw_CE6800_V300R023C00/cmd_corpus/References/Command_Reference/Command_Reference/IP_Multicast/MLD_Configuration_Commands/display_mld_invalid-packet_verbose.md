display mld invalid-packet verbose
==================================

display mld invalid-packet verbose

Function
--------



The **display mld invalid-packet verbose** command displays details of invalid Multicast Listener Discovery (MLD) messages received by a device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld invalid-packet** [ *packet-number* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-number* | Displays details of a specified number of invalid MLD messages recently received. | The value is an integer ranging from 1 to 100. By default, details of all the invalid MLD messages currently stored are displayed. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If the command output contains statistics about invalid MLD messages, you need to run the **display mld invalid-packet verbose** command to view details of invalid MLD messages to locate the fault.Run the **display mld invalid-packet verbose** command to view details of invalid MLD messages recently received. Currently, details of a maximum of 100 invalid MLD messages can be displayed


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display details of one invalid MLD message recently received in the public network instance.
```
<HUAWEI> display mld invalid-packet 1 verbose
       Detailed information of invalid packets
-----------------------------------------------------                           
Packet information (Index 1):
-----------------------------------------------------
Interface           :  100GE1/0/1
Time                :  2022-6-9 15:56:30 UTC
Message Length      :  44
Invalid Type        :  Invalid Ipv6 Multicast Group
Source Address      :  2001:DB8:1::1
0000: 8f 00 a1 62 00 00 00 01 01 00 00 01 ff 11 00 00
0010: 00 00 00 00 00 00 00 00 00 00 00 01 fe c0 00 00
0020: 00 00 01 01 02 00 00 00 c0 55 01 01
-----------------------------------------------------

```

**Table 1** Description of the **display mld invalid-packet verbose** command output
| Item | Description |
| --- | --- |
| Detailed information of invalid packets | Details about the invalid message. |
| Packet information (Index 1) | Sequence number of the invalid message (numbered in the opposite order that the message is received). |
| Interface | Interface that receives the invalid message. |
| Time | Time when the invalid IPv6 PIM message is received, in any of the following formats:   * YYYY-MM-DD HH:MM:SS. * YYYY-MM-DD HH:MM:SS UTC±HH:MM DST. * YYYY-MM-DD HH:MM:SS UTC±HH:MM. * YYYY-MM-DD HH:MM:SS DST.   UTC±HH:MM indicates that a time zone is configured through the clock timezone command; DST indicates that the daylight saving time is configured through clock daylight-saving-time command. |
| Message Length | Length of the invalid message. |
| Invalid Type | Type of the invalid MLD message:   * Unwanted Source List. * Zero Max Resp Code. * Fault Length. * Invalid Multicast Group. * Bad Checksum. * Invalid Multicast Source. * Illegal Report Type. |
| Source Address | Multicast source address. |