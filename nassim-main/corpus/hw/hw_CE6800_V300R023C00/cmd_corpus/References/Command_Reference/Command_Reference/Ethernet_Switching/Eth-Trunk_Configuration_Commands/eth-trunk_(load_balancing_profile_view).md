eth-trunk (load balancing profile view)
=======================================

eth-trunk (load balancing profile view)

Function
--------



The **eth-trunk** command configures an Eth-Trunk load balancing mode in a load balancing profile.

The **undo eth-trunk** command restores the default Eth-Trunk load balancing mode in a load balancing profile.



By default, for the CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, and CE6866K, the load balancing modes are seed(1) and hash-mode(1).

By default, for the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K, the load balancing modes are universal-id(1) and hash-mode(1).

By default, for the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6885-SAN, and CE6885-LL (low latency mode), the load balancing modes are universal-id(1), seed(1), and hash-mode(1).




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**eth-trunk** { **seed** *seed-data* | **hash-mode** *hash-mode-id* } \*

**undo eth-trunk** [ **seed** [ *seed-data* ] | **hash-mode** [ *hash-mode-id* ] ] \*

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**eth-trunk universal-id** *universal-id*

**undo eth-trunk universal-id** [ *universal-id* ]

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**eth-trunk** { **universal-id** *universal-id* | **hash-mode** *hash-mode-id* } \*

**undo eth-trunk** [ **universal-id** [ *universal-id* ] | **hash-mode** [ *hash-mode-id* ] ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **universal-id** *universal-id* | Specifies the offset of the hash algorithm.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16. The default value is 1. |
| **hash-mode** *hash-mode-id* | Specifies the hash algorithm for Eth-Trunk load balancing. | The value is an integer that ranges from 1 to 13. The default value is 1.  The value is an integer that ranges from 1 to 3. The default value is 1.  The value is an integer that ranges from 1 to 9. The default value is 1.  For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 13. The default value is 1.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer that ranges from 1 to 9. The default value is 1.  For the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer that ranges from 1 to 3. The default value is 1. |
| **seed** *seed-data* | Specifies the start hash value of the load balancing hash algorithm.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 1 to 65535. The default value is 1. |



Views
-----

Load balancing profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a hierarchical network, the access layer is connected to the aggregation layer through Eth-Trunks, and the aggregation layer is also connected to the core layer through Eth-Trunks. If the same hash algorithm is configured on devices at both the access layer and aggregation layer, the same hash result will be obtained. As a result, traffic sent by devices at the aggregation layer may not be load balanced on Eth-Trunk member links.

For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K, you can configure different universal-id values on aggregation devices and access devices so that aggregation devices can obtain different hash results from access devices, implementing even load balancing. Different load balancing results will be obtained for traffic sent from an Eth-Trunk when different hash algorithms are used. You can select a proper hash-mode-id for load balancing based on the traffic model. The recommended configurations are as follows:

* The default hash mode is hash mode 1. The scenario where the source and destination are the same is supported.
* In an underlay scenario, hash mode 2 can be used.
* In an overlay scenario, hash mode 3 can be used.
* If the hash mode of Eth-Trunk load balancing is the same as that of ECMP load balancing, hash polarization may occur.

For the CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, and CE6866K, different load balancing results will be obtained for traffic sent from an Eth-Trunk when different hash algorithms are used. You can select a proper hash-mode-id for load balancing based on the traffic model.

* If the source MAC address and source IP address change, you are advised to set hash-mode to 8.
* If the source or destination MAC address changes, you are advised to set hash-mode to 9.
* If the source and destination IP addresses change, you are advised to set hash-mode to 8.
* If the destination MAC address and destination IP address change, you are advised to set hash-mode to 1 or 7.
* If the source MAC address changes, you are advised to set hash-mode to 1, 2, or 7.
* If the destination IP address changes, you are advised to set hash-mode to 7.
* If the source IP address changes, you are advised to set hash-mode to 1, 7, or 9.
* Other hash-mode-id values are applicable to the scenario where incoming traffic is uneven. You are advised to use the default hash algorithm.

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6885-SAN, and CE6885-LL (low latency mode), you can configure different universal-id values on aggregation devices and access devices so that aggregation devices can obtain different hash results from access devices, implementing even load balancing.

* If the source IP address changes, you are advised to set hash-mode to 2.
* If the destination IP address changes, you are advised to set hash-mode to 1 or 5.
* If the source and destination IP addresses change, you are advised to set hash-mode to 4 or 5.
* If the source or destination MAC address changes, you are advised to set hash-mode to 1.
* If the source and destination MAC addresses change, you are advised to set hash-mode to 2 or 5.
* If the source port number changes, you are advised to set hash-mode to 2 or 3.
* If the destination port number changes, you are advised to set hash-mode to 2 or 6.
* Other hash-mode-id values are applicable to the scenario where incoming traffic is uneven. You are advised to use the default hash algorithm.


Example
-------

# Set the load balancing hash algorithm to 3 in a load balancing profile.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile default
[~HUAWEI-load-balance-profile-default] eth-trunk hash-mode 3

```