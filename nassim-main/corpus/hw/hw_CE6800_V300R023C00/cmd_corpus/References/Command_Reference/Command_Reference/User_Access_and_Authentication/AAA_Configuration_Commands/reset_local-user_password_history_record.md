reset local-user password history record
========================================

reset local-user password history record

Function
--------

The **reset local-user password history record** command clears historical passwords stored for the local user.



Format
------

**reset local-user** [ *user-name* ] **password** **history** **record**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Clears the historical passwords of the specified user.  If this parameter is not specified, the historical passwords of all local users are cleared. | The value is a string of 1 to 253 case-sensitive characters, spaces not supported. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

If the administrator wants to record historical passwords of local users again, this command can be used to clear existing historical passwords.



Example
-------

# Clear historical passwords of all local users.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] reset local-user password history record

```