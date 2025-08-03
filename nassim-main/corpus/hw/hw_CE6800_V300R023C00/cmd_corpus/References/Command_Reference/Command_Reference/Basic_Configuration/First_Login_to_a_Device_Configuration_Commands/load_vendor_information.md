load vendor information
=======================

load vendor information

Function
--------



The **load vendor information** command loads a vendor information customization file to customize vendor information.




Format
------

**load vendor information** *fileName*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *fileName* | Name of the vendor information customization file. | The value is a string of 5 to 64 case-sensitive characters (including the file name extension).  The file name extension must be .zip.  The file name cannot contain the following special characters: ~? \* /\ : ' | < > [ ] ; $ ` ! |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to load a vendor information customization file and customize vendor information as required.


Example
-------

# Load the vendor information customization file.
```
<HUAWEI> load vendor information vendor_info.zip

```