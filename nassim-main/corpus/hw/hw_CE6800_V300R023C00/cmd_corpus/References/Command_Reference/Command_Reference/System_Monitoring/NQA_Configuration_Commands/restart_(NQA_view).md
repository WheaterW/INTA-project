restart (NQA view)
==================

restart (NQA view)

Function
--------



The **restart** command stops a running test instance and then restarts this test instance.



By default, the on-going test instance is not aborted manually.


Format
------

**restart**


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

**Usage Scenario**

Running the **restart** command has the same function as running the following commands in sequence:1.Run the **stop** command to stop running NQA test instances. The **stop** command stops only the running NQA test instances (test instances in the active state).2.Run the **start now** command to start the NQA test instance immediately. For the same test instance, the **start now** command can be used again only after the previous configuration is complete.To restart a test instance, you can use the **restart** command.

**Configuration Impact**

If a test instance is not complete, running the **restart** command causes incomplete test results.

**Precautions**

If a test instance is not started, running the **restart** command functions the same as running the **start now** command. Both commands start the test instance immediately.


Example
-------

# Restart the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] destination-address ipv4 10.1.1.1
[*HUAWEI-nqa-user-test] restart

```