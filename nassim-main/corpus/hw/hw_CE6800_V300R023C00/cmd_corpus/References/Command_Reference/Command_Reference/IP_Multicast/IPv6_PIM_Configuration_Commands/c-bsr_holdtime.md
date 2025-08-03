c-bsr holdtime
==============

c-bsr holdtime

Function
--------



The **c-bsr holdtime** command sets a timeout period during which candidate-bootstrap routers (C-BSRs) wait to receive bootstrap messages from the BSR.

The **undo c-bsr holdtime** command restores the default setting.



By default, the timeout period is 130 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-bsr holdtime** *holdtimeValue*

**undo c-bsr holdtime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *holdtimeValue* | Specifies a timeout period during which C-BSRs wait to receive bootstrap messages from the BSR. | The value is an integer ranging from 1 to 214748364, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To maintain the bootstrap router (BSR) status, a BSR dynamically elected among C-BSRs needs to send bootstrap messages carrying the BSR IP address and the rendezvous point (RP)-set information to the C-BSRs at a specific interval (called BS\_interval) that can be set using the **c-bsr interval** command.Only the BSR sends bootstrap messages, and each C-BSR starts a timer and waits to receive bootstrap messages from the BSR before the timer times out. To set the timeout period (called holdtime) of the timer, run the **c-bsr holdtime** command.

* If a C-BSR receives a bootstrap message from the BSR, the C-BSR resets the timer.
* If a C-BSR does not receive a bootstrap message after the holdtime times out, the C-BSR considers the BSR faulty and triggers a new round of BSR election to prevent service interruptions.

Example
-------

# In the public network instance, specify 150 seconds as the timeout period during which C-BSRs wait to receive bootstrap messages from the BSR.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-bsr holdtime 150

```