ssh server-source
=================

ssh server-source

Function
--------



The **ssh server-source** command specifies a source interface for an SSH server.

The **undo ssh server-source** command cancels the specified source interface for an SSH server.



By default, no source interface is specified for an SSH server.


Format
------

**ssh server-source -i** { *interface-type* *interface-number* | *interface-name* }

**ssh server-source all-interface**

**undo ssh server-source -i** { *interface-type* *interface-number* | *interface-name* }

**undo ssh server-source all-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* *interface-number* | Specifies the source interface type and interface number of an SSH server. | - |
| **all-interface** | Indicates that any interface having an IP address configured can be used as the source interface of an SSH server. | - |
| **-i** *interface-name* | Specifies the source interface name of an SSH server. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve system security, an SSH server does not accept login requests from any interface by default. To allow authorized users to log in to the SSH server, run this command to specify the source interface of the SSH server.

**Prerequisites**

If the source interface of the SSH server is a logical interface, the logical interface must have been created. Otherwise, the command cannot be executed successfully.

**Configuration Impact**

After the source interface of the SSH server is specified, the system allows only SFTP, STelnet, SCP, and SNETCONF users to log in to the server through the specified source interface, and SFTP, STelnet, SCP, and SNETCONF users who log in through other interfaces will be rejected. However, the SFTP, STelnet, SCP, and SNETCONF users who have logged in to the server are not affected.

**Precautions**

* After you specify the source interface of the SSH server, ensure that the SFTP, STelnet, SCP, and SNETCONF users can communicate with the specified source interface at Layer 3 so that authorized SFTP, STelnet, SCP, and SNETCONF users can successfully log in to the SSH server.
* The configuration takes effect upon the next login. The system will prompt you to determine whether to continue the operation.
* If the specified source interface is bound to a VPN instance, the SSH server is bound to the VPN instance.
* After a bound VPN instance is deleted, the VPN configuration specified using the **ssh server-source** command will not be cleared but does not take effect. In this case, the SSH server uses a public IP address. If you configure the VPN instance with the same name again, the VPN function is restored.
* After the bound source interface is deleted, the interface configuration in this command is not deleted, but the function does not take effect. After the source interface with the same name is configured again, the function is restored.
* If both the **ssh server-source -i** and **ssh server-source all-interface** commands are run, the interface specified in the **ssh server-source -i** command is preferentially used as the source interface of the ssh server. If the specified source interface fails to be used for login, the system selects an interface from other valid interfaces for login.


Example
-------

# Configure loopback 0 as the source interface of the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback 0
[~HUAWEI-LoopBack0] ip address 10.1.1.1 24
[*HUAWEI-LoopBack0] quit
[*HUAWEI] ssh server-source -i loopback 0
Warning: SSH server source configuration will take effect in the next login. Continue? [Y/N]:y

```