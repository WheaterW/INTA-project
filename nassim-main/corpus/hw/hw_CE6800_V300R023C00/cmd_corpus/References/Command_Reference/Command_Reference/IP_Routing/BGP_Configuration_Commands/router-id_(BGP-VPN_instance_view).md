router-id (BGP-VPN instance view)
=================================

router-id (BGP-VPN instance view)

Function
--------



The **router-id** command configures a router ID in the BGP-VPN instance view.

The **undo router-id** command deletes the router ID configured in the BGP-VPN instance view.



By default, if no router ID is configured for the BGP VPN instance IPv4/IPv6 address family, the BGP router ID (if any) is used. If no BGP router ID exists, an interface IP address in the VPN instance is used.


Format
------

**router-id** { *router-id-value* | **auto-select** }

**undo router-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *router-id-value* | Specifies a router ID in the IPv4 address format. The router ID 0.0.0.0 is not supported. | The value is in dotted decimal notation. |
| **auto-select** | Automatically selects a router ID for the IPv4 or IPv6 address family of an existing BGP VPN instance. | - |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a router ID is configured in the BGP-VPN instance view, the router ID in the BGP-VPN instance view can be distinguished from the BGP router ID to meet the requirements of specific scenarios.The rules for selecting a router ID for a BGP-VPN instance are as follows:

* If loopback interfaces configured with IP addresses are bound to the VPN instance, the largest IP address among the IP addresses of the loopback interfaces is selected as the router ID.
* If no loopback interface configured with an IP address is bound to the VPN instance, the largest IP address among the other interfaces bound to the VPN instance is selected as the router ID, regardless of whether the interface is Up or Down.

**Precautions**

If a BGP VPN peer exists and none of the BGP VPN instance router ID, BGP VPN instance address family router ID, BGP router ID, and RM router ID is configured, the system may display a message indicating that the router ID will change to 0.0.0.0 when you delete the IP address of the last VPN interface.If two devices have different router IDs, an IBGP or EBGP connection can be established between them. If the router IDs are the same and the **router-id allow-same enable** command is run in the BGP view or BGP multi-instance view, an EBGP connection can be established.


Example
-------

# Configure a Router ID for the Device.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] router-id 10.2.3.4

```