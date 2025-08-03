display msdp sa-cache
=====================

display msdp sa-cache

Function
--------



The **display msdp sa-cache** command displays information about (S, G) entries in the source active (SA) cache.




Format
------

**display msdp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **sa-cache** [ *group-address* | *source-address* | { *as-number* | *as-number\_string* } ] \*

**display msdp sa-cache** [ *group-address* | *source-address* | { *as-number* | *as-number\_string* } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays information about cached (S, G) entries in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |
| **all-instance** | Displays information about cached (S, G) entries in all instances. | - |
| *group-address* | Displays information about cached (S, G) entries of a specified group address.  group-address specifies a group address. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| *source-address* | Displays information about cached (S, G) entries of a specified source address.  source-address specifies a source address. | The address is in dotted decimal notation. |
| *as-number* | Displays information about cached (S, G) entries that contain an integral autonomous system (AS) number. | The value is an integer ranging from 1 to 4294967295. |
| *as-number\_string* | Displays information about cached (S, G) entries that contain a dotted notation AS number.  as-number\_string specifies a dotted notation AS number. | The value is in the format of x.y, where x and y are integers that range from 1 to 65535 and from 0 to 65535, respectively. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After the SA cache function is enabled, you can run the **display msdp sa-cache** command to display cached (S, G) entries learned from other Multicast Source Discovery Protocol (MSDP) peers, including the source address, group address, address of the source's rendezvous point (RP), routing protocol, AS number, and timeout period of entries.

**Prerequisites**

The SA cache function has been enabled. By default, the SA cache function is enabled.

**Precautions**

If neither vpn-instance vpn-instance-name nor all-instance is specified, the command displays cached (S, G) entries in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display cached (S, G) entries in the public network instance.
```
<HUAWEI> display msdp sa-cache
 MSDP Source-Active Cache Information of VPN-Instance: public net
 MSDP Total Source-Active Cache - 2 entries
 MSDP matched 2 entries
(10.0.5.120, 225.0.0.1)
 Origin RP: 3.3.3.3
 Pro: ?, AS: ?
 Uptime: 00:01:01, Expires: 00:05:59
(10.0.5.120, 225.0.0.2)
 Origin RP: 3.3.3.3
 Pro: ?, AS: ?
 Uptime: 00:00:01, Expires: 00:05:59

```

**Table 1** Description of the **display msdp sa-cache** command output
| Item | Description |
| --- | --- |
| MSDP Source-Active Cache Information of VPN-Instance | Instance in which cached (S, G) entries are displayed. |
| MSDP Total Source-Active Cache - 2 entries | Number of cached (S, G) entries. |
| MSDP matched 2 entries | Number of (S, G) entries that meet the filter condition. |
| (10.0.5.120, 225.0.0.1) | Multicast source and group addresses. |
| Origin RP | Source's RP address that advertises the (S, G) entry. |
| Pro | Type of the protocol from which the AS number of the source RP is obtained. When the protocol type cannot be obtained, use "?" to indicate the protocol type. |
| AS | AS number of the source RP. If the AS number of the source RP cannot be obtained in the same AS or across ASs, a question mark (?) is used to indicate the AS number. |
| Uptime | Time when the (S, G) entry was cached. |
| Expires | Time when the cached (S, G) entry will time out. |