pki certificate access-control-policy name
==========================================

pki certificate access-control-policy name

Function
--------



The **pki certificate access-control-policy name** command creates a certificate access policy and enters the certificate access policy view, or displays the view of an existing certificate access policy.

The **undo pki certificate access-control-policy name** command deletes a certificate access policy.



By default, no certificate access policy is created.


Format
------

**pki certificate access-control-policy name** *policy-name*

**undo pki certificate access-control-policy name** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *policy-name* | Specifies the name of a certificate access policy. | The value is a string of 1 to 32 case-insensitive characters, spaces and question marks (?) not supported. The character string can contain spaces if it is enclosed with double quotation marks (""). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The access control policy of certificate attributes is an extra measure for certificate verification. Only the certificates meeting specific requirements can pass the verification, and then users' access rights are controlled elaborately.


Example
-------

# Create the certificate access policy policy1 and display its view.
```
<HUAWEI> system-view
[~HUAWEI] pki certificate access-control-policy name policy1
[*HUAWEI-pki-access-policy1]

```