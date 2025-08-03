Mappings Between Commands and YANG
==================================

The MD-CLI commands are generated based on the YANG model supported by a device. The following uses huawei-arp.yang as an example to describe how the MD-CLI commands are generated based on YANG model nodes.

The YANG tree structure of huawei-arp.yang is as follows:

```
module: huawei-arp
+--rw arp  
   +--rw global 
   |  +--rw strict-learn-enable?      boolean 
   |  +--rw l2topo-detect-enable?     boolean 
   |  +--rw rate-trap-interval?       uint32 
   |  +--rw passive-learn-enable?     boolean 
   |  +--rw topo-detect-disable?      boolean 
   |  +--rw con-send-enable?          boolean 
   |  +--rw con-send-maxnum?          uint16 
   |  +--rw gratuitous-drop?          boolean 
   |  +--rw vlanif-expiretime?        uint32 
   |  +--rw host-conflict-period?     uint16 
   |  +--rw host-conflict-threshold?  uint16 
   |  +--rw broadcast-max-num?        uint16 
   +--rw speed-limits 
   |  +--rw speed-limit* [slot-id suppress-type ip-type] 
   |     +--rw slot-id           string                                
   |     +--rw suppress-type     suppress-type                
   |     +--rw ip-type           suppress-ip-type              
   |     +--rw suppress-value    uint32 
   +--rw static-arps         
      +--rw static-arp* [ip-addr ni-name] 
         +--rw ip-addr     ipv4-address-no-zone          
         +--rw ni-name     leafref                      
         +--rw mac-addr    mac-address
         +--rw vlan-id?    uint16 
```

The mappings between MD-CLI commands and the YANG model are as follows:

* The container node in the YANG model is mapped to the MD-CLI node view. The container node name corresponds to the MD-CLI node view name.Take huawei-arp.yang as an example. In the YANG tree structure, the arp and speed-limits nodes are both container nodes.
  ```
  module: huawei-arp
  +--rw arp
     +--rw speed-limits
  ```
  
  On the MD-CLI, the arp and speed-limits nodes are mapped to node views.
  
  ```
  [ADMIN@HUAWEI]
  MDCLI> arp
  
  [ADMIN@HUAWEI]/arp
  MDCLI> speed-limits
  
  [ADMIN@HUAWEI]/arp/speed-limits
  MDCLI> 
  ```
  
  You can specify the names of container nodes of different levels at one time to directly access the view corresponding to the target container node.
  
  ```
  [ADMIN@HUAWEI]
  MDCLI> arp speed-limits
  
  [ADMIN@HUAWEI]/arp/speed-limits
  MDCLI> 
  ```
* The list node in the YANG model is also mapped to the MD-CLI node view. Different from the container node, in the list view, you need to specify all the related key values of the list node in addition to the name of the list node.
  
  Take huawei-arp.yang as an example. In the YANG tree structure, the speed-limit node is a list node, and its key consists of three nodes: slot-id, suppress-type, and ip-type.
  
  ```
  module: huawei-arp
  +--rw arp
     +--rw speed-limits
        +--rw speed-limit* [slot-id suppress-type ip-type]
           +--rw slot-id           string
           +--rw suppress-type     suppress-type
           +--rw ip-type           suppress-ip-type
           +--rw suppress-value    uint32
  ```
  
  On the MD-CLI, the speed-limit node is mapped to the MD-CLI node view. To enter the MD-CLI node view, you need to specify slot-id, suppress-type, and ip-type.
  
  ```
  [ADMIN@HUAWEI]/arp/speed-limits
  MDCLI> speed-limit slot-id 1 suppress-type arp ip-type src-ip
  
  [ADMIN@HUAWEI]/arp/speed-limits/speed-limit[slot-id="1"][suppress-type="arp"][ip-type="src-ip"]
  MDCLI>
  ```
  
  If a list node is nested in a container node, you can specify both the container and list nodes to enter the list node view.
  
  ```
  [ADMIN@HUAWEI]
  MDCLI> arp speed-limit slot-id 1 suppress-type arp ip-type src-ip
  
  [ADMIN@HUAWEI]/arp/speed-limits/speed-limit[slot-id="1"][suppress-type="arp"][ip-type="src-ip"]
  MDCLI>
  ```
* Leaf and leaf-list nodes in the YANG model are mapped to MD-CLI operation objects, with the node names being the names of the operation objects. You can enter an object name and parameter value to modify the configuration and run the **remove** <*object name*> command to delete the configuration.
  
  Take huawei-arp.yang as an example. In the YANG tree structure, strict-learn-enable, l2topo-detect-enable, and rate-trap-interval are all leaf nodes.
  
  ```
  module: huawei-arp
  +--rw arp
     +--rw global
        +--rw strict-learn-enable?      boolean
        +--rw l2topo-detect-enable?     boolean
        +--rw rate-trap-interval?       uint32
  ```
  
  On the MD-CLI, strict-learn-enable, l2topo-detect-enable, and rate-trap-interval are mapped to MD-CLI operation objects. You can run the **remove** <*object name*> command to delete the configuration.
  
  ```
  [*(ex)ADMIN@HUAWEI]/arp/global
  MDCLI> strict-learn-enable false
  
  [*(ex)ADMIN@HUAWEI]/arp/global
  MDCLI> remove rate-trap-interval
  ```
  
  You can enter multiple operation objects and values in one MD-CLI command line.
  
  ```
  [*(ex)ADMIN@HUAWEI]/arp/global
  MDCLI> strict-learn-enable false l2topo-detect-enable true
  ```

