reset bgp evpn
==============

reset bgp evpn

Function
--------



The **reset bgp evpn** command resets a specified or all BGP EVPN connections.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset bgp** [ **instance** *instance-name* ] **evpn** { **all** | *as-number* | *ipv4-address* | **group** *group-name* }

**reset bgp evpn** [ *ipv4-address* ] **slow-peer**

**reset bgp instance** *instance-name* **evpn** [ *ipv4-address* ] **slow-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies a BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **all** | Resets all BGP EVPN connections. | - |
| *as-number* | Specifies a 2-byte AS number (number<1-65535>) or a 4-byte AS number (number<1-65535>.number<0-65535>). | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |
| *ipv4-address* | Resets connections with a specified BGP EVPN peer. | The value is in dotted decimal notation. |
| **group** *group-name* | Resets BGP connections with the specified peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **slow-peer** | Restores a slow peer connection to a normal peer connection. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you want to have the new configuration take effect immediately after the BGP EVPN configuration changes, run the **reset bgp evpn** command.To reset all BGP EVPN connections, run the **reset bgp evpn all** command.

**Configuration Impact**

This command resets all TCP connections established between BGP EVPN peers and therefore results in the re-establishment of BGP EVPN peer relationships. Exercise caution when running this command.


Example
-------

# Reset all BGP EVPN connections.
```
<HUAWEI> reset bgp evpn all

```