peer check-first-as (BGP-VPN instance view)
===========================================

peer check-first-as (BGP-VPN instance view)

Function
--------



The **peer check-first-as enable** command enables a device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer.

The **peer check-first-as disable** command disables a device from checking the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer.

The **undo peer check-first-as enable** command disables a device from checking the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer.

The **undo peer check-first-as disable** command enables a device to check the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer.



By default, a device checks the first AS number in the AS\_Path attribute contained in the update messages received from all EBGP peers or peer groups.


Format
------

**peer** *ipv4-address* **check-first-as** **enable**

**peer** *ipv4-address* **check-first-as** **disable**

**undo peer** *ipv4-address* **check-first-as** **enable**

**undo peer** *ipv4-address* **check-first-as** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


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
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 check-first-as enable

```