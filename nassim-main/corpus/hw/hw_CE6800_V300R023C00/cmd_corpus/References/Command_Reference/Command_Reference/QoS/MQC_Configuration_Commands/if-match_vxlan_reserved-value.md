if-match vxlan reserved-value
=============================

if-match vxlan reserved-value

Function
--------



The **if-match vxlan reserved-value** command configures a matching rule based on the VXLAN reserved field in a traffic classifier.

The **undo if-match vxlan reserved-value** command deletes a matching rule based on the VXLAN reserved field in a traffic classifier.



By default, no matching rule based on the VXLAN reserved field is configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match vxlan reserved-value** *reserved-value*

**undo if-match vxlan reserved-value** [ *reserved-value* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match vxlan transit reserved-value** *reserved-value*

**undo if-match vxlan transit reserved-value** [ *reserved-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *reserved-value* | Specifies the value of the VXLAN reserved field. | The value ranges from 0 to ffffff, in hexadecimal notation. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match vxlan reserved-value** command to classify packets based on the VXLAN reserved field so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

* A traffic policy containing this traffic classifier takes effect only on a VXLAN tunnel decapsulation device.
* A traffic policy containing this traffic classifier cannot be applied to the outbound direction.
* If a traffic classifier contains this matching rule, the traffic behavior supports only packet filtering, traffic statistics collection, redirection, re-marking, and policy-based routing (PBR).

* A traffic policy containing this traffic classifier takes effect only on a VXLAN tunnel decapsulation device.
* A traffic policy containing this traffic classifier cannot be applied to the outbound direction.
* If a traffic classifier contains this matching rule, the traffic behavior supports only packet filtering, traffic statistics collection, redirection (redirection to the CPU is not supported), re-marking, and policy-based routing (PBR).


Example
-------

# Configure a matching rule based on the VXLAN reserved field of 0x8847 in the traffic classifier class1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match vxlan reserved-value 0x8847

```