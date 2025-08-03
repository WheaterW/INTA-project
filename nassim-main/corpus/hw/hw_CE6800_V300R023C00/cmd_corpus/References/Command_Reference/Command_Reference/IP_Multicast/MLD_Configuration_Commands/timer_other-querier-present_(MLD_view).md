timer other-querier-present (MLD view)
======================================

timer other-querier-present (MLD view)

Function
--------



The **timer other-querier-present** command sets a global Keepalive period of other Multicast Listener Discovery (MLD) queriers.

The **undo timer other-querier-present** command restores the default value.



By default, if the robustness variable, the interval for sending MLD general query messages, and the maximum response time of MLD Query messages all use default values, the Keepalive period of other MLD queriers is 255 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**timer other-querier-present** *interval*

**undo timer other-querier-present**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the Keepalive period of other MLD queriers. The formula used to calculate the Keepalive period of other MLD queriers is: Keepalive period of other MLD queriers = Robustness variable x Interval for sending MLD general query messages + 1/2 x maximum response time of MLD Query messages. | The value is an integer that ranges from 60 to 300. |



Views
-----

MLD view,VPN instance MLD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The function of this command is the same as that of the **mld timer other-querier-present** command used in the interface view. The system prefers the configuration in the interface view. The configuration in the MLD view is used only when the configuration in the interface view is not done.


Example
-------

# Set the Keepalive period of other MLD queriers to 200 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] mld
[*HUAWEI-mld] timer other-querier-present 200

```