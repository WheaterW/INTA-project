ttl (UDP jitter test instance)
==============================

ttl (UDP jitter test instance)

Function
--------



The **ttl** command sets the time to live (TTL) value for the NQA jitter test packets.

The **undo ttl** command restores the default TTL value.



By default, the TTL value is 30.


Format
------

**ttl** *ttlValue*

**undo ttl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ttlValue* | Specifies the TTL value of test packets. | The value is an integer ranging from 1 to 255. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

TTL is an 8-bit field in the IP header. The TTL value is decreased by 1 on each hop. When the TTL value is 0, the sender receives an ICMP Time Exceeded packet.The **ttl** command sets the TTL value for test packets so that the test instance is performed within a specified number of hops.

**Configuration Impact**



If the TTL value has been set for test packets, running the **ttl** command again overrides the previous configuration.



**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the TTL value for packets in the test instance named user test to 10.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] ttl 10

```