display rawlink status
======================

display rawlink status

Function
--------



The **display rawlink status** command displays information about IPv4 RawLink connections.




Format
------

**display rawlink status** [ **cid** *pidval* ] [ **socket-id** *fd* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cid** *pidval* | Displays information about the RawLink connection with a specified APP CID. | The value is an integer ranging from 0 to ffffffff. |
| **socket-id** *fd* | Displays information about the RawLink connection with a specified socket ID. | The value is an integer ranging from 0 to 2147418111. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Run the display rawlink status command to check the following information about each valid IPv4 RawLink connection on a device:

* RawLink socket ID
* APP CIDNo information is displayed if there is no RawLink connection on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about IPv4 RawLink connections.
```
<HUAWEI> display rawlink status
-------------------
Cid        SocketId
-------------------
0x80692723        2       
0x80692723        3       
-------------------

```

**Table 1** Description of the **display rawlink status**  command output
| Item | Description |
| --- | --- |
| Cid | APP CID. |
| SocketId | IPv4 RawLink socket ID. |