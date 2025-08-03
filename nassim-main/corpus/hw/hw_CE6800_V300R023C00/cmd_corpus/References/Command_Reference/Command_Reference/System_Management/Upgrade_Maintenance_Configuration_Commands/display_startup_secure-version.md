display startup secure-version
==============================

display startup secure-version

Function
--------



The **display startup secure-version** command displays the secure version information.




Format
------

**display startup secure-version**


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

You can view the security version of each slot, including the current version, expected version, and status to determine whether to update the security version.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# display secure version information.
```
<HUAWEI> display startup secure-version
------------------------------------------------------------------------------
Slot         Type   CurVersion   ExpectedVersion          Status
------------------------------------------------------------------------------
1   MPU     1           1                        Refreshed
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display startup secure-version** command output
| Item | Description |
| --- | --- |
| Slot | Board slot ID. |
| Type | Board type. |
| CurVersion | Current version of the device. |
| ExpectedVersion | Expected version. |
| Status | Current version status:  -Refreshed.  -Need refresh.  -Unsupport. |