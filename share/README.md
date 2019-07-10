This is the code base extracted from plugin service for newton. It consists of:

- common utilities which is irrelevant of any SBI to openstack, just some wrapper for API interaction with other ONAP components

- "newton_base" which is the translation of MultiCloud NBI to OpenStack Newton NBI.

	Since from ONAP perspective, there are limited API requests to OpenStack, the variation between different OpenStack release could be minimal and even invisible. So the MultiCloud Plugin service for Ocata, Pike might also be able to reuse this newton_base library. With this approach we could minimize the effort to maintain MultiCloud Plugin services for various OpenStack releases

- "starlingx_base" which is starlingx base API

- UT helper which simulates the VIM response whenever the requests are issued towards underly OpenStack Newton.
