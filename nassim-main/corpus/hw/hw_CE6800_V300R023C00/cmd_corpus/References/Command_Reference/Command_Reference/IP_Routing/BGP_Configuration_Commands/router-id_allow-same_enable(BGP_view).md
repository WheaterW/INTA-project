router-id allow-same enable(BGP view)
=====================================

router-id allow-same enable(BGP view)

Function
--------



The **router-id allow-same enable** command allows EBGP connections to be established between peers with the same router ID.

The **undo router-id allow-same enable** command restores the default configuration.



By default, EBGP connections cannot be established between peers with the same router ID.


Format
------

**router-id allow-same enable**

**undo router-id allow-same enable**


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

According to the previous protocol, the router ID must be a valid IPv4 host address. The prerequisite for establishing a BGP peer relationship through negotiation is that the router IDs of the two ends are different. In actual scenarios, however, different carriers may set the same router ID. In this case, the peer relationship cannot be established. To solve this problem, the router IDs of EBGP peers can be different, but the router IDs of IBGP peers must be different. That is, IBGP peer relationships cannot be established between devices with the same router ID, but EBGP peer relationships can be established between devices with the same router ID.To allow EBGP peer relationships to be established between peers with the same router ID in a single BGP instance, run the **router-id allow-same enable** command.

**Precautions**

After the **undo router-id allow-same enable** command is run to cancel the configuration, the EBGP connection established between the peers with the same router ID is not torn down immediately. You can run the **reset bgp** command to tear down the connection. After the **reset bgp** command is run, the TCP connection established by BGP is reset and the peer relationship is re-established. As a result, the peer relationship is torn down in a short period of time. Therefore, exercise caution when running this command.


Example
-------

# Allow EBGP connections to be set up between peers with the same router ID.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] router-id allow-same enable

```