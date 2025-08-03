ip (Load balancing profile view)
================================

ip (Load balancing profile view)

Function
--------



The **ip** command sets the load balancing mode of IPv4 packets in a load balancing profile.

The **undo ip** command deletes the load balancing mode of IPv4 packets or restores the default load balancing mode of IPv4 packets in a load balancing profile.



By default, for the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K, IPv4 packets are load balanced based on src-ip, dst-ip, l4-src-port, and l4-dst-port.

By default, for the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-LL (low latency mode), CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM, and CE8851K, IPv4 packets are load balanced based on session-id, dest-qp, src-ip, dst-ip, l4-src-port, and l4-dst-port.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**ip** [ **src-ip** | **dst-ip** | **protocol** | **l4-src-port** | **l4-dst-port** | **src-mac** | **dst-mac** | **flowlabel** | **src-interface** | **dest-qp** | **session-id** ] \*

**undo ip** [ **src-ip** | **dst-ip** | **protocol** | **l4-src-port** | **l4-dst-port** | **src-mac** | **dst-mac** | **flowlabel** | **src-interface** | **dest-qp** | **session-id** ] \*

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**ip** [ **src-ip** | **dst-ip** | **protocol** | **l4-src-port** | **l4-dst-port** ] \*

**undo ip** [ **src-ip** | **dst-ip** | **protocol** | **l4-src-port** | **l4-dst-port** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **src-ip** | Performs load balancing based on the source IP address. | - |
| **dst-ip** | Performs load balancing based on the destination IP address. | - |
| **protocol** | Performs load balancing based on the protocol type. | - |
| **l4-src-port** | Performs load balancing based on the transport-layer source port number. | - |
| **l4-dst-port** | Performs load balancing based on the transport-layer destination port number. | - |
| **src-mac** | Performs load balancing based on the source MAC address.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **dst-mac** | Performs load balancing based on the destination MAC address.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **flowlabel** | Performs load balancing based on flow labels in IPv6 packets.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **src-interface** | Performs load balancing based on the inbound interface.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **dest-qp** | Performs load balancing for RoCEv2 packets based on dest-qp.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **session-id** | Performs load balancing for PPPoE packets based on session-id.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Load balancing profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to configure a load balancing mode for IPv4 packets in a load balancing profile. If no parameter is specified in the **undo ip** command, the default load balancing mode of IPv4 packets is restored in the load balancing profile. If a parameter is specified in the **undo ip** command, the specified load balancing mode of IPv4 packets is deleted from the load balancing profile.

**Precautions**



For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K, the session-id, dst-ip, src-ip, flowtable, l4-dst-port, l4-src-port, and protocol parameters in a load balancing profile do not take effect for PPPoE packets when the packets leave a tunnel.If the device does not support **IPv6** commands in a load balancing profile, load balancing of IPv6 packets is implemented using this command.If you run this command multiple times, only the latest configuration takes effect.




Example
-------

# In the load balancing profile abc, set the load balancing mode of IPv4 packets to protocol.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile abc
[*HUAWEI-load-balance-profile-abc] ip protocol

```