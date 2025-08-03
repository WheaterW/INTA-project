display ops process
===================

display ops process

Function
--------



The **display ops process** command displays information about an OPS process.




Format
------

**display ops process** *method*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *method* | The operation method. | * current: brief information about a specified OPS task that is being executed. * history: information about a historical OPS task. * verbose: detailed information about a specified OPS task that is being executed. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To view information about an OPS process, run the display ops process command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about the OPS process that is being executed.
```
<HUAWEI> display ops process current
--------------------------------------------------------------------------------
ID       ProcessName      State       Command
--------------------------------------------------------------------------------
3        270         running     policy.py 
--------------------------------------------------------------------------------

```

# Display history information about an OPS process.
```
<HUAWEI> display ops process history
Command           : policy.py 1 2 3
ID                : 1000
Owner type        : user
Owner name        : root
Background flag   : false
Trigger time      : 2020-3-28 09:40:01
Start time        : 2020-3-28 09:40:31
End time          : 2020-3-28 09:40:51
Result            : normal

```

# Display detailed information about the OPS process that is being executed.
```
<HUAWEI> display ops process verbose
Command           : policy.py 
ID                : 3
Owner type        : user
Owner name        : root123
Background flag   : true
Trigger time      : 2020-03-12 05:28:11
Start time        : 2020-03-12 05:28:11
State             : running

```

**Table 1** Description of the **display ops process** command output
| Item | Description |
| --- | --- |
| ID | OPS process ID. |
| ProcessName | OPS process Name. |
| State | Status of an OPS process:   * running: the process is being executed. * suspend: the process is stopped. * pending: the process has been activated but not executed. |
| Command | Name of a script. |
| Owner type | Process type:   * User. * Assistant. |
| Owner name | Name of an owner. |
| Background flag | Whether the process is executed in the background:   * false: the process is not executed in the background. * true: the process is executed in the background. |
| Trigger time | Time when a task is triggered. |
| Start time | Time when a task is started. |
| End time | Time when a task is ended. |
| Result | Result of a task:   * Normal: the task ends normally. * user cancel: a user cancels the process. |