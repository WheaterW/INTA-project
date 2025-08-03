pim timer graft-retry
=====================

pim timer graft-retry

Function
--------



The **pim timer graft-retry** command configures the interval at which Graft messages are retransmitted by an interface.

The **undo pim timer graft-retry** command restores the default interval.



By default, the interval for retransmitting Graft messages on an interface is 3 seconds. The default configuration takes effect only after the pim dm command is run on the interface.


Format
------

**pim timer graft-retry** *interval*

**undo pim timer graft-retry**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which an interface retransmits Graft messages. | The value is an integer ranging from 1 to 65535, in seconds. The default value is recommended. |



Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a PIM-DM network, if State-Refresh is enabled on pruned interfaces, it is possible that the forwarding function will never be restored. When a new multicast member is added to a pruned interface, PIM-DM uses the graft mechanism to restore the forwarding function on the interface to save time. In other words, a Router sends a Graft message to require an upstream Router to forward multicast data to this network segment. Upon receipt of the Graft message, the upstream Router returns a Graft-Ack message and re-enables the forwarding function on the interface that received the Graft message. If no Graft-Ack message is received after the pim timer graft-retry is run, the Router will keep sending the same Graft message before it receives a Graft-Ack message from the upstream device.

**Prerequisites**

Multicast has been enabled using the **multicast routing-enable** command.

**Precautions**

The **pim timer graft-retry** command does not apply to interfaces bound to VPNs.


Example
-------

# Set the interval for retransmitting Graft messages to 80 seconds on Vlanif1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim timer graft-retry 80

```