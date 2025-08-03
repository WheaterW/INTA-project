filter-lsa-out peer
===================

filter-lsa-out peer

Function
--------



The **filter-lsa-out peer** command configures a device to filter the LSAs to be sent to the specified neighbor on a P2MP network.

The **undo filter-lsa-out peer** command cancels the configuration.



By default, the LSAs that are to be sent to the specified neighbor on a P2MP network are not filtered.


Format
------

**filter-lsa-out peer** *peer-addr* { **all** | { **ase** [ **acl** { *ase-acl-num* | *ase-acl-name* } ] | **nssa** [ **acl** { *nssa-acl-num* | *nssa-acl-name* } ] | **summary** [ **acl** { *sum-acl-num* | *sum-acl-name* } ] } \* }

**undo filter-lsa-out peer** *peer-addr*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-addr* | Specifies the IP address of a P2MP neighbor. | The value is in dotted decimal notation. |
| **all** | Filters all the outgoing LSAs except Grace LSAs. | - |
| **ase** | Filters AS-external LSAs (Type-5 LSAs). | - |
| **acl** *sum-acl-num* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl** *sum-acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **acl** *ase-acl-num* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl** *ase-acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **acl** *nssa-acl-num* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl** *nssa-acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **nssa** | Filters outgoing NSSA LSAs (Type 7). | - |
| **summary** | Filters outgoing network summary LSAs (Type 3). | - |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a P2MP network, when multiple P2MP links exist between two devices, you can configure the local router to filter the outgoing LSAs on the specified link. This can reduce unnecessary LSA retransmission attempts and save bandwidth resources.For a named ACL, configure filtering rules, only the source address range that is specified by the source parameter and the period of time that is specified by the time-range parameter take effect.

**Precautions**

No link layer protocol is considered as P2MP by default. P2MP must be forcibly changed from another network type. To change the network type to P2MP, run the **ospf network-type p2mp** command.To filter the outgoing LSAs on a specified OSPF interface, run the **ospf filter-lsa-out** command.After the **filter-lsa-out peer** command is run, the received LSAs are not deleted immediately. Instead, they are deleted after a period of time (generally less than one hour).


Example
-------

# On a P2MP network, configure a device to filter all the LSAs (except Grace LSAs) sent to neighbor 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] filter-lsa-out peer 10.1.1.1 all

```