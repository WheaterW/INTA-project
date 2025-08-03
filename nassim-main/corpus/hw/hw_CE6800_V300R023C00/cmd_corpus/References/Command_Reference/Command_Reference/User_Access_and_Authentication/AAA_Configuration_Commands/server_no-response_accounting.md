server no-response accounting
=============================

server no-response accounting

Function
--------



The **server no-response accounting** command configures a device to continue sending accounting packets when the accounting function is configured and a user is authenticated using the local authentication mode after the server does not respond to the user's authentication request.

The **undo server no-response accounting** command restores the default setting.



By default, when the accounting function is configured, the device does not send accounting packets when the server does not respond to a user's authentication request and the user then is authenticated using local authentication.


Format
------

**server no-response accounting**

**undo server no-response accounting**


Parameters
----------

None

Views
-----

Authentication scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Typically, a server functions as both the remote accounting server and the authentication server. If the authentication server does not respond, the accounting server also does not respond. When accounting and authentication + local authentication are configured on a device, a user is authenticated using the local authentication mode after the server does not respond to the user's authentication request. Because the accounting server also does not respond, after the user is authenticated using the local authentication mode, the device still sends accounting packets. As a result, the user goes offline because of accounting-start failures. To prevent this issue, the device does not send accounting packets by default when a user is authenticated using the local authentication mode after the server does not respond to the user's authentication request.


Example
-------

# Configure a device not to send accounting packets when the accounting function is configured and a user is authenticated using the local authentication mode after the server does not respond to the user's authentication request.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authentication-scheme authen1
[*HUAWEI-aaa-authen-authen1] authentication-mode radius local
[*HUAWEI-aaa-authen-authen1] undo server no-response accounting
[*HUAWEI-aaa-authen-authen1] quit
[*HUAWEI-aaa] accounting-scheme acc1
[*HUAWEI-aaa-accounting-acc1] accounting-mode radius

```