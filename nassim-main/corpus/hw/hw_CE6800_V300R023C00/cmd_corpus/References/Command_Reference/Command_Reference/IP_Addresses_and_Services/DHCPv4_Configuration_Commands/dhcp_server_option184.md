dhcp server option184
=====================

dhcp server option184

Function
--------

The **dhcp server option184** command configures Option 184 allocated by a DHCP server to a client.

The **undo dhcp server option184** command deletes Option 184 allocated by a DHCP server to a client.

By default, Option 184 allocated by a DHCP server to a client is not configured.



Format
------

**dhcp server option184** { **as-ip** *ip-address* | **fail-over** *ip-address* *dialer-string* | **ncp-ip** *ip-address* | **voice-vlan** *vlan-id* }

**undo dhcp server option184** [ **as-ip** | **fail-over** | **ncp-ip** | **voice-vlan** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **as-ip** *ip-address* | Specifies the IP address of the backup NCP. | The value is in dotted decimal notation. |
| **fail-over** *ip-address* | Specifies the IP address in the failover route. | The value is in dotted decimal notation. |
| *dialer-string* | Specifies the dialer string. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces. If spaces are used, the string must start and end with double quotation marks ("). |
| **ncp-ip** *ip-address* | Specifies the IP address of the network call processor (NCP). | The value is in dotted decimal notation. |
| **voice-vlan** *vlan-id* | Specifies the ID of a voice VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The dhcp server option184 command applies to only the DHCP server and configures Option 184 allocated by a DHCP server to a client in an interface address pool.

**Prerequisites**

1. The address of an interface address pool has been configured using the **ip address** command.
2. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.


Example
-------

# Configure Option 184 allocated by a DHCP server to a client in the interface address pool on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.2 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server option184 as-ip 10.10.10.10

```