auto-source-trace statistics interval
=====================================

auto-source-trace statistics interval

Function
--------



The **auto-source-trace statistics interval** command sets the packet sampling interval for proactive source tracing.

The **undo auto-source-trace statistics interval** command restores the default packet sampling interval.



By default, the packet sampling interval is 10 seconds.


Format
------

**auto-source-trace statistics interval** *interval-value*

**undo auto-source-trace statistics interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-value* | Specifies the packet sampling interval for proactive source tracing. | The value is an integer that ranges from 10 to 60, in seconds. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **auto-source-trace statistics interval** command to set a proper packet sampling interval based on your site requirements.

**Prerequisites**

The **auto-source-trace enable** command has been run to enable the proactive source tracing function.


Example
-------

# In the attack defense policy named test, set the packet sampling interval for proactive source tracing to 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-source-trace enable
[*HUAWEI-cpu-defend-policy-test] auto-source-trace statistics interval 30

```