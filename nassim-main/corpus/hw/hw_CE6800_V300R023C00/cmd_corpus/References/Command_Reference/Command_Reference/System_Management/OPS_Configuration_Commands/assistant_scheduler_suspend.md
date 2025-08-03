assistant scheduler suspend
===========================

assistant scheduler suspend

Function
--------



The **assistant scheduler suspend** command suppresses functions provided by maintenance assistants.

The **undo assistant scheduler suspend** command cancels the configuration.



By default, the functions provided by maintenance assistants are enabled.


Format
------

**assistant scheduler suspend**

**undo assistant scheduler suspend**


Parameters
----------

None

Views
-----

OPS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To suppress the functions provided by maintenance assistants before clearing the configured maintenance assistants one by one, run the assistant scheduler suspend command.
* To temporarily suppress the functions provided by maintenance assistants (for example, preventive maintenance and upgrade functions), run the assistant scheduler suspend command.

Example
-------

# Suppress the functions provided by maintenance assistants.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant scheduler suspend

```