display software vrl
====================

display software vrl

Function
--------



The **display software vrl** command displays the VRL information.




Format
------

**display software vrl**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Software of an earlier version usually has more vulnerabilities. Attackers can exploit these vulnerabilities to penetrate more systems. Preventing the system from rolling back to an earlier version without authentication or authorization can significantly reduce such risks. You can use the Version Revocation List (VRL) technology to prevent the system from rolling back to a vulnerable version. You can run the **display software vrl** command to view the VRL version.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the VRL that has been loaded to the system.
```
<HUAWEI> display software vrl
---------------------------------------------
Slot       Type       Version 
---------------------------------------------
---------------------------------------------

```

**Table 1** Description of the **display software vrl** command output
| Item | Description |
| --- | --- |
| Slot | Slot of the board where the VRL is configured. |
| Type | Board type. |
| Version | The version of VRL file. |