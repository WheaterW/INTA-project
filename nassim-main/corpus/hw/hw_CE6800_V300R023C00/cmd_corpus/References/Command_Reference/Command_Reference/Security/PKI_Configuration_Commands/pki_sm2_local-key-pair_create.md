pki sm2 local-key-pair create
=============================

pki sm2 local-key-pair create

Function
--------



The **pki sm2 local-key-pair create** command creates the specified SM2 key pair.




Format
------

**pki sm2 local-key-pair create** *key-name* [ **exportable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-name* | Specifies the name of the created SM2 key pair. | The value is a string of 1 to 64 case-sensitive characters without question marks (?) or spaces. If the string is enclosed in double quotation marks (""), the string can contain spaces but cannot contain double quotation marks ("). |
| **exportable** | Specifies the created SM2 key pair as exportable. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Run this command when the certificate needs to use the SM2 key pair.


Example
-------

# Create the SM2 key pair named abc.
```
<HUAWEI> system-view
[HUAWEI] pki sm2 local-key-pair create abc
Info: The name of the new key-pair will be: abc
Info: It will take a few seconds or more. Please wait a moment.
Generating key-pairs finished

```