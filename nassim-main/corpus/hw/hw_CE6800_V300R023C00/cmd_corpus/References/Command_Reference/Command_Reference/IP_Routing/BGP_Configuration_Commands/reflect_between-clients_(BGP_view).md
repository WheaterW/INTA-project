reflect between-clients (BGP view)
==================================

reflect between-clients (BGP view)

Function
--------



The **reflect between-clients** command enables route reflection among clients.

The **undo reflect between-clients** command disables route reflection among clients. If the clients of an RR are fully meshed, you can disable route reflection between the clients to reduce the cost.



By default, route reflection among clients through the RR is enabled.


Format
------

**reflect between-clients**

**undo reflect between-clients**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On some networks, if the clients of an RR establish full-mesh connections with each other, they can directly exchange routing information. Route reflection among clients through the RR is unnecessary. The **undo reflect between-clients** command can be used to prohibit the clients from reflecting routes to each other to reduce costs.

**Prerequisites**

An RR has been configured.

**Configuration Impact**

After the **undo reflect between-clients** command is run, the clients of an RR are prohibited from reflecting routes.

**Precautions**

The **reflect between-clients** command is run only on RRs.


Example
-------

# Enable route reflection between clients.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] reflect between-clients

```