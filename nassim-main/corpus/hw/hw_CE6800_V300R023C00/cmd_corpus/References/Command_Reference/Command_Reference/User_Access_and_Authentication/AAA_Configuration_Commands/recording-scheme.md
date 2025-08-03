recording-scheme
================

recording-scheme

Function
--------

The **recording-scheme** command creates a recording scheme and displays the recording scheme view.

The **undo recording-scheme** command deletes a recording scheme.

By default, no recording scheme is configured on the device.



Format
------

**recording-scheme** *recording-scheme-name*

**undo recording-scheme** *recording-scheme-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *recording-scheme-name* | Specifies the name of a recording scheme. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or the following symbols: / \ : \* ? " < > |. The value cannot be - or --. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

After a recording scheme takes effect, you can view the records such as the executed commands, connection information, and system-level events on the recording server. The records help you locate network faults. Because a recording scheme needs to be associated with an HWTACACS server template, the recording scheme is configured only when HWTACACS authentication or authorization is performed.

Creating a recording template using the
**recording-scheme** command is mandatory for configuration.

**Follow-up Procedure**

After a recording scheme is created and associated with an HWTACACS server template, perform the following configurations in the AAA view:

* Run the **cmd recording-scheme** command to apply a policy in a recording scheme to record the commands executed on the device.
* Run the **outbound recording-scheme** command to apply a policy in a recording scheme to record the connection information.
* Run the **system recording-scheme** command to apply a policy in a recording scheme to record the system events.

**Precautions**

If the recording scheme to be configured does not exist, the **recording-scheme** command creates a recording scheme and displays the recording scheme view. If the recording scheme to be configured already exists, the **recording-scheme** command displays the recording scheme view.

Before deleting a recording scheme, ensure that the scheme has not been referenced by the cmd recording-scheme or outbound recording-scheme or
**system recording-scheme** command.

Example
-------

# Create a service scheme srvscheme1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[*HUAWEI-aaa] recording-scheme recscheme1
[*HUAWEI-aaa-recording-recscheme1]

```