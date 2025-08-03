ssh server ip-block disable
===========================

ssh server ip-block disable

Function
--------



The **ssh server ip-block disable** command disables an SSH server from locking client IP addresses.

The **undo ssh server ip-block disable** command enables an SSH server to lock client IP addresses.



By default, an SSH server is enabled to lock client IP addresses.


Format
------

**ssh server ip-block disable**

**undo ssh server ip-block disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* If an SSH server is enabled to lock client IP addresses, locked client IP addresses fail to pass authentication and are displayed in the **display ssh server ip-block list** command output.
* If an SSH server is disabled from locking client IP addresses, the **display ssh server ip-block list** command does not display any client IP address that is locked because of authentication failures.
* The operation to disable an SSH server from locking client IP addresses poses system risks and is thereby not recommended.

Example
-------

# Disable an SSH server from locking client IP addresses.
```
<HUAWEI> system-view
[~HUAWEI] ssh server ip-block disable

```