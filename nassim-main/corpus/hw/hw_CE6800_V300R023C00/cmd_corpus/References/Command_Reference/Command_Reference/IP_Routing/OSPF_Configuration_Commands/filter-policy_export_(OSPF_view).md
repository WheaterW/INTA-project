filter-policy export (OSPF view)
================================

filter-policy export (OSPF view)

Function
--------



The **filter-policy export** command filters imported routes to be advertised based on a filtering policy.

The **undo filter-policy export** command restores the default setting.



By default, the imported routes to be advertised are not filtered.


Format
------

**filter-policy** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **export** **direct**

**filter-policy** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **export** **bgp**

**filter-policy** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **export** **static**

**filter-policy** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **export** **rip** [ *protocolID* ]

**filter-policy** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **export** **isis** [ *protocolID* ]

**filter-policy** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **export** **ospf** [ *protocolID* ]

**filter-policy** *acl-number* **export** **direct**

**filter-policy** *acl-number* **export** **bgp**

**filter-policy** *acl-number* **export** **static**

**filter-policy** *acl-number* **export** **rip** [ *protocolID* ]

**filter-policy** *acl-number* **export** **isis** [ *protocolID* ]

**filter-policy** *acl-number* **export** **ospf** [ *protocolID* ]

**filter-policy** *acl-number* **export**

**filter-policy** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **export**

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* ] **export** **direct**

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* ] **export** **bgp**

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* ] **export** **static**

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* ] **export** **rip** [ *protocolID* ]

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* ] **export** **isis** [ *protocolID* ]

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* ] **export** **ospf** [ *protocolID* ]

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* ] **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **direct** | Filters direct routes. | - |
| **bgp** | Filters BGP routes. | - |
| **static** | Filters static routes. | - |
| **rip** | Filters RIP routes. | - |
| *protocolID* | Displays information about the ABR or ASBR of an OSPF route in a specified OSPF process. | The value is an integer ranging from 1 to 4294967295. The default value is 1. |
| **isis** | Filters IS-IS routes. | - |
| **ospf** | Filters OSPF routes. | - |
| *acl-number* | Specifies the basic ACL number. | The value is an integer ranging from 2000 to 2999. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After OSPF imports external routes using the **import-route** command, to prevent routing loops, you can run the **filter-policy export** command to filter the imported routes to be advertised. Only the external routes that meet the filtering conditions are converted to Type-5 LSA (AS-external-LSA) or Type 3 LSAs and then advertised. You can specify protocol or protocolID to filter the routes of a specified protocol or process. If the protocol or protocolID parameter is not specified, OSPF filters all imported routes.

**Prerequisites**

Routes of other routing protocols have been imported using the **import-route** command.


Example
-------

# Filter the routes that are imported from IS-IS and advertised by OSPF based on a filtering policy.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix1 permit 1.1.1.1 24
[*HUAWEI] ospf 100
[*HUAWEI-ospf-100] import-route isis
[*HUAWEI-ospf-100] filter-policy ip-prefix prefix1 export

```

# Configure OSPF to use a route-policy named poacl to filter imported routes when OSPF advertises them.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] rule deny source 1.1.1.1 24
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] route-policy poacl permit node 10
[*HUAWEI-route-policy] if-match acl 2000
[*HUAWEI-route-policy] quit
[*HUAWEI] ospf 1
[*HUAWEI-ospf-1] filter-policy route-policy poacl export

```