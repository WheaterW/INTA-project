ipv6 nd ra
==========

ipv6 nd ra

Function
--------



The **ipv6 nd ra** command sets the interval for sending RA messages.

The **undo ipv6 nd ra** command restores the default setting.



By default, The maximum interval is 600s. For the minimum interval, if the maximum interval for advertising RA packets is 9s or greater, it is 1/3 of the maximum interval. In other cases, the default minimum interval is the same as the maximum interval for advertising RA packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra** { **max-interval** *maximum-interval* | **min-interval** *minimum-interval* }

**undo ipv6 nd ra** { **max-interval** | **min-interval** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **max-interval** *maximum-interval* | Specifies the maximum interval for the device to advertise RA messages. | The value is an integer ranging from 4 to 1800, in seconds. The maximum interval cannot be shorter than 4/3 of the minimum interval. |
| **min-interval** *minimum-interval* | Specifies the minimum interval for the device to send RA messages. | The value is an integer ranging from 3 to 1350, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A Router periodically sends RA messages. An RA message carries both the IP address prefix and the flag of stateful address autoconfiguration.You can run the **ipv6 nd ra** command to change the interval for sending RA messages.

**Prerequisites**



Before running the **ipv6 nd ra** command to set the interval for sending RA messages, you need to run the **ipv6 enable** command in the interface view to enable the IPv6 function on the interface.



**Configuration Impact**

Running the **ipv6 nd ra** command will change the number of NS messages that are sent when DAD is performed. Therefore, you are recommended to use the default interval.The **ipv6 nd ra** command is circular in nature. That is, if the intervals set two times are different, the latest setting takes effect.

**Precautions**

Commonly, the interval for sending RA messages must be shorter than or equal to lifetime of the RA messages. You can run the ipv6 nd ra router-lifetime to change the lifetime of the RA messages.The actual interval for sending RA messages is a random value between max-interval and min-interval.


Example
-------

# Set the minimum interval for sending RA messages to 300 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ra min-interval 300

```

# Set the maximum interval for sending RA messages to 1000 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ra max-interval 1000

```