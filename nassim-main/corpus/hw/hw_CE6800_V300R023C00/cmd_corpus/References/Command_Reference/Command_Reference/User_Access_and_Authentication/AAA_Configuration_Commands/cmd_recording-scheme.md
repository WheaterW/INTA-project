cmd recording-scheme
====================

cmd recording-scheme

Function
--------

The **cmd recording-scheme** command applies a policy in a recording scheme to record the commands executed on the device.

The **undo cmd recording-scheme** command deletes a policy from a recording scheme.

By default, the commands that are used on the device are not recorded.



Format
------

**cmd recording-scheme** *recording-scheme-name*

**undo cmd recording-scheme**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *recording-scheme-name* | Specifies the name of a recording scheme. | The recording scheme must already exist. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

During the device configuration, incorrect operations may result in network faults. After the **cmd recording-scheme** command is executed, you can view records of the commands executed on the device to locate the network faults.

**Prerequisites**

A recording scheme has been created by using the **recording-scheme** command and a recording mode has been configured by using the **recording-mode hwtacacs** command.



Example
-------

# Configure a policy in the recording scheme scheme0 to record the commands executed on the device.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template hw1
[*HUAWEI-hwtacacs-hw1] quit
[*HUAWEI] aaa
[*HUAWEI-aaa] recording-scheme scheme0
[*HUAWEI-aaa-recording-scheme0] recording-mode hwtacacs hw1
[*HUAWEI-aaa-recording-scheme0] quit
[*HUAWEI-aaa] cmd recording-scheme scheme0

```