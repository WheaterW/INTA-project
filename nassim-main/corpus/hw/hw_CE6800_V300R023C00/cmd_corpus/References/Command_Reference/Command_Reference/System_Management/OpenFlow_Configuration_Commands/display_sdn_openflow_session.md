display sdn openflow session
============================

display sdn openflow session

Function
--------



The **display sdn openflow session** command displays the OpenFlow connection session information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display sdn openflow session**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After an OpenFlow connection is established, you can run this command to view the OpenFlow connection information and determine whether the connection is successfully established.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# View OpenFlow connection information.
```
<HUAWEI> display sdn openflow session

--------------------------------------------------------------------------------
Agent         : 192.168.70.48
Controller    : 192.168.78.118
UpTime        : 0d21h09m32s
State         : Registered
Role          : Master
VPN-instance  : _public_

--------------------------------------------------------------------------------

```

**Table 1** Description of the **display sdn openflow session** command output
| Item | Description |
| --- | --- |
| Agent | Switch's IP address used to set up an OpenFlow connection. |
| Controller | Controller's IP address used to set up an OpenFlow connection. |
| UpTime | Duration when the session is Up. |
| State | OpenFlow connection status:   * Tocreate: The two ends are attempting to establish the OpenFlow connection. * Connected: A TCP connection is successfully established. * Registered: The OpenFlow connection is successfully established. * Init: The OpenFlow connection is in the initialization state. |
| Role | Controller role:   * Equal: has the highest privilege (read and write) on the switch. * Master: has the same privilege as Equal. * Slave: has the read-only privilege. |
| VPN-instance | VPN instance name. |