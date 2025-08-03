arp learning strict (interface view)
====================================

arp learning strict (interface view)

Function
--------



The **arp learning strict force-enable** command is used to enable strict Address Resolution Protocol (ARP) learning in the interface view.

The **arp learning strict force-disable** command is used to disable strict ARP learning in the interface view.

The **arp learning strict trust** command is used to disable strict ARP learning configured in the interface and enable strict ARP learning configured globally.

The **undo arp learning strict** command is used to disable strict ARP learning configured in the interface and enable strict ARP learning configured globally.



By default, strict ARP learning is disabled.


Format
------

**arp learning strict** { **force-disable** | **force-enable** | **trust** }

**undo arp learning strict**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **force-disable** | Specifies force to disable ARP strict learning. | - |
| **force-enable** | Specifies force to enable ARP strict learning. | - |
| **trust** | Specifies ARP strict learning complies with the global configuration. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The attacker sends a large number of stimulate ARP request and reply messages to a device on a network. As a result, the ARP buffer is overflowed and unable to cache normal ARP entries. Enabling strict ARP learning can address such a problem. Strict ARP learning allows a device to receive only ARP reply message in response to the request sent by itself, ensuring the device security.

**Configuration Impact**

When other devices send ARP request messages to a device enabled with strict ARP learning, the device responds to these devices with reply messages, but does not add MAC addresses of these devices immediately into its ARP entry (or refresh its ARP entry). Instead, the device sends an ARP request message to these devices, and adds MAC address of devices responding to the request to the ARP entry (or refresh the ARP entry).

**Precautions**

After the **arp learning strict force-enable** command is run, the specified interface refreshes or adds ARP entries in strict ARP learning mode. If interfaces on a device have a large number of ARP entries, to simplify configurations, you can run the **arp learning strict** command in the global view to enable strict ARP learning globally.The matching of strict ARP learning is based on the most accuracy principle.

* If strict ARP learning is configured globally and in the interface view, strict ARP learning configured in the interface view is adopted.
* If strict ARP learning is not configured in the interface view, strict ARP learning configured globally is adopted.

Example
-------

# Enable strict ARP learning on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/3
[~HUAWEI-100GE1/0/3] undo portswitch
[*HUAWEI-100GE1/0/3] arp learning strict force-enable

```