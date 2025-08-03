reset bgp mvpn
==============

reset bgp mvpn

Function
--------



The **reset bgp mvpn** command resets BGP connections related to BGP MVPN.




Format
------

**reset bgp mvpn** { **all** | *as-number* | *ipv4-address* | **external** | **internal** | **group** *group-name* }

**reset bgp mvpn** [ *ipv4-address* ] **slow-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Reset all BGP connections. | - |
| *as-number* | Specifies a 2-byte AS number (number<1-65535>) or a 4-byte AS number (number<1-65535>.number<0-65535>). | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |
| *ipv4-address* | Resets the BGP connection with a specified peer. | The value is in dotted decimal notation. |
| **external** | Reset all EBGP connections. | - |
| **internal** | Resets all IBGP connections. | - |
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

The **reset bgp** command is used to make new BGP configurations take effect.If a BGP routing policy is configured on the device that does not support Route-Refresh, the **reset bgp** command can be used to make the new routing policy to take effect.


Example
-------

# Reset all BGP MVPN connections in GR mode.
```
<HUAWEI> reset bgp mvpn all

```