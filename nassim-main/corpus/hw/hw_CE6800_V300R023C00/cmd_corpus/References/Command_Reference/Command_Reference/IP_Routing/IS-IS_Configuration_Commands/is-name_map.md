is-name map
===========

is-name map

Function
--------



The **is-name map** command enables a local device to identify the hostname carried in each LSP and configures a static hostname for the remote IS-IS system.

The **undo is-name map** command disables a local device from identifying the hostname carried in each LSP and deletes the configured hostname for the remote IS-IS system.



By default, no static hostname is configured locally for the remote IS-IS system.


Format
------

**is-name map** *system-id* *symbolic-name*

**undo is-name map** *system-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *system-id* | Specifies the ID of the remote IS-IS system or pseudonode ID. | - |
| *symbolic-name* | Specifies a static hostname of the remote IS-IS system. | The value is a string of 1 to 64 characters. When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In most cases, to check information about IS-IS neighbors and LSDBs on an IS-IS device, you need to use a system ID of a 12-digit hexadecimal number, for example, aaaa.eeee.1234. This representation, however, is complicated and not easy to use. The dynamic hostname exchange mechanism is introduced to facilitate maintenance and management of IS-IS networks. The **is-name map** command is used to configure a simple hostname for the remote device. The configured hostname is not advertised in an LSP.After the remote device is mapped to a hostname, the system ID of the remote device is replaced with the configured hostname when you run the **display isis name-table** command.

**Prerequisites**

An IS-IS process has been created using the **isis** command in the system view.

**Precautions**

If the local device configures a dynamic hostname and the remote device configures a static hostname for the local device, the dynamic hostname overwrites the static one.


Example
-------

# Configure a static hostname of the remote IS-IS system as 0000.0000.0041.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] is-name map 0000.0000.0041 RUTB

```