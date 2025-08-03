protocol inbound
================

protocol inbound

Function
--------



The **protocol inbound** command specifies the protocols that the current user interface supports.

The **undo protocol inbound** command restores the default protocols supported by the current user interface.



By default, the user interface supports all protocol types, including SSH and Telnet.


Format
------

**protocol inbound** { **all** | **ssh** | **telnet** }

**undo protocol inbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Specifies that the system supports all protocols: SSH, Telnet, and all. | - |
| **ssh** | Specifies that the system supports only SSH protocol. | - |
| **telnet** | Specifies that the system supports only Telnet protocol. | - |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To manage users that log in to the user interface, specify the VTY user interface for users login and run the protocol inbound command to configure protocols supported by the VTY user interface.

**Prerequisites**

If ssh is configured in the protocol inbound command, the authentication-mode (user interface view) command must be used to set the authentication mode to aaa. If the authentication mode is set to password, the protocol inbound ssh command cannot be executed.

**Configuration Impact**

After executing the protocol inbound command, the specified VTY user interface supports users login using Telnet and SSH. The command configuration takes effect next time the user log in to the device.

**Precautions**

When the protocol supported by the VTY user interface is SSH, if the SSH server function is enabled but the RSA/DSA/ECC key is not configured, a temporary key is allocated for logging in to the SSH server.To ensure high security, you are advised to use the secure ECC authentication algorithm.The Telnet protocol has security risks. You are advised to use the SSH protocol.


Example
-------

# Configure vty0 to vty4 support for SSH protocol.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0 4
[~HUAWEI-ui-vty0-4] protocol inbound ssh

```