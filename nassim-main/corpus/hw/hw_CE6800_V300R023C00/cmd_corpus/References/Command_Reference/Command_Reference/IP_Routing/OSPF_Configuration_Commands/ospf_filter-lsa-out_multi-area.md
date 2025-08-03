ospf filter-lsa-out multi-area
==============================

ospf filter-lsa-out multi-area

Function
--------



The **ospf filter-lsa-out multi-area** command enables an OSPF multi-area adjacency interface to filter the LSAs to be sent.

The **undo ospf filter-lsa-out multi-area** command disables an OSPF multi-area adjacency interface from filtering the LSAs to be sent.



By default, OSPF multi-area adjacency interfaces do not filter the LSAs to be sent.


Format
------

**ospf filter-lsa-out** { **all** | { **ase** [ **acl** { *ase-acl-num* | *ase-acl-name* } ] | **nssa** [ **acl** { *nssa-acl-num* | *nssa-acl-name* } ] | **summary** [ **acl** { *sum-acl-num* | *sum-acl-name* } ] } \* } **multi-area** { *area-id-integer* | *area-id-ipv4* }

**undo ospf filter-lsa-out multi-area** { *area-id-integer* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Filters all LSAs except Grace LSAs. | - |
| **ase** | Filters AS-external LSAs (Type-5 LSAs). | - |
| **acl** | Specifies the ACL for route filtering. | - |
| *ase-acl-num* | Specifies the number of a basic ACL. | The value is an integer that ranges from 2000 to 2999. |
| *ase-acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **nssa** | Filters NSSA LSAs (Type-7 LSAs). | - |
| *nssa-acl-num* | Specifies the number of a basic ACL. | The value is an integer that ranges from 2000 to 2999. |
| *nssa-acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **summary** | Filters Network-summary LSAs (Type-3 LSAs). | - |
| *sum-acl-num* | Specifies the number of a basic ACL. | The value is an integer that ranges from 2000 to 2999. |
| *sum-acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| *area-id-integer* | Specifies the ID of an OSPF area. | The value is a decimal integer ranging from 0 to 4294967295. |
| *area-id-ipv4* | Specifies the ID of an OSPF area. | The value is in the format of an IP address. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a network, the capacity of the attached device is small. To prevent the memory usage from exceeding the threshold on the attached device due to reception of a large number of LSAs, you can configure an OSPF interface to filter outgoing LSAs, which prevents unnecessary LSAs from being sent to neighbors. This reduces the size of the LSDB on neighbors.

**Prerequisites**

The **ospf enable multi-area** command has been run.

**Configuration Impact**

Filtering outgoing LSAs on an OSPF interface can prevent useless LSAs from being sent to neighbors. This reduces the size of the LSDB on neighbors and speeds up network convergence.The following operations will cause the OSPF neighbor relationship of the interface to be automatically re-established:

* Delete or configure the **ospf filter-lsa-out** command on the interface.
* Delete or configure the **ospf filter-lsa-out acl** command on the interface.
* The ACL rule referenced by the **ospf filter-lsa-out acl** command is modified.

**Precautions**

When filtering conditions are configured for a named ACL, only the configurations specified by source and time-range take effect.Grace LSAs are used to inform neighbors of the graceful restart (GR) time, cause, and interface instance ID when a GR starts or ends. The ospf filter-lsa-out multi-area command does not apply to Grace LSAs.


Example
-------

# Configure multi-area adjacency interface 100GE1/0/1 to filter all outgoing LSAs except Grace LSAs.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 0
[*HUAWEI-ospf-1-area-0.0.0.0] quit
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] quit
[*HUAWEI-ospf-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf enable 1 area 0
[*HUAWEI-100GE1/0/1] ospf enable multi-area 1
[*HUAWEI-100GE1/0/1] ospf filter-lsa-out all multi-area 1

```