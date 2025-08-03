locality
========

locality

Function
--------



The **locality** command configures a locality name for a PKI entity.

The **undo locality** command cancels the configuration.



By default, a PKI entity does not have a locality name.


Format
------

**locality** *locality-name*

**undo locality**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *locality-name* | Specifies the locality name of an entity. | It is a string of 1 to 32 case-sensitive characters, including letters, numerals, apostrophes ('), equal signs (=), parentheses (), plus signs (+), commas (,), minus signs (-), periods (.), slashes (/), colons (:), and spaces. |



Views
-----

PKI entity view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The parameters of a PKI entity contain the identity information of the entity. The CA identifies a certificate applicant based on identity information provided by the entity. To facilitate applicant identification, configure a locality name for the PKI entity, which is used as an alias of the entity. After the locality name is configured for a PKI entity, the certificate request packet sent by the device to the CA server carries this locality name. The CA server verifies every received certificate request packet. For each valid packet, the CA server generates a digital certificate carrying the locality name of the PKI entity.


Example
-------

# Set the locality name to Beijing for a PKI entity.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1] locality Beijing

```