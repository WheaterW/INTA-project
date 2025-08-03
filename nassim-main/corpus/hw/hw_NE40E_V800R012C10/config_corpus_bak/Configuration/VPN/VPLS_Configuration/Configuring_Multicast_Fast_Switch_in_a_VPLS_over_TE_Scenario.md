Configuring Multicast Fast Switch in a VPLS over TE Scenario
============================================================

Multicast fast switch can fast switch VSI multicast traffic from a faulty primary TE tunnel to a backup tunnel. Multicast fast switch can be enabled in VPLS over TE scenarios in which the public network tunnels of a VSI are TE tunnels and the VSI forwards multicast traffic.

#### Usage Scenario

Multicast fast switch can fast switch VSI multicast traffic from a faulty primary TE tunnel to a backup tunnel. Multicast fast switch can be enabled in VPLS over TE scenarios in which the public network tunnels of a VSI are TE tunnels and the VSI forwards multicast traffic.

In a VPLS over TE scenario, multicast fast switch can be implemented between a TE tunnel and an FRR bypass tunnel, between a TE tunnel and a hot standby (HSB) tunnel, or between primary and backup TE tunnels.

**Figure 1** Networking for switching between a TE tunnel and an FRR bypass tunnel  
![](images/fig_dc_ne_vpls_cfg_500101.png)  

**Figure 2** Networking for switching between a TE tunnel and an HSB tunnel  
![](images/fig_dc_ne_vpls_cfg_500102.png)  

**Figure 3** Networking for switching between primary and backup TE tunnels  
![](images/fig_dc_ne_vpls_cfg_500103.png)  


#### Pre-configuration Tasks

Before configuring VPLS multicast fast switch, complete the following tasks:

* Connect interfaces and set physical parameters to ensure that the physical interface status is up.
* Configure a primary MPLS TE tunnel.
* Configure BFD for the primary MPLS TE tunnel.
* Configure a backup MPLS TE tunnel.
* Configure basic VPLS functions.
* Create a VSI.
* Configure a tunnel policy for the VSI.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to enter the VSI view.
3. Run the [**vpls-multicast fast-switch enable**](cmdqueryname=vpls-multicast+fast-switch+enable) command to enable multicast fast switch in a VPLS over TE scenario.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verify the configuration.

Run the [**display this**](cmdqueryname=display+this) command to view the running configuration in the current view.

```
[~HUAWEI-vsi-ldpvsi] display this
```
```
#
vsi ldpvsi
 vpls-multicast fast-switch enable
#
```