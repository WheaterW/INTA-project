filter-policy (RIP view)
========================

filter-policy (RIP view)

Function
--------



The **filter-policy export** command configures a global, protocol, or interface export policy so that only the routes that match the export policy can be added to the routing table and advertised through update packets.

The **undo filter-policy export** command disables route filtering.

The **filter-policy import** command filters the routes that are received in RIP update packets.

The **undo filter-policy import** command disables route filtering.



By default, no export policy is configured.


Format
------

**filter-policy** { **acl-name** *acl-name* | *acl-number* | **ip-prefix** *ip-prefix-name* } **export** [ **static** | **direct** | **bgp** | { **rip** | **ospf** | **isis** } [ *process-id* ] | *interface-type* *interface-number* | *protocol* ]

**filter-policy** { **acl-name** *acl-name* | *acl-number* } **import** [ *interface-type* *interface-number* | *protocol* ]

**filter-policy ip-prefix** *ip-prefix-name* [ **gateway** *ip-prefix-name* ] **import** [ *interface-type* *interface-number* | *protocol* ]

**filter-policy gateway** *ip-prefix-name* **import**

**undo filter-policy export** [ **static** | **direct** | **bgp** | { **rip** | **ospf** | **isis** } [ *process-id* ] | *interface-type* *interface-number* | *protocol* ]

**undo filter-policy import** [ *interface-type* *interface-number* | *protocol* ]

**undo filter-policy** { **acl-name** *acl-name* | *acl-number* | **ip-prefix** *ip-prefix-name* } **export** [ **static** | **direct** | **bgp** | { **rip** | **ospf** | **isis** } [ *process-id* ] | *interface-type* *interface-number* | *protocol* ]

**undo filter-policy** { **acl-name** *acl-name* | *acl-number* } **import** [ *interface-type* *interface-number* | *protocol* ]

**undo filter-policy ip-prefix** *ip-prefix-name* [ **gateway** *ip-prefix-name* ] **import** [ *interface-type* *interface-number* | *protocol* ]

**undo filter-policy gateway** *ip-prefix-name* **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *acl-number* | Specifies the number of a basic ACL that is used to filter routes based on the destination address. | The value is an integer ranging from 2000 to 2999. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list that is used to filter routes based on the destination address. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **static** | Filters static routes. | - |
| **direct** | Filters direct routes. | - |
| **bgp** | Filters BGP routes. | - |
| **rip** | Filters RIP routes. | - |
| **ospf** | Filters OSPF routes. | - |
| **isis** | Filters IS-IS routes. | - |
| *process-id* | Specifies the process ID. process-id is required when the protocol is RIP, OSPF, or IS-IS. | The value is an integer ranging from 1 to 4294967295. |
| *interface-type* | Interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| **gateway** *ip-prefix-name* | Filters routes based on the distributing gateway. | The value is case sensitive. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you want to delete an interface-based export policy, specify interface-type interface-number. Export policies can be deleted from only one interface each time. The command is configured in the RIP process. If you want to filter routes based on an interface or a protocol, you can configure only one export policy for the interface or protocol. If no interface or protocol is specified, the configured export policy takes effect globally. You can configure only one export policy each time.

**Configuration Impact**



If the command is run more than once, the latest configuration overrides the previous one.



**Precautions**

Interface filtering policies cannot be configured for trunk member interfaces or Layer 2 interfaces.


Example
-------

# Apply IP prefix list abc to received RIP routes.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix abc deny 1.1.1.1 24
[*HUAWEI] rip 1
[*HUAWEI-rip-1] filter-policy ip-prefix abc import

```

# Filter imported static routes based on IP Prefix list named abc.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix abc deny 1.1.1.1 24
[*HUAWEI] rip 1
[*HUAWEI-rip-1] filter-policy ip-prefix abc export static

```