snmp-agent password min-length
==============================

snmp-agent password min-length

Function
--------



The **snmp-agent password min-length** command configures the minimum SNMP password length.

The **undo snmp-agent password min-length** command restores the default minimum SNMP password length.



By default, the minimum SNMP password length is 8 bytes.


Format
------

**snmp-agent password min-length** *min-length*

**undo snmp-agent password min-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *min-length* | Specifies the minimum SNMP password length. | The value is an integer ranging from 8 to 16. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve system security and prevent password theft, run the **snmp-agent password min-length** command to configure the minimum SNMP password length. After this command is run, the length of a configured SNMP password must be longer than or equal to the minimum SNMP password length.SNMP passwords consist of the authentication and encryption passwords of local and SNMP users as well as communities.

**Prerequisites**

The **snmp-agent password min-length** command takes effect only when password complexity check is enabled. By default, password complexity check is enabled. If it is disabled, do as follows:

* For the authentication and encryption passwords of SNMP users, run the **undo snmp-agent usm-user password complexity-check disable** command to enable password complexity check.
* For communities, run the **undo snmp-agent community complexity-check disable** command to enable password complexity check.

**Precautions**

Configuring the minimum length of an SNMP password does not affect existing SNMP passwords because the device does not check the password length during configuration restoration. However, the device checks the password length during password configuration.


Example
-------

# Set the minimum SNMP password length to 10.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent password min-length 10

```