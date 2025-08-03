display inof configuration host
===============================

display inof configuration host

Function
--------



The **display inof configuration host** command displays the configuration of iNOF zone members on the device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display inof configuration host** [ **inconsistent** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inconsistent** | Displays the configuration of hosts on only one reflector. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check the configuration of iNOF zone members on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of iNOF zone members on the device.
```
<HUAWEI> display inof configuration host
IPv4 Info:

Host:192.168.1.1
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
Local                                    zone1
192.168.2.1                              zone1
----------------------------------------------------------------------------------

Host:192.168.1.2
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
192.168.2.1                              zone2
----------------------------------------------------------------------------------

Host:192.168.1.3
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
192.168.2.1                              zone3
----------------------------------------------------------------------------------

IPv6 Info:

Host:2001:DB8:1::1
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
Local                                    zone1
2001:DB8:2::1                            zone1
----------------------------------------------------------------------------------

Host:2001:DB8:1::2
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
2001:DB8:2::1                            zone2
----------------------------------------------------------------------------------

Host:2001:DB8:1::3
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
2001:DB8:2::1                            zone3
----------------------------------------------------------------------------------

```

# Display the configuration of hosts on only one reflector.
```
<HUAWEI> display inof configuration host inconsistent
IPv4 Info:

Host:192.168.1.2
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
192.168.2.1                              zone2
----------------------------------------------------------------------------------

Host:192.168.1.3
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
192.168.2.1                              zone3
----------------------------------------------------------------------------------

IPv6 Info:

Host:2001:DB8:1::2
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
2001:DB8:2::1                            zone2
----------------------------------------------------------------------------------

Host:2001:DB8:1::3
----------------------------------------------------------------------------------
Learned-From                             ZoneName
----------------------------------------------------------------------------------
2001:DB8:2::1                            zone3
----------------------------------------------------------------------------------

```

**Table 1** Description of the **display inof configuration host** command output
| Item | Description |
| --- | --- |
| IPv4 Info | IPv4 information. |
| Learned-From | The value can be either of the following:   * If the IP address of the iNOF reflector is displayed, the local device has learned host information from the iNOF reflector. * If Local is displayed, the local device has learned host information from its access interfaces. |
| ZoneName | Zone name. |
| IPv6 Info | IPv6 information. |
| Host | Host. |