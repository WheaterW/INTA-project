tracert-hopfailtimes (Trace test instance)
==========================================

tracert-hopfailtimes (Trace test instance)

Function
--------



The **tracert-hopfailtimes** command sets the maximum hop failures in a probe for a trace test instance. When the number of hop failures reaches the set value, the probe is considered failed.

The **undo tracert-hopfailtimes** command restores the default maximum hop.



By default, a probe is considered failed when there are five hop failures in the probe.


Format
------

**tracert-hopfailtimes** *hopFailTimes*

**undo tracert-hopfailtimes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hopFailTimes* | Specifies the number of continuous hop failures. | The value is an integer ranging from 1 to 255. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the test, the operation of sending a test packet is called a probe. Multiple packets can be sent during a test, which means that a test contains multiple probes.An NQA trace test is used to monitor the forwarding path between the NQA client and a destination and collect statistics about devices along the forwarding path. The process of a test is as follows:1.The client constructs a UDP packet with TTL 1 and sends the packet to the destination.2.After the first-hop device receives the UDP packet, it checks the TTL field and finds that the TTL decreases to 0. Then, it discards the UDP packet and sends an ICMP Time Exceeded packet to the client.3.After the client receives the ICMP Time Exceeded packet, it records the IP address of the first-hop device and re-constructs a UDP packet with TTL 2.4.After the second-hop device receives the UDP packet, it checks the TTL field and finds that the TTL decreases to 0. Then, it discards the UDP packets and returns an ICMP Time Exceeded packet.5.The procedure repeats after the packet reaches the last-hop device. The last-hop device returns an ICMP Port Unreachable packet to the client.In this process, the client may fail to receive the ICMP Time Exceeded packet because the devices between the client and destination are configured with the firewall or configured not to respond to ICMP packets. In this case, the probe of this hop fails. In actual applications, the client may fail to receive the ICMP Time Exceeded packet due to a node fault on the path.By default, the maximum TTL is 30. To prevent continuous hop failures for a long time, you can run the **tracert-hopfailtimes** command to set the maximum hop failures for a trace test instance. When the number of hop failures reaches the set value, the probe fails.

**Configuration Impact**

The **tracert-livetime** command sets the minimum and maximum lifetime of a test instance. This prevents endless traveling of test packets in routing on the network. You are advised to use the **tracert-livetime** command and the **tracert-hopfailtimes** command together to improve efficiency in performing trace tests.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the maximum hop failures for the test instance named user test to 10.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type trace
[*HUAWEI-nqa-user-test] tracert-hopfailtimes 10

```