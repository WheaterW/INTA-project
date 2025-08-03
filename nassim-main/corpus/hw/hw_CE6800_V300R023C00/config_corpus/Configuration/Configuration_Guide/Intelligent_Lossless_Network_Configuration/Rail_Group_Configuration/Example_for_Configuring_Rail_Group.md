Example for Configuring Rail Group
==================================

Example for Configuring Rail Group

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512839138__fig17332184817140), there are two spine nodes, two leaf nodes, and eight servers. Each spine node connects to each leaf node through two interfaces. Each leaf node connects to four servers, each through a different interface. Rail Group needs to be configured on these spine and leaf nodes to improve the network throughput.

**Figure 1** Network diagram of the Rail Group function![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001513158674.png)

#### Procedure

1. Configure the Rail Group function on the spine nodes.
   
   
   
   # Add Spine1's interfaces connected to the two leaf nodes to two Rail Group port groups. The configurations on Spine2 are similar to those on Spine1 and are not described here.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Spine1
   [*HUAWEI] commit
   [~Spine1] rail-group spinegroup1
   [*Spine1-rail-group-spinegroup1] group-member interface 100ge 1/0/1 to 100ge 1/0/2
   [*Spine1-rail-group-spinegroup1] quit
   [*Spine1] rail-group spinegroup2
   [*Spine1-rail-group-spinegroup2] group-member interface 100ge 1/0/3 to 100ge 1/0/4
   [*Spine1-rail-group-spinegroup2] quit
   [*Spine1] commit
   ```
   
   # Enable the Rail Group function on Spine1.
   
   ```
   [~Spine1] load-balance ecmp rail-group enable
   [*Spine1] commit
   ```
2. Configure the Rail Group function on the leaf nodes.
   
   
   
   # Add Leaf1's interfaces connected to servers to the same Rail Group port group. The configurations on Leaf2 are similar to those on Leaf1 and are not described here.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Leaf1
   [*HUAWEI] commit
   [~Leaf1] rail-group leafgroup
   [*Leaf1-rail-group-leafgroup] group-member interface 100ge 1/0/1 to 100ge 1/0/4
   [*Leaf1-rail-group-leafgroup] quit
   [*Leaf1] commit
   ```
   
   # Enable the Rail Group function on Leaf1.
   
   ```
   [~Leaf1] load-balance ecmp rail-group enable
   [*Leaf1] commit
   ```

#### Verifying the Configuration

# Check the Rail Group configuration and status on Spine1.

```
[~Spine1] display rail-group status
Global rail-group configuration: Enable
-------------------------------------------------------------
GroupName                        Index       Interface       
-------------------------------------------------------------
spinegroup1                          0       100GE1/0/1      
                                     1       100GE1/0/2      
spinegroup2                          0       100GE1/0/3      
                                     1       100GE1/0/4      
-------------------------------------------------------------
```

# Check the Rail Group configuration and status on Leaf1.

```
[~Leaf1] display rail-group status
Global rail-group configuration: Enable
-------------------------------------------------------------
GroupName                        Index       Interface       
-------------------------------------------------------------
leafgroup                            0       100GE1/0/1      
                                     1       100GE1/0/2      
                                     2       100GE1/0/3      
                                     3       100GE1/0/4      
-------------------------------------------------------------
```

#### Configuration Scripts

Spine1

```
#
sysname Spine1
#
rail-group spinegroup1
 group-member interface 100GE1/0/1
 group-member interface 100GE1/0/2
#
rail-group spinegroup2
 group-member interface 100GE1/0/3
 group-member interface 100GE1/0/4
#
load-balance ecmp rail-group enable
#
return
```

Spine2

```
#
sysname Spine2
#
rail-group spinegroup1
 group-member interface 100GE1/0/1
 group-member interface 100GE1/0/2
#
rail-group spinegroup2
 group-member interface 100GE1/0/3
 group-member interface 100GE1/0/4
#
load-balance ecmp rail-group enable
#
return
```

Leaf1

```
#
sysname Leaf1
#
rail-group leafgroup
 group-member interface 100GE1/0/1
 group-member interface 100GE1/0/2
 group-member interface 100GE1/0/3
 group-member interface 100GE1/0/4
#
load-balance ecmp rail-group enable
#
return
```

Leaf2

```
#
sysname Leaf2
#
rail-group leafgroup
 group-member interface 100GE1/0/1
 group-member interface 100GE1/0/2
 group-member interface 100GE1/0/3
 group-member interface 100GE1/0/4
#
load-balance ecmp rail-group enable
#
return
```