advertise one-interface-address
===============================

advertise one-interface-address

Function
--------



The **advertise one-interface-address** command enables the type-132 TLV in LSPs to carry the IP address of only one IS-IS interface.

The **undo advertise one-interface-address** command enables the type-132 TLV in LSPs to carry the IP addresses of all IS-IS interfaces.



By default, the type-132 TLV in LSPs carries the IP addresses of all IS-IS interfaces.


Format
------

**advertise one-interface-address**

**undo advertise one-interface-address**


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, on Huawei devices, the type-132 TLV in LSPs carries the IP addresses of all IS-IS interfaces. However, on some non-Huawei devices, the type-132 TLV in LSPs carries the IP address of only one IS-IS interface. To implement interworking between Huawei devices and these non-Huawei devices, run the advertise one-interface-address command on the Huawei devices to enable the type-132 TLV in LSPs to carry the IP address of only one IS-IS interface.After the command is run, the interface IP address carried in the type-132 TLV in LSPs is selected as follows:

* A loopback interface's IP address is preferentially selected.
* If multiple loopback interfaces exist, the highest IP address of these interfaces is preferred. If no loopback interface exists, the highest IP address of other interfaces is selected.

**Precautions**



If a Huawei device fails to interwork with a non-Huawei device before this command is run, the interworking succeeds only after the command is run on the Huawei device and the IS-IS process on the non-Huawei device is restarted to trigger path recalculation.




Example
-------

# Enable the type-132 TLV in LSPs to carry the IP address of only one IS-IS interface.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] advertise one-interface-address

```