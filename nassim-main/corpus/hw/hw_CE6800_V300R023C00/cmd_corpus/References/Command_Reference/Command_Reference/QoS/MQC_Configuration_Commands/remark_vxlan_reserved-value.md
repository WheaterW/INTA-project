remark vxlan reserved-value
===========================

remark vxlan reserved-value

Function
--------



The **remark vxlan reserved-value** command configures an action of re-marking the VXLAN reserved field in a traffic behavior.

The **undo remark vxlan reserved-value** command deletes the configuration.



By default, an action of re-marking the VXLAN reserved field is not configured in a traffic behavior.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**remark vxlan reserved-value** *rsv-value*

**undo remark vxlan reserved-value** [ *rsv-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rsv-value* | Specifies the value of the VXLAN reserved field. | The value ranges from 0x000000 to 0xFFFFFF in hexadecimal notation, and start with 0x. |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To provide differentiated services based on the VXLAN reserved field of packets, run the **remark vxlan reserved-value** command to configure the device to re-mark the VXLAN reserved field of packets so that the device can provide QoS based on the re-marked VXLAN reserved field.

**Follow-up Procedure**

Run the **traffic policy** command to create a traffic policy and run the **classifier behavior** command in the traffic policy view to bind the traffic classifier to the traffic behavior containing VXLAN reserved field re-marking.

**Precautions**

* Traffic policies which define this traffic behavior can only be applied in the outbound direction.- If you run the **remark vxlan reserved-value** command in the same traffic behavior view multiple times, only the latest configuration takes effect.- After re-marking the VXLAN reserved field of a packet, the switch performs a bitwise OR operation on the configured value and current value in the packet. For example, if the reserved field is 0x112233 and the remark vxlan reserved-value 0x221111 command is configured, the field value after re-marking is 0x333333.

Example
-------

# Re-mark the VXLAN reserved field of packets with 0x8847 in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] remark vxlan reserved-value 0x8847

```