mac-ip route generate-mac
=========================

mac-ip route generate-mac

Function
--------



The **mac-ip route generate-mac** command enables the function to generate MAC entries based on MAC/IP routes.

The **undo mac-ip route generate-mac** command disables the function.



By default, the function to generate MAC entries based on MAC/IP routes is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-ip route generate-mac**

**undo mac-ip route generate-mac**


Parameters
----------

None

Views
-----

EVPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In EVPN VXLAN scenarios, if the remote gateway is configured not to advertise MAC routes (mac-route no-advertise) or is configured not to generate MAC routes (**local mac-only-route no-generate**), the local gateway cannot generate MAC entries by default. To guide Layer 2 traffic forwarding, run the **mac-ip route generate-mac** command on the local gateway to enable MAC address entry generation based on MAC/IP routes.

**Precautions**

After the **mac-ip route generate-mac** command is run, if the remote gateway advertises both MAC/IP routes and MAC routes, the local gateway generates MAC entries based on only MAC routes.


Example
-------

# Enable the function to generate MAC address entries based on MAC/IP routes.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] vxlan vni 20
[*HUAWEI-bd10] evpn
[*HUAWEI-bd10-evpn] mac-ip route generate-mac

```