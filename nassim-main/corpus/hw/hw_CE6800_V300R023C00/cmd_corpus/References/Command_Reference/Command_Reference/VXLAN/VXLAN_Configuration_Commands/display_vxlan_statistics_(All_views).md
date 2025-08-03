display vxlan statistics (All views)
====================================

display vxlan statistics (All views)

Function
--------



The **display vxlan statistics** command displays IPv6 VXLAN packet statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vxlan statistics source** *source-ipv6* **peer** *peer-ipv6* **vni** *vni-val*

**display vxlan statistics source** *source-ipv6* **peer** *peer-ipv6*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *peer-ipv6* | Displays IPv6 VXLAN packet statistics collected based on the IPv6 address of the peer virtualized edge node. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vni** *vni-val* | Displays IPv6 VXLAN packets statistics collected based on a specified VNI ID. | The value is an integer ranging from 1 to 16777215. |
| **source** *source-ipv6* | Displays IPv6 VXLAN packets statistics collected based on the IPv6 source address. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After running the **vxlan statistics enable** command to enable IPv6 VXLAN packet statistics collection in the NVE interface view, you can run the **display vxlan statistics** command to view packet statistics by VNI and IPv6 VXLAN tunnel.

**Precautions**

In the IPv6 VXLAN VNI statistics output, unknown-unicast-drops, unknown-multicast-drops, and broadcasts-drops are always displayed as 0.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IPv6 VXLAN packet statistics on the device. Set the source IPv6 address to 2001:DB8:1::1, the IPv6 address of the peer virtualization edge node to 2001:DB8:2::2, and the VNI ID to 1.
```
<HUAWEI> display vxlan statistics source 2001:DB8:1::1 peer 2001:DB8:2::2 vni 1
    Last 300 seconds input rate: 536 bits/sec, 0 packets/sec
    Last 300 seconds output rate: 368 bits/sec, 0 packets/sec
    1051720995 packets input, 134620265610 bytes
    909549472 packets output, 116038062100 bytes
    Input:1051720620 unicast packets, 0 multicast packets
          375 broadcasts
          0 unknown-unicast-drops
          0 unknown-multicast-drops
          0 broadcasts-drops

   Output:909549097 unicast packets, 0 multicast packets
          375 broadcasts

```

**Table 1** Description of the **display vxlan statistics (All views)** command output
| Item | Description |
| --- | --- |
| Last 300 seconds input rate: 536 bits/sec, 0 packets/sec | 536 indicates the number of received bits per second in last 300 seconds; 0 indicates the number of received packets per second in 300 seconds. |
| Last 300 seconds output rate: 368 bits/sec, 0 packets/sec | 368 indicates the number of sent bits per second in last 300 seconds; 0 indicates the number of sent packets per second in 300 seconds. |
| 0 unknown-unicast-drops | Number of discarded unknown unicast packets. |
| 0 unknown-multicast-drops | Number of discarded unknown multicast packets. |
| 0 broadcasts-drops | Number of discarded broadcast packets. |
| 1051720995 packets input, 134620265610 bytes | 1051720995 indicates the number of received packets; 134620265610 indicates the number of bytes of received packets. |
| 909549472 packets output, 116038062100 bytes | 909549472 indicates the number of sent packets; 116038062100 indicates the number of bytes of sent packets. |
| Input:1051720620 unicast packets, 0 multicast packets 375 broadcasts | 1051720620 indicates the number of received unicast packets; 0 indicates the number of received multicast packets; 375 indicates the number of received broadcast packets. |
| Output:909549097 unicast packets, 0 multicast packets 375 broadcasts | 909549097 indicates the number of sent unicast packets; 0 indicates the number of sent multicast packets; 375 indicates the number of sent broadcast packets. |