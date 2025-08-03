display msdp invalid-packet verbose
===================================

display msdp invalid-packet verbose

Function
--------



The **display msdp invalid-packet verbose** command displays details about received invalid Multicast Source Discovery Protocol (MSDP) messages.




Format
------

**display msdp invalid-packet** [ *packet-number* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-number* | Displays details about a specified number of latest received invalid MSDP messages. | The value is an integer ranging from 1 to 100. By default, the command displays details about all received invalid MSDP messages. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If the command output contains statistics about invalid MSDP messages, run the **display msdp invalid-packet packet-number verbose** command to view details about invalid MSDP messages to locate faults.Before using the display msdp invalid-packet command, if verbose is specified, the command displays details about latest received invalid MSDP messages. Currently, details of a maximum of 100 invalid messages can be displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display details of the last received invalid MSDP message in the public network instance.
```
<HUAWEI> display msdp invalid-packet 1 verbose
       Detailed information of invalid packets                                       
-----------------------------------------------------                           
Packet information (Index 1):                                                   
-----------------------------------------------------                           
Interface           :  100GE1/0/1                                           
Time                :  2010-6-9 11:25:46 UTC-08:00                              
Message Length      :  22                                                       
Invalid Type        :  Invalid Addr List                                        
Peer Address         :  10.42.162.13
0000: 00 01 00 02 00 69 00 13 00 04 00 00 00 64 00 02                           
0010: 00 04 81 f4 09 c4                                                         
-----------------------------------------------------

```

**Table 1** Description of the **display msdp invalid-packet verbose** command output
| Item | Description |
| --- | --- |
| Detailed information of invalid packets | Details about the invalid message. |
| Packet information (Index 1) | Sequence number of the invalid message (numbered in the opposite order that the message is received). |
| Interface | Interface that receives the invalid message. |
| Time | Time when the invalid IPv6 PIM message is received, in any of the following formats:   * YYYY-MM-DD HH:MM:SS. * YYYY-MM-DD HH:MM:SS UTC±HH:MM DST. * YYYY-MM-DD HH:MM:SS UTC±HH:MM. * YYYY-MM-DD HH:MM:SS DST.   UTC±HH:MM indicates that a time zone is configured through the clock timezone command; DST indicates that the daylight saving time is configured through clock daylight-saving-time command. |
| Message Length | Length of the invalid message. |
| Invalid Type | Type of the invalid message. |
| Peer Address | Peer address of the invalid MSDP message. |
| 0000: 00 01 00 02 00 69 00 13 00 04 00 00 00 64 00 02 | Contents of the invalid message. |