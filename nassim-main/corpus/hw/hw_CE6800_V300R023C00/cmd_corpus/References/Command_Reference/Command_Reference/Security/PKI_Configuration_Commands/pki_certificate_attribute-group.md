pki certificate attribute-group
===============================

pki certificate attribute-group

Function
--------



The **pki certificate attribute-group** command creates a certificate attribute group and displays the certificate attribute group view, or displays the view of an existing certificate attribute group.

The **undo pki certificate attribute-group** command deletes a certificate attribute group.



By default, no certificate attribute group is created.


Format
------

**pki certificate attribute-group** *group-name*

**undo pki certificate attribute-group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of the certificate attribute group. | The value is a string of 1 to 32 case-insensitive characters, spaces and question marks (?) not supported. The character string can contain spaces if it is enclosed with double quotation marks (""). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The certificate attribute group contains the attribute rules of the certificate. To use such an attribute rule, create a certificate attribute group first.If multiple attribute rules are configured in a certificate attribute group, the relationship among the rules is AND. That is, the action defined in related certificate access control rule is taken only when the certificate to be verified matches all the rules.


Example
-------

# Create the certificate attribute group group1, and display the certificate attribute group view.
```
<HUAWEI> system-view
[~HUAWEI] pki certificate attribute-group group1
[*HUAWEI-pki-attribute-group1]

```