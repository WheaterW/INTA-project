display lldp statistics
=======================

display lldp statistics

Function
--------



The **display lldp statistics** command displays statistics about Link Layer Discovery Protocol (LLDP) packets that all interfaces send and receive or LLDP packets that a specified interface sends and receives.




Format
------

**display lldp statistics** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays statistics about LLDP packets that a specified interface sends and receives. | - |
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



When an LLDP fault occurs on a device, you can run this command to locate the fault based on statistics about LLDP packets sent and received by the device.Note:To view accurate statistics about LLDP packets sent and received by a device within a specified period, run the **reset lldp statistics** command to clear historical statistics. After the specified period expires, run the display lldp statistics command to view statistics about LLDP packets sent and received by the device within the specified period.If no interface is specified when you run the command, statistics about LLDP packets sent and received by all interfaces on the device are displayed.



**Prerequisites**



LLDP has been globally enabled using the lldp enable command in the system view, and LLDP has also been enabled on interfaces using the lldp enable command in the interface view.



**Precautions**

If you want to use thedisplay lldp statistics command to locate faults, note that:

* If two directly connected devices have LLDP enabled at different time, the number of LLDP packets sent or received by one device may be different from the number of LLDP packets received or sent by the other device.
* In a specific period of time, if the number of LLDP packets sent by a local device increases but the number of LLDP packets received by a remote device remains unchanged, the link between the local and remote devices may be faulty.
* In a specific period of time, if the number of LLDP packets sent by a local device is the same as the number of LLDP packets received by a remote device but the local device cannot learn the remote device status, the local device cannot identify the type-length-value (TLV) information encapsulated in LLDP packets sent by the remote device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about LLDP packets that a device sends and receives.
```
<HUAWEI> display lldp statistics
LLDP statistics global Information:
Statistics for 10GE1/0/1:
  Sent Frames            :1212       
  Received Frames        :4               Frames Discarded    :0         
  Frames Error           :0               TLVs Discarded      :0         
  TLVs Unrecognized      :0               Neighbors Expired   :1          
  DCBX TLVs Transmitted  :0               DCBX TLVs Received  :0 
  Med TLVs Transmitted   :0               Med TLVs Received   :0         
  NetCardID TLVs Received:0               
  Last Cleared Time      :never

```

**Table 1** Description of the **display lldp statistics** command output
| Item | Description |
| --- | --- |
| LLDP statistics global Information | Statistics about LLDP packets that a device sends and receives. |
| Frames Discarded | Number of dropped LLDP packets. |
| Frames Error | Number of received error LLDP packets. |
| Received Frames | Number of received LLDP packets. |
| TLVs Discarded | Number of dropped LLDP TLVs. |
| TLVs Unrecognized | Number of unrecognized TLVs received. |
| Neighbors Expired | Number of aged remote neighbors. |
| DCBX TLVs Transmitted | Number of sent DCBX TLVs. |
| DCBX TLVs Received | Number of received DCBX TLVs. |
| Med TLVs Transmitted | Number of sent MED TLVs. |
| Med TLVs Received | Number of received Med TLVs. |
| Last cleared Time | Date and time when statistics about LLDP packets were deleted last time. |
| Sent Frames | Number of sent LLDP packets. |
| NetCardID TLVs Received | Number of received NIC ID TLVs. |