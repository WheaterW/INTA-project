c-rp holdtime
=============

c-rp holdtime

Function
--------



The **c-rp holdtime** command sets a timeout period during which the bootstrap router (BSR) waits to receive Advertisement messages from candidate-rendezvous points (C-RPs).

The **undo c-rp holdtime** command restores the default setting.



By default, a timeout period during which the BSR waits to receive Advertisement messages from C-RPs is 150 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-rp holdtime** *interval*

**undo c-rp holdtime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a timeout period during which the BSR waits to receive Advertisement messages from C-RPs. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the c-rp holdtime command is run for a C-RP, the C-RP encapsulates interval in an Advertisement message and sends it to the BSR. The BSR obtains this interval from the message and starts the timer. If the BSR does not receive the Advertisement message from the C-RP after the timeout period expires, the BSR regards the C-RP invalid or unreachable.


Example
-------

# In the public network instance, specify 100 seconds as the timeout period during which the BSR waits to receive Advertisement messages from C-RPs.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-rp holdtime 100

```