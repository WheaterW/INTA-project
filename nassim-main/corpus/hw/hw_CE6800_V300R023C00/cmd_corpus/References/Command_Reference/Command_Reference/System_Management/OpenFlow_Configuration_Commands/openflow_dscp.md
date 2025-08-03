openflow dscp
=============

openflow dscp

Function
--------



The **openflow dscp** command sets a DSCP priority for OpenFlow packets.

The **undo openflow dscp** command restores the default setting.



The default DSCP priority of OpenFlow packets is the DSCP priority set by the set priority dscp command.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**openflow dscp** *dscp-value*

**undo openflow dscp** [ *dscp-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dscp-value* | Specifies the DSCP priority. | The value is an integer that ranges from 0 to 63 . |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to set the DSCP priority of OpenFlow packets. The DSCP priority of OpenFlow packets sent by the device is then changed to the configured value so that downstream devices can perform QoS scheduling based on the DSCP priority.


Example
-------

# Set the DSCP priority of OpenFlow packets to 63.
```
<HUAWEI> system-view
[~HUAWEI] openflow dscp 63

```