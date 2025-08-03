ecmp seed
=========

ecmp seed

Function
--------



For the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM, and CE8851K:

The **ecmp seed** command configures a start hash value for the seed hash algorithm for ECMP.

The **undo ecmp seed** command restores the default start hash value for the seed hash algorithm for ECMP.

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE6885-SAN, and CE6885-LL in low latency mode:

The **ecmp underlay seed** command configures a start hash value for the seed hash algorithm for underlay ECMP.

The **undo ecmp underlay seed** command restores the default start hash value of the seed hash algorithm for underlay ECMP.

The **ecmp overlay seed** command configures a start hash value for the seed hash algorithm for overlay ECMP.

The **undo ecmp overlay seed** command restores the default start hash value for the seed hash algorithm for overlay ECMP.



For the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM, and CE8851K:

By default, the seed value is 1 for ECMP load balancing.

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE6885-SAN, and CE6885-LL in low latency mode:

By default, the seed value is 1 for ECMP overlay load balancing.

By default, the seed value is 0 for ECMP underlay load balancing.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K:

**ecmp seed** *seed-data*

**undo ecmp seed** *seed-data*

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**ecmp underlay seed** *under-seed-data*

**undo ecmp underlay seed** [ *under-seed-data* ]

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ecmp overlay seed** *over-seed-data*

**undo ecmp overlay seed** [ *over-seed-data* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *seed-data* | Specifies the start hash value in the hash algorithm.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | The value is an integer ranging from 0 to 255. The default value is 1. |
| **underlay** | Indicates underlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *under-seed-data* | Specifies the start hash value of the hash algorithm for underlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 0 to 255. The default value is 0. |
| **overlay** | Indicates overlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *over-seed-data* | Specifies the start hash value of the hash algorithm for overlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 0 to 255. The default value is 1. |



Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Multiple levels of devices may use the same hash algorithm. If a lower-level device uses the same hash algorithm as an upper-level device, the hash results may be uneven or the hash operation may fail. To prevent this issue, configure a start hash value for the seed hash algorithm for ECMP on the lower-level device.

**Precautions**



The ecmp underlay seed <under-seed-data> and **load-balance ecmp rail-group enable** commands are mutually exclusive.




Example
-------

# Set a start hash value for the seed hash algorithm for ECMP to 5.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] ecmp seed 5

```

# Set a start hash value for the seed hash algorithm for overlay load balancing to 5.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] ecmp overlay seed 5

```

# Set a start hash value for the seed hash algorithm for underlay load balancing to 5.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] ecmp underlay seed 5

```