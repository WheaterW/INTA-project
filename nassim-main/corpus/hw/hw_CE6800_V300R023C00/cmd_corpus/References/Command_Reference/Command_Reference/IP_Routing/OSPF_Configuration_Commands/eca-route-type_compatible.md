eca-route-type compatible
=========================

eca-route-type compatible

Function
--------



The **eca-route-type compatible** command sets the route type of the extended community attribute of OSPF VPN to 0x8000.

The **undo eca-route-type compatible** command restores the route type of the extended community attribute of OSPF VPN to 0x0306.



By default, the route type of the extended community attribute of OSPF VPN is 0x0306.


Format
------

**eca-route-type compatible**

**undo eca-route-type compatible**


Parameters
----------

None

Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The eca-route-type compatible command is used in OSPF VPN scenarios.

* For the device supporting standard protocol, you can set the route type of the extended community attribute of OSPF VPN to 0x0306 and configure the device to identify both 0x0306 and 0x8000 route types.
* For the device that does not support standard protocol, you can set the route type of the extended community attribute of OSPF VPN to 0x8000 and configure the device to identify only the 0x8000 route type.By running the eca-route-type compatible command enables devices to communicate with each other and avoid the failure in parsing the route type because the route type of the extended community attribute of OSPF VPN is unrecognized.

**Precautions**

The eca-route-type compatible command cannot be run on the public network.


Example
-------

# Set the route type of the extended community attribute of OSPF VPN to 0x8000.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] ipv4-family
[*HUAWEI-vpn-instance-huawei-af-ipv4] quit
[*HUAWEI-vpn-instance-huawei] quit
[*HUAWEI] ospf 1 vpn-instance huawei
[*HUAWEI-ospf-1] eca-route-type compatible

```