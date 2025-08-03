openflow agent
==============

openflow agent

Function
--------



The **openflow agent** command creates and displays an OpenFlow Agent view or displays the view of an existing OpenFlow Agent.

The **undo openflow agent** command deletes an OpenFlow Agent view.



By default, no OpenFlow Agent view is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**openflow agent**

**undo openflow agent**


Parameters
----------

None

Views
-----

Controller channel view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Before changing the OpenFlow heartbeat interval, configuring the IP address used to set up OpenFlow connection with the specified controller, or configuring OpenFlow authentication, run the **openflow agent** command to create an OpenFlow Agent view first.


Example
-------

# Create and display an OpenFlow Agent view.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent
[*HUAWEI-sdn-agent] controller-ip 10.1.1.1
[*HUAWEI-sdn-agent-ctrl-10.1.1.1] openflow agent
[*HUAWEI-sdn-agent-ctrl-10.1.1.1-openflow]

```