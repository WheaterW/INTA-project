holdtime assert
===============

holdtime assert

Function
--------



The **holdtime assert** command globally sets a timeout period during which PIM interfaces wait to receive Assert messages from the forwarder.

The **undo holdtime assert** command restores the default timeout period.



By default, the timeout period is 180 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**holdtime assert** *assertHoldVal*

**undo holdtime assert**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *assertHoldVal* | Specifies a timeout period during which PIM interfaces wait to receive Assert messages from the forwarder. | The value is an integer ranging from 7 to 65535, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To prevent redundant traffic, a shared network segment should have only one forwarder. Therefore, a Router sends an Assert message immediately after its forwarding interface receives the same multicast packet on a shared network segment, which indicates that more than one forwarder exists. After all PIM Routers on the shared network segment receive Assert messages, the Routers elect a unique forwarder and refresh the outbound interface lists of (\*, G) and (S, G) entries to prune redundant outbound interfaces. The Router that wins the election is called an assert winner, and all the other Routers are called assert losers. Only the assert winner forwards multicast data.The assert winner periodically sends Assert messages to maintain its winner state. If the assert losers do not receive any Assert messages from the assert winner within a specified timeout period, the assert losers restore the pruned interfaces to forward packets. A new round of assert election is then triggered. To set such a timeout period, run the holdtime assert command.


Example
-------

# In the public network instance, specify 100 seconds as the timeout period during which all interfaces wait to receive Assert messages from the forwarder.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] holdtime assert 100

```