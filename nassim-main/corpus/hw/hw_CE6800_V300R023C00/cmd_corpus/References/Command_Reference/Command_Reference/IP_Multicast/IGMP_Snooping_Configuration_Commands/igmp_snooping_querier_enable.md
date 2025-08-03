igmp snooping querier enable
============================

igmp snooping querier enable

Function
--------



The **igmp snooping querier enable** command enables a querier in a VLAN.

The **undo igmp snooping querier enable** command disables a querier in a VLAN.



By default, queriers are disabled in all VLANs.


Format
------

**igmp snooping querier enable**

**undo igmp snooping querier enable**


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

After the querier function is enabled on a Layer 2 device, this device will replace its upstream device to send IGMP Query messages, and will be able to create and maintain multicast forwarding entries at the data link layer, implementing multicast data forwarding.The following conditions must be met before the igmp-snooping querier enable command is run:

* The querier function is configured on a device only after a static multicast group is configured on the connected upstream device. Otherwise, Report messages sent by user hosts cannot be sent to the upstream device. As a result, these user hosts cannot receive required multicast data.
* If the paths from a multicast source to user hosts are in the same Layer 2 network, the querier function can be enabled on a Layer 2 device. This does not affect the normal receiving of multicast data packets.

**Precautions**

The querier function fails to be run in a VLAN in any of the following situations:

* A Dot1q termination sub-interface has been added to the VLAN.
* The **pim sm** command is used to configure PIM-SM on a VLANIF interface in a VLAN.
* The **igmp snooping proxy** command is used to configure IGMP snooping proxy.


Example
-------

# Enable the querier function in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping querier enable

```