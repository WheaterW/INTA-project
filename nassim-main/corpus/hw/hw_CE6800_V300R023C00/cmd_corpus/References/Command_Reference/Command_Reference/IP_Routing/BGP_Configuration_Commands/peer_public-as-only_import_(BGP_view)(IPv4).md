peer public-as-only import (BGP view)(IPv4)
===========================================

peer public-as-only import (BGP view)(IPv4)

Function
--------



The **peer public-as-only import** command enables a device to remove private AS numbers from the AS\_Path list in received BGP Update messages.

The **undo peer public-as-only import** command allows a device to accept BGP Update messages in which the AS\_Path list carries private AS numbers.



By default, a device does not remove private AS numbers from the AS\_Path list when receiving BGP Update messages.


Format
------

**peer** *peerIpv4Addr* **public-as-only** **import** [ **force** ]

**peer** *peerIpv4Addr* **public-as-only** **import** **disable**

**undo peer** *peerIpv4Addr* **public-as-only** **import** [ **force** ]

**undo peer** *peerIpv4Addr* **public-as-only** **import** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **force** | Deletes all private AS numbers from the AS\_Path attribute. | - |
| **disable** | Disables a device from removing the private AS numbers from the AS\_Path list in received BGP Update messages. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, AS numbers range from 1 to 4294967295, including the public, private, and reserved AS numbers. If the **private-4-byte-as enable** command is not run, private AS numbers range from 64512 to 65534, and the AS number 65535 is reserved for special use. If the **private-4-byte-as enable** command is run, private AS numbers range from 64512 to 65534 and from 4200000000 to 4294967294, and the AS numbers 65535 and 4294967295 are reserved for special use.Public AS numbers can be used over the Internet, whereas private AS numbers cannot be advertised to the Internet. If private AS numbers are advertised to the Internet, routing loops may occur. Therefore, private AS numbers are used only within a routing domain.This command enables BGP to process the private and reserved AS numbers in the AS\_Path attribute of BGP routes as required. Reserved AS numbers are processed the same as private AS numbers. The following uses private AS numbers as an example to illustrate the processing modes:If the **peer public-as-only import** command is run without any optional parameter specified and the AS\_Path attribute of BGP routes contains only private AS numbers, BGP deletes these private AS numbers and then accepts update messages. If the AS\_Path contains both public and private AS numbers, BGP does not delete the private AS numbers. If private AS numbers are deleted in this case, a forwarding error may occur. To forcibly delete private AS numbers from the AS\_Path, configure force.

**Configuration Impact**

If the **peer public-as-only** command is run for a peer group, the peers of the peer group inherit the configuration.

**Precautions**

Analyze the network structure with caution and select proper optional parameters to prevent routing loops or forwarding errors.This command takes effect before an export routing policy is configured.


Example
-------

# Enable a BGP device to remove all the private AS numbers from the AS\_Path list in BGP Update messages received from a specified peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 public-as-only import

```