qos ecn enable
==============

qos ecn enable

Function
--------



The **qos ecn enable** command enables the global ECN.

The **undo qos ecn enable** command restores the default settings.



By default, the global explicit congestion advertisement function ECN is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**qos ecn enable**

**undo qos ecn enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the downstream and upstream devices support ECN, the downstream device identifies and marks the network congestion based on the ECN field in the packets. The downstream device notifies the upstream device of the detected network congestion. Upon receiving the notification, the upstream device lowers the rate of sending packets to avoid worsening congestion.


Example
-------

# Enable Global ECN.
```
<HUAWEI> system-view
[~HUAWEI] qos ecn enable

```