send-router-alert disable (MLD view)
====================================

send-router-alert disable (MLD view)

Function
--------



The **send-router-alert disable** command disables the router from sending Multicast Listener Discovery (MLD) messages containing Router-Alert options in IPv6 headers.

The **undo send-router-alert disable** command enables the router to send MLD messages containing Router-Alert options in IPv6 headers.



By default, IPv6 headers of the MLD messages sent by the Router contain Router-Alert options.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**send-router-alert disable**

**undo send-router-alert disable**


Parameters
----------

None

Views
-----

MLD view,VPN instance MLD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The function of this command is the same as that of the mld **send-router-alert disable** command used in the interface view. The system prefers the configuration in the interface view. The configuration in the MLD view is used only when the configuration in the interface view is not done.By default, IP headers of IGMP messages sent by the router contain the Router-Alert option. If the router communicates with a device that does not support the Router-Alert option, run the **send-router-alert disable** command to disable the router from sending IGMP messages containing the Router-Alert option in IP headers.


Example
-------

# In the MLD view, disable the router to send MLD messages containing Router-Alert options in IPv6 headers.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] mld
[*HUAWEI-mld] send-router-alert disable

```