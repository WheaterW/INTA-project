Example for Creating VSs
========================

This section provides an example for creating VSs and allocating resources to the VSs.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration example is supported only by the Admin-VS.

On a network, the MMB of a PS processes all services offered by a service provider (SP). If a service failure on the PS causes a PS failure, other services running on the PS cannot be properly forwarded. To prevent this problem, configure different VSs on the PS to independently carry services to improve network security.

As shown in [Figure 1](#EN-US_TASK_0172360324__fig_dc_vrp_vs_cfg_000901), different VSs can be created on a PS. The VSs carry their own services that are mutually isolated. Services can be quickly differentiated by VS, and physical interfaces can be shared between the VSs, saving physical links and reducing networking costs.

**Figure 1** Creating VSs  
![](images/fig_dc_vrp_vs_cfg_000901.png)  


#### Precautions

* A VS starts after it is created.
* The slot resources of a VS can be allocated only by a PS administrator.
* The same slot resources can be allocated to multiple VSs.
* If a physical interface is allocated to a VS, it cannot be allocated to other VSs. If the physical interface needs to be shared among different VSs, multiple sub-interfaces corresponding to the physical interface need to be allocated to different VSs.
* After slot resources are deleted from a VS, the resources are automatically allocated to the Admin-VS. In this case, the services in the VS are stopped, but relevant services in the Admin-VS are started.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VSs and configure PVMBs for each VS so that the VSs can start.
2. Allocate interfaces to VSs to allow the VSs to forward services.

#### Data Preparation

To complete the configuration, you need the following data:

* Names of the VSs to be created: vs1, vs2, and vs3
* Interface number allocated to each VS

#### Procedure

1. Create and start VSs.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] admin
   [~HUAWEI-admin] virtual-system vs1
   [*HUAWEI-admin-vs:vs1] port-mode port
   [*HUAWEI-admin-vs:vs1] description vs1
   [*HUAWEI-admin-vs:vs1] quit
   [~HUAWEI-admin] virtual-system vs2
   [*HUAWEI-admin-vs:vs2] port-mode port
   [*HUAWEI-admin-vs:vs2] description vs2
   [*HUAWEI-admin-vs:vs2] quit
   [~HUAWEI-admin] virtual-system vs3
   [*HUAWEI-admin-vs:vs3] port-mode port
   [*HUAWEI-admin-vs:vs3] description vs3
   [*HUAWEI-admin-vs:vs3] quit
   [*HUAWEI-admin] commit
   ```
2. Allocate resources to the VSs.
   
   
   ```
   [~HUAWEI-admin] virtual-system vs1
   ```
   ```
   [*HUAWEI-admin-vs:vs1] assign interface gigabitethernet 0/3/2
   ```
   ```
   [*HUAWEI-admin-vs:vs1] quit
   ```
   ```
   [~HUAWEI-admin] virtual-system vs2
   ```
   ```
   [*HUAWEI-admin-vs:vs2] assign interface gigabitethernet 0/3/3
   ```
   ```
   [*HUAWEI-admin-vs:vs2] quit
   ```
   ```
   [~HUAWEI-admin] virtual-system vs3
   ```
   ```
   [*HUAWEI-admin-vs:vs3] assign interface gigabitethernet 0/3/4
   ```
   ```
   [*HUAWEI-admin-vs:vs3] quit
   ```
   ```
   [*HUAWEI-admin] commit
   ```
3. Configure different services or features on the VSs.
   
   
   
   For configuration details, see the related feature configurations. For example, to configure a routing protocol on VS1, see "IP Routing" in *NE40E Configuration Guide - IP Routing*.
4. Verify the configuration.
   
   
   
   Run the **display virtual-system** command on the PS. The command output shows that vs1, vs2, and vs3 have been created and started.
   
   ```
   [~HUAWEI-admin] display virtual-system
   ```
   ```
   ---------------------------------------------------------------
   Name                             Status         Description
   ---------------------------------------------------------------
   Admin-VS                         running         admin-vs
   vs1                              running         vs1
   vs2                              running         vs2
   vs3                              running         vs3
   ---------------------------------------------------------------  
   ```
   
   Run the [**display virtual-system**](cmdqueryname=display+virtual-system) [ **name** *vs-name* ] [ **verbose** ] command on the PS. The following example uses vs1 configurations.
   
   ```
   [~HUAWEI-admin] display virtual-system name vs1 verbose
   ```
   ```
   Name         : vs1
   Status       : running
   Description  :
   Create time  : 2017-03-13 21:24:27+09:30 DST
   Port mode    : port
   System MAC   : 00-e0-fc-12-34-56
   Assigned slot(s)
   pvmb         : 
   pvmb         : 
   CPU(s)
   slot       : 4%
   slot       : 4%
   fcard:/VS_huawei: 0%, 16/41943040 (Used Kbytes/Max Kbytes)
   Assigned interface(s)
     GE3/0/0, slot 3
   Assigned resource(s)
   u4route      : 10000(Max)
   m4route      : 1000(Max)
   u6route      : 1000(Max)
   m6route      : 1000(Max)
   vpn-instance : 256(Max)
   cpu          : 5(weight)
   ```
   Run the [**display virtual-system configuration state**](cmdqueryname=display+virtual-system+configuration+state) command on the PS to check whether VS configurations have been saved.
   ```
   [~HUAWEI-admin] display virtual-system configuration state
   ```
   ```
   -----------------------------------------------------------------
   Name                             Saved-configuration             
   -----------------------------------------------------------------
   Admin-VS                         not saved                       
   vs1                              not saved                       
   vs2                              not saved                       
   vs3                              not saved                       
   -----------------------------------------------------------------
   ```

#### Configuration Files

PS configuration files

```
#
admin
 virtual-system vs1
  description vs1
  port-mode port
  resource u4route upper-limit 1048576
  resource m4route upper-limit 2000
  resource u6route upper-limit 1048576 
  resource m6route upper-limit 512 
  resource vpn-instance upper-limit 512
  resource cpu weight 5 
  assign interface GigabitEthernet0/3/2
 virtual-system vs2
  description vs2
  port-mode port
  resource u4route upper-limit 1048576
  resource m4route upper-limit 2000
  resource u6route upper-limit 1048576 
  resource m6route upper-limit 512 
  resource vpn-instance upper-limit 512
  resource cpu weight 5 
  assign interface GigabitEthernet0/3/3
 virtual-system vs3
  description vs3
  port-mode port
  resource u4route upper-limit 1048576
  resource m4route upper-limit 2000
  resource u6route upper-limit 1048576 
  resource m6route upper-limit 512 
  resource vpn-instance upper-limit 512
  resource cpu weight 5 
  assign interface GigabitEthernet0/3/4
#
```