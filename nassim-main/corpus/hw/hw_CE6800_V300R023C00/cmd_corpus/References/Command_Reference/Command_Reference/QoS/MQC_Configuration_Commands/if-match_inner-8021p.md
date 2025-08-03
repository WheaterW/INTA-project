if-match inner-8021p
====================

if-match inner-8021p

Function
--------



The **if-match inner-8021p** command configures a matching rule based on the 802.1p priority in the inner tag of QinQ packets in a traffic classifier.

The **undo if-match inner-8021p** command deletes a matching rule based on the 802.1p priority in the inner tag of QinQ packets in a traffic classifier.



By default, a matching rule based on the 802.1p priority in the inner tag of QinQ packets is not configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match inner-8021p** *inner-8021p-value* &<1-8>

**undo if-match inner-8021p**

**undo if-match inner-8021p** *inner-8021p-value* &<1-8>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *inner-8021p-value* | Specifies the inner 802.1p priority of QinQ packets. | The value is an integer that ranges from 0 to 7. A larger value indicates a higher priority. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match inner-8021p** command to classify packets based on the 802.1p priority in the inner tag of QinQ packets so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

* The **if-match inner-8021p** command is valid only for the double-tagged packets.
* If you enter multiple 802.1p priorities in the inner tags of packets in the command, a packet matches a rule as long as it matches one of the 802.1p priorities in the inner tags of packets, regardless of whether the relationship between traffic classification rules is AND or OR.
* If you run the **if-match inner-8021p** command in the same traffic classifier view multiple times, only the latest configuration takes effect.

Example
-------

# Configure a matching rule based on the inner 802.1p priority of 1 in QinQ packets in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1 type and
[*HUAWEI-traffic-classifier-c1] if-match inner-8021p 1

```