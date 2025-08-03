arp anti-attack gratuitous-arp drop(System view)
================================================

arp anti-attack gratuitous-arp drop(System view)

Function
--------



The **arp anti-attack gratuitous-arp drop** command enables gratuitous ARP packet discarding.

The **undo arp anti-attack gratuitous-arp drop** command disables gratuitous ARP packet discarding.



By default, gratuitous ARP packet discarding is disabled.


Format
------

**arp anti-attack gratuitous-arp drop**

**undo arp anti-attack gratuitous-arp drop**


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



When a device is connected to a network for the first time, the device broadcasts gratuitous ARP packets to announce its existence and checks whether its IP address conflicts with any other device IP address in the broadcast domain. Any device can send gratuitous ARP packets and receive gratuitous ARP packets without authentication. As a result, a large number of gratuitous ARP packets can be generated, causing devices to be busy processing these packets. This process overloads the CPU and affects the processing of other services. To resolve this problem, you can enable gratuitous ARP packet discarding. After gratuitous ARP packet discarding is enabled, the device discards all received gratuitous ARP packets to prevent excessive CPU consumption.



**Configuration Impact**



After the **arp anti-attack gratuitous-arp drop** command is run, the device discards all received gratuitous ARP packets. The device is unaware of new access devices.



**Precautions**

Gratuitous ARP packet discarding can be enabled in the system view or in the interface view.

* If the **arp anti-attack gratuitous-arp drop** command is enabled in the system view, the device discards gratuitous ARP packets received from all interfaces.
* If the **arp anti-attack gratuitous-arp drop** command is enabled in the interface view, the device discards gratuitous ARP packets received from a specified interface.Gratuitous ARP request discarding enabled in the system view is independent upon that enabled in the interface view.


Example
-------

# Enable gratuitous ARP packet discarding globally.
```
<HUAWEI> system-view
[~HUAWEI] arp anti-attack gratuitous-arp drop

```