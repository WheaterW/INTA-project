peer listen-as (BGP-VPN instance view)
======================================

peer listen-as (BGP-VPN instance view)

Function
--------



The **peer listen-as** command specifies a peer AS from which a dynamic EBGP peer group listens for BGP connection requests.

The **undo peer listen-as** command deletes the specified peer AS from which a dynamic EBGP peer group listens for BGP connection requests.



By default, no peer AS from which a dynamic EBGP peer group listens for BGP connection requests is specified.


Format
------

**peer** *group-name* **listen-as** { *asn* } &<1-6>

**undo peer** *group-name* **listen-as** { *asn* } &<1-6>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a dynamic BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *asn* | Specifies the AS number. | A 2-byte AS number is an integer ranging from 1 to 65535.  A 4-byte AS number can be: An integer ranging from 65536 to 4294967295. In the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The dynamic BGP peer function enables BGP to listen for BGP connection requests from a specified network segment, dynamically establish BGP peer relationships, and add these peers to the same dynamic peer group. This spares you from adding or deleting BGP peer configurations in response to each change in dynamic peers. To specify a peer AS from which a dynamic EBGP peer group listens for BGP connection requests, run the peer listen-as command.

**Prerequisites**

A dynamic EBGP peer group has been created using the **group listen external** command.

**Precautions**

If the **undo peer listen-as** command is run, all connections established between the local device and the dynamic peers in the specified AS are also deleted. Therefore, exercise caution when running this command.If the peer listen-as command is run more than once, all configurations take effect, indicating that a dynamic EBGP peer group can listen for BGP connection requests from more than one peer AS.


Example
-------

# Configure the dynamic EBGP peer group named ex to listen for BGP connection requests from peer AS 200.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group ex listen external
[*HUAWEI-bgp-instance-vpn1] peer ex listen-as 200

```