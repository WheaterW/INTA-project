igmp timer query
================

igmp timer query

Function
--------



The **igmp timer query** command sets the interval at which an interface sends IGMP general query messages.

The **undo igmp timer query** command restores the default setting.



By default, an interface sends IGMP general query messages at an interval of 60s.


Format
------

**igmp timer query** *interval*

**undo igmp timer query**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which an interface sends IGMP general query messages. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If multiple multicast Routers are connected to a shared network segment where hosts reside, these multicast Routers automatically elect a unique querier that is responsible for maintaining IGMP group memberships. The timeout period of a group membership is calculated by using the formula: Timeout period of a group membership = Interval for sending general IGMP query messages x Robustness variable + Maximum response time. To set an interval at which an interface sends general IGMP query messages, run the igmp **timer query** command.

* When a querier starts, the querier sends general query messages for the number of "robustness variable" times to query the multicast groups that have members on the attached network segment. The sending interval is 1/4 of the interval for sending general query messages. The robustness variable can be set by using the **igmp robust-count** command or the robust-count command.
* The querier periodically sends general query messages to maintain memberships. The shorter the interval is, the more sensitive the querier is and the more bandwidth and Router resources are consumed.

**Precautions**

The function of the igmp **timer query** command is the same as the function of the **timer query** command in the IGMP view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.The default interval at which a querier sends General Query messages is 60 seconds, but the default interval defined in the corresponding protocol is 125 seconds. Currently, some vendor devices use the protocol-defined default interval of 125 seconds. To enable the querier to interwork with such devices, you must change the corresponding configuration to ensure that both ends send General Query messages at the same interval.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Set the interval at which VLANIF 1 sends General Query messages to 50 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp timer query 50

```