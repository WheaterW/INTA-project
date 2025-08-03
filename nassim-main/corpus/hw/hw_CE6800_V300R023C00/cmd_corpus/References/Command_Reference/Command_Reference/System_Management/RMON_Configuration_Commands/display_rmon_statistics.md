display rmon statistics
=======================

display rmon statistics

Function
--------



The **display rmon statistics** command displays RMON Ethernet statistics.




Format
------

**display rmon statistics** [ *interface-type* *interface-number* | *interface-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Displays the RMON Ethernet statistics about a specified GE interface. If this parameter is not specified, all the RMON Ethernet statistics will be displayed. | - |
| *interface-number* | Specifies the interface number. | - |
| *interface-name* | Specifies an interface name. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After the rmon statistics command is used to configure the Ethernet statistics function, the system will analyze the packet statistics on an Ethernet interface. To view the information about the interface communication since the statistics function is enabled, run the display rmon statistics command, which facilitates fault location.The device automatically deletes statistics when it is restarted.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display RMON statistics.
```
<HUAWEI> display rmon statistics
Statistics entry 1 owned by userA is valid.
  Interface : 10GE 1/0/1<ifEntry.402653698>
  Received  :
  Octets              :4294966296, Packets          :265484
  Broadcast packets   :262490    , Multicast packets:568
  Undersize packets   :0         , Oversize packets :0
  Fragments packets   :0         , Jabbers packets  :0
  CRC alignment errors:0         , Collisions       :0
  Dropped packets (insufficient resources):0
  Packets received according to length (octets):
  64     :0         ,  65-127  :0         ,  128-255  :0
  256-511:0         ,  512-1023:0         ,  1024-1518:0

```

**Table 1** Description of the **display rmon statistics** command output
| Item | Description |
| --- | --- |
| Statistics entry 1 owned by userA is valid. | Current status of the Ethernet statistics function with the index number being entry-number created by the owner is status.   * entry-number: An index number of the Ethernet statistics function. * owner: An owner. * status: * undercreation: The entry corresponding to the index is invalid. * valid: The entry corresponding to the index is valid. * invalid: The entry corresponding to the index is invalid because of the interface board hot swapping. |
| Interface | Interface on which the Ethernet statistics function is enabled, followed by the OID name of the interface. |
| Received | Statistics about the received packets. |
| Octets | Total number of received bytes. |
| Packets | Total number of received packets. |
| Packets received according to length (octets) | Number of received packets that are classified according to length. |
| Broadcast packets | Number of received broadcast packets. |
| Multicast packets | Number of received multicast packets. |
| Undersize packets | Number of received undersize packets. |
| Oversize packets | Number of received oversize packets. |
| Fragments packets | Number of received undersized data packets with check errors. |
| Jabbers packets | Number of received oversized data packets with check errors. |
| CRC alignment errors | Number of received packets with CRC errors. |
| Collisions | Number of received conflicting packets. |
| Dropped packets (insufficient resources) | Number of discarded packets. |