from __future__ import print_function

import argparse

from stevedore import extension


if __name__ == '__main__':
    flavor = {
        "vcpus": 2,
        "ram": "2048",
        "disk": "2G",
        "swap": False,
        "OS-FLV-EXT-DATA:ephemeral": False
    }

    # Add cloud_extra_info in convert_vim_info
    viminfo = {
        "createTime": "2017-04-01 02:22:27",
        "domain": "Default",
        "name": "TiS_R4",
        "password": "admin",
        "tenant": "admin",
        "type": "openstack",
        "url": "http://128.224.180.14:5000/v3",
        "userName": "admin",
        "vendor": "WindRiver",
        "version": "newton",
        "vimId": "windriver-hudson-dc_RegionOne",
        'cloud_owner': 'windriver-hudson-dc',
        'cloud_region_id': 'RegionOne',
        'cloud_extra_info': '{ \
            "ovsDpdk": { \
                "version": "v1", \
                "arch": "Intel64", \
                "libname": "dataProcessingAccelerationLibrary", \
                "libversion": "v12.1" \
            } \
        }',
        'insecure': 'True'
    }

    extra_specs = [
        # HPA UT1: CPU-Pinning
        {
            "aggregate_instance_extra_specs:storage": "local_image",
            "capabilities:cpu_info:model": "Haswell",
            "hw:cpu_policy": "dedicated",
            "hw:cpu_thread_policy": "prefer"
        },
        # HPA UT2: CPU-Topology
        {
            "aggregate_instance_extra_specs:storage": "local_image",
            "capabilities:cpu_info:model": "Haswell",
            "hw:cpu_sockets": "2",
            "hw:cpu_cores": "4",
            "hw:cpu_threads": "16"
        },
        # HPA UT3: mem_page_size
        {
            "aggregate_instance_extra_specs:storage": "local_image",
            "capabilities:cpu_info:model": "Haswell",
            "hw:mem_page_size": "large"
        },
        # HPA UT4: numa_nodes
        {
            "aggregate_instance_extra_specs:storage": "local_image",
            "capabilities:cpu_info:model": "Haswell",
            "hw:numa_nodes": "2",
            "hw:numa_cpus.0": "0,1",
            "hw:numa_cpus.1": "2,3,4,5",
            "hw:numa_mem.0": "2048",
            "hw:numa_mem.1": "2048"
        },
        # HPA UT5: instruction set
        {
            "aggregate_instance_extra_specs:storage": "local_image",
            "capabilities:cpu_info:model": "Haswell",
            "hw:capabilities:cpu_info:features": "avx,acpi"
        },
        # HPA UT6: pci passthrough
        {
            "aggregate_instance_extra_specs:storage": "local_image",
            "capabilities:cpu_info:model": "Haswell",
            "pci_passthrough:alias": "sriov-vf-intel-8086-15b3:4"
        },
        # HPA UT7: sriov-nic
        {
            "aggregate_instance_extra_specs:sriov_nic": "sriov-nic-intel-8086-15b3-physnet-1:1",
            "capabilities:cpu_info:model": "Haswell"
        }
    ]


    def get_hpa_capabilities(ext, data):
        return (ext.name, ext.obj.get_hpa_capabilities(data))

    for extra_spec in extra_specs:
        data = [flavor, extra_spec, viminfo]

        mgr = extension.ExtensionManager(
            namespace='hpa.discovery',
            invoke_on_load=True,
        )

        results = mgr.map(get_hpa_capabilities, data)
        for name, value in results:
            print(name)
            print(value)
