display igmp snooping invalid-packet verbose
============================================

display igmp snooping invalid-packet verbose

Function
--------



The **display igmp snooping invalid-packet verbose** command displays information about invalid IGMP Snooping packets.




Format
------

**display igmp snooping invalid-packet** [ *packet-number* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-number* | Displays information about the specified number of invalid IGMP Snooping packets latest received. | The value is an integer ranging from 1 to 100. By default, information about all the stored invalid IGMP Snooping packets is displayed. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display igmp snooping invalid-packet** command displays statistics and information about invalid IGMP snooping packets, helping to locate and rectify faults.If IGMP Snooping entries cannot be created on a multicast network, you can run the **display igmp snooping invalid-packet** command to check whether this fault is caused by invalid IGMP Snooping packets received. If the command output shows that the number of invalid IGMP Snooping packets is not 0, run the **display igmp snooping invalid-packet verbose** command to check detailed information about the invalid IGMP Snooping packets for fault location.If the multicast layer-2 invalid-packet igmp snooping max-count has been configured and the max-number value differs from the packet-number value in the **display igmp snooping invalid-packet verbose** command, detailed information about invalid IGMP Snooping packets is displayed based on the smaller one of the two values.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the latest two invalid IGMP Snooping packets received.
```
<HUAWEI> display igmp snooping invalid-packet 2 verbose
       Detailed information of invalid packets
-----------------------------------------------------
Packet information (Index 1):
-----------------------------------------------------
Interface           :  100GE1/0/1
Vlanid              :  10
Time                :  2010-6-1 20:04:35 UTC-08:00
Message Length      :  26
Invalid Type        :  Invalid Multicast Source
Source Address      :  10.0.3.11
0000: 25 00 96 77 01 00 00 20 e1 01 01 01 01 00 e0 00
0010: 00 00 80 00 00 64 00 00 00 00
-----------------------------------------------------

```

**Table 1** Description of the **display igmp snooping invalid-packet verbose** command output
| Item | Description |
| --- | --- |
| Detailed information of invalid packets | Detailed information about invalid packets. |
| Packet information (Index 1) | Indexes of invalid packets arranged in the reverse order as they are received. |
| Interface | Interface from which invalid packets are received. |
| Vlanid | VLAN from which invalid packets are received. |
| Time | Format of the time when the invalid packets are received:   * YYYY-MM-DD HH:MM:SS. * YYYY-MM-DD HH:MM:SS UTC±HH:MM DST. * YYYY-MM-DD HH:MM:SS UTC±HH:MM. * YYYY-MM-DD HH:MM:SS DST.   The UTC±HH:MM information can be set using the clock timezone command, and the DST information can be set using the clock daylight-saving-time command. |
| Message Length | Length of invalid packets. |
| Invalid Type | Type of invalid packets. |
| Source Address | Source address of invalid packets. |
| 0000: 25 00 96 77 01 00 00 20 e1 01 01 01 01 00 e0 00 0010: 00 00 80 00 00 64 00 00 00 00 | Contents of invalid packets. |