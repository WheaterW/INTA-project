rfc1583 compatible different-area-path prefer lower-cost
========================================================

rfc1583 compatible different-area-path prefer lower-cost

Function
--------



The **rfc1583 compatible different-area-path prefer lower-cost** command changes the route selection rule in RFC 1583-compatible mode to be the same as the default route selection rule on the ASBR. That is, if the area IDs of intra and inter routes are different, the route with the smaller cost is preferred; if the area IDs of intra and inter routes are the same, the route with the larger area ID is preferred.

The **undo rfc1583 compatible different-area-path prefer lower-cost** command restores the default route selection rule in RFC 1583 compatible mode.

The **rfc1583 non-compatible backbone-area-path prefer intra** command changes the route selection rule in RFC 1583-incompatible mode to be the same as the default route selection rule on the ASBR. That is, when the area IDs of the intra and inter paths are the same and both areas are backbone areas, the intra-ASBR path is preferred.

The **undo rfc1583 non-compatible backbone-area-path prefer intra** command restores the route selection rule in RFC 1583 incompatible mode to the default rule.



By default, OSPF route selection rules are not configured.


Format
------

**rfc1583 compatible different-area-path prefer lower-cost**

**rfc1583 non-compatible backbone-area-path prefer intra**

**undo rfc1583 compatible different-area-path prefer lower-cost**

**undo rfc1583 non-compatible backbone-area-path prefer intra**


Parameters
----------

None

Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Devices of different vendors or different series of devices of the same vendor are deployed on the same network. For the intra- and inter-route paths to the ASBR, the route selection rules may be different in RFC 1583-compatible and RFC 1583-incompatible scenarios. The different route selection rules may cause loops. To prevent routing loops, you can use a command to change the route selection rule to the default rule on the ASBR.


Example
-------

# Configure the device in RFC 1583 non-compatibility mode to preferentially select intra-area paths.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] undo rfc1583 compatible
[*HUAWEI-ospf-1] rfc1583 non-compatible backbone-area-path prefer intra

```

# Configure the device in RFC 1583 compatibility mode to preferentially select the path with the smallest cost.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] rfc1583 compatible
[*HUAWEI-ospf-1] rfc1583 compatible different-area-path prefer lower-cost

```