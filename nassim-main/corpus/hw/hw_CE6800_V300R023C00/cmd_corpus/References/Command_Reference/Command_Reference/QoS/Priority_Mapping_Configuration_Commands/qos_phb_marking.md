qos phb marking
===============

qos phb marking

Function
--------



The **qos phb marking** command enables or disables mapping between PHBs and DSCP or 802.1p priorities in the outbound direction.

The **undo qos phb marking** command enables or disables mapping between PHBs and DSCP or 802.1p priorities in the outbound direction.



For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

By default, mapping from PHBs to DSCP priorities is disabled and mapping from PHBs to 802.1p priorities is enabled for outgoing packets.

For the CE6885-LL (low latency mode):

By default, mapping from PHBs to DSCP priorities and mapping from PHBs to 802.1p priorities are disabled for outgoing packets.




Format
------

For CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6885-LL (low latency mode):

**qos phb marking dscp enable**

**undo qos phb marking dscp enable**

For CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**qos phb marking 8021p disable**

**undo qos phb marking 8021p disable**

For CE6885-LL (low latency mode):

**qos phb marking 8021p enable**

**undo qos phb marking 8021p enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

* Generally, the **undo qos phb marking dscp enable** command is run on the device that functions as the edge node of a DS domain to disable the mapping between PHBs and DSCP priorities. When the downstream device needs to use DSCP priorities of packets, you can run the **qos phb marking dscp enable** command to enable the mapping between PHBs and DSCP priorities in the outbound direction.
* Generally, the **qos phb marking 8021p disable** command is used on the device that functions as the edge node of a DS domain to disable the mapping between PHBs and 802.1p priorities. When the downstream device needs to use 802.1p priorities of packets, you can run the **undo qos phb marking 8021p disable** command to enable the mapping between PHBs and 802.1p priorities in the outbound direction.

For the CE6885-LL (low latency mode):

* Generally, the mapping between PHBs and DSCP priorities is disabled on the device that functions as the edge node of a DS domain. When the downstream device needs to use DSCP priorities of packets, you can run the **qos phb marking dscp enable** command to enable the mapping between PHBs and DSCP priorities in the outbound direction.
* Generally, the mapping between PHBs and 802.1p priorities is disabled on the device that functions as the edge node of a DS domain. When the downstream device needs to use 802.1p priorities of packets, you can run the **qos phb marking 8021p enable** command to enable the mapping between PHBs and 802.1p priorities in the outbound direction.


Example
-------

# Enable mapping between PHBs and DSCP priorities for outgoing packets on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos phb marking dscp enable

```

# Disable mapping from PHBs to 802.1p priorities for outgoing packets on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos phb marking 8021p disable

```

# Enable mapping from PHBs to 802.1p priorities for outgoing packets on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos phb marking 8021p enable

```