test-type (NQA view)
====================

test-type (NQA view)

Function
--------



The **test-type** command specifies the test type for an NQA test instance.

The **undo test-type** command deletes the test type.



By default, no test type is configured.


Format
------

**test-type** { **tcp** | **jitter** | **icmp** | **icmpjitter** | **trace** | **dns** }

**undo test-type**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tcp** | Indicates a TCP test, which checks TCP services. | - |
| **jitter** | Indicates a UDP jitter test, which checks the jitter in processing UCP packets. | - |
| **icmp** | Indicates an ICMP test to test link connectivity. If an ICMP test instance fails, run the ping -detail or ping ipv6 -detail command to locate the fault. | - |
| **icmpjitter** | Indicates an ICMP jitter test, which checks the path jitter by sending ICMP packets. | - |
| **trace** | Indicates a trace route test, which detects the faulty node on a link. | - |
| **dns** | Indicates a DNS test, which tests DNS service performance. | - |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

NQA test instances measure the performance of various protocols running on the network, so that carriers can collect network operation indexes in real time. When a fault occurs on the network, you can effectively diagnose and locate the fault.NQA diagnoses and locates faults through various types of test instances.The following is an example:

* A DNS test has been configured using the **test-type dns** command. A DNS test is used to measure the speed at which a specified DNS name is resolved to an IP address. The DNS test is carried by UDP packets.
* An ICMP test is configured using the **test-type icmp** command. When sending packets in an ICMP test, you need to set ping parameters according to the parameters of the test group configured by the user. These parameters include TTL, ToS, and delay. After that, you can enable the device to send test packets to the destination address and interface.When receiving a packet, the ICMP test instance checks whether the packet times out. If the packet times out, the ICMP test instance performs timeout processing. If the packet does not time out, the ICMP test instance calculates the RTT and records the information in the historical record and result record.
* To configure an ICMP jitter test, run the **test-type icmpjitter** command. The test uses ICMP packets to simulate end-to-end jitter of various services and detects path jitter.
* A TraceRoute test has been configured using the **test-type trace** command. In a tracert test, packets are sent based on the configured parameters, including the TTL and delay. The TTL of the ICMP Echo Request packet sent by the destination address for the first time is 1. After the TTL expires, an ICMP Echo Reply packet is returned. This process repeats until all packets on the path are responded, the TraceRoute process is complete. The sender collects statistics on the test result based on the received response packets.
* A TCP test is configured using the **test-type tcp** command. When testing the TCP function, you must configure the NQA TCP server on the peer end. The client initiates a test to the specified IP address and port of the server. The TCP test measures the time for setting up a TCP connection.
* A jitter test has been configured using the **test-type jitter** command. During the test, the source end sends data packets to the destination end at a certain interval. The sent data packets have corresponding timestamps. After receiving a data packet, the receiver adds a timestamp to the data packet and sends the data packet back to the source end. After receiving the data packets, the source calculates the jitter time. A jitter test instance supports a maximum of 3000 consecutive packets to simulate voice service traffic.

**Precautions**

* The type of a test instance cannot be modified once it is configured. That is, if you modify the parameters of a test instance during the running of the test instance, the test instance stops running.
* Before starting an ICMP jitter or path jitter test instance in timestamp mode, you need to enable the function of sending and receiving ICMP timestamp packets.

Example
-------

# Set the test type of an NQA test instance to icmp.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp

```

# Set the test type of an NQA test instance to DNS.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type dns

```