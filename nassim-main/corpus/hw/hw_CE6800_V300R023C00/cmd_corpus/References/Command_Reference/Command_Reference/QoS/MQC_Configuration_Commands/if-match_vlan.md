if-match vlan
=============

if-match vlan

Function
--------



The **if-match vlan** command configures a matching rule based on the VLAN ID of packets in a traffic classifier.

The **undo if-match vlan** command deletes a matching rule based on the VLAN ID of packets in a traffic classifier.



By default, a matching rule based on the VLAN ID of packets is not configured in a traffic classifier.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match vlan** *start-vlan-value*

**if-match vlan** *start-vlan-value* **to** *end-vlan-value*

**undo if-match vlan** *start-vlan-value*

**undo if-match vlan** *start-vlan-value* **to** *end-vlan-value*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match vlan** *start-vlan-value* **inner-vlan** *start-inner-vlan-value*

**if-match vlan** *start-vlan-value* **to** *end-vlan-value* **inner-vlan** *start-inner-vlan-value*

**if-match vlan** *start-vlan-value* **inner-vlan** *start-inner-vlan-value* **to** *end-inner-vlan-value*

**undo if-match vlan** *start-vlan-value* **inner-vlan** *start-inner-vlan-value*

**undo if-match vlan** *start-vlan-value* **to** *end-vlan-value* **inner-vlan** *start-inner-vlan-value*

**undo if-match vlan** *start-vlan-value* **inner-vlan** *start-inner-vlan-value* **to** *end-inner-vlan-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-vlan-value* | Specifies the start outer VLAN ID. | The value is an integer ranging from 1 to 4094. |
| *end-vlan-value* | Specifies the end outer VLAN ID. | end-vlan-value specifies the end outer VLAN ID. The value is an integer that ranges from 1 to 4094.  The value of end-vlan-value must be greater than or equal to that of start-vlan-value. If to end-vlan-value is not specified or start-vlan-value and end-vlan-value are set to the same value, traffic classification is performed based on the VLAN ID specified by start-vlan-value. |
| **inner-vlan** *start-inner-vlan-value* | Specifies the start VLAN ID in the inner tag of a QinQ packet.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 4094. |
| *end-inner-vlan-value* | Specifies the end VLAN ID in the inner tag of a QinQ packet.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value of end-inner-vlan-value is an integer that ranges from 1 to 4094.  The value of end-inner-vlan-value must be greater than or equal to that of start-inner-vlan-value. If to end-inner-vlan-value is not specified or start-inner-vlan-value and end-inner-vlan-value are set to the same value, only the VLAN specified by start-inner-vlan-value is matched. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match vlan** command to classify packets based on the VLAN ID so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

A traffic policy to which a traffic classifier containing the **if-match vlan** command is bound cannot be applied to a sub-interface.


Example
-------

# Configure a matching rule based on VLAN 2 in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1 type and
[*HUAWEI-classifier-c1] if-match vlan 2

```