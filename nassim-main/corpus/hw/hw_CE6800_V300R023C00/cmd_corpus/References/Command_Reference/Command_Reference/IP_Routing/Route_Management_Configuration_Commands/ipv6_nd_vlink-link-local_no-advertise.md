ipv6 nd vlink-link-local no-advertise
=====================================

ipv6 nd vlink-link-local no-advertise

Function
--------



The **ipv6 nd vlink-link-local no-advertise** command disables a device from advertising an IPv6 NDP Vlink host route mapped to a link-local address.

The **undo ipv6 nd vlink-link-local no-advertise** command enables a device to advertise an IPv6 NDP Vlink host route mapped to a link-local address.



By default, the device is enabled to advertise an IPv6 NDP Vlink host route for a link-local address.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd vlink-link-local no-advertise**

**undo ipv6 nd vlink-link-local no-advertise**


Parameters
----------

None

Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **ipv6 nd vlink-link-local no-advertise** command disables a device from advertising an IPv6 NDP Vlink host route mapped to a link-local address.

**Prerequisites**

* If this function is to be enabled on a VLANIF interface, IPv6 has been enabled using the **ipv6 enable** command.
* If this function is to be enabled on a 100GE or Eth-Trunk sub-interface, IPv6 has been enabled using the **ipv6 enable** command. In addition, the sub-interface has been enabled to terminate single-tagged packets using the **dot1q termination vid** command.

**Precautions**

You must run the **ipv6 nd direct-route enable** command in the system view or interface view to advertise IPv6 NDP Vlink direct routes. Otherwise, the route summarization function does not take effect.Once the **undo ipv6 enable** command is run in the interface view to disable IPv6, the configuration of the **ipv6 nd vlink-link-local no-advertise** command is also deleted. Exercise caution when using the **undo ipv6 enable** command.


Example
-------

# Disable a device from advertising an IPv6 NDP Vlink host route mapped to a link-local address in the VLANIF interface view.
```
<HUAWEI> system-view
[~HUAWEI] vlan 200
[*HUAWEI-Vlan200] quit
[*HUAWEI] interface vlanif 200
[*HUAWEI-Vlanif200] ipv6 enable
[*HUAWEI-Vlanif200] ipv6 nd direct-route enable
[*HUAWEI-Vlanif200] ipv6 nd vlink-link-local no-advertise

```