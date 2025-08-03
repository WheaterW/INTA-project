ospf filter-lsa-out
===================

ospf filter-lsa-out

Function
--------



The **ospf filter-lsa-out** command configures an OSPF interface to filter outgoing LSAs on a P2P, broadcast, or NBMA network.

The **undo ospf filter-lsa-out** command prevents an OSPF interface from filtering outgoing LSAs on a P2P, broadcast, or NBMA network.



By default, outgoing LSAs are not filtered on a P2P, broadcast, or NBMA network.


Format
------

**ospf filter-lsa-out** { **all** | { **ase** [ **acl** { *ase-acl-num* | *ase-acl-name* } ] | **nssa** [ **acl** { *nssa-acl-num* | *nssa-acl-name* } ] | **summary** [ **acl** { *sum-acl-num* | *sum-acl-name* } ] } \* }

**undo ospf filter-lsa-out**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Filters all LSAs except Grace LSAs. | - |
| **ase** | Filters AS-external LSAs (Type-5 LSAs). | - |
| **acl** | Specifies the ACL for route filtering. | - |
| *ase-acl-num* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| *ase-acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters starting with a letter. It cannot contain spaces. |
| **nssa** | Filters outgoing NSSA LSAs (Type 7). | - |
| *nssa-acl-num* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| *nssa-acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. The value starts with a letter or digit but cannot contain only digits. |
| **summary** | Filters outgoing network summary LSAs (Type 3). | - |
| *sum-acl-num* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| *sum-acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. The value starts with a letter or digit but cannot contain only digits. |



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

**Configuration Impact**

Filtering outgoing LSAs on an OSPF interface can prevent useless LSAs from being sent to neighbors. This reduces the size of the LSDB on neighbors and speeds up network convergence.The following operations will cause the OSPF neighbor relationship of the interface to be automatically re-established:

* Delete or configure the **ospf filter-lsa-out** command on the interface.
* Delete or configure the **ospf filter-lsa-out acl** command on the interface.
* The ACL rule referenced by the **ospf filter-lsa-out acl** command is modified.

**Precautions**



Configure the filtering rules for a named ACL only the source address range that is specified in source and the period that is specified in time-range take effect.Grace LSAs are used to inform the neighbor of the Graceful Restart (GR) time, cause, and interface instance ID when GR starts and ends. The command is not used to filter the grace LSAs.After the **ospf filter-lsa-out** command is run, the LSAs that other devices have received before will not be deleted immediately, but it will be deleted after a period of time (usually no more than one hour).




Example
-------

# Configure an interface to filter all outgoing LSAs except grace LSAs.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf filter-lsa-out all

```