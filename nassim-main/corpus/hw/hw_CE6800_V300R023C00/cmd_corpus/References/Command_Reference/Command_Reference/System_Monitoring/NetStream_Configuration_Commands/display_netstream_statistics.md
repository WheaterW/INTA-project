display netstream statistics
============================

display netstream statistics

Function
--------



The **display netstream statistics** command displays IPv4, IPv6, or VXLAN flow statistics.




Format
------

**display netstream statistics** { **ip** | **ipv6** | **vxlan** **inner-ip** } **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | Displays IPv4 flow statistics. | - |
| **ipv6** | Displays IPv6 flow statistics. | - |
| **vxlan** | Displays VXLAN flexible flow statistics. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run this command to query IPv4, IPv6, or VXLAN flow statistics on a device, including the statistics clearance time, number of packets of different lengths, traffic statistics collection mode, and statistics on different flows.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IPv4 flow statistics on the device.
```
<HUAWEI> system-view
[~HUAWEI] display netstream statistics ip slot 1
 Last time when statistics were cleared: -
 -------------------------------------------------------------------------------
 Packet Length    : Number
 -------------------------------------------------------------------------------
 1      ~    64   : 0
 65     ~    128  : 67308526
 129    ~    256  : 0
 257    ~    512  : 0
 513    ~    1024 : 0
 1025   ~    1500 : 0
 longer than 1500 : 0
 -------------------------------------------------------------------------------
 StreamType
      Current           Aged        Created       Exported       Exported
      (streams)         (streams)   (streams)     (streams)      (Packets)
 -------------------------------------------------------------------------------
 origin
            0              0              0              0              0
 -------------------------------------------------------------------------------
 flex
            2              1              3              1              1
 -------------------------------------------------------------------------------
 flex1
            0              0              0              0              0
 -------------------------------------------------------------------------------

```

**Table 1** Description of the **display netstream statistics** command output
| Item | Description |
| --- | --- |
| Last time when statistics were cleared | Last time when statistics were deleted. |
| Packet Length | Packet length list. |
| Number | Number of packets of different lengths. |
| StreamType | Flow type. |
| Current (streams) | Number of active flows. |
| Aged (streams) | Number of flows aged out. |
| Created (streams) | Number of created flows. |
| Exported (streams) | Number of exported flows. |
| Exported (Packets) | Number of sent packets. |