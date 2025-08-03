lldp management-address
=======================

lldp management-address

Function
--------



The **lldp management-address** command enables LLDP packets to be advertised to neighbors to carry the management IP address of the local device.

The **undo lldp management-address** command disables LLDP packets from carrying the management IP address of the local device.

The **lldp management-address bind interface** command binds the LLDP management IP address to an interface.

The **undo lldp management-address bind** command unbinds the LLDP management IP address from an interface.



By default, the NMS automatically obtains the management IP addresses of managed devices.

The LLDP management address is not bound to any interface by default.




Format
------

**lldp management-address** *ip-address*

**lldp management-address bind interface** { *interface-type* *interface-number* | *interface-name* }

**undo lldp management-address**

**undo lldp management-address bind**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the management IP address to be carried in LLDP packets. | The value is in dotted decimal notation. |
| *interface-type* | Specifies the type of an interface to be bound to the LLDP management address. | - |
| *interface-number* | Specifies the number of an interface to be bound to the LLDP management address. | - |
| *interface-name* | Specifies the name of an interface to be bound to the LLDP management address. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The management IP address is carried in the Management Address TLV in an LLDP packet. The management IP address is used by the NMS to identify devices and implement network management. A management IP address uniquely identifies a device, helping the NMS to determine the network topology and management devices. You can run the **lldp management-address** command to enable LLDP packets to be advertised to neighbors to carry the management IP address of the local device.To specify the IP address of an interface as the LLDP management address, run the **lldp management-address bind interface** command to bind the LLDP management address to the interface.After the LLDP management address is bound to the interface, the device uses the interface's IP address as the management address, if no management address has been configured using the **lldp management-address** command.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.The interface to be bound to the LLDP management address must be a Layer 3 interface. Otherwise, the binding does not take effect.



**Precautions**

If the system fails to find a default IP address, the system uses the bridge MAC address as the LLDP management address.If you run the **lldp management-address** command more than once on the same interface, the latest configuration overrides the previous one.The LLDP management address is selected based on the following rules:If the LLDP management address has been configured using the **lldp management-address** command, the device uses this LLDP management address.

* If no LLDP management address has been configured using the **lldp management-address** command, while the management address is bound to an interface, the devices uses the interface's IP address as the LLDP management address.
* If no LLDP management address has been configured using the **lldp management-address** command, and the management address is not bound to any interface, the device searches the IP address list and automatically uses an IP address as the LLDP management address.
* If no default IP address is available, the device uses the bridge MAC address as the LLDP management address.NOTE: The device searches IP addresses of the following interfaces in sequence for the LLDP management address: Loopback interface, management network interface, and VLANIF interface. The device selects the smallest IP address of the same type of interface as the LLDP management address.


Example
-------

# Bind the LLDP management address to an interface.
```
<HUAWEI> system-view
[~HUAWEI] lldp management-address bind interface 100GE 1/0/1

```