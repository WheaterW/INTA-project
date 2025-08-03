ipv6 nd autoconfig other-flag
=============================

ipv6 nd autoconfig other-flag

Function
--------



The **ipv6 nd autoconfig other-flag** command sets the "other configuration" flag (O flag) in the RA message, indicating whether hosts should use stateful autoconfiguration to obtain additional information (excluding addresses).

The **undo ipv6 nd autoconfig other-flag** command clears the "other configuration" flag (O flag) set in the RA message.



By default, the "other configuration" flag (O flag) is not set in the RA message.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd autoconfig other-flag**

**undo ipv6 nd autoconfig other-flag**


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

* If the O flag is set, the attached hosts should use stateful autoconfiguration to obtain additional configuration information (excluding IPv6 addresses). Additional configuration information includes the router lifetime, neighbor reachable time, retransmission interval, and PMTU.
* If the O flag is not set, the attached hosts should use stateless autoconfiguration to obtain additional configuration information. That is, the attached hosts obtain additional configuration information through the RA messages advertised by Routers.

**Prerequisites**



IPv6 has been enabled on the involved interface using the **ipv6 enable** command.



**Configuration Impact**

If the **ipv6 nd autoconfig managed-address-flag** command has been run to set the M flag of stateful autoconfiguration, the device enables hosts to obtain configurations other than IPv6 addresses through stateful autoconfiguration even if the **ipv6 nd autoconfig other-flag** command is not run.After the **display ipv6 interface** command is run, the command output shows that the attached hosts obtain IPv6 addresses through stateful autoconfiguration or stateless autoconfiguration.

**Precautions**

The interface on a Router cannot use stateful and stateless address autoconfiguration simultaneously to obtain additional configuration information (excluding IPv6 addresses).


Example
-------

# Set the "other configuration" flag (O flag) on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd autoconfig other-flag

```