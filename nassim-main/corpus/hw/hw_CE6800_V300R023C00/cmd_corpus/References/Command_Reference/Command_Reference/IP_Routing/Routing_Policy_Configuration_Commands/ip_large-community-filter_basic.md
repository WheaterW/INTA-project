ip large-community-filter basic
===============================

ip large-community-filter basic

Function
--------



The **ip large-community-filter basic** command sets a basic Large-Community filter.

The **undo ip large-community-filter basic** command deletes a configured basic Large-Community filter.



By default, no basic Large-Community filter is configured.


Format
------

**ip large-community-filter basic** *large-comm-filter-name* [ **index** *index-number* ] *matchMode* { *cmntyStr* } &<1-16>

**undo ip large-community-filter basic** *large-comm-filter-name* [ **index** *index-number* ] [ *matchMode* { *cmntyStr* } &<1-16> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *large-comm-filter-name* | Specifies the name of a basic Large-Community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **index** *index-number* | Specifies the index of a Large-Community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of a Large-Community filter. | The value is an enumerated type:   * permit: Sets the matching mode of a Large-Community filter to permit. * deny: Sets the matching mode of a Large-Community filter to deny. |
| *cmntyStr* | Specifies a value of the Large-Community attribute. | The value is in the format of aa:bb:cc. The values of aa, bb, and cc are integers ranging from 0 to 4294967295. |
| **basic** | Sets a basic Large-Community filter. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The Large-Community attribute is a private attribute of BGP and can be flexibly applied to route-policies. The ip large-community-filter command works with the if-match large-community-filter command so that a filtering rule based on a specific Large-Community filter can be used to filter BGP routes.



**Configuration Impact**



Even after the **route-policy nonexistent-config-check disable** command is run, the system still checks whether the Large-community filter referenced in the command has been created. That is, a nonexistent Large-community filter cannot be referenced in the command.



**Follow-up Procedure**



Run the display ip large-community-filter command to view detailed configuration of the Large-Community filter.



**Precautions**



The relationship between the rules in a Large-Community filter is "AND", which is different from that in an RD filter. This is because each route has only one RD but can have multiple Large-Community values.Large-Community filters in different formats lead to different matching results. Take the following formats as an example:Format 1:ip large-community-filter basic a permit 100:1:1 200:1:1 300:1:1The relationship between 100:1:1, 200:1:1, and 300:1:1 is AND.Format 2:ip large-community-filter basic a permit 100:1:1ip large-community-filter basic a permit 200:1:1 300:1:1The relationship between 200:1:1 and 300:1:1 is AND. The relationship between 100:1:1 and 200:1:1 is OR, and the relationship between 100:1:1 and 300:1:1 is also OR.In format 2, the Large-Community value in each matching rule must be a subset of the Large-Community set in BGP routes.However, the RD filters in the following formats have the same matching result:Format 1:ip rd-filter 100 permit 100:1 200:1 2.2.2.2:1 3.3.3.3:1Format 2:ip rd-filter 100 permit 100:1 200:1ip rd-filter 100 permit 2.2.2.2:1ip rd-filter 100 permit 3.3.3.3:1By default, a Large-Community filter works in deny mode. BGP routes that fail one of the filtering rules do not match the Large-Community filter. If all matching rules in a Large-Community filter work in deny mode, all BGP routes are denied by the filter. To prevent this problem, configure a matching rule in permit mode after one or more matching rules in deny mode so that the routes except for those denied by the preceding filtering rules match the filter.




Example
-------

# Configure a basic Large-Community filter whose name is a.
```
<HUAWEI> system-view
[~HUAWEI] ip large-community-filter basic a deny 1:1:1

```