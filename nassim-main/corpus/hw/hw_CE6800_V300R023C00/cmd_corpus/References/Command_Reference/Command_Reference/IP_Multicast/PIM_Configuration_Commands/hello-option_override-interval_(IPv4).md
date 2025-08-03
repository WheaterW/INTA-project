hello-option override-interval (IPv4)
=====================================

hello-option override-interval (IPv4)

Function
--------



The **hello-option override-interval** command sets the interval for overriding the prune action in a Hello message.

The **undo hello-option override-interval** command restores the default interval.



By default, the interval for overriding the prune action in a Hello message is 2500 ms.


Format
------

**hello-option override-interval** *interval*

**undo hello-option override-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies set the interval for overriding the prune action in a Hello message. | The value ranges from 1 to 65535, in milliseconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Hello messages sent by Routers carry lan-delay and override-interval. override-interval refers to the period during which a downstream Router overrides the prune action. When the values of override-interval on all Routers on the same link are different, the maximum value of these values is used.If a Router receives a Prune message from the upstream interface, it indicates that other downstream Routers still exist in the LAN. If the Router still needs to receive multicast data, it must send a Join message to the upstream interface in the override-interval period.The value of PPT is obtained by the value of lan-delay plus the value of override-interval. When receiving a Prune message from a downstream interface, the Router does not perform the prune action until the PPT times out. If the Router receives a Join message from the downstream interface in PPT, the interface cancels the Prune action.

**Prerequisites**

The **multicast routing-enable** command is run in the public network instance view or VPN instance view.

**Configuration Impact**

If the hello-option override-interval command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, set the interval for overriding the prune action in a Hello message to 2000 ms.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] hello-option override-interval 2000

```