destination-port (TCP test instance view)
=========================================

destination-port (TCP test instance view)

Function
--------



The **destination-port** command can configure the destination port number of an NQA test instance of TCP test type.

The **undo destination-port** command can restore the default setting.



By default, the destination port number of a TCP test instance is 7.


Format
------

**destination-port** *port-number*

**undo destination-port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies the destination port number (TCP port) of an NQA test instance. | The value is an integer from 1 to 65535. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

NQA detects service features by creating test instances. In NQA, two test ends are called an NQA client and an NQA server. An NQA test is initiated by the NQA client. After test instances are configured through commands on the client, NQA places different types of test instances into various test queues. After the test starts, a response packet is returned. Carriers can then know the operating status about protocols by analyzing the received response packet.For a test instance, the port for accessing the server is specified through the destination port number configured with the **destination-port** command on the client.For example, if you need to detect whether the TCP service runs normally on the peer device through a TCP test instance, perform the following configurations:On the server: Configure the TCP server used for NQA tests, including the client IP addresses that are supported and the TCP port number opened to the client.On the client:1.Create an NQA test instance and configure its type as TCP.2.Configure the IP address of the server as the destination IP address and configure the opened TCP port number on the server as the destination port number.3.Start the test instance.

**Precautions**

For a TCP test instance, the destination port number must be the same as the port number enabled on the server.During the running of a test instance, if you modify the destination port parameter, the system prompts you whether to stop the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated, and the parameter value is modified. After you submit the change, the modified parameter value takes effect. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameter fails to be modified.

Example
-------

# Set the destination port number for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type tcp
[*HUAWEI-nqa-user-test] destination-port 2000

```