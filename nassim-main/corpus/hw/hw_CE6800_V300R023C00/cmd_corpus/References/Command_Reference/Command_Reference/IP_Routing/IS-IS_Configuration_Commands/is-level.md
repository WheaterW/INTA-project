is-level
========

is-level

Function
--------



The **is-level** command configures a level for an IS-IS device.

The **undo is-level** command restores the default value.



By default, the level of an IS-IS device is Level-1-2.


Format
------

**is-level** { **level-1** | **level-1-2** | **level-2** }

**undo is-level**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Sets the level of the device to Level-1. It calculates only intra-area routes and maintains the LSDBs of Level-1. | - |
| **level-1-2** | Sets the level of the device to Level-1-2. It calculates both Level-1 and Level-2 routes and maintains the LSDBs of Level-1 and Level-2. | - |
| **level-2** | Sets the level of the device to Level-2. It calculates Level-2 routes and maintains the LSDBs of Level-2. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To support a network with a large number of routes, IS-IS uses a two-level structure in an IS-IS domain. IS-IS devices are classified into the following levels:

* Level-1 device: A Level-1 device manages intra-area routing. It establishes neighbor relationships with only Level-1 and Level-1-2 devices in the same area. Level-1 devices can be connected to other areas through Level-1-2 devices only.
* Level-2 device: A Level-2 device manages intra-area routing. It establishes neighbor relationships with Level-2 devices in the same area and Level-1-2 devices in other areas only. All Level-2 devices form the backbone network of the routing domain. They are responsible for communications between areas. The Level-2 devices in the routing domain must be reachable, and no device of other levels is deployed between every two Level-2 devices.
* Level-1-2 device: A Level-1-2 device can establish Level-1 neighbor relationships with Level-1 devices and Level-1-2 devices in the same area. It can also establish Level-2 neighbor relationships with Level-2 devices and Level-1-2 devices in other areas.In most cases, Level-1 devices are located within an area, Level-2 devices are located between areas, and Level-1-2 devices are located between Level-1 devices and Level-2 devices.The level of an IS-IS device and of an interface determine the level of a neighbor relationship. By default, neighbor relationships between two Level-1-2 devices are Level-1 and Level-2. To establish a Level-1 or Level-2 neighbor relationship, run the **isis circuit-level** command to modify the level of interfaces.If only one area exists, setting the level of devices to Level-1 or Level-2 is recommended to prevent devices from maintaining two LSDBs that are the same. On an IP network, setting the level of all devices to Level-2 for future extension is recommended.The **is-level** command is applicable to all topologies of the IS-IS process.

**Prerequisites**

An IS-IS process has been created using the **isis** command in the system view.

**Configuration Impact**

If the levels of IS-IS devices are changed during network operation, the IS-IS process will be restarted and IS-IS neighbor relationships will be disconnected. Setting the levels of Routers when configuring IS-IS is recommended.

**Precautions**

If neither Level-1 nor Level-2 is specified, the device works at Level-1-2. That is, the device calculates Level-1 and Level-2 routes and maintains Level-1 and Level-2 LSDBs.


Example
-------

# Set the level of the device to Level-1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] is-level level-1

```