if-match discard
================

if-match discard

Function
--------



The **if-match discard** command configures a matching rule based on drop packets in a traffic classifier.

The **undo if-match discard** command deletes a matching rule based on drop packets in a traffic classifier.



By default, a matching rule based on drop packets is not configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match discard**

**undo if-match discard**


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

**Usage Scenario**

After packets reach the device, invalid packets are discarded. You can run the if-match discard command to configure the device to match discarded packets, take action for the discarded packets such as traffic statistics and mirroring, and analyze them.

**Precautions**

* The packets that match the ACL rule cannot match the traffic policy that contains the traffic classifier.
* A traffic policy containing a traffic classifier that defines if-match cannot be applied in the outbound direction.


Example
-------

# Configure a matching rule based on discarded packets in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match discard

```