As shown in the preceding information, the hierarchy of the YANG tree is expressed through the view hierarchy on the MD-CLI. The following example shows the mapping between YANG nodes and MD-CLI commands.

![](../public_sys-resources/note_3.0-en-us.png) 

On the MD-CLI command list on the right, indentation indicates the nesting relationship between MD-CLI views, text in bold indicates the MD-CLI view names and operation object commands, and text in italics indicates related command parameters (including specific parameter types).

```
MD-CLI commands in the YANG tree structure
module: huawei-arp
+--rw arp  ----------------------------------------------------------> arp
   +--rw global ----------------------------------------------------->     global
   |  +--rw strict-learn-enable?      boolean ----------------------->         strict-learn-enable boolean
   |  +--rw l2topo-detect-enable?     boolean ----------------------->         l2topo-detect-enable boolean
   |  +--rw rate-trap-interval?       uint32 ------------------------>         rate-trap-interval uint32
   |  +--rw passive-learn-enable?     boolean ----------------------->         passive-learn-enable boolean
   |  +--rw topo-detect-disable?      boolean ----------------------->         topo-detect-disable boolean
   |  +--rw con-send-enable?          boolean ----------------------->         con-send-enable boolean
   |  +--rw con-send-maxnum?          uint16 ------------------------>         con-send-maxnum uint16
   |  +--rw gratuitous-drop?          boolean ----------------------->         gratuitous-drop boolean
   |  +--rw vlanif-expiretime?        uint32 ------------------------>         vlanif-expiretime uint32
   |  +--rw host-conflict-period?     uint16 ------------------------>         host-conflict-period uint16
   |  +--rw host-conflict-threshold?  uint16 ------------------------>         host-conflict-threshold uint16
   |  +--rw broadcast-max-num?        uint16 ------------------------>         broadcast-max-num uint16
   +--rw speed-limits ----------------------------------------------->      speed-limits
   |  +--rw speed-limit* [slot-id suppress-type ip-type] ------------>         speed-limit slot-id string suppress-type type ip-type ip-type
   |     +--rw slot-id           string                                
   |     +--rw suppress-type     suppress-type                
   |     +--rw ip-type           suppress-ip-type              
   |     +--rw suppress-value    uint32 ----------------------------->            suppress-value uint32
   +--rw static-arps ------------------------------------------------>      static-arps        
      +--rw static-arp* [ip-addr ni-name] --------------------------->         static-arp ip-addr ipv4-address ni-name string
         +--rw ip-addr     ipv4-address-no-zone          
         +--rw ni-name     leafref                      
         +--rw mac-addr    mac-address  ----------------------------->            mac-addr mac-address
         +--rw vlan-id?    uint16 ----------------------------------->            vlan-id uint16
```

The RPC/action node in the YANG model is a maintenance node, through which you can perform maintenance operations. Similar to the container and list nodes, the RPC/action node has its name mapped to that of the MD-CLI node view.

Take huawei-file-operation.yang as an example. In the YANG tree structure, copy-file is an RPC node.

```
module: huawei-file-operation
+---x copy-file
   +---- input
      +---w src-file-name    leafref
      +---w des-file-name    string
```

On the MD-CLI, the copy-file node is mapped to an MD-CLI node view. You can enter the name of an RPC node to enter the RPC view and then perform maintenance operations, for example, copying files.

```
[ADMIN@HUAWEI]
MDCLI> copy-file

[(x)ADMIN@HUAWEI]/copy-file
MDCLI> src-file-name file-1.txt des-file-name file-2.txt

[(x)ADMIN@HUAWEI]/copy-file
MDCLI> emit
```
#### Common Parameter Value Types

The MD-CLI supports all built-in types defined by the YANG language. Common parameter value types are as follows:

* Integer: uint8, uint16, uint32, uint64, int8, int16, int32, int64
* String
* Boolean
* Enumeration
* IP address type: ipv4-address or ipv6-address
* MAC address
* Bits
  
  If the value type is bits and multiple bits need to be input, you need to add "" to enclose multiple bits, for example, "circuit-id remote-id".
* identityref
* Union

For details about all built-in types defined by the YANG language, see the description of built-in types in RFC 7950.

![](../public_sys-resources/caution_3.0-en-us.png) 

In a YANG tree, if different YANG nodes use the same name due to the introduction of the extended data type (augment), in the MD-CLI command tree, <model name + ":" + node name> is used as the command word corresponding to the node, to avoid conflicts.