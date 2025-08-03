Configuring Priorities and Root Protection in MSTP Multi-process
================================================================

You can configure priorities and root protection in Multiple Spanning Tree Protocol (MSTP) multi-process to protect links over access rings.

#### Context

To prevent loops over the access ring after the share links fails, configure priorities and root protection in MSTP multi-process.

Root protection is configured on the access interface of a device with second highest priority.

* For detailed configuration of priorities in MSTP multi-process, see [(Optional) Configuring a Priority for a Device in an MSTI](dc_vrp_mstp_cfg_0008.html).
* For detailed configuration of root protection in MSTP multi-process, see [Configuring Root Protection on an Interface](dc_vrp_mstp_cfg_0030.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) The MSTP priority of a downstream device must be lower than that of a UPE.