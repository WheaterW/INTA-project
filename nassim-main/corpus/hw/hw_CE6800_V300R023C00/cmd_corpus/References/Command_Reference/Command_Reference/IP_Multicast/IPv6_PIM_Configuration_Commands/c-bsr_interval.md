c-bsr interval
==============

c-bsr interval

Function
--------



The **c-bsr interval** command sets the interval at which the bootstrap router (BSR) sends bootstrap messages.

The **undo c-bsr interval** command restores the default setting.



By default, the interval at which the BSR sends bootstrap messages is 60 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-bsr interval** *interval*

**undo c-bsr interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval* | Specifies an interval at which the C-BSR sends bootstrap messages. | The value is an integer ranging from 1 to 107374177, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To maintain the BSR status, a BSR dynamically elected among candidate-bootstrap routers (C-BSRs) needs to periodically send bootstrap messages carrying the BSR IP address and the rendezvous point (RP)-set information to the C-BSRs. To set the interval (called BS\_interval) at which the BSR sends bootstrap messages, run the **c-bsr interval** command.Only the BSR sends bootstrap messages, and each C-BSR starts a timer and waits to receive bootstrap messages from the BSR before the timer times out. The timeout period (called holdtime) of the timer can be configured using the **c-bsr holdtime** command.

* If a C-BSR receives a bootstrap message from the BSR, the C-BSR resets the timer.
* If a C-BSR does not receive a bootstrap message after the holdtime times out, the C-BSR considers the BSR faulty and triggers a new round of BSR election to prevent service interruptions.

Example
-------

# In the public network instance, specify 30 seconds as the interval at which the BSR sends bootstrap messages.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-bsr interval 30

```