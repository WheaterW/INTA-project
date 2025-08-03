reset logbuffer
===============

reset logbuffer

Function
--------



The **reset logbuffer** command deletes logs in a log buffer.




Format
------

**reset logbuffer**


Parameters
----------

None


Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To delete all logs in the log buffer, run the reset logbuffer command.

**Precautions**

Logs cannot be restored after being deleted. Exercise caution when running the reset logbuffer command.


Example
-------

# Delete all logs in the log buffer.
```
<HUAWEI> reset logbuffer
Warning: This command will reset the log buffer. Logs in the buffer will be lost. Continue? [Y/N]: y

```