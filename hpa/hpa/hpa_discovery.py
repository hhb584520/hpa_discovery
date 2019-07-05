import textwrap
import uuid
import logging
from hpa import base


class HPA_Discovery(base.HPA_DiscoveryBase):
    """HPA Discovery implementation.
    """

    def get_cpupining(self, data):
        """Get cpupining capabilities.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        """
        cpupining_capability = {}
        feature_uuid = uuid.uuid4()
        extra_specs = data[1] 

        try:
            if extra_specs.has_key('hw:cpu_policy')\
                    or extra_specs.has_key('hw:cpu_thread_policy'):
                cpupining_capability['hpa-capability-id'] = str(feature_uuid)
                cpupining_capability['hpa-feature'] = 'cpuPinning'
                cpupining_capability['architecture'] = 'generic'
                cpupining_capability['hpa-version'] = 'v1'

                cpupining_capability['hpa-feature-attributes'] = []
                if extra_specs.has_key('hw:cpu_thread_policy'):
                    cpupining_capability['hpa-feature-attributes'].append(
                        {'hpa-attribute-key': 'logicalCpuThreadPinningPolicy',
                         'hpa-attribute-value':
                             '{{\"value\":\"{0}\"}}'.format(
                                 extra_specs['hw:cpu_thread_policy'])
                         })
                if extra_specs.has_key('hw:cpu_policy'):
                    cpupining_capability['hpa-feature-attributes'].append(
                        {'hpa-attribute-key':'logicalCpuPinningPolicy',
                         'hpa-attribute-value':
                             '{{\"value\":\"{0}\"}}'.format(
                                 extra_specs['hw:cpu_policy'])
                         })
        except Exception:
            logging.error(traceback.format_exc())
       
        logging.error(cpupining_capability)

        return cpupining_capability

