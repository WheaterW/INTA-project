radius-server attribute message-authenticator access-request
============================================================

radius-server attribute message-authenticator access-request

Function
--------

The **radius-server attribute message-authenticator access-request** command carries the Message-Authenticator attribute in RADIUS authentication packets sent by the device.

The **undo radius-server attribute message-authenticator access-request** command cancels the Message-Authenticator attribute from RADIUS authentication packets sent by the device.

By default, RADIUS authentication packets do not carry the Message-Authenticator attribute.



Format
------

**radius-server attribute message-authenticator access-request**

**undo radius-server attribute message-authenticator access-request**



Parameters
----------

None


Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

The Message-Authenticator attribute is used to identify and verify authentication packets to prevent invalid packets.

This command is used when the PAP or CHAP authentication is enabled.When EAP authentication is enabled, RADIUS packets contain the Message-Authenticator attribute by default. You do not need to run this command.

Example
-------

# Configure the Message-Authenticator attribute to RADIUS authentication packets.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template test1
[*HUAWEI-radius-test1] radius-server attribute message-authenticator access-request

```