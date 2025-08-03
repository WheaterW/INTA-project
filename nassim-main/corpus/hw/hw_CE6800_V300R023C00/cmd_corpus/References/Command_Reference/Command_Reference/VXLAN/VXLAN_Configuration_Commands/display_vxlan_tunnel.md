display vxlan tunnel
====================

display vxlan tunnel

Function
--------



The **display vxlan tunnel** command displays VXLAN tunnel information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vxlan tunnel** [ *tunnel-id* ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tunnel-id* | Specifies a VXLAN tunnel ID. | The value is an integer ranging from 1 to 4294967295. |
| **verbose** | Displays detailed VXLAN tunnel information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After VXLAN tunnels are established, run the **display vxlan tunnel** command to check tunnel information. The command output helps verify configurations and locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display VXLAN tunnel information.
```
<HUAWEI> display vxlan tunnel
Number of vxlan tunnel : 3
Tunnel ID   Source                Destination           State  Type          Uptime
----------------------------------------------------------------------------------------------------------
4026531844  1.1.1.1               2.2.2.2               up     static        03:12:33
4026531846  1.1.1.1               3.3.3.3               up     static        12:23:45
4026531847  1.1.1.1               4.4.4.4               down   static        -

```

# Display detailed VXLAN tunnel information.
```
<HUAWEI> display vxlan tunnel 4026531841 verbose
    Tunnel ID              : 4026531841
    Source                 : 1.1.1.1
    Destination            : 2.2.2.2
    State                  : up
    Type                   : static
    BypassVxlan            : true
    Uptime                 : 02:22:13

```

**Table 1** Description of the **display vxlan tunnel** command output
| Item | Description |
| --- | --- |
| Number of vxlan tunnel | Number of VXLAN tunnels that have been established. |
| Tunnel ID | VXLAN tunnel ID, which is automatically allocated after a VXLAN tunnel is established. |
| Source | VXLAN tunnel source IP address. |
| Destination | VXLAN tunnel destination IP address. |
| State | VXLAN tunnel status:   * up: The tunnel is reachable. * down: The tunnel is unreachable. |
| Type | VXLAN tunnel type.   * static: peer-list is statically configured. * dynamic: peer-list is dynamically learned by a routing protocol. |
| Uptime | Period during which a VXLAN tunnel is Up.   * If the period is less than 24 hours, the displayed format is hh:mm:ss, where hh, mm, and ss stand for hours, minutes, and seconds, respectively. * If the period is greater than 24 hours but less than 9999 hours, the displayed format is xxxxhxxm. For example, a period of 30 hours and 26 minutes is displayed as 0030h26m. * If the period is greater than 9999 hours, the number of hours is displayed as four asterisks (\*\*\*\*). For example, a period of 10000 hours and 26 minutes is displayed as \*\*\*\*h26m.   If a hyphen (-) is displayed, the VXLAN tunnel is Down. |
| BypassVxlan | Indicates whether the bypass VXLAN tunnel exists:   * true. * false. |