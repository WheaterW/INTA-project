igmp snooping proxy
===================

igmp snooping proxy

Function
--------



The **igmp snooping proxy** command enables IGMP snooping proxy in a VLAN.

The **undo igmp snooping proxy** command disables IGMP snooping proxy in a VLAN.



By default, IGMP Snooping Proxy in a VLAN is disabled.


Format
------

**igmp snooping proxy**

**undo igmp snooping proxy**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Forwarding entries are set up based on IGMP messages exchanged between a Layer 3 device and user hosts. If there are many user hosts, redundant IGMP messages increase the workload of the Layer 2 device.IGMP Snooping Proxy can address this problem. IGMP Snooping Proxy provides two functions: querier function and uniform Report/Leave message transmission function. The querier function enables an IGMP Snooping Proxy-enabled device to replace the connected upstream device to send IGMP Query messages. The uniform Report/Leave message transmission function enables an IGMP Snooping Proxy-enabled device to process IGMP Report/Leave messages received from downstream user hosts. Configuring IGMP Snooping Proxy on a device effectively saves bandwidth between the device and the connected upstream device, and reduces the load of the connected upstream device.

**Configuration Impact**

After IGMP Snooping Proxy is enabled on a device, Report messages sent by users will be terminated on the device.

**Precautions**

The **igmp snooping proxy** command can be configured only when the following conditions are met:

* The querier function can be configured on the local device only after static multicast groups are configured on the upstream device. Otherwise, Join messages of users cannot be sent to the upstream device, and users cannot receive multicast data flows.
* When the links from the multicast source to users are on the same Layer 2 network, you can enable the querier function on the Layer 2 forwarding device. In this case, user multicast data packets can be normally received.The querier function fails to be configured in a VLAN in the following situations:
* The dot1q sub-interface has been bound to the VLAN.
* The querier function has been configured in the VLAN.
* IGMP Report message suppression is configured in a VLAN using the **igmp snooping report-suppress** command.
* PIM-SM has been enabled on the VLANIF interface of the VLAN using the **pim sm** command.

It is recommended that the IGMP version configured on the upstream device be the same as that configured on the local device.



Example
-------

# Enable IGMP Snooping Proxy in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping proxy

```