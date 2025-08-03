ipv6 nd ra-unicast send enable
==============================

ipv6 nd ra-unicast send enable

Function
--------



The **ipv6 nd ra-unicast send enable** command enables a routing device to send unicast RA messages in response to RS messages it receives on an interface.

The **undo ipv6 nd ra-unicast send enable** command restores the default configuration.



By default, a routing device does not send unicast RA messages in response to RS messages it receives on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra-unicast send enable**

**undo ipv6 nd ra-unicast send enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a routing device is connected to a host through a Layer 2 forwarding device, the host obtains the prefix list and other configurations from a received RA message. By default, a routing device does not send RA messages. You can run the **ipv6 nd ra halt disable** command to enable a routing device to send multicast RA messages. If a Layer 2 forwarding device cannot correctly forward multicast RA messages, you can run the **ipv6 nd ra-unicast send enable** command to enable a routing device to send a unicast RA message in response to an RS message received on an interface.Enabling a routing device to send unicast RA messages takes precedence over enabling a routing device to send multicast RA messages.


Example
-------

# Enable a routing device to send unicast RA messages in response to RS messages it receives on an interface.
```
HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ra-unicast send enable

```