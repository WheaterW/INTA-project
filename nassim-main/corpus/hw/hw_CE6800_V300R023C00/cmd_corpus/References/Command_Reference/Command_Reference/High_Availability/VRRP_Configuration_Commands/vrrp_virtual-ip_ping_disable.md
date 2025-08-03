vrrp virtual-ip ping disable
============================

vrrp virtual-ip ping disable

Function
--------



The **vrrp virtual-ip ping disable** command disables the master device from responding to ping packets sent to a virtual IP address.

The **undo vrrp virtual-ip ping disable** command enables the master device to respond to ping packets sent to a virtual IP address.



By default, the master device is enabled to respond to ping packets sent to a virtual IP address.


Format
------

**vrrp virtual-ip ping disable**

**undo vrrp virtual-ip ping disable**


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

The device allows user devices to ping a virtual IP address to serve the following purposes:

* Monitors the operating status of the master Router in a VRRP group.
* Monitors communication between a user device and a network connected by a default gateway using the virtual IP address.

**Configuration Impact**

If the ping to the virtual IP address is enabled, a device on an external network can ping a virtual address. This imposes the Router to ICMP-based attacks.

**Precautions**

After the **vrrp virtual-ip ping disable** command is run to disable the master device from responding to ping packets destined for a virtual IP address, the host route corresponding to the virtual IP address is deleted, affecting services that depend on the host route. For example, if the source IP address of a tunnel is a virtual IP address, the tunnel status is Down after the **vrrp virtual-ip ping disable** command is run.


Example
-------

# Disable the master device from responding to ping packets.
```
<HUAWEI> system-view
[~HUAWEI] vrrp virtual-ip ping disable

```