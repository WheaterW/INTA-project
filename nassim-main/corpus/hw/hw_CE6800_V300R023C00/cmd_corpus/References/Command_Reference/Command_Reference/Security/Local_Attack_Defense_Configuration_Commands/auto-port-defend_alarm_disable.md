auto-port-defend alarm disable
==============================

auto-port-defend alarm disable

Function
--------



The **auto-port-defend alarm disable** command disables the report of port attack defense events.

The **undo auto-port-defend alarm disable** command enables the report of port attack defense events.



By default, the reporting of port attack defense events is enabled.


Format
------

**auto-port-defend alarm disable**

**undo auto-port-defend alarm disable**


Parameters
----------

None

Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a port undergoes a DoS attack, the malicious attack packets sent from this port to the CPU occupy bandwidth. As a result, the CPU cannot process the protocol packets sent from other ports, and services are interrupted. In this situation, you can enable the report of port attack defense events. When the rate of protocol packets on a port exceeds the check threshold, the switch reports an event to notify the network administrator, so that the administrator can promptly take measures to protect the switch.

**Follow-up Procedure**

If you run the **auto-port-defend protocol threshold** command multiple times in the same attack defense policy view, only the latest configuration takes effect.


Example
-------

# Enable the report of port attack defense events in the attack defense policy test.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] undo auto-port-defend alarm disable

```