display mac-address bpdu
========================

display mac-address bpdu

Function
--------



The **display mac-address bpdu** command displays the BPDU MAC address configured on a device.




Format
------

**display mac-address bpdu**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the configured or default BPDU MAC address, run the display bpdu-mac command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the BPDU MAC address.
```
<HUAWEI> display mac-address bpdu
 Maximum BPDU MAC address allowed : 128
 Remaining BPDU MAC address allowed : 124

 Configured BPDU MAC address
 ----------------------------------------------------------------------------
 (001) 010f-e200-0001                   (002) 0180-c200-0000/ffff-ffff-ffc0
 (003) 0180-c200-008a                   (004) 0180-c200-8585

```

**Table 1** Description of the **display mac-address bpdu** command output
| Item | Description |
| --- | --- |
| Maximum BPDU MAC address allowed | Maximum number of BPDU MAC addresses that can be configured on the device. |
| Remaining BPDU MAC address allowed | Number of BPDU MAC addresses that can still be configured on the device. |