ipv6 nd ns retrans-timer
========================

ipv6 nd ns retrans-timer

Function
--------



The **ipv6 nd ns retrans-timer** command sets the interval for sending NS messages.

The **undo ipv6 nd ns retrans-timer** command restores the default setting.



By default, the interval for sending NS messages is 1000 milliseconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ns retrans-timer** *interval*

**undo ipv6 nd ns retrans-timer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval for sending NS messages. | The value is an integer ranging from 1000 to 4294967295, in milliseconds. |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The interval for sending NS messages provides the following functions:

* Controlling the interval for a local Router to probe the reachability of neighbors
* Controlling the interval for a local Router to perform DAD
* Being a parameter field in an RA message to notify the hosts of the interval for sending NS messages

**Prerequisites**



Before running the **ipv6 nd ns retrans-timer** command to set the interval for sending NS messages, you need to run the **ipv6 enable** command in the interface view to enable the IPv6 function on the interface.



**Configuration Impact**

Frequently sending NS messages results in the high CPU usage, which affects the system performance. Therefore, you are recommended to set the interval for sending NS messages to a longer value. The default interval, 1000 milliseconds, is recommended.The **ipv6 nd ns retrans-timer** command is circular in nature. That is, if the intervals set two times are different, the latest setting takes effect.

**Precautions**

Commonly, the interval for sending NS message is the same as that for sending RA messages. In the following cases, however, the interval for sending NS messages is of the default value 1000 milliseconds whereas the interval for sending NA messages is 0 milliseconds.

* The interval for sending NS messages is not set, that is, the default value is used.
* The **undo ipv6 nd ns retrans-timer** command is run to restore the default setting.After a host receives an RA message with the interval for sending NA messages being 0 milliseconds from a Router, it uses the default interval, 1000 milliseconds for sending NS messages, consistent with that on the Router.

Example
-------

# Set the interval for sending NS messages to 10000 milliseconds on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ns retrans-timer 10000

```