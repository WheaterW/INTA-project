snmp-agent notification-log
===========================

snmp-agent notification-log

Function
--------



The **snmp-agent notification-log enable** command enables the alarm logging function.

The **undo snmp-agent notification-log enable** command disables the alarm logging function.



By default, the SNMP agent function is disabled.


Format
------

**snmp-agent notification-log** { **enable** | { **global-ageout** *ageout* [ **minute** *minute* ] | **global-limit** *limit* } \* }

**undo snmp-agent notification-log** { **enable** | { **global-ageout** | **global-limit** } \* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **global-ageout** *ageout* | Specifies the aging time of alarm logs in hours.. | The value is 0, 12 to 36, in hours. By default, the value is 24. Value 0 indicates alarm logs do not age. |
| **minute** *minute* | Specifies the aging time of alarm logs in minutes. | The value is 1 to 59, in minutes. |
| **global-limit** *limit* | Specifies the maximum number of alarm logs allowed to be cached in the log buffer. | The value ranges from 1 to 15000. The default value is 500. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If notification logs in the log buffer do not need to be aged, set the aging time of these notification logs to 0.If the number of notification logs saved to the log buffer within the aging time exceeds the upper limit, new notification logs can still be saved but overwrites the earlier logs in the log buffer.To enable the alarm logging function, run the snmp-agent notification-log enable command.An alarm can be propagated using either of the following types of messages:

* Inform message
* Trap messageOnly the alarms propagated using Inform messages are to be logged. The alarms propagated using trap messages are not logged.The alarms propagated using Inform messages are logged only when the following conditions are met:
* No Inform ACK message is returned when the maximum number of attempts to resend the Inform message in the alarm queue reaches the configured threshold.
* An Inform message is discarded as the number of logged Inform messages reaches the maximum that the alarm queue supports.

**Configuration Impact**

If the size of the log buffer is excessively large, more network resources are consumed. In this case, reduce the size of the log buffer.NOTE:Only Inform logs are saved to the log buffer, and trap logs are not saved to the log buffer.


Example
-------

# Set the aging time of alarm logs to 36 hours.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent notification-log global-ageout 36

```

# Set the maximum number of alarm logs to be cached in the log buffer to 1000.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent notification-log global-limit 1000

```

# Enable the alarm logging function.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent notification-log enable

```