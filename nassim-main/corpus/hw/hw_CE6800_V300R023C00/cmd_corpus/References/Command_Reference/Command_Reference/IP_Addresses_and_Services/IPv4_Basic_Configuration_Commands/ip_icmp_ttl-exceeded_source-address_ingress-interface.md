ip icmp ttl-exceeded source-address ingress-interface
=====================================================

ip icmp ttl-exceeded source-address ingress-interface

Function
--------



The **ip icmp ttl-exceeded source-address ingress-interface** command forcibly configures the IP address of the inbound interface for forwarding packets as the source address of an ICMP Time Exceeded message.

The **undo ip icmp ttl-exceeded source-address ingress-interface** command restores the default configuration.



By default, the IP address of the inbound interface for forwarding packets is not forcibly configured as the source address of an ICMP Time Exceeded message.


Format
------

**ip icmp ttl-exceeded source-address ingress-interface**

**undo ip icmp ttl-exceeded source-address ingress-interface**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Tracert is used to test the path through which a packet passes from a host to the destination. After receiving the packet, an intermediate device sends an ICMP Time Exceeded message to the host. The host then identifies the device according to the source IP address of the ICMP Time Exceeded message. To easily observe the inbound interface of a device along the path, you can configure the IP address of the inbound interface for forwarding packets as the source address of an ICMP Time Exceeded message.



**Precautions**



If both the ip icmp ttl-exceeded source-address ingress-interface and **ip icmp ttl-exceeded source-address** commands are configured, the **ip icmp ttl-exceeded source-address** command takes precedence over the **ip icmp ttl-exceeded source-address ingress-interface** command.




Example
-------

# Configure the IP address of the inbound interface for forwarding packets as the source address of an ICMP Time Exceeded message forcibly.
```
<HUAWEI> system-view
[~HUAWEI] ip icmp ttl-exceeded source-address ingress-interface

```