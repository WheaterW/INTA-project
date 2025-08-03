dhcp enable
===========

dhcp enable

Function
--------



The **dhcp enable** command enables the DHCP function.

The **undo dhcp enable** command disables the DHCP function.



By default, the DHCP function is disabled.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**dhcp enable** [ **ipv4** | **ipv6** ]

**undo dhcp enable** [ **ipv4** | **ipv6** ]

For CE6885-LL (low latency mode):

**dhcp enable**

**undo dhcp enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Configures the device to process only DHCPv4 messages.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ipv6** | Configures the device to process only DHCPv6 messages.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |

None


Views
-----

System view,System view of the virtual system


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



As the network scale expands and the network complexity increases, the network configuration becomes more and more complex. Computer locations often change and the number of computers often exceeds the number of IP addresses that can be allocated. The DHCP is developed to meet these requirements. After you run the **dhcp enable** command to enable DHCP on a device, the device processes both DHCPv4 and DHCPv6 packets. If only DHCPv4 or DHCPv6 packets need to be processed, run the undo dhcp enable ipv4 or undo dhcp enable ipv6 command to disable DHCPv4 or DHCPv6, this effectively reduces the CPU usage of the device.



Network scale and complexity increase makes network configurations complex. For example, computers frequently change their locations, and IP addresses are insufficient for these computers. The DHCP is developed to address these problems.




Example
-------

# Enable the DHCP function on the device.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable

```

# Disable DHCP on the device.
```
<HUAWEI> system-view
[~HUAWEI] undo dhcp enable
Warning: All DHCP functions will be disabled. Continue? [Y/N]:y

```