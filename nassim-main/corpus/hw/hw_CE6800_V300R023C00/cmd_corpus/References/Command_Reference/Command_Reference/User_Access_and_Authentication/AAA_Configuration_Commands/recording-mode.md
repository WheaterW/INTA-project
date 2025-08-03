recording-mode
==============

recording-mode

Function
--------



The **recording-mode** command associates an HWTACACS server template with a recording scheme.

The **undo recording-mode** command unbinds an HWTACACS server template from a recording scheme.



By default, no HWTACACS server template is associated with a recording scheme.


Format
------

**recording-mode hwtacacs** *template-name*

**undo recording-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hwtacacs** *template-name* | Specifies the name of an HWTACACS server template. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  The HWTACACS server template must already exist. |



Views
-----

Recording scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The device needs to send the records such as the executed commands, connection information, and system events to the specified HWTACACS accounting server; therefore, an HWTACACS server template needs to be associated with a recording scheme.

**Prerequisites**

The HWTACACS server template has been created by using the **hwtacacs-server template** command.


Example
-------

# Associate the recording scheme scheme0 with the HWTACACS server template tacacs1.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template tacacs1
[*HUAWEI-hwtacacs-tacacs1] quit
[*HUAWEI] aaa
[*HUAWEI-aaa] recording-scheme scheme0
[*HUAWEI-aaa-recording-scheme0] recording-mode hwtacacs tacacs1

```