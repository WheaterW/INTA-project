send-router-alert disable
=========================

send-router-alert disable

Function
--------



The **send-router-alert disable** command disables the router from sending IGMP messages containing the Router-Alert option in IP headers.

The **undo send-router-alert disable** command restores the default setting.



By default, IP headers of IGMP messages sent by the router contain the Router-Alert option.


Format
------

**send-router-alert disable**

**undo send-router-alert disable**


Parameters
----------

None

Views
-----

IGMP view,VPN instance IGMP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, IP headers of IGMP messages sent by the router contain the Router-Alert option. If the router communicates with a device that does not support the Router-Alertoption, run the **send-router-alert disable** command to disable the router from sending IGMP messages containing the Router-Alert option in IP headers.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

After the **send-router-alert disable** command is run, the router can communicate with a device that does not support the Router-Alert option.

**Precautions**

The function of this command is the same as the function of the **igmp send-router-alert disable** command used in the interface view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.


Example
-------

# In the IGMP view, disable the router from sending IGMP messages containing the Router-Alert option in IP headers.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] igmp
[*HUAWEI-igmp] send-router-alert disable

```