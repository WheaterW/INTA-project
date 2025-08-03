igmp ssm-mapping enable
=======================

igmp ssm-mapping enable

Function
--------



The **igmp ssm-mapping enable** command enables source-specific multicast (SSM) mapping on an interface.

The **undo igmp ssm-mapping enable** command restores the default setting.



By default, SSM mapping is not enabled on an interface.


Format
------

**igmp ssm-mapping enable**

**igmp ssm-mapping enable policy** *policy-name*

**undo igmp ssm-mapping enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **policy** *policy-name* | SSM Mapping Policy Name. | The value is a string of 1 to 31 case-insensitive characters without spaces. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a multicast Router interface runs IGMPv3 but its connected user hosts have to run IGMPv1 or IGMPv2, configure SSM mapping on the multicast Router interface , so the multicast Router interface also provides the SSM service for the hosts that run IGMPv1 or IGMPv2.Enabling the SSM mapping function on an interface is the prerequisite for you to configure SSM mapping related parameters on the interface. If SSM mapping is not enabled, SSM source/group address mapping entries do not take effect on the interface.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Enable SSM mapping on Vlanif1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp ssm-mapping enable

```