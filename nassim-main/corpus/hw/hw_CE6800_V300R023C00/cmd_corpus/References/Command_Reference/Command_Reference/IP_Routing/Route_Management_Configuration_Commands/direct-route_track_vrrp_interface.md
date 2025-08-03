direct-route track vrrp interface
=================================

direct-route track vrrp interface

Function
--------



The **direct-route track vrrp interface** command associates direct routes with a Virtual Router Redundancy Protocol (VRRP) backup group in the loopback interface view.

The **undo direct-route track vrrp interface** command deletes the association between direct routes and a VRRP group in the loopback interface view.



By default, direct routes are not associated with a VRRP group.


Format
------

**direct-route track vrrp interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id* **degrade-cost** *cost-value*

**undo direct-route track vrrp** [ **interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id* **degrade-cost** *cost-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of the interface on which a VRRP group is configured. | - |
| *interface-number* | Specifies the number of the interface on which a VRRP group is configured. | - |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| **degrade-cost** *cost-value* | Specifies a cost to be applied to IP direct routes when the associated VRRP group is in the Backup or Initialize state. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

Loopback interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Two CloudEdge-GWs in equipment room run VRRP, which is deployed on Eth-Trunk interfaces. Packets are transparently transmitted through an AGG-SW. The priority of network segment routes on loopback interfaces is associated with the VRRP status, and the priority of network segment routes on loopback interfaces of the CloudEdge-GW in the Backup state is low.

**Prerequisites**

VRRP has been configured on interfaces.

**Configuration Impact**

After the **direct-route track vrrp interface** command is run, the cost of IP direct routes is adjusted based on the VRRP group status, with details as follows:

* If the VRRP group status is Master, 0 is used as the cost of the IP direct routes. The IP direct routes have the highest priority.
* If the VRRP group status is Backup or Initialize, the cost-value specified in the command is used as the cost of the IP direct routes.

**Follow-up Procedure**

Configure a dynamic routing protocol to import the direct routes.

**Precautions**

You can run only one **direct-route track vrrp interface** command on a loopback interface. Before associating the direct routes with the VRRP group specified by vrid in another **direct-route track vrrp interface** command, you must delete the original **direct-route track vrrp interface** command.


Example
-------

# Associate the direct routes on loopback1 with a VRRP group.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] interface loopback 1
[*HUAWEI-loopback1] vrrp vrid 1 peer-ip 1.1.1.1
[*HUAWEI-loopback1] direct-route track vrrp interface 100GE1/0/1 vrid 1 degrade-cost 300

```