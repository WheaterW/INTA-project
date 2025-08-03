if-match dscp
=============

if-match dscp

Function
--------



The **if-match dscp** command configures a matching rule based on the Differentiated Services Code Point (DSCP) priority of packets in a traffic classifier.

The **undo if-match dscp** command deletes a matching rule based on the DSCP priority of packets in a traffic classifier.



By default, a matching rule based on the DSCP priority of packets is not configured in a traffic classifier.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match dscp** *dscp-value* &<1-8>

**undo if-match dscp** [ *dscp-value* &<1-8> ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match ipv6 dscp** *dscp-value* &<1-8>

**undo if-match ipv6 dscp** [ *dscp-value* &<1-8> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dscp** *dscp-value* | Specifies the DSCP priority. | The value can be a DiffServ code, an integer ranging from 0 to 63, or the name of the DSCP service type such as af11, af12, af13, af21, af22, af23, af31, af32, af33, af41, af42, af43, cs1-cs7, default, and ef.  The values corresponding to service types are as follows:   * af11: 10 * af12: 12 * af13: 14 * af21: 18 * af22: 20 * af23: 22 * af31: 26 * af32: 28 * af33: 30 * af41: 34 * af42: 36 * af43: 38 * cs1: 8 * cs2: 16 * cs3: 24 * cs4: 32 * cs5: 40 * cs6: 48 * cs7: 56 * default: 0 * ef: 46 |
| **ipv6** | Indicates that IPv6 packets are matched. If this parameter is not specified, IPv4 packets are matched.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match dscp** command to classify packets based on the DSCP priority of packets so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

* If you enter multiple DSCP priorities in the command, a packet matches a rule as long as it matches one of the DSCP priorities, regardless of whether the relationship between traffic classification rules is AND or OR.
* In a traffic classifier where the relationship between rules is AND, the if-match dscp and if-match ip-precedence commands cannot be used simultaneously.
* If you run the **if-match dscp** command in the same traffic classifier view multiple times, only the latest configuration takes effect.
* if-match ipv6 dscp and if-match dscp cannot be configured in one traffic classifier.


Example
-------

# Match the packets with the DSCP value being 1 with the traffic classifier class1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match dscp 1

```