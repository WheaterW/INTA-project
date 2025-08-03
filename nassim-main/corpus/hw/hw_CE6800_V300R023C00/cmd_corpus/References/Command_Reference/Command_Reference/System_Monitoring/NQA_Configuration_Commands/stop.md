stop
====

stop

Function
--------



The **stop** command stops the current NQA test instance.



By default, the test stops automatically after test packets are sent.


Format
------

**stop**


Parameters
----------

None

Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To stop a running test instance in the test instance view, run **stop** command.


Example
-------

# Stop the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] destination-address ipv4 10.1.1.1
[*HUAWEI-nqa-user-test] stop

```