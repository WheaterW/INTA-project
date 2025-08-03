pim hello-option lan-delay
==========================

pim hello-option lan-delay

Function
--------



The **pim hello-option lan-delay** command sets the delay in transmitting Prune messages on a shared network segment.

The **undo pim hello-option lan-delay** command restores the default setting.



By default, a PIM interface delays sending Prune messages on the shared network segment for 500 milliseconds.


Format
------

**pim hello-option lan-delay** *interval*

**undo pim hello-option lan-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **lan-delay** *interval* | Specifies the delay in sending Prune messages on the shared network segment. | The value is an integer that ranges from 1 to 32767, in milliseconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Hello messages sent by Routers carry lan-delay and override-interval. lan-delay indicates the delay in transmitting messages in the LAN. When the values of lan-delay on all Routers on the same link are different, the maximum value of these values is used.If a Router receives a Prune message from the upstream interface, it indicates that other downstream Routers still exist in the LAN. If the Router still needs to receive multicast data, it must send a Join message to the upstream interface in the override-interval period.When receiving a Prune message from a downstream interface, the Router does not perform the prune action immediately until the Prune-Pending Timer (PPT) times out. The PPT equals the value of the lan-delay plus the override-interval. If the Router receives a Join message from the downstream interface in PPT, the Router cancels the prune action.

**Prerequisites**

The **multicast routing-enable** command is run in the public network instance view or VPN instance view.

**Configuration Impact**

If the pim hello-option lan-delay command is run more than once, the latest configuration overrides the previous one.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Set the delay for VLANIF 1 to transmit Prune messages in the shared network segment to 200 ms.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim hello-option lan-delay 200

```