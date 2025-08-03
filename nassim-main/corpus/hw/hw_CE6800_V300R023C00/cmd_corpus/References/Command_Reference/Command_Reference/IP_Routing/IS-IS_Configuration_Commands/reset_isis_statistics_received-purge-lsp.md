reset isis statistics received-purge-lsp
========================================

reset isis statistics received-purge-lsp

Function
--------



The **reset isis statistics received-purge-lsp** command clears statistics about received purge LSPs with 00-00 fragments.




Format
------

**reset isis** [ *process-id* ] **statistics** **received-purge-lsp**

**reset isis statistics received-purge-lsp** [ *process-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of the IS-IS process from which statistics about purge LSPs with 00-00 fragments are to be cleared.  By default, statistics about purge LSPs with 00-00 fragments received by all processes are cleared. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When locating faults on an IS-IS network, you can run the **reset isis statistics received-purge-lsp** command to clear statistics about received purge LSPs with 00-00 fragments and then view the latest error information to facilitate fault locating.


Example
-------

# Clear statistics about received purge LSPs with 00-00 fragments.
```
<HUAWEI> reset isis statistics received-purge-lsp

```