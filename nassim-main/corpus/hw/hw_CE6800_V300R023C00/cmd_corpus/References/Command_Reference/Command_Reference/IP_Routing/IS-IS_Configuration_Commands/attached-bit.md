attached-bit
============

attached-bit

Function
--------



The **attached-bit avoid-learning** command prevents an IS-IS Level-1 router from generating a default route after it receives LSPs carrying Attached (ATT) bit 1.

The **undo attached-bit avoid-learning** command restores the default configuration.

The **attached-bit advertise** command configures a rule for setting the Attached (ATT) bit in LSPs.

The **undo attached-bit advertise** command restores the default configuration.



By default, an IS-IS Level-1 router generates a default route only after it receives LSPs carrying ATT bit 1.

By default, the Level-1-2 router sets the ATT bit in LSPs using the default rule.




Format
------

**attached-bit** { { **advertise** { **always** | **never** } } | **avoid-learning** }

**undo attached-bit advertise**

**undo attached-bit avoid-learning**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **always** | Indicates that the ATT bit is set to 1. | - |
| **never** | Indicates that the ATT bit remains at 0. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An ATT bit is a field in LSPs. An ATT bit identifies whether a Level-1 area is attached to other areas. A Level-1-2 router sets the ATT bit to 1 to notify the routers in the Level-1 area of its attachment to a Level-2 backbone area. After a Level-1 router receives the LSPs carrying the ATT bit 1 from the Level-1-2 router, the Level-1 router generates a route with the same destination address as the default route of the Level-1-2 router. Traffic can be forwarded along this route.To prevent the Level-1 router from advertising the default route when the ATT bit is set to 1, run the **attached-bit avoid-learning** command.To prevent the Level-1 router from advertising default routes to the routing table, use either of the following methods:

* Run the **attached-bit advertise never** command on the Level-1-2 router to disable the router from sending LSPs with the ATT bit 1.
* Run the **attached-bit avoid-learning** command on the Level-1 router that is connected to the Level-1-2 router.The difference between the preceding commands lies in that the **attached-bit avoid-learning** command applies to a specified device.

**Prerequisites**



An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.



**Precautions**

Default resetting rule:

* Although the ATT bit is defined in both Level-1 and Level-2 LSPs, it is set only in Level-1 LSPs. In addition, only Level-1-2 routers can set the ATT bit. Therefore, this command takes effect only on Level-1-2 routers.
* The ATT bit is added to the Level-1 LSP only when the Level-2 area addresses in the LSDB contain the area addresses that do not exist in the Level-1 area.


Example
-------

# Disable IS-IS-enabled router from advertising default routes to a routing table when the ATT bit is set to 1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] attached-bit avoid-learning

```

# Enable a Level-1-2 router to set the ATT bit to 1 in the LSPs to be sent in IS-IS process 1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] attached-bit advertise always

```