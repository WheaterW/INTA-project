cmp-request ca-name
===================

cmp-request ca-name

Function
--------



The **cmp-request ca-name** command sets a CA name for the CMP session.

The **undo cmp-request ca-name** command deletes the CA name of the CMP session.



By default, no CA name is configured for a CMP session.


Format
------

**cmp-request ca-name** *ca-name*

**undo cmp-request ca-name**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ca-name* | Indicates the name of the CA and is the field of subject in the CA certificate. | The value is a string of 1 to 128 characters starting and ending with double quotation marks ("). Items in the string are separated by commas (,). Backslashes (\), spaces, double quotation marks ("), single quotation marks ('), asterisks (\*), colons (:), question marks (?), and slashes (/) are not supported. |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A trusted authority enrolls and issues certificates to entities. Therefore, a trusted CA name must be configured.The field order in the CA name must be the same as that in the actual CA certificate. Otherwise, the server regards the name as incorrect.


Example
-------

# Set the CA name for CMP session test.
```
<HUAWEI> system-view
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request ca-name "C=cn,ST=beijing,L=shangdi,O=BB,OU=BB,CN=BB"

```