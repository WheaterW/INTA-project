peer check-first-as (BGP-VPN instance IPv6 address family view) (group)
=======================================================================

peer check-first-as (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer check-first-as enable** command enables a device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.

The **peer check-first-as disable** command disables a device from checking the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.

The **undo peer check-first-as enable** command disables a device from checking the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.

The **undo peer check-first-as disable** command enables a device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.



By default, a device checks the first AS number in the AS\_Path attribute contained in the update messages received from all EBGP peers or peer groups.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **check-first-as** **enable**

**peer** *group-name* **check-first-as** **disable**

**undo peer** *group-name* **check-first-as** **enable**

**undo peer** *group-name* **check-first-as** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **peer check-first-as enable** command is run, BGP checks whether the first AS number in the AS\_Path carried in the Update messages sent by a specified EBGP peer group is the same as the AS where the EBGP peer group resides. If the two AS numbers are different, the update information is rejected. If the **peer check-first-as disable** command is run, BGP does not check the first AS number in the AS\_Path carried in the Update messages sent by a specified EBGP peer group. That is, BGP accepts the Update messages even if the first AS number is not the AS number of the EBGP peer group. This **undo** command deletes the configurations of a specified EBGP peer group and restores the default settings.The check on the first AS number in the AS\_Path attribute of each received Update message can be configured for a specified EBGP peer, the peer group that the EBGP peer belongs to, or the entire BGP process. The configuration takes effect in descending order of priority as follows: EBGP peer > peer group > entire BGP process.

**Follow-up Procedure**



After the check function is enabled, to enable the device to perform a check on received update messages, run the **refresh bgp** command.



**Precautions**



The **check-first-as** command applies to all EBGP peers, whereas the **peer check-first-as** command applies to a specified peer.




Example
-------

# Enable the device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpn1] group test external
[*HUAWEI-bgp-6-vpn1] peer test as-number 200
[*HUAWEI-bgp-6-vpn1] peer test check-first-as enable

```