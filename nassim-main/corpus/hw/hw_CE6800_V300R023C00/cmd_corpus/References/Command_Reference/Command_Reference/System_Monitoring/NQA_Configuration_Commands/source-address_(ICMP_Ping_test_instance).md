source-address (ICMP Ping test instance)
========================================

source-address (ICMP Ping test instance)

Function
--------



The **source-address** command configures the source IP address of an NQA ICMP ping test instance.

The **undo source-address** command restores the default source IP address.



By default, the IP address of the outbound interface that sends test packets is used as the source IP address. You can check the routing table based on the destination IP address for confirmation.


Format
------

**source-address ipv4** *srcAddress*

**source-address ipv6** *srcAddr6*

**undo source-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** *srcAddr6* | Specifies the source IPv6 address of an NQA test instance. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **ipv4** *srcAddress* | Specifies the source IPv4 address of an NQA test instance. | The IP address is in dotted decimal notation. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure the source IP address of a test instance, run the **source-address** command. When test packets arrive at the destination address, the receive end returns reply packets to the configured source IP address.

**Configuration Impact**

If the specified source IP address is not the IP address of the device that sends test packets, no reply packet will be received.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.The same test instance can be assigned only one source address, and the latest configuration overrides the previous one.

Example
-------

# Set the source IP address to 10.1.1.1, respectively, for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] source-address ipv4 10.1.1.1

```

# Set the source IPv6 address to 2001:db8:1::1 for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] source-address ipv6 2001:db8:1::1

```