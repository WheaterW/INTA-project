reset auto-defend attack-source
===============================

reset auto-defend attack-source

Function
--------



The **reset auto-defend attack-source trace-type** command clears the counter of packets traced after attack source tracing based on source MAC addresses, source IP addresses, or source ports+VLANs is configured.

The **reset auto-defend attack-source** command clears information about attack sources.




Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**reset auto-defend attack-source trace-type** { **source-mac** [ *mac-address* ] | **source-ip** [ *ip-address* | *ipv6-address* ] | **source-portvlan** [ **interface** { *interface-name* | *interface-type* *interface-number* } **vlan** *vlan-id* [ **inner-vlan** *inner-vlan-id* ] ] } [ **slot** *slot-id* ]

For CE6885-LL (low latency mode):

**reset auto-defend attack-source trace-type** { **source-mac** [ *mac-address* ] | **source-ip** [ *ip-address* ] | **source-portvlan** [ **interface** { *interface-name* | *interface-type* *interface-number* } **vlan** *vlan-id* ] } [ **slot** *slot-id* ]

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**reset auto-defend attack-source history** [ **slot** *slot-id* ]

**reset auto-defend attack-source** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-mac** *mac-address* | Clears the counter of packets traced after attack source tracing based on source MAC addresses is configured.  If mac-address is specified, the counter of traced packets sent from the specified MAC address is cleared. | The value is in the H-H-H format. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **source-ip** *ip-address* | Clears the counter of packets traced after attack source tracing based on source IP addresses is configured.  If ip-address is specified, the counter of traced packets sent from the specified IP address is cleared. | The value is in dotted decimal notation. |
| **source-ip** *ipv6-address* | Clears the counter of packets traced after attack source tracing based on source IP addresses is configured.  If ipv6-address is specified, the counter of traced packets sent from the specified IPv6 address is cleared.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **source-portvlan** | Clears the counter of packets traced after attack source tracing based on source ports+VLANs is configured.  If a port or VLAN is specified, the counter of traced packets sent from the specified port or VLAN is cleared. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | The value must be set according to the device configuration. |
| **interface** *interface-name* | Specifies an interface name. | - |
| **vlan** *vlan-id* | Specifies the ID of a VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **slot** *slot-id* | Specifies a slot ID.  If slot slot-id is not specified, information about attack sources on the device is cleared. | The value must be set according to the device configuration. |
| **history** | Deletes history attack source information.  If history is not specified, all existing attack source information is deleted. | - |
| **trace-type** | Specifies trace type. | - |
| **inner-vlan** *inner-vlan-id* | Specifies the inner VLAN ID in a QinQ packet.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 4094. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view information about attack sources in a specified period, run the **reset auto-defend attack-source** command to clear existing information about attack sources and run the **display auto-defend attack-source** command. However, the reset auto-defend attack-source clears information about all attack sources. You can run the reset auto-defend attack-source trace-type command to clear information about specified attack sources. To delete history attack source information, run the **reset auto-defend attack-source history** command.

**Precautions**

After the **reset auto-defend attack-source** command is run, information about attack sources is cleared and cannot be restored.


Example
-------

# Delete attack source history information on the device.
```
<HUAWEI> reset auto-defend attack-source history

```

# Delete existing attack source information on the device.
```
<HUAWEI> reset auto-defend attack-source

```

# Clear the counter of traced packets sent from IP address 10.1.1.1.
```
<HUAWEI> reset auto-defend attack-source trace-type source-ip 10.1.1.1

```