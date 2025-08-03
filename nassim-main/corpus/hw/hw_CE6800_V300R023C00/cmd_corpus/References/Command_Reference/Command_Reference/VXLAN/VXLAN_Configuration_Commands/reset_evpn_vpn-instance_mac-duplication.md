reset evpn vpn-instance mac-duplication
=======================================

reset evpn vpn-instance mac-duplication

Function
--------



The **reset evpn vpn-instance mac-duplication** command clears the suppression state of MAC routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset evpn vpn-instance** *vpn-instance-name* **mac-duplication** [ **bridge-domain** *bd-id* ] [ **mac-address** *mac-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of an EVPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string.  The name must be the same as the BD ID. |
| **bridge-domain** *bd-id* | Specifies a BD in which the suppression state of MAC routes is to be cleared. | The value is an integer ranging from 1 to 16777215. |
| **mac-address** *mac-address* | Specifies a MAC route whose suppression state is to be cleared. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a MAC route to a specific MAC address or MAC routes in a specific BD have stopped flapping and you want to restore them before the configured hold-off timer expires, run the reset evpn vpn-instance mac-duplication command. This allows you to manually clear the suppression state of the MAC routes.


Example
-------

# Clear the suppression state of MAC routes in an EVPN instance.
```
<HUAWEI> reset evpn vpn-instance 100 mac-duplication

```