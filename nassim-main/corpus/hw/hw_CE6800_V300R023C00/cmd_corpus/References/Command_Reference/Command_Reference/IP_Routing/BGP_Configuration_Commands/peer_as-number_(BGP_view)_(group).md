peer as-number (BGP view) (group)
=================================

peer as-number (BGP view) (group)

Function
--------



The **peer as-number** command configures an AS number for a specified peer group.

The **undo peer as-number** command deletes the AS number of a specified peer group.



By default, no BGP peer is configured, and no AS number is specified for a peer group.


Format
------

**peer** *group-name* **as-number** *as-number*

**undo peer** *group-name* **as-number**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *as-number* | Specifies a destination AS number. | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |



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

A peer group has been created using the **group** *group-name*{ **external** | **internal** } command.

* If the **group** *group-name***external** command is run, the AS number of the EBGP peer group specified in the **peer as-number** command must be different from the local AS number.
* If the **group** *group-name***internal** command is run, the AS number of the IBGP peer group is the same as the local AS number by default. Therefore, you do not need to run this command.

If the peer group to which a peer belongs is not configured with an AS number or the peer is not added to any peer group, deleting the AS number of the peer resets the peer relationship.Running the **undo peer** *ipv4-address*or **undo peer** *ipv6-address*command deletes configurations related to the peer in all address families. Therefore, exercise caution when running this command.When the local device sends routes to IBGP peers, the AS\_Path attribute does not carry the local AS number. When the local device sends routes to EBGP peers, the AS\_Path attribute carries the local AS number.The recommended hold time is related to the total number of peers in each BGP address family. As the number of peers increases, the recommended minimum hold time increases accordingly. For details, see "Mapping Between the Total Number of Peers in Each BGP Address Family and the Recommended Minimum Hold Time" in the usage guide of the **peer timer** command. Adjust the hold time.


Example
-------

# Set the AS number to 200 for a peer group named test.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200

```