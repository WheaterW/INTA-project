clear configuration candidate
=============================

clear configuration candidate

Function
--------



The **clear configuration candidate** command clears an uncommitted configuration.




Format
------

**clear configuration candidate**


Parameters
----------

None

Views
-----

All views except the user view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To clear a configuration that has not been committed in the two-phase configuration validation mode, you can run the clear configuration candidate command.

**Prerequisites**



A configuration is edited in two-phase configuration validation mode.



**Configuration Impact**



The uncommitted configuration will be deleted, and the system view will be displayed.




Example
-------

# Clear the configuration that has not been committed.
```
<HUAWEI> system-view
[~HUAWEI] sftp server enable
[*HUAWEI] clear configuration candidate

```