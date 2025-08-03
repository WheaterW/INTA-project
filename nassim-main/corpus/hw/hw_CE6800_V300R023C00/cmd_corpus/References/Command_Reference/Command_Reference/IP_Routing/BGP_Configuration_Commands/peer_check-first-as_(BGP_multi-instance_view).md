peer check-first-as (BGP multi-instance view)
=============================================

peer check-first-as (BGP multi-instance view)

Function
--------



The **peer check-first-as enable** command enables a device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer.

The **peer check-first-as disable** command disables a device from checking the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer.

The **undo peer check-first-as enable** command disables a device from checking the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer.

The **undo peer check-first-as disable** command enables a device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer.



By default, a device checks the first AS number in the AS\_Path attribute contained in the update messages received from all EBGP peers or peer groups.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **check-first-as** **enable**

**peer** { *ipv4-address* | *ipv6-address* } **check-first-as** **disable**

**undo peer** { *ipv4-address* | *ipv6-address* } **check-first-as** **enable**

**undo peer** { *ipv4-address* | *ipv6-address* } **check-first-as** **disable**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **check-first-as** **enable**

**peer** *ipv4-address* **check-first-as** **disable**

**undo peer** *ipv4-address* **check-first-as** **enable**

**undo peer** *ipv4-address* **check-first-as** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **peer** *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **peer check-first-as enable** command is run, BGP checks whether the first AS number in the AS\_Path list carried in the Update message sent by a specified EBGP peer is the AS where the EBGP peer resides. If the two AS numbers are different, the Update message is denied. If the **peer check-first-as disable** command is run, BGP does not check the first AS number in the AS\_Path list carried in the Update message sent by a specified EBGP peer. That is, BGP accepts the Update message even if the first AS number is not the AS number of the EBGP peer. This **undo** command deletes the configuration of the specified EBGP peer and restores the default configuration.The check on the first AS number in the AS\_Path attribute of each received Update message can be configured for a specified EBGP peer, the peer group that the EBGP peer belongs to, or the entire BGP process. The configuration takes effect in descending order of priority as follows: EBGP peer > peer group > entire BGP process.

**Follow-up Procedure**

Run the **refresh bgp** command if you want to check the received routes again.

**Precautions**

The **check-first-as** command applies to all EBGP peers, whereas the **peer check-first-as** command applies to a specified peer.


Example
-------

# Enable the device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 check-first-as enable

```