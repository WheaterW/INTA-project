hello-option lan-delay (VPN instance PIM view/PIM view of a public network instance)
====================================================================================

hello-option lan-delay (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **hello-option lan-delay** command sets a delay in transmitting Prune messages on a shared network segment.

The **undo hello-option lan-delay** command restores the default setting.



By default, the delay in transmitting Prune messages on a shared network segment is 500 milliseconds.


Format
------

**hello-option lan-delay** *interval*

**undo hello-option lan-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the delay from the time when the current router receives a Prune message from a downstream router to the time when the current router performs the prune action. | The value is an integer that ranges from 1 to 32767, in milliseconds (ms). |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Hello messages sent by routers carry lan-delay and override-interval. lan-delay indicates the delay in transmitting messages in the LAN. When the values of lan-delay on all routers on the same link are different, the maximum value of these values is used.If a router receives a Prune message from the upstream interface, it indicates that other downstream routers still exist in the LAN. If the router still needs to receive multicast data, it must send a Join message to the upstream interface in the override-interval period.The value of the Prune-Pending Timer (PPT) is obtained by the value of lan-delay plus the value of override-interval. PPT refers to the delay during which the current router receives a Prune message from the downstream interface and performs the prune action. If the router receives a Join message from the downstream interface in PPT, the router cancels the prune action.

**Prerequisites**

The **multicast routing-enable** command is run in the public network instance view or VPN instance view.

**Configuration Impact**

If the hello-option lan-delay command is run more than once, the latest configuration overrides the previous one.

**Precautions**

If the delay in transmitting Prune message is too short, the upstream router will stop forwarding multicast packets before the downstream router determines whether to override the Prune action or not. Exercise caution when running this command.


Example
-------

# Set the delay in transmitting Prune message on the shared network segment to 200 ms in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] hello-option lan-delay 200

```