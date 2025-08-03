router-id
=========

router-id

Function
--------



The **router-id** command configures a Router ID for the Router. Each Router ID uniquely identifies one Device in an AS.

The **undo router-id** command deletes the Router ID configured for the Device.



By default, no BGP Router ID is configured, and the Router ID configured for the route management module through the router id command is used.


Format
------

**router-id** *ipv4-address*

**undo router-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies a router ID in the IPv4 address format. The router ID 0.0.0.0 is not supported. | The value is in dotted decimal notation. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **router-id** command is used to configure a router ID for the device. Each router ID identifies a device in an AS.

**Prerequisites**



The **bgp** command is run to enable BGP.



**Configuration Impact**

In the BGP view, changing the router ID or deleting the configured router ID resets the BGP session.

**Precautions**



By default, the router ID in the RM module is 0.0.0.0 when the device is not configured with any interface. For details about how to select a router ID, see the description of the **router id** command in the system view.If the **router-id** command is not run in the BGP view, the router ID in RM is used by default. When the IP address of the interface that is selected as the router ID is deleted or changed, router ID reselection is triggered. In addition, you need to run the **reset** command for the configuration to take effect. The router IDs of BGP private network instances, BGP public network instances, and RM instances are selected in descending order of priority.If BGP uses the router ID of the RM module and all public IP addresses are deleted, after the **reset** command is run, the BGP router ID changes to 0.0.0.0. As a result, the BGP peer relationship cannot be established.For a BGP public network peer, if the peer exists and neither the BGP router ID nor the router ID in the RM module is configured, when you delete the IP address of the last public network interface, the system may display a message indicating that the router ID will change to 0.0.0.0.If a BGP VPN peer exists and none of the BGP VPN instance router ID, BGP VPN instance address family router ID, BGP router ID, and RM router ID is configured, the system may display a message indicating that the router ID will change to 0.0.0.0 when you delete the IP address of the last VPN interface.If two devices have different router IDs, an IBGP or EBGP connection can be established between them. If the router IDs are the same and the **router-id allow-same enable** command is run in the BGP view, an EBGP connection can be established.




Example
-------

# Configure a Router ID for the Device.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] router-id 10.1.1.1

```