mpls (load balancing profile view)
==================================

mpls (load balancing profile view)

Function
--------



The **mpls** command configures a load balancing mode for MPLS packets in a load balancing profile.

The **undo mpls** command deletes the specified load balancing mode or restores the default load balancing mode of MPLS packets in a load balancing profile.



By default, MPLS packets are load balanced based on top-label and 2nd-label.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K:

**mpls** [ **src-ip** | **dst-ip** | **top-label** | **2nd-label** | **3rd-label** | **src-mac** | **dst-mac** | **src-interface** | **l4-src-port** | **l4-dst-port** | **protocol** ] \*

**undo mpls** [ **src-ip** | **dst-ip** | **top-label** | **2nd-label** | **3rd-label** | **src-mac** | **dst-mac** | **src-interface** | **l4-src-port** | **l4-dst-port** | **protocol** ] \*

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**mpls** [ **src-ip** | **dst-ip** | **top-label** | **2nd-label** ] \*

**undo mpls** [ **src-ip** | **dst-ip** | **top-label** | **2nd-label** ] \*

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**mpls** [ **src-ip** | **dst-ip** | **top-label** | **2nd-label** | **3rd-label** | **src-mac** | **dst-mac** | **src-interface** | **l4-src-port** | **l4-dst-port** | **protocol** | **fourth-label** | **fifth-label** ] \*

**undo mpls** [ **src-ip** | **dst-ip** | **top-label** | **2nd-label** | **3rd-label** | **src-mac** | **dst-mac** | **src-interface** | **l4-src-port** | **l4-dst-port** | **protocol** | **fourth-label** | **fifth-label** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **src-ip** | Performs load balancing based on the source IP address. | - |
| **dst-ip** | Performs load balancing based on the destination IP address. | - |
| **top-label** | Performs load balancing based on the top label. | - |
| **2nd-label** | Performs load balancing based on the second label. | - |
| **3rd-label** | Performs load balancing based on the third label.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **src-interface** | Performs load balancing based on the inbound interface.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **l4-src-port** | Performs load balancing based on the transport-layer source port number.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **l4-dst-port** | Performs load balancing based on the transport-layer destination port number.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **protocol** | Performs load balancing based on the protocol number.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **src-mac** | Performs load balancing based on the source MAC address.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **dst-mac** | Performs load balancing based on the destination MAC address.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **fourth-label** | Performs load balancing based on the fourth label.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **fifth-label** | Performs load balancing based on the fifth label.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Load balancing profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the mpls command to configure a load balancing mode for MPLS packets in a load balancing profile. The **undo mpls** command with no parameter specified restores the default load balancing mode for MPLS packets whereas the **undo mpls** command with a parameter specified deletes the specified load balancing mode for MPLS packets.

**Precautions**

Label-based load balancing takes effect only for labeled packets on the inbound interface.If you run this command multiple times, only the latest configuration takes effect.


Example
-------

# In the load balancing profile abc, set the load balancing mode of MPLS packets to 2nd-label.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile abc
[*HUAWEI-load-balance-profile-abc] mpls 2nd-label

```