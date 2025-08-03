auto-source-trace sample
========================

auto-source-trace sample

Function
--------



The **auto-source-trace sample** command sets the packet sampling ratio for proactive source tracing.

The **undo auto-source-trace sample** command restores the default packet sampling ratio.



By default, the packet sampling ratio is 16. That is, one packet is sampled in every 16 packets.


Format
------

**auto-source-trace sample** *sample-value*

**undo auto-source-trace sample**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sample-value* | Specifies the packet sampling ratio for proactive source tracing. | The options are as follows:   * 8 * 16 * 32 * 64   The default value is 16. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **auto-source-trace sample** command to set the packet sampling ratio. A smaller sampling ratio makes the proactive source tracing result more accurate, but increases the CPU usage. You can set a proper packet sampling ratio based on the requirements on the precision of proactive source tracing and the current CPU usage.

**Prerequisites**

The **auto-source-trace enable** command has been run to enable the proactive source tracing function.


Example
-------

# In the attack defense policy named test, set the packet sampling ratio for proactive source tracing to 32.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-source-trace enable
[*HUAWEI-cpu-defend-policy-test] auto-source-trace sample 32

```