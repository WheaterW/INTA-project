display lldp mdn neighbor
=========================

display lldp mdn neighbor

Function
--------



The **display lldp mdn neighbor** command displays MAC address discovery neighbor (MDN) information about a specific or all interfaces.




Format
------

**display lldp mdn neighbor** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays MDN neighbor information on a specified interface.  If this parameter is not specified, MDN neighbor information on all interfaces is displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view MDN neighbor information, run the display lldp mdn neighbor command. The command output helps check MDN neighbors, Layer 2 information about these neighbors, and interfaces used by these neighbors to connect to the local device.To view the MDN neighbors of the local device and the MAC addresses of these MDN neighbors, run the display lldp mdn neighbor command.



**Prerequisites**



LLDP has been enabled using the lldp enable command in the system view, and MDN has been enabled on interfaces using the lldp mdn enable command in the interface view.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display MDN neighbor information about all interfaces.
```
<HUAWEI> display lldp mdn neighbor
10GE1/0/1 has 1 neighbors:

Neighbor index                     :1
Device ID                          :HUAWEI
Port ID                            :10GE1/0/4
Version                            :--
Platform                           :Huawei Versatile Routing Platform Software
VRP (R) software, Version 8.211 (XXXXXX XXXXXX)
Copyright (C) 2012-2021 Huawei Technologies Co., Ltd.
HUAWEI XXXXXX

Capabilities                       :router switch igmp-capable
MacAddress                         :0024-972b-510b
Discovered time                    :2021-10-16 17:15:46
Expired time                       :169s
Power drawn                        :--
Power request ID                   :--
Power management ID                :--
Power request levels               :--

```

**Table 1** Description of the **display lldp mdn neighbor** command output
| Item | Description |
| --- | --- |
| Neighbor index | Index of an MDN neighbor. |
| Device ID | Device ID of the MDN neighbor. |
| Port ID | Interface information about the MDN neighbor. |
| Version | Version of the MDN neighbor. |
| Platform | Platform information about the MDN neighbor. |
| Capabilities | The MDN neighbor device supports the following functions:   * router: router function. * transparent-bridge: transparent bridge function. * source-router-bridge: source route bridge. * switch: switch function. * host: host function. * igmp-capable: IGMP supported. * repeater: repeater function. * phone: phone function. |
| MacAddress | MAC address of an MDN neighbor. |
| Discovered time | Date and time when an MDN neighbor was discovered. |
| Expired time | Aging time (in seconds) of information about an MDN neighbor. |
| Power drawn | Power consumption. |
| Power request ID | Power request ID. |
| Power management ID | Indicates the power management ID. |
| Power request levels | Power request level. |