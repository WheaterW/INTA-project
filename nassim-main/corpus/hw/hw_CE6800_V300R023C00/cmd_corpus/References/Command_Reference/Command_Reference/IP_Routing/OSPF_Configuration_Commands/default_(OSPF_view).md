default (OSPF view)
===================

default (OSPF view)

Function
--------



The **default** command configures default parameters for OSPF to import external routes. The parameters include the cost, type (Type 1 or Type 2), and tag.

The **undo default** command restores the default setting.



By default, the default cost of the external routes is 1; the type of the imported external routes is Type 2; the default tag value is 1.


Format
------

**default** { **cost** { *costvalue* | **inherit-metric** } | **tag** *tagvalue* | **type** *typevalue* } \*

**undo default** { **cost** [ { *costvalue* | **inherit-metric** } ] | **tag** [ *tagvalue* ] | **type** [ *typevalue* ] } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cost** *costvalue* | Specifies the default cost of the external routes imported by OSPF. | The value is an integer ranging from 0 to 16777214. The default value is 1. |
| **inherit-metric** | Indicates that the cost of the imported route is the one carried in the route. If no cost is specified, the default cost set using the default command is used. | - |
| **tag** *tagvalue* | Specifies the tag of the external routes. | The value is an integer ranging from 0 to 4294967295. The default value is 1. |
| **type** *typevalue* | Specifies the type of the external routes. | The value is 1 or 2.   * 1: Type 1 external route * 2: Type 2 external route   The default value is 2. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The imported external routes carry various parameters that can change the priorities and next hops of those routes in the OSPF routing table.By setting default parameters for OSPF to import external routes, you can control OSPF route selection.The route tag is used to identify protocol-related information. For example, it can be used to differentiate AS numbers when OSPF receives BGP routes. In addition, configuring tag can filter OSPF routes carrying tags.

**Precautions**

The **default tag** command takes effect only for the OSPF process on the public network or the OSPF VPN process for which the **vpn-instance-capability simple** command is run. If the **vpn-instance-capability simple** command is not run for an OSPF VPN process, the tag value configured using the **route-tag** command takes effect.You can run the following commands to set the cost of the imported routes. The priorities of the imported routes are in descending order.

* Run the **apply cost** command to set the route cost.
* Run the import-route (OSPF) command to set the cost of the imported route.
* Run the default (OSPF) command to set the default cost for imported routes.The default (OSPF) command has the lowest priority. Therefore, when configuring this command, check whether other commands are configured. If other commands are configured, the function of this command does not take effect.

Example
-------

# Set the default values of the cost, type, and tag.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] default cost 10 tag 100 type 2

```