state (PKI entity view)
=======================

state (PKI entity view)

Function
--------



The **state** command configures a state or province name for an entity.

The **undo state** command deletes the configuration.



By default, no state or province name is configured for a PKI entity.


Format
------

**state** *state-name*

**undo state**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *state-name* | Specifies the state or province name of an entity. | The value is a string of 1 to 32 case-sensitive characters, including letters, numerals, apostrophes ('), equal signs (=), parentheses (), plus signs (+), commas (,), minus signs (-), periods (.), slashes (/), colons (:), and spaces. |



Views
-----

PKI entity view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The parameters of a PKI entity contain the identity information of the entity. The CA identifies a certificate applicant based on identity information provided by the entity. To facilitate applicant identification, configure a state or province name for a PKI entity.After the state or province name is configured for a PKI entity, the certificate request packet sent by the device to the CA server contains this province name. The CA server verifies every received certificate request packet. For each valid packet, the CA server generates a digital certificate carrying the state or provision name of the PKI entity.


Example
-------

# Configure the province name to Jiangsu for a PKI entity.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1] state Jiangsu

```