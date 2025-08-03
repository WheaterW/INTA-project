reset auto-source-trace record
==============================

reset auto-source-trace record

Function
--------



The **reset auto-source-trace record** command clears records about proactive source tracing.




Format
------

**reset auto-source-trace record** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The **reset auto-source-trace record** command clears records about proactive source tracing.


Example
-------

# Clear records about proactive source tracing on the specified slot.
```
<HUAWEI> reset auto-source-trace record slot 1

```