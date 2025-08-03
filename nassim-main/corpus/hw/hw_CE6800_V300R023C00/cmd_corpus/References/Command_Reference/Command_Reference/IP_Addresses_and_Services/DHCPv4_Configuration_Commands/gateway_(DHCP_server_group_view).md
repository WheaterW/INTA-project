gateway (DHCP server group view)
================================

gateway (DHCP server group view)

Function
--------



The **gateway** command specifies an egress gateway address of the DHCP server in the DHCP server group view.

The **undo gateway** command restores the default setting.



By default, no egress gateway address is specified.


Format
------

**gateway** *ip-address*

**undo gateway**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of an egress gateway. | Dotted decimal notation. |



Views
-----

DHCP server group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP relay agents. If a DHCP server and its DHCP relay agent are on different network segments, you can run the **gateway** command to specify an egress gateway address for the DHCP relay agent. In this way, the DHCP relay agent can communicate with the DHCP server. Run the **gateway-list** command to configure an egress gateway for the DHCP server.

**Precautions**

* If an egress gateway is not configured for a DHCP relay agent using the **gateway** command, the DHCP relay agent uses the interface address as the gateway address to communicate with the DHCP server.
* When two HUAWEI devices function as the DHCP server and DHCP relay agent respectively, they must use the same egress gateway address.

Example
-------

# Specify the egress gateway address of the server group myServers as 10.10.10.1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp relay server group myServers
[*HUAWEI-dhcp-server-group-myServers] gateway 10.10.10.1

```