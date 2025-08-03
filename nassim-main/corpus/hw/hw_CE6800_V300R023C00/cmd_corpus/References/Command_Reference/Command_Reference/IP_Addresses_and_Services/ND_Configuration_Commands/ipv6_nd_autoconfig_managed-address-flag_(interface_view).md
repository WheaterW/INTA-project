ipv6 nd autoconfig managed-address-flag (interface view)
========================================================

ipv6 nd autoconfig managed-address-flag (interface view)

Function
--------



The **ipv6 nd autoconfig managed-address-flag** command sets the "managed address configuration" flag (M flag) in the RA message, indicating whether hosts should use stateful autoconfiguration to obtain addresses.

The **undo ipv6 nd autoconfig managed-address-flag** command clears the "managed address configuration" flag (M flag) set in the RA message.



By default, the "managed address configuration" flag (M flag) is not set in the RA message.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd autoconfig managed-address-flag**

**undo ipv6 nd autoconfig managed-address-flag**


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

**Usage Scenario**

* If the M flag is set, the attached hosts should use stateful autoconfiguration to obtain IPv6 addresses.
* If the M flag is not set, the attached hosts should use stateless autoconfiguration to obtain IPv6 addresses. For example, the attached hosts obtain IPv6 prefixes through the RA messages advertised by Routers.

**Prerequisites**



IPv6 has been enabled on the involved interface using the **ipv6 enable** command.



**Configuration Impact**

If the **ipv6 nd autoconfig managed-address-flag** command is run, hosts can obtain additional configuration information (excluding IPv6 addresses) though the **ipv6 nd autoconfig other-flag** command is not run. Additional configuration information includes the router lifetime, time period for the neighbor to keep reachable, retransmission interval, and PMTU.To check whether the attached hosts obtain IPv6 addresses through stateful autoconfiguration or stateless autoconfiguration, run the **display ipv6 interface** command.

**Precautions**

The interface on a Router cannot use stateful address autoconfiguration and stateless address autoconfiguration simultaneously to obtain IPv6 addresses.


Example
-------

# Set the "managed address configuration" flag (M flag) on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd autoconfig managed-address-flag

```