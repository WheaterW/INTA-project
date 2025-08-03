auto-defend alarm enable
========================

auto-defend alarm enable

Function
--------



The **auto-defend alarm enable** command enables the event reporting function for attack source tracing.

The **undo auto-defend alarm enable** command disables the event reporting function for attack source tracing.



By default, the event reporting function for attack source tracing is disabled.


Format
------

**auto-defend alarm enable**

**undo auto-defend alarm enable**


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

When the number of packets of a specified protocol from an attack source exceeds the threshold in a specified period, the device reports an event to the administrator so that the administrator can take measures to protect the device.

**Prerequisites**

Attack source tracing has been enabled using the **auto-defend enable** command.

**Follow-up Procedure**

Run the **auto-defend alarm threshold** command to set the event reporting threshold for attack source tracing.


Example
-------

# Enable the event reporting function for attack source tracing in the attack defense policy named test.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-defend enable
[*HUAWEI-cpu-defend-policy-test] auto-defend alarm enable

```