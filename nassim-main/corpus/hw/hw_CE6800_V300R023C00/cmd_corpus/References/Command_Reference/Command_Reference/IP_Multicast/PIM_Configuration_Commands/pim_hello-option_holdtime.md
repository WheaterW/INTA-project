pim hello-option holdtime
=========================

pim hello-option holdtime

Function
--------



The **pim hello-option holdtime** command sets the neighbor timeout period carried in PIM Hello packets to be sent by a PIM interface.

The **undo pim hello-option holdtime** command restores the default value.



By default, the neighbor timeout period carried in PIM Hello packets to be sent by a PIM interface is 105 seconds.


Format
------

**pim hello-option holdtime** *helloHoldTime*

**undo pim hello-option holdtime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *helloHoldTime* | Specifies the neighbor timeout period carried in PIM Hello messages to be sent. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to set the neighbor timeout period carried in PIM Hello packets to be sent by a router. If the receive end does not receive any Hello packet from the local device within the timeout period, the receive end considers that the local neighbor is aged. If routers need to quickly detect PIM neighbor changes, set this parameter to a smaller value, but the value must be greater than the configured interval for sending Hello messages.

**Prerequisites**

The multicast routing function has been enabled using the multicast routing-enable command in the public network instance view or VPN instance view.

**Configuration Impact**

If the pim hello-option holdtime command is run more than once, the latest configuration overrides the previous one.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Set the neighbor timeout period carried in the PIM Hello message sent by the PIM interface vlanif 1 to 120 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim hello-option holdtime 120

```