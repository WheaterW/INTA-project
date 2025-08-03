display qos buffer-usage
========================

display qos buffer-usage

Function
--------



The **display qos buffer-usage** command sets the buffer usage in the system or on an interface.




Format
------

**display qos buffer-usage interface** { *interface-name* | *interface-type* *interface-number* }

**display qos buffer-usage** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters, spaces not supported. |
| **slot** *slot-id* | Displays the buffer usage of a specified device. | The value is an integer that ranges from 1 to 16. |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run the display qos buffer-usage command to view the buffer usage of the system or an interface. If you do not specify any parameter, this command displays the buffer usage of the system.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the buffer usage of a specified interface.
```
<HUAWEI> display qos buffer-usage interface 10GE 1/0/1
Total         : 6272 cells (1274 KBytes)
Current used  : 0 cells (0 KBytes)  
Remained      : 6272 cells (1274 KBytes)  
Peak used     : 0 cells (0 KBytes)
Average used  : 0 cells (0 KBytes)
                          
Buffer Usage on each Queue: (cells/KBytes)    
-----------------------------------------------------------------------------   
QueueIndex      Current        Peak        Average        
-----------------------------------------------------------------------------   
0                 0/0           0/0          0/0  
1                 0/0           0/0          0/0  
2                 0/0           0/0          0/0   
3                 0/0           0/0          0/0 
4                 0/0           0/0          0/0
5                 0/0           0/0          0/0 
6                 0/0           0/0          0/0
7                 0/0           0/0          0/0 
-----------------------------------------------------------------------------

```

# Display the buffer usage of the device.
```
<HUAWEI> display qos buffer-usage
------------------------------------------------------------------------------- 
Slot          : 1  
Total         : 20160 cells (4095 KBytes)
Current used  : 0 cells (0 KBytes)
Remained      : 20160 cells (4095 KBytes)
Peak used     : 0 cells (0 KBytes)
Average used  : 0 cells (0 KBytes)
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display qos buffer-usage** command output
| Item | Description |
| --- | --- |
| Total | Total buffer. |
| Current used | Used buffer. |
| Current | Used buffer of the queue. |
| Remained | Remaining buffer. |
| Peak used | Peak value of the used buffer. |
| Peak | Peak value of the used buffer of the queue. |
| Average used | Average value of the used buffer. |
| Average | Average value of the used buffer of the queue. |
| Buffer Usage on each Queue | Buffer usage of each interface queue. |
| QueueIndex | Queue ID. |
| Slot | ID of the device. |