vlan-mapping (traffic behavior view)
====================================

vlan-mapping (traffic behavior view)

Function
--------



The **vlan-mapping** command configures an action of replacing the VLAN ID in a traffic behavior.

The **undo vlan-mapping** command cancels the configuration.



By default, an action of replacing the VLAN ID in a traffic behavior is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vlan-mapping vlan** *vlan-id*

**vlan-mapping inner-vlan** *inner-vlan-id*

**undo vlan-mapping vlan**

**undo vlan-mapping inner-vlan**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inner-vlan** *inner-vlan-id* | Specifies the inner VLAN tag in VLAN packets. | The value is an integer ranging from 1 to 4094. |
| **vlan** *vlan-id* | Specifies the outer VLAN tag in VLAN packets. | The value is an integer ranging from 1 to 4094. |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To allow user packets to be transmitted on the ISP network, configure the device to change VLAN tags in the user packets to VLAN tags supported by the ISP network before the user packets enter the ISP network. This technology is called VLAN mapping. The vlan-mapping command configures VLAN mapping based on services or users in a traffic behavior.

**Precautions**

vlan-mapping can be configured together with only deny, permit, mac-address learning disable, remark 8021p and remark qos-local-id in the same traffic behavior in the inbound direction.


Example
-------

# Configure the device to replace the outer VLAN tag with VLAN 200.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior tb
[*HUAWEI-behavior-tb] vlan-mapping vlan 200

```

# Configure the device to replace the outer VLAN tag with 200 and inner VLAN tag with 300.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior tb
[*HUAWEI-behavior-tb] vlan-mapping vlan 200
[*HUAWEI-behavior-tb] vlan-mapping inner-vlan 300

```