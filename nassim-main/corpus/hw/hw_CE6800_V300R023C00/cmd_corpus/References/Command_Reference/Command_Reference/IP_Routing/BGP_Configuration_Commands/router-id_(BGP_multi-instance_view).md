router-id (BGP multi-instance view)
===================================

router-id (BGP multi-instance view)

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
| *ipv4-address* | Specifies the IPv4 address of a peer. The router ID 0.0.0.0 is not supported. | It is in dotted decimal notation. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **router-id** command is used to specify a router ID for a device. Each router ID identifies a device in an AS.You can configure automatic router ID selection for a BGP-VPN instance to distinguish the router ID of the BGP-VPN instance from the BGP router ID. For more information about the router ID of a BGP-VPN instance, see router-id (BGP-VPN instance IPv4 address family view).



**Configuration Impact**



When you change the router ID of a BGP-VPN instance IPv4 address family or delete a configured router ID, the BGP session will be reset if there are established BGP sessions in the BGP-VPN instance IPv4 address family. Exercise caution when running this command.



**Precautions**



By default, the router ID in the RM module is 0.0.0.0 when the device is not configured with any interface. For details about how to select a router ID, see the description of the **router id** command in the system view.If the **router-id** command is not run in the BGP multi-instance view, the router ID in RM is used by default. When the IP address of the interface that is selected as the router ID is deleted or changed, router ID reselection is triggered. In addition, you need to run the **reset** command for the configuration to take effect.When a BGP instance uses the router ID of the RM module by default and all public IP addresses are deleted, running the **reset** command changes the BGP router ID to 0.0.0.0. As a result, the BGP peer relationship cannot be established.If two devices have different router IDs, an IBGP or EBGP connection can be established between them. If the router IDs are the same and the **router-id allow-same enable** command is run in the BGP multi-instance view, an EBGP connection can be established.




Example
-------

# Configure a Router ID for the Device.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] router-id 10.1.1.1

```