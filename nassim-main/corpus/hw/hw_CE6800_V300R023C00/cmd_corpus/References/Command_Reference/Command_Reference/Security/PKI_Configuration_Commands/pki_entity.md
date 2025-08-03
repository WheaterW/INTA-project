pki entity
==========

pki entity

Function
--------



The **pki entity** command creates a PKI entity and displays the PKI entity view, or displays the view of an existing PKI entity.

The **undo pki entity** command deletes a PKI entity.



By default, no PKI entity is configured.


Format
------

**pki entity** *entity-name*

**undo pki entity** *entity-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **entity** *entity-name* | Specifies the name of a PKI entity. | The value is a string of 1 to 64 case-insensitive characters without question marks (?) or spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A PKI entity refers to the applicant or user of a certificate. A PKI entity is required when you use PKI features. After a PKI entity is created, you can configure attributes for it, for example, common name, country code, email address, FQDN, IP address, geographic area, organization, department, state, and province. These attributes include identity information of the PKI entity. The identity information will be added to the subject of a PKI entity.Windows Server 2003 has a low processing performance. For the device to connect to a Windows Server 2003, the device cannot have too many entities configured or use a large-sized key pair.


Example
-------

# Configure a PKI entity entity1 and enter the PKI entity view.
```
<HUAWEI> system-view
[~HUAWEI] pki entity entity1
[*HUAWEI-pki-entity-entity1]

```