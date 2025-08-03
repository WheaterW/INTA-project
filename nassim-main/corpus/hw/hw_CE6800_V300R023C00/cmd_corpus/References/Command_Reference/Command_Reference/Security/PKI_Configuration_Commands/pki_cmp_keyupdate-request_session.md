pki cmp keyupdate-request session
=================================

pki cmp keyupdate-request session

Function
--------



The **pki cmp keyupdate-request session** command performs a key update request (KUR) to the CMPv2 server based on the CMP session information.




Format
------

**pki cmp keyupdate-request session** *session-name*


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

A device performs a KUR when it has a certificate issued by the CA and requires to update the certificate.After the command is executed, the system checks whether the configurations in the CMP session are sufficient for certificate update application. If no, the system displays an error message. If yes, the system performs a KUR according to the configuration. The updated certificate is saved in a file on the device storage, but not imported to the memory.

**Prerequisites**

A CMP session has been created using the **pki cmp session** command.

**Precautions**



The device does not support the message authentication code mode. If the CMP session mode is set to message authentication code, the system displays an error message.




Example
-------

# Send a KUR to the CMPv2 server.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity_test00
[*HUAWEI-pki-entity-entity_test00] common-name e1
[*HUAWEI-pki-entity-entity_test00] quit
[~HUAWEI] pki rsa local-key-pair create key100
[~HUAWEI] pki import-certificate local filename cert0_local.cer
[~HUAWEI] pki cmp session test00
[*HUAWEI-pki-cmp-session-test00] cmp-request entity entity_test00
[*HUAWEI-pki-cmp-session-test00] cmp-request ca-name "C=cn"
[*HUAWEI-pki-cmp-session-test00] cmp-request server url http://172.16.73.168:8080
[*HUAWEI-pki-cmp-session-test00] cmp-request rsa local-key-pair key100
[*HUAWEI-pki-cmp-session-test00] cmp-request authentication-cert cert0_local.cer
[*HUAWEI-pki-cmp-session-test00] quit
[~HUAWEI] pki cmp keyupdate-request session test00

```