configuration exclusive timeout
===============================

configuration exclusive timeout

Function
--------



The **configuration exclusive timeout** command sets the timeout period before the system automatically unlocks the configuration set.

The **undo configuration exclusive timeout** command restores the default timeout period.



By default, the timeout period is 30 seconds.


Format
------

**configuration exclusive timeout** *timeout-value*

**undo configuration exclusive timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *timeout-value* | Specifies the timeout period before the system automatically unlocks the configuration set. | The value is an integer ranging from 1 to 7200, in seconds. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Running the **configuration exclusive timeout** command can set an allowable maximum period when no commands are delivered by the user that locks the configuration set. After the timeout period expires, the configuration set is automatically unlocked and other users can normally run commands.


Example
-------

# Set the timeout period before the system automatically unlocks the configuration set to 120 seconds.
```
<HUAWEI> system-view
[~HUAWEI] configuration exclusive timeout 120

```