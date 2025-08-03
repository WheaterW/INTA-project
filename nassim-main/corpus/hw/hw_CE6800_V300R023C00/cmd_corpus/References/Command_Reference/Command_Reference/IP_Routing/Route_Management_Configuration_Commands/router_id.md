router id
=========

router id

Function
--------



The **router id** command sets the router ID in the RM module.

The **undo router id** command deletes the configured router ID.



By default, the router ID in the RM module is 0.0.0.0 if no IPv4 interface address is configured for a device.


Format
------

**router id** *router-id*

**undo router id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *router-id* | Specifies the router ID in the format of an IPv4 address. | The value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Some dynamic routing protocols, such as OSPF and BGP, require router IDs. If no router ID is specified when these routing protocols are started, the router ID in RM is used by default.The rules for selecting a router ID are as follows:

1. If the router ID is configured using the **router id** command, set the router ID based on the configuration result. If no router ID is configured, the router ID is selected according to the following rules:

* If loopback interfaces with IP addresses configured exist, the largest IP address of the loopback interfaces is selected as the router ID.
* If no loopback interface is configured with an IP address, the largest IP address among the IP addresses of other interfaces is selected as the router ID (regardless of the Up/Down status of the interface).

1. The router ID is reselected only when the IP address of the interface that is selected as the router ID is deleted or changed. The router ID is not reselected in the following cases:

* The interface is Down.
* A loopback interface address is configured after a non-loopback interface address is selected.
* A larger interface address is configured.You can run the **display router id** command to view the router ID. For a VPN instance, run the display router id vpn-instance <vpn-instance-name> command to check the router ID.

1. The route ID cannot be manually set in the VPN instance. Instead, the route ID can be selected from the interface addresses of the VPN instance according to the preceding two rules.
2. If active and standby s exist, the system backs up the router ID configured using the command and the router ID selected from interface addresses. During the active/standby switchover, the system checks the validity of the router ID selected from the addresses. If the router ID is invalid, the system reselects a router ID.The router ID configured in the protocol view takes precedence over the router ID configured in the system view. A protocol selects the router ID configured in the system view only when the protocol is not configured with its own router ID. If the router ID changes, you need to run the **reset** command to obtain the new router ID. For BGP, you need to run the reset bgp all command to obtain a new router ID.

**Precautions**



If the device is restarted in DB mode, the router ID saved in the DB table before the restart is used. If the device is restarted in CFG mode and the **router id** command is not configured on the device, the router ID of the interface that completes configuration restoration the earliest is used as the router ID after the restart.Description:To improve network stability, you are advised to manually configure the IP address of the loopback interface as the router ID.For a BGP public network peer, if the peer exists and neither the BGP router ID nor the router ID in the RM module is configured, when you delete the IP address of the last public network interface, the system may display a message indicating that the router ID will change to 0.0.0.0.If a BGP VPN peer exists and none of the BGP VPN instance router ID, BGP VPN instance address family router ID, BGP router ID, and RM router ID is configured, the system may display a message indicating that the router ID will change to 0.0.0.0 when you delete the IP address of the last VPN interface.




Example
-------

# Set the device ID in RM to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] router id 10.1.1.1

```