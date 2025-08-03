jitter-packetnum (UDP Jitter test instance)
===========================================

jitter-packetnum (UDP Jitter test instance)

Function
--------



The **jitter-packetnum** command sets the number of the packets sent each time in a probe for UDP Jitter test.

The **undo jitter-packetnum** command restores the default number of the packets sent each time in a probe.



By default, 20 packets are sent each time in a probe.


Format
------

**jitter-packetnum** *packetNum*

**undo jitter-packetnum**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packetNum* | Specifies the number of packets sent each time in a probe. | The value is an integer ranging from 1 to 3000. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a jitter test instance is used to monitor VoIP services, to set the number of the packets sent each time in a probe, run the **jitter-packetnum** command. The test simulates actual traffic within a specified period of time.The **jitter-codec** command can also be used to simulate VoIP services. The **jitter-packetnum** command with a parameter configured, however, can implement more finely granular simulation. In addition, the **jitter-packetnum** command sets the number of packets to be sent for all services, which is widely applied.

**Configuration Impact**

If a code type has been configured, running the **jitter-packetnum** command overrides the configured code type.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Configure that one test to have 3 probe attempts and 1000 packets to be sent for each probe attempt.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] probe-count 3
[*HUAWEI-nqa-user-test] jitter-packetnum 1000

```