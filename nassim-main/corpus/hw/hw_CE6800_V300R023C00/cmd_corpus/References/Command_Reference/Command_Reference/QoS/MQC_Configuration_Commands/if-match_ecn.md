if-match ecn
============

if-match ecn

Function
--------



The **if-match ecn** command configures a matching rule based on the ECN flag of packets in a traffic classifier.

The **undo if-match ecn** command deletes a matching rule based on the ECN flag of packets in a traffic classifier.



By default, a matching rule based on the ECN flag of packets is not configured in a traffic classifier.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match ecn** *ecn-value*

**undo if-match ecn** [ *ecn-value* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match ipv6 ecn** *ecn-value*

**undo if-match ipv6 ecn** [ *ecn-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ecn-value* | Specifies the ECN flag of packets. | The value is an integer ranging from 0 to 3. |
| **ipv6** | Create a matching rule based on the ECN flag of IPv6 packets in a traffic classifier.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match ecn** command to classify packets based on the ECN flag of packets. This ensures that the device processes packets matching the same traffic classifier identically.

**Precautions**

* If you run the **if-match ecn** command in the same traffic classifier view multiple times, only the latest configuration takes effect.
* The if-match ecn and if-match ip-precedence commands cannot be configured in the same traffic classifier in which the logical relationship is AND.
* The if-match ecn and **if-match ipv6 ecn** commands cannot be used together.

Example
-------

# Configure a matching rule based on the ECN flag of 3 in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match ecn 3

```