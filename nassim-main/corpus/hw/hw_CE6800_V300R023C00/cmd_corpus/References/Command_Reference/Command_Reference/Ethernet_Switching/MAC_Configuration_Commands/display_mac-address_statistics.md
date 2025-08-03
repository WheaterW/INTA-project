display mac-address statistics
==============================

display mac-address statistics

Function
--------



The **display mac-address statistics** command displays types and numbers of returned codes when MAC address entries are delivered to or deleted from a specified slot.




Format
------

**display mac-address statistics** { **insert** | **remove** } **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **insert** | Indicates the type and number of returned values when MAC address entries are delivered to a specified slot. | - |
| **remove** | Indicates the type and number of returned values when MAC address entries are deleted from a specified slot. | - |
| **slot** *slot-id* | Displays the delivered or deleted MAC address entries in a specified slot. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When MAC address entries are delivered to or deleted from a specified slot, you can run this command to check the types and numbers of return codes to determine whether an error occurs.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the type and number of returned values when MAC address entries are deleted from slot 1.
```
<HUAWEI> display mac-address statistics remove slot 1
-------------------------------------------------------------------------------
MAC type             Ok      Err  Internal    Param    Empty  Notfound  Timeout
-------------------------------------------------------------------------------
DYNAMIC               b        0         0        0        0         0        0
STATIC                0        0         0        0        0         0        0
BLACKHOLE             0        0         0        0        0         0        0
OAM                   0        0         0        0        0         0        0
MUXVLAN               0        0         0        0        0         0        0
SECMAC                0        0         0        0        0         0        0
STICKYMAC             0        0         0        0        0         0        0
MUXVLAN_REMOTE        0        0         0        0        0         0        0
DHCP_STICKY           0        0         0        0        0         0        0
VM                    0        0         0        0        0         0        0

```

# Display types and numbers of return codes when MAC address entries are delivered to slot 1.
```
<HUAWEI> display mac-address statistics insert slot 1
-------------------------------------------------------------------------------
MAC type             Ok      Err  Internal    Param     Full     Exist  Timeout
-------------------------------------------------------------------------------
DYNAMIC               0        0         0        0        0         0        0
STATIC                0        0         0        0        0         0        0
BLACKHOLE             2        0         0        0        0         0        0
OAM                   0        0         0        0        0         0        0
MUXVLAN               0        0         0        0        0         0        0
SECMAC                0        0         0        0        0         0        0
STICKYMAC             0        0         0        0        0         0        0
MUXVLAN_REMOTE        0        0         0        0        0         0        0
DHCP_STICKY           0        0         0        0        0         0        0
VM                    0        0         0        0        0         0        0

```

**Table 1** Description of the **display mac-address statistics** command output
| Item | Description |
| --- | --- |
| MAC type | Type of a MAC address entry.   * DYNAMIC: dynamic MAC address entry. * STATIC: static MAC address entry. * BLACKHOLE: black-hole MAC address entry. * OAM: OAM MAC address entry. * MUXVLAN: static MAC address entry delivered in the MUX VLAN, which does not overwrite a dynamic MAC address entry. * SECMAC: secure MAC address entry. * STICKYMAC: sticky MAC address entry. * MUXVLAN\_REMOTE: MAC address entry replicated in the MUX VLAN. * DHCP\_STICKY: DHCP sticky MAC address entry. * VM: virtual MAC address entry. |
| Ok | Normal return value. The value is a hexadecimal number. |
| Err | Return value of an error. The value is a hexadecimal number. |
| Internal | Bad request. |
| Param | Bad parameters. |
| Empty | No MAC address entry is available in the chip. |
| Notfound | The MAC address entries to be deleted do not exist in the chip. |
| Timeout | Timeout interval. |
| Full | The number of MAC address entries in the chip has reached the upper limit. |
| Exist | The MAC address entries to be delivered already exist in the chip. |