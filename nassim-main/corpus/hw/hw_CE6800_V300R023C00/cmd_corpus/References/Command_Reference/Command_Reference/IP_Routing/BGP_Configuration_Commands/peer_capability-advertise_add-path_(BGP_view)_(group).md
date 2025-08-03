peer capability-advertise add-path (BGP view) (group)
=====================================================

peer capability-advertise add-path (BGP view) (group)

Function
--------



The **peer capability-advertise add-path** command enables BGP Add-Path function.

The **undo peer capability-advertise add-path** command restores the default setting.



By default, Add-Path funcition is disabled.


Format
------

**peer** *group-name* **capability-advertise** **add-path** { **both** | **receive** | **send** }

**undo peer** *group-name* **capability-advertise** **add-path** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **add-path** | Indicates the Add-Path function. | - |
| **both** | Enables the RR to receive Add-Path routes from and send Add-Path routes to a specified IBGP peer. | - |
| **receive** | Enables the RR to receive Add-Path routes from a specified IBGP peer. | - |
| **send** | Enables the RR to send Add-Path routes to a specified IBGP peer. | - |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When BGP advertises routes, optional functions include Add-Path. Using the **peer capability-advertise add-path** command, you can enable or disable the ADD-PATH function as required.

**Precautions**

If the **peer capability-advertise add-path** command is run for a specified peer and the **peer advertise best-external** command is run for a specified peer group, the peer cannot inherit the function of the **peer advertise best-external** command configured for the peer group when the peer is added to the peer group.peer capability-advertise add-path takes effect only on the routes received from BGP peers.

* If the route received from a BGP peer is preferred, the local BGP routes imported using the network command are not preferred or advertised.
* If the local routes imported using the network command are preferred, the routes received from the BGP peer are not preferred. After the add-path command is run, the routes can be advertised.Enabling or disabling Add-Path will disconnect and then re-establish the peer session. This operation will cause temporary network interruption. Therefore, exercise caution when performing this operation.

Example
-------

# Enable the device to accept Add-Path routes from a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test capability-advertise add-path both

```