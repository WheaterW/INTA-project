fqdn
====

fqdn

Function
--------



The **fqdn** command configures a fully qualified domain name (FQDN) for an entity.

The **undo fqdn** command cancels the configuration.



By default, no FQDN is configured for a PKI entity.


Format
------

**fqdn** *fqdn-name*

**undo fqdn**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **fqdn** *fqdn-name* | Specifies the FQDN of an entity. | The value is a string of 1 to 255 case-sensitive characters, including letters, numerals, apostrophes ('), equal signs (=), parentheses (), plus signs (+), minus signs (-), periods (.), slashes (/), colons (:), at signs (@), underscores (\_), and spaces. |



Views
-----

PKI entity view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The parameters of a PKI entity contain the identity information of the entity. The CA identifies a certificate applicant based on identity information provided by the entity. To facilitate applicant identification, configure an FQDN for the PKI entity, which is used as an alias of the entity.An FQDN is the unique identifier of a PKI entity. It consists of a host name and a domain name, and can be translated into an IP address. A sample of an FQDN is www.example.com.After the FQDN is configured for a PKI entity, the certificate request packet sent by the device to the CA server carries this FQDN. The CA server verifies every received certificate request packet. For each valid packet, the CA server generates a digital certificate carrying the FQDN of the PKI entity.


Example
-------

# Set the FQDN to example.com for an entity.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1] fqdn example.com

```