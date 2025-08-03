Delete
======

You can run the **remove** command to delete different types of nodes (container, list, leaf, and leaf-list nodes).

#### Deleting a Container Node

**You can delete a container node by specifying its name.**

For example, to delete all interface configurations, run the following command:

```
[*(ex)ADMIN@HUAWEI]
MDCLI> remove ifm/interfaces
```

#### Deleting a List Node

**You can delete a list node by specifying its name.**

For example, to delete interface vlanif100, run the following command:

```
[*(ex)ADMIN@HUAWEI]
MDCLI> remove ifm/interfaces/interface[name="vlanif100"]
```
#### Deleting a Leaf Node

**You can delete a leaf node by specifying its name and value.**

For example, to delete the admin-status node configuration of interface MEth0/0/0, run the following command:

```
[*(ex)ADMIN@HUAWEI]
MDCLI> remove ifm/interfaces/interface[name="MEth0/0/0"]/admin-status
```

#### Deleting a Leaf-List Node

**You can delete a leaf-list node by specifying its name and value.**

For example, to delete the source security zone **zone3** from security policy **r1**, run the following command:

```
[*(ex)ADMIN@HUAWEI]/sec-policy/vsys[name="default"]/static-policy/rule[name="r1"]
MDCLI> remove source-zone[.="zone3"]
```