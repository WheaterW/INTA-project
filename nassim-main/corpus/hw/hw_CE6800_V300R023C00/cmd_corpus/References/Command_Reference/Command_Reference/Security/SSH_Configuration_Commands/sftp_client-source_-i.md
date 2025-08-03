sftp client-source -i
=====================

sftp client-source -i

Function
--------



The **sftp client-source -i** command configures the specified interface as the source interface of the device functioning as the SFTP client.



By default, the source IP address of the SFTP client is the IP address of the outbound interface for accessing the SFTP server.


Format
------

**sftp client-source -i** { *interface-type* *interface-number* | *interface-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* *interface-number* | Specifies the interface type and interface number of the local device. | - |
| **-i** *interface-name* | Specifies the interface name of the local device. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you run the **sftp** command to log in to an SFTP server without specifying a source address or source interface, the source address or source interface specified through the sftp client-source command is adopted by default. If you run the **sftp** command and specify the source address or source interface, the specified source address or source interface is adopted. When viewing the current SFTP connection on the server, the specified source IP address or the primary IP address of the specified interface is displayed as the IP address of the user.

**Precautions**

* If the specified source interface has been bound to a VPN instance, the client is automatically bound to the same VPN instance.
* If the specified source interface has been bound to a VPN instance, for example, vpn1, but a different VPN instance, for example, vpn2, is specified in the **sftp client-source -a source-ip-address -vpn-instance vpn-instance-name** command, The vpn configured by this command (vpn2) takes effect.
* After a bound VPN instance is deleted, the VPN configuration specified using the sftp client-source command will not be cleared but does not take effect. In this case, the SFTP server uses a public IP address. If you configure the VPN instance with the same name again, the VPN function restores.
* After a bound source interface is deleted, the interface configuration specified using the sftp client-source command will not be cleared but does not take effect. If you configure the source interface with the same name again, the interface configuration specified using the sftp client-source command is updated and the function restores.

Example
-------

# Set the source interface of the SFTP client to LoopBack0
```
<HUAWEI> system-view
[~HUAWEI] interface LoopBack 0
[*HUAWEI-LoopBack0] quit
[*HUAWEI] sftp client-source -i LoopBack0

```