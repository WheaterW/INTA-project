pki cmp certificate-request session
===================================

pki cmp certificate-request session

Function
--------



The **pki cmp certificate-request session** command sends a certificate request (CR) to the CMPv2 server based on the CMP session information.




Format
------

**pki cmp certificate-request session** *session-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **session** *session-name* | Specifies the name of a CMP session. | The value must be an existing CMP session name. A CMP session name starting with a period (.) is not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device has a certificate issued by CA, the device can perform a CR to apply for a certificate for another device.After this command is executed, the system checks whether the configurations in the CMP session are sufficient for certificate application. If no, the system displays an error message. If yes, the system performs the CR according to the configuration. The obtained certificate is saved in a file on the flash, but not imported to the memory.

**Prerequisites**

A CMP session has been created using the **pki cmp session** command.

**Precautions**

The device does not support the message authentication code mode. If the CMP session mode is set to message authentication code, the system displays an error message.


Example
-------

# Send a CR to the CMPv2 server.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity_test11
[*HUAWEI-pki-entity-entity_test11] common-name e1
[*HUAWEI-pki-entity-entity_test11] quit
[~HUAWEI] pki rsa local-key-pair create key111
[~HUAWEI] pki import-certificate local filename cert1_local.cer
[~HUAWEI] pki cmp session test11
[*HUAWEI-pki-cmp-session-test11] cmp-request entity entity_test11
[*HUAWEI-pki-cmp-session-test11] cmp-request ca-name "C=cn"
[*HUAWEI-pki-cmp-session-test11] cmp-request server url http://172.16.73.168:8080
[*HUAWEI-pki-cmp-session-test11] cmp-request rsa local-key-pair key111
[*HUAWEI-pki-cmp-session-test11] cmp-request authentication-cert cert1_local.cer
[*HUAWEI-pki-cmp-session-test11] quit
[~HUAWEI] pki cmp certificate-request session test11

```