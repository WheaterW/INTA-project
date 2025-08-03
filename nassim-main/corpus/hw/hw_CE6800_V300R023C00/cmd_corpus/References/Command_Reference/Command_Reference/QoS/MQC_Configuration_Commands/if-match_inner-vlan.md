if-match inner-vlan
===================

if-match inner-vlan

Function
--------



The **if-match inner-vlan** command configures a matching rule based on VLAN IDs in the inner and outer tags of QinQ packets in a traffic classifier. You can specify the VLAN ID range in the inner tag.

The undo if-match inner-vlan command deletes a matching rule based on VLAN IDs in the inner and outer tags of QinQ packets in a traffic classifier.



By default, a matching rule based on the VLAN ID in the inner and outer tags of QinQ packets is not configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match inner-vlan** *start-inner-vlan-value* [ **to** *end-inner-vlan-value* ]

**undo if-match inner-vlan** *start-inner-vlan-value* [ **to** *end-inner-vlan-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-inner-vlan-value* | Specifies the start VLAN ID in the inner tag of a QinQ packet. | The value is an integer ranging from 1 to 4094. |
| **to** *end-inner-vlan-value* | Specifies the end VLAN ID in the inner tag of a QinQ packet. | The value is an integer ranging from 1 to 4094. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match inner-vlan** command to classify packets based on the VLAN ID in the inner tag of QinQ packets so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

* The value of end-inner-vlan-value must be greater than or equal to that of start-inner-vlan-value. When they are the same, only the VLAN specified by start-inner-vlan-value is matched.
* If to end-inner-vlan-value is not specified, only the VLAN specified by start-inner-vlan-value is matched.
* The **if-match inner-vlan** command takes effect only for double-tagged original packets. If there are multiple tags, the second tag is matched.

Example
-------

# Configure a matching rule based on the VLAN ID of 100 in the inner tag of QinQ packets in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1 type and
[*HUAWEI-classifier-c1] if-match inner-vlan 100

```