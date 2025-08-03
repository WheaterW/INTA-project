display rmon history
====================

display rmon history

Function
--------



The **display rmon history** command displays RMON historical sampling information.




Format
------

**display rmon history** [ *interface-type* *interface-number* | *interface-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Displays the RMON historical sampling information of a specified interface. If this parameter is not specified, all the RMON historical sampling information will be displayed. | - |
| *interface-number* | Specifies the interface number. | - |
| *interface-name* | Specifies the interface name. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After the rmon history command is used to configure the RMON historical sampling function, the system will sample the interface information periodically. To view RMON historical sampling information, run the display rmon history command. The command output contains the number of historical samples, interval of historical sampling, the latest historical sampling information, the usage rate of Ethernet interfaces, the number of packets with CRC errors, and the total number of packets.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the RMON historical sampling information.
```
<HUAWEI> display rmon history
History control entry 1 owned by Creator is VALID
  Sampled interface     : 10GE 1/0/1
  Sampling interval     : 30(sec) with 10 buckets max
  Last Sampling time    : 0days 00h:09m:43s
  Latest sampled values :
  Octets               :645       , Packets           :7
  Broadcast packets    :7         , Multicast packets :0
  Undersize packets    :6         , Oversize packets  :0
  Fragments packets    :0         , Jabbers packets   :0
  CRC alignment errors :0         , Collisions        :0
  Dropped packets      :0         , Utilization       :0

```

**Table 1** Description of the **display rmon history** command output
| Item | Description |
| --- | --- |
| History control entry 1 owned by Creator is VALID | Current status of the historical sampling function with the index number being entry-number created by the owner is status.   * entry-number: An index number of the history control table entry. * owner: An owner. * status: * undercreation: The entry corresponding to the index is invalid. * valid: The entry corresponding to the index is valid. * invalid: The entry corresponding to the index is invalid because of the interface board hot swapping. |
| Sampled interface | Sampled interface. |
| Sampling interval | Sampling period, in seconds. The system will sample the interface information based on this period. |
| Last Sampling time | Latest sampling time. |
| Latest sampled values | Latest sampled result. |
| Octets | Number of bytes received in a sampling period. |
| Packets | Number of packets received in a sampling period. |
| Broadcast packets | Number of broadcast packets received in a sampling period. |
| Multicast packets | Number of multicast packets received in a sampling period. |
| Undersize packets | Number of undersize packets received in a sampling period. |
| Oversize packets | Number of oversize packets received in a sampling period. |
| Fragments packets | Number of undersize packets with CRC errors received in a sampling period. |
| Jabbers packets | Number of oversize packets with CRC errors received in a sampling period. |
| CRC alignment errors | Number of packets with CRC errors received in a sampling period. |
| Collisions | Number of conflicting packets received in a sampling period. |
| Dropped packets | Number of discarded packets received in a sampling period. |
| Utilization | Bandwidth usage in a sampling period. |