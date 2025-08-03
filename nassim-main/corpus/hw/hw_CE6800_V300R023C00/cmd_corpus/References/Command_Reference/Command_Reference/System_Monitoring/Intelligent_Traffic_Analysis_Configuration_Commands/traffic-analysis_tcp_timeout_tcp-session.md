traffic-analysis tcp timeout tcp-session
========================================

traffic-analysis tcp timeout tcp-session

Function
--------



The **traffic-analysis tcp timeout tcp-session** command enables the switch to age a TCP flow in intelligent traffic analysis based on the FIN or RST flag in the TCP packet header.

The **undo traffic-analysis tcp timeout tcp-session** command restores the default configuration.



By default, a TCP flow in intelligent traffic analysis is not aged out based on the FIN or RST flag in the TCP packet header.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-analysis tcp timeout tcp-session**

**undo traffic-analysis tcp timeout tcp-session**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The FIN or RST flag in a TCP packet indicates that the TCP connection is terminated. When receiving a TCP packet with the FIN or RST flag, the switch immediately ages the corresponding intelligent traffic analysis flow to save memory space. If this command is not run, TCP flows are aged out based on other aging modes, for example, inactive aging or active aging.

**Precautions**

If multiple aging modes are configured on the switch, a flow is aged out when it meets any aging condition.


Example
-------

# Configure the switch to age a TCP flow in intelligent traffic analysis based on the FIN or RST flag in the TCP packet header.
```
<HUAWEI> system-view
[~HUAWEI] traffic-analysis tcp timeout tcp-session

```