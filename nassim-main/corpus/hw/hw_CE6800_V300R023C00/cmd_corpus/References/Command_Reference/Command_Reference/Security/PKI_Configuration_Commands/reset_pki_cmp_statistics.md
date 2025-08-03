reset pki cmp statistics
========================

reset pki cmp statistics

Function
--------



The **reset pki cmp statistics** command clears the statistics on CMP sessions.




Format
------

**reset pki cmp statistics** [ **session** *session-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **session** *session-name* | Specifies the name of a CMP session. | The value must be an existing CMP session name. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a CMP session is specified, the statistics of the session is cleared. If no CMP session is specified, the statistics of all sessions is cleared.


Example
-------

# Clear statistics on CMP session test.
```
<HUAWEI> system-view
[HUAWEI] pki cmp session test
[HUAWEI-pki-cmp-session-test] quit
[HUAWEI] quit
<HUAWEI> reset pki cmp statistics session test

```