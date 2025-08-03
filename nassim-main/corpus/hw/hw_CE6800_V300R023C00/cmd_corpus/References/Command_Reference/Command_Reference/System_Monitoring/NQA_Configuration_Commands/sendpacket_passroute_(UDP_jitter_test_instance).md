sendpacket passroute (UDP jitter test instance)
===============================================

sendpacket passroute (UDP jitter test instance)

Function
--------



The **sendpacket passroute** command configures an NQA UDP Jitter test instance to send packets without searching the routing table.

The **undo sendpacket passroute** command enables an NQA test instance to send packets based on the routing table.



By default, the NQA test packets are sent without searching the routing table.


Format
------

**sendpacket passroute**

**undo sendpacket passroute**


Parameters
----------

None

Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure an NQA test instance to send packets without searching the routing table, run the **sendpacket passroute** command.The **sendpacket passroute** command is applicable to the following scenarios:No source IP address is set.

* If no outbound interface is configured for an NQA test instance, after the **sendpacket passroute** command is run, the source IP address of packets to be sent in the test is obtained using an internal algorithm.
* If an outbound interface is configured for an NQA test instance, after the **sendpacket passroute** command is run, the IP address of the outbound interface is used as the source IP address of packets to be sent in the test.A source IP address is set.
* If no outbound interface is configured for an NQA test instance, after the **sendpacket passroute** command is run, the specified source IP address is used as the source IP address of packets to be sent in the test.
* If an outbound interface is configured for an NQA test instance, after the **sendpacket passroute** command is run, the specified source IP address is used as the source IP address of packets to be sent in the test.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Configure the test instance named user test to send packets without searching the routing table.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] sendpacket passroute

```