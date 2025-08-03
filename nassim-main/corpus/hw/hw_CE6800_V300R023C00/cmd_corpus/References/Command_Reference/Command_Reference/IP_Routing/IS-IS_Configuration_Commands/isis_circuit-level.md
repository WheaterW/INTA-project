isis circuit-level
==================

isis circuit-level

Function
--------



The **isis circuit-level** command sets a link type for an interface on a Level-1-2 router that runs IS-IS.

The **undo isis circuit-level** command restores the default setting.



By default, the link type of an interface on a Level-1-2 router that runs IS-IS is Level-1-2, and both Level-1 and Level-2 adjacencies can be established on the interface.


Format
------

**isis circuit-level** [ **level-1** | **level-2** | **level-1-2** ]

**undo isis circuit-level**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Indicates the Level-1 link type. After the parameter is configured, the interface can set up only Level-1 adjacencies. | - |
| **level-2** | Indicates the Level-2 link type. After the parameter is configured, the interface can set up only Level-2 adjacencies. | - |
| **level-1-2** | Indicates the Level-1-2 link type. After the parameter is configured, the interface can set up both Level-1 and Level-2 adjacencies. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an adjacency is established between a Level-1-2 router and a remote device, the Level-1-2 router sends and receives both Level-1 and Level-2 Hello packets, wasting bandwidth and memory resources. To solve this problem, run the **isis circuit-level** command to set a specified link type for an interface on the Level-1-2 router.

**Prerequisites**

IS-IS has been enabled using the **isis enable** command in the interface view.

**Configuration Impact**

Network flapping may occur if the link type of an IS-IS interface is changed during network operation. Therefore, setting a link type when configuring IS-IS is recommended.

**Precautions**

The link type takes effect only when the system type of IS-IS is Level-1-2. Otherwise, the level defined by the **is-level** command is used.


Example
-------

# Set the link type of 100GE1/0/1 that is connected to a non-backbone device in the same area to Level-1 to prevent 100GE 1/0/1 from receiving and sending Level-2 Hello packets.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis circuit-level level-1

```