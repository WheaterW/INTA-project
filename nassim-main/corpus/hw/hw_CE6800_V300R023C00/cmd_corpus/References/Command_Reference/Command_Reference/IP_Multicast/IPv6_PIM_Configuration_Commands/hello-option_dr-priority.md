hello-option dr-priority
========================

hello-option dr-priority

Function
--------



The **hello-option dr-priority** command sets a designated router (DR) election priority for an IPv6 Router.

The **undo hello-option dr-priority** command restores the default priority.



By default, the DR election priority of an IPv6 Router is 1.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**hello-option dr-priority** *priority*

**undo hello-option dr-priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies a DR election priority. A larger value indicates a higher priority. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On an IPv6 PIM-SM shared network segment, a DR is dynamically elected among candidate Routers. The DR registers local multicast sources and processes join requests from receivers.DR election is based on DR election priorities and IPv6 addresses of Routers. In a DR election process, Routers exchange Hello messages carrying DR priorities. If the Routers have the same priority, the Router with the highest IPv6 address wins the election.If one or more Routers do not support Hello packets that contain a DR election priority, DR election is based on IPv6 addresses of the Router. The Router with the highest IPv6 address wins the election.To change the DR election priority of a Router, run the hello-option dr-priority command.When the source's DR receives multicast data, it sends Register messages to the RP, and add registered egress interface. If too many redundant Register messages are sent to RP, the performance is affected. Run the register-with-probe command to disable Register messages sending function on the source's DR, the DR sends Probe messages instead of Register messages, so that the performance is not affected.


Example
-------

# In the public network instance, set the DR election priority of the Router to 3.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] hello-option dr-priority 3

```