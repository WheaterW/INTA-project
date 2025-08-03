pki cmp session
===============

pki cmp session

Function
--------



The **pki cmp session** command creates a CMP session and displays the CMP session view, or displays the view of an existing CMP session.

The **undo pki cmp session** command deletes a CMP session.



By default, no CMP session exists.


Format
------

**pki cmp session** *session-name*

**undo pki cmp session** *session-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *session-name* | Specifies the name of a CMP session. | The value is a string of 1 to 64 case-insensitive characters without spaces, double quotation marks ("), single quotation marks ('), asterisks (\*), question marks (?), slashes (/), backslashes (\), or colons (:). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before choosing CMPv2 for certificate application, run the **pki cmp session** command to create a CMP session. CMPv2 configurations are performed in the CMP session view.

**Precautions**

When certificate application is based on the CMP session name, the generated certificate name is the CMP session name plus the corresponding certificate suffix. Therefore, the name of the created CMP session name cannot exceed 50 characters. If the name exceeds 50 characters, the certificate file name will exceed 64 characters and therefore cannot be saved on the storage device.


Example
-------

# Create the CMP session test and display the CMP session view.
```
<HUAWEI> system-view
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test]

```