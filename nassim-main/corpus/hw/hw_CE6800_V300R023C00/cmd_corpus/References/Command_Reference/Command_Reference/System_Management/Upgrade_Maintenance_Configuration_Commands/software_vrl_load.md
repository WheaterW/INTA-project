software vrl load
=================

software vrl load

Function
--------



The **software vrl load** command loads a VRL to the system.



By default, a specified VRL file is loaded to the system.


Format
------

**software vrl load** *vrlName*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vrlName* | Configure the VRL file name. | The value is a string of 5 to 63 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Software of an earlier version usually has more vulnerabilities. Attackers can exploit these vulnerabilities to penetrate more systems. Preventing the system from rolling back to an earlier version without authentication or authorization can significantly reduce such risks. You can use the Version Revocation List (VRL) technology to prevent the system from rolling back to a vulnerable version. You can run the **software load** command to load the VRL to the system.


Example
-------

# Load a VRL file to the system.
```
<HUAWEI> software vrl load abc.vrl

```