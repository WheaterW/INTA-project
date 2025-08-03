peer listen-as-segment (BGP-VPN instance IPv4 address family view)
==================================================================

peer listen-as-segment (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer listen-as-segment** command specifies a peer AS range from which a dynamic EBGP peer group listens for BGP connection requests.

The **undo peer listen-as-segment** command deletes the specified peer AS range from which a dynamic EBGP peer group listens for BGP connection requests.



By default, no peer AS range from which a dynamic EBGP peer group listens for BGP connection requests is specified.


Format
------

**peer** *group-name* **listen-as-segment** **begin-as** *begin-asn* **end-as** *end-asn*

**undo peer** *group-name* **listen-as-segment** **begin-as** *begin-asn* **end-as** *end-asn*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |
| **begin-as** *begin-asn* | Specifies the start AS number in an AS range. | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |
| **end-as** *end-asn* | Specifies the end AS number in an AS range. | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To specify a peer AS range from which a dynamic EBGP peer group listens for BGP connection requests, run the peer listen-as-segment command. The dynamic BGP peer function enables BGP to listen for BGP connection requests from a specified network segment, dynamically establish BGP peer relationships, and add these peers to the same dynamic peer group. This spares you from adding or deleting BGP peer configurations in response to each change in BGP peers.



**Precautions**



If the **undo peer listen-as-segment** command is run, all connections established between the local device and the dynamic peers in the specified AS-Segment are also deleted. Therefore, exercise caution when running this command.When you run the **undo peer listen-as-segment** command, ensure that the start and end AS numbers in the AS range to be deleted are the same as those in the configured AS range.




Example
-------

# Configure the dynamic EBGP peer group named ex to listen for BGP connection requests from the peer AS range 200 to 300.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] group ex listen external
[*HUAWEI-bgp-vpn1] peer ex listen-as-segment begin-as 200 end-as 300

```