info-center log-severity
========================

info-center log-severity

Function
--------



The **info-center log-severity** command sets the severity of log messages.

The **undo info-center log-severity** command restores the default severity of log messages.



By default, the log buffer records log messages of levels 0 through 4.


Format
------

**info-center log-severity bymodule-alias** *module-name* *logname* **severity** *log-level*

**undo info-center log-severity bymodule-alias** *module-name* *logname* **severity**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *logname* | Specifies a log name. | The value is a string of 1 to 63 case-insensitive characters, spaces not supported. |
| **severity** *log-level* | Specifies the severity string of log messages. | The value is of the enumerated type.   * emergencies: mapped to 0. An error of the urgency level occurs. * alert: mapped to 1. An error needs to be corrected immediately. * critical: mapped to 2. A serious error occurs. * error: mapped to 3. An error occurs. * warning: mapped to 4. An error may occur. * notification: mapped to 5. An event to be noticed occurs. * informational mapped to 6. An event occurs, and no action is required. * debugging: mapped to 7. Debugging information is displayed. |
| **bymodule-alias** *module-name* | Specifies the name of a module that generates log messages. | The value is a string of 1 to 63 case-insensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The log buffer records log messages of levels 0 through 4 by default. You can run theinfo-center log-severity command to set the log severity as needed:

* Set the severity of log messages to a value ranging 5 through 7 so that the log buffer does not record these log messages.
* Set the severity of log messages to a value ranging 0 through 4 so that the log buffer records these log messages.


Example
-------

# Set the severity of CLI operation logs to error.
```
<HUAWEI> system-view
[~HUAWEI] info-center log-severity bymodule-alias cli cmdrecord severity error

```