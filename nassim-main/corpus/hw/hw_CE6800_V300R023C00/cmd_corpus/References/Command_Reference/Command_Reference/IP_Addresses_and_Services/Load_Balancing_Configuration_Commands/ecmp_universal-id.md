ecmp universal-id
=================

ecmp universal-id

Function
--------



For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

The **ecmp universal-id** command configures a hash algorithm offset for ECMP load balancing.

The **undo ecmp universal-id** command restores the default hash algorithm offset of ECMP load balancing.

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE6885-SAN, and CE6885-LL in low latency mode:

The **ecmp underlay universal-id** command configures a hash algorithm offset for underlay ECMP load balancing.

The **undo ecmp underlay universal-id** command restores the default hash algorithm offset for underlay ECMP load balancing.

The **ecmp overlay universal-id** command configures a hash algorithm offset for overlay ECMP load balancing.

The **undo ecmp overlay universal-id** command restores the default hash algorithm offset for overlay ECMP load balancing.



For the CE6863H-48S6CQ, CE6863H-48S6CQ-K, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6881H-48T6CQ, and CE6881H-48T6CQ-K:

By default, the hash algorithm offset of ECMP load balancing is 1.

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE6885-SAN, and CE6885-LL in low latency mode:

By default, the hash algorithm offset of ECMP overlay load balancing is 1.

By default, the hash algorithm offset for ECMP underlay load balancing is 0.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**ecmp universal-id** *universal-id1*

**undo ecmp universal-id** [ *universal-id1* ]

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**ecmp underlay universal-id** *under-universal-id*

**undo ecmp underlay universal-id** [ *under-universal-id* ]

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ecmp overlay universal-id** *over-universal-id*

**undo ecmp overlay universal-id** [ *over-universal-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *universal-id1* | Sets the Hash algorithm offset of ECMP load balancing.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is an integer ranging from 1 to 16. |
| **underlay** | Indicates underlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *under-universal-id* | Specifies the hash algorithm offset for ECMP underlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 0 to 15. The default value is 0. |
| **overlay** | Indicates overlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *over-universal-id* | Specifies the hash algorithm offset for ECMP overlay load balancing.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 0 to 15. The default value is 1. |



Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If there are multiple equal-cost routes to the same destination, the device uses the hash algorithm to select a forwarding path based on the IP address, MAC address, and port number of each received packet. If four equal-cost routes to the destination IP address exist on the device, all traffic destined for the IP address is evenly distributed to the four forwarding paths. By default, a flow (with the same IP address, MAC address, and port number) is forwarded along the same path calculated using the hash algorithm.The hash algorithm offset affects the forwarding path calculated by the hash algorithm. That is, if the hash algorithm offsets of two devices are different, the outbound interfaces calculated by the hash algorithm for the same traffic on the two devices are different.If you want to select different forwarding paths for the same traffic on different devices, configure different hash algorithm offsets on the devices.

**Precautions**



The ecmp underlay universal-id <under-universal-id> and **load-balance ecmp rail-group enable** commands are mutually exclusive.




Example
-------

# Set the Hash algorithm offset of ECMP load balancing to 2.
```
<HUAWEI> system-view
Enter system view, return user view with return command.                        
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] ecmp universal-id 2

```

# Set the hash algorithm offset for overlay load balancing to 2.
```
<HUAWEI> system-view
Enter system view, return user view with return command.                        
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] ecmp overlay universal-id 2

```

# Set the hash algorithm offset for underlay load balancing to 2.
```
<HUAWEI> system-view
Enter system view, return user view with return command.                        
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] ecmp underlay universal-id 2

```