ipv6 direct-route track vrrp6
=============================

ipv6 direct-route track vrrp6

Function
--------



The **ipv6 direct-route track vrrp6** command associates IPv6 direct routes with a Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group.

The **undo ipv6 direct-route track vrrp6** command dissociates IPv6 direct routes from a VRRP6 backup group.



By default, IPv6 direct routes are not associated with any VRRP6 backup group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 direct-route track vrrp6 vrid** *virtual-router-id* **degrade-cost** *cost-value*

**undo ipv6 direct-route track vrrp6** [ **vrid** *virtual-router-id* **degrade-cost** *cost-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **degrade-cost** *cost-value* | Specifies a cost to be applied to IPv6 direct routes when the associated VRRP6 backup group is in Backup or Initialize status. | The value is an integer ranging from 1 to 4294967295. |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP6 backup group. | The value is an integer ranging from 1 to 255. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a VRRP6 backup group functions as a gateway, the forwarding path of user-to-network is determined by the state of the VRRP6 backup group, and the forwarding path of network-to-user traffic is selected by a dynamic routing protocol. As a result, user-to-network and network-to-user traffic may be transmitted over different paths. When a firewall needs to be deployed on the VRRP6 backup group to increase security, network-to-user traffic cannot pass through the firewall because of the inconsistent forwarding paths of network-to-user and user-to-network traffic. To address this problem, run the **ipv6 direct-route track vrrp6** command to adjust the cost of IPv6 direct routes based on the VRRP6 backup group status, and configure a dynamic routing protocol to import the IPv6 direct routes.

**Prerequisites**

VRRP6 has been configured on the interface.

**Configuration Impact**

After the command is run, the cost of IPv6 direct routes is adjusted based on the VRRP6 backup group status, with details as follows:

* If the VRRP6 backup group status is Master, the default value 0 (the highest priority) is used as the cost of the IPv6 direct routes.
* If the VRRP6 backup group status is Backup or Initialize, the cost-value specified in the command is used as the cost of the IPv6 direct routes.

**Follow-up Procedure**

Configure a dynamic routing protocol to import the IPv6 direct routes.

**Precautions**

The IPv6 direct routes on an interface can be associated with only one VRRP6 backup group. To change the associated VRRP6 backup group, dissociate the IPv6 direct routes from the original VRRP6 backup group first.


Example
-------

# Associate the IPv6 direct routes on 100GE1/0/1 with a VRRP6 backup group.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 direct-route track vrrp6 vrid 1 degrade-cost 300

```