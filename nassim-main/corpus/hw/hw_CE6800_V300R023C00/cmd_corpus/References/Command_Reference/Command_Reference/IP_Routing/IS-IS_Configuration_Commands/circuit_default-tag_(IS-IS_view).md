circuit default-tag (IS-IS view)
================================

circuit default-tag (IS-IS view)

Function
--------



The **circuit default-tag** command sets an administrative tag value for an interface on which IS-IS process is enabled.

The **undo circuit default-tag** command restores the default value.

The ipv6 circuit default-tag command sets an administrative tag for an IS-IS IPv6 interface.

The undo ipv6 circuit default-tag command restores the default value.



By default, the administrative tag value of all interfaces is 0.

By default, the administrative tag for an IS-IS IPv6 interface is 0.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

[ **ipv6** ] **circuit** **default-tag** *tag* [ **level-1** | **level-2** ]

**undo** [ **ipv6** ] **circuit** **default-tag** [ *tag* ] [ **level-1** | **level-2** ]

For CE6885-LL (low latency mode):

**circuit default-tag** *tag* [ **level-1** | **level-2** ]

**undo circuit default-tag** [ *tag* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tag* | Specifies the administrative tag carried in a route imported from an IPv6 interface. | The value is an integer ranging from 1 to 4294967295. |
| **level-1** | Indicates the administrative tag for a Level-1 IPv6 interface. | - |
| **level-2** | Indicates the administrative tag for a Level-2 IPv6 interface. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The administrative tag carries the administrative information about an IP address prefix. It is used to control the routes of different levels and routes imported from multiple areas. Administrative tags can advertise IP address prefixes in the IS-IS domain to control routes, simplifying management.After the **circuit default-tag** command is run, all routes of a specified IS-IS process carry an administrative tag value. The administrative tag value can be used to filter routes as needed.If level-1 and level-2 are not specified in the ipv6 **circuit default-tag** command, the ipv6 **circuit default-tag** command sets an administrative tag for all Level-1 and Level-2 IPv6 interfaces.The administrative tag for an interface is advertised along with routes.

* If the IS-IS cost type is narrow or narrow-compatible, the administrative tag of an interface is not advertised through an LSP.
* If the IS-IS cost type is wide, wide-compatible, or compatible, the administrative tag of an interface is advertised through an LSP.Before using the ipv6 **circuit default-tag** command in an IS-IS process, enable IPv6 in the IS-IS process. For details, see the **isis ipv6 enable** command.

**Prerequisites**

An IS-IS process has been started using the **isis** command.

**Precautions**

When the cost type of IS-IS is wide, wide-compatible, or compatible, the administrative tag value is advertised through an LSP. The cost type can be configured using the **cost-style** command.The administrative tag value configured using the **circuit default-tag** command is the global administrative tag value. The interface administrative tag configured using the **isis tag-value** command takes precedence over the global administrative tag.


Example
-------

# Set the administrative tag for Level-1 interfaces to 30.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] circuit default-tag 30 level-1

```