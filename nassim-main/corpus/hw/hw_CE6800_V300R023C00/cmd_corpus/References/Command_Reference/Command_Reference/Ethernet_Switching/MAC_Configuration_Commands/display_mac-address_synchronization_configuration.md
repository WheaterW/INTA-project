display mac-address synchronization configuration
=================================================

display mac-address synchronization configuration

Function
--------



The **display mac-address synchronization configuration** command displays MAC synchronization configuration on a specified slot.




Format
------

**display mac-address synchronization configuration** { **all** | **slot** *slot-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Specifies all slots. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When the MAC address software and hardware tables are not synchronized, you can run this command to check whether the MAC address software table in all slots or in a slot is synchronized and whether MAC address software and hardware tables are synchronized, including the real-time synchronization status, periodic synchronization status, receiver's synchronization status, learning synchronization status of MAC address software and hardware tables, and aging synchronization status.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display MAC synchronization configuration on slot 1.
```
<HUAWEI> display mac-address synchronization configuration slot 1
-------------------------------------------------------------------------------
     Slot    Realtime  Periodical Timer(ms)  Receive   Chip-learning  Chip-aging
-------------------------------------------------------------------------------
       1     Disable    Disable    1000      Disable      Enable       Enable
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display mac-address synchronization configuration** command output
| Item | Description |
| --- | --- |
| Slot | Slot id. |
| Realtime | MAC synchronization realtime send mode. |
| Periodical | MAC synchronization periodic send mode. |
| Timer(ms) | MAC synchronization timer interval. |
| Receive | MAC synchronization receive mode. |
| Chip-learning | Insert lost MAC address according to the chip. |
| Chip-aging | Remove redundant MAC address according to the chip. |