backup application
==================

backup application

Function
--------



The **backup application** command backs up application data.




Format
------

**backup application** *application-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **application** *application-name* | Specifies the name of an application. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* This command is used to back up the application data on the device. Only the application started by running the **start** command can be backed up by running this command.
* After this command is executed, the applications that have been started on the device are stopped, backed up, and restarted. The applications that have not been started on the device are directly backed up.
* In a single main control board scenario, an error message is displayed when you run this command.


Example
-------

# Back up application data.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] backup application app1
Warning: The application will be stopped in backup progress. Continue? [Y/N]:y
Info: Operating, please wait for a moment...............done.
Info: Succeeded in backup the application.

```