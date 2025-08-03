entity
======

entity

Function
--------



The **entity** command specifies a PKI entity that applies for a certificate.

The **undo entity** command cancels a PKI entity.



By default, no PKI entity is specified.


Format
------

**entity** *entity-name*

**undo entity**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *entity-name* | Specifies the name of a PKI entity. | The value must be an existing PKI entity name. |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a PKI entity requests the local certificate in the PKI realm, the device encapsulates the configuration of the specified PKI entity into the certificate request.

**Prerequisites**

1.The specified PKI entity has been configured by using the **pki entity** command.2.The common name of the PKI entity has been configured using the **common-name** command.

**Precautions**

A PKI realm can be bound to only one PKI entity.


Example
-------

# Bind the PKI entity a to the PKI realm abc.
```
<HUAWEI> system-view
[~HUAWEI] pki entity a
[*HUAWEI-pki-entity-a] common-name test
[*HUAWEI-pki-entity-a] quit
[~HUAWEI] pki realm abc
[*HUAWEI-pki-realm-abc] entity a

```