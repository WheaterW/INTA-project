display mac-address limit
=========================

display mac-address limit

Function
--------



The **display mac-address limit** command displays MAC address learning limit rules.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display mac-address limit**

**display mac-address limit vlan** *vlan-id*

**display mac-address limit** { *interface-name* | *interface-type* *interface-number* }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display mac-address limit** { *nve-interface-name* | *nvePortType* *nvePortNum* } **peer** *ip-address*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display mac-address limit bridge-domain** *bd-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| **vlan** *vlan-id* | Displays the MAC address entry limit in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *nve-interface-name* | Specifies the name of an NVE interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 47. |
| *nvePortType* | Displays the type of an NVE interface.  Only the CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8851K, CE8850-SAN, CE8850-HAM, CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE6863H, CE6863H-K, CE6881H, and CE6881H-K support this parameters.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *nvePortNum* | Displays the number of an NVE interface.  Only the CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8851K, CE8850-SAN, CE8850-HAM, CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE6863H, CE6863H-K, CE6881H, and CE6881H-K support this parameters.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **peer** *ip-address* | Specifies the IP address of a static VXLAN tunnel's remote VTEP for which a MAC address learning limit rule has been configured.  Only the CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8851K, CE8850-SAN, CE8850-HAM, CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE6863H, CE6863H-K, CE6881H, and CE6881H-K support this parameters.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in dotted decimal notation. |
| **bridge-domain** *bd-id* | Specifies the BD ID.  Only the CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8851K, CE8850-SAN, CE8850-HAM, CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE6863H, CE6863H-K, CE6881H, and CE6881H-K support this parameters.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the MAC address learning limit rules configured, you can use the **display mac-address limit** command. The command output helps check whether configurations are correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display MAC address learning limit rules.
```
<HUAWEI> display mac-address limit
MAC limit is enabled
Total MAC limit rule count : 1

Port                 VLAN/VSI/SI/BD   Slot Maximum Action  Alarm  
----------------------------------------------------------------------------
100GE1/0/1              -             <slot_1>      100     forward enable

```

**Table 1** Description of the **display mac-address limit** command output
| Item | Description |
| --- | --- |
| MAC limit is enabled | MAC address learning limit is enabled. |
| Total MAC limit rule count | Total number of MAC address learning limit rules. |
| Maximum | Maximum number of MAC addresses that can be learned. |
| Action | Action taken after the maximum number of MAC addresses is reached:   * discard. * forward. |
| Alarm | Whether an alarm is reported when the number of learned MAC addresses reaches the limit:   * enable: reports alarms. * disable: does not report alarms. |
| Port | Port on which the MAC address learning limit is configured. |
| VLAN/VSI/SI/BD | VLAN ID, BD name, or VSI name of the interface. |