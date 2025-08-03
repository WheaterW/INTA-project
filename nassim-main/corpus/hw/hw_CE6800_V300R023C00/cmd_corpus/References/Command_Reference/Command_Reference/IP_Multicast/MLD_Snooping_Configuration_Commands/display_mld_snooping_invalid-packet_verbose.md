display mld snooping invalid-packet verbose
===========================================

display mld snooping invalid-packet verbose

Function
--------



The **display mld snooping invalid-packet verbose** command displays information about invalid MLD messages received by the device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld snooping invalid-packet** [ *packet-number* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-number* | Displays detailed information about the specified number of invalid MLD snooping packets latest received. | The value is an integer ranging from 1 to 100. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check statistics about invalid MLD messages received by the device, run the **display mld snooping invalid-packet** command. The command output helps locate and rectify faults.If MLD snooping entries cannot be created on a multicast network, run the **display mld snooping invalid-packet** command to check whether this fault is caused by invalid MLD snooping messages received.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about invalid MLD snooping messages received by a device.
```
<HUAWEI> display mld snooping invalid-packet 1 verbose
       Detailed information of invalid packets
-----------------------------------------------------     
Packet information (Index 1):
-----------------------------------------------------
Interface           :  Eth-Trunk1                        
User ID             :  32                            
Time                :  2015-11-19 18:58:10 UTC       
Message Length      :  92                            
Invalid Type        :  Invalid Multicast Group       
Source Address      :  FE80:2000:3::20               
0000: 60 00 00 00 00 34 00 01 fe 80 20 00 00 03 00 00 
0010: 00 00 00 00 00 00 00 20 ff 02 00 00 00 00 00 00 
0020: 00 00 00 00 00 00 00 16 3a 00 01 00 05 02 00 00 
0030: 8f 00 39 9b 00 00 00 01 05 00 00 01 f3 37 00 00 
0040: 00 00 00 00 00 00 00 00 00 00 00 00 20 00 00 05 
0050: 00 00 00 00 00 00 00 00 00 00 01 02 
-----------------------------------------------------

```

**Table 1** Description of the **display mld snooping invalid-packet verbose** command output
| Item | Description |
| --- | --- |
| Detailed information of invalid packets | Detailed information of invalid packets. |
| Packet information (Index 1) | Information about packet with index 1. |
| Interface | Interface name. |
| User ID | User ID. |
| Time | Time when invalid message was received. |
| Message Length | Invalid message length. |
| Invalid Type | Invalid message type. |
| Source Address | Source address. |
| Index | The number of invalid messages sorted by time (reverse order). |