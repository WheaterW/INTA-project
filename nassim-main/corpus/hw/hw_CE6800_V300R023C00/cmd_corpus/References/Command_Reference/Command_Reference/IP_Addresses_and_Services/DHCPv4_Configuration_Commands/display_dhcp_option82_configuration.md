display dhcp option82 configuration
===================================

display dhcp option82 configuration

Function
--------



The **display dhcp option82 configuration** command displays the DHCP Option 82 configuration.




Format
------

**display dhcp option82 configuration** [ **vlan** *vlan-id* | **interface** { *interface-type* *interface-number* | *interface-name* } ]

**display dhcp option82 configuration** { **bridge-domain** *bd-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays the DHCP Option 82 configuration in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **interface** *interface-type* *interface-number* | Displays the DHCP Option 82 configuration on a specified interface. | - |
| *interface-name* | interface-name specifies the name of an interface. | The value is a string of 1 to 128 case-sensitive characters, spaces not supported. |
| **bridge-domain** *bd-id* | Specifies the VLAN ID. | The value is an integer that ranges from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The Option 82 field records the location of a DHCP client. A device inserts the Option 82 field to a DHCP Request message to notify the DHCP server of the DHCP client location. The DHCP server can properly assign an IP address and other configurations to the DHCP client, ensuring DHCP client security.After the Option 82 field is inserted to a DHCP message, run the **display dhcp option82 configuration** command to display the DHCP Option 82 configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all the DHCP Option82 configurations.
```
<HUAWEI> display dhcp option82 configuration
#
dhcp option82 vendor-specific format vendor-sub-option 1 ascii 22
#
interface 100GE1/0/1
 dhcp option82 subscriber-id format ascii 222
 dhcp option82 insert enable
 dhcp option82 encapsulation circuit-id
 dhcp option82 append vendor-specific
 dhcp option82 circuit-id format common
#

```

**Table 1** Description of the **display dhcp option82 configuration** command output
| Item | Description |
| --- | --- |
| dhcp option82 vendor-specific format vendor-sub-option ascii | The Sub9 of the old format is inserted into the Option 82 field of DHCP messages.  To specify the parameter, run the dhcp option82 vendor-specific format command. |
| dhcp option82 subscriber-id format ascii | The Sub6 suboption is inserted into the Option 82 field of DHCP messages.  To specify the parameter, run the dhcp option82 subscriber-id format command. |
| dhcp option82 insert enable | The function of inserting Option 82 to DHCP messages is enabled and the insertion method is configured:   * dhcp option82 rebuild enable: Rebuild mode. * dhcp option82 insert enable: Insert mode.   To specify the parameter, run the dhcp option82 enable command. |
| dhcp option82 encapsulation circuit-id | The suboption inserted into the Option 82 field of DHCP messages is configured.  To specify the parameter, run the dhcp option82 encapsulation command. |
| dhcp option82 append vendor-specific | The Sub9 of the new format is inserted into the Option 82 field of DHCP messages.  To specify the parameter, run the dhcp option82 append vendor-specific command. |
| dhcp option82 circuit-id format common | Format of the circuit-id suboption.  To specify the parameter, run the dhcp option82 format command. |
| interface | Option 82 configuration on interface. |