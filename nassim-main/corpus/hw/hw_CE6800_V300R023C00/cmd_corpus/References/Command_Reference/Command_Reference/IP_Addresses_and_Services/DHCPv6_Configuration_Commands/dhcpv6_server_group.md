dhcpv6 server group
===================

dhcpv6 server group

Function
--------



The **dhcpv6 server group** command creates a DHCPv6 server group and enters the DHCPv6 server group view, or enters the view of a DHCPv6 server group that has been created.

The **undo dhcpv6 server group** command deletes a created DHCPv6 server group.



By default, no DHCPv6 server group is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 server group** *group-name*

**undo dhcpv6 server group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a DHCPv6 server group. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported, can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot be "-" or "--". |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **dhcpv6 server group** command is used on DHCPv6 relay agents. Generally, a DHCPv6 relay agent serves multiple DHCPv6 servers. You can run the **dhcpv6 server group** command to create a DHCPv6 server group to manage all the DHCPv6 servers that share the DHCPv6 relay agent. The DHCPv6 server group allocates IPv6 addresses and other network configuration information to users connected to the DHCPv6 relay agent.

**Follow-up Procedure**

* After a DHCPv6 server group is configured, run the **dhcpv6-server** command to add DHCPv6 servers to the DHCPv6 server group.
* When configuring IP address for DHCPv6 servers, run the **dhcpv6 relay server-select** command on an interface to select the DHCPv6 server group of the DHCPv6 relay agent.

**Precautions**

A maximum of 32 DHCPv6 server groups can be configured on the device. A maximum of 20 DHCPv6 servers can be added to a DHCPv6 server group.


Example
-------

# Create a DHCPv6 server group named DHCPv6-srv1.
```
<HUAWEI> system-view
[~HUAWEI] dhcpv6 server group DHCPv6-srv1

```