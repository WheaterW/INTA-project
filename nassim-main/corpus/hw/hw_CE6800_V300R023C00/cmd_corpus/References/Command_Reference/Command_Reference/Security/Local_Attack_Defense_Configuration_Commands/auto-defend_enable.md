auto-defend enable
==================

auto-defend enable

Function
--------



The **auto-defend enable** command enables automatic attack source tracing.

The **undo auto-defend enable** command disables automatic attack source tracing.



By default, attack source tracing is enabled.


Format
------

**auto-defend enable**

**undo auto-defend enable**


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

A large number of attack packets may attack the device CPU. Attack source tracing enables the device to check attack packets sent to the CPU, trace attack sources, and send logs or alarms to notify the administrator. By default, logs are sent to notify the administrator if attack source tracing is enabled.

**Follow-up Procedure**

After automatic attack source tracing is enabled, the device can trace the source of packets of a specified type sent to the CPU. To configure the packet type, run the **auto-defend protocol** command.

**Precautions**

* Attack source tracing configured in an attack defense policy takes effect only when the attack defense policy is applied in the system view.
* After the attack source tracing function for ICMP packets is enabled on the device, the fast ICMP reply function does not take effect.


Example
-------

# Enable attack source tracing in the attack defense policy named test.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-defend enable

```