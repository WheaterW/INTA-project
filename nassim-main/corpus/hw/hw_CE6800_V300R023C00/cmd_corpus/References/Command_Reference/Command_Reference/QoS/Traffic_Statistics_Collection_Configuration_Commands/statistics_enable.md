statistics enable
=================

statistics enable

Function
--------



The **statistics enable** command enables the statistics function in a traffic behavior.

The **undo statistics enable** command disables the statistics function in a traffic behavior.



By default, the statistics function in a traffic behavior is disabled.


Format
------

**statistics enable** [ **history-record** **interval** *interval-value* ]

**undo statistics enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **history-record** | The history record of statistics. | - |
| **interval** *interval-value* | The interval time of statistics in minutes. | The value is an integer in the range from 1 to 60, |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To view the statistics on a traffic policy, you can use the statistics enabled command to enable the statistics function. After the statistics function is enabled, you can use the **display traffic-policy statistics** command to view the statistics.

**Follow-up Procedure**

Run the **traffic policy** command to create a traffic policy and run the **classifier behavior** command in the traffic policy view to bind the traffic classifier to the traffic behavior containing the traffic statistics collection function.

**Precautions**

The car or deny action cannot be configured together with history statistics in the same traffic behavior.


Example
-------

# Enable the history statistics function.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior test
[*HUAWEI-behavior-test] statistics enable history-record interval 1

```

# Enable the statistics function.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior test
[*HUAWEI-behavior-test] statistics enable

```