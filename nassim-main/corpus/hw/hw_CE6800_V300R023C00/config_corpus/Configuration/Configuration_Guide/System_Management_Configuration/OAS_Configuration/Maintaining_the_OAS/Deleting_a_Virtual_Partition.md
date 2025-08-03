Deleting a Virtual Partition
============================

Deleting a Virtual Partition

#### Procedure

When the OAS functions are not required, you can delete the created virtual partition to improve resource utilization.

| Operation | Command | Description |
| --- | --- | --- |
| Delete the virtual partition of the image storage. | [**delete virtual-partition**](cmdqueryname=delete+virtual-partition) **type image** | - |
| Delete the running root directory partition. | [**delete virtual-partition**](cmdqueryname=delete+virtual-partition) **type rootfs slot** *slot-id* | - |