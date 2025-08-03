display inof configuration zone
===============================

display inof configuration zone

Function
--------



The **display inof configuration zone** command displays the iNOF zone configuration on the device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display inof configuration zone** [ *zone-name* ] [ **inconsistent** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *zone-name* | Specifies the name of an iNOF customized zone. | The value is a string of 1 to 63 case-sensitive characters. |
| **inconsistent** | Specifies the configuration of zones configured on only one reflector. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to check the iNOF zone configuration on the device.

**Precautions**

If the function for automatically adding hosts to the default zone is disabled, the information about the default zone is not displayed in the query result.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of a specified iNOF zone configured on only one reflector.
```
<HUAWEI> display inof configuration zone zone2 inconsistent
IPv4 Info:
Total Zone number: 4
iNOF Default-Zone: Enable

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.4.4                               192.168.109.151
----------------------------------------------------------------------------------

IPv6 Info:
Total Zone number: 4
iNOF Default-Zone: Enable

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:4::4                             2001:DB8:6::1
----------------------------------------------------------------------------------

```

# Display the iNOF zone configuration on the device when the default zone is enabled.
```
<HUAWEI> display inof configuration zone
IPv4 Info:
Total Zone number: 4
iNOF Default-Zone: Enable

ZoneName: Default
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.1.1                               192.168.109.151
192.168.1.1                               192.168.109.153
----------------------------------------------------------------------------------

ZoneName: zone1
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.2.2                               192.168.109.151
192.168.2.2                               192.168.109.153
----------------------------------------------------------------------------------

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.3.3                               192.168.109.151
192.168.3.3                               192.168.109.153
192.168.4.4                               192.168.109.151
----------------------------------------------------------------------------------

ZoneName: zone3
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.5.5                               192.168.109.151
----------------------------------------------------------------------------------

IPv6 Info:
Total Zone number: 4
iNOF Default-Zone: Enable

ZoneName: Default
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:1::1                             2001:DB8:6::1
2001:DB8:1::1                             2001:DB8:6::3
----------------------------------------------------------------------------------

ZoneName: zone1
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:2::2                             2001:DB8:6::1
2001:DB8:2::2                             2001:DB8:6::3
----------------------------------------------------------------------------------

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:3::3                             2001:DB8:6::1
2001:DB8:3::3                             2001:DB8:6::3
2001:DB8:4::4                             2001:DB8:6::1
----------------------------------------------------------------------------------

ZoneName: zone3
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:5::5                             2001:DB8:6::1
----------------------------------------------------------------------------------

```

# Display the iNOF zone configuration on the device when the default zone is disabled.
```
<HUAWEI> display inof configuration zone
IPv4 Info:
Total Zone number: 3
iNOF Default-Zone: Disable

ZoneName: zone1
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.2.2                               Local
192.168.2.2                               192.168.109.153
----------------------------------------------------------------------------------

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.3.3                               Local
192.168.3.3                               192.168.109.153
----------------------------------------------------------------------------------

ZoneName: zone3
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.4.4                               Local
192.168.5.5                               Local
----------------------------------------------------------------------------------

IPv6 Info:
Total Zone number: 3
iNOF Default-Zone: Disable

ZoneName: zone1
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:2::2                             Local
2001:DB8:2::2                             2001:DB8:6::3
----------------------------------------------------------------------------------

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:3::3                             Local
2001:DB8:3::3                             2001:DB8:6::3
----------------------------------------------------------------------------------

ZoneName: zone1
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:4::4                             Local
2001:DB8:5::5                             Local
----------------------------------------------------------------------------------

```

# Display information about the iNOF zones configured on only one reflector.
```
<HUAWEI> display inof configuration zone inconsistent
IPv4 Info:
Total Zone number: 3
iNOF Default-Zone: Disable

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.4.4                               192.168.109.151
----------------------------------------------------------------------------------

ZoneName: zone3
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.5.5                               192.168.109.151
----------------------------------------------------------------------------------

IPv6 Info:
Total Zone number: 3
iNOF Default-Zone: Disable

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:4::4                             2001:DB8:6::1
----------------------------------------------------------------------------------

ZoneName: zone3
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:5::5                             2001:DB8:6::1
----------------------------------------------------------------------------------

```

# Display the configuration of the specified iNOF zone.
```
<HUAWEI> display inof configuration zone zone2
IPv4 Info:
Total Zone number: 4
iNOF Default-Zone: Enable

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
192.168.3.3                               192.168.109.151
192.168.3.3                               192.168.109.153
192.168.4.4                               192.168.109.151
----------------------------------------------------------------------------------

IPv6 Info:
Total Zone number: 4
iNOF Default-Zone: Enable

ZoneName: zone2
----------------------------------------------------------------------------------
Host                                      Learned-From                            
----------------------------------------------------------------------------------
2001:DB8:3::3                             2001:DB8:6::1
2001:DB8:3::3                             2001:DB8:6::3
2001:DB8:4::4                             2001:DB8:6::1
----------------------------------------------------------------------------------

```

**Table 1** Description of the **display inof configuration zone** command output
| Item | Description |
| --- | --- |
| IPv4 Info | IPv4 information. |
| Total Zone number | Total number of zones configured in the current iNOF networking. If the default zone is enabled in the iNOF, the value includes the default zone. Otherwise, the value does not include the default zone. |
| iNOF Default-Zone | iNOF default zone status. The value can be either of the following:   * Disable: The iNOF default zone is disabled. * Enable: The iNOF default zone is enabled. |
| Host | The value can be either of the following:   * Host IP address. In the default zone, this value indicates the IP address of the local host. In the customized zone, this value indicates the IP address of the configured host. * --. In the default zone, this value indicates that no local host IP address exists. In the customized zone, this value indicates that no host IP address is configured. |
| Learned-From | The value can be either of the following:   * IP address of the iNOF reflector: The local device has learned zone information from the iNOF reflector. * Local: The local device has learned zone information from its access interfaces. |
| IPv6 Info | IPv6 information. |
| ZoneName | Domain name. |