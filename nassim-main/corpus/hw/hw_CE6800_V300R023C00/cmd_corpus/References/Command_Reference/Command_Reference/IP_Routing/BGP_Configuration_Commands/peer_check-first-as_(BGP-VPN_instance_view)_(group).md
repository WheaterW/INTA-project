peer check-first-as (BGP-VPN instance view) (group)
===================================================

peer check-first-as (BGP-VPN instance view) (group)

Function
--------



The **peer check-first-as enable** command enables a device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.

The **peer check-first-as disable** command disables a device from checking the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.

The **undo peer check-first-as enable** command disables a device from checking the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.

The **undo peer check-first-as disable** command enables a device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.



By default, a device checks the first AS number in the AS\_Path attribute contained in the update messages received from all EBGP peers or peer groups.


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
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **peer check-first-as enable** command is run, BGP checks whether the first AS number in the AS\_Path carried in the Update messages sent by a specified EBGP peer group is the same as the AS where the EBGP peer group resides. If the two AS numbers are different, the update information is rejected. If the **peer check-first-as disable** command is run, BGP does not check the first AS number in the AS\_Path carried in the Update messages sent by a specified EBGP peer group. That is, BGP accepts the Update messages even if the first AS number is not the AS number of the EBGP peer group. This **undo** command deletes the configurations of a specified EBGP peer group and restores the default settings.The check on the first AS number in the AS\_Path attribute of each received Update message can be configured for a specified EBGP peer, the peer group that the EBGP peer belongs to, or the entire BGP process. The configuration takes effect in descending order of priority as follows: EBGP peer > peer group > entire BGP process.

**Follow-up Procedure**

Run the **refresh bgp** command if you want to check the received routes again.

**Precautions**

The **check-first-as** command applies to all EBGP peers, whereas the **peer check-first-as** command applies to a specified peer.


Example
-------

# Enable the device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test external
[*HUAWEI-bgp-instance-vpn1] peer test check-first-as enable

```