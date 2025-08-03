peer capability-advertise (BGP multi-instance view) (group)
===========================================================

peer capability-advertise (BGP multi-instance view) (group)

Function
--------



The **peer capability-advertise** command enables the optional functions for BGP to advertise routes, including the route-refresh function, conventional functions, and 4-byte AS number function.

The **undo peer capability-advertise** command restores the default setting.



By default, the BGP route-refresh and 4-byte AS number functions are enabled, but conventional functions are disabled.


Format
------

**peer** *group-name* **capability-advertise** { **conventional** | **route-refresh** | **4-byte-as** }

**undo peer** *group-name* **capability-advertise** { **conventional** | **route-refresh** | **4-byte-as** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **conventional** | Indicates conventional functions.   * This parameter is valid only in the BGP view and BGP-VPN instance IPv4 address family view. * After conventional functions are enabled on a device, the device does not have extended functions, such as route-refresh and GR. | - |
| **route-refresh** | Indicates the route-refresh function. | - |
| **4-byte-as** | Indicates the 4-byte AS number function. | - |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BGP has many optional functions when advertising routes, including route-refresh, conventional functions, and 4-byte AS numbers. Using the **peer capability-advertise** command, you can enable or disable these functions as required.



**Precautions**



Enabling or disabling the route-refresh function, conventional function, or 4-byte AS number function causes the peer session to be disconnected and then re-established, leading to a temporary network interruption. Therefore, exercise caution when performing this operation.




Example
-------

# Configure a BGP device to advertise the route-refresh capability to its peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instanc a
[*HUAWEI-bgp-instance-a] group test
[*HUAWEI-bgp-instance-a] peer test capability-advertise route-refresh

```