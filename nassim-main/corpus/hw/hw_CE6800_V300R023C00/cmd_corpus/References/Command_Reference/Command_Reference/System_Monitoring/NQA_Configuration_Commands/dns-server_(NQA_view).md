dns-server (NQA view)
=====================

dns-server (NQA view)

Function
--------



The **dns-server** command sets the IP address of a DNS server for a DNS test instance.

The **undo dns-server** command deletes the IP address of a DNS server.



By default, no IP address is configured for a DNS server.


Format
------

**dns-server ipv4** *ip-address*

**undo dns-server**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** *ip-address* | Specifies an IPv4 address for a DNS server. | The value is in dotted decimal notation. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A DNS test instance detects the speed at which a DNS name is resolved to an IP address. It clearly reflects the performance of the DNS protocol on the network.

**Prerequisites**



The NQA test instance type has been set to DNS test using the **test-type** command.



**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters are changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the IP address of the DNS server to 10.1.1.1 for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type dns
[*HUAWEI-nqa-user-test] dns-server ipv4 10.1.1.1

```