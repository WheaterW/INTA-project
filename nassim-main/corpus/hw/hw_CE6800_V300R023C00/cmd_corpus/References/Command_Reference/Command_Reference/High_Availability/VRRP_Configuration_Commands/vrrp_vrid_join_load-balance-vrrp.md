vrrp vrid join load-balance-vrrp
================================

vrrp vrid join load-balance-vrrp

Function
--------



The **vrrp vrid join load-balance-vrrp** command adds a specified VRRP backup group to a load-balance redundancy group (LBRG).

The **undo vrrp vrid join load-balance-vrrp** command deletes a specified VRRP backup group from an LBRG.



By default, no VRRP backup group is added to an LBRG.


Format
------

**vrrp vrid** *virtual-router-id* **join** **load-balance-vrrp** **vrid** *lb-vrid-value*

**undo vrrp vrid** *virtual-router-id* **join** **load-balance-vrrp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vrid** *virtual-router-id* | Specifies the ID of a member VRRP group. | The value is an integer ranging from 1 to 255. |
| **vrid** *lb-vrid-value* | Specifies the ID of an LBRG. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To implement single-gateway load balancing, run the vrrp vrid join load-balance-vrrp command to add a specified VRRP backup group to an LBRG. The LBRG uses the virtual MAC addresses of the VRRP backup groups in it to respond to different users' ARP request packets destined for virtual IP addresses. The master device of a specified VRRP backup group forwards the traffic of a specified user, implementing load balancing.

**Prerequisites**

The following operations have been performed:Run the vrrp vrid virtual-router-id [ virtual-ip virtual-address ] command to create a VRRP backup group.

* If you use the VRRP backup group as an LBRG, you must assign a virtual IP address to the VRRP backup group.
* If you use the VRRP backup group as an LBRG member group, you do not need to assign a virtual IP address to the VRRP backup group.Run the **vrrp vrid virtual-router-id load-balance** command to create an LBRG.

Example
-------

# Create an LBRG and add a VRRP backup group to the LBRG.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.10.10.10
[*HUAWEI-100GE1/0/1] vrrp vrid 1 load-balance
[*HUAWEI-100GE1/0/1] vrrp vrid 2
[*HUAWEI-100GE1/0/1] vrrp vrid 2 join load-balance-vrrp vrid 1

```