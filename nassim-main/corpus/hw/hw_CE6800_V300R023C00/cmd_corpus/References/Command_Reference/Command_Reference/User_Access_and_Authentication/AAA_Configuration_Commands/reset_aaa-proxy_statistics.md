reset aaa-proxy statistics
==========================

reset aaa-proxy statistics

Function
--------



The reset aaa-proxy statistics command clears statistics about AAA proxy.




Format
------

**reset aaa-proxy statistics** { **error** | **message** | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **error** | Clears statistics of AAA proxy errors. | - |
| **message** | Clears statistics of AAA proxy messages. | - |
| **all** | Clears statistics of AAA proxy errors and messages. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can use the **reset aaa-proxy statistics** command to clear statistics about AAA proxy.


Example
-------

# Clear statistics about AAA proxy modules.
```
<HUAWEI> reset aaa-proxy statistics message

```