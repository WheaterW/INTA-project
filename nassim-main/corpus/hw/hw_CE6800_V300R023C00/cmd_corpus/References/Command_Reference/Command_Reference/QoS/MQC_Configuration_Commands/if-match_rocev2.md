if-match rocev2
===============

if-match rocev2

Function
--------



The **if-match rocev2** command configures a matching rule based on RoCEv2 packet information in a traffic classifier.

The **undo if-match rocev2** command deletes a matching rule based on RoCEv2 packet information in a traffic classifier.



By default, a matching rule based on RoCEv2 packet information is not configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match rocev2** { **opcode** *opcode-value* | **qpair** *qpair-value* | **nack** *nack-value* | **udf** **base** **l4-head** { *udf-data* *udf-mask* **offset** *offset-value* } &<1-4> } \*

**undo if-match rocev2** [ **opcode** *opcode-value* | **qpair** *qpair-value* | **nack** *nack-value* | **udf** **base** **l4-head** { *udf-data* *udf-mask* **offset** *offset-value* } &<1-4> ] \*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match ipv6 rocev2** { **opcode** *opcode-value* | **qpair** *qpair-value* | **nack** *nack-value* | **udf** **base** **l4-head** { *udf-data* *udf-mask* **offset** *offset-value* } &<1-4> } \*

**undo if-match ipv6 rocev2** [ **opcode** *opcode-value* | **qpair** *qpair-value* | **nack** *nack-value* | **udf** **base** **l4-head** { *udf-data* *udf-mask* **offset** *offset-value* } &<1-4> ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **opcode** *opcode-value* | Specifies the value of the Opcode field in RoCEv2 packets. | The value is an integer that ranges from 0 to 255. |
| **qpair** *qpair-value* | Specifies the value of the Qpair field in RoCEv2 packets. | The value is an integer ranging from 0 to 16777215. |
| **nack** *nack-value* | Specifies the value of the Nack field in RoCEv2 packets. | The value is an integer that ranges from 0 to 31. |
| **udf** | Matches user-defined fields in RoCEv2 packets. | - |
| **base** | Specifies the packet header that matches a user-defined rule. | - |
| **l4-head** | Packet L4-header. | - |
| *udf-data* | Indicates the value of the user-defined packet field. | The value is a string of 3 to 10 case-insensitive characters. It cannot contain spaces. |
| *udf-mask* | Indicates the mask of the packet field that is customized by the user. | The value is a string of 3 to 10 case-insensitive characters. It cannot contain spaces. |
| **offset** *offset-value* | Indicates the offset of the packet field that is customized by the user. | The value is an integer ranging from 8 to 20. |
| **ipv6** | Indicates the IPv6 packets.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match rocev2** command to classify RoCEv2 packets so that the device processes RoCEv2 packets matching the same traffic classifier in the same manner and provides fine-granular services.

**Precautions**

* If udf or nack is specified in the **if-match rocev2** command, UDF resources are used to deliver rules. In this case, a traffic policy containing a traffic classifier that defines if-match rocev2 can be applied only in the system view.
* If UDF resources are used, the **if-match rocev2** command supports only eight fields, including two fields occupied by RoCEv2 by default, one field occupied by opcode, one to two fields occupied by qpair (two fields will be occupied if the value exceeds 16 bit width), and one to two fields occupied by customized UDF items. Each field supports a 16 bit width.
* If UDF resources are used and the **if-match rocev2** command is configured with the other if-match commands, the traffic policy will fail to be applied.

Example
-------

# Configure a matching rule based on the Opcode value of 10 in RoCEv2 packets in the traffic classifier class1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match rocev2 opcode 10

```