peer as-number (BGP view)
=========================

peer as-number (BGP view)

Function
--------



The **peer as-number** command creates a peer and configures an AS number for the peer.

The **undo peer** command deletes a specified peer.



By default, no BGP peer is configured, and no AS number is specified for a peer or peer group.


Format
------

**peer** *ipv4-address* **as-number** *as-number*

**undo peer** *ipv4-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *as-number* | Specifies a destination AS number. | For an AS number in integer format, the value ranges from 1 to 4294967295.  For an AS number in dotted notation, it is in the format of x.y, in which x and y are integers, with x ranging from 1 to 65535 and y ranging from 0 to 65535. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **peer as-number** command to create a specified peer relationship and specify the AS number of the peer.

**Precautions**

If the peer group to which a peer belongs is not configured with an AS number or the peer is not added to any peer group, deleting the AS number of the peer resets the peer relationship.Running the **undo peer** *ipv4-address*or **undo peer** *ipv6-address*command deletes configurations related to the peer in all address families. Therefore, exercise caution when running this command.When the local device sends routes to IBGP peers, the AS\_Path attribute does not carry the local AS number. When the local device sends routes to EBGP peers, the AS\_Path attribute carries the local AS number.The recommended hold time is related to the total number of peers in each BGP address family. As the number of peers increases, the recommended minimum hold time increases accordingly. For details, see "Mapping Between the Total Number of Peers in Each BGP Address Family and the Recommended Minimum Hold Time" in the usage guide of the **peer timer** command. Adjust the hold time.


Example
-------

# Set the AS number to 100 for IPv4 peer 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100

```