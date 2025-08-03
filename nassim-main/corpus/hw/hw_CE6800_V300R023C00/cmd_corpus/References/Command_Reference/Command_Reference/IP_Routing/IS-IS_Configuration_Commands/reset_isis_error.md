reset isis error
================

reset isis error

Function
--------



The **reset isis error** command clears information about incorrect LSPs and Hello packets.




Format
------

**reset isis error** [ { *process-id* | **vpn-instance** *vpn-instance-name* } ]

**reset isis error interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Clears the incorrect LSPs and Hello packets of an IS-IS process.  By default, information about incorrect LSPs and Hello packets received by all processes is cleared. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Clears the incorrect LSPs and Hello packets of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **interface** *interface-type* | Clears the incorrect LSPs and Hello packets of an interface. | - |
| *interface-number* | Clears the incorrect LSPs and Hello packets of an interface. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When troubleshooting IS-IS network faults, you can run the **reset isis error** command to clear the existing statistics before checking new information about incorrect LSPs and Hello packets.


Example
-------

# Clear information about incorrect LSPs and Hello packets received by IS-IS process 1.
```
<HUAWEI> reset isis error 1

```