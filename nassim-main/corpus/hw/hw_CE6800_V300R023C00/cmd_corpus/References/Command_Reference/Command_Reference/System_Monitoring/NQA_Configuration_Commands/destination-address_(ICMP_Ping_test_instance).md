destination-address (ICMP Ping test instance)
=============================================

destination-address (ICMP Ping test instance)

Function
--------



The **destination-address** command configures a destination IP address for an NQA test instance of the ICMP ping test type.

The **undo destination-address** command deletes the destination IP address of an NQA test instance of the ICMP ping test type.



By default, the destination address of an NQA test is not configured.


Format
------

**destination-address ipv4** *destAddress*

**destination-address ipv6** *destAddress6*

**undo destination-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** *destAddress6* | Specifies the destination IPv6 address for an NQA test instance. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **ipv4** *destAddress* | Specifies the destination IPv4 address for an NQA test instance. | The address is in dotted decimal notation. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

NQA monitors service features by creating test instances. In NQA, two test ends are called an NQA client and an NQA server. An NQA test is initiated by the NQA client. After test instances are configured on the client, NQA places different types of test instances into various test queues. After the test starts, a response packet is returned. You can then check the operating status about protocols by analyzing the received response packet.For a test instance, the server is specified using the destination IP address configured using the **destination-address** command.

**Configuration Impact**

If a destination IP address has been configured for a test instance, running the **destination-address** command overrides the previous configuration.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.The same test instance can be assigned only one destination address, and the latest configuration overrides the previous one.

Example
-------

# Assign a destination IPv4 address to the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] destination-address ipv4 10.1.1.1

```