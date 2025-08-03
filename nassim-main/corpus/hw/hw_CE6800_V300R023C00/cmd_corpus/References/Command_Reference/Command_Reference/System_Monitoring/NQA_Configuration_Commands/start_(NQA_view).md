start (NQA view)
================

start (NQA view)

Function
--------



The **start** command sets the start mode and end mode for an NQA test instance.

The **undo start** command stops the running NQA test instance. If the start at or start delay command is run but does not take effect, running the undo start command will delete the previous configuration. The undo start command functions the same as the stop command.



By default, the test stops automatically after test packets are sent.


Format
------

**start now**

**start now end at** [ *end-yyyy/mm/dd* ] *end-hh:mm:ss*

**start now end delay** { **seconds** *end-second* | *delay-hh:mm:ss* }

**start now end lifetime** { **seconds** *end-second* | *life-hh:mm:ss* }

**start at** [ *start-yyyy/mm/dd* ] *hh:mm:ss*

**start at** [ *start-yyyy/mm/dd* ] *hh:mm:ss* **end** **at** [ *end-yyyy/mm/dd* ] *end-hh:mm:ss*

**start at** [ *start-yyyy/mm/dd* ] *hh:mm:ss* **end** **delay** { **seconds** *end-second* | *delay-hh:mm:ss* }

**start at** [ *start-yyyy/mm/dd* ] *hh:mm:ss* **end** **lifetime** { **seconds** *end-second* | *life-hh:mm:ss* }

**start delay** { **seconds** *pause-second* | *pause-hh:mm:ss* }

**start delay** { **seconds** *pause-second* | *pause-hh:mm:ss* } **end** **at** [ *end-yyyy/mm/dd* ] *end-hh:mm:ss*

**start delay** { **seconds** *pause-second* | *pause-hh:mm:ss* } **end** **delay** { **seconds** *end-second* | *delay-hh:mm:ss* }

**start delay** { **seconds** *pause-second* | *pause-hh:mm:ss* } **end** **lifetime** { **seconds** *end-second* | *life-hh:mm:ss* }

**start daily** *hh:mm:ss* **to** *end-hh:mm:ss* [ **begin** { *start-yyyy/mm/dd* | *start-old-yyyy/mm/dd* } ] [ **end** { *end-yyyy/mm/dd* | *end-old-yyyy/mm/dd* } ]

**undo start**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **now** | Performs the test immediately. | - |
| **end** | End a test. | - |
| **at** | Start or end test at a time. | - |
| **delay** | Start or end delay time. | - |
| **seconds** *end-second* | The life time or delay time, in seconds. | The value is an integer ranging from 6 to 86399. |
| **lifetime** | Set the test lifetime. | - |
| *start-yyyy/mm/dd* | The date of test start or test end. | yyyy specifies the yea, which is an integer ranging from 1970 to 9999. mm specifies the month, which is an integer ranging from 1 to 12. dd specifies the day, which is an integer ranging from 1 to 31. |
| *hh:mm:ss* | Set the test start time, test end time, life time or delay time. | hh specifies the hour, which is an integer ranging from 0 to 23. mm specifies the minute, which is an integer ranging from 0 to 59. ss specifies the second, which is an integer ranging from 0 to 59. |
| **daily** | Start test daily. | - |
| **to** | Indicates a value range. | - |
| **begin** | Begin a test. | - |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the start mode and end mode for an NQA test instance, run the **start** command.The application scenarios are as follows:

* The test instance is executed at the specified time and ends at the specified time. Run the start at yyyy/mm/dd hh:mm:ss end at yyyy/mm/dd hh:mm:**ss** command.
* The test instance is executed at the specified time and ends after the specified number of seconds. Run the start at yyyy/mm/dd hh:mm:**ss lifetime seconds second** command.
* The test instance is executed after the specified number of seconds and ends at the specified time. Run the start delay seconds second end at yyyy/mm/dd hh:mm:**ss** command.
* The test instance is executed immediately and ends after the specified number of seconds. Run the **start now end lifetime seconds second** command.
* The test instance is executed at the specified time every day and ends at the specified time. Run the start daily hh:mm:ss to hh:mm:**ss** command.Select a proper method for starting a test instance based on service requirements.

**Configuration Impact**



If the **start daily** command is run more than once, the latest configuration overrides the previous one.



**Precautions**

If the number of running test instances reaches the maximum number allowed by the system, the **start** command fails.For the same test instance, the **start now** command can be run again only after the previous test is complete.If a large number of test instances are running in a non-periodic test, wait for a while before starting new test instances.


Example
-------

# Start the test instance 10 hours later.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] destination-address ipv4 10.1.1.1
[*HUAWEI-nqa-user-test] start delay 10:00:00

```

# Start the test instance at 12:12:12.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] destination-address ipv4 10.1.1.1
[*HUAWEI-nqa-user-test] start at 2009/10/19 12:12:12

```

# Start the current test instance immediately.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] destination-address ipv4 10.1.1.1
[*HUAWEI-nqa-user-test] start now

```

# Start the test instance at a fixed time every day.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] destination-address ipv4 10.1.1.1
[*HUAWEI-nqa-user-test] start daily 12:00:00 to 13:00:00 begin 2009/10/19 end 2010/10/20

```