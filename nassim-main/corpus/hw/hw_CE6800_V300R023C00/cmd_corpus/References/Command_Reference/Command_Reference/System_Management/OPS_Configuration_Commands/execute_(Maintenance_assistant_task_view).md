execute (Maintenance assistant task view)
=========================================

execute (Maintenance assistant task view)

Function
--------



The **execute batch-file** command configures batch file execution for a maintenance assistant.

The **execute command** command configures command execution for a maintenance assistant.

The **execute python** command configures Python script execution for a maintenance assistant.

The **undo execute** command cancels the configuration.



By default, no task is configured for a maintenance assistant.


Format
------

**execute** *priority* **command** *command-string*

**execute** *priority* **batch-file** *file-name*

**execute** *priority* **python** *file-name* [ *arguments* ]

**undo execute** *priority*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the task priority. | The value is in the format of integer1[.integer2] to allow an n.5 to be inserted between n and n+1. For example, if a user has configured tasks with the priorities 2 and 3 and needs to perform a task between the tasks with the priorities 2 and 3, the user can set the priority of the new task to 2.5. |
| *command-string* | Specifies a command. | The value is a string of 1 to 511. |
| **batch-file** *file-name* | Specifies the name of a batch file. | The value is a string of 5 to 56 characters. The file name extension is .bat. |
| **python** *file-name* | Specifies a Python script. | The value is a string of 1 to 127 characters. |
| *arguments* | Specifies the parameter of the Python script. | The value is a string of 1 to 383 characters. |



Views
-----

Maintenance assistant task view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure a device to automatically run a large number of commands when a specific condition is met, users can enable batch file execution for a maintenance assistant in the OPS.After a maintenance assistant is created, the assistant must be configured with tasks. Each maintenance assistant can be configured with at most one batch file with the size not greater than 1 MB. The configuration modification in the script takes effect immediately and does not require committing.When users configure the execute command, the OPS checks whether the file name extension is .bat but does not verify the file contents.To configure a device to automatically run a large number of commands when a specific condition is met, users can enable batch file execution for a maintenance assistant in the OPS.

**Prerequisites**

The **assistant** command has been run in the system view to create a maintenance assistant.The **ops install file** command has been run to save the batch file in the $\_user directory.

**Precautions**

After a maintenance assistant is created, the assistant must be configured with tasks.For the **execute batch-file** command:

* When a file operation command is used in a batch file, the absolute path of the file must be specified.
* If a batch file contains configurations that take effect only after being committed, run the **commit** command in the batch file to commit the configurations. Otherwise, the configurations cannot take effect.
* During the configuration, the command checks the name of the batch file (the file name extension must be .bat) but does not check the correctness of the file content.
* After this command is run, the system automatically enters the machine-to-machine mode (Y is automatically entered for the interactive command). Intelligent command rollback is not supported. You need to run the **quit** command before switching the view.

For the **execute command** command:

* You can set the working mode to one-phase or two-phase. If the working mode is two-phase, you need to run the **commit** command in the batch script to commit the configuration. Otherwise, the configuration modification does not take effect.
* During the configuration, the command does not provide help information for the commands in the task.
* During the configuration, the system only checks whether a command matches the command keyword, but does not check the validity of specific parameters.
* After this command is run, the system automatically enters the machine-to-machine mode (Y is automatically entered for the interactive command). Intelligent command rollback is not supported. You need to run the **quit** command before switching the view.

For the **execute python** command:

* Each assistant task can be configured with only one script, and the size of the script file cannot exceed 1 MB.
* The configuration modification in the script takes effect immediately and does not need to be committed.
* The command checks the script name (the file name extension must be .py), but does not check the correctness of the file content.


Example
-------

# Configure a script file named policy.py.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant policy
[*HUAWEI-ops-assistant-policy] execute 3 python policy.py

```

# Configure the reboot command execution for a maintenance assistant.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant reboot
[*HUAWEI-ops-assistant-reboot] execute 1 command reboot

```

# Configure batch file execution for a maintenance assistant.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant task
[*HUAWEI-assistant-task] execute 2 batch-file batch.bat

```