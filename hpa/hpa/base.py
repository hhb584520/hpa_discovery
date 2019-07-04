import abc

import six


@six.add_metaclass(abc.ABCMeta)
class HPA_DiscoveryBase(object):
    """Base class for example plugin used in the tutorial.
    """

    def __init__(self, version="v0"):
        self.version = version

    @abc.abstractmethod
    def get_cpupining(self, data):
        """Get cpupinning capabilities.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        :returns: Iterable producing the formatted text.
        """
