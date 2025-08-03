hashmode
========

hashmode

Function
--------



The **hashmode** command configures a hash mode for ECMP load balancing.

The **undo hashmode** command restores the default hash mode for ECMP load balancing.



By default, the hash mode of ECMP load balancing is 0.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**undo hashmode**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K:

**hashmode** *value1*

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**hashmode** *value2*

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**hashmode** { **overlay** | **underlay** } *value3*

**undo hashmode** { **overlay** | **underlay** } [ *value3* ]

For CE6885-LL (low latency mode):

**hashmode underlay** *value3*

**undo hashmode underlay** *value3*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value3* | Specifies a hash algorithm for ECMP load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 0 to 15. The default value is 0.   * 0: default per-flow load balancing algorithm * 1: polynomial A * 2: polynomial B * 3: polynomial C * 4: polynomial D * 5: polynomial E * 6: polynomial F * 7: polynomial G * 8: polynomial H * 9: polynomial I * 10: polynomial J * 11: polynomial K * 12: polynomial L * 13: polynomial M * 14: polynomial N * 15: polynomial O |
| *value1* | Specifies a hash algorithm for ECMP load balancing.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | The value is an integer ranging from 0 to 5. The default value is 0.   * 0: default per-flow load balancing algorithm * 1: symmetric hash algorithm * 2: polynomial A * 3: polynomial B * 4: polynomial C * 5: polynomial D |
| *value2* | Specifies a hash algorithm for ECMP load balancing.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is an integer ranging from 0 to 2. The default value is 0.   * 0: default per-flow load balancing algorithm * 1: symmetric hash algorithm * 2: per-packet load balancing algorithm |
| **overlay** | Indicates overlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **underlay** | Indicates underlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In ECMP load balancing scenarios, if traffic is unevenly load balanced, you can change the hashmode value to adjust the hash mode so that traffic is evenly load balanced.The load balancing result varies according to the hash algorithm. You can select a proper hash mode for load balancing based on the traffic model.For the CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, and CE6855-48XS8CQ, the polynomial calculation result is closely related to the change rule of packet characteristics, number of ECMP members, and number of packets. The following conclusions are for reference only:

* To configure the same source and destination function, you are advised to set hashmode to 1.
* If the destination IP address changes, you are advised to set hashmode to 0 or 2.
* If the source IP address changes, you are advised to set hashmode to 0 or 2.
* If the source port changes, you are advised to set hashmode to 0 or 2.
* If the destination port changes, you are advised to set hashmode to 0 or 2.
* If the source and destination IP addresses change, you are advised to set hashmode to 0 or 2.In conclusion, you are advised to set hashmode to 0 or 2 unless you configure the same source and destination function.For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H and CE6881H-K, the load balancing mode is as follows:
* To configure the same source and destination function, you are advised to set hashmode to 1.
* If per-packet load balancing is required, you are advised to set hashmode to 2.For E series cards, the load balancing mode is as follows:
* To configure the same source and destination function, you are advised to set hashmode to 1.
* If per-packet load balancing is required, you are advised to set hashmode to 2.For the CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE6863E-48S8CQ, CE6885-SAN, and CE6885-LL in low latency mode:Overlay load balancing:If the destination IP address changes, you are advised to set hashmode to 2 or 14.If the source IP address changes, you are advised to set hashmode to 4 or 15.If the source port changes, you are advised to set hashmode to 0.If the destination port changes, you are advised to set hashmode to 15.If the source and destination IP addresses change, you are advised to set hashmode to 1.If the source and destination ports change, you are advised to set hashmode to 15.Underlay load balancing:If the destination IP address changes, you are advised to set hashmode to 3 or 15.If the source IP address changes, you are advised to set hashmode to 0 or 5.If the source port changes, you are advised to set hashmode to 1.If the destination port changes, you are advised to set hashmode to 0.If the source and destination IP addresses change, you are advised to set hashmode to 2.If the source and destination ports change, you are advised to set hashmode to 0.


Example
-------

# Set the hash mode of ECMP load balancing to 1.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] hashmode 1

```

# Set the hash mode of overlay load balancing to 1.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] hashmode overlay 1

```

# Set the hash mode of underlay load balancing to 1.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] hashmode underlay 1

```