confederation id
================

confederation id

Function
--------



The **confederation id** command configures a BGP confederation and specifies a confederation ID.

The **undo confederation id** command deletes the configured BGP confederation.



By default, no BGP confederation is configured.


Format
------

**confederation id** *as-number*

**undo confederation id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
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

A large AS may contain a huge number of fully meshed IBGP peer relationships. To reduce the number of fully meshed IBGP peer relationships in the AS and keep the integrity of the original AS, perform the following operations:Divide the AS into multiple sub-ASs and run the confederation id command to configure a BGP confederation. Then establish EBGP connections between sub-ASs and establish fully meshed IBGP connections within the same sub-AS.Some key attributes of routes, such as the next hop, MED, and Local\_Pref are not discarded when these routes pass through sub-ASs.

**Precautions**

The confederation ID is equal to the AS number. During the establishment of a peer relationship with a peer in an external AS, specify the confederation ID. All the sub-ASs in the same confederation must be configured with the same confederation ID, and the confederation ID must be different from the number of any sub-AS.


Example
-------

# Configure a confederation ID. An AS is divided into sub-ASs 38, 39, 40, and 41, and their confederation ID is 9. Peer 10.2.3.4 is a member of the AS confederation. Peer 10.11.11.1 is a member outside the AS confederation. For external members, confederation 9 is a unified AS.
```
<HUAWEI> system-view
[~HUAWEI] bgp 41
[*HUAWEI-bgp] confederation id 9
[*HUAWEI-bgp] confederation peer-as 38 39 40
[*HUAWEI-bgp] peer 10.2.3.4 as-number 38
[*HUAWEI-bgp] peer 10.11.11.1 as-number 98

```