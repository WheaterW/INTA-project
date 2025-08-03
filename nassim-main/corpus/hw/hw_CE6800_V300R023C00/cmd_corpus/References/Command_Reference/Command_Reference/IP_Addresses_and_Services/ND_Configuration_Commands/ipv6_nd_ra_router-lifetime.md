ipv6 nd ra router-lifetime
==========================

ipv6 nd ra router-lifetime

Function
--------



The **ipv6 nd ra router-lifetime** command sets the lifetime of the RA messages sent by a Router.

The **undo ipv6 nd ra router-lifetime** command restores the default setting.



By default, the lifetime for RA messages is three times of the maximum interval for advertising RA messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra router-lifetime** *ra-lifetime*

**undo ipv6 nd ra router-lifetime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ra-lifetime* | Specifies the lifetime of the RA messages sent by a Router. | The value is 0 or an integer ranging from 4 to 9000, in seconds. |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A Router adds the lifetime of the RA message to the RA message before sending the RA message to the hosts on the local network segment. The lifetime indicates the validity period of this Router as a default router of these hosts.

**Prerequisites**



IPv6 has been enabled on the involved interface using the **ipv6 enable** command.



**Configuration Impact**

If a host receives an RA message with the lifetime field being 0, the host does not add the address of this router to its default routing entries.

**Precautions**

The lifetime of the RA messages must be longer than or equal to the interval for sending RA messages. (By default, the maximum and minimum intervals for sending RA messages are 600 seconds and 200 seconds, respectively. You can run the **ipv6 nd ra** command to set a proper interval.) If the set lifetime of the RA messages is shorter than the set interval for sending RA messages, the system prompts an error. In such a case, you need to re-set the lifetime.


Example
-------

# On 100GE 1/0/1, set the lifetime of the RA messages sent by a Router to 1000 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ra router-lifetime 1000

```