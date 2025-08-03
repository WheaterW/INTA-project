gateway-list
============

gateway-list

Function
--------

The **gateway-list** command configures an egress gateway address for a DHCP client.

The **undo gateway-list** command deletes a configured egress gateway address.

By default, no gateway address is configured.



Format
------

**gateway-list** *ip-address* &<1-8>

**undo gateway-list** { *ip-address* | **all** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of an egress gateway. | Dotted decimal notation. |
| **all** | Deletes all gateway addresses. | - |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. If a DHCP server and its client are on different network segments, you can run the **gateway-list** command to specify an egress gateway address. In this way, the DHCP server and client can communicate with each other. Then the DHCP server can assign both an IP address and the specified egress gateway address to the client. You can configure multiple gateways in a global address pool to load balance traffic and improve network reliability.

To configure an egress gateway for a DHCP relay agent, run the gateway (DHCP server group view) command.

**Configuration Impact**

If a gateway address is configured on the DHCP server, a DHCP client will obtain the gateway address from the DHCP server and automatically generates a default route to the gateway address. If you run the **option121** command on the DHCP server to allocate classless static routes to DHCP clients, the DHCP client uses an allocated classless static route and does not automatically generate a default route to the gateway address.

**Precautions**

* The IP addresses specified in the **excluded-ip-address** command cannot be configured as a gateway address.
* After an IP address is configured as a gateway address, the device adds the IP address to the list of IP addresses that cannot be automatically allocated, removing the need to run the **excluded-ip-address** command.
* In the IP address pool view, these gateway addresses cannot be subnet broadcast addresses.
* When configuring an egress gateway address for the global address pool of a DHCP server, ensure that this egress gateway address is the same as that of the DHCP relay agent.


Example
-------

# In the IP address pool view, set the egress gateway address for the DHCP client to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] gateway-list 10.1.1.1

```