holdtime assert (VPN instance PIM view/PIM view of a public network instance)
=============================================================================

holdtime assert (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **holdtime assert** command globally sets a timeout period during which PIM interfaces wait to receive Assert messages from the forwarder.

The **undo holdtime assert** command restores the default timeout period.



By default, the timeout period is 180 seconds.


Format
------

**holdtime assert** *interval*

**undo holdtime assert**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a timeout period during which PIM interfaces wait to receive Assert messages from the forwarder. | The value is an integer ranging from 7 to 65535, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent redundant traffic, a shared network segment should have only one forwarder. Therefore, a router sends an Assert message immediately after its forwarding interface receives the same multicast packet on a shared network segment, which indicates that more than one forwarder exists. After all PIM routers on the shared network segment receive Assert messages, the routers elect a unique forwarder and refresh the outbound interface lists of (\*, G) and (S, G) entries to prune redundant outbound interfaces. The router that wins the election is called an assert winner, and all the other routers are called assert losers. Only the assert winner forwards multicast data.The assert winner periodically sends Assert messages to maintain its winner state. If the assert losers do not receive any Assert messages from the assert winner within a specified timeout period, the assert losers restore the pruned interfaces to forward packets. A new round of assert election is then triggered. To set such a timeout period, run the holdtime assert command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the holdtime assert command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, specify 100 seconds as the timeout period during which all interfaces wait to receive Assert messages from the forwarder.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] holdtime assert 100

```