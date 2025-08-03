display isis frr summary
========================

display isis frr summary

Function
--------



The **display isis frr summary** command displays the FRR protection rates of routes in an IS-IS process.




Format
------

**display isis frr summary** [ **level-1** | **level-2** | **level-1-2** ] [ *process-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Displays the FRR protection rates of Level-1 routes. | - |
| **level-2** | Displays the FRR protection rates of Level-2 routes. | - |
| **level-1-2** | Displays the FRR protection rates of all levels of routes. | - |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the IS-IS Auto FRR function is configured, you can run the display isis frr summary command to check the FRR protection rates of routes at different convergence priorities in an IS-IS process.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the FRR protection rates of routes in an IS-IS process.
```
<HUAWEI> display isis frr summary
                                 ISIS(1) Level-1 IPv4 Frr summary
                                 --------------------------------
Priority:                        Critical        High            Medium          Low             Total           
All reachable prefix counts:     0               0               3               5               8                       
Protected counts:                0               0               3               1               4                  
Coverage:                        0%              0%              100%            20%             50%               

                                 ISIS(1) Level-2 IPv4 Frr summary
                                 --------------------------------
Priority:                        Critical        High            Medium          Low             Total           
All reachable prefix counts:     0               0               3               5               8                       
Protected counts:                0               0               0               0               0                  
Coverage:                        0%              0%              0%              0%              0%

```

**Table 1** Description of the **display isis frr summary** command output
| Item | Description |
| --- | --- |
| Total | Summary IS-IS route statistics of all convergence priorities. |
| All reachable prefix counts | Number of IS-IS routes at each convergence priority. |
| Protected counts | Number of protected IS-IS routes at each convergence priority. |
| Priority | Convergence priority of a route:   * Critical. * High. * Medium. * Low. |
| Coverage | FRR protection rate of routes with different convergence priorities. The formula is Coverage = Protected counts/All reachable prefix counts x 100%. |