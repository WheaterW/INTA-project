Maintaining MACsec
==================

Before you start collecting MACsec statistics, clear the existing statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) Statistics cannot be restored after
being cleared. Therefore, you must use the following command with
caution.

#### Procedure

1. Run the [**reset macsec statistics**](cmdqueryname=reset+macsec+statistics) **interface** { *interface-name* | *interface-type* *interface-number* } command to clear statistics about data packets protected by MACsec.
2. Run the [**reset mka statistics**](cmdqueryname=reset+mka+statistics) **interface** { *interface-name* | *interface-type* *interface-number* } command to clear MKA session information.