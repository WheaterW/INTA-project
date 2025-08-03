auto-source-trace enable
========================

auto-source-trace enable

Function
--------



The **auto-source-trace enable** command enables proactive source tracing.

The **undo auto-source-trace enable** command disables proactive source tracing.



By default, proactive source tracing is enabled.


Format
------

**auto-source-trace enable**

**undo auto-source-trace enable**


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

When a device is attacked, you can enable proactive source tracing to collect statistics on attack packets within a specified period for attack locating and defense.


Example
-------

# Enable proactive source tracing in the attack defense policy view.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-source-trace enable

```