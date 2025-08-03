display bgp unnumbered peer interface orf ip-prefix
===================================================

display bgp unnumbered peer interface orf ip-prefix

Function
--------



The **display bgp unnumbered peer interface orf ip-prefix** command displays prefix-based outbound route filter (ORF) information received from BGP unnumbered peers.




Format
------

**display bgp unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **orf** **ip-prefix**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



After the prefix-based ORF capability is successfully negotiated, you can run this command to check prefix-based ORF information received from BGP unnumbered peers.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display prefix-based ORF information received from BGP unnumbered peers.
```
<HUAWEI> display bgp unnumbered peer interface 100GE 1/0/1 orf ip-prefix
Total number of ip-prefix received: 1
 Index  Action  Prefix           MaskLen  MinLen  MaxLen
 10     Permit  10.1.1.0         24       32      32

```

**Table 1** Description of the **display bgp unnumbered peer interface orf ip-prefix** command output
| Item | Description |
| --- | --- |
| Index | Sequence number of an IP prefix list. |
| Action | IP prefix filtering action, which can be:   * deny. * permit. |
| Prefix | Address prefix. |
| MaskLen | Mask length of the address prefix. |
| MinLen | Minimum mask length of the address prefix. |
| MaxLen | Maximum mask length. |