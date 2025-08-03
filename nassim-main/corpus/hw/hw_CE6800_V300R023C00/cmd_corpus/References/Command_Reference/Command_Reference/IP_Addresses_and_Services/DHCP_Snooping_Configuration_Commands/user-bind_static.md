user-bind static
================

user-bind static

Function
--------



The **user-bind static** command configures a static binding table.

The **undo user-bind static** command deletes a static binding table.



By default, no static binding table exists.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**user-bind static** { **ip-address** { *start-ip* [ **to** *end-ip* ] } &<1-10> | **mac-address** *mac-address* } \* [ **interface** { *interface-type* *interface-number* | *interface-name* } ] [ **vlan** *vlan-id* [ **ce-vlan** *ce-vlan-id* ] ]

**undo user-bind static** [ **ip-address** { *start-ip* [ **to** *end-ip* ] } &<1-10> | **mac-address** *mac-address* | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* [ **ce-vlan** *ce-vlan-id* ] ] \*

For CE6885-LL (low latency mode):

**user-bind static** { **ip-address** { *start-ip* [ **to** *end-ip* ] } &<1-10> | **mac-address** *mac-address* } \* [ **interface** { *interface-type* *interface-number* | *interface-name* } ] [ **vlan** *vlan-id* ]

**undo user-bind static** [ **ip-address** { *start-ip* [ **to** *end-ip* ] } &<1-10> | **mac-address** *mac-address* | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *start-ip* | Specifies the IP address of a user in a static binding entry. start-ip specifies the first IP address. | The value is in dotted decimal notation. |
| **to** *end-ip* | Specifies the last IP address. | The value is in dotted decimal notation. The value of end-ip must be greater than that of start-ip. start-ip and end-ip specify a range of IP addresses. |
| **mac-address** *mac-address* | Specifies the user MAC address in a static binding entry. | The value is in hexadecimal notation. The value is in the format of H-H-H. |
| **interface** *interface-type* *interface-number* | Specifies the interface connected to a user in a static binding entry.  â¢interface-type specifies the interface type.  â¢interface-number specifies the interface number. | - |
| *interface-name* | interface-name specifies the name of an interface. | The value is a string of 1 to 128 case-sensitive characters. It cannot contain spaces. |
| **vlan** *vlan-id* | Specifies the user VLAN ID in a static binding entry. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **ce-vlan** *ce-vlan-id* | Specifies the inner VLAN tag of a QinQ packet in a static binding entry.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 4094. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When DHCP snooping is enabled, the device generates dynamic DHCP snooping binding entries for dynamic users, but cannot generate dynamic DHCP snooping binding entries for static users. Therefore, if no static user binding table is available, the device discards all the packets forwarded by static users. To enable the device to forward packets of static users, run the command to configure a static binding table.

**Precautions**

After a static binding table is configured, the checks packets based on the configured static binding entries and discards the packets that do not match the entries.


Example
-------

# Configure a static binding entry for a user in VLAN 2 with the IP address 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] user-bind static ip-address 10.1.1.1 vlan 2

```