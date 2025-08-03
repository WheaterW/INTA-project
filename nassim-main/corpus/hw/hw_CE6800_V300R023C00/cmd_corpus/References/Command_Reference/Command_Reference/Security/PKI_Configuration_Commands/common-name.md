common-name
===========

common-name

Function
--------



The **common-name** command configures a common name for an entity.

The **undo common-name** command cancels the configuration.



By default, a PKI entity does not have a common name.


Format
------

**common-name** *common-name*

**undo common-name**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *common-name* | Specifies the common name of an entity. | The value is a string of 1 to 64 case-sensitive characters, including letters, numerals, apostrophes ('), equal signs (=), parentheses (), plus signs (+), commas (,), minus signs (-), periods (.), slashes (/), colons (:), and spaces. |



Views
-----

PKI entity view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After a PKI entity is created, a common name must be configured to uniquely identify the PKI entity.After the common name is configured for a PKI entity, the certificate request packet sent by the device to the CA server carries this name. The CA server verifies every received certificate request packet. For each valid packet, the CA server generates a digital certificate carrying the common name of the PKI entity.


Example
-------

# Set the common name to test for an entity.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1] common-name test

```