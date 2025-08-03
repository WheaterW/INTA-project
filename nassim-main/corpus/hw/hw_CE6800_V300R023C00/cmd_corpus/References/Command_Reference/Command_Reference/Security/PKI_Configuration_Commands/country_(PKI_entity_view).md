country (PKI entity view)
=========================

country (PKI entity view)

Function
--------



The **country** command configures a country code for an entity.

The **undo country** command deletes the country code of a PKI entity.



By default, no country code is configured for a PKI entity.


Format
------

**country** *country-code*

**undo country**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *country-code* | Specifies the country code of a PKI entity. | The value is a string of 2 case-sensitive characters without spaces.  The value is a standard two-letter code. You can query the country code in ISO 3166. |



Views
-----

PKI entity view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The parameters of a PKI entity contain the identity information of the entity. The CA identifies a certificate applicant based on identity information provided by the entity. To facilitate applicant identification, configure the country code for the PKI entity, which is used as an alias of the entity.After the country code is configured for a PKI entity, the certificate request packet sent by the device to the CA server carries this country code. The CA server verifies every received certificate request packet. For each valid packet, the CA server generates a digital certificate carrying the country code of the PKI entity.


Example
-------

# Configure the country code to CN for a PKI entity.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1] country CN

```