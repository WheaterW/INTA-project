isis cost (interface view)
==========================

isis cost (interface view)

Function
--------



The **isis cost** command sets a link cost for an IS-IS interface.

The **undo isis cost** command restores the default link cost.



By default, the link cost of IS-IS interfaces is 10.


Format
------

**isis cost** *cost* [ **level-1** | **level-2** ]

**isis process-id** *process-id* **cost** *cost* [ **level-1** | **level-2** ]

**undo isis cost** [ *cost* ] [ **level-1** | **level-2** ]

**undo isis process-id** *process-id* **cost** [ *cost* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cost** *cost* | Specifies a link cost for the SPF calculation. | * The value is an integer. The value range depends on the cost style. * When the cost style is narrow, narrow-compatible, or compatible, the value ranges from 1 to 63. * If the cost style is wide or wide-compatible, the value ranges from 1 to 16777214. * maximum: sets the link cost of an interface to 16777215. * The minimum value varies according to the interface type. When the interface type is Loopback, the minimum value is 0. For other interface types, the minimum value is 1.   This parameter can be configured only when the IS-IS cost style is wide or wide-compatible. After the cost of an interface is set to 16777215, the neighbor TLV generated on the link of the interface cannot be used for route calculation but can only be used to transmit TE information.  The cost style is configured using the cost-style command. |
| **level-1** | Sets the link cost value for the Level-1 interface. | - |
| **level-2** | Sets the link cost value for the Level-2 interface.  If Level-1 or Level-2 is not specified in the command, the link cost is set for Level-1 and Level-2 interfaces by default. | - |
| **process-id** *process-id* | Specifies the IID of an IS-IS multi-instance process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a large-scale network, there may be multiple valid routes to the same destination. IS-IS uses the SPF algorithm to calculate an optimal route and transmits traffic over the optimal route, which causes the following problems:

* All traffic is forwarded through the optimal path, which may cause load imbalance.
* If the optimal path on the network is intermittently disconnected, traffic is still forwarded along the optimal path before convergence, causing traffic loss.To solve the preceding problem, run the **isis cost** command to set different link costs for interfaces so that traffic can be forwarded along different physical links.

**Prerequisites**



IS-IS has been enabled on the interface using the **isis enable** command in the interface view.



**Configuration Impact**



If the link cost is changed, routes of the entire network are recalculated, and the traffic forwarding path changes accordingly.



**Precautions**



If both the **isis cost** and **circuit-cost** commands are run to set the link cost for an interface, the link cost set using the **isis cost** command takes effect.




Example
-------

# Set the link cost of the Level-2 link on 100GE1/0/1 to 5.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis cost 5 level-2

```