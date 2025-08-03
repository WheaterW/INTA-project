display oas application-software
================================

display oas application-software

Function
--------



The **display oas application-software** command displays information about installed image software packages.




Format
------

**display oas application-software** [ *software-name* **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *software-name* | Specifies the name of an image software package. | The value is a string of 1 to 127 case-sensitive characters without spaces. |
| **verbose** | Detailed information about the image software package. | - |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

* To view information about all installed image software packages, run the **display oas application-software** command.
* After specifying the software-name parameter in the **display oas application-software** command, you can view detailed information about a single image software package.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all installed image software packages.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] display oas application-software

-------------------------------------------------------------------------------------------------------
Software Name     Software Version   Software Type   Software Architecture     Manufacturer 
-------------------------------------------------------------------------------------------------------

oas1234567890.zip 1.0.0              docker          x86_64             
       DPL 

-------------------------------------------------------------------------------------------------------

```

# Display details about a single image software package.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] display oas application-software oas-test-healthy_ls.zip verbose
--------------------------------------------------------------------------------
Image Name                     : oas-test-healthy_ls
Image Path                     : flash:/oas/images
Image Type                     : docker
Image Architecture             : x86_64
Image version                  : 1.0.0
Image Create Time              : 2020-10-20T14:15:14.712657565Z
Image Released By Manufacturer : DPL
Image Description              : open application system
Image Sha256                   : 7a73b9979fa3696f7c75f1f5718dfd143b1897d2efe77fb
                                 ae1e6dd9ef3402b0c
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display oas application-software** command output
| Item | Description |
| --- | --- |
| Software Name | Name of the image software package. |
| Software Version | Image software package version. |
| Software Type | Type of the image software package. |
| Software Architecture | Architecture of the image software package. |
| Manufacturer | Vendor that releases the image software package. |
| Image Name | Image name. |
| Image Type | Image type. |
| Image Architecture | Image architecture. |
| Image version | Image version. |
| Image Create Time | Time when the image was created. |
| Image Released By Manufacturer | Image vendor. |
| Image Description | Image description. |
| Image Sha256 | SHA256 value of the image. |
| Image Path | Image storage path. |