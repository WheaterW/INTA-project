agetime
=======

agetime

Function
--------



The **agetime** command sets the aging time of an NQA test.

The **undo agetime** command restores the default aging time.



By default, the aging time of an NQA test is 0, indicating that the test is not aged.


Format
------

**agetime** *ageTimeValue*

**undo agetime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ageTimeValue* | Specifies the aging time of an NQA test. | The value is in the format of HH:MM:SS. HH specifies an hour that ranges from 0 to 23; MM specifies a minute that ranges from 0 to 59; SS specifies a second that ranges from 0 to 59. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent endless running of a test instance, age the test instance periodically. The **agetime** command can be used to set the aging time to change the survival time of a test instance in the system.

* The aging time is started when the NQA test instance is in the inactive state. When the aging time expires, the system deletes the NQA test instance automatically.
* The aging time is reset when the NQA test instance is in the active state.

**Prerequisites**



The type of an NQA test instance has been specified using the **test-type** command.



**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the aging time of the NQA test named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] agetime 1:0:0

```