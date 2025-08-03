display buffer optimization configuration
=========================================

display buffer optimization configuration

Function
--------



The **display buffer optimization configuration** command displays buffer optimization information, including the buffer size of each plane, buffer configuration of each interface, and distance-based headroom buffer check result.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display buffer optimization configuration slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the plane buffer optimization function is enabled, the device re-allocates the plane buffer. After distance-based headroom buffer check is enabled, the device measures the headroom buffer size required by the long-distance interface. You can run this command to view information about the buffer allocation of each plane and the distance-based headroom buffer check result.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display buffer optimization information.
```
<HUAWEI> display buffer optimization configuration slot 1
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Default
Current buffer optimization mode: Default
Interface that can be enabled with both PFC and buffer optimization:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8       400GE1/0/3       400GE1/0/4       400GE1/0/7       400GE1/0/8 

-----------------------------------------------------------------------------------------------------------------------
Pipe                       Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                         5120
   1                         5120
   2                         5120
   3                         5120
   4                         5120
   5                         5120

-----------------------------------------------------------------------------------------------------------------------
Interface        Port        Chip        Pipe       PFC          Mode         DetectHdrmResult     RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1         16           0           0       Enable       level-100               12496            12500
100GE1/0/2         20           0           0       Enable       level-100                   -            12500
-----------------------------------------------------------------------------------------------------------------------

```

# Display buffer optimization information. (Currently, the configured mode and the mode that takes effect are both the enhanced long-distance mode. Only the CE6860-SAN and CE8850-SAN support the enhanced long-distance mode.)
```
<HUAWEI> display buffer optimization configuration slot 1
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Enhanced-long-distance
Current buffer optimization mode: Enhanced-long-distance
Interface that can be enabled with both PFC and buffer optimization:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8       400GE1/0/3       400GE1/0/4       400GE1/0/7       400GE1/0/8 
Interface that can be enabled with ABS PFC:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8

-----------------------------------------------------------------------------------------------------------------------
Pipe                          Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                           14336
   1                            1024
   2                           38400
   3                            1024
   4                            1024
   5                            1024

-----------------------------------------------------------------------------------------------------------------------
Interface         Port       Chip        Pipe         PFC            Mode       DetectHdrmResult           RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1          16          0           0         Enable         level-100             12496                  12500
100GE1/0/2          20          0           0         Disable        level-100                 -                  12500
-----------------------------------------------------------------------------------------------------------------------

```

# Display buffer optimization information.
```
<HUAWEI> display buffer optimization configuration slot 1
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Long-distance
Current buffer optimization mode: Long-distance
Interface that can be enabled with both PFC and buffer optimization:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8       400GE1/0/3       400GE1/0/4       400GE1/0/7       400GE1/0/8 

-----------------------------------------------------------------------------------------------------------------------
Pipe                       Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                        20480
   1                         3072
   2                        20480
   3                         3072
   4                         3072
   5                         3072

-----------------------------------------------------------------------------------------------------------------------
Interface        Port        Chip        Pipe       PFC          Mode         DetectHdrmResult     RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1         16           0           0       Enable       level-100               12496            12500
100GE1/0/2         20           0           0       Enable       level-100                   -            12500
-----------------------------------------------------------------------------------------------------------------------

```

# Display buffer optimization information.
```
<HUAWEI> display buffer optimization configuration slot 1
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Long-distance
Current buffer optimization mode: Default
Interface that can be enabled with both PFC and buffer optimization:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8       400GE1/0/3       400GE1/0/4       400GE1/0/7       400GE1/0/8 

-----------------------------------------------------------------------------------------------------------------------
Pipe                       Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                         5120
   1                         5120
   2                         5120
   3                         5120
   4                         5120
   5                         5120

-----------------------------------------------------------------------------------------------------------------------
Interface        Port        Chip        Pipe       PFC          Mode         DetectHdrmResult     RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1         16           0           0       Enable       level-100               12496            12500
100GE1/0/2         20           0           0       Enable       level-100                   -            12500
-----------------------------------------------------------------------------------------------------------------------

```

# Display buffer optimization information.
```
<HUAWEI> display buffer optimization configuration slot 1
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Default
Current buffer optimization mode: Long-distance
Interface that can be enabled with both PFC and buffer optimization:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8       400GE1/0/3       400GE1/0/4       400GE1/0/7       400GE1/0/8 

-----------------------------------------------------------------------------------------------------------------------
Pipe                       Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                        20480
   1                         3072
   2                        20480
   3                         3072
   4                         3072
   5                         3072

-----------------------------------------------------------------------------------------------------------------------
Interface        Port        Chip        Pipe       PFC          Mode         DetectHdrmResult     RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1         16           0           0       Enable       level-100               12496            12500
100GE1/0/2         20           0           0       Enable       level-100                   -            12500
-----------------------------------------------------------------------------------------------------------------------

```

