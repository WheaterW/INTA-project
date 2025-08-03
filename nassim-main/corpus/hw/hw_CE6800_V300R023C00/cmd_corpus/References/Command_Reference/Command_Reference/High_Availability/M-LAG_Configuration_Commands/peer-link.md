peer-link
=========

peer-link

Function
--------



The **peer-link** command configures an interface as the peer-link interface.

The **undo peer-link** command deletes the peer-link interface configuration on a specified interface.



By default, an interface is not a peer-link interface.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**peer-link** *peer-linkid*

**undo peer-link** [ *peer-linkid* ]

For CE6855-48XS8CQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**peer-link** *peer-linkid* **virtual-link**

**undo peer-link** *peer-linkid* **virtual-link**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-linkid* | Specifies the peer-link interface ID. | The value is 1. |
| **virtual-link** | Specifies the peer-link interface as a virtual interface for virtual peering M-LAG.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The peer-link command configures an interface as the peer-link interface.

**Prerequisites**

A DFS group has been configured.

**Precautions**

* An interface configured as a peer-link interface is added to all VLANs by default. However, if a VLAN is bound to a BD, the peer-link interface is not added to the VLAN.
* An interface configured as a peer-link interface cannot be configured with any other service.
* The peer-link *peer-linkid***virtual-link** command and the **mld snooping enable** command in the system view are mutually exclusive.


Example
-------

# Configure Eth-Trunk 2 as a virtual peer-link interface (supported only by the CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE8855, CE8851-32CQ4BQ, CE6866, CE6860-HAM, CE6866K, CE6863E-48S8CQ, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE6860-SAN, and CE8850-SAN).
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] quit
[*HUAWEI] interface eth-trunk 2
[*HUAWEI-Eth-Trunk2] peer-link 1 virtual-link

```

# Configure the Eth-Trunk interface with ID 2 as the peer-link interface.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] quit
[*HUAWEI] interface eth-trunk 2
[*HUAWEI-Eth-Trunk2] peer-link 1

```