ip address ignore primary-sub enable
====================================

ip address ignore primary-sub enable

Function
--------



The **ip address ignore primary-sub enable** command enables a device to ignore the primary or secondary status of IP addresses.

The **undo ip address ignore primary-sub enable** command restores the default configuration.



By default, a device differentiates primary IP addresses from secondary IP addresses.


Format
------

**ip address ignore primary-sub enable**

**undo ip address ignore primary-sub enable**


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



When the primary IP address of an interface needs to be deleted, the default configuration affects user services of the secondary IP address. To prevent services of users with secondary IP addresses from being affected, you can enable the device to ignore the primary/secondary status of secondary IP addresses before configuring secondary IP addresses on the device. In this manner, any IP address configured on the interface can be deleted.



**Configuration Impact**



After a device is enabled to ignore the primary or secondary status of IP addresses, no secondary IP address can be configured using the **ip address ip-address sub** command.In primary/secondary IP address mode, the device uses the primary IP address of an interface to interact with other devices while processing specific services. When a device is enabled to ignore the primary or secondary status of IP addresses, the device uses the first IP address of an interface to interact with other devices while processing specific services. For example, the device uses the first IP address of an interface to establish a neighbor relationship while processing a routing protocol service (the neighbor relationship can be viewed using the **display this** command on the interface).



**Precautions**

* For IP addresses in primary/secondary mode:
* An interface can be configured with one primary IP address and multiple secondary IP addresses.
* If a secondary IP address exists, the primary IP address cannot be deleted.
* If the primary and secondary IP addresses are configured on an interface of a device, the device cannot be enabled to ignore the primary or secondary status of IP addresses.
* For the mode of ignoring the primary and secondary IP addresses:
* Multiple IP addresses can be configured for an interface.
* Any IP address configured on an interface can be deleted.
* If multiple IP addresses are configured on an interface of a device, the device cannot be restored to the IP address primary/secondary mode.


Example
-------

# Enable the device to ignore the primary or secondary status of IP addresses.
```
<HUAWEI> system-view
[~HUAWEI] ip address ignore primary-sub enable

```