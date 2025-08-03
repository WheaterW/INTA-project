cmp-request entity
==================

cmp-request entity

Function
--------



The **cmp-request entity** command sets the entity name used to apply for certificate through CMPv2.

The **undo cmp-request entity** command deletes the entity name used to apply for certificate through CMPv2.



By default, the entity name used to apply for certificate through CMPv2 is not configured.


Format
------

**cmp-request entity** *entity-name*

**undo cmp-request entity**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *entity-name* | Specifies the entity name for certificate application through CMPv2. | The value must be an existing PKI entity name and cannot contain backslashes (\), spaces, double quotation marks ("), single quotation marks ('), asterisks (\*), colons (:), question marks (?), or slashes (/). |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To apply for a certificate through CMPv2, create a CMP session and specify the entity name in the CMP session.

**Prerequisites**

1.A PKI entity has been created using the **pki entity** command.2.A PKI entity common name has been created using the **common-name** command.

**Precautions**

The specified entity can be referenced only by one CMP session or PKI realm.


Example
-------

# Set the entity name the device uses when applying for a certificate through CMPv2 to entity1.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1] common-name huawei
[*HUAWEI-pki-entity-entity1] quit
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request entity entity1

```