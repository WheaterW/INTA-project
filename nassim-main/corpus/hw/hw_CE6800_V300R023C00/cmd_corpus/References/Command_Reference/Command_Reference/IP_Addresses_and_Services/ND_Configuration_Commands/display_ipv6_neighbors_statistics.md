display ipv6 neighbors statistics
=================================

display ipv6 neighbors statistics

Function
--------



The **display ipv6 neighbors statistics** command displays statistics about ND entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 neighbors statistics static**

**display ipv6 neighbors statistics all**

**display ipv6 neighbors statistics interface** { *interface-name* | *interface-type* *interface-num* }

**display ipv6 neighbors statistics slot** *slot-num*

**display ipv6 neighbors statistics slot all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays statistics about all ND entries on a device. | - |
| **interface** *interface-name* | Displays statistics about ND entries on the interface with a specified name. | The value is a string of 1 to 63 case-insensitive characters without spaces. |
| **interface** *interface-type* *interface-num* | Displays statistics about ND entries on the interface with a specified type and number. | - |
| **slot** *slot-num* | Displays statistics about ND entries in a specified slot. | The value is a string of 1 to 23 case-sensitive characters. It cannot contain spaces. |
| **static** | Displays the maximum number of static ND entries on a device and the current number of static ND entries. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check statistics about ND entries, run the display ipv6 neighbors statistics command. Based on the command output, you can obtain the overall status of ND entries and check whether the number of ND entries reaches the upper limit.

**Prerequisites**

The IPv6 function has been enabled using the **ipv6 enable** command in the view of an interface before the **display ipv6 neighbors statistics interface** command is run to check statistics about ND entries on the interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about all ND entries on a device.
```
<HUAWEI> display ipv6 neighbors statistics all
-----------------------------------------------
State     Dynamic      Static       Remote     
-----------------------------------------------
Incmp     0            4            0          
Reach     1            2            0          
Stale     0            -            -          
Delay     0            -            -          
Probe     0            -            -          
-----------------------------------------------
Total     1            6            0

```

# Display statistics about ND entries in a specified slot.
```
<HUAWEI> display ipv6 neighbors statistics slot 1
-----------------------------------------------
State     Dynamic      Static       Remote     
-----------------------------------------------
Incmp     0            0            0          
Reach     0            2            0          
Stale     1            -            -          
Delay     0            -            -          
Probe     0            -            -          
-----------------------------------------------
Total     1            2            0

```

# Display statistics about static ND entries.
```
<HUAWEI> display ipv6 neighbors statistics static
Maximum number of static ND entries on each board    : 65536
Number of static ND entries configured on all boards : 6

```

**Table 1** Description of the **display ipv6 neighbors statistics** command output
| Item | Description |
| --- | --- |
| Dynamic | Number of dynamic ND entries. |
| Static | Number of static ND entries. |
| Remote | Number of remote ND entries. |
| Incmp | Number of ND entries in the INCMP state. |
| Reach | Number of ND entries in the Reach state. |
| Stale | Number of ND entries in the Stale state. |
| Delay | Number of ND entries in the Delay state. |
| Probe | Number of ND entries in the Probe state. |
| slot | Slot No. |
| Maximum number of static ND entries on each board | Maximum number of static ND entries on each board. |
| Number of static ND entries configured on all boards | Number of static ND entries configured on all boards. |