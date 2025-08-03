display arp packet statistics bridge-domain
===========================================

display arp packet statistics bridge-domain

Function
--------



The **display arp packet statistics bridge-domain** command displays statistics about ARP packets in a bridge domain (BD).



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display arp packet statistics bridge-domain** *bd-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bd-id* | Displays statistics about ARP packets in a BD with a specified ID.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view statistics about ARP packets in a BD, run the **display arp packet statistics bridge-domain** command.



**Precautions**



To ensure that the statistics displayed using the display arp packet statistics bridge-domain are valid, first run the reset arp packet statistics bridge-domain command to clear historical statistics.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about ARP packets in BD 10.
```
<HUAWEI> display arp packet statistics bridge-domain 10
ARP Packets Received
  Total:                                        0
  ARP Pkt Receive Request:                      0
  ARP Pkt Receive Gratuitous:                   0
  ARP Pkt Receive Gateway-mac Proxy:            0
  Discard For Host Mismatch:                    0
  Discard For Other:                            0
ARP Packets Sent
  Total:                                        0
  ARP Pkt Send Unicast:                         0
  ARP Pkt Send Broadcast:                       0
  ARP Pkt Send Gratuitous:                      0
  ARP Pkt Send Gateway-mac Proxy:               0
  ARP Pkt Send L2 Proxy:                        0

```

**Table 1** Description of the **display arp packet statistics bridge-domain** command output
| Item | Description |
| --- | --- |
| ARP Packets Received | ARP packets received in a BD. |
| ARP Pkt Receive Gratuitous | Number of received gratuitous ARP packets. |
| ARP Packets Sent | ARP packets sent in a BD. |
| ARP Pkt Send Unicast | Number of sent unicast packets. |
| ARP Pkt Send Gratuitous | Number of sent gratuitous ARP packets. |
| ARP Pkt Send L2 Proxy | Number of proxy packets sent in a BD or by a VBDIF interface. |
| ARP Pkt Receive Request | Number of received request packets (gratuitous ARP packets and gateway proxy packets excluded). |
| ARP Pkt Receive Gateway-mac Proxy | Number of received gateway proxy packets. |
| ARP Pkt Send Broadcast | Number of sent broadcast packets (gratuitous ARP packets and gateway proxy packets excluded). |
| ARP Pkt Send Gateway-mac Proxy | Number of sent gateway proxy packets. |
| Discard For Other | Number of packets discarded due to other reasons. |
| Discard For Host Mismatch | Number of packets discarded due to mismatch in broadcast suppression. |
| Total | Total count. |