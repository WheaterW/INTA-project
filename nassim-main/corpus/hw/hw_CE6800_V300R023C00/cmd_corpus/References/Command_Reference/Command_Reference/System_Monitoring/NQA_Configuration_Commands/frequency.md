frequency
=========

frequency

Function
--------



The **frequency** command sets the interval at which an NQA test instance is automatically performed.

The **undo frequency** command restores the default interval.



By default, no interval is set. An NQA test instance is performed once.


Format
------

**frequency** *frequencyValue*

**undo frequency**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *frequencyValue* | Specifies the interval at which an NQA test instance is performed. | The value is an integer ranging from 1 to 604800, in seconds. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **start** command sets the start time and end time for an NQA test instance. If a test instance needs to be performed periodically during the interval between the start time and end time, run the **frequency** command to set the interval at which the NQA test instance is performed automatically.If no end time is set, the test will not stop automatically. You need to stop it manually.For example, if the start daily 12:00:00 to 13:00:00 begin 2009/10/19 end 2010/10/20 command is run to configure an ICMP test instance to run once between 12:00 to 13:00 each day, and thefrequency 1200 command is run to set the interval to 1200 seconds, the start time of the ICMP test instance can be:

* 12:00, at which the ICMP test is automatically performed for the first time
* 12:20, at which the ICMP test is automatically performed for the second time
* 12:40, at which the ICMP test is automatically performed for the third time
* 13:00, at which the ICMP test is automatically performed for the fourth timeIf the interval at which an NQA test instance is automatically performed is set, you do not need to perform the NQA test instance manually.

**Configuration Impact**

If an active/standby switchover is performed on the NQA client before the test instance is complete, any of the following situations may occur:

* If the interval at which a test instance is automatically performed is not set, the test instance stops after the active/standby switchover is complete.
* If the interval at which a test instance is automatically performed is set, the test instance will be performed from the next period after the active/standby switchover is complete.

**Precautions**

The interval at which the test is automatically performed must be greater than the test timeout period set by using the **timeout** command. Otherwise, packets time out.If you change the test period during the running of a test instance, the system prompts you whether to stop the test instance. Press "Y" or "N" as required.

* If you enter Y, the current test instance is stopped and parameters are modified. After you submit the modification, the modified parameters take effect. To restart the test instance, run the **start** command.
* If you enter N, the parameter modification fails and the current test instance continues to run.If the value of frequency is smaller than (Number of sent packets â 1) x interval + timeout + 1, the test result may be no result. For a test instance that supports jitter-packetnum, the number of sent packets is probe-count x jitter-packetnum.

Example
-------

# Set the interval at which the test instance named user test is automatically performed to 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] frequency 20

```