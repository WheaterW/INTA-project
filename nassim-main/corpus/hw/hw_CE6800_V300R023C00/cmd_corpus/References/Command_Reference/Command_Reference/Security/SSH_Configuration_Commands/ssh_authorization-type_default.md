ssh authorization-type default
==============================

ssh authorization-type default

Function
--------



The **ssh authorization-type default** command sets the authorization method for an SSH connection to AAA or Root.

The **undo ssh authorization-type default** command restores the authorization method.



By default, the authorization method for an SSH connection is AAA.


Format
------

**ssh authorization-type default** { **aaa** | **root** }

**undo ssh authorization-type default**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **aaa** | Sets the authorization method for an SSH connection to AAA. | - |
| **root** | Sets the authorization method for an SSH connection to Root. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



If the authorization type of the SSH connection is set to AAA, the SSH user level is the user level configured in the AAA view.If the authorization type of the SSH connection is Root and public key authentication is used, the SSH user level varies according to the SSH service type.

In SNETCONF, SFTP, or SCP service mode, the user level is directly set to 3.In STelnet service mode, the user level is the level configured in the VTY user interface view.This command takes effect for both IPv4 and IPv6.




Example
-------

# Set the authorization method for SSH connections to AAA.
```
<HUAWEI> system-view
[~HUAWEI] ssh authorization-type default aaa

```