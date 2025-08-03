mac-address flapping detection exclude
======================================

mac-address flapping detection exclude

Function
--------



The **mac-address flapping detection exclude** command adds a MAC address to the flapping detection whitelist, so that the MAC address flapping detection will not be performed for the MAC address.

The **undo mac-address flapping detection exclude** command deletes a MAC address from the flapping detection whitelist.



By default, no MAC address is added to the MAC flapping detection whitelist.


Format
------

**mac-address flapping detection exclude** *mac-address* *mac-address-mask*

**undo mac-address flapping detection exclude** *mac-address* *mac-address-mask*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a MAC address. | The value is in the format of H-H-H. H is a 4-digit hexadecimal number, such as 00e0 and fc01. If an H contains less than four hexadecimal digits, the first digits contained in the H are 0s. For example, if an H is e0, it is equal to 00e0. |
| *mac-address-mask* | Specifies a MAC address mask. | The value is an integer ranging from 24 to 48. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, the system performs flapping detection for all MAC addresses. In some scenarios, for example, in a scenario where the flapping of a MAC address is caused by a specific device or operation faults, flapping detection does not need to be implemented for the MAC address, so flapping detection is not needed for this MAC address.To disable the system from implementing flapping detection for a MAC address, run the **mac-address flapping detection exclude** command to add the MAC address to the MAC flapping detection whitelist. After configuration, if flapping occurs on the specific MAC address, no MAC flapping alarm or record is generated for this MAC address.




Example
-------

# Add a MAC address to the MAC flapping detection whitelist.
```
<HUAWEI> system-view
[~HUAWEI] mac-address flapping detection exclude 1-1-1 48

```