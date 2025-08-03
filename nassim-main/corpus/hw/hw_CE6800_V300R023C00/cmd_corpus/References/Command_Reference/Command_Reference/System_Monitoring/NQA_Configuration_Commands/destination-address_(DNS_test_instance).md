destination-address (DNS test instance)
=======================================

destination-address (DNS test instance)

Function
--------



The **destination-address** command configures a destination URL address for an NQA test instance.

The **undo destination-address** command deletes a destination URL address.



By default, the destination address of an NQA test is not configured.


Format
------

**destination-address url** *urlValue*

**undo destination-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **url** *urlValue* | Specifies the destination URL for an NQA test instance. | The value is a string of 1 to 230 case-sensitive characters, spaces not supported.  The string can contain spaces if it is enclosed in double quotation marks ("). |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

NQA monitors service features by creating test instances. In NQA, two test ends are called an NQA client and an NQA server. An NQA test is initiated by the NQA client. After test instances are configured on the client, NQA places different types of test instances into various test queues. After the test starts, a response packet is returned. You can then check the operating status about protocols by analyzing the received response packet.For a test instance, the server is specified using the destination MAC address configured using the **destination-address** command.

**Configuration Impact**

If a destination MAC address has been configured for a test instance, running the **destination-address** command overrides the previous configuration.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.The URL must contain a period (.). Otherwise, the test may fail.

Example
-------

# Set a destination URL for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type dns
[*HUAWEI-nqa-user-test] destination-address url dta.huawei.com

```