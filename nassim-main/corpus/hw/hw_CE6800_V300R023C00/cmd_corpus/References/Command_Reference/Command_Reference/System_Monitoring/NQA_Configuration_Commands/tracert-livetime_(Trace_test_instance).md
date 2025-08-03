tracert-livetime (Trace test instance)
======================================

tracert-livetime (Trace test instance)

Function
--------



The **tracert-livetime** command sets the lifetime of a trace test instance.

The **undo tracert-livetime** command restores the default lifetime.



By default, the initial TTL of packets is 1, and the maximum TTL of packets is 30.


Format
------

**tracert-livetime first-ttl** *first-ttl* **max-ttl** *max-ttl*

**undo tracert-livetime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **first-ttl** *first-ttl* | Specifies the initial TTL of packets. | The value is 1. |
| **max-ttl** *max-ttl* | Specifies the maximum TTL of packets. | The value is an integer ranging from 1 to 255. max-ttl must be greater than or equal to first-ttl |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the minimum and maximum lifetime of a test instance, run the **tracert-livetime** command. This prevents endless traveling of test packets in routing on the network.

**Configuration Impact**

When configuring first-ttl and max-ttl, ensure that max-ttl is not smaller than max-ttl; otherwise, the configuration fails.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the lifetime of the test instance named user test, with the initial TTL 5 and the maximum TTL 20.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type trace
[*HUAWEI-nqa-user-test] tracert-livetime first-ttl 5 max-ttl 20

```