display inof rpfr connection information
========================================

display inof rpfr connection information

Function
--------

The **display inof rpfr connection information** command displays RPFR RoCE connection information.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6885-SAN and CE8850-SAN.



Format
------

**display inof rpfr connection information**


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

You can run this command to view RPFR RoCE connection information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display RPFR RoCE connection information.
```
<HUAWEI> display inof rpfr connection information
Total Num: 2
----------------------------------------------------------------------------------------
DIP                SIP                    AccessInterface   QueueNum       DelayTime(ms)
----------------------------------------------------------------------------------------
192.168.1.1        192.168.1.2            100GE1/0/1               9                 100 
192.168.2.1        192.168.2.2            100GE1/0/2               5                 100 
----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display inof rpfr connection information** command output
| Item | Description |
| --- | --- |
| Total Num | Total number of RoCE connections on all storage nodes connected to the device. |
| DIP | Destination IP address, that is, the IP address of the compute node. |
| SIP | Source IP address, that is, the IP address of the storage node. |
| AccessInterface | Access interface, that is, the access interface of the storage node on the local device. |
| QueueNum | Number of RoCE connection queues. |
| DelayTime | Delay in sending proxy packets. |