igmp max-response-time
======================

igmp max-response-time

Function
--------



The **igmp max-response-time** command sets the maximum response time of IGMP Query messages on an interface.

The **undo igmp max-response-time** command restores the default setting.



By default, the maximum response time of IGMP Query messages on an interface is 10s.


Format
------

**igmp max-response-time** *interval*

**undo igmp max-response-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the maximum response time of IGMP Query messages. | The value is an integer ranging from 1 to 25, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The maximum response time is used to control the deadline for user hosts to send Report messages. In practice, the response time on a host is a random value from 0 to the maximum response time. The shorter the response time is, the more quickly the IGMP device obtains multicast member information and the more the bandwidth and Router resources are consumed. To set the maximum response time, run the igmp **max-response-time** command.After receiving an IGMP Query message, a user host starts a timer for each group that it joins. The value of the timer ranges from 0 to the maximum response time. When the timer expires, the host sends Report messages.The maximum response time can be used to control the deadline for sending Report messages by the user host. If the maximum response time is properly set, user hosts can rapidly respond to Query messages, and traffic congestion caused by a large number of hosts simultaneously sending response packets is prevented.The function of the igmp **max-response-time** command is the same as the function of the **max-response-time** command in the IGMP view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Set the maximum response time for IGMP Query messages to 8 seconds on vlanif 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp max-response-time 8

```