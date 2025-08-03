system recording-scheme
=======================

system recording-scheme

Function
--------

The **system recording-scheme** command applies a policy in a recording scheme to record the system events.

The **undo system recording-scheme** command deletes a policy from a recording scheme. System events are not recorded then.

By default, system events are not recorded.



Format
------

**system recording-scheme** *recording-scheme-name*

**undo system recording-scheme**



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

The system events recorded on the server help you monitor devices. When network faults occur, you can locate faults based on the system events recorded on the server.

**Prerequisites**

A recording scheme has been created using the **recording-scheme** command in the AAA view and an HWTACACS server template has been associated with a recording scheme using the **recording-mode hwtacacs** command in the recording scheme view.

**Precautions**

Currently, the device can record only the events caused by the **reboot** command.



Example
-------

# Apply a policy in the recording scheme named scheme to record the system events.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template hw1
[*HUAWEI-hwtacacs-hw1] quit
[*HUAWEI] aaa
[*HUAWEI-aaa] recording-scheme scheme
[*HUAWEI-aaa-recording-scheme] recording-mode hwtacacs hw1
[*HUAWEI-aaa-recording-scheme] quit
[*HUAWEI-aaa] system recording-scheme scheme

```