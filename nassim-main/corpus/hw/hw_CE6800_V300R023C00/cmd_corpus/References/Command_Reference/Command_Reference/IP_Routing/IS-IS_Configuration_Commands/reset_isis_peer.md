reset isis peer
===============

reset isis peer

Function
--------



The **reset isis peer** command resets the neighbor relationship with a specified IS-IS neighbor.




Format
------

**reset isis peer** *system-id* [ *process-id* | { **vpn-instance** *vpn-instance-name* } ]

**reset isis** *process-id* **peer** *system-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *system-id* | Specifies the system ID of an IS-IS neighbor. | - |
| *process-id* | Specifies the IS-IS process ID of the neighbor with which the neighbor relationship needs to be reset. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the IS-IS process belongs. For the default VPN instance, this parameter is optional. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The reset isis peer command is used when a device needs to re-establish the neighbor relationship with a specified neighbor.If process-id is not specified in the reset isis peer command, all IS-IS processes re-establish neighbor relationships with a specified neighbor.This command is used to re-establish neighbor relationships with a specified neighbor, which may cause route flapping. Therefore, exercise caution when running this command.


Example
-------

# Reset the neighbor relationships with the IS-IS neighbor with system ID 0000.0c11.1111.
```
<HUAWEI> reset isis peer 0000.0c11.1111

```