from __future__ import print_function

import argparse

from stevedore import extension


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--width',
        default=20,
        type=int,
        help='maximum output width for text',
    )
    parsed_args = parser.parse_args()

    flavor = {
        "vcpus": "2",
        "ram": "2048",
        "disk": "2048",
        "swap": "2048",
        "OS-FLV-EXT-DATA:ephemeral": "23"
    }
    extra_specs = {
        "aggregate_instance_extra_specs:storage": "local_image",
        "capabilities:cpu_info:model": "Haswell",
        "hw:cpu_policy": "dedicated",
        "hw:cpu_thread_policy": "prefer"
    }
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
        'cloud_extra_info': {
            "ovsDpdk": {
                "version": "v1",
                "arch": "Intel64",
                "libname": "dataProcessingAccelerationLibrary",
                "libversion": "v12.1",
            }
        },
        'insecure': 'True'
    }

    data = [flavor, extra_specs, viminfo]

    mgr = extension.ExtensionManager(
        namespace='hpa.discovery',
        invoke_on_load=True,
        invoke_args=(parsed_args.width,),
    )

    def get_hpa_capabilities(ext, data):
        return (ext.name, ext.obj.get_hpa_capabilities(data))

    results = mgr.map(get_hpa_capabilities, data)
    for name, value in results:
        print(name)
        print(value)
