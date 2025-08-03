ntp trusted authentication-keyid
================================

ntp trusted authentication-keyid

Function
--------



The **ntp trusted authentication-keyid** command specifies the authentication key to be trustworthy.

The **undo ntp trusted authentication-keyid** command cancels the current configuration.



By default, no authentication key is specified to be reliable.


Format
------

**ntp trusted authentication-keyid** *key-id*

**undo ntp trusted authentication-keyid** *key-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-id* | Specifies a key ID. | The value is an integer ranging from 1 to 4294967295. |
| **trusted** | Trusted. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When identity authentication is enabled, this command can be used to specify that one or more keys are reliable. The client synchronizes only with the server that provides a reliable key. If the server provides an unreliable key, the client does not synchronize with the server.Description:

* The key must be set to a reliable key for the device that needs to synchronize the clock.
* When the client is synchronized with the authentication server, the authentication key only needs to be set to a reliable key on the client. Do not set this parameter on the server.

**Prerequisites**



The NTP authentication key has been set using the **ntp authentication-keyid** command.



**Precautions**



If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP server function. To enable the NTP server function, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.




Example
-------

# Enable NTP identity authentication, use HMAC-SHA256 encryption, and specify the key as a reliable key.
```
<HUAWEI> system-view
[~HUAWEI] ntp authentication enable
[*HUAWEI] ntp authentication-keyid 37 authentication-mode hmac-sha256 YsHsjx_202206
[*HUAWEI] ntp trusted authentication-keyid 37

```