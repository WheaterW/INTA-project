display msdp sa-count
=====================

display msdp sa-count

Function
--------



The **display msdp sa-count** command displays statistics about (S, G) entries in the source active (SA) cache.




Format
------

**display msdp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **sa-count** [ *as-number* | *as-number\_string* ]

**display msdp sa-count** [ *as-number* | *as-number\_string* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays statistics about cached (S, G) entries in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, which do not contain spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **all-instance** | Displays statistics about cached (S, G) entries in all instances. | - |
| *as-number* | Displays information about cached (S, G) entries that contain an integral autonomous system (AS) number. | The value is an integer that ranges from 1 to 4294967295. |
| *as-number\_string* | Displays information about cached (S, G) entries that contain a dotted notation AS number.  as-number\_string specifies a dotted notation AS number. | The value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After the SA cache function is enabled, you can run the **display msdp sa-count** command to display statistics about the (S, G) entries in the SA cache.

**Prerequisites**

The SA cache function has been enabled. By default, the SA cache function is enabled.

**Precautions**

If neither vpn-instance vpn-instance-name nor all-instance is specified, the command displays cached (S, G) entries in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about cached (S, G) entries in the public network instance
```
<HUAWEI> display msdp sa-count
MSDP Source-Active Count Information of VPN-Instance: public net
Number of cached Source-Active entries, counted by Peer
  Peer's Address     Number of SA
  10.10.10.10        5
Number of source and group, counted by AS
  AS     Number of source    Number of group
  ?      3                      3
  Total 5 Source-Active entry matched

```

**Table 1** Description of the **display msdp sa-count** command output
| Item | Description |
| --- | --- |
| MSDP Source-Active Count Information of VPN-Instance | Instance in which statistics about cached (S, G) entries are displayed. |
| Number of cached Source-Active entries, counted by Peer | Number of cached (S, G) entries of each peer. |
| Number of SA | Number of cached (S, G) entries received from the peer. |
| Number of source and group, counted by AS | Number of cached (S, G) entries of each AS to which the source's RP belongs. |
| Number of source | Number of sources in the AS.  If 0 is displayed in the Number of source and Number of group fields, the local device does not receive SA messages from its MSDP peer. In this case, contact technical support personnel to troubleshoot faults. |
| Number of group | Number of groups in the AS. |
| Peer's Address | Address of the peer that sends the SA message. |
| AS | AS number. |