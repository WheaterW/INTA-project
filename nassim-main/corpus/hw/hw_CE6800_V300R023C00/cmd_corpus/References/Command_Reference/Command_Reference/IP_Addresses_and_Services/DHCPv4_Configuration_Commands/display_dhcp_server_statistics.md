display dhcp server statistics
==============================

display dhcp server statistics

Function
--------



The **display dhcp server statistics** command displays statistics on a DHCP server.




Format
------

**display dhcp server statistics**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run the display dhcp server statistics command to check whether the client is correctly configured or the network is connected.

**Follow-up Procedure**

After detecting incorrect message statistics on a DHCP server, run the **reset dhcp server statistics** command to clear message statistics on the DHCP server.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on the DHCP server.
```
<HUAWEI> display dhcp server statistics
 DHCP Server Statistics: 
 
 Client Request:             6 
  Dhcp Discover:             1 
  Dhcp Request:              4 
  Dhcp Decline:              0 
  Dhcp Release:              1 
  Dhcp Inform:               0 
 Server Reply:               4 
  Dhcp Offer:                1 
  Dhcp Ack:                  3 
  Dhcp Nak:                  0 
 Bad Messages:               0

```

**Table 1** Description of the **display dhcp server statistics** command output
| Item | Description |
| --- | --- |
| DHCP Server Statistics | Statistics about the DHCP server. |
| Server Reply | Number of DHCP messages sent from the DHCP server to the DHCP client. |
| Client Request | Number of messages that a DHCP client sends to a DHCP server. |
| Dhcp Discover | Number of DHCP DISCOVER packets sent from the DHCP client to the DHCP server. |
| Dhcp Request | Number of DHCP REQUEST packets sent from the DHCP client to the DHCP server. |
| Dhcp Decline | Number of DHCP DECLINE packets sent from the DHCP client to the DHCP server. |
| Dhcp Release | Number of DHCP RELEASE packets sent from the DHCP client to the DHCP server. |
| Dhcp Inform | Number of DHCP INFORM packets sent from the DHCP client to the DHCP server. |
| Dhcp Offer | Number of DHCP OFFER packets sent from the DHCP server to the DHCP client. |
| Dhcp Ack | Number of DHCP ACK packets sent from the DHCP server to the DHCP client. |
| Dhcp Nak | Number of DHCP NAK packets sent from the DHCP server to the DHCP client. |
| Bad Messages | Number of unknown messages. |