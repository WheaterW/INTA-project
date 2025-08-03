igmp snooping querier enable (Bridge domain view)
=================================================

igmp snooping querier enable (Bridge domain view)

Function
--------



The **igmp snooping querier enable** command enables a querier in a BD.

The **undo igmp snooping querier enable** command disables a querier in a BD.



By default, queriers are disabled in all BDs.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping querier enable**

**undo igmp snooping querier enable**


Parameters
----------

None

Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the querier function is enabled on a Layer 2 device, this device will replace its upstream device to send IGMP Query messages, and will be able to create and maintain multicast forwarding entries at the data link layer, implementing multicast data forwarding.The following conditions must be met before the igmp snooping querier enable command is run:

* The querier function is configured on a device only after a static multicast group is configured on the connected upstream device. Otherwise, Report messages sent by user hosts cannot be sent to the upstream device. As a result, these user hosts cannot receive required multicast data.
* If the paths from a multicast source to user hosts are in the same Layer 2 network, the querier function can be enabled on a Layer 2 device. This does not affect the normal receiving of multicast data packets.

**Precautions**

The querier function fails to be run in a VLAN/VSI/BD in any of the following situations:

* The **igmp snooping proxy** command is used to configure IGMP snooping proxy.

Example
-------

# Enable the querier function in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping querier enable

```