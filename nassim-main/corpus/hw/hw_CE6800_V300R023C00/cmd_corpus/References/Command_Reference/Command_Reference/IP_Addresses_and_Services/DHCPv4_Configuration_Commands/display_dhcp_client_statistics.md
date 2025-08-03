display dhcp client statistics
==============================

display dhcp client statistics

Function
--------



The **display dhcp client statistics** command displays message statistics on a DHCP/BOOTP client.




Format
------

**display dhcp client statistics** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays message statistics on a specified interface. | - |
| *interface-name* | Displays message statistics on a specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When the device functions as the DHCP client, the display dhcp client statistics command displays message statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display message statistics on a DHCP/BOOTP client.
```
<HUAWEI> display dhcp client statistics
DHCP message statistics on interface vlanif10 :                     
Input: total 0 packets                                                          
  Bootp reply             :          0                                          
  Offer                   :          0                                          
  Ack                     :          0                                          
  Nak                     :          0                                          
Output: total 0 packets                                                         
  Bootp request           :          0                                          
  Discover                :          0                                          
  Request                 :          0                                          
    Request of init-reboot:          0                                          
    Request of selecting  :          0                                          
    Request of renewing   :          0                                          
    Request of rebinding  :          0                                          
  Decline                 :          0                                          
  Release                 :          0

```

**Table 1** Description of the **display dhcp client statistics** command output
| Item | Description |
| --- | --- |
| Bootp reply | Number of BOOTP replies received by the client from the server. |
| Bootp request | Number of BOOTP requests received by the server from the client. |
| Offer | Number of Offer messages received by the client from the server. |
| Ack | Number of ACK messages received by the client from the server. |
| Nak | Number of NAK messages received by the client from the server. |
| Discover | Number of Discover messages received by the server from the client. |
| Request | Number of Request messages received by the server from the client. |
| Request of init-reboot | Number of Request of init-reboot messages received by the server from the client. |
| Request of selecting | Number of Request of selecting messages received by the server from the client. |
| Request of renewing | Number of Request of renewing messages received by the server from the client. |
| Request of rebinding | Number of Request of rebinding messages received by the server from the client. |
| Decline | Number of Decline messages received by the server from the client. |
| Release | Number of Release messages received by the server from the client. |
| Input | Total number of DHCP messages received by the client. |
| Output | Total number of messages forwarded by the client. |