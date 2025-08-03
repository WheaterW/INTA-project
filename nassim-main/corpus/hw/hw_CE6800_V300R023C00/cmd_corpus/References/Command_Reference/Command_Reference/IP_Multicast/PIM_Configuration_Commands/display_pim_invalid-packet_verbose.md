display pim invalid-packet verbose
==================================

display pim invalid-packet verbose

Function
--------



The **display pim invalid-packet verbose** command displays statistics about received invalid PIM messages and details of these messages.




Format
------

**display pim invalid-packet** [ *packet-number* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-number* | Displays details about a specified number of latest received invalid PIM messages. | The value is an integer ranging from 1 to 100. By default, the command displays details about all received invalid PIM messages. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If packet-number and verbose are specified, the command displays details about the specified number of latest received invalid PIM messages. Currently, details of a maximum of 100 invalid PIM messages can be displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display details of the last received invalid PIM message in the public network instance.
```
<HUAWEI> display pim invalid-packet 1 verbose
       Detailed information of invalid packets
-----------------------------------------------------
Packet information (Index 1):
-----------------------------------------------------
Interface           :  100GE1/0/1
Time                :  2010-6-1 20:04:35 UTC-08:00
Message Length      :  26
Invalid Type        :  Invalid Multicast Source
Source Address      :  10.0.3.3
0000: 25 00 96 77 01 00 00 20 e1 01 01 01 01 00 e0 00
0010: 00 00 80 00 00 64 00 00 00 00
-----------------------------------------------------

```

**Table 1** Description of the **display pim invalid-packet verbose** command output
| Item | Description |
| --- | --- |
| Detailed information of invalid packets | Details about the invalid PIM message. |
| Packet information (Index 1) | Sequence number of the invalid PIM message.  Invalid PIM messages are numbered in the reverse order of the time that messages are received. That is, the last received message has the largest sequence number. |
| Interface | Interface that receives the invalid PIM message. |
| Time | Time when the invalid SPT switch message was received, in any of the following formats:   * YYYY-MM-DD HH:MM:SS. * YYYY-MM-DD HH:MM:SS UTC±HH:MM DST. * YYYY-MM-DD HH:MM:SS UTC±HH:MM. * YYYY-MM-DD HH:MM:SS DST.   UTC±HH:MM indicates that a time zone is configured using the clock timezone command. DST indicates that the daylight saving time is configured using the clock daylight-saving-time command. |
| Message Length | Length of the invalid PIM message. |
| Invalid Type | Type of the invalid PIM message. |
| Source Address | Source address of the invalid PIM message. |
| 0000 | Contents in the invalid PIM message. |