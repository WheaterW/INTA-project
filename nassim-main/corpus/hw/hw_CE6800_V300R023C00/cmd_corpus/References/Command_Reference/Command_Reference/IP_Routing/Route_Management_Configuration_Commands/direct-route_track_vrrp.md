direct-route track vrrp
=======================

direct-route track vrrp

Function
--------



The **direct-route track vrrp** command associates direct routes with a Virtual Router Redundancy Protocol (VRRP) backup group.

The **undo direct-route track vrrp** command dissociates direct routes from a VRRP group.



By default, no direct routes are associated with a VRRP group.


Format
------

**direct-route track vrrp vrid** *virtual-router-id* **degrade-cost** *cost-value*

**undo direct-route track vrrp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **degrade-cost** *cost-value* | Specifies the cost of a direct route that the virtual IP network segment generates when the VRRP status is Backup or Initialize. | The value is an integer ranging from 1 to 4294967295. |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a VRRP group functions as a user gateway, user-to-network traffic and network-to-user traffic may travel through different paths. This case occurs because user-to-network traffic traverses the master device in the VRRP group, but network-to-user traffic is transmitted through a path that a dynamic routing protocol selects. When a firewall is configured for the VRRP group to improve network security, path inconsistency causes the firewall to block both user-to-network and network-to-user traffic. Additionally, path inconsistency increases the difficulty and cost in traffic policing and accounting. To resolve problems caused by path inconsistency, run the **direct-route track vrrp** command to associate direct routes with a VRRP group. The association allows devices to modify their direct route costs based on the VRRP status. To change the path that a dynamic routing protocol selects based on the VRRP status, configure a dynamic routing protocol to import direct routes.

**Prerequisites**

VRRP has been configured on the interface.

**Configuration Impact**

After the **direct-route track vrrp** command is run, the VRRP-enabled device modifies the cost of direct routes that the virtual IP network segment generates based on the VRRP status:

* When the VRRP status is Master, the direct route cost is set to the default value 0. The IP direct routes have the highest priority.
* When the VRRP status is Backup or Initialize, the value specified in cost-value is used as the direct route cost.

**Follow-up Procedure**

Configure a dynamic routing protocol to import direct routes.

**Precautions**

Direct routes on an interface can be associated with only one VRRP group. To associate the direct routes with another VRRP group, delete the original direct-route track vrrp configuration.


Example
-------

# Associate the direct routes of 100GE1/0/1 with a VRRP group.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1
[*HUAWEI-100GE1/0/1] direct-route track vrrp vrid 1 degrade-cost 300

```