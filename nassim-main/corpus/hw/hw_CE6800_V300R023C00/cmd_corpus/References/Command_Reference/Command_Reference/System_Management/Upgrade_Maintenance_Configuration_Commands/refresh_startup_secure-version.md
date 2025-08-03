refresh startup secure-version
==============================

refresh startup secure-version

Function
--------



The **refresh startup secure-version** command updates the secure version of boards.



By default, the security version of a specified slot is updated to the latest version.


Format
------

**refresh startup secure-version** { **slot** *slot-name* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** [ *slot-name* ] | Slot name. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |
| **all** | Indicates all boards. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Software of an earlier version usually has more vulnerabilities. Attackers can exploit these vulnerabilities to penetrate more systems. Preventing the system from rolling back to an earlier version without authentication or authorization can significantly reduce such risks. Once the secure version is upgraded to the expected one, you cannot roll back to the earlier version.After the device starts stably, if the value of Status in the **display startup secure-version** command output of a slot is Need Refresh, run the **refresh startup secure-version** command to update the security version of the slot.


Example
-------

# Refresh the security version.
```
<HUAWEI> system-view
[~HUAWEI] refresh startup secure-version all
Warning: This operation will set the nv-count of the board. Once set, this device cannot be rolled back to an earlier one. Are you sure you want to perform this operation? [Y/N]:y
Warning: This operation is irrevocable and you have no means to cancel it once committed. Are you sure to do this operation? [Y/N]:y
Info: Operating, please wait for a moment.
Info: Slot 1 success to refresh CPU NV counter.

```