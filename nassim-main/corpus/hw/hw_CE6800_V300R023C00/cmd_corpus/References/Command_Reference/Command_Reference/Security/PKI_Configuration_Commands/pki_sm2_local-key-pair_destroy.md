pki sm2 local-key-pair destroy
==============================

pki sm2 local-key-pair destroy

Function
--------



The **pki sm2 local-key-pair destroy** command deletes the specified SM2 key pair.




Format
------

**pki sm2 local-key-pair destroy** *key-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-name* | Specifies the name of the SM2 key pair to be deleted. | The value must be the name of an existing key pair. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

It is recommended that you run this command to destroy the specified SM2 key pair if it is leaked, damaged, unused or lost.

**Prerequisites**

An SM2 key pair has been created using the **pki sm2 local-key-pair create** command, or the SM2 key pair has been imported to the device memory using the **pki import sm2-key-pair** command.


Example
-------

# Destroy the SM2 key pair named abc.
```
<HUAWEI> system-view
[~HUAWEI] pki sm2 local-key-pair create abc
Info: The name of the new key-pair will be: abc                                                                                     
Info: It will take a few seconds or more. Please wait a moment.                                                                     
Generating key-pairs finished 
[~HUAWEI] pki sm2 local-key-pair destroy abc
Warning: The name of the key pair to be deleted is abc.                                                                             
Are you sure you want to delete the key pair? [Y/N]:y                                                                               
Info: It will take a few seconds or more to destroy key pairs. Please wait a moment.                                                
Info: Delete SM2 key pair success.

```