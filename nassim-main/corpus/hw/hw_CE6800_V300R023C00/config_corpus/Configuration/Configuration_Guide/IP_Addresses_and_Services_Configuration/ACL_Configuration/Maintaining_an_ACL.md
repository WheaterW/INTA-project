Maintaining an ACL
==================

Maintaining an ACL

#### Displaying ACL Information

[Table 1](#EN-US_TASK_0000001176662573__table111673020226) describes the operations for displaying ACL information.

**Table 1** Operations for displaying ACL information
| Operation | Command | Description |
| --- | --- | --- |
| Display the resource usage of each service. | [**display system tcam bank resource**](cmdqueryname=display+system+tcam+bank+resource+slot+chip) [ **slot** *slot-id* [ **chip** *chip-id* ] ] | None |
| Display TCAM resource information of a device. | [**display system tcam resource acl**](cmdqueryname=display+system+tcam+resource+acl+slot) [ **slot** *slot-id* ] | None |

#### Clearing ACL Information

[Table 2](#EN-US_TASK_0000001176662573__table8793745121619) describes the operations for clearing ACL information.

![](public_sys-resources/notice_3.0-en-us.png) 

The cleared statistics cannot be restored. Therefore, exercise caution when performing this operation.


**Table 2** Operations for clearing ACL information
| Operation | Command | Description |
| --- | --- | --- |
| Clear ACL statistics. | [**reset acl counter**](cmdqueryname=reset+acl+counter+name+all) { **name** *acl-name* | *acl-number* | **all** } | After running this command to clear the historical ACL statistics, you can run the **display acl** command to display ACL rules and statistics about the packets matching the ACL rules in the current period. |