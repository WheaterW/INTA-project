display radius-server accounting-stop-packet
============================================

display radius-server accounting-stop-packet

Function
--------



The **display radius-server accounting-stop-packet** command displays information about Accounting-Stop packets on the RADIUS server.




Format
------

**display radius-server accounting-stop-packet** { **all** | **ip** *ip-address* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays all Accounting-Stop packets. | - |
| **ip** *ip-address* | Displays the Accounting-Stop packets with the specified IP address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The display radius-server accounting-stop-packet command output helps you check configurations or isolate faults.Note: When there are a large number of Accounting-Stop packets, the total number of Accounting-Stop packets is accurate. However, to ensure user-friendly display, only some detailed data is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the Accounting-Stop packets with the IP address being 10.138.104.32.
```
<HUAWEI> display radius-server accounting-stop-packet ip 10.138.104.32
 ------------------------------------------------------------------------------ 
 Time Stamp  Resend Times  Session Time  Username                               
 ------------------------------------------------------------------------------ 
 1980409     6             22            g@rds                                  
 ------------------------------------------------------------------------------ 
 Total: 1, printed: 1

```

**Table 1** Description of the **display radius-server accounting-stop-packet** command output
| Item | Description |
| --- | --- |
| Time Stamp | Time when an Accounting-Stop packet is placed into the buffer queue. |
| Resend Times | Number of times that Accounting-Stop packets have been retransmitted. |
| Session Time | Session time, in seconds. |
| Username | User name. |