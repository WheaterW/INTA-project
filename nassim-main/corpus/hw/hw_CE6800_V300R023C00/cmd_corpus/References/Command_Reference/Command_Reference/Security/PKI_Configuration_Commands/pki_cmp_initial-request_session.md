pki cmp initial-request session
===============================

pki cmp initial-request session

Function
--------



The **pki cmp initial-request session** command performs an initial request (IR) to the CMPv2 server based on the CMP session information.




Format
------

**pki cmp initial-request session** *session-name*


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

After the command is executed, the system checks whether the configurations in the CMP session are sufficient for certificate application. If no, the system displays an error message. If yes, the system performs an IR according to the configuration. The obtained certificate is saved in a file on the flash, but not imported to the memory. If the server issues the CA certificate during the response period, the CA certificate is also saved in a file.

**Prerequisites**

A CMP session has been created using the **pki cmp session** command.


Example
-------

# Send an IR to the CMPv2 server.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity_ir
[*HUAWEI-pki-entity-entity_ir] common-name e1
[*HUAWEI-pki-entity-entity_ir] quit
[~HUAWEI] pki rsa local-key-pair create keyIR
[~HUAWEI] pki cmp session testir
[*HUAWEI-pki-cmp-session-testir] cmp-request entity entity_ir
[*HUAWEI-pki-cmp-session-testir] cmp-request ca-name "C=cn"
[*HUAWEI-pki-cmp-session-testir] cmp-request server url http://172.16.73.168:8080
[*HUAWEI-pki-cmp-session-testir] cmp-request rsa local-key-pair keyIR
[*HUAWEI-pki-cmp-session-testir] quit
[~HUAWEI] pki cmp initial-request session testir

```