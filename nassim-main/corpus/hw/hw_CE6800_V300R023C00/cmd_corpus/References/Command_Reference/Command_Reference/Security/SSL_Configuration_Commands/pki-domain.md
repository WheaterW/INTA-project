pki-domain
==========

pki-domain

Function
--------



The **pki-domain** command binds a PKI realm to an SSL policy.

The **undo pki-domain** command unbinds a PKI realm from an SSL policy.



By default, no PKI realm is bound.


Format
------

**pki-domain** *pki-domain*

**undo pki-domain** *pki-domain*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pki-domain* | Specifies a PKI realm. | The value is a string of 1 to 64 case-sensitive characters without spaces. |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **pki-domain** command to bind a PKI realm to an SSL policy.

**Precautions**

The **pki-domain** command is mutually exclusive with the certificate, trusted-ca, and crl load commands.


Example
-------

# Bind a PKI realm to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] pki realm abc
[~HUAWEI-pki-realm-abc] quit
[~HUAWEI] ssl policy a
[~HUAWEI-ssl-policy-a] pki-domain abc

```

# Bind the PKI realm to which an initial certificate is loaded to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy a
[*HUAWEI-ssl-policy-a] pki-domain default
Warning: A preset certificate is loaded to the specified PKI domain. The current operation has security risks. Continue? [Y/N]:y
[*HUAWEI-ssl-policy-a]

```