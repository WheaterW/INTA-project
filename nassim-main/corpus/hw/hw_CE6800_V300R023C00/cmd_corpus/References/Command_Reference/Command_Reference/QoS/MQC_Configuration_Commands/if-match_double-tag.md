if-match double-tag
===================

if-match double-tag

Function
--------



The **if-match double-tag** command configures a matching rule based on double tags of packets in a traffic classifier.

The **undo if-match double-tag** command deletes a matching rule based on double tags of packets in a traffic classifier.



By default, a matching rule based on double tags of packets is not configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match double-tag**

**undo if-match double-tag**


Parameters
----------

None

Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the if-match double-tag command to classify traffic based on double tags so that the device processes packets matching the same traffic classifier in the same manner.If you run this command multiple times in the same traffic classifier view, the latest configuration takes effect.


Example
-------

# Configure a matching rule based on double tags of packets in the traffic classifier class1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match double-tag

```