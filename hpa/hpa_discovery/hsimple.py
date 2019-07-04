import textwrap
from hpa_discovery import base


class Simple(base.HFormatterBase):
    """A very basic formatter.
    """

    def hformat(self, data):
        """Format the data and return unicode text.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        """
        for name, value in sorted(data.items()):
            full_text = ': {name} : {value}'.format(
                name=name,
                value=value,
            )
            wrapped_text = textwrap.fill(
                full_text,
                initial_indent='',
                subsequent_indent='    ',
                width=self.max_width,
            )
            yield wrapped_text + '\n'
    
    def tformat(self, data):
        """Format the data and return unicode text.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        """
        for name, value in sorted(data.items()):
            full_text = '------{name} : {value}'.format(
                name=name,
                value=value,
            )
            wrapped_text = textwrap.fill(
                full_text,
                initial_indent='',
                subsequent_indent='    ',
                width=self.max_width,
            )
            yield wrapped_text + '\n'
