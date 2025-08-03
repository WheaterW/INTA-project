tunnel pipe dscp
================

tunnel pipe dscp

Function
--------



The **tunnel pipe dscp** command sets the DiffServ mode to pipe on a tunnel interface and sets the DSCP priority in pipe mode.

The **undo tunnel pipe dscp** command restores the DiffServ mode on a tunnel interface to uniform.



By default, the DiffServ mode on a tunnel interface is uniform.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tunnel pipe dscp** *dscpvalue*

**undo tunnel pipe dscp** [ *dscpvalue* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dscpvalue* | Specifies an IP DSCP priority. | The value is an integer that ranges from 0 to 63 . |



Views
-----

Tunnel interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The DiffServ mode enables the device to mark different priorities for different services, so that the services can be scheduled in a tunnel based on their priorities.

* Uniform mode: The network transmits voice, video, and data services. When different service flows of enterprise users enter a tunnel, devices on the campus network must assign priorities in descending order to the voice, video, and data services to provide differentiated services.
* Pipe mode: You can set the DiffServ mode to the pipe mode when you want all packets that enter the tunnel to use the same IP DSCP priority.

**Precautions**

If both the qos phb marking dscp enable and **tunnel pipe dscp** commands are configured, the device processes packets entering the tunnel as follows:1.Sets the priority of the packets to the IP DSCP value (dscp-value1) configured by the **tunnel pipe dscp** command.2.Maps this priority to the DSCP value (dscp-value2) configured by the **ip-dscp-outbound** command used in the DiffServ domain applied to the tunnel outbound interface. That is, the DSCP priority of GRE-encapsulated packets is dscp-value2.


Example
-------

# Set the DiffServ mode to pipe on tunnel interface 1 and set the DSCP priority to 32.
```
<HUAWEI> system-view
[~HUAWEI] interface tunnel 1
[*HUAWEI-Tunnel1] tunnel pipe dscp 32

```

# Restores the DiffServ mode is uniform for the Tunnel.
```
<HUAWEI> system-view
[~HUAWEI] interface tunnel 1
[*HUAWEI-Tunnel1] undo tunnel pipe dscp 32

```