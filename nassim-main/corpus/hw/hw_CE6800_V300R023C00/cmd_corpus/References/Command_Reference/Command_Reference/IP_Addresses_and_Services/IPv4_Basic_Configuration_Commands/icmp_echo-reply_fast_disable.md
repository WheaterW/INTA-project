icmp echo-reply fast disable
============================

icmp echo-reply fast disable

Function
--------



The **icmp echo-reply fast disable** command disables the fast ICMP reply function on the device.

The **undo icmp echo-reply fast disable** command enables the fast ICMP reply function on the device.



By default, the fast ICMP reply function is enabled on the device.


Format
------

**icmp echo-reply fast disable**

**undo icmp echo-reply fast disable**


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

By default, the fast ICMP reply function is enabled on the device. The device will quickly reply to the received ICMP Echo Request packets whose destination address is the device IP address, improving the forwarding performance. In some maintenance or debugging scenarios, you can run the **icmp echo-reply fast disable** command to disable the fast ICMP reply function.

**Precautions**

* Fast ICMP reply is unavailable to ICMP packets received on the management network port.
* Fast ICMP reply is unavailable to fragmented packets.
* After the attack source tracing function for ICMP packets is enabled on the device, the fast ICMP reply function does not take effect.
* If the fast ICMP reply function is enabled on a device, the traffic suppression function does not take effect for ICMP packets.
* The device supports the fast ICMP reply function only for the common ICMP packets.

Example
-------

# Disable the fast ICMP reply function on the device.
```
<HUAWEI> system-view
[~HUAWEI] icmp echo-reply fast disable

```