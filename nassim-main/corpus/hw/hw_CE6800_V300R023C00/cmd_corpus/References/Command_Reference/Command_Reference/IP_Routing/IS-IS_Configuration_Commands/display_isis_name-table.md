display isis name-table
=======================

display isis name-table

Function
--------



The **display isis name-table** command displays the mapping between the hostname and the system ID.




Format
------

**display isis name-table** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ]

**display isis** *process-id* **name-table**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays mesh-group information about a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To run the mapping between the hostname and the system ID, run the display isis name-table command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the mapping between the hostname and the system ID.
```
<HUAWEI> display isis name-table 1
Name table information for ISIS(1) Level-1
---------------------------------------------
System ID               Hostname       Type
6789.0000.0001          RUTA           DYNAMIC
0000.0000.0041          RUTB           STATIC

```

**Table 1** Description of the **display isis name-table** command output
| Item | Description |
| --- | --- |
| System ID | Host system ID. |
| Hostname | Host name. |
| Type | Type of the host name:   * DYNAMIC: this host name is local configured using the is-name command. * STATIC: this host name is mapped using the is-name map command. |
| Level | IS-IS level. |