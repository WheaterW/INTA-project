display qos micro-burst status all
==================================

display qos micro-burst status all

Function
--------



The **display qos micro-burst status all** command displays information about all interfaces enabled with microburst detection and packet loss information on the interfaces.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display qos micro-burst status all**


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

**Usage Scenario**



You can run the **display qos micro-burst status all** command to view information about all interfaces enabled with microburst detection and packet loss information on the interfaces.



**Prerequisites**

1. The microburst detection function has been enabled on the device using the **qos micro-burst detection** [ **enhanced** ] **enable** **slot** slot-id command in the system view.
2. The microburst detection function has been enabled on an interface using the **qos micro-burst detection enable** command in the interface view.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# In default microburst detection mode, display all interfaces enabled with microburst detection and packet loss information on the interfaces.
```
<HUAWEI> display qos micro-burst status all
Slot 1                     Mode: default(5ms)
---------------------------------------------
Interface                  Discard(packets)  
---------------------------------------------
10GE1/0/1                                 0
10GE1/0/2                                 0
---------------------------------------------

```

**Table 1** Description of the **display qos micro-burst status all** command output
| Item | Description |
| --- | --- |
| Slot | ID of a slot enabled with microburst detection. |
| Interface | Interface enabled with microburst detection. |
| Mode | Microburst detection mode:   * default(5ms): In default mode, the packet sampling interval is 5 ms. * enhanced(1ms): In enhanced mode, the packet sampling interval is 1 ms. |
| Discard | Number of discarded packets. |