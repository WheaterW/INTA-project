ops run python
==============

ops run python

Function
--------



The **ops run python** command executes a script.

The **ops stop process** command stops a running OPS process.




Format
------

**ops run python** *script-name* [ *arguments* ]

**ops stop process** *process-id*

**ops run python background** *script-name* [ *arguments* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *script-name* | Specifies the name of a script. | The value is a string of 1 to 127 characters. |
| *arguments* | Specifies the script parameter, which is parsed by the script. | The value is a string of 1 to 383 characters. |
| *process-id* | Process ID. | IDs are automatically allocated by the system. You can run the display ops process state command to query the process ID. |
| **background** | Executes the script in the background. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To execute a script, run the **ops run python** command. A maximum of 10 scripts can be concurrently executed. Scripts can be executed in the foreground or background in the OPS.

* When scripts are executed in the foreground, users can view the script execution output and interoperate with scripts. In addition, users can press Ctrl+C to end the script execution, but scripts may keep being executed if codes do not cover the Ctrl+C operation.User input is transparently transmitted to scripts, and the OPS does not proactively perform timeout tests.If a script is executed in the foreground and a user closes the window, the script execution will be ended.
* When scripts are executed in the background, users cannot view the script execution output. Users receive only a null character string in any interaction operation.To stop a running process, run the **ops stop process** command.

**Prerequisites**

A script has been installed on the device.

* The Python script has been uploaded to the device.
* The **ops install file** command is run in the system view to install the script.The **display ops process current** command has been run to query the process ID.

**Configuration Impact**

If a script contains configuration delivering operations, the system configuration will be affected.After a process is stopped, subsequent operations are no longer performed, and all resources applied for this process will be released.

**Follow-up Procedure**

Run the **display ops process history** command to view information about the stopped process. Information shows that a user cancels this process.

**Precautions**

The **ops stop process** command is potentially service-affecting. The running process will be stopped suddenly. Therefore, exercise caution when running this command.When a command is executed, a log is recorded. When running the **ops run python** command with arguments specified, do not carry sensitive information (such as user passwords). This prevents security risks caused by log leakage. If sensitive information needs to be carried, you are advised to write it into another python script as a parameter of the cli.execute interface of the ops module and run the ops run python <script-name> command to execute the script.


Example
-------

# Stop a running script with the process ID 2002.
```
<HUAWEI> ops stop process 2002
Warning: This operation maybe lost some data, are you sure stop the process? [Y/N]Y

```

# Execute the script config.py with the parameter "1 2 3".
```
<HUAWEI> ops run python config.py "1 2 3"

```