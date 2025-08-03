collect diagnostic information(user view)
=========================================

collect diagnostic information(user view)

Function
--------



The **collect diagnostic information** command collects the system log information.




Format
------

**collect diagnostic information** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to save the system log information to the current log directory.When a fault occurs in the system, you can run this command and locate the fault based on the saved log information.

**Precautions**



If another user is collecting the information at the same time, the current user needs to try again later. Logs whose file name length exceeds 64 characters are not collected. If the diagnostic\_information directory exists in the user operation directory, the diagnostic\_information directory will be deleted after this command is executed.




Example
-------

# Collect the system log information of a specified slot.
```
<HUAWEI> collect diagnostic information slot 1

```

# Collect the system log information of all slots.
```
<HUAWEI> collect diagnostic information

```