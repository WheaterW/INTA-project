trace enable
============

trace enable

Function
--------



The **trace enable** command enables service diagnosis.

The **undo trace enable** command disables service diagnosis.



By default, service diagnosis is disabled.


Format
------

**trace enable** [ **brief** ]

**undo trace enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **brief** | Configures the device to output brief service diagnosis information. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

It is difficult to locate problems during user access based on debugging information on existing networks because multiple users may get online or offline simultaneously and debugging information about a specified user cannot be displayed. Service diagnosis allows maintenance personnel to customize attributes and create diagnosis objects to diagnose information about services of specified users. To enable service diagnosis, run the **trace enable** command.Service diagnosis information can be displayed in two methods:The **trace enable brief** command configures the device to output brief service diagnosis information.The **trace enable** command configures the device to output detailed service diagnosis information.

**Follow-up Procedure**

After the service diagnosis function is enabled, run the **trace object** command to create a diagnosis object. After a diagnosis object is successfully created and an ID is generated for the object, the system diagnoses specific services.After the trace function is enabled, if you want to display trace information on the device interface (that is, the output mode is command-line, corresponding to the trace object output command-line command), you need to enable the debugging function and set the timeout period for disabling the debugging function for service diagnosis to take effect. The corresponding configuration is as follows:terminal monitorterminal debuggingdebugging timeout value

**Precautions**

Service diagnosis affects system performance. Therefore, enable service diagnosis only when fault locating is required. After locating faults, immediately run the **undo trace enable** command to disable service diagnosis.The **trace enable** command is not recorded in the configuration file. Therefore, run the **trace enable** command again after the device restarts to make service diagnosis take effect.When service diagnostic information is output to the CLI by default, you need to run the **trace enable** command again if you open a different VTY window.


Example
-------

# Enable the service diagnosis function and configure the device to output brief service diagnosis information.
```
<HUAWEI> system-view
[~HUAWEI] trace enable brief

```