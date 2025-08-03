abort trial
===========

abort trial

Function
--------



The **abort trial** command disables the trial running of a configuration.




Format
------

**abort trial** [ { **session** *session-id* | **persist** *persistId* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **session** *session-id* | Specifies the ID of a session for which the trial running of the configuration is to be disabled. | The value is an integer ranging from 0 to 65535. |
| **persist** *persistId* | Specifies a persistence ID for a configuration trial run. | The value is a string of 1 to 256 case-sensitive characters. It can be any visible ASCII characters excluding spaces. If double quotation marks are used around the tag name, spaces are allowed in the tag name. The value cannot start with a digit and cannot be a hyphen (-). |



Views
-----

All views except the user view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In two-phase validation mode, you can run the **commit trial** command to enable configuration trial run after a configuration command is configured. You can also specify the time parameter in the **commit trial** command to set the timeout period of the trial run. After the trial run times out, the system configuration is automatically rolled back to the state before the trial run. Before the trial run times out, you can run the **abort trial** command to stop the trial run and roll back the system configuration to the state before the trial run. You can also specify the session parameter in the **abort trial** command to specify a session to end the trial run initiated by the session. You can specify the persistId parameter to end the persistent configuration trial run.

**Prerequisites**

The **commit trial** command has been run for a configuration.

**Configuration Impact**



After the trial running of the configuration is disabled, the system configuration rolls back to the configuration state before the trial running.



**Precautions**



The **abort trial** command must be run in the two-phase configuration validation mode.




Example
-------

# Disable the persistent configuration trial run.
```
<HUAWEI> system-view
[~HUAWEI] sysname hello
[*HUAWEI] commit trial persist abcid
Info: The system enters the trial configuration mode.
The system will revert to previous configuration if the trial configuration is not confirmed in 600 seconds.
[~hello] abort trial persist abcid
Warning: The trial configuration will be rolled back. Continue? [Y/N]:Y
Info: The trial configuration rollback succeeded.
[~HUAWEI]

```

# Disable the trial run of a specified session.
```
<HUAWEI> system-view
[~HUAWEI] sysname hello
[*HUAWEI] commit trial
Info: The system enters the trial configuration mode.
The system will revert to previous configuration if the trial configuration is not confirmed in 600 seconds.
[~hello] abort trial session ?
  392  Session in trial configuration mode

[~hello] abort trial session 392
Warning: The trial configuration will be rolled back. Continue? [Y/N]:Y
Info: The trial configuration rollback succeeded.
[~HUAWEI]

```

# Disable the trial running of a configuration.
```
<HUAWEI> system-view
[~HUAWEI] sysname rollback
[*HUAWEI] commit trial 120
Committing..done. 
Info: The system enters the trial configuration mode.
The system will revert to previous configuration if the trial configuration is not confirmed in 120 seconds.
[*rollback] abort trial
Warning: The trial configuration will be rolled back. Continue? [Y/N]:y

```