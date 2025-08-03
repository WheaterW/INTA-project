organization
============

organization

Function
--------



The **organization** command configures a PKI entity's organization name.

The **undo organization** command deletes a PKI entity's organization name.



By default, a PKI entity does not have an organization name.


Format
------

**organization** *organization-name*

**undo organization**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **organization** *organization-name* | Specifies the organization name of the PKI entity. | It is a string of 1 to 32 case-sensitive characters, including letters, numerals, apostrophes ('), equal signs (=), parentheses (), plus signs (+), commas (,), minus signs (-), periods (.), slashes (/), colons (:), and spaces. |



Views
-----

PKI entity view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The parameters of a PKI entity contain the identity information of the entity. The CA identifies a certificate applicant based on identity information provided by the entity. To facilitate applicant identification, configure an organization name for the PKI entity, which is used as an alias of the entity.After the organization name is configured for a PKI entity, the certificate request packet sent by the device to the CA server carries this organization name. The CA server verifies every received certificate request packet. For each valid packet, the CA server generates a digital certificate carrying the organization name of the PKI entity.


Example
-------

# Set the organization name of the PKI entity to org1.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1] organization org1

```