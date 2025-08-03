display vxlan statistics
========================

display vxlan statistics

Function
--------



The **display vxlan statistics** command displays VXLAN packet statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vxlan statistics source** *source-ip* **peer** *peer-ip* **vni** *vni-id*

**display vxlan statistics vni** *vni-id*

**display vxlan statistics source** *source-ip* **peer** *peer-ip*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *peer-ip* | Displays VXLAN packet statistics collected based on the IP address of the peer virtualized edge node. | The value is in dotted decimal notation. |
| **vni** *vni-id* | Displays VXLAN packets statistics collected based on a specified VNI ID. | The value is an integer ranging from 1 to 16777215. |
| **source** *source-ip* | Displays VXLAN packets statistics collected based on the source IP address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After you run the **vxlan statistics enable** command to enable VXLAN packet statistics collection in the NVE interface view, you can run the **display vxlan statistics** command to view packet statistics by VNI and VXLAN tunnel.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display VXLAN packet statistics collected based on the VNI with the ID of 1.
```
<HUAWEI> display vxlan statistics vni 1
-------------------------------------------------------------------------------------------
Item                     Packets                       Bytes     Packets/s          Bytes/s
-------------------------------------------------------------------------------------------
Inbound            13,399,602,115          2,331,530,768,010       190,897       33,216,123
Outbound           10,821,560,506          1,864,696,688,120        42,986        7,479,634
-------------------------------------------------------------------------------------------

```

# Display VXLAN packet statistics collected based on the source IP address 1.1.1.1, VNI with the ID of 1, and the IP address of the peer virtualized edge node as 1.1.1.2.
```
<HUAWEI> display vxlan statistics source 1.1.1.1 peer 1.1.1.2 vni 1
-------------------------------------------------------------------------------------------
Item                     Packets                       Bytes     Packets/s          Bytes/s
-------------------------------------------------------------------------------------------
Inbound             1,608,444,626            279,869,364,924       191,298       33,285,908
Outbound              922,508,265            159,219,643,258        20,246        3,522,820
-------------------------------------------------------------------------------------------

```

# Display VXLAN packet statistics collected based on the source IP address 1.1.1.1, and the IP address of the peer virtualized edge node as 1.1.1.2.
```
<HUAWEI> display vxlan statistics source 1.1.1.1 peer 1.1.1.2
-------------------------------------------------------------------------------------------
Item                     Packets                       Bytes     Packets/s          Bytes/s
-------------------------------------------------------------------------------------------
Inbound             1,766,628,190            306,970,426,564       190,948       33,225,118
Outbound              922,624,140            159,239,805,508        20,209        3,516,422
-------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display vxlan statistics** command output
| Item | Description |
| --- | --- |
| Item | Statistical item. |
| Packets | Number of packets. |
| Bytes | Number of bytes. |
| Packets/s | Indicates the rate of packets. |
| Bytes/s | Indicates the rate of bytes. |
| 0 unknown-unicast-drops | Number of discarded unknown unicast packets. |
| 0 unknown-multicast-drops | Number of discarded unknown multicast packets. |
| 0 broadcasts-drops | Number of discarded broadcast packets. |