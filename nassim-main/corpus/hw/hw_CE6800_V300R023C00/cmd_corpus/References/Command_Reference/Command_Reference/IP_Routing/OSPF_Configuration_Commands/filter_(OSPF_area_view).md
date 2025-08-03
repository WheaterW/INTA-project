filter (OSPF area view)
=======================

filter (OSPF area view)

Function
--------



The **filter export** command filters the outgoing Type-3 LSAs of the local area.

The **undo filter export** command restores the default setting.

The **filter import** command filters incoming Type-3 LSAs of the local area.

The **undo filter import** command restores the default setting.



By default, outgoing Type-3 LSAs of the local area are not filtered.

By default, the incoming Type-3 LSAs are not filtered.




Format
------

**filter** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **export**

**filter** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **import** [ **include-abr-summary** ]

**filter** *acl-number* **export**

**filter** *acl-number* **import** [ **include-abr-summary** ]

**undo filter** [ **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* | *acl-number* ] **export**

**undo filter** [ **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* | *acl-number* ] **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **include-abr-summary** | Specifies a route-policy for the summarized route on the ABR. | - |
| *acl-number* | Specifies the basic ACL number. | The value is an integer ranging from 2000 to 2999. |



Views
-----

OSPF area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **filter export** command to filter LSAs in an area to prevent useless LSAs from being sent to other areas. This reduces the size of the LSDB and speeds up network convergence. You can run this command in the local area to set filtering conditions for the Type 3 LSAs to be advertised.You can run the **filter import** command to filter LSAs in an area to prevent unnecessary LSAs from being accepted from other areas. This reduces the size of the LSDB and speeds up network convergence. You can run this command in the local area to set filtering conditions for the incoming Type 3 LSAs.

**Configuration Impact**



After filtering conditions are set for the outgoing Type-3 LSAs to be advertised using the **filter export** command, only the outgoing Type-3 LSAs that match the filtering conditions can be advertised.After filtering conditions are set for the incoming Type-3 LSAs using the **filter import** command, only the incoming Type-3 LSAs that match the filtering conditions can be accepted.



**Precautions**



This command can be configured only on ABRs.




Example
-------

# Configure OSPF to filter outgoing Type-3 LSAs.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix1 permit 1.1.1.1 24
[*HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] filter ip-prefix prefix1 export

```

# Filter incoming Type-3 LSAs within the local area.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix1 permit 1.1.1.1 24
[*HUAWEI] ospf 100
[*HUAWEI-ospf-100] area 1
[*HUAWEI-ospf-100-area-0.0.0.1] filter ip-prefix prefix1 import

```