ipv6 nd security strict
=======================

ipv6 nd security strict

Function
--------



The **ipv6 nd security strict** command enables the strict security mode on an interface.

The **undo ipv6 nd security strict** command restores the default security mode.



By default, the strict security mode is not enabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd security strict**

**undo ipv6 nd security strict**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, an interface receives all secure and insecure ND messages. To prevent network attacks, you need to enable the strict security mode on the interface. In this mode, the following ND messages are considered insecure and discarded:

* The received ND message does not carry the CGA or RSA option. That is, the interface that sends the ND message is not configured with the CGA address.
* The key length in the received ND message is out of the range allowed on the interface.
* The rate of processing the received ND message exceeds the rate limit of the system.
* The difference between the receive time and the send time of the ND message is out of the time range allowed on the interface.Note:On a link, device A is configured with strict IPv6 SEND whereas device B is not. In this case, device A regards the ND messages sent from device B insecure and rejects them.

**Prerequisites**



IPv6 has been enabled on the involved interface using the **ipv6 enable** command.



**Configuration Impact**



After the strict security mode is enabled on an interface, the system will not perform Duplicate Address Detection (DAD) on insecure nodes. In this case, the insecure conflicting addresses that may exist on the network cannot be detected. Therefore, re-triggering of DAD is recommended after the strict security mode is disabled.



**Precautions**



If an interface has been enabled to work in strict security mode, configure all addresses of the interface as CGA addresses. Otherwise, the interface may select a common IPv6 address as the source address, which causes a security check failure and a service interruption.




Example
-------

# Enable the strict security mode on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd security strict

```