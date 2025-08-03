network-entity
==============

network-entity

Function
--------



The **network-entity** command configures a Network Entity Title (NET) for an IS-IS process.

The **undo network-entity** command deletes the NET configured for an IS-IS process.



By default, no NET is configured.


Format
------

**network-entity** *net-addr*

**undo network-entity** *net-addr*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *net-addr* | Specifies a NET. | The value is in the X...X.XXXX. XXXX.XXXX.00 format, in which the first "X...X" is the area address, the twelve Xs in the middle is the System ID of the device, and the 00 in the end is NSAP Selector (SEL). |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

NET is the special form of the network service access point (NSAP). IS-IS starts only when the NET is configured for the IS-IS process.NET consists of the following parts:

* Area ID, which is variable (1 to 13 bytes). The area IDs of the routers in the same area are identical.
* System ID (6 bytes) of this router. The system ID must be unique in the whole area and backbone area.
* Last byte (SEL), with value 00.In general, an IS-IS process is configured with only one NET. When you want to redefine an area, to combine it with other areas or divide it into sub-areas for example, you can configure the router with multiple NETs to ensure the correctness of routes.

**Prerequisites**

An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.

**Precautions**

An area address uniquely identifies an area in a routing domain. All devices in a Level-1 area must have the same area address. Devices in a Level-2 area can have different area addresses.The system ID must be unique in the entire area and backbone area.When configuring multiple NETs in the same process, ensure that they have the same system ID.After the undo network-entity command is run, NET-related configurations are deleted, and IS-IS functions become unavailable. Therefore, exercise caution when running this command.A maximum of three NETs can be configured in an IS-IS process.If different devices in the same IS-IS domain are configured with the same NET, a conflict occurs. Although the system automatically resolves the conflict, various problems (for example, service functions become invalid) occur. Therefore, you are not advised to configure the same network entity for devices in the same IS-IS domain.


Example
-------

# Set the NET to 10.0001.1010.1020.1030.00, in which the system ID is 1010.1020.1030 and area ID is 10.0001.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] network-entity 10.0001.1010.1020.1030.00

```