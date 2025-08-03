igmp snooping proxy (Bridge domain view)
========================================

igmp snooping proxy (Bridge domain view)

Function
--------



The **igmp snooping proxy** command enables IGMP snooping proxy in a BD.

The **undo igmp snooping proxy** command disables IGMP snooping proxy in a BD.



By default, IGMP Snooping Proxy in a BD is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping proxy**

**undo igmp snooping proxy**


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

Forwarding entries are set up based on IGMP messages exchanged between a Layer 3 device and user hosts. If there are many user hosts, redundant IGMP messages increase the workload of the Layer 2 device.IGMP Snooping Proxy can address this problem. IGMP Snooping Proxy provides two functions: querier function and uniform Report/Leave message transmission function. The querier function enables an IGMP Snooping Proxy-enabled device to replace the connected upstream device to send IGMP Query messages. The uniform Report/Leave message transmission function enables an IGMP Snooping Proxy-enabled device to process IGMP Report/Leave messages received from downstream user hosts. Configuring IGMP Snooping Proxy on a device effectively saves bandwidth between the device and the connected upstream device, and reduces the load of the connected upstream device.

**Configuration Impact**

After IGMP Snooping Proxy is enabled on a device, Report messages sent by users will be terminated on the device.

**Precautions**

If the vtep-src command has been run in the BD view, IGMP snooping cannot be configured in the BD view.The **igmp snooping proxy** command can be configured only when the following conditions are met:

* The querier function can be configured on the local device only after static multicast groups are configured on the upstream device. Otherwise, Join messages of users cannot be sent to the upstream device, and users cannot receive multicast data flows.
* When the links from the multicast source to users are on the same Layer 2 network, you can enable the querier function on the Layer 2 forwarding device. In this case, user multicast data packets can be received normally.The querier function fails to be configured in a BD in the following situations:
* IGMP Report message suppression has been configured in the BD using the **igmp snooping report-suppress** command.

It is recommended that the IGMP version configured on the upstream device be the same as that configured on the local device.


Example
-------

# Enable IGMP Snooping Proxy in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping proxy

```