# Display buffer optimization information. (The configured enhanced long-distance mode does not take effect. Only the CE6860-SAN and CE8850-SAN support the enhanced long-distance mode.)
```
<HUAWEI> display buffer optimization configuration slot 1
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Enhanced-long-distance
Current buffer optimization mode: Default
Interface that can be enabled with both PFC and buffer optimization:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8       400GE1/0/3       400GE1/0/4       400GE1/0/7       400GE1/0/8 
Interface that can be enabled with ABS PFC:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8

-----------------------------------------------------------------------------------------------------------------------
Pipe                          Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                            5120
   1                            5120
   2                            5120
   3                            5120
   4                            5120
   5                            5120

-----------------------------------------------------------------------------------------------------------------------
Interface         Port       Chip        Pipe         PFC            Mode       DetectHdrmResult           RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1          16          0           0         Enable         level-100             12496                  12500
100GE1/0/2          20          0           0         Disable        level-100                 -                  12500
-----------------------------------------------------------------------------------------------------------------------

```

# Display buffer optimization information. (Currently, the long-distance mode takes effect, and the enhanced long-distance mode is configured. Only the CE6860-SAN and CE8850-SAN support the enhanced long-distance mode.)
```
<HUAWEI> display buffer optimization configuration slot 1
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Enhanced-long-distance
Current buffer optimization mode: Long-distance
Interface that can be enabled with both PFC and buffer optimization:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8       400GE1/0/3       400GE1/0/4       400GE1/0/7       400GE1/0/8 
Interface that can be enabled with ABS PFC:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8

-----------------------------------------------------------------------------------------------------------------------
Pipe                          Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                           20480
   1                            3072
   2                           20480
   3                            3072
   4                            3072
   5                            3072

-----------------------------------------------------------------------------------------------------------------------
Interface         Port       Chip        Pipe         PFC            Mode       DetectHdrmResult           RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1          16          0           0         Enable         level-100             12496                  12500
100GE1/0/2          20          0           0         Disable        level-100                 -                  12500
-----------------------------------------------------------------------------------------------------------------------

```

# Display buffer optimization information. (Currently, the enhanced long-distance mode takes effect, and the long-distance mode is configured. Only the CE6860-SAN and CE8850-SAN support the enhanced long-distance mode.)
```
<HUAWEI> display buffer optimization configuration slot 1
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Long-distance
Current buffer optimization mode: Enhanced-long-distance
Interface that can be enabled with both PFC and buffer optimization:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8       400GE1/0/3       400GE1/0/4       400GE1/0/7       400GE1/0/8 
Interface that can be enabled with ABS PFC:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8

-----------------------------------------------------------------------------------------------------------------------
Pipe                          Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                           14336
   1                            1024
   2                           38400
   3                            1024
   4                            1024
   5                            1024

-----------------------------------------------------------------------------------------------------------------------
Interface         Port       Chip        Pipe         PFC            Mode       DetectHdrmResult           RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1          16          0           0         Enable         level-100             12496                  12500
100GE1/0/2          20          0           0         Disable        level-100                 -                  12500
-----------------------------------------------------------------------------------------------------------------------

```

# Display buffer optimization information. (Currently, the enhanced long-distance mode takes effect. Only the CE6860-SAN and CE8850-SAN support the enhanced long-distance mode.)
```
<HUAWEI> display buffer optimization configuration slot 1
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Default
Current buffer optimization mode: Enhanced-long-distance
Interface that can be enabled with both PFC and buffer optimization:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8       400GE1/0/3       400GE1/0/4       400GE1/0/7       400GE1/0/8 
Interface that can be enabled with ABS PFC:
100GE1/0/1       100GE1/0/2       100GE1/0/3       100GE1/0/4       100GE1/0/5       100GE1/0/6       100GE1/0/7        
100GE1/0/8

-----------------------------------------------------------------------------------------------------------------------
Pipe                          Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                           14336
   1                            1024
   2                           38400
   3                            1024
   4                            1024
   5                            1024

-----------------------------------------------------------------------------------------------------------------------
Interface         Port       Chip        Pipe         PFC            Mode       DetectHdrmResult           RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1          16          0           0         Enable         level-100             12496                  12500
100GE1/0/2          20          0           0         Disable        level-100                 -                  12500
-----------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display buffer optimization configuration** command output
| Item | Description |
| --- | --- |
| Buffer unit | Buffer unit. |
| Buffer | Buffer size. |
| Configure buffer optimization mode | Buffer optimization mode. The options are as follows:   * Default: The plane buffer optimization mode is not configured. * Long-distance: The plane buffer optimization mode is long-distance mode. * Enhanced-long-distance: The plane buffer optimization mode is enhanced long-distance mode. |
| Current buffer optimization mode | Buffer optimization mode that takes effect currently. The options are as follows:   * Default: The plane buffer optimization mode is not configured or the configured plane buffer optimization mode does not take effect. * Long-distance: The plane buffer optimization mode that takes effect is long-distance mode. * Enhanced-long-distance: The plane buffer optimization mode that takes effect is enhanced long-distance mode. |
| Interface | Interface. |
| Interface that can be enabled with both PFC and buffer optimization | Interfaces that support both PFC and plane buffer optimization. |
| Interface that can be enabled with ABS PFC | Interfaces that support antilocking PFC. |
| PFC | Whether PFC is enabled on an interface. |
| Pipe | Plane ID. |
| Port | Interface number. |
| Chip | Chip ID. |
| Mode | Interface long-distance mode set for distance-based headroom buffer check. |
| DetectHdrmResult | Based on the detection packets, distance-based headroom buffer check calculates the headroom space required for zero-packet-loss transmission on the current link.  If - is displayed, the detection fails. |
| RequiredHdrm | Theoretically required headroom buffer space that is calculated using distance-based headroom buffer check based on the configured long-distance mode of the interface. |