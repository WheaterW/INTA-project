echo-interval
=============

echo-interval

Function
--------



The **echo-interval** command sets the heartbeat interval of the OpenFlow connection.

The **undo echo-interval** command restores the default heartbeat interval of the OpenFlow connection.



By default, the heartbeat interval of the OpenFlow connection is 5 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**echo-interval** *interval*

**undo echo-interval** [ *interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the heartbeat interval of the OpenFlow connection. | The value is an integer that ranges from 5 to 60. The default value is 5. |



Views
-----

OpenFlow-forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The controller and switch establishing the OpenFlow connection periodically exchange heartbeat packets to detect whether the peer end is still available. You can set the heartbeat interval for the OpenFlow connection, that is, specify the frequency at which the heartbeat packets are sent between the controller and switch.


Example
-------

# Set the heartbeat interval of the OpenFlow connection to 35 seconds.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent
[*HUAWEI-sdn-agent] controller-ip 10.1.1.1
[*HUAWEI-sdn-agent-ctrl-10.1.1.1] openflow agent
[*HUAWEI-sdn-agent-ctrl-10.1.1.1-openflow] echo-interval 35

```