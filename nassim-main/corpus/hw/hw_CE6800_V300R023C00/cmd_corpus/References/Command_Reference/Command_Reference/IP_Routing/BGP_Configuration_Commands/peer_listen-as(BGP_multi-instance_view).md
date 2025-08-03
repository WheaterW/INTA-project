peer listen-as(BGP multi-instance view)
=======================================

peer listen-as(BGP multi-instance view)

Function
--------



The **peer listen-as** command specifies a peer AS from which a dynamic EBGP peer group listens for BGP connection requests.

The **undo peer listen-as** command deletes the specified peer AS from which a dynamic EBGP peer group listens for BGP connection requests.



By default, no peer AS from which a dynamic EBGP peer group listens for BGP connection requests is specified.


Format
------

**peer** *peerGroupName* **listen-as** { *asn* } &<1-6>

**undo peer** *peerGroupName* **listen-as** { *asn* } &<1-6>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a dynamic BGP peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *asn* | Specifies the AS number. | A 2-byte AS number is an integer ranging from 1 to 65535.  A 4-byte AS number can be: An integer ranging from 65536 to 4294967295. In the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively |



Views
-----

BGP multi-instance view


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
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] group ex listen external
[*HUAWEI-bgp-instance-a] peer ex listen-as 200

```