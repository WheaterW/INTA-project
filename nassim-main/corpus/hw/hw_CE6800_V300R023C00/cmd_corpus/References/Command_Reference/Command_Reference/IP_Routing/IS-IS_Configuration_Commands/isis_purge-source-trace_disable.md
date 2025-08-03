isis purge-source-trace disable
===============================

isis purge-source-trace disable

Function
--------



The **isis purge-source-trace disable** command disables IS-IS purge LSP source tracing globally.

The **undo isis purge-source-trace disable** command enables IS-IS purge LSP source tracing globally.



By default, IS-IS purge LSP source tracing is enabled globally.


Format
------

**isis purge-source-trace disable**

**undo isis purge-source-trace disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If network-wide IS-IS LSPs are deleted, purge LSPs are flooded, which adversely affects network stability. In this case, source tracing must be implemented to locate the root cause of the fault immediately to minimize the impact. However, IS-IS itself does not support source tracing. A conventional solution is isolation node by node until the faulty node is located, but the solution is complex and time-consuming. To address this problem, enable IS-IS purge LSP source tracing.



**Precautions**



After the command is run, IS-IS purge LSP source tracing is disabled globally, and source tracing information is no longer recorded.




Example
-------

# Disable IS-IS purge LSP source tracing.
```
<HUAWEI> system-view
[~HUAWEI] isis purge-source-trace disable

```