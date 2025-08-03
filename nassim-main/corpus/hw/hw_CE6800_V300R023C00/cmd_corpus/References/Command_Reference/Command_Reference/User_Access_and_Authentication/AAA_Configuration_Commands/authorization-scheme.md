authorization-scheme
====================

authorization-scheme

Function
--------

The **authorization-scheme** command applies an authorization scheme to a domain.

The **undo authorization-scheme** command unbinds an authorization scheme from a domain.

By default, no authorization scheme is applied to a domain.



Format
------

**authorization-scheme** *authorization-scheme-name*

**undo authorization-scheme**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *authorization-scheme-name* | Specifies the name of an authorization scheme. | The authorization scheme must already exist. |




Views
-----

AAA domain view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

RADIUS integrates authentication and authorization; therefore, RADIUS authorization and authentication must be used together. HWTACACS separates authentication from authorization; therefore, you can configure another authorization type even if HWTACACS authentication, local authentication is used. To authorize users in a domain, run the authorization-scheme (AAA domain view) command.

**Prerequisites**

An authorization scheme has been created and configured with required parameters, for example, the authorization mode and command line authorization.

**Precautions**

* If local authentication is used, the administrator privilege level is the local user privilege level configured using the **local-user privilege level** command.
* If remote authentication is used, the administrator privilege level is in the following descending order of priority:
* User privilege level sent from the server to the device after the authentication is successful
* Administrator privilege level configured using the **admin-user privilege level** command in the service scheme view
* User privilege level configured using the user privilege command in the user interface view
* If both remote authentication and local authentication are configured for a user and remote authentication is performed prior to local authentication, the administrator privilege level is the one used during remote authentication. When local authentication is performed due to the remote authentication server not responding, the administrator privilege level is the local user privilege level configured using the **local-user privilege level** command.


Example
-------

# Apply the authorization scheme author1 to the domain isp1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authorization-scheme author1
[*HUAWEI-aaa-author-author1] quit
[*HUAWEI-aaa] domain isp1
[*HUAWEI-aaa-domain-isp1] authorization-scheme author1

```