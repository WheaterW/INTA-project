ipv6 nd direct-route prefix
===========================

ipv6 nd direct-route prefix

Function
--------



The **ipv6 nd direct-route prefix** command sets a route summarization address and the length of a route summarization prefix for IPv6 NDP Vlink direct routes.

The **undo ipv6 nd direct-route prefix** command restores the default configuration.



By default, the length of the route summarization prefix for IPv6 NDP Vlink direct routes is 128 bits.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd direct-route prefix** *ipv6-address* [ *prefix-length* ]

**undo ipv6 nd direct-route prefix** *ipv6-address* *prefix-length*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies a route summarization address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the length of a route summarization prefix, which cannot be less than the length of an interface IPv6 address prefix. | The value is an integer ranging from 1 to 128. The default value is 128. |



Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **ipv6 nd direct-route prefix** command sets a route summarization address and the length of a route summarization prefix for IPv6 NDP Vlink direct routes.

**Prerequisites**

* If this function is to be enabled on a VLANIF or VBDIF interface, IPv6 has been enabled using the **ipv6 enable** command.
* If this function is to be enabled on a 100GE or Eth-Trunk sub-interface, IPv6 has been enabled using the **ipv6 enable** command. In addition, the sub-interface has been enabled to terminate single-tagged packets using the **dot1q termination vid** command.

**Precautions**

ND entries corresponding to IPv6 addresses dynamically generated on interfaces do not support IPv6 NDP Vlink direct route aggregation.


Example
-------

# Set the route summarization address to 2001:db8::1 and the length of a route summarization prefix for IPv6 NDP Vlink direct routes to 25 bits.
```
<HUAWEI> system-view
[~HUAWEI] vlan 200
[*HUAWEI-Vlan200] quit
[*HUAWEI] interface vlanif 200
[*HUAWEI-Vlanif200] ipv6 enable
[*HUAWEI-Vlanif200] ipv6 address 2001:db8::1 24
[*HUAWEI-Vlanif200] ipv6 nd direct-route enable
[*HUAWEI-Vlanif200] ipv6 nd direct-route prefix 2001:db8::1 25

```