server enable (Service-RESTCONF view)
=====================================

server enable (Service-RESTCONF view)

Function
--------



The **server enable** command enables the RESTCONF service function based on HTTP protocol.

The **undo server enable** command disables the RESTCONF service function based on HTTP protocol.

The **secure-server enable** command enables the RESTCONF service function based on HTTPS protocol.

The **undo secure-server enable** command disables the RESTCONF service function based on HTTPS protocol.



By default, the RESTCONF server function is disabled.


Format
------

**server enable**

**secure-server enable**

**undo server enable**

**undo secure-server enable**


Parameters
----------

None

Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

RESTCONF, an HTTP/HTTPS-based protocol, provides RESTful programmatic interfaces and allows users to add, delete, modify, and query network device data.Users can enable the RESTCONF function using this command.

**Prerequisites**

Run the **service restconf** command to enter SERVICE-RESTCONF view.

**Precautions**

* HTTP has security risks. You are advised to enable RESTCONF based on HTTPS.
* For security purposes, you are advised not to run the **server enable** command. If you need to run this command, run the **install feature-software WEAKEA** command to install the weak security algorithm/protocol package WEAKEA first.

Example
-------

# Enable the RESTCONF server function.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] secure-server enable

```