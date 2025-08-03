reset isis all
==============

reset isis all

Function
--------



The **reset isis all** command restarts an IS-IS process.




Format
------

**reset isis all** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ]

**reset isis** *process-id* **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the IS-IS process belongs. For the default VPN instance, this parameter is optional. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The reset isis all command is used when LSPs need be immediately refreshed. For example, after the area-authentication-mode and domain-authentication-mode commands are run, you can run the reset isis all command to clear the old LSPs remaining on the device.

**Precautions**

Restarting an IS-IS process may interrupt services. Therefore, exercise caution when running the reset isis all command.


Example
-------

# Clear information about incorrect LSPs and Hello packets received by IS-IS process 1.
```
<HUAWEI> reset isis all 1

```