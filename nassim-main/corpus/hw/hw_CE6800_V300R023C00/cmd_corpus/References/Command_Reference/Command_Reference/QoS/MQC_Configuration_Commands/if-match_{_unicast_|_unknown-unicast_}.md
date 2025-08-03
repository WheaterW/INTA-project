if-match { unicast | unknown-unicast }
======================================

if-match { unicast | unknown-unicast }

Function
--------



The **if-match unicast** command configures a matching rule for Layer 2 known unicast packets in a traffic classifier.

The undo if-match unknown-unicast command deletes a matching rule for Layer 2 known unicast packets in a traffic classifier.

The **if-match unknown-unicast** command configures a matching rule for Layer 2 unknown unicast packets in a traffic classifier.

The **undo if-match unknown-unicast** command deletes a matching rule for Layer 2 unknown unicast packets in a traffic classifier.



By default, a matching rule for Layer 2 known unicast packets is not configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match** { **unicast** | **unknown-unicast** }

**undo if-match** { **unicast** | **unknown-unicast** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unicast** | Matches unicast packets. | - |
| **unknown-unicast** | Specify unknown-unicast packets to match. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the if-match { unicast | unknown-unicast } command to configure a matching rule for Layer 2 known or unknown unicast packets so that the device processes Layer 2 known or unknown unicast packets matching the same traffic classifier in the same manner.

**Precautions**

A traffic policy containing this matching rule cannot be applied to the outbound direction.


Example
-------

# Configure a matching rule for Layer 2 known unicast packets in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match unicast

```