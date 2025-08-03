Maintaining an ACL6
===================

Maintaining an ACL6

#### Displaying ACL6 Information

[Table 1](#EN-US_TASK_0000001130621652__table141227425571) describes the operations for displaying ACL6 information.

**Table 1** Operations for displaying ACL6 information
| Operation | Command | Description |
| --- | --- | --- |
| Display the resource usage of each service. | [**display system tcam bank resource**](cmdqueryname=display+system+tcam+bank+resource+slot+chip) [ **slot** *slot-id* [ **chip** *chip-id* ] ] | None |
| Display TCAM resource information of a device. | [**display system tcam resource acl**](cmdqueryname=display+system+tcam+resource+acl+slot) [ **slot** *slot-id* ] | None |

#### Clearing ACL6 Information

[Table 2](#EN-US_TASK_0000001130621652__table8793745121619) describes the operations for clearing ACL6 information.

![](public_sys-resources/notice_3.0-en-us.png) 

The cleared statistics cannot be restored. Therefore, exercise caution when performing this operation.


**Table 2** Operations for clearing ACL6 information
| Operation | Command | Description |
| --- | --- | --- |
| Clear ACL6 statistics. | [**reset acl ipv6 counter**](cmdqueryname=reset+acl+ipv6+counter+name+all) { **name** *acl6-name* | *acl6-number* | **all** } | After running this command to clear the historical ACL6 statistics, you can run the **display acl ipv6** command to display ACL6 rules and statistics about the packets matching the ACL6 rules in the current period. |