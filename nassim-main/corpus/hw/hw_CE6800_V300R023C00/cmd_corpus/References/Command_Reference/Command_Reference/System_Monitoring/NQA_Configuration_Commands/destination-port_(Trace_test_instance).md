destination-port (Trace test instance)
======================================

destination-port (Trace test instance)

Function
--------



The **destination-port** command can configure the destination port number of an NQA trace test instance.

The **undo destination-port** command can restore the default setting.



By default, the destination port number of a trace test is 33434.


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

During the running of a test instance, if you modify the destination port parameter, the system prompts you whether to stop the test instance. Press Y or N as required.

* If you press Y, the test instance is terminated, and the parameter value is changed. After you submit the change, the changed parameter value takes effect. To restart the test instance, run the **start** command.
* If you press N, the parameter fails to be modified, and the test instance continues to run.Ports 33434 to 33678 are the default ports for tracert. If these ports are used as the destination ports for NQA test instances, NQA packets may be discarded due to rate limiting. You are advised to use ports other than ports 33434 to 33678 as the destination ports of NQA test instances.

Example
-------

# Set the destination port number for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type trace
[*HUAWEI-nqa-user-test] destination-port 2000

```