(Optional) Configuring RPFR
===========================

(Optional) Configuring RPFR

#### Context

A switch enabled with RDMA Proxy for Fast Recovery (RPFR) can function as an RDMA proxy to implement fast fault recovery. If the native multipathing software of the operating system instead of Huawei's multipathing software is used on compute nodes and RPFR is enabled on the access switch of a storage node, the switch can detect the fault of its link to the storage node and instruct the affected compute nodes to switch to the backup link. In this way, services can be quickly recovered from such a link fault. The following uses the single-layer networking of centralized storage as an example to describe the implementation of RPFR.

**Figure 1** Implementation of RPFR  
![](figure/en-us_image_0000001663780465.png)

1. The storage node sends the access information to DeviceA, and DeviceA records the access interface and connection information.
2. DeviceA detects that its link to the storage node is faulty.
3. DeviceA sends a disconnection request to the compute node.
4. After receiving the disconnection request, the compute node disables the original connection on plane A and switches to the backup link on plane B.

![](public_sys-resources/note_3.0-en-us.png) 

RPFR takes effect only on the following device models: CE6860-SAN, CE8850-SAN, CE6885-SAN.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
   
   By default, the AI service is disabled.
3. Enable iNOF and enter the iNOF view.
   
   
   ```
   [inof](cmdqueryname=inof)
   ```
   
   By default, iNOF is disabled.
4. Enable RPFR.
   
   
   ```
   [rpfr enable](cmdqueryname=rpfr+enable)
   ```
   
   By default, RPFR is disabled.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```