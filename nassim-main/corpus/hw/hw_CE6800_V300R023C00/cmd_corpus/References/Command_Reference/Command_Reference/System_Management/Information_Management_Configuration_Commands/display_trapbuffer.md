display trapbuffer
==================

display trapbuffer

Function
--------



The **display trapbuffer** command displays traps in a trap buffer.




Format
------

**display trapbuffer** [ **size** *buffersize* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **size** *buffersize* | Displays traps in a trap buffer. If no parameter is specified, all traps in the trap buffer are displayed. | The value is an integer ranging from 1 to 1024. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view traps in the trap buffer, run the **display trapbuffer** command.

**Precautions**

If there are a large number of traps on the device, running the **display trapbuffer** command to display specified trap amount is recommended. Otherwise, the following problems may occur due to excessive traps:

* The displayed information is repeatedly refreshed, causing desired information unable to be located.
* The system does not respond because of long-time information traversing and searching.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display traps in a trap buffer.
```
<HUAWEI> display trapbuffer
Trapping buffer configuration and contents : enabled
Allowed max buffer size : 1024
Actual buffer size : 256
Channel number : 3 , Channel name : trapbuffer
Dropped messages : 0
Overwritten messages : 
Current messages : 187
Apr 23 2020 19:20:32 HUAWEI %%01STANDARD/6/linkup:CID=0x807a271c-OID=1.3.6.1.6.3.1.1.5.4;The interface status changes. (ifName=Ethernet1/0/1, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is Up.)

```

# Display three traps in the trap buffer.
```
<HUAWEI> display trapbuffer size 3
Trapping buffer configuration and contents : enabled
Allowed max buffer size : 1024
Channel number : 3 , Channel name : trapbuffer
Actual buffer size : 256
Dropped messages : 0
Overwritten messages : 0
Current messages : 187
Apr 23 2020 19:20:32 HUAWEI %%01STANDARD/6/linkup:CID=0x807a271c-OID=1.3.6.1.6.3.1.1.5.4;The interface status changes. (ifName=Ethernet1/0/1, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is Up.)
Apr 23 2020 19:20:32 HUAWEI %%01STANDARD/6/linkup:CID=0x807a271c-OID=1.3.6.1.6.3.1.1.5.4;The interface status changes. (ifName=Ethernet1/0/1.125, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is Up.)
Apr 23 2020 19:20:32 HUAWEI %%01STANDARD/6/linkup:CID=0x807a271c-OID=1.3.6.1.6.3.1.1.5.4;The interface status changes. (ifName=Ethernet1/0/1.124, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is Up.)

```

**Table 1** Description of the **display trapbuffer** command output
| Item | Description |
| --- | --- |
| Trapping buffer configuration and contents | Status of the trap buffer:   * enabled. * disabled. |
| Allowed max buffer size | Maximum size of the trap buffer. |
| Actual buffer size | Used size of the trap buffer. |
| Channel number | Channel number. |
| Channel name | Channel name. |
| Dropped messages | Number of dropped messages. |
| Overwritten messages | Number of overwritten messages. |
| Current messages | Number of existing messages. |