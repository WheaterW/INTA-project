ip ttl decrement disable
========================

ip ttl decrement disable

Function
--------



The **ip ttl decrement disable** command disables the device from decreasing the packet TTL by 1 when forwarding IP packets.

The **undo ip ttl decrement disable** command enables the device to decrease the packet TTL by 1 when forwarding IP packets.



By default, the device decreases the packet TTL by 1 when forwarding IP packets.


Format
------

**ip ttl decrement disable**

**undo ip ttl decrement disable**


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

After distributed packets are forwarded at Layer 3, the TTL of the packets is decreased by 1. The contents of the packets are changed. To ensure that the contents of the distributed packets are the same as the original packet contents, run the **ip ttl decrement disable** command on the device to make the packet TTL unchanged when the distributed packets are forwarded at Layer 3.


Example
-------

# Disable the device from decreasing the packet TTL by 1 when forwarding packets.
```
<HUAWEI> system-view
[~HUAWEI] ip ttl decrement disable

```