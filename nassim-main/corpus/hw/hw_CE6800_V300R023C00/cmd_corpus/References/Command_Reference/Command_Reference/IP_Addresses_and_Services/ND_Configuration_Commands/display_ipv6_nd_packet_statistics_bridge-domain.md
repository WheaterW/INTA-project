display ipv6 nd packet statistics bridge-domain
===============================================

display ipv6 nd packet statistics bridge-domain

Function
--------



The **display ipv6 nd packet statistics bridge-domain** command displays the number of sent and received ND messages in a specified BD.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd packet statistics bridge-domain** [ *bd-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bd-id* | Displays the number of sent and received ND messages in a BD with a specified ID.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The bd-id value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To analyze and verify whether the NS multicast suppression function is normal, run the display ipv6 nd packet statistics bridge-domain command to view the number of sent and received ND messages in a specified BD. If the bd-id parameter is specified, the number of sent and received ND messages only in the specified BD is displayed. If the bd-id parameter is not specified, the numbers of sent and received ND messages in all BDs are displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the number of sent and received ND messages in BD 10.
```
<HUAWEI> display ipv6 nd packet statistics bridge-domain 10
ND Packets  Received
Total                          : 0                          
ND Pkt Revceive NS Unicast     : 0                          
ND Pkt Revceive NS Multicast   : 0                          
ND Pkt Revceive NA Unicast     : 0                          
ND Pkt Revceive NA Multicast   : 0                           
ND Pkt Discard NS Unicast      : 0                          
ND Pkt Discard NS Multicast    : 0                          
ND Pkt Discard NA              : 0                          
ND Packets Sent
Total                          : 0                          
ND Pkt Send NS Unicast         : 0                          
ND Pkt Send NS Multicast       : 0                          
ND Pkt Send NA Unicast         : 0                          
ND Pkt Send NA Multicast       : 0

```

**Table 1** Description of the **display ipv6 nd packet statistics bridge-domain** command output
| Item | Description |
| --- | --- |
| ND Packets Received | Received ND messages. |
| ND Pkt Revceive NS Unicast | Number of received NS unicast messages. |
| ND Pkt Revceive NS Multicast | Number of received NS multicast messages. |
| ND Pkt Revceive NA Unicast | Number of received NA unicast messages. |
| ND Pkt Revceive NA Multicast | Number of received NA multicast messages. |
| ND Pkt Discard NS Unicast | Number of discarded NS unicast messages. |
| ND Pkt Discard NS Multicast | Number of discarded NS multicast messages. |
| ND Pkt Discard NA | Number of discarded NA messages. |
| ND Packets Sent | Sent ND messages. |
| ND Pkt Send NS Unicast | Number of sent NS unicast messages. |
| ND Pkt Send NS Multicast | Number of sent NS multicast messages. |
| ND Pkt Send NA Unicast | Number of sent NA unicast messages. |
| ND Pkt Send NA Multicast | Number of sent NA multicast messages. |
| Total | Total number of received or sent ND messages. |