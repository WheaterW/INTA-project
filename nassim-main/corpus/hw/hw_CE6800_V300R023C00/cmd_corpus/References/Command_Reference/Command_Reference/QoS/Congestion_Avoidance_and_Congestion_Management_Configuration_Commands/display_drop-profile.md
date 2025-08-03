display drop-profile
====================

display drop-profile

Function
--------



The **display drop-profile** command displays the configuration of a WRED drop profile. If no parameter is specified, brief information about all WRED drop profiles is displayed.




Format
------

**display drop-profile** [ *drop-profile-name* | **brief** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *drop-profile-name* | Displays detailed information about a WRED drop profile with the specified name. | The value must be the name of an existing drop profile on the device. |
| **brief** | Displays brief information about all WRED drop profiles. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can use the **display drop-profile** command to view the number of configured drop profiles and all configuration of a specified drop profile.

**Precautions**



If the brief and drop-profile-name parameters are not specified, detailed information about all drop profiles is displayed.For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, and CE8850-HAM:You can configure a maximum of 16 drop profiles, including the default drop profile. The default drop profile can be modified but cannot be deleted.For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, and CE6885-LL (low latency mode):You can configure a maximum of 63 drop profiles, including the default drop profile. The default drop profile can be modified but cannot be deleted.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about all drop profiles on the device (for the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K and CE6820S).
```
<HUAWEI> display drop-profile
Drop-profile[1]: default
Color    Mode         Low-limit   High-limit  Unit     Discard(%)
-----------------------------------------------------------------
Green    Percentage   100         100         %        100
Yellow   Percentage   100         100         %        100
Red      Percentage   100         100         %        100
-----------------------------------------------------------------
Drop-profile[2]: dp1
Color    Mode         Low-limit   High-limit  Unit     Discard(%)
-----------------------------------------------------------------
Green    Percentage   100         100         %        100
Yellow   Percentage   100         100         %        100
Red      Percentage   100         100         %        100
-----------------------------------------------------------------

```

# Display detailed information about all drop profiles on the device (for the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T and CE6863E-48S8CQ).
```
<HUAWEI> display drop-profile
Drop-profile[1]: default                                         
Color    Mode         Low-limit   High-limit  Unit    Discard(%)  
-----------------------------------------------------------------
Green    Percentage   100         100         %       100         
Yellow   Percentage   100         100         %       100         
Red      Percentage   100         100         %       100         
ECN      Percentage   100         100         %       100         
-----------------------------------------------------------------
Drop-profile[2]: dp1                                             
Color    Mode         Low-limit   High-limit  Unit    Discard(%)  
-----------------------------------------------------------------
Green    Buffer-size  256         90000       Bytes   90          
Yellow   Percentage   100         100         %       100         
Red      Percentage   100         100         %       100         
ECN      Percentage   100         100         %       100         
-----------------------------------------------------------------

```

# Display brief information about all drop profiles on the device.
```
<HUAWEI> display drop-profile brief
Drop-profile Maximum: 16
Total: 1
-----------------------------------------------------------------                                                                                                 
        index               drop-profile name                                                                                       
-----------------------------------------------------------------                                                                   
        1                   default                                                                                                 
-----------------------------------------------------------------

```
```
<HUAWEI> display drop-profile brief
Drop-profile Maximum: 63
Total: 1
-----------------------------------------------------------------                                                                                                 
        index               drop-profile name                                                                                       
-----------------------------------------------------------------                                                                   
        1                   default                                                                                                 
-----------------------------------------------------------------

```

**Table 1** Description of the **display drop-profile** command output
| Item | Description |
| --- | --- |
| drop-profile name | Drop profile name. |
| Color | Color of the packets. The values are as follows:  -Green.  -Yellow.  -Red.  To set the color of packets, run the color command. |
| Mode | Configuration mode of threshold:  -Buffer-size.  -Percentage. |
| Low-limit | Lower drop threshold, in percentage. |
| High-limit | Upper drop threshold, in percentage. |
| Unit | The configuration mode of threshold is buffer-size, in bytes.  The configuration mode of threshold is percentage, in percentage. |
| Drop-profile Maximum | Maximum number of drop profiles supported by the device. |
| index | Drop profile index. |
| Total | Number of configured drop profiles. |
| Drop-profile[1] | Drop profile name in which 1 indicates the drop profile index. |
| Discard | Maximum drop probability, in percentage. |