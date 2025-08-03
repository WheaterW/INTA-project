delay-suppression enable
========================

delay-suppression enable

Function
--------



The **delay-suppression enable** command enables alarm suppression on the Router.

The **undo delay-suppression enable** command disables alarm suppression on the Router.



By default, alarm suppression is enabled.


Format
------

**delay-suppression enable**

**undo delay-suppression enable**


Parameters
----------

None

Views
-----

Alarm management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can configure a suppression period for reporting an alarm or clearing an alarm. An alarm is reported if the relevant fault persists after the suppression period expires; a clear alarm is reported if the relevant fault is rectified during the suppression period.Alarm suppression is used to suppress the managed nodes that generate repeated alarms, service intermittence alarms, and persistent alarms so as to prevent a large number of invalid alarms.

**Configuration Impact**

If this function is disabled, the following symptoms may occur:

* Alarms that last for a very short time are also presented to users.
* Alarms that last for a short time are frequently generated.

**Precautions**



You can set the value of cause-period to 0 in the **suppression alarm cause-period** command for an alarm that you are concerned about. This alarm is not suppressed even if alarm suppression is enabled.




Example
-------

# Enable alarm suppression.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] delay-suppression enable

```