display default-parameter bmp
=============================

display default-parameter bmp

Function
--------



The **display default-parameter bmp** command displays default BGP Monitoring Protocol (BMP) configurations.




Format
------

**display default-parameter bmp**


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



To check the default interval at which a router sends BGP running statistics to a monitoring server and whether statistics about all received routes or only accepted routes are sent to the monitoring server, run the **display default-parameter bmp** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display default BMP configurations.
```
<HUAWEI> display default-parameter bmp
statistics-timer : 3600
route-mode : post-policy

```

**Table 1** Description of the **display default-parameter bmp** command output
| Item | Description |
| --- | --- |
| statistics-timer | Interval at which the router sends BGP running statistics to the monitoring server, in seconds. |
| route-mode | Whether statistics about all received routes or only accepted routes are sent to the monitoring server. |