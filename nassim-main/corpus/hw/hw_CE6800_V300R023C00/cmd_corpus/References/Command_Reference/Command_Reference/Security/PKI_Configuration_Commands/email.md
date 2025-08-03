email
=====

email

Function
--------



The **email** command configures an email address for a PKI entity.

The **undo email** command cancels the configuration.



By default, no email address is configured for a PKI entity.


Format
------

**email** *email-address*

**undo email**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *email-address* | Specifies the email address of a PKI entity. | The value is a string of 1 to 128 case-sensitive characters, including letters, numerals, apostrophes ('), equal signs (=), parentheses (), plus signs (+), minus signs (-), periods (.), slashes (/), colons (:), at signs (@), underscores (\_), and spaces. |



Views
-----

PKI entity view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The parameters of a PKI entity contain the identity information of the entity. The CA identifies a certificate applicant based on identity information provided by the entity. To facilitate applicant identification, configure an email address for the PKI entity, which is used as an alias of the entity.After the email address is configured for a PKI entity, the certificate request packet sent by the device to the CA server carries this email address. The CA server verifies every received certificate request packet. For each valid packet, the CA server generates a digital certificate carrying the email address of the PKI entity.


Example
-------

# Set the email address to test@example.com for an entity.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity_email
[*HUAWEI-pki-entity-entity_email] email test@example.com

```