lldp management-address interface-mode
======================================

lldp management-address interface-mode

Function
--------



The **lldp management-address interface-mode** command configures a management address TLV to use a local interface address. After the lldp management-address command is run, the LLDP management address TLV carries the IP address of the local interface.

The **undo lldp management-address interface-mode** command disables the LLDP management address TLV from using a local interface address.



By default, the management address is not configured to work in interface mode.


Format
------

**lldp management-address interface-mode**

**undo lldp management-address interface-mode**


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



The management address is carried in the Management Address TLV in an LLDP packet. The management address is used by the NMS to identify devices and implement network management. A management address uniquely identifies a device, helping the NMS to determine the network topology and management devices.To enable the management address to be advertised to neighbors to be a local interface address, run the **lldp management-address interface-mode** command.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Precautions**

When the management address works in interface mode, both IPv4 and IPv6 addresses can be used as management addresses. IPv4 and IPv6 addresses are selected separately. If neither of the two addresses is available, the MAC address of the interface is used as the management address.Priority of the management address in management address interface mode:

* IPv4 address: selects the primary address.
* IPv6 address: selects the global or global CGA address. If there are multiple addresses, select the smallest IPv6 address.Note: The IPv6 address must be the IPv6 address of an up interface and cannot be the same as the peer address.


Example
-------

# This command is used to set the interface mode of the LLDP management address.
```
<HUAWEI> system-view
[~HUAWEI] lldp management-address interface-mode

```