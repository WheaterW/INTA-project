outbound recording-scheme
=========================

outbound recording-scheme

Function
--------

The **outbound recording-scheme** command applies a policy to a recording scheme to record the connection information.

The **undo outbound recording-scheme** command deletes a policy from a recording scheme. Connection information is not recorded then.

By default, connection information is not recorded.



Format
------

**outbound recording-scheme** *recording-scheme-name*

**undo outbound recording-scheme**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *recording-scheme-name* | Specifies the name of a recording scheme. | The value is a string of 1 to 32 case-sensitive characters, and cannot contain spaces. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

Incorrect connections may result in network faults, for example, loops. The connection information recorded on a server helps you monitor devices. When network faults occur, you can locate faults based on the connection information recorded on the server.

**Prerequisites**

A recording scheme has been created using the **recording-scheme** command in the AAA view and an HWTACACS server template has been associated with a recording scheme using the **recording-mode hwtacacs** command in the recording scheme view.



Example
-------

# Apply a policy to the recording scheme named scheme to record the connection information.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template hw1
[*HUAWEI-hwtacacs-hw1] quit
[*HUAWEI] aaa
[*HUAWEI-aaa] recording-scheme scheme
[*HUAWEI-aaa-recording-scheme] recording-mode hwtacacs hw1
[*HUAWEI-aaa-recording-scheme] quit
[*HUAWEI-aaa] outbound recording-scheme scheme

```