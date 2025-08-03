destination-port (UDP Jitter test instance)
===========================================

destination-port (UDP Jitter test instance)

Function
--------



The **destination-port** command can configure the destination port number of an NQA test instance of UDP jitter test type.

The **undo destination-port** command, you can restore the default setting.



By default, to perform a UDP jitter test, you must run the destination-port command to specify a port number for the UDP jitter test.


Format
------

**destination-port** *destPort-value*

**undo destination-port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *destPort-value* | Specifies the destination port number (UDP port) of an NQA test instance. | The value is an integer from 1 to 65535. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

NQA monitors service features by creating test instances. In NQA, two test ends are called an NQA client and an NQA server. An NQA test is initiated by the NQA client. After test instances are configured on the client, NQA places different types of test instances into various test queues. After the test starts, a response packet is returned. Carriers can then check the operating status about protocols by analyzing the received response packet.For a test instance, the port for accessing the server is specified using the destination port number configured using the **destination-port** command on the client.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the destination port number for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] destination-port 2000

```