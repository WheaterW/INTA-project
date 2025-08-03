organization-unit
=================

organization-unit

Function
--------



The **organization-unit** command configures the department name for a PKI entity.

The **undo organization-unit** command restores the default setting.



Specifies the department name for a PKI entity.


Format
------

**organization-unit** *organization-unit-name*

**undo organization-unit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **organization-unit** *organization-unit-name* | Specifies the department name for a PKI entity. | The value is a string of 1 to 31 case-sensitive characters. The characters can be letters, integers, apostrophe ('), equal sign (=), brackets (), plus sign (+), comma (,), minus sign (-), dot (.), slash (/), colon (:), and spaces. |



Views
-----

PKI entity view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The parameters of a PKI entity contain the identity information of the entity. The CA identifies a certificate applicant based on identity information provided by the entity. To facilitate applicant identification, configure a department name for the PKI entity, which is used as an alias of the entity.After the department name is configured for a PKI entity, the certificate request packet sent by the device to the CA server carries this department name. The CA server verifies every received certificate request packet. For each valid packet, the CA server generates a digital certificate carrying the department name of the PKI entity.


Example
-------

# Configure the department name of a PKI entity to Group1, Sale.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1] organization-unit Group1,Sale

```