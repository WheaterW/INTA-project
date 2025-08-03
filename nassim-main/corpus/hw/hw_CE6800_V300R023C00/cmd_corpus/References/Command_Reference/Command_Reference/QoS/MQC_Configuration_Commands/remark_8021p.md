remark 8021p
============

remark 8021p

Function
--------



The **remark 8021p** command configures an action of re-marking the 802.1p priority in VLAN packets in a traffic behavior.

The **undo remark 8021p** command deletes the configuration.



By default, an action of re-marking the 802.1p priority in VLAN packets is not configured in a traffic behavior.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**remark 8021p** { *8021p-value* | **inner-8021p** }

**undo remark 8021p** [ { *8021p-value* | **inner-8021p** } ]

For CE6885-LL (low latency mode):

**remark 8021p** *8021p-value*

**undo remark 8021p** [ *8021p-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *8021p-value* | Specifies the 802.1p priority in VLAN packets. | The value is an integer that ranges from 0 to 7. A larger value indicates a higher priority in VLAN packets. |
| **inner-8021p** | Inherits the 802.1p priority in the inner tag.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To provide differentiated services based on the inner 802.1p priority in VLAN packets, run the **remark 8021p** command to configure the device to re-mark the inner 802.1p priority in VLAN packets in a traffic behavior.

**Follow-up Procedure**

Run the **traffic policy** command to create a traffic policy and run the **classifier behavior** command in the traffic policy view to bind the traffic classifier to the traffic behavior containing 802.1p priority re-marking.

**Precautions**

* If you run the **remark 8021p** command in the same traffic behavior view multiple times, only the latest configuration takes effect.
* The **remark 8021p** command can change only the 802.1p priority of packets but not queues where packets are scheduled. To change the queues where packets are scheduled, run the **remark local-precedence** command.
* When a traffic policy containing remark 8021p is applied to the inbound direction, the traffic policy takes effect only for Layer 2 packets.
* When you run the remark 8021p inner-8021p command to configure packets to inherit the 802.1p priority from the inner tag, the 802.1p priority inherited by packets remains unchanged if the packets carry a single tag.
* Traffic behaviors defining remark dscp and remark 8021p can be configured in the same traffic policy and take effect at the same time.
* When a traffic policy containing remark 8021p is applied to the inbound direction of an interface and the **undo qos phb marking 8021p disable** command is run to enable PHB mapping for outgoing packets, the **undo qos phb marking 8021p disable** command takes effect first, and the **remark 8021p** command takes effect last. When a traffic policy containing remark 8021p is applied to the outbound direction of an interface and the **undo qos phb marking 8021p disable** command is run to enable PHB mapping for outgoing packets, the **remark 8021p** command takes effect first, and the **undo qos phb marking 8021p disable** command takes effect last. When a traffic policy containing remark 8021p inner-8021p is applied to the inbound direction of an interface and the **undo qos phb marking 8021p disable** command is run to enable PHB mapping for outgoing packets, the **undo qos phb marking 8021p disable** command takes effect first, and the remark 8021p inner-8021p command takes effect last.
* The remark 8021p inner-8021p command cannot be applied to the outbound direction.
* If the **remark local-precedence** command is configured in a traffic behavior, the traffic behavior does not support the remark 8021p action.
* The network-slice-instance action and remark 8021p inner-8021p cannot be configured together in a traffic behavior.


Example
-------

# Re-mark 802.1p priorities of VLAN packets with 4 in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] remark 8021p 4

```

# Configure a traffic behavior named b1 to re-mark the 802.1p priority of VLAN packets as the inner 802.1p priority.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] remark 8021p inner-8021p

```