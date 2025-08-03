display port high-precision rate detection result
=================================================

display port high-precision rate detection result

Function
--------



The **display port high-precision rate detection result** command displays the high-precision rate detection result of an interface.




Format
------

**display port high-precision rate detection result**


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



After the port high-precision rate detection of a port is enabled, you can run this command to query the result of the high-precision rate detection of the port.



**Prerequisites**



Before running the query command, run the **port high-precision rate detection** command to enable the high-precision rate detection function. Otherwise, the query result is empty.



**Precautions**



When the high-precision rate detection function is enabled on an interface, the last detection result is cleared.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the high-precision rate detection result of an interface.
```
<HUAWEI> display port high-precision rate detection result
Interface                     : 10GE1/0/1
Configured detection duration : 120 Min
Detection start time          : 07-08-2020 07:21:09
Detection end time            : --
Average input rate            : 10 Mbits/sec
Average output rate           : 9 Mbits/sec

Top 10 input rate:
-------------------------------------------
Time                 Input Rate(Mbits/sec)
-------------------------------------------
07-08-2020 08:21:29:023                  8
07-08-2020 07:20:09:098                  8
07-08-2020 07:18:09:012                  7
07-08-2020 07:21:09:002                  7
07-08-2020 08:28:19:059                  6
07-08-2020 07:23:10:038                  6
07-08-2020 07:23:09:015                  5
07-08-2020 08:22:22:034                  5
07-08-2020 07:11:09:005                  4
07-08-2020 07:11:01:954                  4
-------------------------------------------

Top 10 output rate:
-------------------------------------------
Time                 Output Rate(Mbits/sec)
-------------------------------------------
07-08-2020 07:31:09:034                  10
07-08-2020 08:21:09:049                  10
07-08-2020 08:22:19:056                   9
07-08-2020 08:11:09:460                   9
07-08-2020 08:21:29:099                   9
07-08-2020 07:33:09:431                   8
07-08-2020 07:55:09:582                   7
07-08-2020 07:55:19:959                   7
07-08-2020 08:29:09:054                   6
07-08-2020 07:44:09:730                   6
-------------------------------------------

```

**Table 1** Description of the **display port high-precision rate detection result** command output
| Item | Description |
| --- | --- |
| Interface | Interface to be detected. |
| Configured detection duration | Indicates the configured detection duration, in minutes. |
| Detection start time | Time when the high-precision detection function is enabled. |
| Detection end time | Indicates the end time of high-precision rate detection.  --: The high-precision rate detection is not complete. |
| Average input rate | Indicates the average inbound rate in a high-precision rate detection period. |
| Average output rate | Indicates the average outbound rate in a high-precision rate detection period. |
| Top 10 input rate | Maximum 10 inbound rate detected. |
| Top 10 output rate | Maximum 10 detected outbound rates. |
| Time | Time when the detected high-precision rate is generated. |
| Input Rate | Indicates the high-precision rate in the inbound direction, in Mbit/s. |
| Output Rate | Indicates the high-precision rate in the outbound direction, in Mbit/s. |