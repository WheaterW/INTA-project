option184
=========

option184

Function
--------

The **option184** command configures the Option 184 field for the DHCP client.

The **undo option184** command deletes a configuration in the Option 184 field.

By default, no content in the Option 184 field is configured.



Format
------

**option184** { **as-ip** *ip-address* | **fail-over** *ip-address* *dialer-string* | **ncp-ip** *ip-address* | **voice-vlan** *vlan-id* }

**undo option184** [ **as-ip** | **fail-over** | **ncp-ip** | **voice-vlan** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **as-ip** *ip-address* | Specifies the IP address of the backup NCP. | The value is in dotted decimal notation. |
| **fail-over** *ip-address* | Specifies the IP address in the failover route. | The value is in dotted decimal notation. |
| *dialer-string* | Specifies the dialer string. | The value is a string of 1 to 64 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **ncp-ip** *ip-address* | Specifies the IP address of the NCP. | The value is in dotted decimal notation. |
| **voice-vlan** *vlan-id* | Specifies the ID of a voice VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

The option184 command applies to only the DHCP server and configures Option 184 allocated by a DHCP server to a client in a global address pool.



Example
-------

# In the IP address pool view, configure the Option 184 field.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] option184 as-ip 192.168.1.10

```