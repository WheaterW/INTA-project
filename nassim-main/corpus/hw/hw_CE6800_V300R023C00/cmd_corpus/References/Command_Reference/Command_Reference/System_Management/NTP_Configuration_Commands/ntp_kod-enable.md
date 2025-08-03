ntp kod-enable
==============

ntp kod-enable

Function
--------



The **ntp kod-enable** command enables a device to send kiss codes on appropriate conditions.

The **undo ntp kod-enable** command disables a device from sending kiss codes.



By default, KoD is not enabled.


Format
------

**ntp kod-enable**

**undo ntp kod-enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **ntp kod-enable** command is used on the server. In specific scenarios, the server sends kiss codes RATE and DENY to the client.Scenario where the server sends the DENY code to the client:If the NTP ACL access control level is set to peer, server, synchronization, or query on the server and the source IP address of NTP packets received by the server matches the ACL deny rule or does not match any rule, the server sends the DENY code to the client. After the client receives the DENY code, all NTP sessions with the server should be disconnected and NTP request packets should be stopped.Scenario where the server sends the RATE code to the client:If the NTP ACL access control level is set to limited on the server, the source IP address of the NTP packets received by the server matches the ACL permit rule, and the polling interval for the client to send NTP packets is less than the minimum interval for sending packets set on the server, the server sends the RATE code to the client. After receiving the RATE code, the client should reduce the polling interval for sending NTP request packets to the server. Each time the client receives the RATE code, it reduces the polling interval for sending NTP request packets by 1.You can run the **ntp discard** command to set the minimum inter-packet interval and average inter-packet interval of NTP.



**Precautions**



This command is valid only in version 4.If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP server function. To enable the NTP server function, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.




Example
-------

# Enable KoD for sending kiss codes.
```
<HUAWEI> system-view
[~HUAWEI] ntp kod-enable

```