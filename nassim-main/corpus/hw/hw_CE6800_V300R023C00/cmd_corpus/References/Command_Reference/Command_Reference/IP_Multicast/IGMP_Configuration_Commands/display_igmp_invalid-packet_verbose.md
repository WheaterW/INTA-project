display igmp invalid-packet verbose
===================================

display igmp invalid-packet verbose

Function
--------



The **display igmp invalid-packet verbose** command displays statistics about received invalid IGMP messages and details about these messages.




Format
------

**display igmp invalid-packet** [ *packet-number* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-number* | Displays details about a specified number of latest received invalid IGMP messages. | The value is an integer ranging from 1 to 100. By default, the command displays details about all received invalid IGMP messages. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view detailed information about a specified number of invalid IGMP messages that are received recently.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display details of the last received invalid IGMP message in the public network instance.
```
<HUAWEI> display igmp invalid-packet 1 verbose
       Detailed information of invalid packets
-----------------------------------------------------
Packet information (Index 6):
-----------------------------------------------------
Interface           :  100GE1/0/1
Time                :  2010-6-9 11:03:51 UTC-08:00
Message Length      :  24
Invalid Type        :  Invalid Multicast Group
Source Address      :  10.0.3.3
0000: 16 3c 00 00 01 34 04 04
-----------------------------------------------------

```

**Table 1** Description of the **display igmp invalid-packet verbose** command output
| Item | Description |
| --- | --- |
| Detailed information of invalid packets | Details about the invalid message. |
| Packet information (Index 6) | Sequence number of the invalid message (numbered in the opposite order that the message is received). |
| Interface | Interface that receives the invalid message. |
| Time | Time when the invalid IPv6 PIM message is received, in any of the following formats:   * YYYY-MM-DD HH:MM:SS. * YYYY-MM-DD HH:MM:SS UTC±HH:MM DST. * YYYY-MM-DD HH:MM:SS UTC±HH:MM. * YYYY-MM-DD HH:MM:SS DST.   UTC±HH:MM indicates that a time zone is configured through the clock timezone command; DST indicates that the daylight saving time is configured through clock daylight-saving-time command. |
| Message Length | Length of the invalid message. |
| Invalid Type | Type of the invalid message. |
| Source Address | Source address of the invalid message. |
| 0000: 16 3c 00 00 01 34 04 04 | Contents of the invalid message. |