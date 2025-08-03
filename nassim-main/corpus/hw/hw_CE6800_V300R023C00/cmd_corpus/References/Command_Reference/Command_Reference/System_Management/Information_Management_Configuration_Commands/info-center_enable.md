info-center enable
==================

info-center enable

Function
--------



The **info-center enable** command enables information management, which allows information to be output to a remote terminal or server.

The **undo info-center enable** command disables information management.



Information management is enabled by default.


Format
------

**info-center enable**

**undo info-center enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The system logs the running status of a device in real time. After information management is enabled using the **info-center enable** command, logs can be output to a remote terminal or syslog server and stored to provide a reference for network administrators to monitor the device running status or diagnose network faults.

**Configuration Impact**



After you run the **info-center enable** command to enable information management, logs generated on the device can be output through the configured channel to the specified remote terminal or server.Logs generated after the information management function is disabled using the **undo info-center enable** command will not be sent to a terminal or remote server.Logs recording the execution of the **info-center enable** command will be sent to a terminal or remote server by default.



**Follow-up Procedure**

After enabling information management, configure rules for outputting logs to a remote terminal or server.

**Precautions**

After the **undo info-center enable** command is run to disable information management, the fault management component does not send any alarm information (such as traps, notifications, and alarm indicators) to terminals, remote servers, or subscribers. Active and historical alarms generated on the device are recorded only in alarm logs.


Example
-------

# Enable information management.
```
<HUAWEI> system-view
[~HUAWEI] info-center enable

```