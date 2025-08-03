dhcp snooping enable(system view)
=================================

dhcp snooping enable(system view)

Function
--------



The **dhcp snooping enable** command enables DHCP snooping.

The **undo dhcp snooping enable** command disables DHCP snooping.



By default, DHCP snooping is disabled on the device.


Format
------

**dhcp snooping enable** [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> ]

**undo dhcp snooping enable** [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id1* | Represents the number of the first VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vlan-id2* | Specifies the ID of the last VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

DHCP snooping is a DHCP security feature. Enabling DHCP snooping on a device can effectively improve DHCP security. After DHCP snooping is enabled using the **dhcp snooping enable** command, the device processes both DHCPv4 and DHCPv6 packets. If only DHCPv4 or DHCPv6 packets need to be processed, run the undo dhcp snooping enable ipv4 or undo dhcp snooping enable ipv6 command to disable DHCPv4 snooping or DHCPv6 snooping. This effectively reduces the CPU usage of the device.You must enable DHCP snooping globally before enabling DHCP snooping on an interface, in a VLAN, or in a BD.

**Prerequisites**

DHCP has been enabled globally using the **dhcp enable** command.

**Follow-up Procedure**

After DHCP snooping is enabled on an interface connected to users, in a VLAN, or in a BD, run the dhcp snooping trusted command to configure the interface connected to the DHCP server as a trusted interface. In this case, the DHCP snooping binding table can be generated.

**Precautions**

In the system view, the **dhcp snooping enable** command is used to enable DHCP snooping.If you run this command in the VLAN view, the command takes effect for the DHCP messages of the specified VLAN on all interfaces. If you run the **dhcp snooping enable** command in the interface view, the command takes effect for all the DHCP messages received on the specified interface. If both DHCP relay and VRRP are configured on a device, DHCP snooping cannot be enabled.


Example
-------

# Enable DHCP snooping globally.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable

```

# Enable DHCP snooping for VLANs 20 to 25 in a batch.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan batch 20 to 25
[*HUAWEI] dhcp snooping enable vlan 20 to 25

```

# Disable DHCP snooping globally.
```
<HUAWEI> system-view
[~HUAWEI] undo dhcp snooping enable
Warning: DHCP snooping will be disabled on the device. Continue? [Y/N]:y

```