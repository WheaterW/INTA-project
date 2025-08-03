register-source (IPv6)
======================

register-source (IPv6)

Function
--------



The **register-source** command specifies an IPv6 address using which the source's designated router (DR) sends Register messages.

The **undo register-source** command restores the default setting.



By default, no IPv6 address is specified for the source's DR to send Register messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**register-source** *ipv6-address*

**undo register-source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies a global IPv6 unicast address using which the source's DR sends Register messages. | The address is in the format of X:X:X:X:X:X:X:X. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the source's DR uses more than one or a filtered out IPv6 address to send Register messages to the rendezvous point (RP), errors occur in the registration process and extra traffic occupies bandwidth on the network. To address this issue, run the **register-source** command to specify an IPv6 unicast address (a loopback interface's address is recommended) using which the source's DR sends Register messages.

**Prerequisites**

PIM-SM has been enabled on the interface of the IPv6 address to be specified by the ipv6-address parameter.

**Configuration Impact**

If the **register-source** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The command configuration is effective only when the interface of the specified IPv6 address is in the Up state.


Example
-------

# In the public network instance view, specify 2001:DB8:11::1 as the IPv6 address using which the source's DR sends Register message.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] register-source 2001:DB8:11::1

```