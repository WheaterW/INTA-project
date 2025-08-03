server no-response authorization
================================

server no-response authorization

Function
--------



The **server no-response authorization** command enables the device to authorize users in the configured authorization sequence after local authentication is performed if server authentication fails.

The **undo server no-response authorization** command is used to configure server+local authentication. If a user does not respond to server authentication, the device directly requests local authorization.



By default, when the authorization function is configured, the device does not send authorization packets when the server does not respond to a user's authentication request and the user then is authenticated using local authentication.


Format
------

**server no-response authorization**

**undo server no-response authorization**


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

**Usage Scenario**

Generally, if both remote and local authentication are configured on a device and the device does not respond to remote authentication, the device selects local authentication. After a user enters local authentication, the device directly requests local authorization. After this command is run, the device continues to perform authorization in the configured authorization mode.

**Precautions**

RADIUS authentication and authorization are integrated. Therefore, when RADIUS authentication and local authentication are configured, if the remote authentication does not respond, the device still selects local authorization.You can run the **display access-user user-id** command to view the authentication and authorization modes.


Example
-------

# Configure a device not to send authorization packets when the authorization function is configured and a user is authenticated using the local authentication mode after the server does not respond to the user's authentication request.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authentication-scheme authen1
[*HUAWEI-aaa-authen-authen1] authentication-mode hwtacacs local
[*HUAWEI-aaa-authen-authen1] undo server no-response authorization
[*HUAWEI-aaa-authen-authen1] quit
[*HUAWEI-aaa] authorization-scheme author1
[*HUAWEI-aaa-author-author1] authorization-mode hwtacacs local

```