reset local-access-user password history record
===============================================

reset local-access-user password history record

Function
--------



The **reset local-access-user password history record** command clears historical passwords of local access users.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**reset local-access-user** [ *user-name* ] **password** **history** **record**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Clears the historical passwords of the specified user.  If this parameter is not specified, the historical passwords of all local access users are cleared. | The value is a string of 1 to 64 case-sensitive characters without spaces. |



Views
-----

AAA view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

If the administrator wants to record the historical passwords of local access users again, run this command to clear the historical passwords of local access users.


Example
-------

# Clear historical passwords of all local access users.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] reset local-access-user password history record

```