Summary of DAA Configuration Tasks
==================================

Summary_of_DAA_Configuration_Tasks

#### DAA Deployment on a New Network

The roadmap
for deploying DAA on a new network is as follows:

1. Build a network environment.
   * Ensure that authorized users can access the network regardless
     of which authentication or accounting mode is used.
   * Plan an AAA domain and a user group and ensure that they can
     distinguish various service types and accommodate users of the corresponding
     service types.
2. Deploy DAA services on a BRAS.
   1. Plan and configure basic items, such as interfaces and routes.
   2. Plan an AAA domain, and configure an authentication mode, an
      accounting mode, a RADIUS server group, and an address pool for the
      AAA domain.
   3. Plan user groups.
   4. Configure DAA.

#### DAA Deployment on an Existing Network

The
DAA networking mode is similar to a general AAA networking mode. The
following points must be noted:

* Check whether the used AAA server type is available for the
  DAA function on a BRAS and whether a device functions as a policy
  server.
* Check whether the configured AAA domain and user group are
  consistent with DAA deployment objectives. If they are inconsistent,
  reconfigure an AAA domain and a user group and ensure that the reconfiguration
  does not affect user services or AAA procedures.
* Do not configure both DAA and behavior aggregate (BA) classification
  because they are mutually exclusive.