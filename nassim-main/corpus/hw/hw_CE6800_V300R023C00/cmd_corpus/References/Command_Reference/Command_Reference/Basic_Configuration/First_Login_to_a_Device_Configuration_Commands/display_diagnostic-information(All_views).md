display diagnostic-information(All views)
=========================================

display diagnostic-information(All views)

Function
--------



The **display diagnostic-information** command displays diagnostic information about the current system.




Format
------

**display diagnostic-information** [ *module-name* ] &<1-8> [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *module-name* | Displays diagnostic file information for the specified module. | The value is of the enumerated type and must be set according to the device configuration. |
| **slot** *slot-id* | Displays diagnostic file information about a specified slot. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. Set the value according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If a fault occurs in the system, you can run this command to collect information for fault locating if a faulty module cannot be determined.

**Precautions**

* Running this command may cause high CPU usage for a short period of time.
* This command displays only diagnostic information on the terminal screen.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the high-level diagnostic information about the SMP module.
```
<HUAWEI> display diagnostic-information level high smp
=============================================================================== 
                 display version                                                
=============================================================================== 
                                                                                
                                                                                
                                                                                
=============================================================================== 
                 display patch-information                                      
=============================================================================== 
                                                                                
Info: No patch exists.                                                          
The current state is: Idle                                                      
                                                                                
=============================================================================== 
                 display alarm active verbose                                   
=============================================================================== 
                                                                                
                                                                                
                                                                                
=============================================================================== 
                 display current-configuration                                  
=============================================================================== 
                                                                                
!Software Version V800R011C00B001                                               
!Last configuration was updated at 2015-05-07 10:18:40+00:00

```